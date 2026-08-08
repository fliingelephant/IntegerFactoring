#!/usr/bin/env python3
"""Proof-blind N-only reconstruction of the fixed F111 certificate."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
STATEMENT = HERE / "RECONSTRUCT_STATEMENT.md"
PUBLIC_INPUT = HERE / "RECONSTRUCT_INPUT.json"
EXPECTED_STATEMENT_SHA256 = "e1a573feaceb2465d599df21a41b46372c25c6c30cb15ad7d1b6c56230fe0dae"
EXPECTED_INPUT_SHA256 = "8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_uint(value: int) -> bytes:
    payload = value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big")
    return len(payload).to_bytes(8, "big") + payload


def hash_uint(value: int) -> str:
    return hashlib.sha256(canonical_uint(value)).hexdigest()


def hash_uint_sequence(values: list[int]) -> str:
    digest = hashlib.sha256()
    digest.update(len(values).to_bytes(8, "big"))
    for value in values:
        digest.update(canonical_uint(value))
    return digest.hexdigest()


def exact_nth_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        powered = middle**exponent
        if powered < value:
            low = middle
        elif powered > value:
            high = middle
        else:
            return middle
    return low if low**exponent == value else None


def largest_perfect_power(value: int) -> tuple[int, int, int]:
    tests = 0
    for exponent in range(value.bit_length(), 1, -1):
        tests += 1
        root = exact_nth_root(value, exponent)
        if root is not None:
            return root, exponent, tests
    return value, 1, tests


def deterministic_basis(
    endpoint_values: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    pending = [
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoint_values)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = {
        "initial_stack_items": len(pending),
        "generated_stack_pushes": 0,
        "stack_pops": 0,
        "maximum_stack_size": len(pending),
        "unit_discards": 0,
        "perfect_power_exponent_tests": 0,
        "perfect_power_extractions": 0,
        "perfect_power_exponent_sum": 0,
        "basis_gcd_tests": 0,
        "overlap_events": 0,
        "identical_merges": 0,
        "nonidentical_splits": 0,
        "basis_appends": 0,
    }

    while pending:
        value, signature = pending.pop()
        stats["stack_pops"] += 1
        if value == 1:
            stats["unit_discards"] += 1
            continue
        root, power, tests = largest_perfect_power(value)
        stats["perfect_power_exponent_tests"] += tests
        if power > 1:
            value = root
            signature = {
                endpoint: power * multiplicity
                for endpoint, multiplicity in signature.items()
            }
            stats["perfect_power_extractions"] += 1
            stats["perfect_power_exponent_sum"] += power

        for position, (old_value, old_signature) in enumerate(basis):
            stats["basis_gcd_tests"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            basis.pop(position)
            stats["overlap_events"] += 1
            if value == old_value:
                merged = dict(signature)
                for endpoint, multiplicity in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + multiplicity
                pending.append((value, merged))
                stats["generated_stack_pushes"] += 1
                stats["identical_merges"] += 1
            else:
                pending.extend(
                    (
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, old_signature),
                        (old_value // divisor, old_signature),
                    )
                )
                stats["generated_stack_pushes"] += 4
                stats["nonidentical_splits"] += 1
            stats["maximum_stack_size"] = max(stats["maximum_stack_size"], len(pending))
            break
        else:
            basis.append((value, signature))
            stats["basis_appends"] += 1

    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoint_values)
    for position, (block, signature) in enumerate(basis):
        assert largest_perfect_power(block)[1] == 1
        assert all(math.gcd(block, old_block) == 1 for old_block, _ in basis[:position])
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= block**multiplicity
    assert reconstructed == endpoint_values
    stats["final_basis_blocks"] = len(basis)
    stats["final_signature_entries"] = sum(len(signature) for _, signature in basis)
    return basis, stats


def frozen_pairs(
    basis: list[tuple[int, dict[int, int]]], relation_count: int
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    pairs = []
    supports = []
    for relation_index in range(relation_count):
        support = [
            block
            for block, signature in basis
            if signature.get(2 * relation_index, 0)
            + signature.get(2 * relation_index + 1, 0)
            > 0
        ]
        assert support
        supports.append(support)
        pairs.append((support[0], 1) if len(support) == 1 else (support[0], support[1]))
    return pairs, supports


def hash_record_trace(records: list[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    digest.update(len(records).to_bytes(8, "big"))
    for record in records:
        digest.update(canonical_uint(int(record["c"])))
        digest.update(canonical_uint(int(record["w"])))
        provenance = json.dumps(
            record["provenance"], sort_keys=True, separators=(",", ":")
        ).encode()
        digest.update(len(provenance).to_bytes(8, "big"))
        digest.update(provenance)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    statement_hash = sha256_file(STATEMENT)
    input_hash = sha256_file(PUBLIC_INPUT)
    assert statement_hash == EXPECTED_STATEMENT_SHA256
    assert input_hash == EXPECTED_INPUT_SHA256
    supplied = json.loads(PUBLIC_INPUT.read_text(encoding="utf-8"))
    modulus = int(supplied["N"])
    n = int(supplied["n"])
    bound = int(supplied["bound"])
    stop_count = int(supplied["source_stop_relation_count"])
    assert modulus % 2 == 1
    assert n == modulus.bit_length()
    assert bound == n * n

    nontrivial_trial_gcds = [
        {"trial": trial, "gcd": math.gcd(trial, modulus)}
        for trial in range(2, bound + 1)
        if math.gcd(trial, modulus) != 1
    ]

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()
    attempts = 0
    duplicate_residues = 0
    sign_counts = {
        "minus": {"unit": 0, "improper_N": 0, "proper": 0},
        "plus": {"unit": 0, "improper_N": 0, "proper": 0},
    }
    improper_screens = []
    proper_screens = []

    def attempt(c: int, provenance: dict[str, object]) -> bool:
        nonlocal attempts, duplicate_residues
        attempts += 1
        if c in seen_residues:
            duplicate_residues += 1
            return False
        seen_residues.add(c)
        w = pow(c, -1, modulus)
        record_index = len(records)
        record = {"c": c, "w": w, "P": c * w, "provenance": provenance}
        records.append(record)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if divisor == 1:
                sign_counts[sign]["unit"] += 1
            elif divisor == modulus:
                sign_counts[sign]["improper_N"] += 1
                identity = "c_equals_w" if sign == "minus" else "c_plus_w_equals_N"
                assert (sign == "minus" and c == w) or (
                    sign == "plus" and c + w == modulus
                )
                improper_screens.append(
                    {
                        "record_index_zero_based": record_index,
                        "sign": sign,
                        "gcd": divisor,
                        "c": c,
                        "w": w,
                        "identity": identity,
                        "provenance": provenance,
                    }
                )
            else:
                sign_counts[sign]["proper"] += 1
                proper_screens.append(
                    {
                        "record_index_zero_based": record_index,
                        "sign": sign,
                        "gcd": divisor,
                        "c": c,
                        "w": w,
                        "provenance": provenance,
                    }
                )
        endpoints.extend((c, w))
        return True

    for seed in range(2, n + 1):
        assert attempt(seed, {"kind": "initial_seed", "seed": seed})

    seed_relation_count = len(records)
    seed_endpoints = list(endpoints)
    basis, basis_stats = deterministic_basis(seed_endpoints)
    ordered_frozen_pairs, seed_supports = frozen_pairs(basis, seed_relation_count)

    for pair_index, (u, v) in enumerate(ordered_frozen_pairs):
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                attempt(
                    c,
                    {
                        "kind": "frozen_seed_basis_pair",
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )

    frozen_record_count = len(records)
    frozen_attempt_count = attempts
    frozen_duplicate_count = duplicate_residues
    assert frozen_record_count < stop_count

    stop_provenance = None
    for appended_index, (u, v) in enumerate(((2, 3), (2, 4))):
        stopped = False
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                provenance = {
                    "kind": "nonadaptive_seed_pair",
                    "pair_index_zero_based": appended_index,
                    "u": u,
                    "v": v,
                    "exponent": exponent,
                    "orientation": orientation,
                }
                retained = attempt(c, provenance)
                if retained and len(records) == stop_count:
                    stop_provenance = provenance
                    stopped = True
                    break
            if stopped:
                break
        if stopped:
            break
    assert stop_provenance is not None
    assert len(records) == stop_count
    assert attempts - duplicate_residues == len(records) == len(seen_residues)
    assert len(endpoints) == 2 * len(records)
    assert sum(sign_counts[sign][kind] for sign in sign_counts for kind in sign_counts[sign]) == 2 * len(records)

    # Advice enters only after the complete public source trace exists.
    selected_indices = [
        int(index) for index in supplied["dependency_relation_indices_zero_based"]
    ]
    indices_in_range = bool(selected_indices) and all(
        0 <= index < len(records) for index in selected_indices
    )
    indices_distinct = len(selected_indices) == len(set(selected_indices))
    indices_increasing = all(
        left < right for left, right in zip(selected_indices, selected_indices[1:])
    )
    indices_end_at_stop = selected_indices[-1] == len(records) - 1
    assert indices_in_range and indices_distinct and indices_increasing and indices_end_at_stop

    selected_records = [records[index] for index in selected_indices]
    provenance_split = dict(
        sorted(Counter(record["provenance"]["kind"] for record in selected_records).items())
    )
    selected_appended_counts = Counter(
        (
            int(record["provenance"]["pair_index_zero_based"]),
            int(record["provenance"]["u"]),
            int(record["provenance"]["v"]),
        )
        for record in selected_records
        if record["provenance"]["kind"] == "nonadaptive_seed_pair"
    )
    selected_appended_pairs = [
        {
            "pair_index_zero_based": pair_index,
            "u": u,
            "v": v,
            "selected_relations": count,
        }
        for (pair_index, u, v), count in sorted(selected_appended_counts.items())
    ]
    selected_values = [int(record["P"]) for record in selected_records]
    selected_product = math.prod(selected_values)
    positive_root = math.isqrt(selected_product)
    product_is_square = positive_root * positive_root == selected_product
    root_mod_N = positive_root % modulus
    root_square_mod_N = root_mod_N * root_mod_N % modulus
    root_is_global = root_mod_N in (1, modulus - 1)
    terminal_minus = math.gcd(positive_root - 1, modulus)
    terminal_plus = math.gcd(positive_root + 1, modulus)
    terminal_proper = [
        divisor
        for divisor in (terminal_minus, terminal_plus)
        if 1 < divisor < modulus
    ]

    basis_signature_digest = hashlib.sha256()
    basis_signature_digest.update(len(basis).to_bytes(8, "big"))
    for block, signature in basis:
        basis_signature_digest.update(canonical_uint(block))
        basis_signature_digest.update(len(signature).to_bytes(8, "big"))
        for endpoint, multiplicity in sorted(signature.items()):
            basis_signature_digest.update(endpoint.to_bytes(8, "big"))
            basis_signature_digest.update(multiplicity.to_bytes(8, "big"))

    checks = {
        "authorized_input_hashes_match": True,
        "n_and_bound_match_N": n == modulus.bit_length() and bound == n * n,
        "trial_gcd_screen_all_one": not nontrivial_trial_gcds,
        "basis_reconstructs_seed_endpoints": True,
        "basis_blocks_pairwise_coprime": all(
            math.gcd(block, old_block) == 1
            for position, (block, _) in enumerate(basis)
            for old_block, _ in basis[:position]
        ),
        "basis_blocks_not_perfect_powers": all(
            largest_perfect_power(block)[1] == 1 for block, _ in basis
        ),
        "exact_stop_reached": len(records) == stop_count,
        "attempt_accounting": attempts - duplicate_residues == len(records),
        "all_direct_screens_classified": (
            sum(
                sign_counts[sign][kind]
                for sign in sign_counts
                for kind in sign_counts[sign]
            )
            == 2 * len(records)
        ),
        "advice_indices_valid": (
            indices_in_range
            and indices_distinct
            and indices_increasing
            and indices_end_at_stop
        ),
        "selected_support_crosses_layers": (
            provenance_split.get("frozen_seed_basis_pair", 0) > 0
            and provenance_split.get("nonadaptive_seed_pair", 0) > 0
        ),
        "selected_product_is_exact_square": product_is_square,
        "root_squares_to_one_mod_N": root_square_mod_N == 1,
        "root_is_non_global": not root_is_global,
        "terminal_gcd_exposes_proper_divisor": bool(terminal_proper),
        "no_decomposition_or_primality_routine_used": True,
        "index_list_treated_only_as_post_generation_advice": True,
    }
    failures = [name for name, passed in checks.items() if not passed]
    output = {
        "status": "PASS" if not failures else "FAIL",
        "role": "proof-blind N-only verification of one fixed advised certificate",
        "isolation": {
            "files_read": ["RECONSTRUCT_STATEMENT.md", "RECONSTRUCT_INPUT.json"],
            "statement_sha256": statement_hash,
            "input_sha256": input_hash,
            "other_F111_files_read": [],
            "F98_F109_F110_files_read": [],
        },
        "public_input": {
            "N": modulus,
            "n": n,
            "bound": bound,
            "source_stop_relation_count": stop_count,
            "advice_index_count": len(selected_indices),
        },
        "checks": checks,
        "failures": failures,
        "trial_screen": {
            "range": [2, bound],
            "values_checked": bound - 1,
            "nonunit_gcds": nontrivial_trial_gcds,
        },
        "basis": {
            "block_list": [block for block, _ in basis],
            "operation_count_definitions": {
                "perfect_power_exponent_tests": "candidate exponents tested from bit_length down to 2 during work-stack processing",
                "basis_gcd_tests": "ordered basis entries scanned during work-stack processing",
                "generated_stack_pushes": "items pushed after the initial endpoint stack",
            },
            "operation_counts": basis_stats,
            "signature_sha256": basis_signature_digest.hexdigest(),
            "seed_supports": seed_supports,
            "frozen_pair_list": [list(pair) for pair in ordered_frozen_pairs],
        },
        "source_trace": {
            "seed_record_count": seed_relation_count,
            "frozen_record_count": frozen_record_count,
            "frozen_attempt_count": frozen_attempt_count,
            "frozen_duplicate_count": frozen_duplicate_count,
            "stop_record_count": len(records),
            "total_attempt_count": attempts,
            "total_duplicate_count": duplicate_residues,
            "stop_provenance": stop_provenance,
            "record_trace_sha256": hash_record_trace(records),
        },
        "direct_sign_screens": {
            "counts": sign_counts,
            "proper_screen_count": len(proper_screens),
            "proper_screens": proper_screens,
            "nonunit_improper_screen_count": len(improper_screens),
            "nonunit_improper_screens": improper_screens,
            "improper_explanation": "minus gcd N means c=w; plus gcd N means c+w=N because 1<=c,w<N",
        },
        "advised_support": {
            "indices_in_range": indices_in_range,
            "indices_distinct": indices_distinct,
            "indices_strictly_increasing": indices_increasing,
            "last_index_is_final_record": indices_end_at_stop,
            "index_count": len(selected_indices),
            "index_sequence_sha256": hash_uint_sequence(selected_indices),
            "provenance_split": provenance_split,
            "crosses_frozen_and_appended_layers": checks[
                "selected_support_crosses_layers"
            ],
            "selected_appended_pairs": selected_appended_pairs,
            "selected_exact_values_are_distinct": len(selected_values)
            == len(set(selected_values)),
            "selected_exact_value_sequence_sha256": hash_uint_sequence(selected_values),
        },
        "exact_square_certificate": {
            "selected_product_is_square": product_is_square,
            "selected_product_bit_length": selected_product.bit_length(),
            "selected_product_byte_length": max(
                1, (selected_product.bit_length() + 7) // 8
            ),
            "selected_product_canonical_sha256": hash_uint(selected_product),
            "positive_root_bit_length": positive_root.bit_length(),
            "positive_root_byte_length": max(1, (positive_root.bit_length() + 7) // 8),
            "positive_root_canonical_sha256": hash_uint(positive_root),
            "canonical_encoding": "8-byte unsigned big-endian payload length followed by minimal unsigned big-endian payload",
            "selected_product_mod_N": selected_product % modulus,
            "root_mod_N": root_mod_N,
            "root_square_mod_N": root_square_mod_N,
            "root_is_global_plus_or_minus_one": root_is_global,
            "gcd_root_minus_one_N": terminal_minus,
            "gcd_root_plus_one_N": terminal_plus,
            "proper_terminal_divisors": terminal_proper,
        },
        "factor_free_boundary": {
            "allowed_operations_used": [
                "exact integer arithmetic",
                "modular exponentiation",
                "modular inverse",
                "gcd",
                "exact perfect-power extraction",
                "integer square root",
                "SHA-256",
            ],
            "forbidden_operations_used": [],
            "general_integer_factorization_used": False,
            "endpoint_prime_factorization_used": False,
            "primality_testing_used": False,
            "known_divisors_of_N_used": False,
        },
        "advice_boundary": {
            "index_list_is_external_advice": True,
            "source_generation_uses_index_list": False,
            "certificate_verification_uses_index_list": True,
            "selector_constructed": False,
            "probability_law_claimed": False,
            "all_input_algorithm_claimed": False,
            "narrow_claim": "the supplied fixed indices verify one factor-revealing cross-layer certificate for this N",
        },
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
