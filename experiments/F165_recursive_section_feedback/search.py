#!/usr/bin/env python3
"""Registered F165-D01 depth-two recursive decorated-section scan."""

from __future__ import annotations

import argparse
from collections import Counter
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time


EXPERIMENT_ID = "F165-D01"
CORPUS_SIZE = 64
PRIME_LOW = 10_000
PRIME_HIGH = 20_000
RECURSIVE_LEVELS = 2
SUPPORT_CAP = 2


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


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def construct_corpus() -> list[tuple[int, int]]:
    primes = [value for value in range(PRIME_LOW, PRIME_HIGH + 1) if is_prime(value)]
    pairs = []
    for p in primes:
        for q in primes:
            if p < q < 2 * p:
                pairs.append((p, q))
    pairs.sort()
    if len(pairs) < CORPUS_SIZE:
        raise AssertionError("fixed prime range has fewer than 64 admissible pairs")
    return pairs[:CORPUS_SIZE]


def load_pinned_core(root: Path, registration: dict[str, object]):
    observed = {
        relative: sha256_file(root / relative)
        for relative in registration["upstream_pins"]
    }
    if observed != registration["upstream_pins"]:
        raise AssertionError("a preregistered upstream interface changed")
    path = root / "experiments/F157_sparse_section_feedback_capability/search.py"
    spec = importlib.util.spec_from_file_location("f165_pinned_f157_core", path)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot load pinned factor-free core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, observed


def add_record(
    modulus: int,
    records: list[dict[str, object]],
    exact_index: dict[int, int],
    value: int,
    supplied_root: int,
    layer: str,
    origin: dict[str, object],
) -> tuple[bool, dict[str, int] | None]:
    old_column = exact_index.get(value)
    if old_column is None:
        exact_index[value] = len(records)
        records.append(
            {
                "A": value,
                "alpha": supplied_root,
                "first_layer": layer,
                "layers": [layer],
                "occurrence_count": 1,
                "first_origin": origin,
            }
        )
        return True, None
    old = records[old_column]
    ratio = supplied_root * pow(int(old["alpha"]), -1, modulus) % modulus
    if pow(ratio, 2, modulus) != 1:
        raise AssertionError("equal exact values supplied inconsistent roots")
    if ratio not in (1, modulus - 1):
        return False, {
            "root": ratio,
            "gcd_minus": math.gcd(ratio - 1, modulus),
            "gcd_plus": math.gcd(ratio + 1, modulus),
        }
    old["occurrence_count"] = int(old["occurrence_count"]) + 1
    if layer not in old["layers"]:
        old["layers"].append(layer)
    return False, None


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
    return left_v.symmetric_difference(right_v), result


