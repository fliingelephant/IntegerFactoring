#!/usr/bin/env python3

import json
import math


def is_prime_by_trial_division(value: int) -> bool:
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


m = 17
left_factor = 1_871
right_factor = 34_511
N = 64_570_081
n = N.bit_length()
bound = n * n
relation_value = 3**m

assert is_prime_by_trial_division(left_factor)
assert is_prime_by_trial_division(right_factor)
assert N == left_factor * right_factor == (3**m - 1) // 2
assert relation_value == 1 + 2 * N
assert min(left_factor, right_factor) > bound

g = math.gcd(left_factor - 1, right_factor - 1)
A = (left_factor - 1) // g
B = (right_factor - 1) // g
assert (g, A, B) == (170, 11, 203)
assert math.gcd(A * B, N - 1) == 1

lucas_checks = {}
for prime, base, prime_divisors in (
    (left_factor, 14, (2, 5, 11, 17)),
    (right_factor, 7, (2, 5, 7, 17, 29)),
):
    assert pow(base, prime - 1, prime) == 1
    residues = [pow(base, (prime - 1) // divisor, prime) for divisor in prime_divisors]
    assert all(math.gcd(residue - 1, prime) == 1 for residue in residues)
    lucas_checks[str(prime)] = residues

trajectory = []
for r in range(1, m):
    c = pow(3, r)
    w = pow(c, -1, N)
    assert w == pow(3, m - r)
    assert c * w == relation_value
    assert math.gcd(c, N) == math.gcd(w, N) == 1
    assert math.gcd(c - w, N) == math.gcd(c + w, N) == 1
    trajectory.append((r, c, w))

unique_residues = {pow(3, exponent, N) for exponent in range(bound + 1)}
assert len(unique_residues) == m

print(
    json.dumps(
        {
            "N": N,
            "factorization": [left_factor, right_factor],
            "n": n,
            "n_squared": bound,
            "stable_parameters": {"g": g, "A": A, "B": B},
            "lucas_residues": lucas_checks,
            "relation_value": relation_value,
            "nontrivial_trajectory_residues": len(trajectory),
            "unique_residues_through_n_squared": len(unique_residues),
            "all_direct_sign_screens": "gcd 1",
            "all_duplicate_dependency_roots": "global +1",
        },
        indent=2,
        sort_keys=True,
    )
)
