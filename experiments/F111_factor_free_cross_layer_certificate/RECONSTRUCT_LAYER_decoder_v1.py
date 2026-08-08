#!/usr/bin/env python3
"""Proof-blind, factor-free reconstruction of the fixed F111 frozen layer.

This program reads only RECONSTRUCT_INPUT.json.  It implements the public
arithmetic specification in RECONSTRUCT_STATEMENT.md and
RECONSTRUCT_LAYER_STATEMENT.md without factorization or primality tests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Iterable


def unsigned_bytes(value: int) -> bytes:
    if value < 0:
        raise ValueError("canonical unsigned encoding received a negative integer")
    size = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(size, "big")


def hash_integer_sequence(values: Iterable[int]) -> str:
    digest = hashlib.sha256()
    count = 0
    for value in values:
        payload = unsigned_bytes(value)
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)
        count += 1
    digest.update(count.to_bytes(8, "big"))
    return digest.hexdigest()


def hash_bitsets(values: Iterable[int], width: int) -> str:
    digest = hashlib.sha256()
    byte_width = (width + 7) // 8
    count = 0
    for value in values:
        digest.update(value.to_bytes(byte_width, "little"))
        count += 1
    digest.update(width.to_bytes(8, "big"))
    digest.update(count.to_bytes(8, "big"))
    return digest.hexdigest()


def integer_nth_root(value: int, exponent: int) -> int:
    """Return floor(value**(1/exponent)) using exact integer arithmetic."""
    if exponent == 2:
        return math.isqrt(value)
    bit_length = value.bit_length()
    low = 1 << ((bit_length - 1) // exponent)
    high = 1 << ((bit_length + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


_perfect_power_cache: dict[int, tuple[int, int]] = {}


def maximal_perfect_power(value: int) -> tuple[int, int]:
    """Return (base, largest exponent), with exponent one if none exists."""
    cached = _perfect_power_cache.get(value)
    if cached is not None:
        return cached
    for exponent in range(value.bit_length() - 1, 1, -1):
        base = integer_nth_root(value, exponent)
        if pow(base, exponent) == value:
            result = (base, exponent)
            _perfect_power_cache[value] = result
            return result
    result = (value, 1)
    _perfect_power_cache[value] = result
    return result


def add_signatures(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = left.copy()
    for index, multiplicity in right.items():
        result[index] = result.get(index, 0) + multiplicity
    return result


def scale_signature(signature: dict[int, int], multiplier: int) -> dict[int, int]:
    return {index: multiplicity * multiplier for index, multiplicity in signature.items()}


def deterministic_gcd_basis(values: list[int], label: str) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    operations = {
        "initial_stack_items": len(stack),
        "pops": 0,
        "discarded_ones": 0,
        "perfect_power_reductions": 0,
        "basis_gcd_scans": 0,
        "overlaps": 0,
        "equal_merges": 0,
        "proper_splits": 0,
        "basis_appends": 0,
        "maximum_stack_size": len(stack),
        "maximum_basis_size": 0,
    }

    next_progress = 100_000
    while stack:
        operations["pops"] += 1
        value, signature = stack.pop()
        if value == 1:
            operations["discarded_ones"] += 1
            continue

        base, exponent = maximal_perfect_power(value)
        if exponent > 1:
            value = base
            signature = scale_signature(signature, exponent)
            operations["perfect_power_reductions"] += 1

        overlap_index = None
        overlap_gcd = 1
        for index, (other_value, _) in enumerate(basis):
            operations["basis_gcd_scans"] += 1
            divisor = math.gcd(value, other_value)
            if divisor > 1:
                overlap_index = index
                overlap_gcd = divisor
                break

        if overlap_index is None:
            basis.append((value, signature))
            operations["basis_appends"] += 1
            operations["maximum_basis_size"] = max(operations["maximum_basis_size"], len(basis))
        else:
            operations["overlaps"] += 1
            other_value, other_signature = basis.pop(overlap_index)
            if value == other_value:
                stack.append((value, add_signatures(signature, other_signature)))
                operations["equal_merges"] += 1
            else:
                stack.extend(
                    [
                        (overlap_gcd, signature),
                        (value // overlap_gcd, signature),
                        (overlap_gcd, other_signature),
                        (other_value // overlap_gcd, other_signature),
                    ]
                )
                operations["proper_splits"] += 1
            operations["maximum_stack_size"] = max(operations["maximum_stack_size"], len(stack))

        if operations["basis_gcd_scans"] >= next_progress:
            print(
                f"{label}: {operations['basis_gcd_scans']} gcd scans, "
                f"{operations['pops']} pops, {len(basis)} basis items, {len(stack)} stack items",
                flush=True,
            )
            next_progress += 100_000

    basis.sort(key=lambda item: item[0])
    return basis, operations


def pairwise_coprime_check(values: list[int]) -> bool:
    """Use a product/remainder tree to test each value against all others."""
    if not values:
        return True
    levels = [values]
    while len(levels[-1]) > 1:
        previous = levels[-1]
        levels.append(
            [
                previous[index] * previous[index + 1]
                if index + 1 < len(previous)
                else previous[index]
                for index in range(0, len(previous), 2)
            ]
        )

    complements = [1]
    for level_index in range(len(levels) - 1, 0, -1):
        children = levels[level_index - 1]
        child_complements = [0] * len(children)
        for parent_index, parent_complement in enumerate(complements):
            left_index = 2 * parent_index
            left = children[left_index]
            if left_index + 1 < len(children):
                right = children[left_index + 1]
                child_complements[left_index] = (parent_complement * (right % left)) % left
                child_complements[left_index + 1] = (parent_complement * (left % right)) % right
            else:
                child_complements[left_index] = parent_complement % left
        complements = child_complements
    return all(math.gcd(value, complement) == 1 for value, complement in zip(values, complements))


def validate_basis(
    original_values: list[int], basis: list[tuple[int, dict[int, int]]]
) -> dict[str, object]:
    blocks = [value for value, _ in basis]
    reconstructed = [1] * len(original_values)
    signature_entries = 0
    for block, signature in basis:
        for index, multiplicity in signature.items():
            reconstructed[index] *= pow(block, multiplicity)
            signature_entries += 1
    mismatches = [
        index for index, (expected, actual) in enumerate(zip(original_values, reconstructed)) if expected != actual
    ]
    nonprimitive_blocks = [block for block in blocks if maximal_perfect_power(block)[1] > 1]
    return {
        "block_count": len(blocks),
        "signature_entry_count": signature_entries,
        "pairwise_coprime": pairwise_coprime_check(blocks),
        "perfect_power_free": not nonprimitive_blocks,
        "nonprimitive_block_count": len(nonprimitive_blocks),
        "exact_reconstruction": not mismatches,
        "reconstruction_mismatch_count": len(mismatches),
        "block_sha256": hash_integer_sequence(blocks),
    }


def row_reduce_and_kernel(rows: list[int], column_count: int) -> tuple[dict[int, int], list[int]]:
    pivots: dict[int, int] = {}
    for source_row in rows:
        row = source_row
        while row:
            pivot = row.bit_length() - 1
            existing = pivots.get(pivot)
            if existing is not None:
                row ^= existing
                continue
            for other_pivot, other_row in list(pivots.items()):
                if (other_row >> pivot) & 1:
                    pivots[other_pivot] = other_row ^ row
            pivots[pivot] = row
            break

    free_columns = [index for index in range(column_count) if index not in pivots]
    kernel = []
    for free_column in free_columns:
        vector = 1 << free_column
        for pivot, row in pivots.items():
            if (row >> free_column) & 1:
                vector |= 1 << pivot
        kernel.append(vector)
    return pivots, kernel


def selected_indices(bitset: int) -> list[int]:
    indices = []
    while bitset:
        low_bit = bitset & -bitset
        indices.append(low_bit.bit_length() - 1)
        bitset ^= low_bit
    return indices


def screen_class(divisor: int, modulus: int) -> str:
    if divisor == 1:
        return "unit"
    if divisor == modulus:
        return "improper_nonunit"
    return "proper_factor"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    started = time.monotonic()
    public_input = json.loads(arguments.input.read_text(encoding="utf-8"))
    modulus = int(public_input["N"])
    bit_length = int(public_input["n"])
    bound = int(public_input["bound"])
    if bit_length != modulus.bit_length() or bound != bit_length * bit_length:
        raise AssertionError("public n or bound is inconsistent with N")

    trial_nonunits = [(value, math.gcd(value, modulus)) for value in range(2, bound + 1) if math.gcd(value, modulus) != 1]
    if trial_nonunits:
        raise AssertionError(f"trial gcd range contains nonunits: {trial_nonunits}")
    print(f"verified gcd(t, N)=1 for every 2 <= t <= {bound}", flush=True)

    seen_residues: set[int] = set()
    seed_records: list[dict[str, int | str]] = []
    frozen_records: list[dict[str, int | str]] = []
    source_attempts = 0
    source_duplicates = 0
    source_endpoint_count = 0
    screen_counts = {"unit": 0, "improper_nonunit": 0, "proper_factor": 0}
    improper_screens: list[dict[str, int | str]] = []
    proper_screens: list[dict[str, int | str]] = []

    def attempt(residue: int, layer: str, provenance: dict[str, int | str]) -> None:
        nonlocal source_attempts, source_duplicates, source_endpoint_count
        source_attempts += 1
        if residue in seen_residues:
            source_duplicates += 1
            return
        seen_residues.add(residue)
        common_divisor = math.gcd(residue, modulus)
        if common_divisor != 1:
            raise AssertionError(f"retained residue {residue} is not invertible; gcd={common_divisor}")
        inverse = pow(residue, -1, modulus)
        relation_value = residue * inverse
        minus_gcd = math.gcd(residue - inverse, modulus)
        plus_gcd = math.gcd(residue + inverse, modulus)
        record_index = len(seed_records) + len(frozen_records)
        for sign, divisor in (("minus", minus_gcd), ("plus", plus_gcd)):
            classification = screen_class(divisor, modulus)
            screen_counts[classification] += 1
            if classification != "unit":
                detail = {
                    "record_index": record_index,
                    "layer": layer,
                    "sign": sign,
                    "gcd": divisor,
                    "residue": residue,
                    "inverse": inverse,
                }
                if classification == "improper_nonunit":
                    improper_screens.append(detail)
                else:
                    proper_screens.append(detail)
        record: dict[str, int | str] = {
            "record_index": record_index,
            "residue": residue,
            "inverse": inverse,
            "relation_value": relation_value,
            "minus_gcd": minus_gcd,
            "plus_gcd": plus_gcd,
        }
        record.update(provenance)
        if layer == "seed":
            seed_records.append(record)
        else:
            frozen_records.append(record)
        source_endpoint_count += 2

    for residue in range(2, bit_length + 1):
        attempt(residue, "seed", {"seed": residue})
    if len(seed_records) != bit_length - 1:
        raise AssertionError("seed retention count is not n-1")

    seed_endpoints: list[int] = []
    for record in seed_records:
        seed_endpoints.extend((int(record["residue"]), int(record["inverse"])))
    seed_basis, seed_basis_operations = deterministic_gcd_basis(seed_endpoints, "seed basis")
    seed_basis_validation = validate_basis(seed_endpoints, seed_basis)
    if not all(
        seed_basis_validation[key]
        for key in ("pairwise_coprime", "perfect_power_free", "exact_reconstruction")
    ):
        raise AssertionError(f"seed gcd basis validation failed: {seed_basis_validation}")

    frozen_pairs: list[tuple[int, int]] = []
    for seed_index in range(len(seed_records)):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in seed_basis
            if signature.get(left_endpoint, 0) + signature.get(right_endpoint, 0) > 0
        ]
        if not support:
            raise AssertionError(f"seed relation {seed_index} has empty basis support")
        frozen_pairs.append((support[0], 1 if len(support) == 1 else support[1]))
    print(
        f"seed basis has {len(seed_basis)} blocks and defines {len(frozen_pairs)} ordered frozen pairs",
        flush=True,
    )

    attempts_before_frozen = source_attempts
    duplicates_before_frozen = source_duplicates
    for pair_index, (left, right) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            attempt(
                (pow(left, exponent, modulus) * right) % modulus,
                "frozen",
                {
                    "pair_index": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_power_times_v",
                },
            )
            attempt(
                (left * pow(right, exponent, modulus)) % modulus,
                "frozen",
                {
                    "pair_index": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_times_v_power",
                },
            )
    frozen_attempts = source_attempts - attempts_before_frozen
    frozen_duplicates = source_duplicates - duplicates_before_frozen
    if frozen_attempts != len(frozen_pairs) * 2 * (bound + 1):
        raise AssertionError("frozen attempt count disagrees with the complete trajectory size")
    print(
        f"complete frozen source: {frozen_attempts} attempts, {frozen_duplicates} duplicates, "
        f"{len(frozen_records)} retained records",
        flush=True,
    )

    normalized_values: list[int] = []
    first_normalized_index: dict[int, int] = {}
    repeated_value_classes: set[int] = set()
    removed_units = 0
    removed_repeat_occurrences = 0
    for record in frozen_records:
        value = int(record["relation_value"])
        if value == 1:
            removed_units += 1
        elif value in first_normalized_index:
            removed_repeat_occurrences += 1
            repeated_value_classes.add(value)
        else:
            first_normalized_index[value] = len(normalized_values)
            normalized_values.append(value)
    if len(normalized_values) + removed_units + removed_repeat_occurrences != len(frozen_records):
        raise AssertionError("exact-value normalization does not partition frozen records")
    print(
        f"normalization: {len(normalized_values)} columns, {removed_units} units, "
        f"{removed_repeat_occurrences} repeated occurrences",
        flush=True,
    )

    exact_basis, exact_basis_operations = deterministic_gcd_basis(normalized_values, "exact-value basis")
    exact_basis_validation = validate_basis(normalized_values, exact_basis)
    if not all(
        exact_basis_validation[key]
        for key in ("pairwise_coprime", "perfect_power_free", "exact_reconstruction")
    ):
        raise AssertionError(f"exact-value gcd basis validation failed: {exact_basis_validation}")
    print(f"exact-value basis validated with {len(exact_basis)} blocks", flush=True)

    public_rows: list[int] = []
    row_seen: set[int] = set()
    zero_block_rows = 0
    repeated_block_rows = 0
    for _, signature in exact_basis:
        row = 0
        for column, multiplicity in signature.items():
            if multiplicity & 1:
                row |= 1 << column
        if row == 0:
            zero_block_rows += 1
        elif row in row_seen:
            repeated_block_rows += 1
        else:
            row_seen.add(row)
            public_rows.append(row)

    pivots, kernel_basis = row_reduce_and_kernel(public_rows, len(normalized_values))
    rank = len(pivots)
    kernel_dimension = len(normalized_values) - rank
    if len(kernel_basis) != kernel_dimension:
        raise AssertionError("constructed kernel basis has the wrong dimension")
    for vector in kernel_basis:
        if any((row & vector).bit_count() & 1 for row in public_rows):
            raise AssertionError("constructed vector is outside the public-row kernel")
    kernel_pivots, _ = row_reduce_and_kernel(kernel_basis, len(normalized_values))
    if len(kernel_pivots) != len(kernel_basis):
        raise AssertionError("constructed kernel vectors are not independent")
    print(
        f"public matrix: {len(public_rows)} distinct nonzero rows, rank {rank}, "
        f"kernel dimension {kernel_dimension}",
        flush=True,
    )

    kernel_results = []
    any_non_global_root = False
    any_proper_terminal_gcd = False
    for vector_index, vector in enumerate(kernel_basis):
        columns = selected_indices(vector)
        product = math.prod(normalized_values[column] for column in columns)
        root = math.isqrt(product)
        if root * root != product:
            raise AssertionError(f"kernel vector {vector_index} product is not an exact square")
        residue = root % modulus
        if pow(residue, 2, modulus) != 1:
            raise AssertionError(f"kernel vector {vector_index} root does not square to one modulo N")
        minus_gcd = math.gcd(residue - 1, modulus)
        plus_gcd = math.gcd(residue + 1, modulus)
        globally_positive = residue == 1
        globally_negative = residue == modulus - 1
        non_global = not (globally_positive or globally_negative)
        proper_terminal = any(1 < divisor < modulus for divisor in (minus_gcd, plus_gcd))
        any_non_global_root |= non_global
        any_proper_terminal_gcd |= proper_terminal
        kernel_results.append(
            {
                "basis_vector_index": vector_index,
                "selected_column_count": len(columns),
                "selected_columns": columns,
                "vector_sha256": hash_bitsets([vector], len(normalized_values)),
                "product_bit_length": product.bit_length(),
                "root_bit_length": root.bit_length(),
                "root_sha256": hash_integer_sequence([root]),
                "root_residue_mod_N": residue,
                "root_is_global_plus_one": globally_positive,
                "root_is_global_minus_one": globally_negative,
                "gcd_root_minus_one_N": minus_gcd,
                "gcd_root_plus_one_N": plus_gcd,
                "proper_terminal_gcd": proper_terminal,
            }
        )
        print(
            f"kernel vector {vector_index}: {len(columns)} columns, root mod N={residue}, "
            f"gcds=({minus_gcd}, {plus_gcd})",
            flush=True,
        )

    frozen_record_digest_values = []
    for record in frozen_records:
        frozen_record_digest_values.extend(
            (
                int(record["residue"]),
                int(record["inverse"]),
                int(record["relation_value"]),
                int(record["pair_index"]),
                int(record["exponent"]),
                0 if record["orientation"] == "u_power_times_v" else 1,
            )
        )

    result = {
        "verdict": "PASS" if not any_proper_terminal_gcd else "FAIL",
        "verdict_definition": "PASS means every vector in a complete frozen-layer kernel basis has only globally signed terminal gcds.",
        "public_instance": {
            "N": modulus,
            "n": bit_length,
            "bound": bound,
            "source_stop_relation_count_unused_for_complete_frozen_layer": int(public_input["source_stop_relation_count"]),
            "advice_index_count_unused_for_complete_frozen_layer": len(public_input["dependency_relation_indices_zero_based"]),
            "trial_gcd_range_start": 2,
            "trial_gcd_range_end": bound,
            "trial_nonunit_count": len(trial_nonunits),
        },
        "source": {
            "seed_attempt_count": bit_length - 1,
            "seed_retained_record_count": len(seed_records),
            "seed_basis_blocks": [block for block, _ in seed_basis],
            "seed_basis_operations": seed_basis_operations,
            "seed_basis_validation": seed_basis_validation,
            "frozen_pairs": [[left, right] for left, right in frozen_pairs],
            "frozen_pair_count": len(frozen_pairs),
            "frozen_attempt_count": frozen_attempts,
            "frozen_duplicate_count": frozen_duplicates,
            "raw_frozen_relation_count": len(frozen_records),
            "total_attempt_count_through_frozen_layer": source_attempts,
            "total_duplicate_count_through_frozen_layer": source_duplicates,
            "total_retained_record_count_through_frozen_layer": len(seed_records) + len(frozen_records),
            "endpoint_count_through_frozen_layer": source_endpoint_count,
            "frozen_record_sha256": hash_integer_sequence(frozen_record_digest_values),
            "direct_screen_counts_through_frozen_layer": screen_counts,
            "improper_nonunit_screens": improper_screens,
            "proper_factor_screens": proper_screens,
        },
        "normalization": {
            "removed_unit_value_count": removed_units,
            "removed_repeated_exact_occurrence_count": removed_repeat_occurrences,
            "repeated_exact_value_class_count": len(repeated_value_classes),
            "distinct_normalized_column_count": len(normalized_values),
            "normalized_values_sha256": hash_integer_sequence(normalized_values),
        },
        "factor_free_exact_value_basis": {
            "operations": exact_basis_operations,
            "validation": exact_basis_validation,
            "zero_block_row_count": zero_block_rows,
            "repeated_nonzero_block_row_count": repeated_block_rows,
        },
        "public_parity_matrix": {
            "distinct_nonzero_row_count": len(public_rows),
            "column_count": len(normalized_values),
            "rank": rank,
            "kernel_dimension": kernel_dimension,
            "rows_sha256_little_endian_fixed_width": hash_bitsets(public_rows, len(normalized_values)),
            "kernel_basis_sha256_little_endian_fixed_width": hash_bitsets(kernel_basis, len(normalized_values)),
        },
        "kernel_basis_results": kernel_results,
        "complete_frozen_dependency_space": {
            "any_basis_root_non_global": any_non_global_root,
            "any_basis_vector_has_proper_terminal_gcd": any_proper_terminal_gcd,
            "contains_proper_factor": any_proper_terminal_gcd,
            "completeness_reason": (
                "The public block rows contain every primitive valuation row modulo two, equal rows are redundant, "
                "and the normalized-root map is a homomorphism. A full binary kernel basis therefore determines "
                "the image of every normalized frozen dependency. Removed units and duplicate-value pairs add only "
                "global +1 roots."
            ),
        },
        "method_boundary": {
            "factor_free": True,
            "allowed_operations_used": [
                "integer gcd",
                "modular inverse",
                "modular exponentiation",
                "exact integer nth-root extraction",
                "exact integer square root",
                "binary Gaussian elimination",
            ],
            "forbidden_operations_used": [],
            "fixed_instance_only": True,
            "statement": (
                f"This exhausts the dependency space of the one public frozen batch for N={modulus}. "
                "It is not a selector, probability statement, all-input theorem, or factoring algorithm."
            ),
        },
        "elapsed_seconds_decoder": time.monotonic() - started,
    }
    arguments.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {arguments.output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
