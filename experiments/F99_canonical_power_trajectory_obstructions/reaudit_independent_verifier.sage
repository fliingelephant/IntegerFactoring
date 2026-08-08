#!/usr/bin/env sage

import json
from math import gcd


# Recompute the complete fixed witness without importing either prior verifier.
N = 64_570_081
p = 1_871
q = 34_511
m = 17
n = N.bit_length()
limit = n**2

assert N == p * q == (3**m - 1) // 2
assert is_prime(p) and is_prime(q)
assert list(factor(p - 1)) == [(2, 1), (5, 1), (11, 1), (17, 1)]
assert list(factor(q - 1)) == [(2, 1), (5, 1), (7, 1), (17, 1), (29, 1)]

lucas_residues = {}
for prime, base, divisors in (
    (p, 14, (2, 5, 11, 17)),
    (q, 7, (2, 5, 7, 17, 29)),
):
    assert power_mod(base, prime - 1, prime) == 1
    residues = []
    for divisor in divisors:
        residue = int(power_mod(base, (prime - 1) // divisor, prime))
        assert gcd(residue - 1, prime) == 1
        residues.append(residue)
    lucas_residues[str(prime)] = residues

assert (n, limit) == (26, 676)
assert min(p, q) > limit
assert all(gcd(value, N) == 1 for value in range(2, limit + 1))

shared = gcd(p - 1, q - 1)
left = (p - 1) // shared
right = (q - 1) // shared
assert (shared, left, right) == (170, 11, 203)
assert gcd(left * right, N - 1) == 1

common_product = 3**m
assert common_product == 1 + 2 * N
assert [multiplicative_order(Mod(3, modulus)) for modulus in (p, q, N)] == [m, m, m]

presentations = {}
for exponent in range(limit + 1):
    c = int(power_mod(3, exponent, N))
    w = int(inverse_mod(c, N))
    product = c * w
    if c == 1:
        assert product == 1
    else:
        assert product == common_product
        assert gcd(c - w, N) == gcd(c + w, N) == 1
    presentations[c] = product

assert len(presentations) == 17
assert set(presentations.values()) == {1, common_product}
assert gcd(common_product - 1, N) == N
assert gcd(common_product + 1, N) == 1


# Instantiate the private-row construction at a parameter not used by the
# prior audit. This checks all CRT and valuation identities on exact integers.
T = 5
Ks = [2**e - 1 for e in range(1, T + 1)]
private_primes = []
for e in range(1, T + 1):
    lower = 2 ** (T + e)
    prime = int(next_prime(lower))
    assert lower < prime < 2 * lower
    private_primes.append(prime)
assert len(set(private_primes)) == T

M = 2**T * prod(prime**2 for prime in private_primes)
moduli = [2**T] + [prime**2 for prime in private_primes]
targets = [1] + [
    int((prime - 1) * inverse_mod(K, prime**2) % (prime**2))
    for K, prime in zip(Ks, private_primes)
]
a = int(CRT_list(targets, moduli))
assert 0 <= a < M
assert gcd(a, M) == 1
assert a != 1
assert gcd(M, 7) == 1

alpha = next(value for value in (1 + step * M for step in range(1, 7)) if gcd(value, 7 * M) == 1)
beta = next(value for value in (a + step * M for step in range(1, 7)) if gcd(value, 7 * M) == 1)
assert M < alpha < 7 * M
assert M < beta < 7 * M
assert alpha != beta

modulus = 7 * M
prime_left = next(alpha + step * modulus for step in range(20_000) if is_prime(alpha + step * modulus))
prime_right = next(beta + step * modulus for step in range(20_000) if is_prime(beta + step * modulus))
assert prime_left != prime_right
assert prime_left > M and prime_right > M

sample_N = int(prime_left * prime_right)
assert sample_N % M == a
products = [1 + K * sample_N for K in Ks]
private_rows = []
for index, (e, K, prime) in enumerate(zip(range(1, T + 1), Ks, private_primes)):
    c = 2**e
    assert products[index] % c == 0
    w = products[index] // c
    assert 0 < w < sample_N
    assert int(inverse_mod(c, sample_N)) == w
    assert valuation(products[index], prime) == 1
    assert all(products[other] % prime != 0 for other in range(T) if other != index)
    private_rows.append([1 if products[column] % prime == 0 else 0 for column in range(T)])

assert Matrix(GF(2), private_rows).rank() == T

print(json.dumps({
    "status": "PASS",
    "fixed_witness": {
        "N": N,
        "factors": [p, q],
        "n": n,
        "bound": limit,
        "lucas_residues": lucas_residues,
        "stable_parameters": [shared, left, right],
        "unique_residues": len(presentations),
        "nontrivial_relation_value": common_product,
        "direct_sign_screens": "all gcd 1",
        "duplicate_root": "global +1",
    },
    "private_row_sample": {
        "T": T,
        "q_e": private_primes,
        "M_bits": M.bit_length(),
        "N_bits": sample_N.bit_length(),
        "private_row_rank": T,
    },
}, indent=2, sort_keys=True, default=int))
