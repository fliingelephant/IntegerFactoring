#!/usr/bin/env python3
"""Finite checks for the proof-blind F09 phase reconstruction.

This script has no third-party dependencies.  It checks the character
classification on small fields, searches the cyclotomic product assertion for
many small primes, and emits the complete ell=3, N=91 certificate as JSON.
The finite search is corroboration only; RESULT.md contains the proofs.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from itertools import combinations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def primes_below(bound: int) -> list[int]:
    return [n for n in range(2, bound) if is_prime(n)]


def cyclotomic_prime_value(ell: int, x: int, modulus: int) -> int:
    return sum(pow(x, exponent, modulus) for exponent in range(ell)) % modulus


def cyclotomic_roots(ell: int, modulus: int) -> list[int]:
    return [
        x
        for x in range(modulus)
        if cyclotomic_prime_value(ell, x, modulus) == 0
    ]


def local_phase_exponent(a: int, p: int, root: int, ell: int) -> int:
    residue = pow(a % p, (p - 1) // ell, p)
    phase_log = {pow(root, exponent, p): exponent for exponent in range(ell)}
    return phase_log[residue]


def check_character_classification() -> dict[str, object]:
    checks: dict[str, object] = {}
    for ell in [2, 3, 5, 7, 11]:
        invariant_coefficients: list[list[int]] = []
        for a in range(ell):
            for b in range(ell):
                invariant = all(
                    (a * x + b * y - a * y - b * x) % ell == 0
                    for x in range(ell)
                    for y in range(ell)
                )
                if invariant:
                    invariant_coefficients.append([a, b])
        expected = [[coefficient, coefficient] for coefficient in range(ell)]
        assert invariant_coefficients == expected

        anti_diagonal = [(t, (-t) % ell) for t in range(ell)]
        for coefficient in range(1, ell):
            kernel = [
                [x, y]
                for x in range(ell)
                for y in range(ell)
                if coefficient * (x + y) % ell == 0
            ]
            assert kernel == [list(point) for point in anti_diagonal]

        checks[str(ell)] = {
            "invariant_coefficients": invariant_coefficients,
            "nontrivial_joint_rank": 1,
            "nontrivial_kernel_size": ell,
        }

    ell = 5
    zeta_labels = lambda point: point
    ordered_vector_distinct = len(
        {zeta_labels((x, y)) for x in range(ell) for y in range(ell)}
    )
    multiset_labels_by_sum: dict[str, int] = {}
    for total in range(ell):
        labels = {
            tuple(sorted((x, y)))
            for x in range(ell)
            for y in range(ell)
            if (x + y) % ell == total
        }
        multiset_labels_by_sum[str(total)] = len(labels)
        assert len(labels) == (ell + 1) // 2

    checks["swap_transcript_counterexamples_at_ell_5"] = {
        "ordered_vector_image_size": ordered_vector_distinct,
        "ordered_vector_kernel_size": 1,
        "multiset_labels_per_fixed_sum": multiset_labels_by_sum,
        "same_sum_distinguished_points": [[0, 0], [1, 4]],
    }
    return checks


def search_cyclotomic_product(bound: int) -> dict[str, object]:
    ell_values = [ell for ell in primes_below(32) if ell % 2 == 1]
    rational_prime_count = 0
    rational_a_count = 0
    symbol_evaluation_count = 0

    for ell in ell_values:
        for p in primes_below(bound):
            if p % ell != 1:
                continue
            roots = cyclotomic_roots(ell, p)
            assert len(roots) == ell - 1
            phase_logs = [
                {pow(root, exponent, p): exponent for exponent in range(ell)}
                for root in roots
            ]
            rational_prime_count += 1
            for a in range(1, p):
                residue = pow(a, (p - 1) // ell, p)
                exponent_sum = sum(phase_log[residue] for phase_log in phase_logs)
                assert exponent_sum % ell == 0
                rational_a_count += 1
                symbol_evaluation_count += len(roots)

    return {
        "ell_values": ell_values,
        "rational_prime_bound_exclusive": bound,
        "rational_primes_tested": rational_prime_count,
        "rational_a_values_tested": rational_a_count,
        "individual_symbols_evaluated": symbol_evaluation_count,
        "counterexamples": [],
    }


def build_n91_certificate() -> dict[str, object]:
    ell = 3
    factors = [7, 13]
    modulus = math.prod(factors)
    selected_root = 16
    local_roots = {p: selected_root % p for p in factors}
    assert local_roots == {7: 2, 13: 3}

    roots = cyclotomic_roots(ell, modulus)
    assert roots == [9, 16, 74, 81]
    root_rows = [
        {"rho": root, "mod_7": root % 7, "mod_13": root % 13}
        for root in roots
    ]

    root_gcds = {
        f"{left},{right}": math.gcd(right - left, modulus)
        for left, right in combinations(roots, 2)
    }
    assert root_gcds == {
        "9,16": 7,
        "9,74": 13,
        "9,81": 1,
        "16,74": 1,
        "16,81": 13,
        "74,81": 7,
    }

    requested_values = [15, 18, 16]
    requested_phase_pairs: dict[str, object] = {}
    for value in requested_values:
        pair = [
            local_phase_exponent(value, p, local_roots[p], ell) for p in factors
        ]
        requested_phase_pairs[str(value)] = {
            "phase_exponents_at_7_and_13": pair,
            "scalar_product_exponent": sum(pair) % ell,
        }
    assert requested_phase_pairs == {
        "15": {
            "phase_exponents_at_7_and_13": [0, 1],
            "scalar_product_exponent": 1,
        },
        "18": {
            "phase_exponents_at_7_and_13": [1, 0],
            "scalar_product_exponent": 1,
        },
        "16": {
            "phase_exponents_at_7_and_13": [2, 1],
            "scalar_product_exponent": 0,
        },
    }

    requested_phase_pairs_by_root: dict[str, object] = {}
    for root in roots:
        roots_at_factors = {p: root % p for p in factors}
        requested_phase_pairs_by_root[str(root)] = {}
        for value in requested_values:
            pair = [
                local_phase_exponent(value, p, roots_at_factors[p], ell)
                for p in factors
            ]
            requested_phase_pairs_by_root[str(root)][str(value)] = {
                "phase_exponents_at_7_and_13": pair,
                "scalar_product_exponent": sum(pair) % ell,
            }
    assert requested_phase_pairs_by_root == {
        "9": {
            "15": {"phase_exponents_at_7_and_13": [0, 2], "scalar_product_exponent": 2},
            "18": {"phase_exponents_at_7_and_13": [1, 0], "scalar_product_exponent": 1},
            "16": {"phase_exponents_at_7_and_13": [2, 2], "scalar_product_exponent": 1},
        },
        "16": requested_phase_pairs,
        "74": {
            "15": {"phase_exponents_at_7_and_13": [0, 2], "scalar_product_exponent": 2},
            "18": {"phase_exponents_at_7_and_13": [2, 0], "scalar_product_exponent": 2},
            "16": {"phase_exponents_at_7_and_13": [1, 2], "scalar_product_exponent": 0},
        },
        "81": {
            "15": {"phase_exponents_at_7_and_13": [0, 1], "scalar_product_exponent": 1},
            "18": {"phase_exponents_at_7_and_13": [2, 0], "scalar_product_exponent": 2},
            "16": {"phase_exponents_at_7_and_13": [1, 1], "scalar_product_exponent": 2},
        },
    }

    pair_fibers: Counter[tuple[int, int]] = Counter()
    scalar_fibers: Counter[int] = Counter()
    multiset_fibers: Counter[tuple[int, int]] = Counter()
    units = [value for value in range(modulus) if math.gcd(value, modulus) == 1]
    for value in units:
        pair = tuple(
            local_phase_exponent(value, p, local_roots[p], ell) for p in factors
        )
        pair_fibers[pair] += 1
        scalar_fibers[sum(pair) % ell] += 1
        multiset_fibers[tuple(sorted(pair))] += 1

    assert len(units) == 72
    assert set(pair_fibers.values()) == {8}
    assert scalar_fibers == Counter({0: 24, 1: 24, 2: 24})
    assert multiset_fibers == Counter(
        {(0, 0): 8, (0, 1): 16, (0, 2): 16, (1, 1): 8, (1, 2): 16, (2, 2): 8}
    )

    conjugate_pairs = {str(root): pow(root, 2, modulus) for root in roots}
    assert conjugate_pairs == {"9": 81, "16": 74, "74": 16, "81": 9}

    return {
        "ell": ell,
        "N": modulus,
        "factorization_used_for_check": factors,
        "selected_root": selected_root,
        "selected_local_roots": {str(p): local_roots[p] for p in factors},
        "requested_phase_pairs": requested_phase_pairs,
        "requested_phase_pairs_by_global_root": requested_phase_pairs_by_root,
        "unit_group_size": len(units),
        "ordered_phase_pair_fibers": {
            f"{left},{right}": pair_fibers[(left, right)]
            for left in range(ell)
            for right in range(ell)
        },
        "scalar_product_fibers": {
            str(exponent): scalar_fibers[exponent] for exponent in range(ell)
        },
        "unordered_phase_multiset_fibers": {
            f"{left},{right}": multiset_fibers[(left, right)]
            for left in range(ell)
            for right in range(left, ell)
        },
        "roots_of_Phi_3_mod_N": root_rows,
        "pairwise_root_difference_gcds": root_gcds,
        "root_conjugation_rho_to_rho_squared": conjugate_pairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=2000)
    args = parser.parse_args()

    report = {
        "character_checks": check_character_classification(),
        "cyclotomic_product_counterexample_search": search_cyclotomic_product(
            args.prime_bound
        ),
        "ell_3_N_91_certificate": build_n91_certificate(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