def decode(
    modulus: int,
    records: list[dict[str, object]],
    core,
    label: str,
) -> dict[str, object]:
    endpoints = [
        (int(record["A"]), column)
        for column, record in enumerate(records)
        if int(record["A"]) > 1
    ]
    blocks, row_masks, refinement = core.factor_free_parity_basis(
        endpoints, len(records), label
    )
    column_blocks: list[list[int]] = [[] for _ in records]
    q_products = [1] * len(records)
    for block_index, (block, mask) in enumerate(zip(blocks, row_masks)):
        if math.gcd(block, modulus) != 1:
            raise AssertionError("factor-free parity block is not a unit")
        for column in core.compact_mask_members(mask):
            column_blocks[column].append(block_index)
            q_products[column] *= block

    vectors: list[frozenset[int]] = []
    lifts: list[int] = []
    halves: list[int] = []
    for column, record in enumerate(records):
        value = int(record["A"])
        q_value = q_products[column]
        if value % q_value:
            raise AssertionError("factor-free squareclass product does not divide A")
        quotient = value // q_value
        half = math.isqrt(quotient)
        if half * half != quotient:
            raise AssertionError("factor-free coordinates leave a nonsquare quotient")
        alpha = int(record["alpha"])
        lift = alpha * pow(half, -1, modulus) % modulus
        vector = frozenset(column_blocks[column])
        q_mod = 1
        for block_index in vector:
            q_mod = q_mod * blocks[block_index] % modulus
        if pow(lift, 2, modulus) != q_mod:
            raise AssertionError("decorated lift does not square to its parity value")
        vectors.append(vector)
        lifts.append(lift)
        halves.append(half)

    inverse_blocks = [pow(block, -1, modulus) for block in blocks]
    pivots: dict[int, tuple[frozenset[int], int]] = {}
    selected = []
    roots = Counter()
    first_non_global = None
    for column, (source_v, source_z) in enumerate(zip(vectors, lifts)):
        parity = source_v
        lift = source_z
        while parity:
            pivot = max(parity)
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = (parity, lift)
                selected.append(column)
                break
            parity, lift = star(
                parity, lift, known[0], known[1], inverse_blocks, modulus
            )
        else:
            if pow(lift, 2, modulus) != 1:
                raise AssertionError("kernel remainder is not a root of one")
            if lift == 1:
                roots["global_plus"] += 1
            elif lift == modulus - 1:
                roots["global_minus"] += 1
            else:
                roots["non_global"] += 1
                if first_non_global is None:
                    first_non_global = {
                        "column": column,
                        "root": lift,
                        "gcd_minus": math.gcd(lift - 1, modulus),
                        "gcd_plus": math.gcd(lift + 1, modulus),
                    }

    summary = {
        "columns": len(records),
        "rows": len(blocks),
        "rank": len(pivots),
        "nullity": len(records) - len(pivots),
        "global_plus_elimination_roots": roots["global_plus"],
        "global_minus_elimination_roots": roots["global_minus"],
        "non_global_elimination_roots": roots["non_global"],
        "normalized_root_image_nonzero": first_non_global is not None,
        "selected_basis_columns": len(selected),
        "exact_value_sha256": hash_integer_sequence(int(record["A"]) for record in records),
        "block_sha256": hash_integer_sequence(blocks),
        "selected_column_sha256": hash_integer_sequence(selected),
        "factor_free_refinement": refinement,
    }
    return {
        "summary": summary,
        "blocks": blocks,
        "row_masks": row_masks,
        "vectors": vectors,
        "lifts": lifts,
        "halves": halves,
        "selected": selected,
        "first_non_global": first_non_global,
    }


def dependency_support(
    modulus: int,
    context: dict[str, object],
    target_column: int,
    expected_root: int,
) -> list[int]:
    vectors = context["vectors"]
    lifts = context["lifts"]
    blocks = context["blocks"]
    inverse_blocks = [pow(block, -1, modulus) for block in blocks]
    pivots: dict[int, tuple[frozenset[int], int, int]] = {}
    for column, (source_v, source_z) in enumerate(zip(vectors, lifts)):
        parity = source_v
        lift = source_z
        combination = 1 << column
        while parity:
            pivot = max(parity)
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = (parity, lift, combination)
                break
            parity, lift = star(
                parity, lift, known[0], known[1], inverse_blocks, modulus
            )
            combination ^= known[2]
        else:
            if column == target_column:
                if lift != expected_root:
                    raise AssertionError("dependency replay root changed")
                return [
                    index
                    for index in range(column + 1)
                    if (combination >> index) & 1
                ]
        if column == target_column:
            break
    raise AssertionError("target dependency was not reconstructed")


def make_root_certificate(
    modulus: int,
    records: list[dict[str, object]],
    context: dict[str, object],
    layer: str,
) -> dict[str, object] | None:
    witness = context["first_non_global"]
    if witness is None:
        return None
    support = dependency_support(
        modulus, context, int(witness["column"]), int(witness["root"])
    )
    values = [int(records[column]["A"]) for column in support]
    product = math.prod(values)
    integer_root = math.isqrt(product)
    if integer_root * integer_root != product:
        raise AssertionError("reported parity dependency is not an exact square")
    normalized = integer_root % modulus
    if normalized != int(witness["root"]):
        raise AssertionError("exact square root and decorated root disagree")
    return {
        "type": "normalized_root",
        "layer": layer,
        "dependency_columns": support,
        "relation_values": values,
        "integer_root_mod_N": normalized,
        "gcd_minus": math.gcd(normalized - 1, modulus),
        "gcd_plus": math.gcd(normalized + 1, modulus),
    }


