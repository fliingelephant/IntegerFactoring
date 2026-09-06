#!/usr/bin/env python3
"""Registered F157-D01 sparse decorated-section feedback capability scan."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import gc
import hashlib
import json
import math
from pathlib import Path
import time

from gmpy2 import gcd as gmp_gcd
from gmpy2 import mpz


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unsigned_bytes(value: int) -> bytes:
    size = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(size, "big")


def hash_integer_sequence(values) -> str:
    digest = hashlib.sha256()
    count = 0
    for value in values:
        payload = unsigned_bytes(int(value))
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)
        count += 1
    digest.update(count.to_bytes(8, "big"))
    return digest.hexdigest()


def write_json(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def integer_nth_root(value: int, exponent: int) -> int:
    if exponent == 2:
        return math.isqrt(value)
    low = 1 << ((value.bit_length() - 1) // exponent)
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


ODD_PRIME_EXPONENTS = (53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3)


def squareclass_primitive(value: int) -> tuple[int, str]:
    """Remove an exact square and exact odd-power redundancy, without factoring."""
    if math.isqrt(value) ** 2 == value:
        return 1, "square"
    changed = False
    while True:
        for exponent in ODD_PRIME_EXPONENTS:
            if exponent > value.bit_length():
                continue
            root = integer_nth_root(value, exponent)
            if pow(root, exponent) == value:
                value = root
                changed = True
                if math.isqrt(value) ** 2 == value:
                    return 1, "square"
                break
        else:
            return value, "odd_power" if changed else "primitive"


COMPACT_MASK_THRESHOLD = 2048
CompactMask = tuple[int, ...] | int


def compact_mask_members(mask: CompactMask):
    if isinstance(mask, tuple):
        yield from mask
        return
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def compact_mask_size(mask: CompactMask) -> int:
    return len(mask) if isinstance(mask, tuple) else mask.bit_count()


def compact_mask_from_int(mask: int) -> CompactMask:
    if mask.bit_count() > COMPACT_MASK_THRESHOLD:
        return mask
    return tuple(compact_mask_members(mask))


def compact_mask_xor(left: CompactMask, right: CompactMask) -> CompactMask:
    if isinstance(left, tuple) and isinstance(right, tuple):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            elif right[j] < left[i]:
                result.append(right[j])
                j += 1
            else:
                i += 1
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        if len(result) <= COMPACT_MASK_THRESHOLD:
            return tuple(result)
        value = 0
        for column in result:
            value |= 1 << column
        return value
    left_value = left if isinstance(left, int) else sum(1 << column for column in left)
    right_value = right if isinstance(right, int) else sum(1 << column for column in right)
    return compact_mask_from_int(left_value ^ right_value)


def vector_xor(left: frozenset[int], right: frozenset[int]) -> frozenset[int]:
    return left.symmetric_difference(right)


def product_tree(values: list[int]) -> list[list[int]]:
    levels = [[mpz(value) for value in values]]
    while len(levels[-1]) > 1:
        old = levels[-1]
        levels.append(
            [
                old[index] * old[index + 1]
                if index + 1 < len(old)
                else old[index]
                for index in range(0, len(old), 2)
            ]
        )
    return levels


PRODUCT_FOREST_LEAVES = 8192


def product_forest(values: list[int]) -> list[list[list[int]]]:
    return [
        product_tree(values[start : start + PRODUCT_FOREST_LEAVES])
        for start in range(0, len(values), PRODUCT_FOREST_LEAVES)
    ]


def complement_gcds(values: list[int]) -> tuple[list[int], list[list[list[int]]]]:
    if len(values) == 1:
        return [1], [[values]]
    forest = product_forest(values)
    roots = [levels[-1][0] for levels in forest]
    result = []
    for tree_index, levels in enumerate(forest):
        root = roots[tree_index]
        root_complement = mpz(1)
        for other_index, other_root in enumerate(roots):
            if other_index != tree_index:
                root_complement = root_complement * (other_root % root) % root
        complements = [root_complement]
        for level_index in range(len(levels) - 1, 0, -1):
            children = levels[level_index - 1]
            child_complements = [mpz(0)] * len(children)
            for parent_index, parent_complement in enumerate(complements):
                left_index = 2 * parent_index
                left = children[left_index]
                if left_index + 1 < len(children):
                    right = children[left_index + 1]
                    child_complements[left_index] = (
                        (parent_complement % left) * (right % left)
                    ) % left
                    child_complements[left_index + 1] = (
                        (parent_complement % right) * (left % right)
                    ) % right
                else:
                    child_complements[left_index] = parent_complement % left
            complements = child_complements
        result.extend(
            int(gmp_gcd(value, other))
            for value, other in zip(levels[0], complements)
        )
    return result, forest


def descend_overlap(value: int, levels: list[list[int]], node: int, level: int) -> int:
    while level > 0:
        children = levels[level - 1]
        left = 2 * node
        right = left + 1
        if gmp_gcd(value, children[left]) > 1:
            node = left
        elif right < len(children) and gmp_gcd(value, children[right]) > 1:
            node = right
        else:
            raise AssertionError("overlap tree lost a certified divisor")
        level -= 1
    return node


def overlap_partner(
    index: int, value: int, forest: list[list[list[int]]]
) -> int:
    tree_index, local_index = divmod(index, PRODUCT_FOREST_LEAVES)
    levels = forest[tree_index]
    node = local_index
    for level_index in range(len(levels) - 1):
        sibling = node ^ 1
        if (
            sibling < len(levels[level_index])
            and gmp_gcd(value, levels[level_index][sibling]) > 1
        ):
            partner = descend_overlap(value, levels, sibling, level_index)
            if partner == local_index:
                raise AssertionError("overlap search returned its own leaf")
            return tree_index * PRODUCT_FOREST_LEAVES + partner
        node //= 2
    for other_tree, other_levels in enumerate(forest):
        if other_tree == tree_index:
            continue
        if gmp_gcd(value, other_levels[-1][0]) > 1:
            partner = descend_overlap(
                value, other_levels, 0, len(other_levels) - 1
            )
            return other_tree * PRODUCT_FOREST_LEAVES + partner
    raise AssertionError("fully covered entry has no other overlap")


def normalize_entries(
    entries: list[tuple[int, CompactMask]], stats: Counter
) -> list[tuple[int, CompactMask]]:
    grouped: dict[int, CompactMask] = {}
    for value, mask in entries:
        if value <= 1 or not mask:
            stats["discarded_trivial_entries"] += 1
            continue
        primitive, kind = squareclass_primitive(value)
        if kind == "square":
            stats["discarded_square_entries"] += 1
            continue
        if kind == "odd_power":
            stats["odd_power_reductions"] += 1
        old = grouped.get(primitive)
        grouped[primitive] = mask if old is None else compact_mask_xor(old, mask)
    normalized = []
    for value, mask in grouped.items():
        if mask:
            normalized.append((value, mask))
        else:
            stats["cancelled_equal_value_entries"] += 1
    normalized.sort(key=lambda item: item[0])
    return normalized


def factor_free_parity_basis(
    endpoints: list[tuple[int, int]], relation_count: int, label: str
) -> tuple[list[int], list[CompactMask], dict[str, object]]:
    """Return a complete pairwise-coprime nonsquare labelled basis."""
    stats: Counter = Counter()
    active: list[tuple[int, CompactMask]] = [
        (value, (column,)) for value, column in endpoints if value > 1
    ]
    final: list[tuple[int, CompactMask]] = []
    round_index = 0
    while active:
        round_index += 1
        active = normalize_entries(active, stats)
        if not active:
            break
        print(
            f"{label}: normalized round {round_index}, entries={len(active)}, "
            f"mask_incidences={sum(compact_mask_size(mask) for _, mask in active)}, "
            f"large_masks={sum(isinstance(mask, int) for _, mask in active)}",
            flush=True,
        )
        values = [value for value, _ in active]
        gcds, levels = complement_gcds(values)
        stats["batch_rounds"] += 1
        stats["batch_entries"] += len(active)
        next_active: list[tuple[int, CompactMask]] = []
        stuck_indices = []
        for index, ((value, mask), divisor) in enumerate(zip(active, gcds)):
            if divisor == 1:
                final.append((value, mask))
                stats["finalized_entries"] += 1
            elif divisor < value:
                next_active.extend(((divisor, mask), (value // divisor, mask)))
                stats["batch_proper_splits"] += 1
            else:
                stuck_indices.append(index)

        if next_active:
            next_active.extend(active[index] for index in stuck_indices)
            active = next_active
        elif stuck_indices:
            used: set[int] = set()
            forced: list[tuple[int, CompactMask]] = []
            for index in stuck_indices:
                if index in used:
                    continue
                value, mask = active[index]
                partner = overlap_partner(index, value, levels)
                if partner in used:
                    continue
                other, other_mask = active[partner]
                divisor = math.gcd(value, other)
                if divisor == 1:
                    raise AssertionError("forced overlap pair is coprime")
                used.add(index)
                used.add(partner)
                forced.extend(
                    (
                        (divisor, compact_mask_xor(mask, other_mask)),
                        (value // divisor, mask),
                        (other // divisor, other_mask),
                    )
                )
                stats["forced_pair_splits"] += 1
            forced.extend(active[index] for index in stuck_indices if index not in used)
            active = forced
        else:
            active = []

        del gcds, levels, values
        gc.collect()

        print(
            f"{label}: refine round {round_index}, active={len(active)}, "
            f"final={len(final)}, batch_splits={stats['batch_proper_splits']}, "
            f"forced={stats['forced_pair_splits']}",
            flush=True,
        )
        if round_index > 256:
            raise AssertionError("factor-free refinement exceeded 256 rounds")

    final.sort(key=lambda item: item[0])
    blocks = [value for value, _ in final]
    masks = [mask for _, mask in final]
    if any(not mask for mask in masks):
        raise AssertionError("terminal parity block has an empty row")
    if any(math.isqrt(block) ** 2 == block for block in blocks):
        raise AssertionError("terminal parity block is a square")
    if blocks:
        gcds, _ = complement_gcds(blocks)
        if any(divisor != 1 for divisor in gcds):
            raise AssertionError("terminal parity blocks are not pairwise coprime")
    if any(
        column < 0 or column >= relation_count
        for mask in masks
        for column in compact_mask_members(mask)
    ):
        raise AssertionError("terminal row contains an invalid column")
    stats["terminal_blocks"] = len(blocks)
    stats["terminal_row_incidences"] = sum(compact_mask_size(mask) for mask in masks)
    stats["terminal_distinct_rows"] = len(set(masks))
    stats["maximum_terminal_row_degree"] = max(
        (compact_mask_size(mask) for mask in masks), default=0
    )
    return blocks, masks, dict(stats)


def deterministic_gcd_basis(values: list[int]) -> list[tuple[int, dict[int, int]]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    while stack:
        value, signature = stack.pop()
        if value == 1:
            continue
        multiplier = 1
        for exponent in range(value.bit_length() - 1, 1, -1):
            root = integer_nth_root(value, exponent)
            if pow(root, exponent) == value:
                value = root
                multiplier = exponent
                signature = {
                    index: old_exponent * exponent
                    for index, old_exponent in signature.items()
                }
                break
        for position, (old, old_signature) in enumerate(basis):
            divisor = math.gcd(value, old)
            if divisor == 1:
                continue
            basis.pop(position)
            if value == old:
                merged = signature.copy()
                for index, exponent in old_signature.items():
                    merged[index] = merged.get(index, 0) + exponent
                stack.append((value, merged))
            else:
                stack.extend(
                    (
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, old_signature),
                        (old // divisor, old_signature),
                    )
                )
            break
        else:
            basis.append((value, signature))
    basis.sort(key=lambda item: item[0])
    return basis


def frozen_seed_pairs(modulus: int, n: int) -> list[tuple[int, int]]:
    endpoints = []
    for seed in range(2, n + 1):
        endpoints.extend((seed, pow(seed, -1, modulus)))
    basis = deterministic_gcd_basis(endpoints)
    pairs = []
    for seed_index in range(n - 1):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in basis
            if signature.get(left_endpoint, 0) + signature.get(right_endpoint, 0) > 0
        ]
        if not support:
            raise AssertionError("empty frozen seed support")
        pairs.append((support[0], 1 if len(support) == 1 else support[1]))
    return pairs


def generate_base(instance: dict[str, object]) -> tuple[list[dict[str, int]], dict[str, object]]:
    modulus = int(instance["N"])
    mode = str(instance["mode"])
    n = modulus.bit_length()
    bound = n * n
    seen: set[int] = set()
    seed_records: list[dict[str, int]] = []
    frozen_records: list[dict[str, int]] = []
    attempts = 0
    duplicates = 0
    screens = Counter()
    proper_screens = []

    def attempt(residue: int, layer: str) -> None:
        nonlocal attempts, duplicates
        attempts += 1
        if residue in seen:
            duplicates += 1
            return
        seen.add(residue)
        common = math.gcd(residue, modulus)
        if common != 1:
            raise AssertionError(f"source residue has gcd {common} with N")
        inverse = pow(residue, -1, modulus)
        for sign, value in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(value, modulus)
            classification = "unit" if divisor == 1 else "improper" if divisor == modulus else "proper"
            screens[classification] += 1
            if classification == "proper":
                proper_screens.append({"sign": sign, "factor": divisor, "c": residue, "w": inverse})
        record = {"c": residue, "w": inverse, "A": residue * inverse}
        if layer == "seed":
            seed_records.append(record)
        else:
            frozen_records.append(record)

    for seed in range(2, n + 1):
        attempt(seed, "seed")
    pairs = frozen_seed_pairs(modulus, n)
    attempts_before = attempts
    duplicates_before = duplicates
    for left, right in pairs:
        left_power = 1
        right_power = 1
        for _ in range(bound + 1):
            attempt(left_power * right % modulus, "frozen")
            attempt(left * right_power % modulus, "frozen")
            left_power = left_power * left % modulus
            right_power = right_power * right % modulus

    if proper_screens:
        raise AssertionError(f"old frozen source has a proper direct screen: {proper_screens[0]}")
    raw_base = frozen_records if mode == "F111" else seed_records + frozen_records
    first: dict[int, dict[str, int]] = {}
    removed_units = 0
    removed_repeats = 0
    for record in raw_base:
        value = record["A"]
        if value == 1:
            removed_units += 1
        elif value in first:
            removed_repeats += 1
        else:
            first[value] = record
    records = list(first.values())
    if mode == "F111" and len(records) != int(instance["expected_base_columns"]):
        raise AssertionError(
            f"F111 normalized base count {len(records)} changed from "
            f"{instance['expected_base_columns']}"
        )
    if mode == "F118" and len(raw_base) != int(instance["expected_old_columns"]):
        raise AssertionError("F118 old frozen column count changed")
    return records, {
        "n": n,
        "B": bound,
        "seed_records": len(seed_records),
        "frozen_pair_count": len(pairs),
        "total_attempts": attempts,
        "total_duplicates": duplicates,
        "frozen_attempts": attempts - attempts_before,
        "frozen_duplicates": duplicates - duplicates_before,
        "raw_base_records": len(raw_base),
        "distinct_nonunit_exact_values": len(records),
        "removed_unit_values": removed_units,
        "removed_repeated_exact_values": removed_repeats,
        "old_direct_screen_counts": dict(screens),
        "proper_old_direct_screens": len(proper_screens),
        "pair_sha256": hash_integer_sequence(value for pair in pairs for value in pair),
        "exact_value_sha256": hash_integer_sequence(record["A"] for record in records),
    }


def star(
    left_v: frozenset[int],
    left_z: int,
    right_v: frozenset[int],
    right_z: int,
    inverse_blocks: list[int],
    modulus: int,
) -> tuple[frozenset[int], int]:
    result = left_z * right_z % modulus
    for block in left_v.intersection(right_v):
        result = result * inverse_blocks[block] % modulus
    return vector_xor(left_v, right_v), result


def build_lifts_and_decode(
    modulus: int,
    records: list[dict[str, int]],
    blocks: list[int],
    row_masks: list[CompactMask],
) -> tuple[list[frozenset[int]], list[int], list[int], dict[str, object]]:
    column_count = len(records)
    column_blocks: list[list[int]] = [[] for _ in range(column_count)]
    q_products = [1] * column_count
    for block_index, (block, mask) in enumerate(zip(blocks, row_masks)):
        if math.gcd(block, modulus) != 1:
            raise AssertionError("public parity block is not a unit modulo N")
        for column in compact_mask_members(mask):
            column_blocks[column].append(block_index)
            q_products[column] *= block

    vectors: list[frozenset[int]] = []
    lifts: list[int] = []
    for column, record in enumerate(records):
        value = record["A"]
        q_value = q_products[column]
        if value % q_value:
            raise AssertionError("public squareclass product does not divide its exact relation")
        quotient = value // q_value
        half = math.isqrt(quotient)
        if half * half != quotient:
            raise AssertionError("factor-free coordinates leave a nonsquare quotient")
        if math.gcd(half, modulus) != 1:
            raise AssertionError("factor-free half-root is not a unit")
        vector = frozenset(column_blocks[column])
        lift = pow(half, -1, modulus)
        q_mod = 1
        for block_index in vector:
            q_mod = q_mod * blocks[block_index] % modulus
        if pow(lift, 2, modulus) != q_mod:
            raise AssertionError("actual decorated lift does not square to Q(v)")
        vectors.append(vector)
        lifts.append(lift)

    inverse_blocks = [pow(block, -1, modulus) for block in blocks]
    pivots: dict[int, tuple[frozenset[int], int]] = {}
    selected = []
    dependency_roots = Counter()
    non_global = []
    maximum_reduced_support = 0
    for column, (source_v, source_z) in enumerate(zip(vectors, lifts)):
        parity = source_v
        lift = source_z
        while parity:
            maximum_reduced_support = max(maximum_reduced_support, len(parity))
            pivot = max(parity)
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = (parity, lift)
                selected.append(column)
                break
            parity, lift = star(parity, lift, known[0], known[1], inverse_blocks, modulus)
        else:
            if pow(lift, 2, modulus) != 1:
                raise AssertionError("decorated dependency is not a root of one")
            if lift == 1:
                dependency_roots["global_plus"] += 1
            elif lift == modulus - 1:
                dependency_roots["global_minus"] += 1
            else:
                dependency_roots["non_global"] += 1
                non_global.append(
                    {
                        "column": column,
                        "root": lift,
                        "gcd_minus": math.gcd(lift - 1, modulus),
                        "gcd_plus": math.gcd(lift + 1, modulus),
                    }
                )
    return vectors, lifts, selected, {
        "columns_after_exact_value_dedup": column_count,
        "rank": len(pivots),
        "kernel_nullity_after_exact_value_dedup": column_count - len(pivots),
        "selected_basis_records": len(selected),
        "global_plus_basis_roots": dependency_roots["global_plus"],
        "global_minus_basis_roots": dependency_roots["global_minus"],
        "non_global_basis_roots": dependency_roots["non_global"],
        "normalized_root_image_dimension": 1 if non_global else 0,
        "maximum_reduced_support": maximum_reduced_support,
        "selected_source_column_sha256": hash_integer_sequence(selected),
    }


def direct_screen(
    modulus: int,
    vector: frozenset[int],
    lift: int,
    blocks: list[int],
) -> dict[str, object]:
    inverse = pow(lift, -1, modulus)
    minus = math.gcd(lift - inverse, modulus)
    plus = math.gcd(lift + inverse, modulus)
    q_mod = 1
    for block in vector:
        q_mod = q_mod * blocks[block] % modulus
    identity_minus = math.gcd(q_mod - 1, modulus)
    identity_plus = math.gcd(q_mod + 1, modulus)
    if (minus, plus) != (identity_minus, identity_plus):
        raise AssertionError("public dense-screen gcd identity failed")
    return {
        "z": lift,
        "w": inverse,
        "gcd_minus": minus,
        "gcd_plus": plus,
        "q_mod_N": q_mod,
        "proper": (1 < minus < modulus) or (1 < plus < modulus),
    }


def scan_feedback(
    modulus: int,
    factors: tuple[int, int],
    blocks: list[int],
    vectors: list[frozenset[int]],
    lifts: list[int],
    selected: list[int],
) -> dict[str, object]:
    inverse_blocks = [pow(block, -1, modulus) for block in blocks]
    basis_vectors = [vectors[column] for column in selected]
    basis_lifts = [lifts[column] for column in selected]
    support_one_hits = []
    for basis_index, (source_column, vector, lift) in enumerate(
        zip(selected, basis_vectors, basis_lifts)
    ):
        screen = direct_screen(modulus, vector, lift, blocks)
        if screen["proper"]:
            support_one_hits.append(
                {
                    "basis_index": basis_index,
                    "source_column": source_column,
                    "parity_support": len(vector),
                }
                | screen
            )

    basis_count = len(selected)
    degree = Counter(block for vector in basis_vectors for block in vector)
    light_degree_cap = 256
    heavy_blocks = {block for block, count in degree.items() if count > light_degree_cap}
    heavy_sets = [vector.intersection(heavy_blocks) for vector in basis_vectors]
    heavy_vectors = [tuple(sorted(vector)) for vector in heavy_sets]
    light_vectors = [
        frozenset(
            block
            for block in vector
            if 1 < degree[block] <= light_degree_cap
        )
        for vector in basis_vectors
    ]
    maximum_shared = max(
        (sum(degree[block] > 1 for block in vector) for vector in basis_vectors),
        default=0,
    )
    maximum_heavy = max(map(len, heavy_vectors), default=0)
    subset_count = sum(1 << len(vector) for vector in heavy_vectors)
    light_postings: dict[int, list[int]] = defaultdict(list)
    for basis_index, vector in enumerate(light_vectors):
        for block in vector:
            light_postings[block].append(basis_index)

    q_local = []
    for factor in factors:
        if modulus % factor or factor <= 1 or factor >= modulus:
            raise AssertionError("disclosed indexing factor is invalid")
        local_values = [pow(lift, 2, factor) for lift in basis_lifts]
        q_local.append(local_values)

    joint_by_first: dict[int, dict[int, list[int]]] = defaultdict(
        lambda: defaultdict(list)
    )
    joint_by_second: dict[int, dict[int, list[int]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for index, (first_value, second_value) in enumerate(zip(*q_local)):
        joint_by_first[first_value][second_value].append(index)
        joint_by_second[second_value][first_value].append(index)

    block_local = [
        [block % factor for block in blocks]
        for factor in factors
    ]
    inverse_square_block_local = [
        [pow(value * value % factor, -1, factor) for value in values]
        for factor, values in zip(factors, block_local)
    ]
    candidate_pairs: set[int] = set()
    lookup_occurrences = 0
    index_queries = 0
    for left in range(basis_count):
        heavy = heavy_vectors[left]
        left_inverses = [pow(q_local[position][left], -1, factor) for position, factor in enumerate(factors)]
        intersection: set[int] = set()

        def visit(position: int, products: tuple[int, int]) -> None:
            nonlocal lookup_occurrences, index_queries
            if position == len(heavy):
                frozen_intersection = frozenset(intersection)
                base_targets = tuple(
                    products[factor_position]
                    * products[factor_position]
                    * left_inverses[factor_position]
                    % factor
                    for factor_position, factor in enumerate(factors)
                )
                for sign in (1, -1):
                    first_target = sign * base_targets[0] % factors[0]
                    second_target = sign * base_targets[1] % factors[1]
                    index_queries += 2
                    first_buckets = joint_by_first.get(first_target, {})
                    second_buckets = joint_by_second.get(second_target, {})
                    for other_second, matches in first_buckets.items():
                        if other_second == second_target:
                            continue
                        lookup_occurrences += len(matches)
                        for right in matches:
                            if right <= left:
                                continue
                            if not light_vectors[left].isdisjoint(light_vectors[right]):
                                continue
                            if heavy_sets[left].intersection(heavy_sets[right]) == frozen_intersection:
                                candidate_pairs.add(left * basis_count + right)
                    for other_first, matches in second_buckets.items():
                        if other_first == first_target:
                            continue
                        lookup_occurrences += len(matches)
                        for right in matches:
                            if right <= left:
                                continue
                            if not light_vectors[left].isdisjoint(light_vectors[right]):
                                continue
                            if heavy_sets[left].intersection(heavy_sets[right]) == frozen_intersection:
                                candidate_pairs.add(left * basis_count + right)
                return
            visit(position + 1, products)
            block = heavy[position]
            intersection.add(block)
            visit(
                position + 1,
                tuple(
                    products[factor_position] * block_local[factor_position][block] % factor
                    for factor_position, factor in enumerate(factors)
                ),
            )
            intersection.remove(block)

        visit(0, (1, 1))
        if left % 10_000 == 0:
            print(
                f"N={modulus}: support-two heavy index left={left}/{basis_count}, "
                f"queries={index_queries}, candidates={len(candidate_pairs)}",
                flush=True,
            )

    light_pair_occurrences = 0
    light_owned_pairs = 0
    for posting_index, block in enumerate(sorted(light_postings)):
        posting = light_postings[block]
        for left_position, left in enumerate(posting):
            for right in posting[left_position + 1 :]:
                light_pair_occurrences += 1
                common = basis_vectors[left].intersection(basis_vectors[right])
                common_light = [
                    common_block
                    for common_block in common
                    if 1 < degree[common_block] <= light_degree_cap
                ]
                if min(common_light) != block:
                    continue
                light_owned_pairs += 1
                local_pair = []
                for factor_position, factor in enumerate(factors):
                    q_pair = q_local[factor_position][left] * q_local[factor_position][right] % factor
                    for common_block in common:
                        q_pair = (
                            q_pair
                            * inverse_square_block_local[factor_position][common_block]
                            % factor
                        )
                    local_pair.append(q_pair)
                minus_proper = (local_pair[0] == 1) != (local_pair[1] == 1)
                plus_proper = (local_pair[0] == factors[0] - 1) != (
                    local_pair[1] == factors[1] - 1
                )
                possible = minus_proper or plus_proper
                if possible:
                    candidate_pairs.add(left * basis_count + right)
        if posting_index % 10_000 == 0:
            print(
                f"N={modulus}: support-two light index block={posting_index}/"
                f"{len(light_postings)}, owned_pairs={light_owned_pairs}, "
                f"candidates={len(candidate_pairs)}",
                flush=True,
            )

    support_two_hits = []
    candidate_no_proper = 0
    sorted_candidate_keys = sorted(candidate_pairs)
    for key in sorted_candidate_keys:
        left, right = divmod(key, basis_count)
        vector, lift = star(
            basis_vectors[left],
            basis_lifts[left],
            basis_vectors[right],
            basis_lifts[right],
            inverse_blocks,
            modulus,
        )
        screen = direct_screen(modulus, vector, lift, blocks)
        if screen["proper"]:
            common = basis_vectors[left].intersection(basis_vectors[right])
            common_product = math.prod(blocks[index] for index in common)
            support_two_hits.append(
                {
                    "basis_indices": [left, right],
                    "source_columns": [selected[left], selected[right]],
                    "left_parity_support": len(basis_vectors[left]),
                    "right_parity_support": len(basis_vectors[right]),
                    "intersection_support": len(common),
                    "public_C": common_product,
                }
                | screen
            )
        else:
            candidate_no_proper += 1

    if candidate_no_proper:
        raise AssertionError(
            "factor-assisted asymmetric index retained a pair without a proper public gcd"
        )

    pair_count = basis_count * (basis_count - 1) // 2
    hit_pairs = len(support_two_hits)
    return {
        "support_one": {
            "exact_scanned_count": basis_count,
            "proper_hit_count": len(support_one_hits),
            "null_count": basis_count - len(support_one_hits),
            "hits": support_one_hits,
        },
        "support_two": {
            "exact_scanned_unordered_pair_count": pair_count,
            "factor_assisted_subset_states": subset_count,
            "factor_assisted_heavy_subset_states": subset_count,
            "factor_assisted_heavy_block_count": len(heavy_blocks),
            "factor_assisted_light_degree_cap": light_degree_cap,
            "factor_assisted_light_block_count": len(light_postings),
            "factor_assisted_light_pair_occurrences": light_pair_occurrences,
            "factor_assisted_light_owned_pairs": light_owned_pairs,
            "factor_assisted_index_queries": index_queries,
            "factor_assisted_lookup_occurrences": lookup_occurrences,
            "factor_assisted_candidate_pair_count": len(candidate_pairs),
            "indexed_candidates_without_proper_public_gcd": candidate_no_proper,
            "proper_hit_pair_count": hit_pairs,
            "null_pair_count": pair_count - hit_pairs,
            "maximum_shared_block_support": maximum_shared,
            "maximum_heavy_block_support": maximum_heavy,
            "candidate_pair_sha256": hash_integer_sequence(
                sorted_candidate_keys
            ),
            "hits": support_two_hits,
            "index_completeness": (
                "Pairs with a common light block are enumerated once under their least "
                "common light block. All other pairs have only a heavy intersection; "
                "that exact intersection is one enumerated heavy subset. For each "
                "sign, the joint two-factor index keeps exactly the asymmetric cases: "
                "Q_j = epsilon*C^2/Q_i modulo one disclosed factor but not the other. "
                "Thus every possible proper screen, and no globally same-sign screen, "
                "is replayed by a public star-product and gcd."
            ),
        },
    }


def analyze_instance(instance: dict[str, object]) -> dict[str, object]:
    started = time.monotonic()
    modulus = int(instance["N"])
    print(f"N={modulus}: generate frozen base", flush=True)
    records, source = generate_base(instance)
    exact_values = [(record["A"], column) for column, record in enumerate(records)]
    print(
        f"N={modulus}: factor-free refine {len(exact_values)} exact values for {len(records)} columns",
        flush=True,
    )
    blocks, masks, refinement = factor_free_parity_basis(
        exact_values, len(records), f"N={modulus}"
    )
    vectors, lifts, selected, decoder = build_lifts_and_decode(
        modulus, records, blocks, masks
    )
    if decoder["rank"] != int(instance["expected_old_rank"]):
        raise AssertionError(
            f"factor-free rank {decoder['rank']} != pinned old rank {instance['expected_old_rank']}"
        )
    if decoder["normalized_root_image_dimension"] != 0:
        raise AssertionError("registered frozen-null base has a non-global factor-free root")
    old_columns = (
        source["distinct_nonunit_exact_values"]
        if instance["mode"] == "F111"
        else source["raw_base_records"]
    )
    if old_columns - int(instance["expected_old_rank"]) != int(instance["expected_old_kernel_nullity"]):
        raise AssertionError("pinned old nullity comparison changed")
    print(
        f"N={modulus}: rank={decoder['rank']}, basis={len(selected)}, scan feedback",
        flush=True,
    )
    feedback = scan_feedback(
        modulus,
        (int(instance["p"]), int(instance["q"])),
        blocks,
        vectors,
        lifts,
        selected,
    )
    return {
        "N": modulus,
        "mode": instance["mode"],
        "source": source,
        "factor_free_basis": refinement
        | {
            "block_sha256": hash_integer_sequence(blocks),
            "row_degree_sha256": hash_integer_sequence(
                sorted(compact_mask_size(mask) for mask in masks)
            ),
            "all_exact_relations_reconstructed": True,
            "all_blocks_pairwise_coprime_nonsquare_units": True,
        },
        "old_decoder_comparison": decoder
        | {
            "pinned_old_columns": old_columns,
            "pinned_old_rank": int(instance["expected_old_rank"]),
            "pinned_old_kernel_nullity": int(instance["expected_old_kernel_nullity"]),
            "rank_matches": True,
            "old_normalized_root_image_zero": True,
        },
        "feedback": feedback,
        "elapsed_seconds": time.monotonic() - started,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--development-instance-index", type=int)
    arguments = parser.parse_args()
    started = time.monotonic()
    spec = json.loads(arguments.input.read_text())
    root = Path(__file__).resolve().parents[2]
    pin_paths = {
        "F111_RECONSTRUCT_INPUT.json": root / "experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_INPUT.json",
        "F111_RECONSTRUCT_LAYER_decoder_v1.py": root / "experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_LAYER_decoder_v1.py",
        "F111_RECONSTRUCT_LAYER_decoder_v2.py": root / "experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_LAYER_decoder_v2.py",
        "F118_OUTPUT.json": root / "experiments/F118_58bit_full_source_null_search/OUTPUT.json",
        "F118_scan_full_source.py": root / "experiments/F118_58bit_full_source_null_search/scan_full_source.py",
        "F156_PROOF.md": root / "experiments/F156_sparse_section_feedback_source/PROOF.md",
        "F156_STATEMENT.md": root / "experiments/F156_sparse_section_feedback_source/STATEMENT.md",
    }
    observed_pins = {name: sha256_file(path) for name, path in pin_paths.items()}
    if observed_pins != spec["pins"]:
        raise AssertionError("a pinned upstream source or input changed")
    results = []
    instances = spec["instances"]
    if arguments.development_instance_index is not None:
        instances = [instances[arguments.development_instance_index]]
    for instance in instances:
        results.append(analyze_instance(instance))
        write_json(
            arguments.output,
            {
                "status": "RUNNING",
                "role": "registered fixed-corpus F156 support-one/two capability scan",
                "pins": observed_pins,
                "instances": results,
                "elapsed_seconds": time.monotonic() - started,
            },
        )
    support_one_hits = sum(item["feedback"]["support_one"]["proper_hit_count"] for item in results)
    support_two_hits = sum(item["feedback"]["support_two"]["proper_hit_pair_count"] for item in results)
    payload = {
        "status": "PASS",
        "verdict": "CAPABILITY" if support_one_hits or support_two_hits else "FINITE_NULL",
        "role": "registered fixed-corpus F156 support-one/two capability scan",
        "pins": observed_pins,
        "instances": results,
        "summary": {
            "instance_count": len(results),
            "support_one_proper_hits": support_one_hits,
            "support_two_proper_hit_pairs": support_two_hits,
            "any_new_feedback_factor": bool(support_one_hits or support_two_hits),
            "claim_boundary": (
                "Fixed finite capability/null evidence only. Factor-assisted indexing is used "
                "only to locate all support-two direct-screen candidates. Every hit is "
                "constructed from the public factor-free basis and verified by direct gcd."
            ),
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    write_json(arguments.output, payload)
    print(json.dumps(payload["summary"], sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
