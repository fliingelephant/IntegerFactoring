#!/usr/bin/env python3
"""Independent, proof-blind reconstruction for F102.

This program reads only the public replay JSON permitted by
RECONSTRUCTION_STATEMENT.md.  Run it with ``sage -python``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import signal
import sys
import time
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from sage.all import factor, is_prime
from sage.version import version as sage_version


HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parent / "F98_multiseed_presentation_closure_kill" / "PUBLIC_REPLAY_OUTPUT.json"
STATEMENT = HERE / "RECONSTRUCTION_STATEMENT.md"
RECONSTRUCTION = HERE / "RECONSTRUCT.md"
OUTPUT = HERE / "BLIND_RECONSTRUCT_OUTPUT.json"
LOG = HERE / "BLIND_RECONSTRUCT_RUN.log"
MANIFEST = HERE / "BLIND_RECONSTRUCT_MANIFEST.json"
REQUIRED_PUBLIC_SHA256 = "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab"
EXPECTED_FULL = {
    "columns": 9414,
    "rows": 11034,
    "rank": 8926,
    "nullity": 488,
    "initial_degree_one_rows": 7884,
    "peeled_columns": 7633,
    "core_columns": 1781,
    "core_rows": 1299,
    "core_rank": 1293,
    "core_nullity": 488,
    "core_components": [1781],
    "ordered_core_column_sha256": "5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8",
}
EXPECTED_PREFIX = {
    "columns": 4293,
    "rows": 5658,
    "rank": 4291,
    "nullity": 2,
    "initial_degree_one_rows": 4062,
    "peeled_columns": 3920,
    "core_columns": 373,
    "core_rows": 387,
    "core_rank": 371,
    "core_nullity": 2,
    "core_components": [373],
    "ordered_core_column_sha256": "9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relation(seed_or_endpoint: int, modulus: int) -> tuple[int, int, int]:
    c = seed_or_endpoint
    w = pow(c, -1, modulus)
    return c * w, c, w


def unique_pairs(active_pairs: list[list[int]]) -> list[tuple[int, int, int]]:
    answer = []
    seen = set()
    for active_index, pair in enumerate(active_pairs):
        uv = tuple(pair)
        if uv not in seen:
            seen.add(uv)
            answer.append((active_index, uv[0], uv[1]))
    return answer


def raw_stream(public: dict, hypothesis: str = "f98_first_occurrence") -> list[dict]:
    N, n, B = public["N"], public["n"], public["B"]
    records = []
    for seed in range(2, n + 1):
        P, c, w = relation(seed, N)
        records.append({"P": P, "c": c, "w": w, "kind": "initial_seed", "seed": seed})

    pairs = unique_pairs(public["active_pairs"])
    identity_start_seen = False
    for active_index, u, v in pairs:
        family_seen = set(range(2, n + 1))
        start = 2 if hypothesis == "e2_all" else 1
        for exponent in range(start, B + 1):
            endpoints = (
                ("u_power_times_v", pow(u, exponent, N) * v % N),
                ("u_times_v_power", u * pow(v, exponent, N) % N),
            )
            for orientation, c in endpoints:
                if hypothesis == "e1_gt_n" and c <= n:
                    continue
                if hypothesis in {"e1_family_first_nonseed", "f98_first_occurrence"}:
                    if c in family_seen:
                        continue
                    family_seen.add(c)
                # The trajectory start c = uv = 1 is shared by the two
                # inverse-pair families.  It is a common start state, so the
                # first-occurrence stream retains it only for the first such
                # family.  An identity reached later inside a trajectory is a
                # distinct raw occurrence and remains in the stream.
                if hypothesis == "f98_first_occurrence" and exponent == 1 and c == 1:
                    if identity_start_seen:
                        continue
                    identity_start_seen = True
                P, c, w = relation(c, N)
                records.append(
                    {
                        "P": P,
                        "c": c,
                        "w": w,
                        "kind": "feedback_trajectory",
                        "active_index": active_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    }
                )
    return records


def first_nonzero_values(records: list[dict], raw_limit: int | None = None) -> list[dict]:
    seen = set()
    answer = []
    stop = len(records) if raw_limit is None else min(raw_limit, len(records))
    for raw_index, record in enumerate(records[:stop]):
        P = record["P"]
        if P == 1 or P in seen:
            continue
        seen.add(P)
        answer.append(record | {"raw_index": raw_index})
    return answer


@lru_cache(maxsize=None)
def exact_factorization(value: int) -> tuple[tuple[int, int], ...]:
    factors = tuple((int(prime), int(exponent)) for prime, exponent in factor(value))
    product = 1
    for prime, exponent in factors:
        assert is_prime(prime)
        product *= prime**exponent
    assert product == value
    return factors


def odd_prime_support(value: int) -> tuple[int, ...]:
    return tuple(prime for prime, exponent in exact_factorization(value) if exponent & 1)


def gf2_rank(column_supports: list[tuple[int, ...]], row_index: dict[int, int]) -> int:
    pivots = {}
    for support in column_supports:
        vector = 0
        for prime in support:
            vector ^= 1 << row_index[prime]
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return len(pivots)


def peel(column_supports: list[tuple[int, ...]], order: str) -> tuple[set[int], int, list[int]]:
    row_columns = defaultdict(set)
    for column, support in enumerate(column_supports):
        for prime in support:
            row_columns[prime].add(column)
    initial_degree_one = sum(len(columns) == 1 for columns in row_columns.values())
    active = set(range(len(column_supports)))

    if order == "fifo":
        queue = deque(prime for prime, columns in row_columns.items() if len(columns) == 1)

        def take():
            return queue.popleft()

        def add(prime):
            queue.append(prime)

        def nonempty():
            return bool(queue)

    else:
        pending = [prime for prime, columns in row_columns.items() if len(columns) == 1]
        rng = random.Random(102)
        rng.shuffle(pending)

        def take():
            return pending.pop()

        def add(prime):
            pending.append(prime)

        def nonempty():
            return bool(pending)

    deletion_sequence = []
    while nonempty():
        prime = take()
        columns = row_columns[prime]
        if len(columns) != 1:
            continue
        column = next(iter(columns))
        if column not in active:
            continue
        active.remove(column)
        deletion_sequence.append(column)
        for incident_prime in column_supports[column]:
            incident = row_columns[incident_prime]
            incident.discard(column)
            if len(incident) == 1:
                add(incident_prime)
    return active, initial_degree_one, deletion_sequence


def component_sizes(core: set[int], column_supports: list[tuple[int, ...]]) -> list[int]:
    row_columns = defaultdict(list)
    for column in core:
        for prime in column_supports[column]:
            row_columns[prime].append(column)
    unseen = set(core)
    sizes = []
    while unseen:
        start = unseen.pop()
        stack = [start]
        size = 0
        while stack:
            column = stack.pop()
            size += 1
            for prime in column_supports[column]:
                for neighbor in row_columns[prime]:
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        stack.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def hash_encodings(values: list[int]) -> dict[str, str]:
    encodings = {
        "newline_final": ("\n".join(map(str, values)) + "\n").encode(),
        "newline_no_final": "\n".join(map(str, values)).encode(),
        "comma_final": (",".join(map(str, values)) + ",").encode(),
        "comma_no_final": ",".join(map(str, values)).encode(),
        "space_no_final": " ".join(map(str, values)).encode(),
        "json_compact": json.dumps(values, separators=(",", ":")).encode(),
        "json_default": json.dumps(values).encode(),
        "u64_be": b"".join(value.to_bytes(8, "big") for value in values),
        "u64_le": b"".join(value.to_bytes(8, "little") for value in values),
    }
    if not values or max(values) < 2**32:
        encodings["u32_be"] = b"".join(value.to_bytes(4, "big") for value in values)
        encodings["u32_le"] = b"".join(value.to_bytes(4, "little") for value in values)
    return {name: sha256_bytes(data) for name, data in encodings.items()}


def analyze(records: list[dict], raw_limit: int | None) -> dict:
    columns = first_nonzero_values(records, raw_limit)
    supports = [odd_prime_support(record["P"]) for record in columns]
    primes = sorted({prime for support in supports for prime in support})
    row_index = {prime: index for index, prime in enumerate(primes)}
    rank = gf2_rank(supports, row_index)
    fifo, initial_degree_one, fifo_deletions = peel(supports, "fifo")
    shuffled, initial_degree_one_2, shuffled_deletions = peel(supports, "shuffled")
    assert initial_degree_one == initial_degree_one_2
    core_supports = [supports[column] for column in sorted(fifo)]
    core_primes = sorted({prime for support in core_supports for prime in support})
    core_row_index = {prime: index for index, prime in enumerate(core_primes)}
    core_rank = gf2_rank(core_supports, core_row_index)
    values = [columns[column]["P"] for column in sorted(fifo)]
    core_records = [columns[column] for column in sorted(fifo)]
    seed_values = sorted(record["seed"] for record in core_records if record["kind"] == "initial_seed")
    feedback_records = [record for record in core_records if record["kind"] == "feedback_trajectory"]
    orientations = Counter(record["orientation"] for record in feedback_records)
    families = sorted({(record["active_index"], record["u"], record["v"]) for record in feedback_records})
    row_degrees = Counter(prime for support in core_supports for prime in support)
    index_hashes = hash_encodings(sorted(fifo))
    return {
        "columns": len(columns),
        "rows": len(primes),
        "rank": rank,
        "nullity": len(columns) - rank,
        "initial_degree_one_rows": initial_degree_one,
        "peeled_columns": len(fifo_deletions),
        "core_columns": len(fifo),
        "core_rows": len(core_primes),
        "core_rank": core_rank,
        "core_nullity": len(fifo) - core_rank,
        "core_components": component_sizes(fifo, supports),
        "orders_same": fifo == shuffled and len(fifo_deletions) == len(shuffled_deletions),
        "deletion_sequences_different": fifo_deletions != shuffled_deletions,
        "peeling_order_digests": {
            "fifo": hash_encodings(fifo_deletions)["comma_no_final"],
            "seeded_shuffled_lifo": hash_encodings(shuffled_deletions)["comma_no_final"],
        },
        "final_minimum_incident_row_degree": min(row_degrees.values()),
        "core_indices": sorted(fifo),
        "ordered_core_column_sha256": index_hashes["comma_no_final"],
        "hash_payload": "ascending zero-based core column indices joined by ASCII commas, without a trailing comma",
        "core_value_sha256_diagnostics": hash_encodings(values),
        "seed_values_in_core": seed_values,
        "feedback_columns_in_core": len(feedback_records),
        "feedback_family_count": len(families),
        "feedback_families": [list(family) for family in families],
        "orientation_counts": dict(sorted(orientations.items())),
        "columns_data": columns,
    }


def replay_certificate(public: dict, records: list[dict], columns: list[dict]) -> dict:
    certificate = public["decoder"]["first_useful_certificate"]
    raw_indices = certificate["selected_raw_indices_zero_based"]
    column_indices = certificate["selected_columns_zero_based"]
    witnesses = certificate["witness_records"]
    mismatches = []
    for position, (raw_index, column_index, witness) in enumerate(zip(raw_indices, column_indices, witnesses)):
        actual = records[raw_index]
        for key in ("P", "c", "w"):
            if actual[key] != witness[key]:
                mismatches.append({"position": position, "field": key, "expected": witness[key], "actual": actual[key]})
        if columns[column_index]["P"] != witness["P"]:
            mismatches.append(
                {
                    "position": position,
                    "field": "selected_column_P",
                    "expected": witness["P"],
                    "actual": columns[column_index]["P"],
                }
            )
        provenance = witness["provenance"]
        if provenance["kind"] == "initial_seed":
            checks = {"kind": "initial_seed", "seed": provenance["seed"]}
        else:
            checks = {
                "kind": "feedback_trajectory",
                "active_index": provenance["active_relation_index_zero_based"],
                "u": provenance["u"],
                "v": provenance["v"],
                "exponent": provenance["exponent"],
                "orientation": provenance["orientation"],
            }
        for key, expected in checks.items():
            if actual.get(key) != expected:
                mismatches.append({"position": position, "field": key, "expected": expected, "actual": actual.get(key)})
    return {
        "support": certificate["support"],
        "witness_count": len(witnesses),
        "raw_indices_exact": not mismatches,
        "selected_columns_exact": not mismatches,
        "mismatch_count": len(mismatches),
        "mismatch_sample": mismatches[:5],
        "selected_column_indices": column_indices,
    }


def finite_claim_check(result: dict, expected: dict) -> dict:
    observed = {key: result[key] for key in expected}
    mismatches = {
        key: {"expected": expected[key], "observed": observed[key]}
        for key in expected
        if observed[key] != expected[key]
    }
    return {"status": "PASS" if not mismatches else "FAIL", "observed": observed, "mismatches": mismatches}


def factorization_transcript_hash(columns: list[dict]) -> str:
    transcript = [[record["P"], [list(item) for item in exact_factorization(record["P"])]] for record in columns]
    return sha256_bytes(json.dumps(transcript, separators=(",", ":")).encode())


def stream_summary(records: list[dict]) -> dict:
    values = [record["P"] for record in records]
    distinct = set(values)
    return {
        "raw_records": len(records),
        "raw_identity_records": values.count(1),
        "distinct_values_including_identity": len(distinct),
        "duplicate_occurrences": len(values) - len(distinct),
        "distinct_nonidentity_values": len(distinct - {1}),
    }


def public_witness_index_mismatches(public: dict, records: list[dict]) -> int:
    certificate = public["decoder"]["first_useful_certificate"]
    mismatches = 0
    for raw_index, witness in zip(
        certificate["selected_raw_indices_zero_based"], certificate["witness_records"]
    ):
        if raw_index >= len(records) or records[raw_index]["P"] != witness["P"]:
            mismatches += 1
    return mismatches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args()
    signal.alarm(args.timeout)
    started = time.time()
    log_lines = [
        "F102 proof-blind reconstruction run",
        f"start_utc={datetime.now(timezone.utc).isoformat()}",
        f"internal_hard_timeout_seconds={args.timeout}",
        "external_hard_timeout_seconds=300",
    ]
    public_bytes = PUBLIC.read_bytes()
    actual_hash = sha256_bytes(public_bytes)
    if actual_hash != REQUIRED_PUBLIC_SHA256:
        raise RuntimeError(f"public artifact hash mismatch: {actual_hash}")
    public = json.loads(public_bytes)
    log_lines.append(f"public_sha256={actual_hash}")

    records = raw_stream(public)
    stream = stream_summary(records)
    full = analyze(records, None)
    prefix = analyze(records, 5616)
    certificate = replay_certificate(public, records, full["columns_data"])
    certificate_in_core = set(certificate["selected_column_indices"]).issubset(full["core_indices"])
    full_check = finite_claim_check(full, EXPECTED_FULL)
    prefix_check = finite_claim_check(prefix, EXPECTED_PREFIX)

    e2_records = raw_stream(public, "e2_all")
    e2_prefix = analyze(e2_records, 5616)
    gt_n_records = raw_stream(public, "e1_gt_n")
    family_records = raw_stream(public, "e1_family_first_nonseed")
    failed_attempts = [
        {
            "name": "start_feedback_at_exponent_2",
            "status": "FAIL",
            "reason": "The selected raw prefix has the wrong rank defect and core.",
            "observed": {
                "raw_records": len(e2_records),
                "prefix_columns": e2_prefix["columns"],
                "prefix_nullity": e2_prefix["nullity"],
                "prefix_core_columns": e2_prefix["core_columns"],
                "prefix_core_sha256": e2_prefix["ordered_core_column_sha256"],
            },
        },
        {
            "name": "retain_only_endpoints_strictly_above_n",
            "status": "FAIL",
            "reason": "It emits no P=1 record, has the wrong raw length, and misses public witness indices.",
            "observed": stream_summary(gt_n_records)
            | {"public_witness_index_mismatches": public_witness_index_mismatches(public, gt_n_records)},
        },
        {
            "name": "family_first_occurrence_without_shared_start_deduplication",
            "status": "FAIL",
            "reason": "It retains the shared inverse-family identity start twice.",
            "observed": stream_summary(family_records)
            | {"public_witness_index_mismatches": public_witness_index_mismatches(public, family_records)},
        },
    ]

    full_public = {key: value for key, value in full.items() if key not in {"core_indices", "columns_data"}}
    prefix_public = {key: value for key, value in prefix.items() if key not in {"core_indices", "columns_data"}}
    finite_pass = (
        full_check["status"] == "PASS"
        and prefix_check["status"] == "PASS"
        and full["orders_same"]
        and prefix["orders_same"]
        and full["deletion_sequences_different"]
        and prefix["deletion_sequences_different"]
        and full["core_nullity"] == full["nullity"]
        and prefix["core_nullity"] == prefix["nullity"]
        and full["final_minimum_incident_row_degree"] >= 2
        and prefix["final_minimum_incident_row_degree"] >= 2
        and certificate["raw_indices_exact"]
        and certificate_in_core
        and full["seed_values_in_core"] == [2, 11, 27]
        and full["feedback_columns_in_core"] == 1778
        and full["feedback_family_count"] == 8
        and full["orientation_counts"] == {"u_power_times_v": 1138, "u_times_v_power": 640}
    )
    result = {
        "status": "PASS" if finite_pass else "FAIL",
        "scope": {
            "passed": "Frozen F98 prime-parity matrix, prefix, peeling-order invariance, complete-kernel preservation by zero extension (with equal nullity as a finite cross-check), and certificate containment.",
            "not_claimed": [
                "The prime matrix is public.",
                "Connectedness implies a useful root.",
                "Every composite input has a nonempty or rank-deficient core.",
                "Useful circuits have inverse-polynomial density.",
                "This construction is a factoring algorithm.",
            ],
        },
        "input": {
            "N": public["N"],
            "n": public["n"],
            "B": public["B"],
            "active_pair_records": len(public["active_pairs"]),
            "distinct_active_pair_families": len(unique_pairs(public["active_pairs"])),
            "public_artifact_sha256": actual_hash,
            "required_public_artifact_sha256": REQUIRED_PUBLIC_SHA256,
        },
        "stream": stream,
        "stream_rule": {
            "seeds": "c = 2,...,n; w = c^(-1) mod N; P = c*w",
            "feedback": "For each first active-pair family, e = 1,...,B, in u_power_times_v then u_times_v_power order.",
            "endpoint_first_occurrence": "Suppress c in 2,...,n and later repeats of c inside one family.",
            "shared_start": "Among inverse-pair families with uv = 1, retain the common e=1 identity start once.",
            "matrix_columns": "Discard P=1, then retain the first raw occurrence of each exact P.",
        },
        "full": full_public,
        "prefix_before_raw_index_5616": prefix_public,
        "checks": {
            "full_claims": full_check,
            "prefix_claims": prefix_check,
            "certificate_public_witness_replay": certificate,
            "all_166_certificate_columns_in_full_core": certificate_in_core,
            "factorization_transcript_sha256": factorization_transcript_hash(full["columns_data"]),
            "all_factorizations_multiply_back_and_all_bases_are_prime": True,
        },
        "failed_attempts_preserved": failed_attempts,
        "elapsed_seconds": time.time() - started,
    }
    log_lines.extend(
        [
            f"raw_records={stream['raw_records']}",
            f"distinct_nonidentity_values={stream['distinct_nonidentity_values']}",
            f"full_status={full_check['status']}",
            f"prefix_status={prefix_check['status']}",
            f"certificate_replay_exact={certificate['raw_indices_exact']}",
            f"certificate_in_core={certificate_in_core}",
            f"final_status={result['status']}",
            f"elapsed_seconds={result['elapsed_seconds']:.6f}",
            "PASS scope is finite and frozen-batch only; excluded claims are listed in BLIND_RECONSTRUCT_OUTPUT.json.",
        ]
    )

    if args.write_artifacts:
        output_bytes = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
        OUTPUT.write_bytes(output_bytes)
        log_bytes = ("\n".join(log_lines) + "\n").encode()
        LOG.write_bytes(log_bytes)
        manifest = {
            "status": result["status"],
            "run_utc": datetime.now(timezone.utc).isoformat(),
            "command": "DOT_SAGE=/tmp/f102_blind_sage timeout 300s sage -python blind_reconstruct_f102.py --timeout 240 --write-artifacts",
            "hard_timeout": {"external_seconds": 300, "internal_sigalrm_seconds": args.timeout},
            "exit_status": 0,
            "runtime": {"python": sys.version, "sage": sage_version},
            "read_scope": [str(STATEMENT), str(PUBLIC)],
            "artifacts": {
                "statement": {"path": str(STATEMENT), "sha256": sha256_bytes(STATEMENT.read_bytes())},
                "reconstruction": {
                    "path": str(RECONSTRUCTION),
                    "sha256": sha256_bytes(RECONSTRUCTION.read_bytes()),
                },
                "public_input": {"path": str(PUBLIC), "sha256": actual_hash},
                "source": {"path": str(Path(__file__).resolve()), "sha256": sha256_bytes(Path(__file__).read_bytes())},
                "output": {"path": str(OUTPUT), "sha256": sha256_bytes(output_bytes)},
                "log": {"path": str(LOG), "sha256": sha256_bytes(log_bytes)},
            },
            "failed_attempts_preserved_in": str(OUTPUT),
        }
        MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "elapsed_seconds": result["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
