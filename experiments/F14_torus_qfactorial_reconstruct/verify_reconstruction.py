#!/usr/bin/env python3
"""Independent finite checks for F14 torus q-factorial reconstruction.

Approach-family ID: F14_torus_qfactorial_reconstruct.
Python standard library only.  The accompanying RESULT.md contains the proofs;
this source records exact finite witnesses and sanity checks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


FAMILY = "F14_torus_qfactorial_reconstruct"


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


def prime_factors(value: int) -> list[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime: int) -> int:
    assert is_prime(prime)
    if prime == 2:
        return 1
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("prime field has no primitive root")


def multiplicative_order(value: int, prime: int) -> int:
    assert math.gcd(value, prime) == 1
    order = prime - 1
    for factor in prime_factors(order):
        while order % factor == 0 and pow(value, order // factor, prime) == 1:
            order //= factor
    return order


def prime_field_order_witness(order: int) -> dict[str, int]:
    if order == 1:
        return {"order": 1, "prime": 2, "element": 1}
    multiplier = 1
    while True:
        prime = multiplier * order + 1
        if is_prime(prime):
            generator = primitive_root(prime)
            element = pow(generator, (prime - 1) // order, prime)
            assert multiplicative_order(element, prime) == order
            return {"order": order, "prime": prime, "element": element}
        multiplier += 1


def p_value(base: int, m_bound: int) -> int:
    value = 1
    for exponent in range(1, m_bound + 1):
        value *= 1 - base**exponent
    return value


def t_value(base: int, length: int) -> int:
    value = 1
    for exponent in range(1, length + 1):
        value *= (1 - base**exponent) ** (length + 1 - exponent)
    return value


def modular_p_value(base: int, length: int, modulus: int) -> int:
    value = 1
    for exponent in range(1, length + 1):
        value = value * (1 - pow(base, exponent, modulus)) % modulus
    return value


def modular_t_value(base: int, length: int, modulus: int) -> int:
    value = 1
    for exponent in range(1, length + 1):
        factor = (1 - pow(base, exponent, modulus)) % modulus
        value = value * pow(factor, length + 1 - exponent, modulus) % modulus
    return value


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        if left_coefficient == 0:
            continue
        for right_index, right_coefficient in enumerate(right):
            if right_coefficient:
                result[left_index + right_index] += left_coefficient * right_coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_power(base: list[int], exponent: int) -> list[int]:
    result = [1]
    while exponent:
        if exponent & 1:
            result = poly_multiply(result, base)
        exponent >>= 1
        if exponent:
            base = poly_multiply(base, base)
    return result


def binomial_factor(exponent: int) -> list[int]:
    result = [0] * (exponent + 1)
    result[0] = 1
    result[exponent] = -1
    return result


def shifted_q(shift: int, length: int) -> list[int]:
    result = [1]
    for index in range(1, length + 1):
        result = poly_multiply(result, binomial_factor(shift + index))
    return result


def shifted_t(shift: int, length: int) -> list[int]:
    result = [1]
    for index in range(1, length + 1):
        factor = binomial_factor(shift + index)
        result = poly_multiply(result, poly_power(factor, length + 1 - index))
    return result


def reachable_sums(weights: list[int]) -> set[int]:
    sums = {0}
    for weight in weights:
        sums |= {value + weight for value in sums}
    return sums


def balanced_tree_counts(length: int) -> tuple[int, int, int]:
    if length == 1:
        return 1, 0, 0
    left_length = length // 2
    right_length = length - left_length
    left_leaves, left_internal, left_power_bits = balanced_tree_counts(left_length)
    right_leaves, right_internal, right_power_bits = balanced_tree_counts(right_length)
    return (
        left_leaves + right_leaves,
        left_internal + right_internal + 1,
        left_power_bits + right_power_bits + right_length.bit_length(),
    )


def totients(limit: int) -> list[int]:
    values = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if values[prime] == prime:
            for multiple in range(prime, limit + 1, prime):
                values[multiple] -= values[multiple] // prime
    if limit >= 1:
        values[1] = 1
    return values


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0 and value:
        value //= prime
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    example_n = 875
    example_a = 631
    example_m = 3
    example_length = example_m - 1
    example_p = p_value(example_a, example_length)
    example_t = t_value(example_a, example_length)
    example_gcd_p = math.gcd(example_p, example_n)
    example_gcd_t = math.gcd(example_t, example_n)
    assert example_gcd_p == 175
    assert example_gcd_t == 875
    assert example_gcd_t % example_gcd_p == 0

    primes = [value for value in range(2, 48) if is_prime(value)]
    prime_zero_checks = 0
    for prime in primes:
        for length in range(1, 11):
            for base in range(prime):
                assert (modular_p_value(base, length, prime) == 0) == (
                    modular_t_value(base, length, prime) == 0
                )
                prime_zero_checks += 1

    gcd_divisibility_checks = 0
    for modulus in range(2, 301):
        for base in range(-10, 21):
            for length in range(1, 7):
                gcd_p = math.gcd(p_value(base, length), modulus)
                gcd_t = math.gcd(t_value(base, length), modulus)
                assert gcd_t % gcd_p == 0
                gcd_divisibility_checks += 1

    order_witnesses = [prime_field_order_witness(order) for order in range(1, 41)]

    lcm_exponent = math.lcm(*range(1, 5))
    lcm_prime = 13
    lcm_base = 2
    lcm_order = multiplicative_order(lcm_base, lcm_prime)
    lcm_factor = (1 - pow(lcm_base, lcm_exponent, lcm_prime)) % lcm_prime
    lcm_true_q = modular_p_value(lcm_base, 4, lcm_prime)
    lcm_true_t = modular_t_value(lcm_base, 4, lcm_prime)
    assert lcm_exponent == 12
    assert lcm_order == 12
    assert lcm_factor == 0
    assert lcm_true_q == 3
    assert lcm_true_t == 7

    addition_checks = 0
    for shift in range(4):
        for left_length in range(1, 6):
            for right_length in range(1, 6):
                total_length = left_length + right_length
                left_q = shifted_q(shift, left_length)
                right_q = shifted_q(shift + left_length, right_length)
                assert shifted_q(shift, total_length) == poly_multiply(left_q, right_q)
                expected_t = poly_multiply(
                    poly_multiply(shifted_t(shift, left_length), poly_power(left_q, right_length)),
                    shifted_t(shift + left_length, right_length),
                )
                assert shifted_t(shift, total_length) == expected_t
                addition_checks += 2

    support_records = []
    for length in range(1, 21):
        q_degree = length * (length + 1) // 2
        t_degree = length * (length + 1) * (length + 2) // 6
        q_sums = reachable_sums(list(range(1, length + 1)))
        t_weights = [
            exponent
            for exponent in range(1, length + 1)
            for _ in range(length + 1 - exponent)
        ]
        t_sums = reachable_sums(t_weights)
        assert q_sums == set(range(q_degree + 1))
        assert t_sums == set(range(t_degree + 1))
        support_records.append(
            {
                "length": length,
                "formal_q_support_size": len(q_sums),
                "formal_t_support_size": len(t_sums),
            }
        )

    specialized_q3 = shifted_q(0, 3)
    specialized_t2 = shifted_t(0, 2)
    assert specialized_q3[3] == 0
    assert specialized_t2[2] == 0

    floor_checks = 0
    minimum_floor_slack = None
    tight_floor_examples = []
    for bound in range(1, 2001):
        root = math.isqrt(bound)
        quotients = {bound // divisor for divisor in range(1, bound + 1)}
        lower_bound = 2 * root - 1
        slack = len(quotients) - lower_bound
        assert slack >= 0
        if minimum_floor_slack is None or slack < minimum_floor_slack:
            minimum_floor_slack = slack
            tight_floor_examples = [bound]
        elif slack == minimum_floor_slack and len(tight_floor_examples) < 20:
            tight_floor_examples.append(bound)
        floor_checks += 1

    phi_limit = 5000
    phi_values = totients(phi_limit)
    phi_prefix = 0
    degree_records = []
    for bound in range(1, phi_limit + 1):
        phi_prefix += phi_values[bound]
        assert phi_values[bound] * (1 + math.log2(bound)) + 1e-12 >= bound
        assert phi_prefix * 4 * (1 + math.log2(bound)) + 1e-12 >= bound * bound
        if bound in {1, 2, 4, 10, 100, 1000, 5000}:
            degree_records.append(
                {
                    "bound": bound,
                    "sum_phi": phi_prefix,
                    "requested_lower_bound": str(bound * bound / (4 * (1 + math.log2(bound)))),
                }
            )

    tree_records = []
    for length in [1, 2, 3, 4, 8, 16, 100, 1024]:
        leaves, internal, power_bits = balanced_tree_counts(length)
        assert leaves == length
        assert internal == length - 1
        tree_records.append(
            {
                "length": length,
                "leaves": leaves,
                "internal_nodes": internal,
                "sum_right_exponent_bit_lengths": power_bits,
            }
        )

    cyclotomic_bound = 10
    q_cyclotomic_weights = {
        str(order): cyclotomic_bound // order for order in range(1, cyclotomic_bound + 1)
    }
    t_cyclotomic_weights = {}
    for order in range(1, cyclotomic_bound + 1):
        quotient = cyclotomic_bound // order
        t_cyclotomic_weights[str(order)] = (
            quotient * (cyclotomic_bound + 1)
            - order * quotient * (quotient + 1) // 2
        )

    source = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "source": str(source),
        "source_sha256": sha256(source),
        "gcd_counterexample": {
            "N": example_n,
            "a": example_a,
            "m": example_m,
            "P": example_p,
            "S": example_t,
            "gcd_P_N": example_gcd_p,
            "gcd_S_N": example_gcd_t,
            "valuations": {
                "P_at_5": valuation(example_p, 5),
                "P_at_7": valuation(example_p, 7),
                "S_at_5": valuation(example_t, 5),
                "S_at_7": valuation(example_t, 7),
            },
        },
        "prime_zero_set_checks": prime_zero_checks,
        "gcd_divisibility_checks": gcd_divisibility_checks,
        "prime_field_order_witnesses_through_40": order_witnesses,
        "one_lcm_false_positive": {
            "M": 4,
            "prime": lcm_prime,
            "a": lcm_base,
            "order": lcm_order,
            "lcm_1_through_M": lcm_exponent,
            "one_lcm_factor": lcm_factor,
            "Q_M": lcm_true_q,
            "T_M": lcm_true_t,
        },
        "shifted_addition_identity_checks": addition_checks,
        "formal_support_records": support_records,
        "specialized_cancellation_examples": {
            "Q_3_coefficients_low_to_high": specialized_q3,
            "T_2_coefficients_low_to_high": specialized_t2,
        },
        "floor_quotient_checks": floor_checks,
        "minimum_floor_bound_slack": minimum_floor_slack,
        "first_tight_floor_examples": tight_floor_examples,
        "degree_bound_records": degree_records,
        "balanced_evaluator_tree_records": tree_records,
        "cyclotomic_weights_at_M_10": {
            "Q": q_cyclotomic_weights,
            "T": t_cyclotomic_weights,
        },
    }
    Path(args.output).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
