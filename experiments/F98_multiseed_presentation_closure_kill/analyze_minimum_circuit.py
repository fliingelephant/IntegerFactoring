#!/usr/bin/env python3
"""Diagnose support at most three and one larger F98 circuit, factor-free."""

from __future__ import annotations

import bisect
import json
import math
from pathlib import Path

from public_factorization_free_replay import (
    gcd_free_basis,
    parity_coprime_basis,
    relation_columns,
)


MODULUS = 202537109
GENERAL_FACTOR_RELATION_COUNT = 5616
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "SMALL_SUPPORT_OUTPUT.json"


def root_test(indices: tuple[int, ...], records: list[dict[str, object]]) -> dict[str, object]:
    product = 1
    for index in indices:
        product *= int(records[index]["P"])
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError("A parity-zero circuit was not an exact square.")
    minus = math.gcd(root - 1, MODULUS)
    plus = math.gcd(root + 1, MODULUS)
    return {
        "indices_zero_based": list(indices),
        "indices_one_based": [index + 1 for index in indices],
        "relation_products": [int(records[index]["P"]) for index in indices],
        "provenances": [records[index]["provenance"] for index in indices],
        "root": root,
        "root_mod_N": root % MODULUS,
        "gcd_root_minus_one_N": minus,
        "gcd_root_plus_one_N": plus,
        "useful": 1 < minus < MODULUS or 1 < plus < MODULUS,
        "duplicate_relation_values": len({int(records[index]["P"]) for index in indices}) < len(indices),
    }


