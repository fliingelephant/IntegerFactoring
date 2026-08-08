#!/usr/bin/env python3
"""Bounded search for stable trial-hard F98 one-round peeling counterexamples."""

from __future__ import annotations

import argparse
from collections import Counter, deque
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent
F98_SOURCE = HERE.parent / "F98_multiseed_presentation_closure_kill" / "public_factorization_free_replay.py"
EXPECTED_F98_SHA256 = "5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if sha256(F98_SOURCE) != EXPECTED_F98_SHA256:
    raise AssertionError("the pinned F98 public source hash changed")
SPEC = importlib.util.spec_from_file_location("f104_pinned_f98", F98_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import the pinned F98 public source")
F98 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F98)


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value, flag in enumerate(sieve) if flag]


def is_prime_trial(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def stable_certificate(p: int, q: int) -> dict[str, int | bool]:
    g = math.gcd(p - 1, q - 1)
    A = (p - 1) // g
    B = (q - 1) // g
    final_gcd = math.gcd(A * B, p * q - 1)
    return {"g": g, "A": A, "B": B, "gcd_AB_N_minus_1": final_gcd, "stable": final_gcd == 1}


def row_rank(row_masks: list[int]) -> int:
    pivots: dict[int, int] = {}
    for original in row_masks:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def peel(row_masks: list[int], column_count: int, reverse: bool = False) -> tuple[list[int], list[int], list[int]]:
    active = (1 << column_count) - 1
    degrees = [mask.bit_count() for mask in row_masks]
    column_rows: list[list[int]] = [[] for _ in range(column_count)]
    for row_index, mask in enumerate(row_masks):
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            column_rows[bit.bit_length() - 1].append(row_index)
            remaining ^= bit

    degree_one = [row for row, degree in enumerate(degrees) if degree == 1]
    queue = deque(sorted(degree_one, reverse=reverse))
    removed: list[int] = []
    while queue:
        row = queue.pop() if reverse else queue.popleft()
        if degrees[row] != 1:
            continue
        lone = row_masks[row] & active
        assert lone.bit_count() == 1
        column = lone.bit_length() - 1
        active ^= lone
        removed.append(column)
        for incident_row in column_rows[column]:
            degrees[incident_row] -= 1
            if degrees[incident_row] == 1:
                queue.append(incident_row)

    core_columns: list[int] = []
    remaining = active
    while remaining:
        bit = remaining & -remaining
        core_columns.append(bit.bit_length() - 1)
        remaining ^= bit
    core_rows = [mask & active for mask in row_masks if mask & active]
    return core_columns, core_rows, removed


def p66_matrix(unique_records: list[tuple[int, dict[str, object]]]) -> dict[str, object]:
    initial_entries: list[tuple[int, int]] = []
    relation_values: list[int] = []
    for column, (_, record) in enumerate(unique_records):
        mask = 1 << column
        c = int(record["c"])
        w = int(record["w"])
        value = int(record["P"])
        assert c * w == value
        initial_entries.extend(((c, mask), (w, mask)))
        relation_values.append(value)

    blocks, refinements, gcd_tests = F98.parity_coprime_basis(initial_entries)
    row_masks: list[int] = []
    square_blocks = 0
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            row_masks.append(mask)
    rank, kernel = F98.binary_kernel_basis(row_masks, len(unique_records))
    assert rank == row_rank(row_masks)
    return {
        "row_masks": row_masks,
        "relation_values": relation_values,
        "rank": rank,
        "kernel": kernel,
        "blocks": len(blocks),
        "square_blocks": square_blocks,
        "refinements": refinements,
        "gcd_tests": gcd_tests,
    }


def summarize_matrix(matrix_data: dict[str, object], column_count: int, modulus: int) -> dict[str, object]:
    rows = list(matrix_data["row_masks"])
    core_columns, core_rows, removed = peel(rows, column_count)
    reverse_columns, _, _ = peel(rows, column_count, reverse=True)
    assert core_columns == reverse_columns

    full_rank = int(matrix_data["rank"])
    core_rank = row_rank(core_rows)
    full_nullity = column_count - full_rank
    core_nullity = len(core_columns) - core_rank
    assert full_nullity == core_nullity

    global_plus = 0
    global_minus = 0
    non_global: list[dict[str, int]] = []
    for vector in list(matrix_data["kernel"]):
        product = 1
        support = 0
        remaining = vector
        while remaining:
            bit = remaining & -remaining
            column = bit.bit_length() - 1
            product *= matrix_data["relation_values"][column]
            support += 1
            remaining ^= bit
        root = math.isqrt(product)
        assert root * root == product
        residue = root % modulus
        if residue == 1:
            global_plus += 1
        elif residue == modulus - 1:
            global_minus += 1
        else:
            non_global.append(
                {
                    "support": support,
                    "root_mod_N": residue,
                    "gcd_root_minus_one_N": math.gcd(root - 1, modulus),
                    "gcd_root_plus_one_N": math.gcd(root + 1, modulus),
                }
            )

    return {
        "columns": column_count,
        "rows": len(rows),
        "rank": full_rank,
        "nullity": full_nullity,
        "initial_degree_one_rows": sum(mask.bit_count() == 1 for mask in rows),
        "peeled_columns": len(removed),
        "core_columns": len(core_columns),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": core_nullity,
        "core_nonempty": bool(core_columns),
        "core_rank_deficient": core_nullity > 0,
        "kernel_preserved": True,
        "peel_order_independent_two_orders": True,
        "core_columns_sha256": hashlib.sha256(",".join(map(str, core_columns)).encode()).hexdigest(),
        "row_degree_histogram": dict(sorted(Counter(mask.bit_count() for mask in rows).items())),
        "core_row_degree_histogram": dict(sorted(Counter(mask.bit_count() for mask in core_rows).items())),
        "public_kernel_basis_roots": {
            "basis_size": len(matrix_data["kernel"]),
            "global_plus": global_plus,
            "global_minus": global_minus,
            "non_global_count": len(non_global),
            "first_non_global": non_global[0] if non_global else None,
        },
        "p66": {
            key: matrix_data[key]
            for key in ("blocks", "square_blocks", "refinements", "gcd_tests")
        },
    }


def run_one_round(modulus: int) -> dict[str, object]:
    """Replay the pinned one-round rule. This function receives only N."""
    started = time.monotonic()
    n = modulus.bit_length()
    bound = n * n
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        if 1 < divisor < modulus:
            return {"status": "trial_factor", "factor": divisor, "trial": trial, "n": n, "B": bound}

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()

    def retain(c: int, provenance: dict[str, object]) -> dict[str, object] | None:
        if c in seen_residues:
            return None
        seen_residues.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "status": "direct_factor",
                    "factor": divisor,
                    "sign": sign,
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        records.append({"c": c, "w": w, "P": c * w, "provenance": provenance})
        endpoints.extend((c, w))
        return None

    for seed in range(2, n + 1):
        direct = retain(seed, {"kind": "initial_seed", "seed": seed})
        if direct is not None:
            return {"status": "initial_direct_factor", "n": n, "B": bound, "direct": direct}

    initial_basis, initial_basis_stats = F98.gcd_free_basis(endpoints)
    initial_columns = F98.relation_columns(initial_basis, len(records))
    initial_decoder = F98.decode_relations(modulus, records)
    if initial_decoder["status"] == "factor":
        return {
            "status": "initial_decoder_factor",
            "n": n,
            "B": bound,
            "initial_decoder": initial_decoder,
        }

    active: list[tuple[int, tuple[int, int]]] = []
    for relation_index, column in enumerate(initial_columns):
        if not any(exponent & 1 for exponent in column.values()):
            continue
        support = sorted(initial_basis[index][0] for index in column)
        pair = (support[0], 1) if len(support) == 1 else tuple(support[:2])
        active.append((relation_index, pair))
        if len(active) == n:
            break

    new_relations = 0
    for relation_index, (u, v) in active:
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                before = len(records)
                direct = retain(
                    c,
                    {
                        "kind": "feedback_trajectory",
                        "round": 1,
                        "active_relation_index_zero_based": relation_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                new_relations += len(records) - before
                if direct is not None:
                    return {
                        "status": "trajectory_direct_factor",
                        "n": n,
                        "B": bound,
                        "active_pair_count": len(active),
                        "retained_before_factor": len(records),
                        "direct": direct,
                        "elapsed_seconds": time.monotonic() - started,
                    }

    unique_records: list[tuple[int, dict[str, object]]] = []
    seen_values: set[int] = set()
    zero_values = 0
    duplicate_values = 0
    for raw_index, record in enumerate(records):
        value = int(record["P"])
        if value == 1:
            zero_values += 1
            continue
        if value in seen_values:
            duplicate_values += 1
            continue
        seen_values.add(value)
        unique_records.append((raw_index, record))

    matrix_data = p66_matrix(unique_records)
    matrix_summary = summarize_matrix(matrix_data, len(unique_records), modulus)
    provenance_kinds = Counter(str(record["provenance"]["kind"]) for _, record in unique_records)
    return {
        "status": "round_complete",
        "N": modulus,
        "n": n,
        "B": bound,
        "initial_seed_count": n - 1,
        "initial_basis_size": len(initial_basis),
        "initial_basis_stats": initial_basis_stats,
        "initial_decoder": {
            key: initial_decoder[key]
            for key in (
                "status",
                "unique_relation_count",
                "nonsquare_row_count",
                "squareclass_rank",
                "kernel_dimension",
                "global_plus_basis_roots_before_factor",
                "global_minus_basis_roots_before_factor",
            )
        },
        "active_pair_count": len(active),
        "active_pairs": [
            {"relation_index_zero_based": index, "u": pair[0], "v": pair[1]}
            for index, pair in active
        ],
        "new_feedback_relations": new_relations,
        "retained_relation_count": len(records),
        "zero_relation_value_count": zero_values,
        "duplicate_relation_value_count": duplicate_values,
        "unique_relation_count": len(unique_records),
        "unique_provenance_kinds": dict(sorted(provenance_kinds.items())),
        "matrix": matrix_summary,
        "elapsed_seconds": time.monotonic() - started,
    }


def write_output(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def scan(args: argparse.Namespace) -> dict[str, object]:
    started = time.monotonic()
    primes = [p for p in primes_through(args.prime_max) if args.prime_min <= p <= args.prime_max and p > 3]
    pairs_tested = 0
    stable_tested = 0
    completed = 0
    trace: list[dict[str, object]] = []
    counterexample = None

    payload: dict[str, object] = {
        "status": "running",
        "role": "factor-assisted bounded discovery with an N-only pinned F98 replay",
        "f98_source_sha256": sha256(F98_SOURCE),
        "scan_bounds": {
            "prime_min": args.prime_min,
            "prime_max": args.prime_max,
            "pair_cap": args.pair_cap,
            "pairs_per_p": args.pairs_per_p,
            "enumeration": "p ascending; q from the descending opposite tail, then descending offsets",
        },
    }

    for p_index, p in enumerate(primes):
        q_indices = [len(primes) - 1 - p_index - offset for offset in range(args.pairs_per_p)]
        for q_index in q_indices:
            if q_index <= p_index or pairs_tested >= args.pair_cap:
                continue
            q = primes[q_index]
            N = p * q
            n = N.bit_length()
            bound = n * n
            if p <= bound:
                continue
            pairs_tested += 1
            certificate = stable_certificate(p, q)
            if not certificate["stable"]:
                continue
            stable_tested += 1
            result = run_one_round(N)
            entry = {
                "pair_ordinal": pairs_tested,
                "stable_ordinal": stable_tested,
                "p": p,
                "q": q,
                "N": N,
                "n": n,
                "B": bound,
                "trial_hard": p > bound and q > bound,
                "stable_certificate": certificate,
                "result": result,
            }
            trace.append(entry)
            if result["status"] == "round_complete":
                completed += 1
                if not result["matrix"]["core_rank_deficient"]:
                    replay = run_one_round(N)
                    assert replay["status"] == "round_complete"
                    assert replay["matrix"] == result["matrix"]
                    entry["deterministic_second_replay_match"] = True
                    counterexample = entry
                    break

            payload.update(
                {
                    "pairs_tested": pairs_tested,
                    "stable_pairs_tested": stable_tested,
                    "completed_rounds": completed,
                    "trace": trace,
                    "counterexample": counterexample,
                    "elapsed_seconds": time.monotonic() - started,
                }
            )
            write_output(args.output, payload)
            print(
                f"stable={stable_tested} N={N} status={result['status']} completed={completed}",
                file=sys.stderr,
                flush=True,
            )
        if counterexample is not None or pairs_tested >= args.pair_cap:
            break

    payload.update(
        {
            "status": "counterexample" if counterexample is not None else "cap_complete",
            "pairs_tested": pairs_tested,
            "stable_pairs_tested": stable_tested,
            "completed_rounds": completed,
            "trace": trace,
            "counterexample": counterexample,
            "elapsed_seconds": time.monotonic() - started,
        }
    )
    write_output(args.output, payload)
    return payload


def verify(args: argparse.Namespace) -> dict[str, object]:
    assert args.verify_p is not None and args.verify_q is not None
    p = args.verify_p
    q = args.verify_q
    assert p != q and p % 2 == q % 2 == 1
    assert is_prime_trial(p) and is_prime_trial(q)
    assert args.verify_modulus == p * q
    N = args.verify_modulus
    n = N.bit_length()
    bound = n * n
    assert p > bound and q > bound
    certificate = stable_certificate(p, q)
    assert certificate["stable"]
    first = run_one_round(N)
    second = run_one_round(N)
    assert first == second or (
        {key: value for key, value in first.items() if key != "elapsed_seconds"}
        == {key: value for key, value in second.items() if key != "elapsed_seconds"}
    )
    assert first["status"] == "round_complete"
    assert not first["matrix"]["core_rank_deficient"]
    payload = {
        "status": "PASS",
        "role": "pinned counterexample verification",
        "f98_source_sha256": sha256(F98_SOURCE),
        "p": p,
        "q": q,
        "N": N,
        "n": n,
        "B": bound,
        "trial_hard": True,
        "stable_certificate": certificate,
        "two_replays_match_ignoring_timing": True,
        "result": first,
    }
    write_output(args.output, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--prime-min", type=int, default=300)
    parser.add_argument("--prime-max", type=int, default=1200)
    parser.add_argument("--pair-cap", type=int, default=200)
    parser.add_argument("--pairs-per-p", type=int, default=4)
    parser.add_argument("--verify-modulus", type=int)
    parser.add_argument("--verify-p", type=int)
    parser.add_argument("--verify-q", type=int)
    args = parser.parse_args()

    print(f"source_sha256={sha256(Path(__file__).resolve())}", file=sys.stderr)
    print(f"f98_source_sha256={sha256(F98_SOURCE)}", file=sys.stderr)
    if args.verify_modulus is None:
        payload = scan(args)
    else:
        payload = verify(args)
    print(f"status={payload['status']}")
    print(f"elapsed_seconds={payload.get('elapsed_seconds', payload.get('result', {}).get('elapsed_seconds'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
