#!/usr/bin/env python3
"""Independent finite certificate for the reconstructed F13 statements.

The assertions exhaust all residue classes for the listed small prime pairs.
They check the algebraic formulas, but the accompanying RESULT.md contains the
general proofs.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
from pathlib import Path


def units(modulus: int) -> list[int]:
    return [value for value in range(modulus) if math.gcd(value, modulus) == 1]


def tau(value: int, modulus: int) -> int:
    return pow(value, modulus, modulus * modulus)


def teichmueller(value: int, prime: int) -> int:
    """Return the unique lift modulo prime^2 satisfying T^prime = T."""
    residue = value % prime
    candidates = [
        residue + digit * prime
        for digit in range(prime)
        if pow(residue + digit * prime, prime, prime * prime)
        == (residue + digit * prime) % (prime * prime)
    ]
    assert len(candidates) == 1
    return candidates[0]


def valuation_category(value: int, prime: int) -> int:
    if value % prime:
        return 0
    if value % (prime * prime):
        return 1
    return 2


def high_digit(value: int, modulus: int) -> int:
    canonical = value % (modulus * modulus)
    low = canonical % modulus
    return ((canonical - low) // modulus) % modulus


def proper_factor(value: int, modulus: int) -> bool:
    divisor = math.gcd(value, modulus)
    return 1 < divisor < modulus


def check_structure(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    square = modulus * modulus
    quotient_units = units(modulus)

    actual_kernel = [value for value in units(square) if value % modulus == 1]
    stated_kernel = sorted((1 + digit * modulus) % square for digit in range(modulus))
    assert actual_kernel == stated_kernel
    assert all(tau(value, modulus) == 1 for value in actual_kernel)

    for value in quotient_units:
        expected_p = pow(teichmueller(value, p), q, p * p)
        expected_q = pow(teichmueller(value, q), p, q * q)
        image = tau(value, modulus)
        assert image % (p * p) == expected_p
        assert image % (q * q) == expected_q
        for kernel_element in actual_kernel:
            assert tau(value * kernel_element, modulus) == image

        assert pow(image, modulus + 1, square) == pow(image, p + q, square)

    exponent = math.lcm(p - 1, q - 1)
    invertible = math.gcd(modulus, exponent) == 1
    quotient_image = {pow(value, modulus, modulus) for value in quotient_units}
    assert (len(quotient_image) == len(quotient_units)) == invertible

    inverse = None
    if invertible:
        inverse = pow(modulus, -1, exponent)
        for value in quotient_units:
            image = tau(value, modulus)
            untwisted = pow(image, inverse, square)
            assert untwisted % modulus == value
            assert untwisted % (p * p) == teichmueller(value, p)
            assert untwisted % (q * q) == teichmueller(value, q)

    return {
        "p": p,
        "q": q,
        "kernel_size": len(actual_kernel),
        "quotient_exponent": exponent,
        "power_map_invertible": invertible,
        "inverse_exponent": inverse,
        "quotient_image_size": len(quotient_image),
    }


def check_consecutive_differences(p: int, q: int, comparisons: int) -> dict[str, object]:
    modulus = p * q
    square = modulus * modulus
    bases = units(modulus)
    states = [tau(base, modulus) for base in bases]
    rows = []

    for index in range(1, comparisons + 1):
        next_states = [tau(state, modulus) for state in states]
        equal_p = equal_q = success = 0
        local_categories_p = [0, 0, 0]
        local_categories_q = [0, 0, 0]
        for state, next_state in zip(states, next_states, strict=True):
            difference = (next_state - state) % square
            category_p = valuation_category(difference, p)
            category_q = valuation_category(difference, q)
            local_categories_p[category_p] += 1
            local_categories_q[category_q] += 1
            assert category_p != 1
            assert category_q != 1
            p_equal = category_p == 2
            q_equal = category_q == 2
            equal_p += p_equal
            equal_q += q_equal
            success += p_equal != q_equal

        roots_p = math.gcd(pow(q, index) * (q - 1), p - 1)
        roots_q = math.gcd(pow(p, index) * (p - 1), q - 1)
        expected_equal_p = roots_p * (q - 1)
        expected_equal_q = roots_q * (p - 1)
        expected_success = expected_equal_p + expected_equal_q - 2 * roots_p * roots_q
        assert equal_p == expected_equal_p
        assert equal_q == expected_equal_q
        assert success == expected_success
        rows.append(
            {
                "comparison": index,
                "roots_mod_p": roots_p,
                "roots_mod_q": roots_q,
                "equal_mod_p2": equal_p,
                "equal_mod_q2": equal_q,
                "proper_gcd_successes": success,
                "valuation_counts_p": local_categories_p,
                "valuation_counts_q": local_categories_q,
            }
        )
        states = next_states

    return {"p": p, "q": q, "unit_count": len(bases), "comparisons": rows}


def local_additive_counts(p: int, q: int, prime: int) -> list[int]:
    modulus = p * q
    counts = [0, 0, 0]
    for residue in range(1, prime):
        defect = (
            pow(residue + 1, modulus, prime * prime)
            - pow(residue, modulus, prime * prime)
            - 1
        ) % (prime * prime)

        if prime == p:
            formula = (
                pow(teichmueller(residue + 1, p), q, p * p)
                - pow(teichmueller(residue, p), q, p * p)
                - 1
            ) % (p * p)
        else:
            formula = (
                pow(teichmueller(residue + 1, q), p, q * q)
                - pow(teichmueller(residue, q), p, q * q)
                - 1
            ) % (q * q)
        assert defect == formula
        counts[valuation_category(defect, prime)] += 1
    return counts


def predicted_two_stage_success(counts_p: list[int], counts_q: list[int]) -> int:
    p0, p1, p2 = counts_p
    q0, q1, q2 = counts_q
    return p0 * (q1 + q2) + (p1 + p2) * q0 + p1 * q2 + p2 * q1


def check_additive_defect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    square = modulus * modulus
    counts_p = local_additive_counts(p, q, p)
    counts_q = local_additive_counts(p, q, q)
    pair_counts: collections.Counter[tuple[int, int]] = collections.Counter()
    successes = 0

    for base in units(modulus):
        defect = (tau(base + 1, modulus) - tau(base, modulus) - 1) % square
        category_pair = (valuation_category(defect, p), valuation_category(defect, q))
        pair_counts[category_pair] += 1

        first = math.gcd(defect, modulus)
        succeeded = proper_factor(defect, modulus)
        if first == modulus:
            assert defect % modulus == 0
            succeeded = proper_factor((defect // modulus) % modulus, modulus)
        successes += succeeded

    for category_p in range(3):
        for category_q in range(3):
            assert pair_counts[(category_p, category_q)] == counts_p[category_p] * counts_q[category_q]

    predicted = predicted_two_stage_success(counts_p, counts_q)
    assert successes == predicted

    if q == p + 2 and p > 3:
        assert counts_p == [p - 2, 0, 1]
        assert counts_q == [q - 4, 0, 3]
        assert successes == 4 * (p - 2)
    if (p, q) == (3, 5):
        assert counts_p == [0, 1, 1]
        assert counts_q == [3, 0, 1]
        assert successes == 7

    return {
        "p": p,
        "q": q,
        "unit_count": (p - 1) * (q - 1),
        "valuation_counts_p": counts_p,
        "valuation_counts_q": counts_q,
        "two_stage_successes": successes,
        "two_stage_probability": f"{successes}/{(p - 1) * (q - 1)}",
    }


def check_high_digits(p: int, q: int, iterate_count: int) -> dict[str, object]:
    assert p < q < 2 * p
    modulus = p * q
    bases = units(modulus)
    states = [tau(base, modulus) for base in bases]
    union_success = [False] * len(bases)
    rows = []

    assert math.gcd(q, p - 1) == 1
    assert math.gcd(p, q - 1) == 1

    for index in range(1, iterate_count + 1):
        lows = [state % modulus for state in states]
        assert len(set(lows)) == len(bases)

        divisible_p = divisible_q = successes = 0
        for position, state in enumerate(states):
            digit = high_digit(state, modulus)
            p_event = digit % p == 0
            q_event = digit % q == 0
            divisible_p += p_event
            divisible_q += q_event
            success = p_event != q_event
            successes += success
            union_success[position] |= success

        assert divisible_p <= 2 * (p - 1)
        assert divisible_q <= q - 1
        assert successes <= 2 * (p - 1) + (q - 1)
        rows.append(
            {
                "iterate": index,
                "p_divides_high_digit": divisible_p,
                "q_divides_high_digit": divisible_q,
                "proper_gcd_successes": successes,
            }
        )
        states = [tau(state, modulus) for state in states]

    union_count = sum(union_success)
    count_bound = iterate_count * (2 * (p - 1) + (q - 1))
    assert union_count <= count_bound
    return {
        "p": p,
        "q": q,
        "unit_count": len(bases),
        "iterate_count": iterate_count,
        "iterates": rows,
        "union_successes": union_count,
        "union_count_bound": count_bound,
        "probability_bound": f"{iterate_count}*(2/{q - 1}+1/{p - 1})",
    }


def build_report() -> dict[str, object]:
    structure_pairs = [(3, 5), (3, 7), (5, 7), (7, 13)]
    difference_pairs = [(3, 7), (5, 7), (7, 11), (7, 13), (11, 13), (17, 19)]
    additive_pairs = [(3, 5), (5, 7), (7, 11), (11, 13), (17, 19), (29, 31)]
    balanced_pairs = [(3, 5), (5, 7), (7, 11), (7, 13), (11, 13), (13, 17), (17, 19), (19, 23), (23, 43)]
    return {
        "status": "all assertions passed",
        "structure": [check_structure(p, q) for p, q in structure_pairs],
        "consecutive_differences": [
            check_consecutive_differences(p, q, comparisons=3) for p, q in difference_pairs
        ],
        "additive_defect": [check_additive_defect(p, q) for p, q in additive_pairs],
        "high_digits": [check_high_digits(p, q, iterate_count=4) for p, q in balanced_pairs],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    report = build_report()
    arguments.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: all assertions passed; wrote {arguments.output}")


if __name__ == "__main__":
    main()