def make_component(
    records: list[dict[str, object]],
    context: dict[str, object],
    basis_position: int,
) -> dict[str, object]:
    column = int(context["selected"][basis_position])
    vector = context["vectors"][column]
    return {
        "basis_position": basis_position,
        "source_column": column,
        "exact_value": int(records[column]["A"]),
        "integer_half": int(context["halves"][column]),
        "block_values": [int(context["blocks"][index]) for index in sorted(vector)],
        "lift": int(context["lifts"][column]),
        "first_origin": records[column]["first_origin"],
    }


def make_section_certificate(
    modulus: int,
    records: list[dict[str, object]],
    context: dict[str, object],
    layer: str,
    subset: tuple[int, ...],
    z: int,
    w: int,
    gcd_minus: int,
    gcd_plus: int,
) -> dict[str, object]:
    return {
        "type": "section_direct",
        "layer": layer,
        "basis_subset": list(subset),
        "components": [make_component(records, context, index) for index in subset],
        "z": z,
        "w": w,
        "exact_value": z * w,
        "gcd_minus": gcd_minus,
        "gcd_plus": gcd_plus,
    }


def replay_n_only_certificate(modulus: int, certificate: dict[str, object]) -> dict[str, object]:
    kind = certificate["type"]
    if kind == "base_seed_direct":
        c = int(certificate["c"])
        w = pow(c, -1, modulus)
        minus = math.gcd(c - w, modulus)
        plus = math.gcd(c + w, modulus)
        passed = (
            w == int(certificate["w"])
            and c * w == int(certificate["exact_value"])
            and minus == int(certificate["gcd_minus"])
            and plus == int(certificate["gcd_plus"])
            and ((1 < minus < modulus) or (1 < plus < modulus))
        )
        return {"N_only": True, "passed": passed, "gcd_minus": minus, "gcd_plus": plus}
    if kind == "section_direct":
        components = certificate["components"]
        all_blocks = sorted({
            int(block)
            for component in components
            for block in component["block_values"]
        })
        for index, block in enumerate(all_blocks):
            if block <= 1 or math.gcd(block, modulus) != 1 or math.isqrt(block) ** 2 == block:
                raise AssertionError("certificate contains an invalid parity block")
            for other in all_blocks[index + 1 :]:
                if math.gcd(block, other) != 1:
                    raise AssertionError("certificate parity blocks are not coprime")
        component_sets = []
        component_lifts = []
        for component in components:
            values = [int(value) for value in component["block_values"]]
            half = int(component["integer_half"])
            exact = int(component["exact_value"])
            lift = int(component["lift"])
            if exact != half * half * math.prod(values):
                raise AssertionError("certificate exact decomposition failed")
            if exact % modulus != 1:
                raise AssertionError("certificate relation is not 1 modulo N")
            if lift != pow(half, -1, modulus):
                raise AssertionError("certificate lift is not the supplied actual lift")
            if pow(lift, 2, modulus) != math.prod(values) % modulus:
                raise AssertionError("certificate lift square failed")
            component_sets.append(set(values))
            component_lifts.append(lift)
        if len(components) == 1:
            z = component_lifts[0]
        elif len(components) == 2:
            common = math.prod(component_sets[0].intersection(component_sets[1]))
            z = component_lifts[0] * component_lifts[1] * pow(common, -1, modulus) % modulus
        else:
            raise AssertionError("registered section certificate has invalid support")
        w = pow(z, -1, modulus)
        minus = math.gcd(z - w, modulus)
        plus = math.gcd(z + w, modulus)
        passed = (
            z == int(certificate["z"])
            and w == int(certificate["w"])
            and z * w == int(certificate["exact_value"])
            and minus == int(certificate["gcd_minus"])
            and plus == int(certificate["gcd_plus"])
            and ((1 < minus < modulus) or (1 < plus < modulus))
        )
        return {"N_only": True, "passed": passed, "gcd_minus": minus, "gcd_plus": plus}
    if kind == "normalized_root":
        values = [int(value) for value in certificate["relation_values"]]
        if any(value % modulus != 1 for value in values):
            raise AssertionError("root certificate contains a nonrelation")
        product = math.prod(values)
        integer_root = math.isqrt(product)
        if integer_root * integer_root != product:
            raise AssertionError("root certificate product is not a square")
        root = integer_root % modulus
        minus = math.gcd(root - 1, modulus)
        plus = math.gcd(root + 1, modulus)
        passed = (
            root == int(certificate["integer_root_mod_N"])
            and minus == int(certificate["gcd_minus"])
            and plus == int(certificate["gcd_plus"])
            and root not in (1, modulus - 1)
            and ((1 < minus < modulus) or (1 < plus < modulus))
        )
        return {"N_only": True, "passed": passed, "gcd_minus": minus, "gcd_plus": plus}
    raise AssertionError("unknown certificate type")


