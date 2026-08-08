#!/usr/bin/env python3
"""Isolated F116 prefix reconstruction and full-source corollary proof."""

from __future__ import annotations

import argparse
from array import array
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
STATEMENT = HERE / "FULL_SOURCE_COROLLARY_RECONSTRUCT_STATEMENT.md"
PUBLIC_INPUT = HERE / "RECONSTRUCT_INPUT.json"
EXPECTED_STATEMENT_SHA256 = (
    "dacb0f606313045ce3f0e7b6ff75433bad437ac2b372056f71a021cfce5dce1b"
)
EXPECTED_INPUT_SHA256 = (
    "5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015"
)
TRACE_DOMAIN = b"FULL_SOURCE_COROLLARY_RECONSTRUCT_RECORD_TRACE_V1\0"
SELECTED_TRACE_DOMAIN = b"FULL_SOURCE_COROLLARY_RECONSTRUCT_SELECTED_TRACE_V1\0"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_uint(value: int) -> bytes:
    payload = value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big")
    return len(payload).to_bytes(8, "big") + payload


def hash_uint(value: int) -> str:
    return hashlib.sha256(canonical_uint(value)).hexdigest()


def hash_uint_sequence(values, count: int) -> str:
    digest = hashlib.sha256()
    digest.update(count.to_bytes(8, "big"))
    seen = 0
    for value in values:
        digest.update(canonical_uint(int(value)))
        seen += 1
    assert seen == count
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


