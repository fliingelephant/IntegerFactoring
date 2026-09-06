"""Finite counterexample search for the F151 V2 hostile re-audit.

This script is an audit aid, not evidence for the general theorems.
It checks the exact finite ranges printed in its final summary.
"""

from itertools import combinations
from math import gcd


def prime_divisors(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def order(a, modulus):
    x = 1
    for e in range(1, modulus + 1):
        x = x * a % modulus
        if x == 1:
            return e
    raise AssertionError((a, modulus))


def character(a, p):
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def primes_through(limit):
    return [p for p in range(2, limit + 1) if prime_divisors(p) == [p]]


component_cases = 0
bank_cases = 0
for n_modulus in range(6, 351):
    factors = prime_divisors(n_modulus)
    for bound in range(4, min(n_modulus - 2, 18) + 1):
        for alpha in range(1, n_modulus):
            if gcd(alpha, n_modulus) != 1 or order(alpha, n_modulus) <= bound:
                continue

            component_cases += 1
            short_component = any(order(alpha % r, r) <= bound for r in factors)
            scans = [gcd(pow(alpha, e, n_modulus) - 1, n_modulus) for e in range(1, bound + 1)]
            proper_scan = any(1 < value < n_modulus for value in scans)
            assert short_component == proper_scan, (n_modulus, bound, alpha, factors, scans)

            if proper_scan:
                continue

            bank_cases += 1
            endpoints = {
                e: pow(alpha, e, n_modulus)
                for e in range(1, bound // 4 + 1)
            }
            for e, f in combinations(endpoints, 2):
                c_e = endpoints[e]
                c_f = endpoints[f]
                assert gcd(c_e - c_f, n_modulus) == 1
                assert gcd(c_e + c_f, n_modulus) == 1
                assert gcd(c_e * c_f - 1, n_modulus) == 1
                assert gcd(c_e * c_f + 1, n_modulus) == 1
            for c_e in endpoints.values():
                inverse = pow(c_e, -1, n_modulus)
                assert gcd(c_e - inverse, n_modulus) == 1
                assert gcd(c_e + inverse, n_modulus) == 1


torus_cases = 0
odd_primes = primes_through(43)[1:]
for p, q in combinations(odd_primes, 2):
    n_modulus = p * q
    if min(p, q) <= 5:
        continue

    representatives = {}
    for delta in range(1, n_modulus):
        if gcd(delta, n_modulus) != 1:
            continue
        signs = (character(delta, p), character(delta, q))
        if signs in ((1, -1), (-1, 1)) and signs not in representatives:
            representatives[signs] = delta
        if len(representatives) == 2:
            break
    assert len(representatives) == 2

    half = pow(2, -1, n_modulus)
    for alpha in range(1, n_modulus):
        if gcd(alpha, n_modulus) != 1:
            continue
        if order(alpha % p, p) <= 4 or order(alpha % q, q) <= 4:
            continue
        inverse = pow(alpha, -1, n_modulus)
        x = (alpha + inverse) * half % n_modulus
        for signs, delta in representatives.items():
            torus_cases += 1
            b = pow(delta, -1, n_modulus) * (x * x - 1) % n_modulus
            assert (character(b, p), character(b, q)) == signs
            assert (character(b, p) == 1) != (character(b, q) == 1)

            t_prev, t_now = 1, x
            for exponent in range(21):
                if exponent == 0:
                    chebyshev = t_prev
                elif exponent == 1:
                    chebyshev = t_now
                else:
                    t_prev, t_now = t_now, (2 * x * t_now - t_prev) % n_modulus
                    chebyshev = t_now
                rhs = (pow(alpha, exponent, n_modulus) + pow(inverse, exponent, n_modulus)) * half % n_modulus
                assert chebyshev == rhs


assert order(3, 77) == 30
assert order(3, 7) == 6
assert order(3, 11) == 5
assert all(gcd(pow(3, e) - 1, 77) == 1 for e in range(1, 5))
assert gcd(pow(3, 5) - 1, 77) == 11

print(
    {
        "component_upgrade_cases": component_cases,
        "surviving_short_bank_cases": bank_cases,
        "torus_orientation_cases": torus_cases,
        "N_range": [6, 350],
        "B_range": [4, 18],
        "torus_prime_limit": 43,
        "chebyshev_exponent_range": [0, 20],
        "status": "PASS",
    }
)