def refinement_summary(old_blocks: list[int], new_blocks: list[int], core) -> dict[str, object]:
    old_set = set(old_blocks)
    new_set = set(new_blocks)
    preserved = len(old_set.intersection(new_set))
    if not new_blocks:
        return {
            "old_blocks": len(old_blocks),
            "new_blocks": 0,
            "preserved_old_blocks": 0,
            "strictly_split_old_blocks": 0,
            "changed_without_proper_overlap": len(old_blocks),
            "witnesses": [],
        }
    levels = core.product_tree(new_blocks)
    root = levels[-1][0]
    split_count = 0
    changed_without_proper = 0
    witnesses = []
    for old in old_blocks:
        if old in new_set:
            continue
        overlap = math.gcd(old, root)
        parts = []
        if overlap > 1:
            stack = [(len(levels) - 1, 0)]
            while stack:
                level, node = stack.pop()
                value = levels[level][node]
                common = math.gcd(old, value)
                if common == 1:
                    continue
                if level == 0:
                    parts.append(common)
                    continue
                left = 2 * node
                right = left + 1
                if right < len(levels[level - 1]):
                    stack.append((level - 1, right))
                stack.append((level - 1, left))
        proper = sorted({part for part in parts if 1 < part < old})
        if proper:
            split_count += 1
            if len(witnesses) < 8:
                witnesses.append({"old_block": old, "proper_parts": proper})
        else:
            changed_without_proper += 1
    return {
        "old_blocks": len(old_blocks),
        "new_blocks": len(new_blocks),
        "preserved_old_blocks": preserved,
        "strictly_split_old_blocks": split_count,
        "changed_without_proper_overlap": changed_without_proper,
        "witnesses": witnesses,
    }


