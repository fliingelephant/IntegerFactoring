#!/usr/bin/env python3
"""Proof-blind, factor-free reconstruction of the fixed F111 interaction.

The program reads only RECONSTRUCT_INTERACTION_INPUT.json.  It reconstructs
the ordered source, a complete union square-class matrix, all requested
kernels, and the cross-layer quotient without factorization or primality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


sys.dont_write_bytecode = True
CHUNK_SIZE = 64
PROGRESS_SCAN_INTERVAL = 50_000_000


def unsigned_bytes(value: int) -> bytes:
    if value < 0:
        raise ValueError("unsigned encoding received a negative integer")
    length = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(length, "big")


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


def hash_bitsets(bitsets: Iterable[int], width: int) -> str:
    digest = hashlib.sha256()
    byte_width = (width + 7) // 8
    count = 0
    for bitset in bitsets:
        digest.update(bitset.to_bytes(byte_width, "little"))
        count += 1
    digest.update(width.to_bytes(8, "big"))
    digest.update(count.to_bytes(8, "big"))
    return digest.hexdigest()


def integer_nth_root(value: int, exponent: int) -> int:
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


@dataclass
class BasisChunk:
    items: list[tuple[int, dict[int, int]]]
    product: int


class ChunkedOrderedBasis:
    """Ordered basis with exact batched first-overlap searches."""

    def __init__(self) -> None:
        self.chunks: list[BasisChunk] = []
        self.size = 0

    def append(self, item: tuple[int, dict[int, int]]) -> None:
        if not self.chunks or len(self.chunks[-1].items) >= CHUNK_SIZE:
            self.chunks.append(BasisChunk([], 1))
        chunk = self.chunks[-1]
        chunk.items.append(item)
        chunk.product *= item[0]
        self.size += 1

    def first_overlap(
        self, value: int, operations: dict[str, int]
    ) -> tuple[int, int, int] | None:
        for chunk_index, chunk in enumerate(self.chunks):
            operations["batch_gcd_queries"] += 1
            if math.gcd(value, chunk.product) == 1:
                operations["logical_basis_gcd_scans"] += len(chunk.items)
                continue
            for item_index, (other_value, _) in enumerate(chunk.items):
                operations["logical_basis_gcd_scans"] += 1
                operations["item_gcd_queries_inside_positive_chunks"] += 1
                divisor = math.gcd(value, other_value)
                if divisor > 1:
                    return chunk_index, item_index, divisor
            raise AssertionError("positive chunk gcd had no overlapping item")
        return None

    def remove(self, chunk_index: int, item_index: int) -> tuple[int, dict[int, int]]:
        chunk = self.chunks[chunk_index]
        item = chunk.items.pop(item_index)
        self.size -= 1
        if chunk.items:
            chunk.product = math.prod(value for value, _ in chunk.items)
        else:
            self.chunks.pop(chunk_index)
        return item

    def flatten(self) -> list[tuple[int, dict[int, int]]]:
        return [item for chunk in self.chunks for item in chunk.items]


def deterministic_gcd_basis(
    values: list[int], label: str
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis = ChunkedOrderedBasis()
    operations = {
        "initial_stack_items": len(stack),
        "pops": 0,
        "discarded_ones": 0,
        "perfect_power_reductions": 0,
        "logical_basis_gcd_scans": 0,
        "batch_gcd_queries": 0,
        "item_gcd_queries_inside_positive_chunks": 0,
        "overlaps": 0,
        "equal_merges": 0,
        "proper_splits": 0,
        "basis_appends": 0,
        "maximum_stack_size": len(stack),
        "maximum_basis_size": 0,
        "chunk_size": CHUNK_SIZE,
    }
    next_progress = PROGRESS_SCAN_INTERVAL

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

        overlap = basis.first_overlap(value, operations)
        if overlap is None:
            basis.append((value, signature))
            operations["basis_appends"] += 1
            operations["maximum_basis_size"] = max(operations["maximum_basis_size"], basis.size)
        else:
            chunk_index, item_index, divisor = overlap
            other_value, other_signature = basis.remove(chunk_index, item_index)
            operations["overlaps"] += 1
            if value == other_value:
                stack.append((value, add_signatures(signature, other_signature)))
                operations["equal_merges"] += 1
            else:
                stack.extend(
                    [
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, other_signature),
                        (other_value // divisor, other_signature),
                    ]
                )
                operations["proper_splits"] += 1
            operations["maximum_stack_size"] = max(operations["maximum_stack_size"], len(stack))

        if operations["logical_basis_gcd_scans"] >= next_progress:
            print(
                f"{label}: logical_scans={operations['logical_basis_gcd_scans']} "
                f"batch_queries={operations['batch_gcd_queries']} pops={operations['pops']} "
                f"basis={basis.size} stack={len(stack)}",
                flush=True,
            )
            next_progress = (
                operations["logical_basis_gcd_scans"] // PROGRESS_SCAN_INTERVAL + 1
            ) * PROGRESS_SCAN_INTERVAL

    result = basis.flatten()
    result.sort(key=lambda item: item[0])
    return result, operations


def pairwise_coprime_check(values: list[int]) -> bool:
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
        next_complements = [0] * len(children)
        for parent_index, complement in enumerate(complements):
            left_index = 2 * parent_index
            left = children[left_index]
            if left_index + 1 < len(children):
                right = children[left_index + 1]
                next_complements[left_index] = (complement * (right % left)) % left
                next_complements[left_index + 1] = (complement * (left % right)) % right
            else:
                next_complements[left_index] = complement % left
        complements = next_complements
    return all(math.gcd(value, complement) == 1 for value, complement in zip(values, complements))


def validate_basis(
    originals: list[int], basis: list[tuple[int, dict[int, int]]]
) -> dict[str, object]:
    blocks = [block for block, _ in basis]
    reconstructed = [1] * len(originals)
    signature_entries = 0
    for block, signature in basis:
        for index, multiplicity in signature.items():
            if not 0 <= index < len(originals) or multiplicity <= 0:
                raise AssertionError("invalid exact basis signature")
            reconstructed[index] *= pow(block, multiplicity)
            signature_entries += 1
    mismatch_count = sum(expected != actual for expected, actual in zip(originals, reconstructed))
    nonprimitive_count = sum(maximal_perfect_power(block)[1] > 1 for block in blocks)
    result = {
        "block_count": len(blocks),
        "signature_entry_count": signature_entries,
        "pairwise_coprime": pairwise_coprime_check(blocks),
        "perfect_power_free": nonprimitive_count == 0,
        "nonprimitive_block_count": nonprimitive_count,
        "exact_reconstruction": mismatch_count == 0,
        "reconstruction_mismatch_count": mismatch_count,
        "block_sha256": hash_integer_sequence(blocks),
    }
    if not result["pairwise_coprime"] or not result["perfect_power_free"] or not result["exact_reconstruction"]:
        raise AssertionError(f"gcd basis validation failed: {result}")
    return result


def public_parity_rows(
    basis: list[tuple[int, dict[int, int]]], column_count: int
) -> tuple[list[int], dict[str, int]]:
    rows: list[int] = []
    seen: set[int] = set()
    zero_count = 0
    repeated_count = 0
    for _, signature in basis:
        row = 0
        for column, multiplicity in signature.items():
            if multiplicity & 1:
                row |= 1 << column
        if row == 0:
            zero_count += 1
        elif row in seen:
            repeated_count += 1
        else:
            seen.add(row)
            rows.append(row)
    if any(row >> column_count for row in rows):
        raise AssertionError("public row exceeds its declared width")
    return rows, {
        "zero_block_row_count": zero_count,
        "repeated_nonzero_block_row_count": repeated_count,
    }


def restrict_and_remap_rows(
    union_rows: list[int], union_indices_in_local_order: list[int]
) -> list[int]:
    union_to_local = {union_index: local_index for local_index, union_index in enumerate(union_indices_in_local_order)}
    if len(union_to_local) != len(union_indices_in_local_order):
        raise AssertionError("coordinate remap is not injective")
    rows: list[int] = []
    seen: set[int] = set()
    for union_row in union_rows:
        local_row = 0
        remaining = union_row
        while remaining:
            bit = remaining & -remaining
            union_index = bit.bit_length() - 1
            local_index = union_to_local.get(union_index)
            if local_index is not None:
                local_row |= 1 << local_index
            remaining ^= bit
        if local_row and local_row not in seen:
            seen.add(local_row)
            rows.append(local_row)
    return rows


def row_reduce_and_kernel(rows: list[int], column_count: int) -> tuple[dict[int, int], list[int]]:
    pivots: dict[int, int] = {}
    for source_row in rows:
        row = source_row
        while row:
            pivot = row.bit_length() - 1
            existing = pivots.get(pivot)
            if existing is None:
                pivots[pivot] = row
                break
            row ^= existing

    ordered_pivots = sorted(pivots)
    for pivot in ordered_pivots:
        pivot_row = pivots[pivot]
        for higher_pivot in ordered_pivots:
            if higher_pivot > pivot and ((pivots[higher_pivot] >> pivot) & 1):
                pivots[higher_pivot] ^= pivot_row

    free_columns = [column for column in range(column_count) if column not in pivots]
    kernel: list[int] = []
    for free_column in free_columns:
        vector = 1 << free_column
        for pivot, row in pivots.items():
            if (row >> free_column) & 1:
                vector |= 1 << pivot
        kernel.append(vector)
    return pivots, kernel


def selected_indices(vector: int) -> list[int]:
    result = []
    while vector:
        bit = vector & -vector
        result.append(bit.bit_length() - 1)
        vector ^= bit
    return result


def canonical_root_class(residue: int, modulus: int) -> int:
    return min(residue, (-residue) % modulus)


def root_class_span(residues: list[int], modulus: int) -> dict[str, object]:
    span = {1}
    independent_generator_indices = []
    for index, residue in enumerate(residues):
        generator = canonical_root_class(residue, modulus)
        if generator in span:
            continue
        old_span = list(span)
        span.update(canonical_root_class((value * generator) % modulus, modulus) for value in old_span)
        independent_generator_indices.append(index)
    return {
        "rank_mod_global_sign": len(independent_generator_indices),
        "independent_basis_vector_indices": independent_generator_indices,
        "image_class_count": len(span),
        "image_classes": sorted(span),
    }


def decode_vector(vector: int, values: list[int], modulus: int, vector_index: int) -> dict[str, object]:
    columns = selected_indices(vector)
    product = math.prod(values[column] for column in columns)
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError(f"kernel vector {vector_index} does not give an exact square")
    residue = root % modulus
    if pow(residue, 2, modulus) != 1:
        raise AssertionError(f"kernel vector {vector_index} root does not square to one")
    minus_gcd = math.gcd(residue - 1, modulus)
    plus_gcd = math.gcd(residue + 1, modulus)
    if residue == 1:
        classification = "+1"
    elif residue == modulus - 1:
        classification = "-1"
    else:
        classification = "non-global"
    proper = any(1 < divisor < modulus for divisor in (minus_gcd, plus_gcd))
    if proper != (classification == "non-global"):
        raise AssertionError("root classification and terminal gcd classification disagree")
    return {
        "basis_vector_index": vector_index,
        "selected_column_count": len(columns),
        "selected_columns": columns,
        "vector_sha256": hash_bitsets([vector], len(values)),
        "product_bit_length": product.bit_length(),
        "product_sha256": hash_integer_sequence([product]),
        "root_bit_length": root.bit_length(),
        "root_sha256": hash_integer_sequence([root]),
        "root_residue_mod_N": residue,
        "root_classification": classification,
        "gcd_root_minus_one_N": minus_gcd,
        "gcd_root_plus_one_N": plus_gcd,
        "proper_terminal_gcd": proper,
    }


def decode_system(
    name: str, rows: list[int], values: list[int], modulus: int
) -> tuple[dict[str, object], list[int]]:
    pivots, kernel = row_reduce_and_kernel(rows, len(values))
    rank = len(pivots)
    if len(kernel) != len(values) - rank:
        raise AssertionError(f"{name}: kernel dimension identity failed")
    for vector in kernel:
        if any((row & vector).bit_count() & 1 for row in rows):
            raise AssertionError(f"{name}: kernel vector is not orthogonal")
    kernel_rank, _ = row_reduce_and_kernel(kernel, len(values))
    if len(kernel_rank) != len(kernel):
        raise AssertionError(f"{name}: kernel vectors are dependent")
    results = [decode_vector(vector, values, modulus, index) for index, vector in enumerate(kernel)]
    root_map = root_class_span([int(result["root_residue_mod_N"]) for result in results], modulus)
    classification_counts = {"+1": 0, "-1": 0, "non-global": 0}
    for result in results:
        classification_counts[str(result["root_classification"])] += 1
    system = {
        "name": name,
        "column_count": len(values),
        "distinct_nonzero_row_count": len(rows),
        "rank": rank,
        "kernel_dimension": len(kernel),
        "rows_sha256_little_endian_fixed_width": hash_bitsets(rows, len(values)),
        "kernel_basis_sha256_little_endian_fixed_width": hash_bitsets(kernel, len(values)),
        "basis_root_classification_counts": classification_counts,
        "normalized_root_map": root_map,
        "contains_useful_dependency": int(root_map["rank_mod_global_sign"]) > 0,
        "kernel_basis_results": results,
    }
    print(
        f"{name}: columns={len(values)} rows={len(rows)} rank={rank} "
        f"kernel={len(kernel)} normalized_root_rank={root_map['rank_mod_global_sign']}",
        flush=True,
    )
    return system, kernel


class BinarySpan:
    def __init__(self) -> None:
        self.pivots: dict[int, int] = {}

    def add(self, vector: int) -> bool:
        reduced = vector
        while reduced:
            pivot = reduced.bit_length() - 1
            existing = self.pivots.get(pivot)
            if existing is None:
                self.pivots[pivot] = reduced
                return True
            reduced ^= existing
        return False

    @property
    def rank(self) -> int:
        return len(self.pivots)


def remap_vector(local_vector: int, union_indices_in_local_order: list[int]) -> int:
    result = 0
    while local_vector:
        bit = local_vector & -local_vector
        local_index = bit.bit_length() - 1
        result |= 1 << union_indices_in_local_order[local_index]
        local_vector ^= bit
    return result


def normalize_records(records: list[dict[str, int | str]]) -> tuple[list[int], dict[str, object]]:
    values: list[int] = []
    first_indices: dict[int, int] = {}
    unit_count = 0
    duplicate_count = 0
    duplicate_classes: set[int] = set()
    first_record_indices: list[int] = []
    for record in records:
        value = int(record["relation_value"])
        if value == 1:
            unit_count += 1
        elif value in first_indices:
            duplicate_count += 1
            duplicate_classes.add(value)
        else:
            first_indices[value] = len(values)
            values.append(value)
            first_record_indices.append(int(record["record_index"]))
    if len(records) != unit_count + duplicate_count + len(values):
        raise AssertionError("normalization counts do not partition raw records")
    return values, {
        "raw_record_count": len(records),
        "unit_value_count": unit_count,
        "duplicate_exact_occurrence_count": duplicate_count,
        "duplicate_exact_value_class_count": len(duplicate_classes),
        "distinct_nonunit_exact_value_count": len(values),
        "values_sha256": hash_integer_sequence(values),
        "first_record_indices_sha256": hash_integer_sequence(first_record_indices),
    }


def run_self_checks() -> None:
    if maximal_perfect_power(64) != (2, 6) or maximal_perfect_power(72) != (72, 1):
        raise AssertionError("exact perfect-power self-check failed")
    test_basis = ChunkedOrderedBasis()
    test_values: list[int] = []
    aggregate = 1
    candidate = 2
    while len(test_values) < 12:
        if math.gcd(candidate, aggregate) == 1:
            test_values.append(candidate)
            aggregate *= candidate
            test_basis.append((candidate, {len(test_values) - 1: 1}))
        candidate += 1
    for probe in range(2, 250):
        operations = {
            "batch_gcd_queries": 0,
            "logical_basis_gcd_scans": 0,
            "item_gcd_queries_inside_positive_chunks": 0,
        }
        actual = test_basis.first_overlap(probe, operations)
        expected = None
        for index, value in enumerate(test_values):
            divisor = math.gcd(probe, value)
            if divisor > 1:
                expected = (0, index, divisor)
                break
        if actual != expected:
            raise AssertionError("chunked first-overlap self-check failed")
    state = 1
    for width in range(1, 10):
        for _ in range(40):
            rows = []
            for _ in range(2 * width + 1):
                state = (1103515245 * state + 12345) & ((1 << 31) - 1)
                rows.append(state & ((1 << width) - 1))
            pivots, kernel = row_reduce_and_kernel(rows, width)
            if len(pivots) + len(kernel) != width:
                raise AssertionError("binary kernel dimension self-check failed")
            if any(any((row & vector).bit_count() & 1 for row in rows) for vector in kernel):
                raise AssertionError("binary kernel orthogonality self-check failed")
            kernel_pivots, _ = row_reduce_and_kernel(kernel, width)
            if len(kernel_pivots) != len(kernel):
                raise AssertionError("binary kernel independence self-check failed")
    print("internal exact-arithmetic self-checks passed", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    started = time.monotonic()
    run_self_checks()

    input_bytes = arguments.input.read_bytes()
    public_input = json.loads(input_bytes)
    modulus = int(public_input["N"])
    bit_length = int(public_input["n"])
    bound = int(public_input["bound"])
    stop_count = int(public_input["source_stop_relation_count"])
    if modulus.bit_length() != bit_length or bound != bit_length * bit_length or modulus % 2 != 1:
        raise AssertionError("public instance metadata is inconsistent")
    trial_nonunits = [
        {"value": value, "gcd": math.gcd(value, modulus)}
        for value in range(2, bound + 1)
        if math.gcd(value, modulus) != 1
    ]
    if trial_nonunits:
        raise AssertionError(f"trial gcd range contains nonunits: {trial_nonunits}")
    print(f"verified gcd(t, N)=1 for every 2 <= t <= {bound}", flush=True)

    seen_residues: set[int] = set()
    records: list[dict[str, int | str]] = []
    source_attempts = 0
    source_duplicates = 0
    endpoint_count = 0
    screen_counts = {"unit": 0, "improper_nonunit": 0, "proper_factor": 0}
    nonunit_screens: list[dict[str, int | str]] = []

    def attempt(residue: int, layer: str, provenance: dict[str, int | str]) -> bool:
        nonlocal source_attempts, source_duplicates, endpoint_count
        source_attempts += 1
        if residue in seen_residues:
            source_duplicates += 1
            return False
        seen_residues.add(residue)
        residue_gcd = math.gcd(residue, modulus)
        if residue_gcd != 1:
            raise AssertionError(f"retained residue {residue} is not invertible; gcd={residue_gcd}")
        inverse = pow(residue, -1, modulus)
        relation_value = residue * inverse
        minus_gcd = math.gcd(residue - inverse, modulus)
        plus_gcd = math.gcd(residue + inverse, modulus)
        record_index = len(records)
        for sign, divisor in (("minus", minus_gcd), ("plus", plus_gcd)):
            if divisor == 1:
                classification = "unit"
            elif divisor == modulus:
                classification = "improper_nonunit"
            else:
                classification = "proper_factor"
            screen_counts[classification] += 1
            if classification != "unit":
                nonunit_screens.append(
                    {
                        "record_index": record_index,
                        "layer": layer,
                        "residue": residue,
                        "inverse": inverse,
                        "sign": sign,
                        "gcd": divisor,
                        "classification": classification,
                    }
                )
        record: dict[str, int | str] = {
            "record_index": record_index,
            "layer": layer,
            "residue": residue,
            "inverse": inverse,
            "relation_value": relation_value,
            "minus_gcd": minus_gcd,
            "plus_gcd": plus_gcd,
        }
        record.update(provenance)
        records.append(record)
        endpoint_count += 2
        return True

    for seed in range(2, bit_length + 1):
        attempt(seed, "frozen", {"provenance_kind": "seed", "seed": seed})
    seed_record_count = len(records)
    if seed_record_count != bit_length - 1:
        raise AssertionError("seed record count is not n-1")

    seed_endpoints: list[int] = []
    for record in records:
        seed_endpoints.extend((int(record["residue"]), int(record["inverse"])))
    seed_basis, seed_basis_operations = deterministic_gcd_basis(seed_endpoints, "seed gcd basis")
    seed_basis_validation = validate_basis(seed_endpoints, seed_basis)
    frozen_pairs: list[tuple[int, int]] = []
    for seed_index in range(seed_record_count):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in seed_basis
            if signature.get(left_endpoint, 0) + signature.get(right_endpoint, 0) > 0
        ]
        if not support:
            raise AssertionError("seed relation has empty basis support")
        frozen_pairs.append((support[0], 1 if len(support) == 1 else support[1]))
    print(f"seed basis blocks={len(seed_basis)} frozen pairs={len(frozen_pairs)}", flush=True)

    frozen_attempt_start = source_attempts
    frozen_duplicate_start = source_duplicates
    for pair_index, (left, right) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            attempt(
                (pow(left, exponent, modulus) * right) % modulus,
                "frozen",
                {
                    "provenance_kind": "frozen_seed_basis_pair",
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
                    "provenance_kind": "frozen_seed_basis_pair",
                    "pair_index": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_times_v_power",
                },
            )
    frozen_end = len(records)
    frozen_attempt_count = source_attempts - frozen_attempt_start
    frozen_duplicate_count = source_duplicates - frozen_duplicate_start
    expected_frozen_attempts = len(frozen_pairs) * 2 * (bound + 1)
    if frozen_attempt_count != expected_frozen_attempts:
        raise AssertionError("complete frozen trajectory attempt count is wrong")
    print(
        f"frozen layer records={frozen_end} attempts={frozen_attempt_count} "
        f"duplicates={frozen_duplicate_count}",
        flush=True,
    )

    appended_attempt_start = source_attempts
    appended_duplicate_start = source_duplicates
    stop_reached = len(records) == stop_count
    for pair_index, (left, right) in enumerate(((2, 3), (2, 4))):
        if stop_reached:
            break
        for exponent in range(bound + 1):
            attempt(
                (pow(left, exponent, modulus) * right) % modulus,
                "appended",
                {
                    "provenance_kind": "nonadaptive_seed_pair",
                    "appended_pair_index": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_power_times_v",
                },
            )
            if len(records) == stop_count:
                stop_reached = True
                break
            attempt(
                (left * pow(right, exponent, modulus)) % modulus,
                "appended",
                {
                    "provenance_kind": "nonadaptive_seed_pair",
                    "appended_pair_index": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_times_v_power",
                },
            )
            if len(records) == stop_count:
                stop_reached = True
                break
    if not stop_reached or len(records) != stop_count:
        raise AssertionError("declared retained-record stop was not reached exactly")
    appended_attempt_count = source_attempts - appended_attempt_start
    appended_duplicate_count = source_duplicates - appended_duplicate_start
    frozen_records = records[:frozen_end]
    appended_records = records[frozen_end:]
    print(
        f"exact stop={len(records)} appended records={len(appended_records)} "
        f"appended attempts={appended_attempt_count} duplicates={appended_duplicate_count}",
        flush=True,
    )

    frozen_values, frozen_normalization = normalize_records(frozen_records)
    appended_values, appended_normalization = normalize_records(appended_records)
    union_values, union_normalization = normalize_records(records)
    frozen_value_set = set(frozen_values)
    appended_value_set = set(appended_values)
    shared_values = frozen_value_set & appended_value_set
    union_index = {value: index for index, value in enumerate(union_values)}
    if len(union_index) != len(union_values):
        raise AssertionError("union normalization retained a repeated value")
    frozen_union_indices = [union_index[value] for value in frozen_values]
    appended_standalone_union_indices = [union_index[value] for value in appended_values]
    if frozen_union_indices != list(range(len(frozen_values))):
        raise AssertionError("frozen union coordinates are not the source-order prefix")
    appended_new_union_indices = [
        index for index, value in enumerate(union_values) if value not in frozen_value_set
    ]
    appended_new_values = [union_values[index] for index in appended_new_union_indices]
    if len(union_values) != len(frozen_values) + len(appended_new_values):
        raise AssertionError("union coordinate ownership does not partition distinct values")
    print(
        f"normalization frozen={len(frozen_values)} appended={len(appended_values)} "
        f"union={len(union_values)} shared={len(shared_values)} appended_new={len(appended_new_values)}",
        flush=True,
    )

    union_basis, union_basis_operations = deterministic_gcd_basis(union_values, "union exact-value basis")
    union_basis_validation = validate_basis(union_values, union_basis)
    union_rows, union_row_normalization = public_parity_rows(union_basis, len(union_values))
    frozen_rows = restrict_and_remap_rows(union_rows, frozen_union_indices)
    appended_standalone_rows = restrict_and_remap_rows(union_rows, appended_standalone_union_indices)
    appended_new_rows = restrict_and_remap_rows(union_rows, appended_new_union_indices)
    print(f"union exact basis blocks={len(union_basis)} public rows={len(union_rows)}", flush=True)

    frozen_system, frozen_kernel = decode_system(
        "frozen_standalone_and_union_owned", frozen_rows, frozen_values, modulus
    )
    appended_standalone_system, appended_standalone_kernel = decode_system(
        "appended_standalone", appended_standalone_rows, appended_values, modulus
    )
    appended_new_system, appended_new_kernel = decode_system(
        "globally_new_appended_coordinates", appended_new_rows, appended_new_values, modulus
    )
    union_system, union_kernel = decode_system("global_union", union_rows, union_values, modulus)

    embedded_frozen_kernel = [remap_vector(vector, frozen_union_indices) for vector in frozen_kernel]
    embedded_appended_new_kernel = [
        remap_vector(vector, appended_new_union_indices) for vector in appended_new_kernel
    ]
    for vector in embedded_frozen_kernel + embedded_appended_new_kernel:
        if any((row & vector).bit_count() & 1 for row in union_rows):
            raise AssertionError("embedded one-layer kernel vector is outside the union kernel")
    direct_sum_span = BinarySpan()
    for vector in embedded_frozen_kernel + embedded_appended_new_kernel:
        if not direct_sum_span.add(vector):
            raise AssertionError("disjoint one-layer kernel bases are not independent")
    direct_sum_dimension = len(embedded_frozen_kernel) + len(embedded_appended_new_kernel)
    if direct_sum_span.rank != direct_sum_dimension:
        raise AssertionError("one-layer direct-sum dimension is wrong")

    quotient_basis: list[int] = []
    full_span = direct_sum_span
    for vector in union_kernel:
        if full_span.add(vector):
            quotient_basis.append(vector)
    quotient_dimension = len(union_kernel) - direct_sum_dimension
    if len(quotient_basis) != quotient_dimension or full_span.rank != len(union_kernel):
        raise AssertionError("cross-layer quotient basis is incomplete")

    quotient_results = []
    for index, vector in enumerate(quotient_basis):
        result = decode_vector(vector, union_values, modulus, index)
        selected = [int(column) for column in result["selected_columns"]]
        result["selected_frozen_owned_coordinate_count"] = sum(
            column < len(frozen_values) for column in selected
        )
        result["selected_appended_owned_coordinate_count"] = sum(
            column >= len(frozen_values) for column in selected
        )
        quotient_results.append(result)
    quotient_root_map = root_class_span(
        [int(result["root_residue_mod_N"]) for result in quotient_results], modulus
    )

    rank_frozen = int(frozen_system["rank"])
    rank_appended_new = int(appended_new_system["rank"])
    rank_union = int(union_system["rank"])
    kernel_frozen_dimension = int(frozen_system["kernel_dimension"])
    kernel_appended_new_dimension = int(appended_new_system["kernel_dimension"])
    kernel_union_dimension = int(union_system["kernel_dimension"])
    dimension_identity_left = (
        kernel_union_dimension - kernel_frozen_dimension - kernel_appended_new_dimension
    )
    dimension_identity_right = rank_frozen + rank_appended_new - rank_union
    if dimension_identity_left != dimension_identity_right or dimension_identity_left != quotient_dimension:
        raise AssertionError("cross-layer dimension identity failed")

    frozen_root_rank = int(frozen_system["normalized_root_map"]["rank_mod_global_sign"])
    appended_new_root_rank = int(appended_new_system["normalized_root_map"]["rank_mod_global_sign"])
    union_root_rank = int(union_system["normalized_root_map"]["rank_mod_global_sign"])
    root_map_descends = frozen_root_rank == 0 and appended_new_root_rank == 0
    if root_map_descends and int(quotient_root_map["rank_mod_global_sign"]) != union_root_rank:
        raise AssertionError("quotient root-map rank does not equal the union rank")
    every_useful_union_coordinate_dependency_crosses = frozen_root_rank == 0 and appended_new_root_rank == 0

    record_digest_data: list[int] = []
    for record in records:
        record_digest_data.extend(
            (
                int(record["record_index"]),
                0 if record["layer"] == "frozen" else 1,
                int(record["residue"]),
                int(record["inverse"]),
                int(record["relation_value"]),
                int(record["minus_gcd"]),
                int(record["plus_gcd"]),
            )
        )

    result = {
        "reconstruction_status": "PASS",
        "public_instance": {
            "N": modulus,
            "n": bit_length,
            "bound": bound,
            "source_stop_relation_count": stop_count,
            "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
            "trial_gcd_range_start": 2,
            "trial_gcd_range_end": bound,
            "trial_nonunit_count": len(trial_nonunits),
        },
        "ordered_source": {
            "seed_record_count": seed_record_count,
            "seed_basis_blocks": [block for block, _ in seed_basis],
            "seed_basis_operations": seed_basis_operations,
            "seed_basis_validation": seed_basis_validation,
            "frozen_pairs": [[left, right] for left, right in frozen_pairs],
            "frozen_pair_count": len(frozen_pairs),
            "frozen_trajectory_attempt_count": frozen_attempt_count,
            "frozen_trajectory_duplicate_residue_count": frozen_duplicate_count,
            "frozen_layer_raw_record_count_including_seeds": len(frozen_records),
            "appended_attempt_count": appended_attempt_count,
            "appended_duplicate_residue_count": appended_duplicate_count,
            "appended_raw_record_count": len(appended_records),
            "total_attempt_count": source_attempts,
            "total_duplicate_residue_count": source_duplicates,
            "total_retained_record_count": len(records),
            "endpoint_count": endpoint_count,
            "exact_stop_reached": len(records) == stop_count,
            "record_sequence_sha256": hash_integer_sequence(record_digest_data),
            "direct_sign_screen_counts": screen_counts,
            "nonunit_sign_screens": nonunit_screens,
        },
        "exact_value_coordinates": {
            "frozen_standalone": frozen_normalization,
            "appended_standalone": appended_normalization,
            "global_union": union_normalization,
            "shared_distinct_nonunit_exact_value_count": len(shared_values),
            "shared_distinct_nonunit_exact_values_sha256": hash_integer_sequence(sorted(shared_values)),
            "union_frozen_owned_coordinate_count": len(frozen_values),
            "union_newly_appended_coordinate_count": len(appended_new_values),
            "union_newly_appended_values_sha256": hash_integer_sequence(appended_new_values),
        },
        "factor_free_union_basis": {
            "operations": union_basis_operations,
            "validation": union_basis_validation,
            "row_normalization": union_row_normalization,
        },
        "complete_systems": {
            "frozen_standalone": frozen_system,
            "appended_standalone": appended_standalone_system,
            "globally_new_appended_coordinates": appended_new_system,
            "global_union": union_system,
        },
        "cross_layer_quotient": {
            "K_F_dimension": kernel_frozen_dimension,
            "K_A_new_dimension": kernel_appended_new_dimension,
            "K_U_dimension": kernel_union_dimension,
            "K_F_direct_sum_K_A_dimension": direct_sum_dimension,
            "quotient_dimension": quotient_dimension,
            "dimension_identity_left": dimension_identity_left,
            "dimension_identity_right": dimension_identity_right,
            "dimension_identity_verified": True,
            "quotient_basis_sha256_little_endian_fixed_width": hash_bitsets(
                quotient_basis, len(union_values)
            ),
            "quotient_basis_results": quotient_results,
            "one_layer_normalized_root_maps_are_trivial": root_map_descends,
            "normalized_root_map_descends_to_quotient": root_map_descends,
            "quotient_normalized_root_map": quotient_root_map,
        },
        "answers": {
            "frozen_layer_alone_contains_useful_dependency": bool(
                frozen_system["contains_useful_dependency"]
            ),
            "appended_layer_alone_contains_useful_dependency": bool(
                appended_standalone_system["contains_useful_dependency"]
            ),
            "global_union_contains_useful_dependency": bool(
                union_system["contains_useful_dependency"]
            ),
            "globally_new_appended_coordinates_contain_useful_dependency": bool(
                appended_new_system["contains_useful_dependency"]
            ),
            "every_useful_union_coordinate_dependency_crosses_first_occurrence_layer_boundary": (
                every_useful_union_coordinate_dependency_crosses
            ),
            "coordinate_boundary_note": (
                "Cross-layer means the globally deduplicated first-occurrence coordinates. "
                "A value first retained in the frozen layer stays frozen-owned even if an appended record repeats it."
            ),
        },
        "factor_free_completeness": {
            "factorization_used": False,
            "primality_test_used": False,
            "known_factor_used": False,
            "allowed_operations_used": [
                "integer gcd",
                "modular inverse",
                "modular exponentiation",
                "exact integer nth-root extraction",
                "exact integer square root",
                "binary Gaussian elimination",
                "finite root-class span enumeration modulo global sign",
            ],
            "reason": (
                "Pairwise-coprime perfect-power-free blocks reconstruct every union value. "
                "Each rational-prime parity row is either its block signature row or zero, and each nonzero block row "
                "is realized by an odd internal exponent. Restriction therefore gives the complete row space of every system. "
                "The reported independent nullspace vectors have dimension columns minus rank."
            ),
        },
        "fixed_instance_boundary": {
            "fixed_instance_only": True,
            "statement": (
                f"This result concerns only N={modulus}, n={bit_length}, bound={bound}, stop={stop_count}, "
                "the specified source order, and first-occurrence coordinate convention. It gives no stop selector, "
                "other-input theorem, density law, success probability, or polynomial bit-time factoring algorithm."
            ),
        },
        "elapsed_seconds_decoder": time.monotonic() - started,
    }
    arguments.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {arguments.output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
