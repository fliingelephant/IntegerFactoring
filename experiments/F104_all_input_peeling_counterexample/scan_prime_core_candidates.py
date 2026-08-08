#!/usr/bin/env python3
"""Fast factor-assisted candidate scan using hidden prime-parity row masks.

For discovery only, this replaces terminal P66 nonsquare-block masks with
the theorem-equivalent set of distinct nonzero hidden prime-parity masks.
Any candidate must still pass the separate factor-free P66 replay.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent
BASE_SOURCE = HERE / "scan_one_round_cores.py"
EXPECTED_BASE_SHA256 = "41c8ddee5d51d85349af2b61e239f81f9c6e12fb13d1eca92f0440f5d5eece50"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if sha256(BASE_SOURCE) != EXPECTED_BASE_SHA256:
    raise AssertionError("the exact N-only scan source hash changed")
SPEC = importlib.util.spec_from_file_location("f104_exact_replay", BASE_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import the exact F104 replay")
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)


def is_prime_u64(value: int) -> bool:
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd = value - 1
    shift = 0
    while odd % 2 == 0:
        odd //= 2
        shift += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        residue = pow(base, odd, value)
        if residue in (1, value - 1):
            continue
        for _ in range(shift - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def pollard_divisor(value: int) -> int:
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return prime
    constant = 1
    while True:
        x = 2
        y = 2
        divisor = 1
        while divisor == 1:
            x = (x * x + constant) % value
            y = (y * y + constant) % value
            y = (y * y + constant) % value
            divisor = math.gcd(abs(x - y), value)
        if divisor != value:
            return divisor
        constant += 1


def factor_u64(value: int) -> dict[int, int]:
    assert 0 < value < 1 << 64
    prime_factors: list[int] = []
    stack = [value]
    while stack:
        current = stack.pop()
        if current == 1:
            continue
        if is_prime_u64(current):
            prime_factors.append(current)
            continue
        divisor = pollard_divisor(current)
        stack.extend((divisor, current // divisor))
    factors = Counter(prime_factors)
    result = dict(sorted(factors.items()))
    assert math.prod(prime**exponent for prime, exponent in result.items()) == value
    assert all(is_prime_u64(prime) for prime in result)
    return result


def hidden_prime_matrix(unique_records: list[tuple[int, dict[str, object]]]) -> dict[str, object]:
    prime_masks: dict[int, int] = {}
    relation_values: list[int] = []
    factor_cache: dict[int, dict[int, int]] = {1: {}}
    for column, (_, record) in enumerate(unique_records):
        relation_values.append(int(record["P"]))
        endpoint_parity: set[int] = set()
        for endpoint in (int(record["c"]), int(record["w"])):
            factors = factor_cache.get(endpoint)
            if factors is None:
                factors = factor_u64(endpoint)
                factor_cache[endpoint] = factors
            for prime, exponent in factors.items():
                if exponent & 1:
                    if prime in endpoint_parity:
                        endpoint_parity.remove(prime)
                    else:
                        endpoint_parity.add(prime)
        for prime in endpoint_parity:
            prime_masks[prime] = prime_masks.get(prime, 0) ^ (1 << column)

    distinct_rows = sorted({mask for mask in prime_masks.values() if mask})
    rank, kernel = BASE.F98.binary_kernel_basis(distinct_rows, len(unique_records))
    assert rank == BASE.row_rank(distinct_rows)
    return {
        "row_masks": distinct_rows,
        "relation_values": relation_values,
        "rank": rank,
        "kernel": kernel,
        "blocks": len(distinct_rows),
        "square_blocks": 0,
        "refinements": 0,
        "gcd_tests": 0,
        "hidden_prime_count": len(prime_masks),
        "distinct_nonzero_mask_count": len(distinct_rows),
        "factored_distinct_endpoint_count": len(factor_cache) - 1,
    }


# The N-only generation and all direct/initial screens remain byte-for-byte in
# BASE.run_one_round. Only its terminal matrix builder is replaced for this
# factor-assisted discovery source.
BASE.p66_matrix = hidden_prime_matrix


def normalize_result(result: dict[str, object]) -> dict[str, object]:
    if result.get("status") != "round_complete":
        return result
    diagnostic = result["matrix"].pop("p66")
    result["matrix"]["hidden_prime_diagnostic"] = diagnostic
    result["matrix"]["row_source"] = "distinct nonzero hidden prime-parity masks"
    result["matrix"]["p66_mask_equivalence_theorem_used"] = True
    return result


def write_output(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-min", type=int, required=True)
    parser.add_argument("--prime-max", type=int, required=True)
    parser.add_argument("--pair-cap", type=int, required=True)
    parser.add_argument("--pairs-per-p", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    primes = [
        prime
        for prime in BASE.primes_through(args.prime_max)
        if args.prime_min <= prime <= args.prime_max and prime > 3
    ]
    pairs_tested = 0
    stable_tested = 0
    completed = 0
    trace: list[dict[str, object]] = []
    counterexample = None

    payload: dict[str, object] = {
        "status": "running",
        "role": "factor-assisted hidden-prime candidate scan; candidate requires factor-free P66 replay",
        "source_sha256": sha256(Path(__file__).resolve()),
        "exact_replay_source_sha256": sha256(BASE_SOURCE),
        "f98_source_sha256": BASE.sha256(BASE.F98_SOURCE),
        "workflow_change": {
            "generation_and_screens": "unchanged pinned N-only replay",
            "discovery_rows": "distinct nonzero hidden prime-parity masks",
            "justification": "terminal P66 and hidden prime rows have the same distinct nonzero masks",
            "acceptance": "separate factor-free P66 replay required",
        },
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
            certificate = BASE.stable_certificate(p, q)
            if not certificate["stable"]:
                continue
            stable_tested += 1
            result = normalize_result(BASE.run_one_round(N))
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
                    second = normalize_result(BASE.run_one_round(N))
                    assert second["status"] == "round_complete"
                    first_matrix = result["matrix"]
                    second_matrix = second["matrix"]
                    assert first_matrix == second_matrix
                    entry["deterministic_second_prime_replay_match"] = True
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
            "status": "counterexample_candidate" if counterexample is not None else "cap_complete",
            "pairs_tested": pairs_tested,
            "stable_pairs_tested": stable_tested,
            "completed_rounds": completed,
            "trace": trace,
            "counterexample": counterexample,
            "elapsed_seconds": time.monotonic() - started,
        }
    )
    write_output(args.output, payload)
    print(f"status={payload['status']}")
    print(f"elapsed_seconds={payload['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