def scan_level(
    modulus: int,
    level: int,
    records: list[dict[str, object]],
    exact_index: dict[int, int],
    old_context: dict[str, object],
    core,
) -> tuple[dict[str, object], dict[str, object]]:
    label = f"level_{level}"
    selected = old_context["selected"]
    basis_vectors = [old_context["vectors"][column] for column in selected]
    basis_lifts = [old_context["lifts"][column] for column in selected]
    inverse_blocks = [pow(block, -1, modulus) for block in old_context["blocks"]]
    rank = len(selected)
    attempted = rank + rank * (rank - 1) // 2
    candidate_digest = hashlib.sha256()
    screens = Counter()
    direct_hits = 0
    proper_divisors: set[int] = set()
    first_direct = None
    new_values = 0
    duplicates = 0
    duplicate_root_splits = 0
    first_duplicate_root = None

    def process(subset: tuple[int, ...], vector: frozenset[int], z: int) -> None:
        nonlocal direct_hits, first_direct, new_values, duplicates
        nonlocal duplicate_root_splits, first_duplicate_root
        w = pow(z, -1, modulus)
        minus = math.gcd(z - w, modulus)
        plus = math.gcd(z + w, modulus)
        for sign, divisor in (("minus", minus), ("plus", plus)):
            kind = "proper" if 1 < divisor < modulus else "unit" if divisor == 1 else "improper"
            screens[f"{sign}_{kind}"] += 1
            if kind == "proper":
                proper_divisors.add(divisor)
        proper = (1 < minus < modulus) or (1 < plus < modulus)
        if proper:
            direct_hits += 1
            if first_direct is None:
                first_direct = make_section_certificate(
                    modulus, records, old_context, label, subset, z, w, minus, plus
                )
        value = z * w
        payload = [len(subset), subset[0] + 1, (subset[1] + 1) if len(subset) == 2 else 0,
                   z, w, value, minus, plus]
        for item in payload:
            encoded = unsigned_bytes(item)
            candidate_digest.update(len(encoded).to_bytes(8, "big"))
            candidate_digest.update(encoded)
        origin = {
            "kind": "section_feedback",
            "level": level,
            "basis_subset": list(subset),
            "source_columns": [int(selected[index]) for index in subset],
        }
        created, duplicate_split = add_record(
            modulus, records, exact_index, value, 1, label, origin
        )
        if created:
            new_values += 1
        else:
            duplicates += 1
        if duplicate_split is not None:
            duplicate_root_splits += 1
            if first_duplicate_root is None:
                first_duplicate_root = duplicate_split | {"origin": origin}

    for index in range(rank):
        process((index,), basis_vectors[index], basis_lifts[index])
    for left in range(rank):
        for right in range(left + 1, rank):
            vector, z = star(
                basis_vectors[left], basis_lifts[left],
                basis_vectors[right], basis_lifts[right],
                inverse_blocks, modulus,
            )
            process((left, right), vector, z)

    if attempted != new_values + duplicates:
        raise AssertionError("candidate accounting changed")
    new_context = decode(modulus, records, core, f"N={modulus} {label} union")
    block_change = refinement_summary(
        old_context["blocks"], new_context["blocks"], core
    )
    root_certificate = make_root_certificate(
        modulus, records, new_context, f"{label}_union"
    )
    replays = []
    for certificate in (first_direct, root_certificate):
        if certificate is not None:
            replay = replay_n_only_certificate(modulus, certificate)
            if not replay["passed"]:
                raise AssertionError("N-only positive replay failed")
            replays.append({"certificate_type": certificate["type"], "replay": replay})
    result = {
        "level": level,
        "frozen_basis_rank": rank,
        "attempted_nonempty_support_at_most_two": attempted,
        "strict_new_exact_values": new_values,
        "duplicate_exact_values": duplicates,
        "duplicate_root_split_count": duplicate_root_splits,
        "first_duplicate_root_split": first_duplicate_root,
        "direct_screen_counts": dict(screens),
        "proper_direct_candidate_count": direct_hits,
        "proper_divisors": sorted(proper_divisors),
        "first_direct_certificate": first_direct,
        "union_decoder": new_context["summary"],
        "first_root_certificate": root_certificate,
        "factor_free_block_change": block_change,
        "candidate_sha256": candidate_digest.hexdigest(),
        "N_only_positive_replays": replays,
    }
    return result, new_context


