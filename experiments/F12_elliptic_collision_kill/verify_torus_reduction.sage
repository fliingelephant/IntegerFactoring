#!/usr/bin/env sage
"""Verify the multiplicative-torus collision formula and exact probabilities.

Approach-family ID: F12_elliptic_collision_kill.
"""

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"
INSTANCES = [(101, 103), (11, 101)]


def torus_superfactorial(base, length, modulus):
    value = 1
    power = base % modulus
    for difference in range(1, length):
        value = value * pow(1 - power, length - difference, modulus) % modulus
        power = power * base % modulus
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    polynomial_ring = PolynomialRing(ZZ, "z")
    z = polynomial_ring.gen()
    symbolic_checks = []
    for length in range(2, 11):
        orbit = [z**index for index in range(length)]
        direct = prod(
            orbit[left] - orbit[right]
            for left in range(length)
            for right in range(left + 1, length)
        )
        formula = z**binomial(length, 3) * prod(
            (1 - z**difference)**(length - difference)
            for difference in range(1, length)
        )
        assert direct == formula
        symbolic_checks.append(
            {
                "m": length,
                "monomial_exponent": int(binomial(length, 3)),
                "polynomial_degree": int(formula.degree()),
            }
        )

    instance_records = []
    for p, q in INSTANCES:
        N = p * q
        length = math.isqrt(N)
        assert p < q and length * length < N
        assert p - 1 <= length - 1
        assert q - 1 >= length
        success_count_q = 0
        primitive_count_q = 0
        for residue in range(1, q):
            order = int(Mod(residue, q).multiplicative_order())
            collision_value = torus_superfactorial(residue, length, q)
            assert (collision_value != 0) == (order >= length)
            success_count_q += order >= length
            primitive_count_q += order == q - 1
        assert primitive_count_q == euler_phi(q - 1)

        global_unit_count = 0
        global_success_count = 0
        for base in range(1, N):
            if gcd(base, N) != 1:
                continue
            global_unit_count += 1
            collision_value = torus_superfactorial(base, length, N)
            collision_mod_p = collision_value % p
            collision_mod_q = collision_value % q
            assert collision_mod_p == 0
            expected_success = Mod(base, q).multiplicative_order() >= length
            assert (collision_mod_q != 0) == expected_success
            divisor = gcd(collision_value, N)
            assert (divisor == p) == expected_success
            global_success_count += expected_success
        assert global_unit_count == (p - 1) * (q - 1)
        assert global_success_count == (p - 1) * success_count_q

        direct_check_bases = []
        for base in range(2, min(N, 8)):
            if gcd(base, N) != 1:
                continue
            orbit = [pow(base, index, N) for index in range(length)]
            direct = 1
            for left in range(length):
                for right in range(left + 1, length):
                    direct = direct * (orbit[left] - orbit[right]) % N
            formula = (
                pow(base, int(binomial(length, 3)), N)
                * torus_superfactorial(base, length, N)
            ) % N
            assert direct == formula
            direct_check_bases.append(base)

        success_probability = Fraction(int(success_count_q), int(q - 1))
        primitive_probability = Fraction(int(primitive_count_q), int(q - 1))
        instance_records.append(
            {
                "N": N,
                "p": p,
                "q": q,
                "m_floor_sqrt_N": length,
                "p_minus_1_le_m_minus_1": True,
                "q_minus_1_ge_m": True,
                "unit_count": global_unit_count,
                "successful_units": global_success_count,
                "exact_conditional_success_probability": str(success_probability),
                "exact_conditional_success_numerator": success_probability.numerator,
                "exact_conditional_success_denominator": success_probability.denominator,
                "primitive_root_probability": str(primitive_probability),
                "primitive_root_count": primitive_count_q,
                "primitive_probability_ge_inverse_log_bound": (
                    float(primitive_probability) >= 1 / (1 + math.log2(q - 1))
                ),
                "direct_formula_check_bases": direct_check_bases,
            }
        )

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "purpose": "torus q-superfactorial conditional reduction",
        "identity": "prod_{0<=i<j<m}(a^i-a^j)=a^binomial(m,3)*prod_{d=1}^{m-1}(1-a^d)^(m-d)",
        "symbolic_checks": symbolic_checks,
        "instances": instance_records,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
