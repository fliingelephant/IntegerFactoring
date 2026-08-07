#!/usr/bin/env python3
"""Bounded target-free kill test for the F96 n-squared residue menu."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


def factor_small(value: int) -> dict[int, int]:
    """Trial-factor a bounded public integer for input selection only."""
    factors: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def stable_semiprime_certificate(modulus: int) -> dict[str, object] | None:
    factors = factor_small(modulus)
    if len(factors) != 2 or any(exponent != 1 for exponent in factors.values()):
        return None
    p, q = sorted(factors)
    if p == 2 or p == q:
        return None
    common_order = math.gcd(p - 1, q - 1)
    local_a = (p - 1) // common_order
    local_b = (q - 1) // common_order
    stability_gcd = math.gcd(local_a * local_b, modulus - 1)
    if stability_gcd != 1:
        return None
    return {
        "p": p,
        "q": q,
        "g": common_order,
        "A": local_a,
        "B": local_b,
        "gcd_AB_N_minus_1": stability_gcd,
        "factor_product_check": p * q == modulus,
    }


def exponent_pairs(bound: int):
    for total in range(2 * bound + 1):
        for exponent_a in range(bound + 1):
            exponent_b = total - exponent_a
            if 0 <= exponent_b <= bound:
                yield exponent_a, exponent_b


def multiplicative_order(value: int, modulus: int) -> int:
    if math.gcd(value, modulus) != 1:
        raise ValueError("The order is defined here only for a unit.")
    residue = 1
    for order in range(1, modulus + 1):
        residue = residue * value % modulus
        if residue == 1:
            return order
    raise AssertionError("A public unit order did not close within N steps.")


def run_target_free_menu(modulus: int, block_x: int) -> dict[str, object]:
    """Run the exact F96 menu using only N and its public normalized blocks."""
    bit_length = modulus.bit_length()
    bound = bit_length * bit_length
    subgroup_order = multiplicative_order(block_x, modulus)
    seed_inverse = pow(3, -1, modulus)
    seed_product = 3 * seed_inverse
    if seed_inverse != block_x * block_x:
        raise AssertionError("The public seed inverse is not x squared.")
    if seed_product != 3 * block_x * block_x or seed_product != 1 + 2 * modulus:
        raise AssertionError("The square-inverse family identity failed.")
    if math.isqrt(seed_product) ** 2 == seed_product:
        raise AssertionError("The seed relation must have nonzero square class.")

    seen_residues: set[int] = set()
    distinct_collisions = 0
    global_collisions = 0
    first_global_collision: dict[str, object] | None = None
    for pair_ordinal, (exponent_a, exponent_b) in enumerate(
        exponent_pairs(bound), start=1
    ):
        residue = (
            pow(3, exponent_a, modulus)
            * pow(block_x, exponent_b, modulus)
            % modulus
        )
        if residue in seen_residues:
            continue
        seen_residues.add(residue)
        if math.gcd(residue, modulus) != 1:
            raise AssertionError("A word in public unit blocks became a nonunit.")
        inverse = pow(residue, -1, modulus)
        relation_product = residue * inverse
        if relation_product % modulus != 1:
            raise AssertionError("A canonical inverse relation failed.")
        if relation_product == seed_product:
            continue
        combined = seed_product * relation_product
        induced_root = math.isqrt(combined)
        if induced_root * induced_root != combined:
            continue

        distinct_collisions += 1
        factor_minus = math.gcd(induced_root - 1, modulus)
        factor_plus = math.gcd(induced_root + 1, modulus)
        common = math.gcd(seed_product, relation_product)
        seed_square_root = math.isqrt(seed_product // common)
        new_square_root = math.isqrt(relation_product // common)
        if seed_square_root * seed_square_root != seed_product // common:
            raise AssertionError("The seed quotient did not normalize to a square.")
        if new_square_root * new_square_root != relation_product // common:
            raise AssertionError("The new quotient did not normalize to a square.")
        if induced_root != common * seed_square_root * new_square_root:
            raise AssertionError("The induced root did not match public normalization.")
        record = {
            "exponents": [exponent_a, exponent_b],
            "exponent_pair_ordinal_1_based": pair_ordinal,
            "unique_residue_ordinal_1_based": len(seen_residues),
            "c": residue,
            "w": inverse,
            "P": relation_product,
            "k": (relation_product - 1) // modulus,
            "normalization": {
                "D": common,
                "seed_root": seed_square_root,
                "new_root": new_square_root,
            },
            "induced_root": induced_root,
            "root_mod_n": induced_root % modulus,
            "gcd_root_minus_one_n": factor_minus,
            "gcd_root_plus_one_n": factor_plus,
            "useful": 1 < factor_minus < modulus,
        }
        if record["useful"]:
            return {
                "status": "useful_closure",
                "N": modulus,
                "x": block_x,
                "n": bit_length,
                "exponent_bound_each": bound,
                "menu_order": "increasing a+b, then increasing a; duplicate residues skipped",
                "exponent_pairs_total": (bound + 1) * (bound + 1),
                "exponent_pairs_examined_through_result": pair_ordinal,
                "unique_residues_examined_through_result": len(seen_residues),
                "generated_subgroup_order": subgroup_order,
                "menu_covers_entire_generated_subgroup": False,
                "distinct_same_class_collisions_through_result": distinct_collisions,
                "global_sign_collisions_through_result": global_collisions,
                "first_global_sign_collision": first_global_collision,
                "seed_relation": {
                    "g": 3,
                    "w": seed_inverse,
                    "P": seed_product,
                    "normalized_blocks": [3, block_x],
                },
                "first_useful_closure": record,
            }

        global_collisions += 1
        if first_global_collision is None:
            first_global_collision = record

    return {
        "status": "finite_null",
        "N": modulus,
        "x": block_x,
        "n": bit_length,
        "exponent_bound_each": bound,
        "menu_order": "increasing a+b, then increasing a; duplicate residues skipped",
        "exponent_pairs_total": (bound + 1) * (bound + 1),
        "exponent_pairs_examined_through_result": (bound + 1) * (bound + 1),
        "unique_residues_examined_through_result": len(seen_residues),
        "generated_subgroup_order": subgroup_order,
        "menu_covers_entire_generated_subgroup": len(seen_residues) == subgroup_order,
        "distinct_same_class_collisions_through_result": distinct_collisions,
        "global_sign_collisions_through_result": global_collisions,
        "first_global_sign_collision": first_global_collision,
        "seed_relation": {
            "g": 3,
            "w": seed_inverse,
            "P": seed_product,
            "normalized_blocks": [3, block_x],
        },
        "first_useful_closure": None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-min", type=int, required=True)
    parser.add_argument("--x-max", type=int, required=True)
    parser.add_argument("--control-x", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.x_min < 3 or args.x_min % 2 == 0 or args.x_max < args.x_min:
        raise ValueError("Require odd 3 <= x_min <= x_max.")
    if args.control_x % 2 == 0:
        raise ValueError("The control x must be odd.")

    started = time.monotonic()
    control_modulus = (3 * args.control_x * args.control_x - 1) // 2
    control_certificate = stable_semiprime_certificate(control_modulus)
    if control_certificate is None:
        raise AssertionError("The declared positive control is not a stable semiprime.")
    control_menu = run_target_free_menu(control_modulus, args.control_x)
    if control_menu["status"] != "useful_closure":
        raise AssertionError("The declared positive control did not close.")

    stable_inputs_tested: list[dict[str, object]] = []
    selection_trace: list[dict[str, object]] = []
    first_counterexample: dict[str, object] | None = None
    family_inputs_examined = 0
    semiprimes_rejected_as_unstable = 0
    not_distinct_odd_semiprimes_rejected = 0
    for block_x in range(args.x_min, args.x_max + 1, 2):
        family_inputs_examined += 1
        modulus = (3 * block_x * block_x - 1) // 2
        factors = factor_small(modulus)
        trace_record: dict[str, object] = {
            "x": block_x,
            "N": modulus,
            "factorization_certificate": {
                str(prime): exponent for prime, exponent in factors.items()
            },
        }
        distinct_odd_semiprime = (
            len(factors) == 2
            and all(exponent == 1 for exponent in factors.values())
            and 2 not in factors
        )
        if not distinct_odd_semiprime:
            not_distinct_odd_semiprimes_rejected += 1
            trace_record["selection_status"] = "not_distinct_odd_semiprime"
            selection_trace.append(trace_record)
            continue
        certificate = stable_semiprime_certificate(modulus)
        if certificate is None:
            semiprimes_rejected_as_unstable += 1
            trace_record["selection_status"] = "stable_condition_failed"
            selection_trace.append(trace_record)
            continue
        trace_record["selection_status"] = "selected_stable_semiprime"
        trace_record["stable_certificate"] = certificate
        selection_trace.append(trace_record)
        menu = run_target_free_menu(modulus, block_x)
        record = {
            "x": block_x,
            "N": modulus,
            "selection_certificate": certificate,
            "menu": menu,
        }
        stable_inputs_tested.append(record)
        if menu["status"] == "finite_null":
            first_counterexample = record
            break

    output = {
        "experiment_id": "F97_square_inverse_seed_n2_kill",
        "status": "counterexample" if first_counterexample is not None else "finite_cap_null",
        "family": "N_x=(3*x^2-1)/2 for odd x",
        "bounds": {
            "x_min_inclusive": args.x_min,
            "x_max_inclusive": args.x_max,
            "odd_x_only": True,
            "stop_rule": "first stable distinct odd semiprime with finite_null menu, else cap",
            "control_x": args.control_x,
        },
        "data_policy": {
            "input_selection_and_certificate_only": [
                "bounded trial factorization of N_x",
                "distinct odd semiprime test",
                "gcd(A*B,N_x-1)=1 stable-condition test",
            ],
            "per_input_selector_receives": [
                "N_x",
                "public normalized blocks 3 and x",
                "fixed exponent bound n^2 and ordering",
            ],
            "per_input_selector_does_not_receive": [
                "p or q",
                "a target endpoint",
                "a target relation value",
                "a target word",
            ],
        },
        "positive_control": {
            "x": args.control_x,
            "N": control_modulus,
            "selection_certificate": control_certificate,
            "menu": control_menu,
        },
        "search_counts": {
            "family_inputs_examined": family_inputs_examined,
            "not_distinct_odd_semiprimes_rejected": not_distinct_odd_semiprimes_rejected,
            "distinct_semiprimes_rejected_as_unstable": semiprimes_rejected_as_unstable,
            "stable_semiprimes_tested": len(stable_inputs_tested),
        },
        "stable_inputs_tested": stable_inputs_tested,
        "selection_trace": selection_trace,
        "first_counterexample": first_counterexample,
        "elapsed_seconds": time.monotonic() - started,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(f"status={output['status']}")
    print(
        f"control_N={control_modulus} control_status={control_menu['status']} "
        f"control_word={control_menu['first_useful_closure']['exponents']}"
    )
    print(
        f"family_inputs_examined={family_inputs_examined} "
        f"stable_semiprimes_tested={len(stable_inputs_tested)}"
    )
    if first_counterexample is not None:
        print(
            f"counterexample_x={first_counterexample['x']} "
            f"counterexample_N={first_counterexample['N']}"
        )
    print(f"output_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