def analyze_public(modulus: int, core) -> dict[str, object]:
    started = time.monotonic()
    n = modulus.bit_length()
    records: list[dict[str, object]] = []
    exact_index: dict[int, int] = {}
    screens = Counter()
    proper_divisors: set[int] = set()
    first_base_direct = None
    duplicate_root_splits = []
    for c in range(2, n + 2):
        divisor = math.gcd(c, modulus)
        if divisor != 1:
            raise AssertionError("registered corpus has a nonunit base seed")
        w = pow(c, -1, modulus)
        minus = math.gcd(c - w, modulus)
        plus = math.gcd(c + w, modulus)
        for sign, value in (("minus", minus), ("plus", plus)):
            kind = "proper" if 1 < value < modulus else "unit" if value == 1 else "improper"
            screens[f"{sign}_{kind}"] += 1
            if kind == "proper":
                proper_divisors.add(value)
        if first_base_direct is None and ((1 < minus < modulus) or (1 < plus < modulus)):
            first_base_direct = {
                "type": "base_seed_direct",
                "layer": "base",
                "c": c,
                "w": w,
                "exact_value": c * w,
                "gcd_minus": minus,
                "gcd_plus": plus,
            }
        created, duplicate_split = add_record(
            modulus,
            records,
            exact_index,
            c * w,
            1,
            "base",
            {"kind": "base_seed", "c": c, "w": w},
        )
        if not created and duplicate_split is not None:
            duplicate_root_splits.append(duplicate_split)

    base_context = decode(modulus, records, core, f"N={modulus} base")
    base_root = make_root_certificate(modulus, records, base_context, "base")
    base_replays = []
    for certificate in (first_base_direct, base_root):
        if certificate is not None:
            replay = replay_n_only_certificate(modulus, certificate)
            if not replay["passed"]:
                raise AssertionError("base N-only positive replay failed")
            base_replays.append({"certificate_type": certificate["type"], "replay": replay})
    base = {
        "n": n,
        "attempted_unit_seeds": n,
        "distinct_exact_values": len(records),
        "duplicate_exact_values": n - len(records),
        "duplicate_root_split_count": len(duplicate_root_splits),
        "direct_screen_counts": dict(screens),
        "proper_divisors": sorted(proper_divisors),
        "first_direct_certificate": first_base_direct,
        "decoder": base_context["summary"],
        "first_root_certificate": base_root,
        "N_only_positive_replays": base_replays,
    }

    level_results = []
    context = base_context
    for level in range(1, RECURSIVE_LEVELS + 1):
        result, context = scan_level(
            modulus, level, records, exact_index, context, core
        )
        level_results.append(result)

    base_positive = bool(base["proper_divisors"]) or bool(base["decoder"]["normalized_root_image_nonzero"])
    level_one_positive = (
        level_results[0]["proper_direct_candidate_count"] > 0
        or level_results[0]["union_decoder"]["normalized_root_image_nonzero"]
        or level_results[0]["duplicate_root_split_count"] > 0
    )
    level_two_positive = (
        level_results[1]["proper_direct_candidate_count"] > 0
        or level_results[1]["union_decoder"]["normalized_root_image_nonzero"]
        or level_results[1]["duplicate_root_split_count"] > 0
    )
    all_proper = set(base["proper_divisors"])
    for result in level_results:
        all_proper.update(result["proper_divisors"])
        root = result["first_root_certificate"]
        if root is not None:
            for key in ("gcd_minus", "gcd_plus"):
                value = int(root[key])
                if 1 < value < modulus:
                    all_proper.add(value)
    if base_root is not None:
        for key in ("gcd_minus", "gcd_plus"):
            value = int(base_root[key])
            if 1 < value < modulus:
                all_proper.add(value)
    output = {
        "N": modulus,
        "public_input_keys": ["N"],
        "base": base,
        "levels": level_results,
        "base_null": not base_positive,
        "level_one_null_given_base_null": (not level_one_positive) if not base_positive else None,
        "level_two_positive_after_earlier_nulls": (
            (not base_positive) and (not level_one_positive) and level_two_positive
        ),
        "all_public_proper_divisors": sorted(all_proper),
        "final_distinct_exact_values": len(records),
        "elapsed_seconds": time.monotonic() - started,
    }
    del context, base_context, records
    gc.collect()
    return output


