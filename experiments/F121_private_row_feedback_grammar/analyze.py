#!/usr/bin/env python3
"""Registered exact replay for the F121 N=4033 feedback comparison."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import time


N = 4033
N_BITS = 12
BOUND = 144
Q = 2017


def canonical_uint(value: int) -> bytes:
    payload = value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big")
    return len(payload).to_bytes(8, "big") + payload


def hash_uint(value: int) -> str:
    return hashlib.sha256(canonical_uint(value)).hexdigest()


def hash_uint_sequence(values) -> str:
    values = list(values)
    digest = hashlib.sha256(len(values).to_bytes(8, "big"))
    for value in values:
        digest.update(canonical_uint(int(value)))
    return digest.hexdigest()


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1 if divisor == 2 else 2
    return True


def factor_integer(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


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


def largest_perfect_power(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_nth_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def deterministic_seed_basis(
    endpoints: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    work = [(value, {index: 1}) for index, value in enumerate(endpoints) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = {
        "initial_items": len(work),
        "work_pops": 0,
        "gcd_tests": 0,
        "perfect_power_extractions": 0,
        "equal_merges": 0,
        "unequal_splits": 0,
    }
    while work:
        value, signature = work.pop()
        stats["work_pops"] += 1
        if value == 1:
            continue
        root, power = largest_perfect_power(value)
        if power > 1:
            value = root
            signature = {
                endpoint: power * multiplicity
                for endpoint, multiplicity in signature.items()
            }
            stats["perfect_power_extractions"] += 1
        for position, (old_value, old_signature) in enumerate(basis):
            stats["gcd_tests"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            basis.pop(position)
            if value == old_value:
                merged = dict(signature)
                for endpoint, multiplicity in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + multiplicity
                work.append((value, merged))
                stats["equal_merges"] += 1
            else:
                work.extend(
                    (
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, old_signature),
                        (old_value // divisor, old_signature),
                    )
                )
                stats["unequal_splits"] += 1
            break
        else:
            basis.append((value, signature))

    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoints)
    for position, (block, signature) in enumerate(basis):
        assert largest_perfect_power(block)[1] == 1
        assert all(math.gcd(block, prior) == 1 for prior, _ in basis[:position])
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= block**multiplicity
    assert reconstructed == endpoints
    stats["final_blocks"] = len(basis)
    stats["signature_entries"] = sum(len(signature) for _, signature in basis)
    return basis, stats


def frozen_pairs_from_basis(
    basis: list[tuple[int, dict[int, int]]], relation_count: int
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    pairs = []
    supports = []
    for relation in range(relation_count):
        support = [
            block
            for block, signature in basis
            if signature.get(2 * relation, 0)
            + signature.get(2 * relation + 1, 0)
            > 0
        ]
        assert support
        supports.append(support)
        pairs.append((support[0], 1) if len(support) == 1 else (support[0], support[1]))
    return pairs, supports


def complete_binary_kernel(rows: list[int], columns: int) -> tuple[int, list[int]]:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    kernel = []
    for free_column in range(columns):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        assert all((row & vector).bit_count() % 2 == 0 for row in rows)
        kernel.append(vector)
    assert len(pivots) + len(kernel) == columns
    return len(pivots), kernel


def analyze_matrix(records: list[dict[str, object]]) -> dict[str, object]:
    values = [int(record["P"]) for record in records]
    row_masks: dict[int, int] = {}
    factorizations = []
    for column, value in enumerate(values):
        factors = factor_integer(value)
        factorizations.append(factors)
        for prime, exponent in factors.items():
            if exponent & 1:
                row_masks[prime] = row_masks.get(prime, 0) | (1 << column)
    rank, kernel = complete_binary_kernel(list(row_masks.values()), len(values))
    roots = []
    proper_divisors = set()
    for basis_index, vector in enumerate(kernel):
        selected = []
        bits = vector
        while bits:
            low = bits & -bits
            selected.append(low.bit_length() - 1)
            bits ^= low
        product = math.prod(values[column] for column in selected)
        root = math.isqrt(product)
        assert root * root == product
        residue = root % N
        assert residue * residue % N == 1
        minus = math.gcd(root - 1, N)
        plus = math.gcd(root + 1, N)
        proper = sorted(divisor for divisor in {minus, plus} if 1 < divisor < N)
        proper_divisors.update(proper)
        roots.append(
            {
                "basis_index": basis_index,
                "support": len(selected),
                "vector_sha256": hash_uint(vector),
                "product_bit_length": product.bit_length(),
                "product_sha256": hash_uint(product),
                "root_mod_N": residue,
                "root_is_global_plus": residue == 1,
                "root_is_global_minus": residue == N - 1,
                "root_is_non_global": residue not in (1, N - 1),
                "gcd_root_minus_one_N": minus,
                "gcd_root_plus_one_N": plus,
                "proper_divisors": proper,
            }
        )
    return {
        "column_count": len(values),
        "prime_row_count": len(row_masks),
        "rank": rank,
        "nullity": len(kernel),
        "kernel_basis_sha256": hash_uint_sequence(kernel),
        "global_plus_basis_roots": sum(row["root_is_global_plus"] for row in roots),
        "global_minus_basis_roots": sum(row["root_is_global_minus"] for row in roots),
        "non_global_basis_roots": sum(row["root_is_non_global"] for row in roots),
        "proper_divisors": sorted(proper_divisors),
        "basis_roots": roots,
        "factorizations": factorizations,
    }


def q_valuation(value: int) -> int:
    valuation = 0
    while value % Q == 0:
        value //= Q
        valuation += 1
    return valuation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()

    assert N.bit_length() == N_BITS
    assert BOUND == N_BITS * N_BITS
    assert N == 2 * Q - 1
    assert is_prime(Q)
    assert pow(2, -1, N) == Q

    trial_nonunits = []
    for trial in range(2, BOUND + 1):
        divisor = math.gcd(trial, N)
        if divisor != 1:
            trial_nonunits.append({"trial": trial, "gcd": divisor})
    first_trial_proper = next(
        row for row in trial_nonunits if 1 < row["gcd"] < N
    )

    seen_residues: set[int] = set()
    raw_records: list[dict[str, object]] = []
    attempted_positions = 0
    duplicate_residues = 0
    direct_proper = []
    direct_improper = []

    def attempt(c: int, provenance: dict[str, object]) -> None:
        nonlocal attempted_positions, duplicate_residues
        attempted_positions += 1
        assert 0 <= c < N
        if c in seen_residues:
            duplicate_residues += 1
            return
        seen_residues.add(c)
        assert math.gcd(c, N) == 1
        w = pow(c, -1, N)
        relation_value = c * w
        assert relation_value % N == 1
        raw_index = len(raw_records)
        raw_records.append(
            {"c": c, "w": w, "P": relation_value, "provenance": provenance}
        )
        for sign, signed in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(signed, N)
            if 1 < divisor < N:
                direct_proper.append(
                    {
                        "raw_index": raw_index,
                        "sign": sign,
                        "gcd": divisor,
                        "c": c,
                        "w": w,
                        "provenance": provenance,
                    }
                )
            elif divisor == N:
                direct_improper.append(
                    {
                        "raw_index": raw_index,
                        "sign": sign,
                        "c": c,
                        "w": w,
                        "provenance": provenance,
                    }
                )

    for seed in range(2, N_BITS + 1):
        attempt(seed, {"kind": "seed", "seed": seed})
    seed_count = len(raw_records)
    assert seed_count == N_BITS - 1
    seed_endpoints = [
        endpoint
        for record in raw_records[:seed_count]
        for endpoint in (int(record["c"]), int(record["w"]))
    ]
    seed_basis, seed_basis_stats = deterministic_seed_basis(seed_endpoints)
    frozen_pairs, seed_supports = frozen_pairs_from_basis(seed_basis, seed_count)

    frozen_attempt_start = attempted_positions
    for pair_index, (u, v) in enumerate(frozen_pairs):
        u_power = 1
        v_power = 1
        for exponent in range(BOUND + 1):
            attempt(
                u_power * v % N,
                {
                    "kind": "frozen",
                    "pair_index": pair_index,
                    "u": u,
                    "v": v,
                    "exponent": exponent,
                    "orientation": "u_power_v",
                },
            )
            attempt(
                u * v_power % N,
                {
                    "kind": "frozen",
                    "pair_index": pair_index,
                    "u": u,
                    "v": v,
                    "exponent": exponent,
                    "orientation": "u_v_power",
                },
            )
            u_power = u_power * u % N
            v_power = v_power * v % N
    frozen_attempts = attempted_positions - frozen_attempt_start

    all_pair_attempt_start = attempted_positions
    pair_index = 0
    for u in range(2, N_BITS):
        for v in range(u + 1, N_BITS + 1):
            u_power = 1
            v_power = 1
            for exponent in range(BOUND + 1):
                attempt(
                    u_power * v % N,
                    {
                        "kind": "all_pair",
                        "pair_index": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": "u_power_v",
                    },
                )
                attempt(
                    u * v_power % N,
                    {
                        "kind": "all_pair",
                        "pair_index": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": "u_v_power",
                    },
                )
                u_power = u_power * u % N
                v_power = v_power * v % N
            pair_index += 1
    all_pair_attempts = attempted_positions - all_pair_attempt_start

    expected_positions = (N_BITS - 1) + 2 * (BOUND + 1) * (
        (N_BITS - 1) + (N_BITS - 1) * (N_BITS - 2) // 2
    )
    assert attempted_positions == expected_positions
    assert attempted_positions == len(raw_records) + duplicate_residues

    exact_records: list[dict[str, object]] = []
    exact_first: dict[int, int] = {}
    unit_raw_count = 0
    repeated_exact_count = 0
    for raw_index, record in enumerate(raw_records):
        value = int(record["P"])
        if value == 1:
            unit_raw_count += 1
        elif value in exact_first:
            repeated_exact_count += 1
        else:
            exact_first[value] = len(exact_records)
            exact_records.append({**record, "raw_index": raw_index})
    assert len(exact_records) + unit_raw_count + repeated_exact_count == len(raw_records)

    static_matrix = analyze_matrix(exact_records)

    order_two = 1
    power = 2 % N
    while power != 1:
        power = power * 2 % N
        order_two += 1
        assert order_two <= N
    two_subgroup = {pow(2, exponent, N) for exponent in range(order_two)}

    feedback_candidates = []
    feedback_identity_checks = 0
    for a in range(2, N_BITS + 1):
        a_power = 1
        q_power = 1
        for exponent in range(BOUND + 1):
            first = a_power * Q % N
            second = a * q_power % N
            assert first == pow(a, exponent, N) * pow(2, -1, N) % N
            assert second == a * pow(2, -exponent, N) % N
            feedback_identity_checks += 2
            feedback_candidates.append(
                (
                    first,
                    {
                        "kind": "feedback",
                        "a": a,
                        "q": Q,
                        "exponent": exponent,
                        "orientation": "a_power_q",
                    },
                )
            )
            feedback_candidates.append(
                (
                    second,
                    {
                        "kind": "feedback",
                        "a": a,
                        "q": Q,
                        "exponent": exponent,
                        "orientation": "a_q_power",
                    },
                )
            )
            a_power = a_power * a % N
            q_power = q_power * Q % N

    promoted_seen = set(seen_residues)
    promoted_exact_first = dict(exact_first)
    promoted_records = list(exact_records)
    feedback_new_residues = []
    feedback_new_exact_values = []
    feedback_direct_proper = []
    for c, provenance in feedback_candidates:
        if c in promoted_seen:
            continue
        promoted_seen.add(c)
        assert math.gcd(c, N) == 1
        w = pow(c, -1, N)
        value = c * w
        feedback_new_residues.append(c)
        for sign, signed in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(signed, N)
            if 1 < divisor < N:
                feedback_direct_proper.append(
                    {
                        "sign": sign,
                        "gcd": divisor,
                        "c": c,
                        "w": w,
                        "provenance": provenance,
                    }
                )
        if value != 1 and value not in promoted_exact_first:
            promoted_exact_first[value] = len(promoted_records)
            feedback_new_exact_values.append(value)
            promoted_records.append(
                {"c": c, "w": w, "P": value, "provenance": provenance}
            )
    promoted_matrix = analyze_matrix(promoted_records)

    unit_residues = [c for c in range(1, N) if math.gcd(c, N) == 1]
    universe_values: dict[int, tuple[int, int]] = {}
    for c in unit_residues:
        w = pow(c, -1, N)
        value = c * w
        if value != 1 and value not in universe_values:
            universe_values[value] = (c, w)
    universe_q_odd = [
        {"P": value, "c": endpoints[0], "w": endpoints[1], "valuation": q_valuation(value)}
        for value, endpoints in universe_values.items()
        if q_valuation(value) & 1
    ]
    static_q_odd = [
        {
            "column": column,
            "P": int(record["P"]),
            "c": int(record["c"]),
            "w": int(record["w"]),
            "valuation": q_valuation(int(record["P"])),
        }
        for column, record in enumerate(exact_records)
        if q_valuation(int(record["P"])) & 1
    ]
    promoted_q_odd = [
        {
            "column": column,
            "P": int(record["P"]),
            "c": int(record["c"]),
            "w": int(record["w"]),
            "valuation": q_valuation(int(record["P"])),
        }
        for column, record in enumerate(promoted_records)
        if q_valuation(int(record["P"])) & 1
    ]

    c110 = 110
    w110 = pow(c110, -1, N)
    p110 = c110 * w110
    c110_column = exact_first[p110]
    c110_record = exact_records[c110_column]
    c110_root = math.isqrt(p110)
    c110_minus = math.gcd(c110_root - 1, N)
    c110_plus = math.gcd(c110_root + 1, N)
    c110_zero_parity = all(exponent % 2 == 0 for exponent in factor_integer(p110).values())

    q_seed_record = raw_records[0]
    q_exact_value = 2 * Q
    q_column = exact_first[q_exact_value]

    checks = {
        "fixed_dimensions": N.bit_length() == N_BITS and BOUND == N_BITS * N_BITS,
        "q_is_prime": is_prime(Q),
        "N_equals_2q_minus_1": N == 2 * Q - 1,
        "q_is_inverse_of_2": pow(2, -1, N) == Q,
        "seed_2_relation_is_2_times_q": q_seed_record["c"] == 2
        and q_seed_record["w"] == Q
        and q_seed_record["P"] == N + 1,
        "q_is_final_seed_basis_block": Q in [block for block, _ in seed_basis],
        "seed_2_frozen_pair_is_2_q": frozen_pairs[0] == (2, Q),
        "source_position_accounting": attempted_positions == expected_positions,
        "all_source_residues_are_units": len(raw_records) == len(seen_residues),
        "feedback_words_are_inverse_two_laurent_words": feedback_identity_checks
        == 2 * (N_BITS - 1) * (BOUND + 1),
        "static_q_row_is_private": len(static_q_odd) == 1
        and static_q_odd[0]["P"] == q_exact_value,
        "promoted_q_row_is_private": len(promoted_q_odd) == 1
        and promoted_q_odd[0]["P"] == q_exact_value,
        "universe_q_row_is_globally_private": len(universe_q_odd) == 1
        and universe_q_odd[0]["P"] == q_exact_value,
        "c110_is_non_global_square_root": w110 == c110
        and p110 == c110 * c110
        and c110 not in (1, N - 1)
        and c110 * c110 % N == 1,
        "c110_terminal_gcds_are_proper": 1 < c110_minus < N and 1 < c110_plus < N,
        "c110_column_has_zero_parity": c110_zero_parity,
        "static_matrix_has_CLOSE": static_matrix["nullity"] > 0,
        "static_matrix_has_ROOT": static_matrix["non_global_basis_roots"] > 0,
        "promoted_matrix_has_CLOSE": promoted_matrix["nullity"] > 0,
        "promoted_matrix_has_ROOT": promoted_matrix["non_global_basis_roots"] > 0,
    }
    failures = [name for name, passed in checks.items() if not passed]

    output = {
        "status": "PASS" if not failures else "FAIL",
        "fixed_input": {"N": N, "n": N_BITS, "B": BOUND, "q": Q},
        "checks": checks,
        "failures": failures,
        "elapsed_seconds": time.monotonic() - started,
        "arithmetic": {
            "N_factorization": factor_integer(N),
            "q_is_prime": is_prime(Q),
            "inverse_of_2": pow(2, -1, N),
            "order_of_2_mod_N": order_two,
            "two_subgroup_size": len(two_subgroup),
            "two_subgroup_fully_seen_by_static_source": two_subgroup <= seen_residues,
        },
        "trial_screen": {
            "range": [2, BOUND],
            "nonunit_count": len(trial_nonunits),
            "nonunits": trial_nonunits,
            "first_proper": first_trial_proper,
        },
        "seed_basis": {
            "blocks": [block for block, _ in seed_basis],
            "operation_counts": seed_basis_stats,
            "supports": seed_supports,
            "frozen_pairs": [list(pair) for pair in frozen_pairs],
            "seed_2_support": seed_supports[0],
            "seed_2_frozen_pair": list(frozen_pairs[0]),
        },
        "static_source": {
            "expected_positions": expected_positions,
            "attempted_positions": attempted_positions,
            "seed_attempts": N_BITS - 1,
            "frozen_attempts": frozen_attempts,
            "all_pair_attempts": all_pair_attempts,
            "first_residue_count": len(raw_records),
            "duplicate_residue_count": duplicate_residues,
            "unit_raw_count": unit_raw_count,
            "repeated_exact_count": repeated_exact_count,
            "distinct_nonunit_exact_count": len(exact_records),
            "residue_sequence_sha256": hash_uint_sequence(
                int(record["c"]) for record in raw_records
            ),
            "exact_value_sequence_sha256": hash_uint_sequence(
                int(record["P"]) for record in exact_records
            ),
            "unit_group_size": len(unit_residues),
            "unit_residue_coverage_count": len(seen_residues & set(unit_residues)),
            "missing_unit_count": len(set(unit_residues) - seen_residues),
            "missing_units": sorted(set(unit_residues) - seen_residues),
            "proper_direct_screen_count": len(direct_proper),
            "proper_direct_screens": direct_proper,
            "improper_direct_screen_count": len(direct_improper),
            "improper_direct_screens": direct_improper,
        },
        "q_row": {
            "q": Q,
            "protected_exact_value": q_exact_value,
            "protected_column": q_column,
            "static_odd_row_occurrences": static_q_odd,
            "promoted_odd_row_occurrences": promoted_q_odd,
            "full_canonical_unit_universe_distinct_exact_count": len(universe_values),
            "full_canonical_unit_universe_odd_row_occurrences": universe_q_odd,
        },
        "one_step_feedback": {
            "declared_part": "pair (2,q) is already the seed-2 frozen pair",
            "hypothetical_part": "pairs (a,q) for every seed a=2..n",
            "candidate_attempt_count": len(feedback_candidates),
            "distinct_candidate_residue_count": len(
                {candidate for candidate, _ in feedback_candidates}
            ),
            "inverse_two_identity_checks": feedback_identity_checks,
            "new_first_residue_count": len(feedback_new_residues),
            "new_first_residues": feedback_new_residues,
            "new_first_residue_sequence_sha256": hash_uint_sequence(
                feedback_new_residues
            ),
            "new_distinct_exact_value_count": len(feedback_new_exact_values),
            "new_distinct_exact_values": feedback_new_exact_values,
            "new_exact_value_sequence_sha256": hash_uint_sequence(
                feedback_new_exact_values
            ),
            "proper_direct_screen_count_on_new_residues": len(feedback_direct_proper),
            "proper_direct_screens_on_new_residues": feedback_direct_proper,
        },
        "c110_declared_witness": {
            "c": c110,
            "inverse": w110,
            "P": p110,
            "exact_column": c110_column,
            "first_record": c110_record,
            "root_mod_N": c110_root,
            "root_square_mod_N": c110_root * c110_root % N,
            "gcd_root_minus_one_N": c110_minus,
            "gcd_root_plus_one_N": c110_plus,
            "zero_parity_column": c110_zero_parity,
            "named_pair": [10, 11],
            "named_exponent": 1,
            "is_feedback_witness": False,
        },
        "static_matrix": static_matrix,
        "promoted_matrix": promoted_matrix,
        "boundary": {
            "mathematical_no_stop_source_replayed": True,
            "operational_source_would_stop_in_trial_screen": True,
            "feedback_layer_is_not_declared_F116": True,
            "factorization_used_only_in_registered_small_replay": True,
            "general_CLOSE_claimed": False,
            "general_ROOT_claimed": False,
        },
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
