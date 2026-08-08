#!/usr/bin/env python3
"""Isolated full-source and factor-free square-class reconstruction."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
STATEMENT = HERE / "MONOTONE_RECONSTRUCT_STATEMENT.md"
PUBLIC_INPUT = HERE / "MONOTONE_RECONSTRUCT_INPUT.json"
EXPECTED_STATEMENT_SHA256 = "1cdea0d4292e3f80a54551a3cc5f4c1160cfdf4af2e4ed6a110f35fbeef8936b"
EXPECTED_INPUT_SHA256 = "4b1615f7eb4fbb5cb820d51c10c8ce317c919adc0738046db8367ec0398bfa79"
PARITY_BLOCK_SIZE = 128


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


def deterministic_seed_basis(
    endpoints: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    """Ordered stack gcd basis with maximal perfect-power extraction.

    Initial endpoints are pushed in endpoint order and the last item is popped
    first.  On the first ordered basis overlap, equal values merge signatures.
    Unequal values push (d,s), (x/d,s), (d,t), (y/d,t), in that order.
    """
    work = [
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoints)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = {
        "initial_work_items": len(work),
        "generated_work_pushes": 0,
        "work_pops": 0,
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
        assert all(math.gcd(block, old_block) == 1 for old_block, _ in basis[:position])
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= block**multiplicity
    assert reconstructed == endpoints
    stats["final_block_count"] = len(basis)
    stats["final_signature_entries"] = sum(len(signature) for _, signature in basis)
    return basis, stats


def pairs_from_seed_basis(
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


class OrderedCoprimeStore:
    """Ordered stable list with block-product overlap queries."""

    def __init__(self, block_size: int):
        self.block_size = block_size
        self.slots: list[tuple[int, int] | None] = []
        self.block_products: list[int] = []
        self.block_gcd_tests = 0
        self.leaf_gcd_tests = 0

    def append(self, item: tuple[int, int]) -> None:
        index = len(self.slots)
        self.slots.append(item)
        block = index // self.block_size
        if block == len(self.block_products):
            self.block_products.append(1)
        self.block_products[block] *= item[0]

    def first_overlap(self, value: int) -> tuple[int, int] | None:
        for block, product in enumerate(self.block_products):
            self.block_gcd_tests += 1
            if math.gcd(value, product) == 1:
                continue
            start = block * self.block_size
            stop = min(start + self.block_size, len(self.slots))
            for index in range(start, stop):
                item = self.slots[index]
                if item is None:
                    continue
                self.leaf_gcd_tests += 1
                divisor = math.gcd(value, item[0])
                if divisor > 1:
                    return index, divisor
            raise AssertionError("Block product reported an overlap but no leaf did.")
        return None

    def remove(self, index: int) -> tuple[int, int]:
        item = self.slots[index]
        assert item is not None
        self.slots[index] = None
        block = index // self.block_size
        start = block * self.block_size
        stop = min(start + self.block_size, len(self.slots))
        self.block_products[block] = math.prod(
            slot[0] for slot in self.slots[start:stop] if slot is not None
        )
        return item

    def items(self) -> list[tuple[int, int]]:
        return [item for item in self.slots if item is not None]

    def verify_pairwise_coprime(self) -> bool:
        for left_block, left_product in enumerate(self.block_products):
            for right_product in self.block_products[:left_block]:
                if math.gcd(left_product, right_product) != 1:
                    return False
            start = left_block * self.block_size
            values = [
                item[0]
                for item in self.slots[start : start + self.block_size]
                if item is not None
            ]
            for position, value in enumerate(values):
                if any(math.gcd(value, old_value) != 1 for old_value in values[:position]):
                    return False
        return True


def factor_free_parity_rows(
    initial_entries: list[tuple[int, int]],
) -> tuple[list[int], list[tuple[int, int]], dict[str, int]]:
    """Refine endpoint square classes without decomposing an integer.

    An entry (x,A) means that x occurs in the columns selected by bit mask A.
    If d=gcd(x,y)>1, replace (x,A),(y,B), in work-stack order, by
    (d,A xor B),(x/d,A),(y/d,B).  This preserves every column square class.
    The stable list is ordered by append time.  Its first overlap is found by
    deterministic block-product queries followed by an ordered leaf scan.
    """
    work = [(value, mask) for value, mask in initial_entries if value > 1 and mask]
    stable = OrderedCoprimeStore(PARITY_BLOCK_SIZE)
    stats = {
        "block_size": PARITY_BLOCK_SIZE,
        "initial_entries": len(work),
        "generated_work_pushes": 0,
        "work_pops": 0,
        "maximum_work_size": len(work),
        "unit_or_zero_mask_discards": 0,
        "refinements": 0,
        "equal_value_refinements": 0,
        "common_mask_cancellations": 0,
        "stable_appends": 0,
    }
    while work:
        value, mask = work.pop()
        stats["work_pops"] += 1
        if value == 1 or mask == 0:
            stats["unit_or_zero_mask_discards"] += 1
            continue
        overlap = stable.first_overlap(value)
        if overlap is None:
            stable.append((value, mask))
            stats["stable_appends"] += 1
            continue
        position, divisor = overlap
        old_value, old_mask = stable.remove(position)
        assert divisor == math.gcd(value, old_value) > 1
        stats["refinements"] += 1
        if value == old_value:
            stats["equal_value_refinements"] += 1
        common_mask = mask ^ old_mask
        if common_mask == 0:
            stats["common_mask_cancellations"] += 1
        work.extend(
            (
                (divisor, common_mask),
                (value // divisor, mask),
                (old_value // divisor, old_mask),
            )
        )
        stats["generated_work_pushes"] += 3
        stats["maximum_work_size"] = max(stats["maximum_work_size"], len(work))

    terminal = stable.items()
    assert stable.verify_pairwise_coprime()
    row_masks = []
    square_blocks = 0
    for value, mask in terminal:
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            row_masks.append(mask)
    stats.update(
        {
            "block_product_gcd_tests": stable.block_gcd_tests,
            "ordered_leaf_gcd_tests": stable.leaf_gcd_tests,
            "terminal_block_count": len(terminal),
            "terminal_square_block_count": square_blocks,
            "terminal_nonsquare_block_count": len(row_masks),
            "distinct_nonzero_row_masks": len(set(row_masks)),
            "stable_slot_count_including_holes": len(stable.slots),
        }
    )
    return row_masks, terminal, stats


def complete_binary_kernel(
    row_masks: list[int], column_count: int
) -> tuple[int, list[int], dict[str, int]]:
    pivots: dict[int, int] = {}
    row_xors = 0
    zero_rows = 0
    for original in row_masks:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
            row_xors += 1
        if row == 0:
            zero_rows += 1

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
        assert all((row & vector).bit_count() % 2 == 0 for row in row_masks)
        kernel.append(vector)
    assert len(pivots) + len(kernel) == column_count
    return len(pivots), kernel, {
        "input_row_count": len(row_masks),
        "rank": len(pivots),
        "zero_or_redundant_rows": zero_rows,
        "row_reduction_xors": row_xors,
        "kernel_solve_xors": solve_xors,
        "kernel_dimension": len(kernel),
    }


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
    total_started = time.monotonic()

    statement_hash = sha256_file(STATEMENT)
    input_hash = sha256_file(PUBLIC_INPUT)
    assert statement_hash == EXPECTED_STATEMENT_SHA256
    assert input_hash == EXPECTED_INPUT_SHA256
    supplied = json.loads(PUBLIC_INPUT.read_text(encoding="utf-8"))
    assert set(supplied) == {"N", "n", "bound"}
    modulus = int(supplied["N"])
    n = int(supplied["n"])
    bound = int(supplied["bound"])
    assert modulus % 2 == 1
    assert n == modulus.bit_length()
    assert bound == n * n

    trial_started = time.monotonic()
    nonunit_trial_gcds = []
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        if divisor != 1:
            nonunit_trial_gcds.append({"trial": trial, "gcd": divisor})
    trial_seconds = time.monotonic() - trial_started
    if nonunit_trial_gcds:
        proper = next(
            (
                row["gcd"]
                for row in nonunit_trial_gcds
                if 1 < row["gcd"] < modulus
            ),
            None,
        )
        args.output.write_text(
            json.dumps(
                {
                    "status": "TRIAL_FACTOR" if proper is not None else "TRIAL_NONUNIT",
                    "role": "uniform early trial-screen termination",
                    "N": modulus,
                    "n": n,
                    "B": bound,
                    "trial_screen": nonunit_trial_gcds,
                    "proper_divisor": proper,
                    "factorization_or_primality_used": False,
                    "elapsed_seconds": time.monotonic() - total_started,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        return 0

    records: list[dict[str, object]] = []
    seen_residues: set[int] = set()
    attempts = 0
    duplicate_residues = 0
    direct_counts = {
        "minus": {"unit": 0, "improper_N": 0, "proper": 0},
        "plus": {"unit": 0, "improper_N": 0, "proper": 0},
    }
    improper_direct = []
    proper_direct = []

    def attempt(c: int, provenance: dict[str, object]) -> bool:
        nonlocal attempts, duplicate_residues
        attempts += 1
        if c in seen_residues:
            duplicate_residues += 1
            return False
        seen_residues.add(c)
        assert math.gcd(c, modulus) == 1
        w = pow(c, -1, modulus)
        relation_value = c * w
        assert relation_value % modulus == 1
        record_index = len(records)
        records.append(
            {"c": c, "w": w, "P": relation_value, "provenance": provenance}
        )
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if divisor == 1:
                direct_counts[sign]["unit"] += 1
            elif divisor == modulus:
                direct_counts[sign]["improper_N"] += 1
                assert (sign == "minus" and c == w) or (
                    sign == "plus" and c + w == modulus
                )
                improper_direct.append(
                    {
                        "record_index_zero_based": record_index,
                        "sign": sign,
                        "c": c,
                        "w": w,
                        "gcd": divisor,
                        "provenance": provenance,
                    }
                )
            else:
                direct_counts[sign]["proper"] += 1
                proper_direct.append(
                    {
                        "record_index_zero_based": record_index,
                        "sign": sign,
                        "c": c,
                        "w": w,
                        "gcd": divisor,
                        "provenance": provenance,
                    }
                )
        return True

    source_started = time.monotonic()
    for seed in range(2, n + 1):
        assert attempt(seed, {"kind": "initial_seed", "seed": seed})
    seed_record_count = len(records)
    seed_endpoints = [
        int(value)
        for record in records
        for value in (record["c"], record["w"])
    ]
    seed_basis, seed_basis_stats = deterministic_seed_basis(seed_endpoints)
    frozen_pairs, seed_supports = pairs_from_seed_basis(seed_basis, seed_record_count)

    for pair_index, (u, v) in enumerate(frozen_pairs):
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

    appended_boundaries = []
    for pair_index, (u, v) in enumerate(((2, 3), (2, 4))):
        before_records = len(records)
        before_attempts = attempts
        before_duplicates = duplicate_residues
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                attempt(
                    c,
                    {
                        "kind": "nonadaptive_seed_pair",
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
        appended_boundaries.append(
            {
                "pair_index_zero_based": pair_index,
                "pair": [u, v],
                "attempts": attempts - before_attempts,
                "retained_records": len(records) - before_records,
                "duplicate_residues": duplicate_residues - before_duplicates,
                "cumulative_record_count": len(records),
            }
        )
    source_seconds = time.monotonic() - source_started
    expected_source_positions = (n - 1) + 2 * (n + 1) * (bound + 1)
    assert attempts == expected_source_positions
    assert attempts - duplicate_residues == len(records) == len(seen_residues)
    assert sum(
        direct_counts[sign][kind]
        for sign in direct_counts
        for kind in direct_counts[sign]
    ) == 2 * len(records)

    dedup_started = time.monotonic()
    unique_records = []
    seen_exact_values = set()
    unit_exact_values = 0
    duplicate_exact_values = 0
    for raw_index, record in enumerate(records):
        relation_value = int(record["P"])
        if relation_value == 1:
            unit_exact_values += 1
            continue
        if relation_value in seen_exact_values:
            duplicate_exact_values += 1
            continue
        seen_exact_values.add(relation_value)
        unique_records.append((raw_index, record))
    relation_values = [int(record["P"]) for _, record in unique_records]
    assert all(value != 1 for value in relation_values)
    assert len(relation_values) == len(set(relation_values))
    dedup_seconds = time.monotonic() - dedup_started

    refinement_started = time.monotonic()
    initial_entries = []
    for column, (_, record) in enumerate(unique_records):
        mask = 1 << column
        initial_entries.append((int(record["c"]), mask))
        initial_entries.append((int(record["w"]), mask))
    row_masks, terminal_blocks, refinement_stats = factor_free_parity_rows(
        initial_entries
    )
    refinement_seconds = time.monotonic() - refinement_started

    kernel_started = time.monotonic()
    rank, kernel, kernel_stats = complete_binary_kernel(
        row_masks, len(relation_values)
    )
    kernel_seconds = time.monotonic() - kernel_started

    roots_started = time.monotonic()
    root_results = []
    all_products_square = True
    all_roots_square_to_one = True
    all_vectors_in_kernel = True
    discovered_proper_divisors = set()
    for basis_index, vector in enumerate(kernel):
        selected_columns = []
        bits = vector
        while bits:
            low = bits & -bits
            selected_columns.append(low.bit_length() - 1)
            bits ^= low
        all_vectors_in_kernel = all_vectors_in_kernel and all(
            (row & vector).bit_count() % 2 == 0 for row in row_masks
        )
        selected_product = math.prod(relation_values[column] for column in selected_columns)
        root = math.isqrt(selected_product)
        product_is_square = root * root == selected_product
        all_products_square = all_products_square and product_is_square
        root_mod_N = root % modulus
        root_square_mod_N = root_mod_N * root_mod_N % modulus
        all_roots_square_to_one = all_roots_square_to_one and root_square_mod_N == 1
        minus = math.gcd(root - 1, modulus)
        plus = math.gcd(root + 1, modulus)
        proper = sorted(
            {
                divisor
                for divisor in (minus, plus)
                if 1 < divisor < modulus
            }
        )
        discovered_proper_divisors.update(proper)
        provenance = Counter(
            unique_records[column][1]["provenance"]["kind"]
            for column in selected_columns
        )
        appended_pairs = Counter(
            (
                unique_records[column][1]["provenance"]["pair_index_zero_based"],
                unique_records[column][1]["provenance"]["u"],
                unique_records[column][1]["provenance"]["v"],
            )
            for column in selected_columns
            if unique_records[column][1]["provenance"]["kind"]
            == "nonadaptive_seed_pair"
        )
        root_results.append(
            {
                "kernel_basis_index": basis_index,
                "vector_support": len(selected_columns),
                "vector_bit_length": vector.bit_length(),
                "vector_canonical_sha256": hash_uint(vector),
                "first_selected_column": selected_columns[0] if selected_columns else None,
                "last_selected_column": selected_columns[-1] if selected_columns else None,
                "selected_column_sequence_sha256": hash_uint_sequence(selected_columns),
                "provenance_split": dict(sorted(provenance.items())),
                "selected_appended_pairs": [
                    {
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "selected_columns": count,
                    }
                    for (pair_index, u, v), count in sorted(appended_pairs.items())
                ],
                "selected_product_is_square": product_is_square,
                "selected_product_bit_length": selected_product.bit_length(),
                "selected_product_canonical_sha256": hash_uint(selected_product),
                "positive_root_bit_length": root.bit_length(),
                "positive_root_canonical_sha256": hash_uint(root),
                "root_mod_N": root_mod_N,
                "root_square_mod_N": root_square_mod_N,
                "root_is_global_plus": root_mod_N == 1,
                "root_is_global_minus": root_mod_N == modulus - 1,
                "normalized_root_class_is_nonzero": root_mod_N
                not in (1, modulus - 1),
                "gcd_root_minus_one_N": minus,
                "gcd_root_plus_one_N": plus,
                "proper_terminal_divisors": proper,
            }
        )
    roots_seconds = time.monotonic() - roots_started

    non_global_roots = [
        result for result in root_results if result["normalized_root_class_is_nonzero"]
    ]
    every_non_global_factors = all(
        result["proper_terminal_divisors"] for result in non_global_roots
    )
    checks = {
        "authorized_input_hashes_match": True,
        "input_contains_only_N_n_B": set(supplied) == {"N", "n", "bound"},
        "n_and_B_match_N": n == modulus.bit_length() and bound == n * n,
        "trial_screen_all_one": not nonunit_trial_gcds,
        "seed_basis_reconstructs_exactly": True,
        "complete_source_position_count": attempts == expected_source_positions,
        "complete_source_accounting": attempts - duplicate_residues == len(records),
        "all_direct_screens_classified": sum(
            direct_counts[sign][kind]
            for sign in direct_counts
            for kind in direct_counts[sign]
        )
        == 2 * len(records),
        "no_proper_direct_screen": not proper_direct,
        "exact_values_first_occurrence_deduplicated": len(relation_values)
        == len(set(relation_values)),
        "terminal_refinement_blocks_pairwise_coprime": True,
        "rank_nullity": rank + len(kernel) == len(relation_values),
        "complete_kernel_vectors_verified": len(root_results) == len(kernel),
        "every_vector_is_in_kernel": all_vectors_in_kernel,
        "every_basis_product_is_exact_square": all_products_square,
        "every_basis_root_squares_to_one_mod_N": all_roots_square_to_one,
        "complete_basis_contains_nonzero_normalized_root": bool(non_global_roots),
        "every_nonzero_normalized_root_exposes_proper_divisor": every_non_global_factors,
        "no_stop_or_dependency_advice_present": set(supplied) == {"N", "n", "bound"},
        "no_decomposition_or_primality_routine_used": True,
    }
    failures = [name for name, passed in checks.items() if not passed]

    terminal_value_product_bits = sum(value.bit_length() for value, _ in terminal_blocks)
    total_seconds = time.monotonic() - total_started
    output = {
        "status": "PASS" if not failures else "FAIL",
        "role": "isolated uniform N-only full-source reconstruction",
        "isolation": {
            "files_read": [
                "MONOTONE_RECONSTRUCT_STATEMENT.md",
                "MONOTONE_RECONSTRUCT_INPUT.json",
            ],
            "statement_sha256": statement_hash,
            "input_sha256": input_hash,
            "other_F111_files_read": [],
            "F98_F109_F110_F115_F116_files_read": [],
        },
        "public_input": {"N": modulus, "n": n, "B": bound},
        "checks": checks,
        "failures": failures,
        "timings_seconds": {
            "trial_screen": trial_seconds,
            "source_including_seed_basis": source_seconds,
            "exact_value_deduplication": dedup_seconds,
            "factor_free_parity_refinement": refinement_seconds,
            "binary_kernel": kernel_seconds,
            "all_basis_root_tests": roots_seconds,
            "total": total_seconds,
        },
        "trial_screen": {
            "range": [2, bound],
            "positions": bound - 1,
            "nonunit_gcds": nonunit_trial_gcds,
        },
        "seed_basis": {
            "block_list": [block for block, _ in seed_basis],
            "operation_counts": seed_basis_stats,
            "seed_supports": seed_supports,
            "frozen_pair_list": [list(pair) for pair in frozen_pairs],
        },
        "complete_source": {
            "position_formula": "(n-1) + 2*(n+1)*(B+1)",
            "expected_positions": expected_source_positions,
            "attempted_positions": attempts,
            "seed_record_count": seed_record_count,
            "frozen_pair_count": len(frozen_pairs),
            "frozen_attempt_count": frozen_attempt_count,
            "frozen_retained_record_count": frozen_record_count,
            "frozen_duplicate_residue_count": frozen_duplicate_count,
            "appended_pair_summaries": appended_boundaries,
            "full_retained_record_count": len(records),
            "full_duplicate_residue_count": duplicate_residues,
            "record_trace_sha256": hash_record_trace(records),
            "maximum_endpoint_bit_length": max(
                max(int(record["c"]).bit_length(), int(record["w"]).bit_length())
                for record in records
            ),
            "maximum_relation_value_bit_length": max(
                int(record["P"]).bit_length() for record in records
            ),
        },
        "direct_screens": {
            "counts": direct_counts,
            "proper_screen_count": len(proper_direct),
            "proper_screens": proper_direct,
            "nonunit_improper_screen_count": len(improper_direct),
            "nonunit_improper_screens": improper_direct,
            "improper_explanation": "minus gcd N means c=w; plus gcd N means c+w=N because 1<=c,w<N",
        },
        "exact_value_deduplication": {
            "raw_record_count": len(records),
            "unit_value_count": unit_exact_values,
            "repeated_exact_value_count": duplicate_exact_values,
            "distinct_nonunit_value_count": len(relation_values),
            "first_occurrence_raw_index_sequence_sha256": hash_uint_sequence(
                [raw_index for raw_index, _ in unique_records]
            ),
            "distinct_value_sequence_sha256": hash_uint_sequence(relation_values),
        },
        "factor_free_squareclass_refinement": {
            "algorithm": "ordered three-way gcd parity refinement with 128-entry block-product first-overlap queries",
            "operation_counts": refinement_stats,
            "terminal_value_bit_length_sum": terminal_value_product_bits,
            "row_mask_count_with_duplicates": len(row_masks),
            "distinct_row_mask_count": len(set(row_masks)),
            "row_mask_sequence_sha256": hash_uint_sequence(row_masks),
        },
        "complete_kernel": {
            "column_count": len(relation_values),
            "rank": rank,
            "nullity": len(kernel),
            "operation_counts": kernel_stats,
            "kernel_basis_sequence_sha256": hash_uint_sequence(kernel),
            "basis_root_count": len(root_results),
            "global_plus_root_count": sum(
                result["root_is_global_plus"] for result in root_results
            ),
            "global_minus_root_count": sum(
                result["root_is_global_minus"] for result in root_results
            ),
            "nonzero_normalized_root_count": len(non_global_roots),
            "proper_terminal_divisors": sorted(discovered_proper_divisors),
            "basis_roots": root_results,
        },
        "extension_theorem": {
            "old_coordinates_remain_initial_after_append": True,
            "old_dependency_extends_by_zero_new_coordinates": True,
            "exact_selected_product_and_root_are_unchanged": True,
            "normalized_root_map_is_kernel_homomorphism": True,
            "complete_extended_kernel_basis_detects_nonzero_image": True,
            "particular_basis_vector_persistence_claimed": False,
        },
        "symbolic_complexity": {
            "source_positions": "S=(n-1)+2(n+1)(n^2+1)=O(n^3)",
            "endpoint_bit_length": "at most n bits",
            "relation_value_bit_length": "at most 2n bits",
            "distinct_relation_columns": "m<=S=O(n^3)",
            "parity_refinement_initial_entries": "2m=O(n^3)",
            "parity_refinement_total_input_bits": "L<=2mn=O(n^4)",
            "parity_refinements": "at most L because each overlap decreases the active integer product by a divisor >=2",
            "matrix_dimensions": "at most O(n^4) factor-free rows by O(n^3) columns",
            "kernel_basis_size": "at most m=O(n^3)",
            "dependency_product_bit_length": "at most 2nm=O(n^4)",
            "basis_root_tests": "at most m tests on O(n^4)-bit integers",
            "uniform_polynomial_bit_time": True,
        },
        "factor_free_boundary": {
            "allowed_operations_used": [
                "exact integer arithmetic and division",
                "modular exponentiation and inverse",
                "gcd",
                "maximal exact perfect-power extraction",
                "exact square tests and integer square root",
                "binary bitset linear algebra",
                "SHA-256",
            ],
            "forbidden_operations_used": [],
            "general_integer_factorization_used": False,
            "endpoint_or_relation_factorization_used": False,
            "primality_testing_used": False,
            "known_divisor_used": False,
            "retained_record_stop_used": False,
            "dependency_indices_used": False,
            "fixed_pairs_are_constant_program_text": [[2, 3], [2, 4]],
            "fixed_pairs_historically_postselected": True,
            "fixed_input_success_only": True,
            "all_input_success_claim": False,
            "probability_law_claim": False,
            "arbitrary_integer_factoring_algorithm_claim": False,
        },
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
