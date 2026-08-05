#!/usr/bin/env python3
"""Exact finite kill tests for the F13 Teichmuller-lift route.

Approach-family ID: F13_teichmuller_lift_kill.
Python standard library only; every reported probability is exact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


FAMILY = "F13_teichmuller_lift_kill"
INSTANCES = [
    (3, 5),
    (3, 7),
    (5, 7),
    (7, 11),
    (11, 13),
    (13, 17),
    (101, 103),
    (1009, 1013),
    (10007, 10009),
]
ITERATIONS = 3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def lcm(left: int, right: int) -> int:
    return left // math.gcd(left, right) * right


def crt_pair(left: int, right: int, left_modulus: int, right_modulus: int) -> int:
    return (
        left
        + left_modulus
        * ((right - left) * pow(left_modulus, -1, right_modulus) % right_modulus)
    ) % (left_modulus * right_modulus)


def teichmuller(residue: int, prime: int) -> int:
    return pow(residue % prime, prime, prime * prime)


def global_teichmuller(base: int, p: int, q: int) -> int:
    return crt_pair(teichmuller(base, p), teichmuller(base, q), p * p, q * q)


def valuation_category(value: int, prime: int) -> int:
    value %= prime * prime
    if value % prime:
        return 0
    return 2 if value == 0 else 1


def additive_categories(prime: int, exponent: int) -> list[int]:
    modulus = prime * prime

    def twisted(value: int) -> int:
        return pow(value % prime, prime * exponent, modulus)

    counts = [0, 0, 0]
    for ratio in range(1, prime):
        defect = (twisted(ratio + 1) - twisted(ratio) - 1) % modulus
        counts[valuation_category(defect, prime)] += 1
    assert sum(counts) == prime - 1
    return counts


def category_probability(counts: list[int], prime: int, category: int) -> Fraction:
    return Fraction(counts[category], prime - 1)


def additive_success_record(p: int, q: int) -> dict[str, object]:
    counts_p = additive_categories(p, q)
    counts_q = additive_categories(q, p)
    probabilities_p = [category_probability(counts_p, p, category) for category in range(3)]
    probabilities_q = [category_probability(counts_q, q, category) for category in range(3)]
    first_stage = probabilities_p[0] * (probabilities_q[1] + probabilities_q[2]) + (
        probabilities_p[1] + probabilities_p[2]
    ) * probabilities_q[0]
    second_stage = probabilities_p[1] * probabilities_q[2] + probabilities_p[2] * probabilities_q[1]
    total = first_stage + second_stage
    assert total == 1 - sum(
        probabilities_p[category] * probabilities_q[category] for category in range(3)
    )
    return {
        "local_category_counts_p": counts_p,
        "local_category_counts_q": counts_q,
        "local_category_probabilities_p": [str(value) for value in probabilities_p],
        "local_category_probabilities_q": [str(value) for value in probabilities_q],
        "first_gcd_success_probability": str(first_stage),
        "principal_quotient_extra_probability": str(second_stage),
        "two_stage_total_success_probability": str(total),
        "expected_independent_trials": str(1 / total) if total else None,
    }


def iterated_difference_record(p: int, q: int) -> dict[str, object]:
    common = math.gcd(p - 1, q - 1)
    records = []
    union_bound = Fraction(0)
    for iteration in range(1, ITERATIONS + 1):
        zero_p = Fraction(common, p - 1)
        zero_q = Fraction(math.gcd((p**iteration) * (p - 1), q - 1), q - 1)
        success = zero_p * (1 - zero_q) + (1 - zero_p) * zero_q
        union_bound += success
        records.append(
            {
                "difference": f"tau^{iteration + 1}(a)-tau^{iteration}(a)",
                "zero_probability_mod_p": str(zero_p),
                "zero_probability_mod_q": str(zero_q),
                "proper_gcd_probability": str(success),
            }
        )
    return {
        "gcd_p_minus_1_q_minus_1": common,
        "iterations": records,
        "three_value_union_bound": str(min(Fraction(1), union_bound)),
        "note": "A local iterated difference divisible by a prime is already zero modulo its square.",
    }


def high_digit_record(p: int, q: int) -> dict[str, object]:
    n = p * q
    marginal_p_bound = Fraction(math.ceil(q / p), q - 1)
    marginal_q_bound = Fraction(1, p - 1)
    collection_bound = min(Fraction(1), ITERATIONS * (marginal_p_bound + marginal_q_bound))
    record: dict[str, object] = {
        "per_value_zero_probability_mod_p_upper_bound": str(marginal_p_bound),
        "per_value_zero_probability_mod_q_upper_bound": str(marginal_q_bound),
        "three_value_proper_gcd_union_bound": str(collection_bound),
        "bound_hypothesis": "p<q<2p and both exponent maps permute the local unit groups",
    }
    if n <= 50_000:
        unit_count = 0
        successes = [0] * ITERATIONS
        union_successes = 0
        modulus = n * n
        for base in range(1, n):
            if math.gcd(base, n) != 1:
                continue
            unit_count += 1
            any_success = False
            exponent = n
            for index in range(ITERATIONS):
                lifted = pow(base, exponent, modulus)
                high_digit = (lifted - lifted % n) // n
                divisor = math.gcd(high_digit, n)
                if 1 < divisor < n:
                    successes[index] += 1
                    any_success = True
                exponent *= n
            union_successes += any_success
        record.update(
            {
                "exact_unit_count": unit_count,
                "exact_per_value_proper_gcd_probabilities": [
                    str(Fraction(count, unit_count)) for count in successes
                ],
                "exact_three_value_union_probability": str(Fraction(union_successes, unit_count)),
            }
        )
    return record


def two_stage_additive(base_a: int, base_b: int, n: int) -> tuple[int, int | None]:
    modulus = n * n
    defect = (
        pow((base_a + base_b) % modulus, n, modulus)
        - pow(base_a, n, modulus)
        - pow(base_b, n, modulus)
    ) % modulus
    first = math.gcd(defect, n)
    if first != n:
        return first, None
    assert defect % n == 0
    second = math.gcd(defect // n, n)
    return first, second


def fixed_probe_record(p: int, q: int) -> dict[str, object]:
    n = p * q
    modulus = n * n
    units = [value for value in range(1, min(n, 65)) if math.gcd(value, n) == 1]
    additive_pairs = [
        (left, right)
        for left in units[:12]
        for right in units[:12]
    ]
    additive_successes = []
    for left, right in additive_pairs:
        first, second = two_stage_additive(left, right, n)
        divisor = first if 1 < first < n else second
        if divisor is not None and 1 < divisor < n:
            additive_successes.append([left, right, divisor])

    iterate_successes = []
    high_digit_successes = []
    for base in units:
        values = [pow(base, n**iteration, modulus) for iteration in range(1, ITERATIONS + 2)]
        for iteration in range(ITERATIONS):
            divisor = math.gcd(values[iteration + 1] - values[iteration], n)
            if 1 < divisor < n:
                iterate_successes.append([base, iteration + 1, divisor])
            high_digit = (values[iteration] - values[iteration] % n) // n
            divisor = math.gcd(high_digit, n)
            if 1 < divisor < n:
                high_digit_successes.append([base, iteration + 1, divisor])

    twice_root = math.isqrt(4 * n)
    if twice_root * twice_root < 4 * n:
        twice_root += 1
    identity_gcds = []
    for base in units:
        lifted = pow(base, n, modulus)
        assert pow(lifted, n + 1, modulus) == pow(lifted, p + q, modulus)
        defect = (pow(lifted, n + 1, modulus) - pow(lifted, twice_root, modulus)) % modulus
        divisor = math.gcd(defect, n)
        if 1 < divisor < n:
            identity_gcds.append([base, divisor])

    return {
        "bases_tested": len(units),
        "additive_pairs_tested": len(additive_pairs),
        "additive_two_stage_factor_hits": additive_successes[:20],
        "iterated_difference_factor_hits": iterate_successes[:20],
        "high_digit_factor_hits": high_digit_successes[:20],
        "ceil_2_sqrt_N": twice_root,
        "true_p_plus_q": p + q,
        "rounded_exponent_identity_factor_hits": identity_gcds[:20],
    }


def structural_record(p: int, q: int) -> dict[str, object]:
    n = p * q
    modulus = n * n
    assert is_prime(p) and is_prime(q) and p < q

    sample_bases = [base for base in range(1, min(n, 80)) if math.gcd(base, n) == 1]
    for base in sample_bases:
        lifted = pow(base, n, modulus)
        assert lifted % (p * p) == pow(teichmuller(base, p), q, p * p)
        assert lifted % (q * q) == pow(teichmuller(base, q), p, q * q)
        assert pow(lifted, n + 1, modulus) == pow(lifted, p + q, modulus)
        assert (pow((base * 2) % modulus, n, modulus) - pow(base, n, modulus) * pow(2, n, modulus)) % modulus == 0

    principal_samples = range(n) if n <= 50_000 else list(range(100)) + [n - 1]
    coordinate_pairs = set()
    for coefficient in principal_samples:
        principal = (1 + coefficient * n) % modulus
        assert pow(principal, n, modulus) == 1
        coordinate_pairs.add(((q * coefficient) % p, (p * coefficient) % q))
    if n <= 50_000:
        assert len(coordinate_pairs) == n

    exponent = lcm(p - 1, q - 1)
    exponent_gcd = math.gcd(n, exponent)
    untwist_verified = False
    if exponent_gcd == 1:
        inverse_exponent = pow(n, -1, exponent)
        for base in sample_bases:
            assert pow(pow(base, n, modulus), inverse_exponent, modulus) == global_teichmuller(base, p, q)
        untwist_verified = True
    else:
        inverse_exponent = None

    return {
        "N": n,
        "p": p,
        "q": q,
        "balanced_q_lt_2p": q < 2 * p,
        "lambda_teichmuller_quotient": exponent,
        "gcd_N_lambda": exponent_gcd,
        "factor_aware_inverse_N_mod_lambda": inverse_exponent,
        "factor_aware_untwist_verified": untwist_verified,
        "principal_coefficients_checked": len(principal_samples),
        "principal_coordinate_pairs_distinct": len(coordinate_pairs),
        "additive_defect": additive_success_record(p, q),
        "iterated_tau_difference": iterated_difference_record(p, q),
        "principal_high_digit": high_digit_record(p, q),
        "fixed_small_probes": fixed_probe_record(p, q),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    records = [structural_record(p, q) for p, q in INSTANCES]
    source = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "instances": records,
        "source": str(source),
        "source_sha256": sha256(source),
    }
    Path(args.output).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

