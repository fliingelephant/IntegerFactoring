#!/usr/bin/env python3
"""Exact bounded analysis of the F95 square-class collision at N=2773."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from collections import deque
from pathlib import Path


def is_square(value: int) -> tuple[bool, int]:
    root = math.isqrt(value)
    return root * root == value, root


def multiplicative_order(value: int, modulus: int) -> int:
    if math.gcd(value, modulus) != 1:
        raise ValueError("The order is defined here only for a unit.")
    residue = 1
    for order in range(1, modulus + 1):
        residue = residue * value % modulus
        if residue == 1:
            return order
    raise AssertionError("A unit order did not close within N steps.")


def generated_subgroup(
    generators: tuple[int, ...], modulus: int
) -> tuple[dict[int, tuple[int, ...]], list[int]]:
    """Return shortest positive-generator words and deterministic BFS order."""
    identity_word = (0,) * len(generators)
    words = {1: identity_word}
    order = [1]
    queue = deque([1])
    while queue:
        residue = queue.popleft()
        word = words[residue]
        for index, generator in enumerate(generators):
            child = residue * generator % modulus
            if child in words:
                continue
            child_word = list(word)
            child_word[index] += 1
            words[child] = tuple(child_word)
            order.append(child)
            queue.append(child)
    return words, order


def generated_subgroup_signed(
    generators: tuple[int, ...], modulus: int
) -> dict[int, tuple[int, ...]]:
    """Return shortest signed-generator words under a fixed step order."""
    identity_word = (0,) * len(generators)
    words = {1: identity_word}
    queue = deque([1])
    steps: list[tuple[int, tuple[int, ...]]] = []
    for index, generator in enumerate(generators):
        positive = [0] * len(generators)
        positive[index] = 1
        negative = [0] * len(generators)
        negative[index] = -1
        steps.append((generator, tuple(positive)))
        steps.append((pow(generator, -1, modulus), tuple(negative)))
    while queue:
        residue = queue.popleft()
        word = words[residue]
        for step, delta in steps:
            child = residue * step % modulus
            if child in words:
                continue
            words[child] = tuple(
                word[index] + delta[index] for index in range(len(generators))
            )
            queue.append(child)
    return words


def relation_for_residue(residue: int, modulus: int) -> dict[str, int]:
    inverse = pow(residue, -1, modulus)
    product = residue * inverse
    if product % modulus != 1:
        raise AssertionError("Canonical inverse relation failed.")
    return {
        "c": residue,
        "w": inverse,
        "P": product,
        "k": (product - 1) // modulus,
    }


def collision_with_first(
    first_product: int, candidate: dict[str, int], modulus: int
) -> dict[str, object] | None:
    if candidate["P"] == first_product:
        return None
    square, induced_root = is_square(first_product * candidate["P"])
    if not square:
        return None
    divisor = math.gcd(induced_root - 1, modulus)
    return {
        **candidate,
        "induced_root": induced_root,
        "root_mod_n": induced_root % modulus,
        "gcd_root_minus_one_n": divisor,
        "gcd_root_plus_one_n": math.gcd(induced_root + 1, modulus),
        "useful": 1 < divisor < modulus,
    }


def exponent_pairs(bound_a: int, bound_b: int):
    for total in range(bound_a + bound_b + 1):
        for exponent_a in range(bound_a + 1):
            exponent_b = total - exponent_a
            if 0 <= exponent_b <= bound_b:
                yield exponent_a, exponent_b


def direct_integer_products(
    generators: tuple[int, int], modulus: int
) -> list[tuple[int, int, int]]:
    values: list[tuple[int, int, int]] = []
    power_a = 1
    exponent_a = 0
    while power_a < modulus:
        power_b = 1
        exponent_b = 0
        while power_a * power_b < modulus:
            if exponent_a or exponent_b:
                values.append((exponent_a, exponent_b, power_a * power_b))
            exponent_b += 1
            power_b *= generators[1]
        exponent_a += 1
        power_a *= generators[0]
    return sorted(values, key=lambda item: (item[2], item[0], item[1]))


def canonical_relation_census(modulus: int) -> list[dict[str, int | bool]]:
    relation_by_product: dict[int, dict[str, int | bool]] = {}
    for raw_g in range(2, modulus):
        if math.gcd(raw_g, modulus) != 1:
            continue
        raw_w = pow(raw_g, -1, modulus)
        if raw_w <= 1:
            continue
        g = min(raw_g, raw_w)
        w = max(raw_g, raw_w)
        product = g * w
        square, _ = is_square(product)
        candidate: dict[str, int | bool] = {
            "g": g,
            "w": w,
            "P": product,
            "k": (product - 1) // modulus,
            "square": square,
        }
        previous = relation_by_product.get(product)
        if previous is None or (g, w) < (int(previous["g"]), int(previous["w"])):
            relation_by_product[product] = candidate
    relations = sorted(
        relation_by_product.values(),
        key=lambda item: (int(item["P"]), int(item["g"]), int(item["w"])),
    )
    for index, relation in enumerate(relations):
        relation["index"] = index
    return relations


def is_prime_small(value: int) -> bool:
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


def distinct_odd_semiprime_factors(value: int) -> tuple[int, int] | None:
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor != 0:
            continue
        cofactor = value // divisor
        if divisor != cofactor and is_prime_small(divisor) and is_prime_small(cofactor):
            return divisor, cofactor
    return None


def normalize_pair(
    first: dict[str, int | bool],
    second: dict[str, int | bool],
    modulus: int,
) -> dict[str, object]:
    first_product = int(first["P"])
    second_product = int(second["P"])
    common = math.gcd(first_product, second_product)
    first_square, first_root = is_square(first_product // common)
    second_square, second_root = is_square(second_product // common)
    combined_square, induced_root = is_square(first_product * second_product)
    if not (first_square and second_square and combined_square):
        raise AssertionError("A same-square-class pair did not normalize exactly.")
    if induced_root != common * first_root * second_root:
        raise AssertionError("The normalized induced root is inconsistent.")
    root_minus = math.gcd(induced_root - 1, modulus)
    root_plus = math.gcd(induced_root + 1, modulus)
    normalized_minus = math.gcd(first_root - second_root, modulus)
    normalized_plus = math.gcd(first_root + second_root, modulus)
    if (root_minus, root_plus) != (normalized_minus, normalized_plus):
        raise AssertionError("The exact gcd identities failed.")
    return {
        "relation_1": first,
        "relation_2": second,
        "D": common,
        "A": first_root,
        "B": second_root,
        "gcd_A_B": math.gcd(first_root, second_root),
        "induced_root": induced_root,
        "root_mod_n": induced_root % modulus,
        "gcd_root_minus_one_n": root_minus,
        "gcd_root_plus_one_n": root_plus,
        "gcd_A_minus_B_n": normalized_minus,
        "gcd_A_plus_B_n": normalized_plus,
        "global_sign": (
            "+1" if induced_root % modulus == 1
            else "-1" if induced_root % modulus == modulus - 1
            else "non_global"
        ),
        "useful": 1 < root_minus < modulus,
    }


def first_global_semiprime_counterexample(maximum: int) -> dict[str, object] | None:
    """Find a bounded distinct-semiprime pair showing that class equality is insufficient."""
    for modulus in range(15, maximum + 1, 2):
        factors = distinct_odd_semiprime_factors(modulus)
        if factors is None:
            continue
        relations = canonical_relation_census(modulus)
        nonsquare = [relation for relation in relations if not relation["square"]]
        for first_index, first in enumerate(nonsquare):
            for second in nonsquare[first_index + 1 :]:
                square, _ = is_square(int(first["P"]) * int(second["P"]))
                if not square:
                    continue
                normalized = normalize_pair(first, second, modulus)
                if normalized["global_sign"] in {"+1", "-1"}:
                    return {
                        "N": modulus,
                        "factorization_certificate": list(factors),
                        **normalized,
                    }
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--block-a", type=int, required=True)
    parser.add_argument("--block-b", type=int, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    modulus = args.n
    generators = (args.block_a, args.block_b)
    target = args.target
    bit_length = modulus.bit_length()

    first_relation = relation_for_residue(generators[0], modulus)
    expected_first_product = generators[0] * generators[1] ** 2
    if first_relation["P"] != expected_first_product:
        raise AssertionError("The declared first square normalization is inconsistent.")
    target_relation = relation_for_residue(target, modulus)

    orders = [multiplicative_order(generator, modulus) for generator in generators]
    words, subgroup_order = generated_subgroup(generators, modulus)
    signed_words = generated_subgroup_signed(generators, modulus)
    target_word = words.get(target)
    target_inverse_word = words.get(target_relation["w"])
    target_root_ratio = target * pow(generators[1], -1, modulus) % modulus
    subgroup_involution = pow(generators[1], orders[1] // 2, modulus)
    if target_root_ratio * target_root_ratio % modulus != 1:
        raise AssertionError("The target-to-first-root ratio is not an involution.")

    direct_records: list[dict[str, object]] = []
    direct_collisions: list[dict[str, object]] = []
    target_endpoint_hits: list[dict[str, object]] = []
    target_relation_hits: list[dict[str, object]] = []
    for exponent_a, exponent_b, product in direct_integer_products(generators, modulus):
        relation = relation_for_residue(product, modulus)
        record: dict[str, object] = {
            "exponents": [exponent_a, exponent_b],
            "raw_product": product,
            **relation,
        }
        direct_records.append(record)
        if target in (relation["c"], relation["w"]):
            target_endpoint_hits.append(record)
        if relation["P"] == target_relation["P"]:
            target_relation_hits.append(record)
        collision = collision_with_first(first_relation["P"], relation, modulus)
        if collision is not None:
            direct_collisions.append({"exponents": [exponent_a, exponent_b], **collision})

    capacity_records = [
        record
        for record in direct_records
        if int(record["exponents"][0]) <= 1 and int(record["exponents"][1]) <= 2
    ]
    capacity_collisions = [
        record
        for record in direct_collisions
        if int(record["exponents"][0]) <= 1 and int(record["exponents"][1]) <= 2
    ]

    menu_results: dict[str, object] = {}
    for label, bound in (("n", bit_length), ("n_squared", bit_length * bit_length)):
        menu_records: list[dict[str, object]] = []
        menu_target_hits: list[dict[str, object]] = []
        menu_collisions: list[dict[str, object]] = []
        seen_residues: set[int] = set()
        for pair_ordinal, (exponent_a, exponent_b) in enumerate(
            exponent_pairs(bound, bound), start=1
        ):
            residue = (
                pow(generators[0], exponent_a, modulus)
                * pow(generators[1], exponent_b, modulus)
                % modulus
            )
            if residue in seen_residues:
                continue
            seen_residues.add(residue)
            relation = relation_for_residue(residue, modulus)
            record = {
                "exponents": [exponent_a, exponent_b],
                "residue": residue,
                "raw_product_below_n": (
                    generators[0] ** exponent_a * generators[1] ** exponent_b < modulus
                ),
                **relation,
            }
            menu_records.append(record)
            if residue == target or relation["w"] == target:
                menu_target_hits.append(record)
            collision = collision_with_first(first_relation["P"], relation, modulus)
            if collision is not None:
                menu_collisions.append(
                    {
                        "exponents": [exponent_a, exponent_b],
                        "residue": residue,
                        "exponent_pair_ordinal_1_based": pair_ordinal,
                        "unique_residue_ordinal_1_based": len(menu_records),
                        **collision,
                    }
                )
        menu_results[label] = {
            "exponent_bound_each": bound,
            "ordering": "increasing a+b, then increasing a; duplicate residues skipped",
            "exponent_pairs_considered": (bound + 1) * (bound + 1),
            "unique_residues_tested": len(menu_records),
            "target_hits": menu_target_hits,
            "same_square_class_collision_count": len(menu_collisions),
            "useful_same_square_class_collision_count": sum(
                bool(record["useful"]) for record in menu_collisions
            ),
            "first_same_square_class_collision": (
                menu_collisions[0] if menu_collisions else None
            ),
        }

    subgroup_collisions: list[dict[str, object]] = []
    for residue in subgroup_order:
        relation = relation_for_residue(residue, modulus)
        collision = collision_with_first(first_relation["P"], relation, modulus)
        if collision is not None:
            subgroup_collisions.append(
                {
                    "residue": residue,
                    "shortest_positive_word": list(words[residue]),
                    "shortest_signed_word": list(signed_words[residue]),
                    **collision,
                }
            )

    relations = canonical_relation_census(modulus)
    nonsquare_relations = [relation for relation in relations if not relation["square"]]
    collision_count = 0
    useful_count = 0
    global_plus_count = 0
    global_minus_count = 0
    first_useful: dict[str, object] | None = None
    first_global_plus: dict[str, object] | None = None
    first_global_minus: dict[str, object] | None = None
    f95_pair: dict[str, object] | None = None
    for first_index, first in enumerate(nonsquare_relations):
        for second in nonsquare_relations[first_index + 1 :]:
            square, _ = is_square(int(first["P"]) * int(second["P"]))
            if not square:
                continue
            collision_count += 1
            normalized = normalize_pair(first, second, modulus)
            if normalized["useful"]:
                useful_count += 1
                if first_useful is None:
                    first_useful = normalized
            elif normalized["global_sign"] == "+1":
                global_plus_count += 1
                if first_global_plus is None:
                    first_global_plus = normalized
            elif normalized["global_sign"] == "-1":
                global_minus_count += 1
                if first_global_minus is None:
                    first_global_minus = normalized
            else:
                raise AssertionError("An odd-modulus root was neither useful nor global.")
            products = {int(first["P"]), int(second["P"])}
            if products == {first_relation["P"], target_relation["P"]}:
                f95_pair = normalized

    global_counterexample = first_global_semiprime_counterexample(199)
    if global_counterexample is None:
        raise AssertionError("The bounded global-sign counterexample search was null.")

    output = {
        "experiment_id": "F96_squareclass_collision_boundary",
        "status": "exact_bounded_result",
        "data_policy": {
            "n2773_selector_uses_factors": False,
            "bounded_counterexample_scan": (
                "public trial factorization classifies distinct odd semiprime inputs"
            ),
            "public_inputs": ["N", "first normalized blocks", "F95 target for membership query"],
            "certificate_only_steps": [
                "complete BFS over the generated subgroup",
                "complete canonical-relation pair census",
            ],
            "polynomial_in_log_n_public_steps": [
                "verification of a supplied word",
                "fixed two-block exponent menus with bounds polynomial in bit_length(N)",
                "gcd square normalization and induced-root gcd tests",
            ],
        },
        "inputs": {
            "N": modulus,
            "bit_length": bit_length,
            "blocks": list(generators),
            "target": target,
            "first_relation": first_relation,
            "target_relation": target_relation,
        },
        "subgroup": {
            "generator_orders": orders,
            "size": len(words),
            "collapse_certificate": {
                "three_times_43_squared_mod_n": (
                    generators[0] * generators[1] * generators[1] % modulus
                ),
                "meaning": "3 is 43^(-2), so <3,43> equals <43>",
            },
            "target_nonmembership_certificate": {
                "target_times_43_inverse_mod_n": target_root_ratio,
                "ratio_squared_mod_n": target_root_ratio * target_root_ratio % modulus,
                "ratio_is_global_sign": target_root_ratio in {1, modulus - 1},
                "43_half_order_power_mod_n": subgroup_involution,
                "cyclic_subgroup_unique_involution": True,
            },
            "target_is_member": target_word is not None,
            "target_shortest_positive_word": list(target_word) if target_word is not None else None,
            "target_inverse_is_member": target_inverse_word is not None,
            "target_inverse_shortest_positive_word": (
                list(target_inverse_word) if target_inverse_word is not None else None
            ),
            "complete_residue_scan_collision_count": len(subgroup_collisions),
            "complete_residue_scan_collision_fraction": (
                f"{len(subgroup_collisions)}/{len(words)}"
            ),
            "distinct_collision_relation_values": len(
                {int(record["P"]) for record in subgroup_collisions}
            ),
            "complete_residue_scan_useful_collision_count": sum(
                bool(record["useful"]) for record in subgroup_collisions
            ),
            "first_complete_residue_scan_collision": (
                subgroup_collisions[0] if subgroup_collisions else None
            ),
            "complete_residue_scan_collisions": subgroup_collisions,
        },
        "direct_integer_feedback": {
            "all_nonnegative_monomials_below_n_count": len(direct_records),
            "target_endpoint_hits": target_endpoint_hits,
            "target_relation_hits": target_relation_hits,
            "same_square_class_collision_count": len(direct_collisions),
            "useful_same_square_class_collision_count": sum(
                bool(record["useful"]) for record in direct_collisions
            ),
            "first_same_square_class_collision": direct_collisions[0] if direct_collisions else None,
            "single_relation_capacity_candidates": capacity_records,
            "single_relation_capacity_collision_count": len(capacity_collisions),
        },
        "canonical_residue_menus": menu_results,
        "full_relation_census": {
            "unique_relation_values": len(relations),
            "nonsquare_relation_values": len(nonsquare_relations),
            "same_nonzero_square_class_pairs": collision_count,
            "useful_pairs": useful_count,
            "global_plus_pairs": global_plus_count,
            "global_minus_pairs": global_minus_count,
            "first_useful_pair": first_useful,
            "first_global_plus_pair": first_global_plus,
            "first_global_minus_pair": first_global_minus,
            "f95_pair": f95_pair,
        },
        "bounded_global_sign_counterexample": {
            "search_range": "distinct odd semiprimes N <= 199",
            "first_under_increasing_N_then_relation_order": global_counterexample,
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(f"status={output['status']}")
    print(
        f"subgroup_size={len(words)} orders={orders} "
        f"target_is_member={target_word is not None}"
    )
    print(
        f"direct_products={len(direct_records)} direct_collisions={len(direct_collisions)} "
        f"subgroup_collisions={len(subgroup_collisions)}"
    )
    print(
        f"relation_collisions={collision_count} useful={useful_count} "
        f"global_plus={global_plus_count} global_minus={global_minus_count}"
    )
    print(f"output_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