def main() -> int:
    n = MODULUS.bit_length()
    bound = n * n
    records: list[dict[str, object]] = []
    endpoint_values: list[int] = []
    seen: set[int] = set()

    def retain(c: int, provenance: dict[str, object]) -> None:
        if c in seen:
            return
        seen.add(c)
        w = pow(c, -1, MODULUS)
        records.append(
            {
                "c": c,
                "w": w,
                "P": c * w,
                "provenance": provenance,
            }
        )
        endpoint_values.extend((c, w))

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})
    initial_basis, _ = gcd_free_basis(endpoint_values)
    initial_columns = relation_columns(initial_basis, len(records))
    active = []
    for relation_index, column in enumerate(initial_columns):
        if not any(exponent & 1 for exponent in column.values()):
            continue
        support = sorted(initial_basis[index][0] for index in column)
        pair = (support[0], 1) if len(support) == 1 else tuple(support[:2])
        active.append((relation_index, pair))
        if len(active) == n:
            break

    for relation_index, (u, v) in active:
        for exponent in range(bound + 1):
            candidates = (
                ("u_power_times_v", pow(u, exponent, MODULUS) * v % MODULUS),
                ("u_times_v_power", u * pow(v, exponent, MODULUS) % MODULUS),
            )
            for orientation, c in candidates:
                retain(
                    c,
                    {
                        "kind": "feedback_trajectory",
                        "round": 1,
                        "active_relation_index_zero_based": relation_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                if len(records) >= GENERAL_FACTOR_RELATION_COUNT:
                    break
            if len(records) >= GENERAL_FACTOR_RELATION_COUNT:
                break
        if len(records) >= GENERAL_FACTOR_RELATION_COUNT:
            break
    if len(records) != GENERAL_FACTOR_RELATION_COUNT:
        raise AssertionError("The declared relation prefix was not reproduced.")

    initial_entries = []
    for index, record in enumerate(records):
        mask = 1 << index
        initial_entries.append((int(record["c"]), mask))
        initial_entries.append((int(record["w"]), mask))
    parity_blocks, refinements, gcd_tests = parity_coprime_basis(initial_entries)
    row_masks = [
        mask
        for value, mask in parity_blocks
        if math.isqrt(value) ** 2 != value
    ]
    parities = [0] * len(records)
    for row_index, mask in enumerate(row_masks):
        remaining = mask
        while remaining:
            low = remaining & -remaining
            column = low.bit_length() - 1
            parities[column] ^= 1 << row_index
            remaining ^= low

    support_one = []
    for index, parity in enumerate(parities):
        if parity == 0:
            support_one.append(root_test((index,), records))

    parity_classes: dict[int, list[int]] = {}
    for index, parity in enumerate(parities):
        parity_classes.setdefault(parity, []).append(index)
    support_two = []
    first_useful_two = None
    for indices in parity_classes.values():
        if len(indices) < 2:
            continue
        for position, left in enumerate(indices):
            for right in indices[position + 1 :]:
                result = root_test((left, right), records)
                support_two.append(result)
                if result["useful"] and (
                    first_useful_two is None
                    or result["indices_zero_based"][-1]
                    < first_useful_two["indices_zero_based"][-1]
                ):
                    first_useful_two = result
    if any(not result["duplicate_relation_values"] for result in support_two):
        raise AssertionError("A support-two class pair had distinct relation values.")
    if any(result["useful"] for result in support_two):
        raise AssertionError("A useful support-two circuit invalidates triple compression.")

    first_useful_three = None
    triple_matches = 0
    for left in range(len(records)):
        for middle in range(left + 1, len(records)):
            target = parities[left] ^ parities[middle]
            candidates = parity_classes.get(target)
            if not candidates:
                continue
            position = bisect.bisect_right(candidates, middle)
            for right in candidates[position:]:
                triple_matches += 1
                result = root_test((left, middle, right), records)
                if result["useful"] and (
                    first_useful_three is None
                    or result["indices_zero_based"][-1]
                    < first_useful_three["indices_zero_based"][-1]
                ):
                    first_useful_three = result
                break

    pivots: dict[int, tuple[int, int]] = {}
    first_general = None
    for index, parity in enumerate(parities):
        reduced = parity
        combination = 1 << index
        while reduced:
            pivot = reduced.bit_length() - 1
            old = pivots.get(pivot)
            if old is None:
                pivots[pivot] = (reduced, combination)
                break
            reduced ^= old[0]
            combination ^= old[1]
        else:
            indices = tuple(
                relation_index
                for relation_index in range(index + 1)
                if (combination >> relation_index) & 1
            )
            result = root_test(indices, records)
            if result["useful"]:
                first_general = {
                    "relation_index_zero_based": index,
                    "dependency_size": len(indices),
                    "witness": result,
                }
                break
    if first_general is None or first_general["relation_index_zero_based"] != 5615:
        raise AssertionError("The prior Gaussian factor prefix did not reproduce.")
    raw_indices = first_general["witness"]["indices_zero_based"]
    indices_by_value: dict[int, list[int]] = {}
    for index in raw_indices:
        indices_by_value.setdefault(int(records[index]["P"]), []).append(index)
    reduced_indices = tuple(
        indices[-1]
        for _, indices in sorted(indices_by_value.items())
        if len(indices) & 1
    )
    reduced_result = root_test(reduced_indices, records)
    if not reduced_result["useful"]:
        raise AssertionError("Duplicate-value cancellation lost the useful root.")
    first_general["raw_support"] = len(raw_indices)
    first_general["distinct_relation_values_in_raw_support"] = len(indices_by_value)
    first_general["reduced_distinct_value_support"] = len(reduced_indices)
    first_general["even_duplicate_occurrences_removed"] = len(raw_indices) - len(
        reduced_indices
    )
    first_general["reduced_witness"] = reduced_result

    output = {
        "experiment": "F98_multiseed_presentation_closure_kill",
        "role": "factorization-free small-support diagnosis and one larger circuit",
        "input": {
            "N": MODULUS,
            "n": n,
            "B": bound,
            "input_policy": "diagnostic receives only N and a pinned public prefix length",
            "forbidden_operations_used": [],
        },
        "target_free_prefix": {
            "relation_count": len(records),
            "active_pairs": [list(pair) for _, pair in active],
            "factor_free_nonsquare_rows": len(row_masks),
            "factor_free_gcd_refinements": refinements,
            "factor_free_gcd_pair_tests": gcd_tests,
        },
        "support_one": {
            "matches": len(support_one),
            "useful": sum(result["useful"] for result in support_one),
            "first": support_one[0] if support_one else None,
        },
        "support_two": {
            "matches": len(support_two),
            "useful": sum(result["useful"] for result in support_two),
            "duplicate_value_matches": sum(
                result["duplicate_relation_values"] for result in support_two
            ),
            "first_useful": first_useful_two,
        },
        "support_three": {
            "matches_with_first_right_per_pair": triple_matches,
            "first_useful": first_useful_three,
            "first_right_test_is_complete": True,
            "sufficiency_reason": (
                "Every support-two parity-class pair in this prefix has an "
                "identical relation value, so its connecting root is P congruent "
                "to +1 modulo N. Replacing one right endpoint by another in the "
                "same class therefore preserves the triple root residue."
            ),
        },
        "first_general_dependency_factor": first_general,
        "scope": (
            "The null covers supports one, two, and three in this pinned prefix. "
            "The 166-column Gaussian witness is not claimed minimal above support three."
        ),
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"support_one_useful={output['support_one']['useful']}")
    print(f"support_two_useful={output['support_two']['useful']}")
    print(f"support_three_first_useful={first_useful_three is not None}")
    print(f"general_dependency_size={first_general['dependency_size']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