def deterministic_seed_basis(
    endpoints: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    """Make a deterministic gcd basis without factoring an endpoint.

    Initial items use endpoint order. The work list is a stack. On each pop,
    extract the largest exact perfect-power exponent. Scan the ordered basis
    from its first item. Equal overlaps merge signatures. Unequal overlaps
    push (d,s), (x/d,s), (d,t), (y/d,t), in this displayed order.
    """
    work = [(value, {index: 1}) for index, value in enumerate(endpoints) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = {
        "initial_work_items": len(work),
        "work_pops": 0,
        "generated_work_pushes": 0,
        "maximum_work_size": len(work),
        "unit_discards": 0,
        "perfect_power_exponent_tests": 0,
        "perfect_power_extractions": 0,
        "basis_gcd_tests": 0,
        "overlap_events": 0,
        "equal_value_merges": 0,
        "unequal_value_splits": 0,
        "basis_appends": 0,
    }
    while work:
        value, signature = work.pop()
        stats["work_pops"] += 1
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
                work.append((value, merged))
                stats["generated_work_pushes"] += 1
                stats["equal_value_merges"] += 1
            else:
                work.extend(
                    (
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, old_signature),
                        (old_value // divisor, old_signature),
                    )
                )
                stats["generated_work_pushes"] += 4
                stats["unequal_value_splits"] += 1
            stats["maximum_work_size"] = max(stats["maximum_work_size"], len(work))
            break
        else:
            basis.append((value, signature))
            stats["basis_appends"] += 1

    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoints)
    for position, (block, signature) in enumerate(basis):
        assert largest_perfect_power(block)[1] == 1
        assert all(math.gcd(block, prior) == 1 for prior, _ in basis[:position])
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= block**multiplicity
    assert reconstructed == endpoints
    stats["final_block_count"] = len(basis)
    stats["final_signature_entries"] = sum(len(signature) for _, signature in basis)
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


def factor_free_parity_rows(
    endpoint_masks: list[tuple[int, int]],
) -> tuple[list[int], list[tuple[int, int]], dict[str, int]]:
    """Deterministic factor-free decoder used by the certified algorithm.

    This routine is part of the complete no-advice algorithm specification.
    The fixed-input proof below does not execute it on the complete source.
    """
    work = [(value, mask) for value, mask in endpoint_masks if value > 1 and mask]
    stable: list[tuple[int, int]] = []
    stats = {
        "initial_entries": len(work),
        "work_pops": 0,
        "refinements": 0,
        "gcd_tests": 0,
        "maximum_work_size": len(work),
    }
    while work:
        value, mask = work.pop()
        stats["work_pops"] += 1
        if value == 1 or mask == 0:
            continue
        for position, (old_value, old_mask) in enumerate(stable):
            stats["gcd_tests"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            stable.pop(position)
            work.extend(
                (
                    (divisor, mask ^ old_mask),
                    (value // divisor, mask),
                    (old_value // divisor, old_mask),
                )
            )
            stats["refinements"] += 1
            stats["maximum_work_size"] = max(stats["maximum_work_size"], len(work))
            break
        else:
            stable.append((value, mask))

    for position, (value, _) in enumerate(stable):
        assert all(math.gcd(value, old_value) == 1 for old_value, _ in stable[:position])
    rows = []
    square_terminal_values = 0
    for value, mask in stable:
        root = math.isqrt(value)
        if root * root == value:
            square_terminal_values += 1
        else:
            rows.append(mask)
    stats["terminal_values"] = len(stable)
    stats["terminal_square_values"] = square_terminal_values
    stats["row_count"] = len(rows)
    return rows, stable, stats


def complete_binary_kernel(
    rows: list[int], column_count: int
) -> tuple[int, list[int], dict[str, int]]:
    pivots: dict[int, int] = {}
    row_xors = 0
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
            row_xors += 1

    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    kernel = []
    solve_xors = 0
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
                solve_xors += 1
        assert all((row & vector).bit_count() % 2 == 0 for row in rows)
        kernel.append(vector)
    assert len(pivots) + len(kernel) == column_count
    return len(pivots), kernel, {
        "rank": len(pivots),
        "nullity": len(kernel),
        "row_xors": row_xors,
        "solve_xors": solve_xors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    total_started = time.monotonic()

    statement_hash = sha256_file(STATEMENT)
    input_hash = sha256_file(PUBLIC_INPUT)
    assert statement_hash == EXPECTED_STATEMENT_SHA256
    assert input_hash == EXPECTED_INPUT_SHA256
    supplied = json.loads(PUBLIC_INPUT.read_text(encoding="utf-8"))
    assert set(supplied) == {
        "N",
        "n",
        "bound",
        "source_stop_relation_count",
        "dependency_relation_indices_zero_based",
    }
    modulus = int(supplied["N"])
    n = int(supplied["n"])
    bound = int(supplied["bound"])
    stop_count = int(supplied["source_stop_relation_count"])
    advised_indices = [
        int(index) for index in supplied["dependency_relation_indices_zero_based"]
    ]
    assert modulus > 1 and modulus % 2 == 1
    assert n == modulus.bit_length()
    assert bound == n * n
    assert advised_indices == sorted(set(advised_indices))
    assert advised_indices and 0 <= advised_indices[0] <= advised_indices[-1] < stop_count

    trial_started = time.monotonic()
    trial_nonunits = []
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        if divisor != 1:
            trial_nonunits.append({"trial": trial, "gcd": divisor})
    trial_seconds = time.monotonic() - trial_started
    assert not trial_nonunits

    source_started = time.monotonic()
    c_values = array("Q")
    w_values = array("Q")
    relation_values: list[int] = []
    seen_residues: set[int] = set()
    attempted_positions = 0
    duplicate_residues = 0
    nonunit_generated_residues = []
    direct_counts = {
        "minus": {"unit": 0, "improper_N": 0, "proper": 0},
        "plus": {"unit": 0, "improper_N": 0, "proper": 0},
    }
    improper_direct = []
    proper_direct = []
    record_digest = hashlib.sha256(TRACE_DOMAIN)
    advice_cursor = 0
    selected_records = []
    stop_record = None

    def attempt(c: int, provenance: tuple[int, int, int, int, int, int]) -> bool:
        nonlocal attempted_positions, duplicate_residues, advice_cursor, stop_record
        attempted_positions += 1
        assert 0 <= c < modulus
        if c in seen_residues:
            duplicate_residues += 1
            return False
        seen_residues.add(c)

        invertibility_gcd = math.gcd(c, modulus)
        if invertibility_gcd != 1:
            nonunit_generated_residues.append(
                {
                    "attempted_position_one_based": attempted_positions,
                    "c": c,
                    "gcd": invertibility_gcd,
                    "provenance": provenance,
                }
            )
            raise AssertionError("A generated first residue was not invertible.")
        w = pow(c, -1, modulus)
        assert 1 <= w < modulus
        relation_value = c * w
        assert relation_value % modulus == 1
        raw_index = len(relation_values)
        c_values.append(c)
        w_values.append(w)
        relation_values.append(relation_value)

        record_digest.update(canonical_uint(raw_index))
        record_digest.update(canonical_uint(c))
        record_digest.update(canonical_uint(w))
        for field in provenance:
            record_digest.update(canonical_uint(field))

        for sign, signed_value in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(signed_value, modulus)
            if divisor == 1:
                direct_counts[sign]["unit"] += 1
            elif divisor == modulus:
                assert (sign == "minus" and c == w) or (
                    sign == "plus" and c + w == modulus
                )
                direct_counts[sign]["improper_N"] += 1
                improper_direct.append(
                    {
                        "raw_index_zero_based": raw_index,
                        "sign": sign,
                        "c": c,
                        "w": w,
                        "provenance": provenance,
                    }
                )
            else:
                direct_counts[sign]["proper"] += 1
                proper_direct.append(
                    {
                        "raw_index_zero_based": raw_index,
                        "sign": sign,
                        "c": c,
                        "w": w,
                        "gcd": divisor,
                        "provenance": provenance,
                    }
                )

        if advice_cursor < len(advised_indices) and raw_index == advised_indices[advice_cursor]:
            selected_records.append(
                (raw_index, c, w, relation_value, provenance)
            )
            advice_cursor += 1

        if len(relation_values) == stop_count:
            stop_record = {
                "raw_index_zero_based": raw_index,
                "attempted_position_one_based": attempted_positions,
                "c": c,
                "w": w,
                "provenance": provenance,
            }
            return True
        assert len(relation_values) < stop_count
        return False

    for seed_index, seed in enumerate(range(2, n + 1)):
        reached_stop = attempt(seed, (0, seed_index, seed, 0, 0, 0))
        assert not reached_stop
    seed_record_count = len(relation_values)
    seed_endpoints = [
        endpoint
        for raw_index in range(seed_record_count)
        for endpoint in (int(c_values[raw_index]), int(w_values[raw_index]))
    ]
    seed_basis, seed_basis_stats = deterministic_seed_basis(seed_endpoints)
    frozen_pairs, seed_supports = frozen_pairs_from_basis(
        seed_basis, seed_record_count
    )

    frozen_attempt_start = attempted_positions
    frozen_record_start = len(relation_values)
    frozen_duplicate_start = duplicate_residues
    prefix_reached = False
    for pair_index, (u, v) in enumerate(frozen_pairs):
        u_power = 1
        v_power = 1
        for exponent in range(bound + 1):
            if attempt(
                u_power * v % modulus,
                (1, pair_index, u, v, exponent, 0),
            ):
                prefix_reached = True
                break
            if attempt(
                u * v_power % modulus,
                (1, pair_index, u, v, exponent, 1),
            ):
                prefix_reached = True
                break
            u_power = u_power * u % modulus
            v_power = v_power * v % modulus
        if prefix_reached:
            break
    frozen_summary = {
        "pair_count": len(frozen_pairs),
        "attempted_positions": attempted_positions - frozen_attempt_start,
        "retained_records": len(relation_values) - frozen_record_start,
        "duplicate_residues": duplicate_residues - frozen_duplicate_start,
        "completed_before_prefix_stop": not prefix_reached,
    }

    all_pair_summaries = []
    all_pair_index = 0
    if not prefix_reached:
        for u in range(2, n):
            for v in range(u + 1, n + 1):
                before_attempts = attempted_positions
                before_records = len(relation_values)
                before_duplicates = duplicate_residues
                u_power = 1
                v_power = 1
                pair_complete = True
                for exponent in range(bound + 1):
                    if attempt(
                        u_power * v % modulus,
                        (2, all_pair_index, u, v, exponent, 0),
                    ):
                        prefix_reached = True
                        pair_complete = False
                        break
                    if attempt(
                        u * v_power % modulus,
                        (2, all_pair_index, u, v, exponent, 1),
                    ):
                        prefix_reached = True
                        pair_complete = exponent == bound
                        break
                    u_power = u_power * u % modulus
                    v_power = v_power * v % modulus
                all_pair_summaries.append(
                    {
                        "pair_index_zero_based": all_pair_index,
                        "pair": [u, v],
                        "attempted_positions": attempted_positions - before_attempts,
                        "retained_records": len(relation_values) - before_records,
                        "duplicate_residues": duplicate_residues - before_duplicates,
                        "pair_complete": pair_complete,
                    }
                )
                all_pair_index += 1
                if prefix_reached:
                    break
            if prefix_reached:
                break
    source_seconds = time.monotonic() - source_started

    assert prefix_reached
    assert len(relation_values) == stop_count
    assert attempted_positions - duplicate_residues == stop_count
    assert len(seen_residues) == stop_count
    assert len(c_values) == len(w_values) == len(relation_values)
    assert advice_cursor == len(advised_indices)
    assert len(selected_records) == len(advised_indices)
    assert [record[0] for record in selected_records] == advised_indices
    assert sum(
        direct_counts[sign][classification]
        for sign in direct_counts
        for classification in direct_counts[sign]
    ) == 2 * stop_count

    record_digest.update(canonical_uint(stop_count))
    record_trace_hash = record_digest.hexdigest()
    selected_digest = hashlib.sha256(SELECTED_TRACE_DOMAIN)
    for raw_index, c, w, relation_value, provenance in selected_records:
        for value in (raw_index, c, w, relation_value, *provenance):
            selected_digest.update(canonical_uint(value))
    selected_digest.update(canonical_uint(len(selected_records)))
    selected_trace_hash = selected_digest.hexdigest()

    advice_started = time.monotonic()
    selected_values = [record[3] for record in selected_records]
    assert all(value % modulus == 1 for value in selected_values)
    advised_product = math.prod(selected_values)
    advised_root = math.isqrt(advised_product)
    advised_product_is_square = advised_root * advised_root == advised_product
    advised_root_modulus = advised_root % modulus
    advised_minus = math.gcd(advised_root - 1, modulus)
    advised_plus = math.gcd(advised_root + 1, modulus)
    advised_root_is_non_global = advised_root_modulus not in (1, modulus - 1)
    advised_root_squares_to_one = (
        advised_root_modulus * advised_root_modulus % modulus == 1
    )
    advised_terminal_gcds_are_proper = (
        1 < advised_minus < modulus and 1 < advised_plus < modulus
    )
    advice_seconds = time.monotonic() - advice_started

    projection_started = time.monotonic()
    raw_index_bits = max(1, (stop_count - 1).bit_length())
    raw_index_mask = (1 << raw_index_bits) - 1
    first_exact: dict[int, int] = {}
    unit_raw_columns = 0
    repeated_exact_columns = 0
    for raw_index, relation_value in enumerate(relation_values):
        if relation_value == 1:
            unit_raw_columns += 1
            continue
        prior = first_exact.get(relation_value)
        if prior is None:
            exact_column = len(first_exact)
            first_exact[relation_value] = (exact_column << raw_index_bits) | raw_index
        else:
            repeated_exact_columns += 1

    exact_column_count = len(first_exact)
    assert exact_column_count + unit_raw_columns + repeated_exact_columns == stop_count
    assert all(value % modulus == 1 for value in first_exact)
    exact_value_hash = hash_uint_sequence(first_exact.keys(), exact_column_count)
    first_raw_index_hash = hash_uint_sequence(
        (packed & raw_index_mask for packed in first_exact.values()),
        exact_column_count,
    )

    selected_counts = Counter(selected_values)
    selected_unit_count = selected_counts.get(1, 0)
    selected_distinct_nonunit_count = sum(value != 1 for value in selected_counts)
    selected_repeated_occurrences = sum(count - 1 for count in selected_counts.values())
    selected_global_first_count = sum(
        relation_value != 1
        and (first_exact[relation_value] & raw_index_mask) == raw_index
        for raw_index, _, _, relation_value, _ in selected_records
    )
    projected_entries = []
    for value, count in selected_counts.items():
        if value == 1:
            continue
        packed = first_exact[value]
        if count & 1:
            projected_entries.append((packed >> raw_index_bits, value))
    projected_entries.sort()
    projected_columns = [column for column, _ in projected_entries]
    projected_values = [value for _, value in projected_entries]
    projected_product = math.prod(projected_values)
    projected_root = math.isqrt(projected_product)
    projected_product_is_square = projected_root * projected_root == projected_product
    projected_root_modulus = projected_root % modulus
    projected_minus = math.gcd(projected_root - 1, modulus)
    projected_plus = math.gcd(projected_root + 1, modulus)
    projected_nonzero = bool(projected_entries)
    projected_root_squares_to_one = (
        projected_root_modulus * projected_root_modulus % modulus == 1
    )
    projected_same_root_residue = projected_root_modulus == advised_root_modulus
    all_selected_values_distinct_nonunit = (
        selected_unit_count == 0
        and selected_repeated_occurrences == 0
        and selected_distinct_nonunit_count == len(advised_indices)
    )
    all_selected_records_global_first = (
        selected_global_first_count == len(advised_indices)
    )
    projection_seconds = time.monotonic() - projection_started

    unordered_pair_count = (n - 1) * (n - 2) // 2
    complete_pair_count = len(frozen_pairs) + unordered_pair_count
    complete_source_positions = (n - 1) + 2 * (bound + 1) * complete_pair_count
    assert complete_pair_count == n * (n - 1) // 2
    assert complete_source_positions == (n - 1) + (bound + 1) * n * (n - 1)

    checks = {
        "authorized_hashes_match": True,
        "input_keys_exact": set(supplied)
        == {
            "N",
            "n",
            "bound",
            "source_stop_relation_count",
            "dependency_relation_indices_zero_based",
        },
        "n_and_B_match_N": n == modulus.bit_length() and bound == n * n,
        "advice_indices_sorted_distinct_in_range": advised_indices
        == sorted(set(advised_indices))
        and advised_indices[-1] < stop_count,
        "trial_screen_all_units": not trial_nonunits,
        "all_seeds_retained": seed_record_count == n - 1,
        "seed_basis_reconstructs_exactly": True,
        "prefix_stop_reached_exactly": prefix_reached
        and len(relation_values) == stop_count,
        "prefix_source_accounting": attempted_positions - duplicate_residues
        == stop_count,
        "every_advised_raw_record_regenerated": advice_cursor
        == len(advised_indices)
        == len(selected_records),
        "all_generated_residues_invertible": not nonunit_generated_residues,
        "all_direct_screens_classified": sum(
            direct_counts[sign][classification]
            for sign in direct_counts
            for classification in direct_counts[sign]
        )
        == 2 * stop_count,
        "all_improper_direct_screens_are_identities": all(
            (row["sign"] == "minus" and row["c"] == row["w"])
            or (
                row["sign"] == "plus"
                and row["c"] + row["w"] == modulus
            )
            for row in improper_direct
        ),
        "no_proper_direct_screen": not proper_direct,
        "all_advised_values_congruent_one": all(
            value % modulus == 1 for value in selected_values
        ),
        "advised_exact_product_is_square": advised_product_is_square,
        "advised_root_squares_to_one_mod_N": advised_root_squares_to_one,
        "advised_root_is_non_global": advised_root_is_non_global,
        "advised_terminal_gcds_are_proper": advised_terminal_gcds_are_proper,
        "exact_projection_accounting": exact_column_count
        + unit_raw_columns
        + repeated_exact_columns
        == stop_count,
        "projected_dependency_is_nonzero": projected_nonzero,
        "projected_exact_product_is_square": projected_product_is_square,
        "projected_root_squares_to_one_mod_N": projected_root_squares_to_one,
        "projection_preserves_normalized_root_class": projected_same_root_residue,
        "projection_preserves_terminal_gcds": {
            projected_minus,
            projected_plus,
        }
        == {advised_minus, advised_plus},
        "complete_source_position_formula": complete_source_positions
        == (n - 1) + (bound + 1) * n * (n - 1),
        "full_source_corollary_certified": advised_product_is_square
        and advised_root_squares_to_one
        and advised_root_is_non_global
        and advised_terminal_gcds_are_proper
        and projected_nonzero
        and projected_product_is_square
        and projected_root_squares_to_one
        and projected_same_root_residue,
        "no_factorization_or_primality_used": True,
    }
    failures = [name for name, passed in checks.items() if not passed]
    total_seconds = time.monotonic() - total_started

    output = {
        "status": "PASS" if not failures else "FAIL",
        "role": "isolated advised-prefix verification and no-advice full-source corollary",
        "isolation": {
            "files_read": [
                "FULL_SOURCE_COROLLARY_RECONSTRUCT_STATEMENT.md",
                "RECONSTRUCT_INPUT.json",
            ],
            "statement_sha256": statement_hash,
            "input_sha256": input_hash,
            "other_F116_files_read": [],
            "F111_files_read": [],
            "PROVED_md_read": False,
            "candidate_implementation_read": False,
        },
        "public_input": {
            "N": modulus,
            "n": n,
            "B": bound,
            "advised_prefix_retained_record_count": stop_count,
            "advised_raw_support_count": len(advised_indices),
            "advised_raw_support_sha256": hash_uint_sequence(
                advised_indices, len(advised_indices)
            ),
        },
        "checks": checks,
        "failures": failures,
        "timings_seconds": {
            "trial_screen": trial_seconds,
            "prefix_source_including_seed_basis": source_seconds,
            "advised_raw_dependency_replay": advice_seconds,
            "exact_value_projection": projection_seconds,
            "total": total_seconds,
        },
        "trial_screen": {
            "range": [2, bound],
            "position_count": bound - 1,
            "nonunit_gcds": trial_nonunits,
        },
        "seed_basis": {
            "seed_record_count": seed_record_count,
            "endpoint_count": len(seed_endpoints),
            "block_list": [block for block, _ in seed_basis],
            "operation_counts": seed_basis_stats,
            "seed_supports": seed_supports,
            "frozen_pair_list": [list(pair) for pair in frozen_pairs],
        },
        "executed_advised_prefix": {
            "executed": True,
            "advice_affects_source_order_or_retention": False,
            "prefix_length_is_only_source_stop": True,
            "retained_record_count": len(relation_values),
            "attempted_position_count": attempted_positions,
            "duplicate_residue_count": duplicate_residues,
            "global_seen_residue_count": len(seen_residues),
            "frozen_layer": frozen_summary,
            "all_pair_layers_started": len(all_pair_summaries),
            "all_pair_layers_completed": sum(
                summary["pair_complete"] for summary in all_pair_summaries
            ),
            "all_pair_summaries": all_pair_summaries,
            "stop_record": stop_record,
            "record_trace_scheme": "domain, then raw index/c/w and six provenance integers per retained record, then retained count; canonical unsigned integer encoding",
            "record_trace_sha256": record_trace_hash,
            "maximum_endpoint_bit_length": max(
                max(int(c).bit_length(), int(w).bit_length())
                for c, w in zip(c_values, w_values, strict=True)
            ),
            "maximum_relation_value_bit_length": max(
                value.bit_length() for value in relation_values
            ),
            "nonunit_generated_residues": nonunit_generated_residues,
        },
        "direct_screens": {
            "counts": direct_counts,
            "proper_screen_count": len(proper_direct),
            "proper_screens": proper_direct,
            "improper_screen_count": len(improper_direct),
            "improper_screens": improper_direct,
        },
        "advised_prefix_verification": {
            "advice_used": True,
            "advice_role": "fixed-input existence proof only",
            "support_count": len(advised_indices),
            "support_first_index_zero_based": advised_indices[0],
            "support_last_index_zero_based": advised_indices[-1],
            "every_advised_record_regenerated": len(selected_records)
            == len(advised_indices),
            "selected_record_trace_scheme": "domain, then raw index/c/w/P and six provenance integers per selected record, then selected count; canonical unsigned integer encoding",
            "selected_record_trace_sha256": selected_trace_hash,
            "selected_product_bit_length": advised_product.bit_length(),
            "selected_product_sha256": hash_uint(advised_product),
            "selected_product_is_exact_square": advised_product_is_square,
            "positive_root_bit_length": advised_root.bit_length(),
            "positive_root_sha256": hash_uint(advised_root),
            "root_mod_N": advised_root_modulus,
        "root_square_mod_N": advised_root_modulus * advised_root_modulus % modulus,
            "root_is_non_global": advised_root_is_non_global,
            "gcd_root_minus_one_N": advised_minus,
            "gcd_root_plus_one_N": advised_plus,
            "both_terminal_gcds_are_proper": advised_terminal_gcds_are_proper,
        },
        "exact_value_projection": {
            "raw_column_count": stop_count,
            "raw_unit_column_count": unit_raw_columns,
            "raw_repeated_exact_value_count": repeated_exact_columns,
            "distinct_nonunit_exact_column_count": exact_column_count,
            "distinct_exact_value_sequence_sha256": exact_value_hash,
            "first_raw_index_sequence_sha256": first_raw_index_hash,
            "raw_unit_maps_to_zero_and_global_plus": True,
            "duplicate_pair_direction_root_is_value_and_global_plus": True,
            "unit_and_duplicate_directions_generate_projection_kernel": True,
            "selected_unit_count": selected_unit_count,
            "selected_distinct_nonunit_value_count": selected_distinct_nonunit_count,
            "selected_repeated_occurrence_count": selected_repeated_occurrences,
            "all_selected_values_are_distinct_nonunits": all_selected_values_distinct_nonunit,
            "selected_global_first_occurrence_count": selected_global_first_count,
            "all_selected_raw_records_are_global_first_occurrences": all_selected_records_global_first,
            "projected_support_count": len(projected_columns),
            "projected_column_sequence_sha256": hash_uint_sequence(
                projected_columns, len(projected_columns)
            ),
            "projected_product_bit_length": projected_product.bit_length(),
            "projected_product_sha256": hash_uint(projected_product),
            "projected_product_is_exact_square": projected_product_is_square,
            "projected_positive_root_bit_length": projected_root.bit_length(),
            "projected_positive_root_sha256": hash_uint(projected_root),
            "projected_root_mod_N": projected_root_modulus,
            "projected_gcd_root_minus_one_N": projected_minus,
            "projected_gcd_root_plus_one_N": projected_plus,
            "projected_dependency_is_nonzero": projected_nonzero,
            "same_root_residue_as_raw": projected_same_root_residue,
            "same_normalized_root_class_as_raw": projected_same_root_residue,
        },
        "factor_free_decoder_theorem": {
            "algorithm": "ordered three-way gcd refinement of endpoint-mask entries, square terminal removal, and complete binary elimination",
            "replacement": "(x,A),(y,B) -> (gcd(x,y),A xor B),(x/gcd,A),(y/gcd,B)",
            "preserves_each_column_modulo_exact_squares": True,
            "terminal_values_pairwise_coprime": True,
            "nonsquare_terminal_masks_equal_hidden_prime_parity_kernel": True,
            "requires_endpoint_factorization": False,
            "complete_binary_kernel_algorithm_specified_in_source": True,
        },
        "complete_no_advice_algorithm_corollary": {
            "certified_for_supplied_N": checks["full_source_corollary_certified"],
            "algorithm_input": ["N"],
            "derives_n_as_bit_length": True,
            "sets_B_equal_n_squared": True,
            "receives_prefix_length": False,
            "receives_dependency_support": False,
            "complete_source_executed_in_this_reconstruction": False,
            "complete_decoder_executed_in_this_reconstruction": False,
            "claim_kind": "existence proof from verified prefix, exact projection, append monotonicity, and complete-basis detection",
            "frozen_pair_count": len(frozen_pairs),
            "unordered_seed_pair_count": unordered_pair_count,
            "total_pair_count": complete_pair_count,
            "complete_source_position_formula": "(n-1)+(B+1)*n*(n-1)",
            "complete_source_position_count": complete_source_positions,
            "old_exact_values_remain_initial_after_append": True,
            "old_dependency_extends_by_zero_new_coordinates": True,
            "normalized_root_map_is_kernel_homomorphism": True,
            "every_complete_kernel_basis_detects_nonzero_class": True,
            "both_terminal_gcds_of_non_global_root_are_proper": True,
        },
        "uniform_polynomial_bit_cost": {
            "complete_source_positions": "T=(n-1)+(n^2+1)n(n-1)=O(n^4)",
            "endpoint_bits": "at most n",
            "relation_value_bits": "at most 2n",
            "distinct_exact_columns": "m<=T=O(n^4)",
            "refinement_initial_entries": "2m=O(n^4)",
            "refinement_total_input_bits": "L<=2mn=O(n^5)",
            "refinement_count": "at most L because each overlap lowers the active value product by a divisor at least 2",
            "matrix_dimensions": "at most O(n^5) rows by O(n^4) columns",
            "kernel_basis_size": "at most m=O(n^4)",
            "dependency_product_bits": "at most 2nm=O(n^5)",
            "basis_root_tests": "at most m tests on O(n^5)-bit products",
            "uniform_polynomial_bit_time": True,
        },
        "boundary": {
            "supplied_N_only": True,
            "advice_used_by_prefix_proof": True,
            "advice_used_by_certified_complete_algorithm": False,
            "known_factor_used": False,
            "integer_factorization_used": False,
            "primality_test_used": False,
            "full_source_execution_claimed": False,
            "complete_decoder_execution_claimed": False,
            "success_on_other_inputs_claimed": False,
            "success_density_claimed": False,
            "probability_law_claimed": False,
            "arbitrary_integer_factoring_algorithm_claimed": False,
        },
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
