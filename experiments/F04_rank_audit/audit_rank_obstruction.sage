#!/usr/bin/env sage
"""Independent hostile audit of the finite F04 AKS-rank witness.

This source does not import or call any F04_rankkill source.  It checks the
AKS parameters, the two Frobenius reductions, all local shifts, and the
degree-23 obstruction directly in Sage.
"""

import argparse
import json
import math
import time


P = 271
Q = 293
N = P * Q
R = 269


def trial_prime(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def manual_order(a, m):
    if math.gcd(a, m) != 1:
        return None
    x = 1
    for k in range(1, int(euler_phi(m)) + 1):
        x = x * (a % m) % m
        if x == 1:
            return k
    raise AssertionError("order did not divide phi(m)")


def quotient_power(base, exponent):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result *= base
        exponent >>= 1
        if exponent:
            base *= base
    return result


def local_scan(characteristic, cofactor):
    poly = PolynomialRing(GF(characteristic), "x")
    x = poly.gen()
    modulus = x**R - 1
    quotient = poly.quotient(modulus, "z")
    z = quotient.gen()

    factors = sorted(
        int(factor.degree())
        for factor, multiplicity in modulus.factor()
        for _ in range(int(multiplicity))
    )
    all_degrees = []
    positive = []
    for a in range(characteristic):
        aa = quotient(a)
        h = quotient_power(z + aa, cofactor) - quotient_power(z, cofactor) - aa
        degree = int(gcd(h.lift(), modulus).degree())
        all_degrees.append(degree)
        if degree:
            positive.append([a, degree])

    # Directly check the exponent-N global error and its Frobenius-substituted
    # cofactor form at boundary/interior shifts, independently of the scan.
    frobenius_checks = []
    for a in [1, 2, 133, 266, 267]:
        aa = quotient(a)
        direct = quotient_power(z + aa, N) - quotient_power(z, N) - aa
        h = quotient_power(z + aa, cofactor) - quotient_power(z, cofactor) - aa
        substituted = quotient(h.lift()(quotient_power(z, characteristic)))
        direct_degree = int(gcd(direct.lift(), modulus).degree())
        h_degree = int(gcd(h.lift(), modulus).degree())
        assert direct == substituted
        assert direct_degree == h_degree == 0
        frobenius_checks.append(
            {
                "a": a,
                "direct_equals_substituted_h": True,
                "direct_gcd_degree": direct_degree,
                "h_gcd_degree": h_degree,
            }
        )

    distribution = {
        str(degree): all_degrees.count(degree)
        for degree in sorted(set(all_degrees))
    }
    return {
        "characteristic": characteristic,
        "cofactor": cofactor,
        "order_characteristic_mod_r": manual_order(characteristic, R),
        "factor_degrees": factors,
        "positive_local_residues": positive,
        "degree_distribution": distribution,
        "standard_and_ceiling_degrees": all_degrees[1:268],
        "frobenius_checks": frobenius_checks,
    }


def obstruction_checks(characteristic):
    poly = PolynomialRing(GF(characteristic), "y")
    y = poly.gen()
    modulus = y**R - 1
    degrees = set()
    y23_coefficients_correct = True
    nontrivial_common_degree_positive = []
    for a in range(1, characteristic):
        aa = poly(a)
        g = (y**2 + aa) * (y + aa) ** 22 - y**24 - aa
        degrees.add(int(g.degree()))
        y23_coefficients_correct &= g[23] == 22 * aa
        common = gcd(g, modulus)
        if common.degree() and common != y - 1:
            nontrivial_common_degree_positive.append(
                [a, int(common.degree()), str(common)]
            )
    return {
        "characteristic": characteristic,
        "degrees_for_nonzero_a": sorted(degrees),
        "all_y23_coefficients_equal_22a": bool(y23_coefficients_correct),
        "unexpected_common_factors": nontrivial_common_degree_positive,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    assert P * Q == N
    assert trial_prime(P) and trial_prime(Q)
    assert N**4 > 2**65
    assert N**61 < 2**993
    assert 264 * 16 < 65**2  # 264 < (65/4)^2
    assert 993**2 < 265 * 61**2
    assert all(math.gcd(a, N) == 1 for a in range(2, R + 1))

    orders_through_r = {
        s: manual_order(N, s)
        for s in range(2, R + 1)
        if math.gcd(N, s) == 1
    }
    # The exact logarithmic brackets show every order through 268 is below
    # (log_2 N)^2, while order 268 at r=269 is above it.
    assert max(orders_through_r[s] for s in orders_through_r if s <= 265) <= 264
    assert [int(euler_phi(s)) for s in [266, 267, 268]] == [108, 176, 132]
    assert orders_through_r[R] == 268
    assert pow(N % R, 134, R) == R - 1
    assert pow(N % R, 4, R) == 239

    assert 268 * 65**2 > 16 * 266**2
    assert 268 * 265 < 267**2
    high_precision_shift = RealField(200)(268).sqrt() * RealField(200)(N).log(2)
    assert 266 < high_precision_shift < 267

    assert manual_order(P, R) == 268
    assert manual_order(Q, R) == 67
    assert pow(2, 134, R) == R - 1 and pow(2, 4, R) != 1
    chain_24 = {int(e): int(pow(24, e, R)) for e in [2, 4, 8, 16, 32, 64, 67]}
    assert chain_24 == {2: 38, 4: 99, 8: 117, 16: 239, 32: 93, 64: 41, 67: 1}

    scan_p = local_scan(P, Q)
    scan_q = local_scan(Q, P)
    assert scan_p["factor_degrees"] == [1, 268]
    assert scan_q["factor_degrees"] == [1, 67, 67, 67, 67]
    assert scan_p["positive_local_residues"] == [[0, 269], [269, 1], [270, 1]]
    assert scan_q["positive_local_residues"] == [[0, 269], [291, 1], [292, 1]]
    assert set(scan_p["standard_and_ceiling_degrees"]) == {0}
    assert set(scan_q["standard_and_ceiling_degrees"]) == {0}

    obstruction_p = obstruction_checks(P)
    obstruction_q = obstruction_checks(Q)
    assert obstruction_p["degrees_for_nonzero_a"] == [23]
    assert obstruction_q["degrees_for_nonzero_a"] == [23]
    assert obstruction_p["all_y23_coefficients_equal_22a"]
    assert obstruction_q["all_y23_coefficients_equal_22a"]
    assert not obstruction_p["unexpected_common_factors"]
    assert not obstruction_q["unexpected_common_factors"]

    equal_rank_pairs = 268 * 290 + 2 * 2 + 1
    mismatch_pairs = N - equal_rank_pairs
    assert mismatch_pairs == 1678

    result = {
        "family": "F04_rank_audit",
        "status": "passed",
        "N": N,
        "factors": [P, Q],
        "factors_prime_by_trial_division": True,
        "not_perfect_power_reason": "prime factor exponents are both one",
        "preliminary_gcd_scan_survives": True,
        "exact_log_brackets": ["N^4 > 2^65", "N^61 < 2^993"],
        "r": R,
        "order_N_mod_r": orders_through_r[R],
        "phi_266_267_268": [108, 176, 132],
        "shift_expression_200_bit": str(high_precision_shift),
        "standard_floor_bound": 266,
        "chain_24_mod_269": chain_24,
        "scan_mod_271": scan_p,
        "scan_mod_293": scan_q,
        "obstruction_mod_271": obstruction_p,
        "obstruction_mod_293": obstruction_q,
        "uniform_crt_mismatch_count": mismatch_pairs,
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, default=int)
        handle.write("\n")
    print("PASS: independent AKS rank-obstruction audit", flush=True)


main()
