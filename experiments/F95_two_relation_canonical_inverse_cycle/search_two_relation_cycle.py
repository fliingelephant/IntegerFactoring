#!/usr/bin/env python3
"""Bounded public search for a two-relation canonical-inverse saturation cycle."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


def factor_public_integer(value: int) -> dict[int, int]:
    """Trial-factor a public certificate integer; never used to select candidates."""
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


def is_prime_public(value: int) -> bool:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--ell", type=int, default=2)
    parser.add_argument("--g-min", type=int, default=2)
    parser.add_argument("--g-max", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    modulus = args.n
    ell = args.ell
    if ell != 2:
        raise ValueError("This bounded run implements the requested ell=2 first test.")
    if not (2 <= args.g_min <= args.g_max < modulus):
        raise ValueError("Require 2 <= g_min <= g_max < N.")

    # Candidate construction uses only N, gcd, inversion, multiplication, and
    # exact integer comparisons.  Inverse-paired endpoints are deduplicated by
    # their exact relation value P=g*w.
    relation_by_value: dict[int, dict[str, int]] = {}
    unit_candidates = 0
    nonunit_candidates = 0
    inverse_one_candidates = 0
    for raw_g in range(args.g_min, args.g_max + 1):
        common = math.gcd(raw_g, modulus)
        if common != 1:
            nonunit_candidates += 1
            continue
        unit_candidates += 1
        raw_w = pow(raw_g, -1, modulus)
        if raw_w <= 1:
            inverse_one_candidates += 1
            continue
        g = min(raw_g, raw_w)
        w = max(raw_g, raw_w)
        product = g * w
        if product % modulus != 1:
            raise AssertionError("Canonical inverse relation failed.")
        quotient = (product - 1) // modulus
        record = {
            "g": g,
            "w": w,
            "P": product,
            "k": quotient,
        }
        previous = relation_by_value.get(product)
        if previous is None or (g, w) < (previous["g"], previous["w"]):
            relation_by_value[product] = record

    relations = sorted(
        relation_by_value.values(),
        key=lambda item: (item["P"], item["g"], item["w"]),
    )
    for index, relation in enumerate(relations):
        relation["relation_index"] = index
        root = math.isqrt(relation["P"])
        relation["individual_exact_square"] = root * root == relation["P"]

    # Lexicographic finite enumeration: relations are sorted by
    # (P,g,w), then all i<j pairs are tested in nested-loop order.  The
    # search test is factor-free with respect to P_i: equal nonzero parity
    # columns are detected by P_i*P_j being a square while neither P_i is a
    # square.  Hidden factors of N are never used.
    pair_tests = 0
    square_product_pairs = 0
    witness: dict[str, object] | None = None
    for first_index, first in enumerate(relations):
        if first["individual_exact_square"]:
            continue
        for second_index in range(first_index + 1, len(relations)):
            second = relations[second_index]
            if second["individual_exact_square"]:
                continue
            pair_tests += 1
            combined = first["P"] * second["P"]
            induced_root = math.isqrt(combined)
            if induced_root * induced_root != combined:
                continue
            square_product_pairs += 1
            factor_minus = math.gcd(induced_root - 1, modulus)
            if not (1 < factor_minus < modulus):
                continue

            first_factors = factor_public_integer(first["P"])
            second_factors = factor_public_integer(second["P"])
            basis = sorted(set(first_factors) | set(second_factors))
            first_column = [first_factors.get(prime, 0) for prime in basis]
            second_column = [second_factors.get(prime, 0) for prime in basis]
            first_mod = [entry % ell for entry in first_column]
            second_mod = [entry % ell for entry in second_column]
            if not any(first_mod) or not any(second_mod):
                raise AssertionError("An individually nonclosing column became zero.")
            if first_mod != second_mod:
                raise AssertionError("Square product did not give equal parity columns.")

            shared_block = math.gcd(first["P"], second["P"])
            residual_1 = first["P"] // shared_block
            residual_2 = second["P"] // shared_block
            residual_root_1 = math.isqrt(residual_1)
            residual_root_2 = math.isqrt(residual_2)
            if residual_root_1 * residual_root_1 != residual_1:
                raise AssertionError("First quotient by the shared block is not square.")
            if residual_root_2 * residual_root_2 != residual_2:
                raise AssertionError("Second quotient by the shared block is not square.")
            public_basis = [shared_block, residual_root_1, residual_root_2]
            if any(
                math.gcd(public_basis[i], public_basis[j]) != 1
                for i in range(len(public_basis))
                for j in range(i + 1, len(public_basis))
            ):
                raise AssertionError("The witness public basis is not pairwise coprime.")

            cofactor = modulus // factor_minus
            witness = {
                "selection_order": {
                    "criterion": "first successful i<j in relations sorted by (P,g,w)",
                    "first_index": first_index,
                    "second_index": second_index,
                    "pair_tests_before_and_including_witness": pair_tests,
                },
                "relation_1": first,
                "relation_2": second,
                "distinct_relation_values": first["P"] != second["P"],
                "gcd_free_prime_basis_certificate": basis,
                "integer_exponent_column_1": first_column,
                "integer_exponent_column_2": second_column,
                "column_mod_ell_1": first_mod,
                "column_mod_ell_2": second_mod,
                "individual_nonclosing": [any(first_mod), any(second_mod)],
                "second_closes_after_first": first_mod == second_mod,
                "kernel_direction_mod_ell": [1, 1],
                "first_matrix_rank_mod_ell": 1,
                "two_column_matrix_rank_mod_ell": 1,
                "first_kernel_dimension": 0,
                "two_column_kernel_dimension": 1,
                "public_square_normalized_basis": public_basis,
                "public_integer_exponent_column_1": [1, 2, 0],
                "public_integer_exponent_column_2": [1, 0, 2],
                "public_column_mod_ell_1": [1, 0, 0],
                "public_column_mod_ell_2": [1, 0, 0],
                "combined_product": combined,
                "induced_exact_root": induced_root,
                "root_square_check": induced_root * induced_root == combined,
                "root_mod_n": induced_root % modulus,
                "gcd_root_minus_one_n": factor_minus,
                "gcd_root_plus_one_n": math.gcd(induced_root + 1, modulus),
                "verified_factor": factor_minus,
                "verified_cofactor": cofactor,
                "factor_product_check": factor_minus * cofactor == modulus,
                "factor_is_prime": is_prime_public(factor_minus),
                "cofactor_is_prime": is_prime_public(cofactor),
                "deleting_first_relation_loses_second_closure": any(second_mod),
                "public_factorizations_for_certificate": {
                    str(first["P"]): {str(p): e for p, e in first_factors.items()},
                    str(second["P"]): {str(p): e for p, e in second_factors.items()},
                },
            }
            break
        if witness is not None:
            break

    output = {
        "experiment_id": "F95_two_relation_canonical_inverse_cycle",
        "status": "witness" if witness is not None else "finite_null",
        "algorithm_data_policy": {
            "candidate_selection_uses_hidden_factors": False,
            "candidate_operations": [
                "integer range enumeration",
                "gcd(g,N)",
                "least positive modular inverse",
                "exact multiplication and division",
                "integer square root",
                "gcd(root-1,N)",
            ],
            "public_trial_factorization_use": (
                "witness certificate only; not used to select or reject pairs"
            ),
        },
        "bounds": {
            "N": modulus,
            "ell": ell,
            "g_min_inclusive": args.g_min,
            "g_max_inclusive": args.g_max,
            "full_nontrivial_residue_range": (
                args.g_min == 2 and args.g_max == modulus - 1
            ),
            "pair_order": "lexicographic after sorting unique relations by (P,g,w)",
        },
        "counts": {
            "raw_g_candidates": args.g_max - args.g_min + 1,
            "unit_candidates": unit_candidates,
            "nonunit_candidates_skipped_after_public_gcd": nonunit_candidates,
            "inverse_one_candidates_skipped": inverse_one_candidates,
            "unique_canonical_relation_values": len(relations),
            "non_square_relation_values": sum(
                not relation["individual_exact_square"] for relation in relations
            ),
            "pair_tests": pair_tests,
            "square_product_pairs_seen": square_product_pairs,
        },
        "witness": witness,
        "elapsed_seconds": time.monotonic() - started,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(f"status={output['status']}")
    print(f"N={modulus} ell={ell} g_range=[{args.g_min},{args.g_max}]")
    print(
        "relations="
        f"{len(relations)} pair_tests={pair_tests} "
        f"square_product_pairs={square_product_pairs}"
    )
    if witness is not None:
        print(
            "witness="
            f"P1={witness['relation_1']['P']} "
            f"P2={witness['relation_2']['P']} "
            f"root={witness['induced_exact_root']} "
            f"factor={witness['verified_factor']}"
        )
    print(f"output_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