def factor_assisted_classification(
    public_result: dict[str, object], p: int, q: int
) -> dict[str, object]:
    divisors = [int(value) for value in public_result["all_public_proper_divisors"]]
    if any(value not in (p, q) for value in divisors):
        raise AssertionError("a public proper divisor is not a disclosed prime factor")
    return {
        "role": "post-hoc classification only",
        "p": p,
        "q": q,
        "N_matches": p * q == int(public_result["N"]),
        "public_proper_divisors_match_disclosed_factors": True,
        "observed_factor_labels": ["p" if value == p else "q" for value in divisors],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    started = time.monotonic()
    directory = Path(__file__).resolve().parent
    root = directory.parents[1]
    registration = json.loads((directory / "REGISTRATION.json").read_text())
    if registration["status"] != "FROZEN_BEFORE_AUTHORITATIVE_RUN":
        raise AssertionError("registration status changed")
    if registration["parameters"] != {
        "corpus_size": CORPUS_SIZE,
        "prime_low_inclusive": PRIME_LOW,
        "prime_high_inclusive": PRIME_HIGH,
        "recursive_levels": RECURSIVE_LEVELS,
        "support_cap": SUPPORT_CAP,
        "base_seed_rule": "all units 2<=c<=n+1",
    }:
        raise AssertionError("registered parameters changed")
    core, upstream = load_pinned_core(root, registration)
    corpus = construct_corpus()
    corpus_hash = hash_integer_sequence(value for pair in corpus for value in pair)
    if registration["corpus_sha256"] is not None and corpus_hash != registration["corpus_sha256"]:
        raise AssertionError("deterministic corpus hash changed")

    results = []
    first_level_two_only = None
    for index, (p, q) in enumerate(corpus):
        modulus = p * q
        print(
            f"F165 instance {index + 1}/{len(corpus)}: N={modulus}", flush=True
        )
        public = analyze_public(modulus, core)
        private = factor_assisted_classification(public, p, q)
        entry = {
            "corpus_index": index,
            "public": public,
            "factor_assisted_classification": private,
        }
        results.append(entry)
        if first_level_two_only is None and public["level_two_positive_after_earlier_nulls"]:
            level_two = public["levels"][1]
            certificate = level_two["first_direct_certificate"] or level_two["first_root_certificate"]
            first_level_two_only = {
                "corpus_index": index,
                "N": modulus,
                "public_certificate": certificate,
                "N_only_replays": level_two["N_only_positive_replays"],
            }
        write_json(
            arguments.output,
            {
                "status": "RUNNING",
                "experiment_id": EXPERIMENT_ID,
                "upstream_pins": upstream,
                "corpus_sha256": corpus_hash,
                "completed_instances": len(results),
                "instances": results,
                "first_level_two_only": first_level_two_only,
                "elapsed_seconds": time.monotonic() - started,
            },
        )

    counts = Counter()
    for entry in results:
        public = entry["public"]
        counts["base_null"] += int(public["base_null"])
        counts["level_one_null_after_base_null"] += int(
            public["level_one_null_given_base_null"] is True
        )
        counts["level_two_only_positive"] += int(
            public["level_two_positive_after_earlier_nulls"]
        )
        counts["level_one_direct_positive"] += int(
            public["levels"][0]["proper_direct_candidate_count"] > 0
        )
        counts["level_two_direct_positive"] += int(
            public["levels"][1]["proper_direct_candidate_count"] > 0
        )
        counts["level_one_root_positive"] += int(
            public["levels"][0]["union_decoder"]["normalized_root_image_nonzero"]
        )
        counts["level_two_root_positive"] += int(
            public["levels"][1]["union_decoder"]["normalized_root_image_nonzero"]
        )
        counts["level_one_strict_new_value"] += int(
            public["levels"][0]["strict_new_exact_values"] > 0
        )
        counts["level_two_strict_new_value"] += int(
            public["levels"][1]["strict_new_exact_values"] > 0
        )
        counts["level_one_strict_block_refinement"] += int(
            public["levels"][0]["factor_free_block_change"]["strictly_split_old_blocks"] > 0
        )
        counts["level_two_strict_block_refinement"] += int(
            public["levels"][1]["factor_free_block_change"]["strictly_split_old_blocks"] > 0
        )
    output = {
        "status": "PASS",
        "experiment_id": EXPERIMENT_ID,
        "claim_scope": "fixed 64-instance finite capability classification only",
        "parameters": registration["parameters"],
        "upstream_pins": upstream,
        "corpus_sha256": corpus_hash,
        "corpus_pairs": [[p, q] for p, q in corpus],
        "summary_instance_counts": dict(counts),
        "first_level_two_only": first_level_two_only,
        "instances": results,
        "public_evidence_boundary": {
            "analysis_function_receives_only_N": True,
            "candidate_source_uses_no_disclosed_factor": True,
            "factor_free_parity_decoder": True,
            "every_reported_positive_certificate_has_N_only_replay": True,
            "disclosed_factors_used_only_for_post_hoc_classification": True,
        },
        "limitations": [
            "finite corpus only",
            "no success density",
            "no minimal-depth claim",
            "no all-input source theorem",
            "no asymptotic factoring conclusion",
        ],
        "elapsed_seconds": time.monotonic() - started,
    }
    write_json(arguments.output, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
