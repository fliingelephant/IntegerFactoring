#!/usr/bin/env sage

import json
from math import gcd


# Fixed witness: recompute every arithmetic claim independently.
m = 17
N = 64_570_081
p = 1_871
q = 34_511
n = N.bit_length()
bound = n * n

assert N == (3**m - 1) // 2 == p * q
assert bool(is_prime(p)) and bool(is_prime(q))
assert list(factor(p - 1)) == [(2, 1), (5, 1), (11, 1), (17, 1)]
assert list(factor(q - 1)) == [(2, 1), (5, 1), (7, 1), (17, 1), (29, 1)]

lucas = {}
for prime, base in ((p, 14), (q, 7)):
    divisors = [Integer(r) for r, _ in factor(prime - 1)]
    assert power_mod(base, prime - 1, prime) == 1
    values = []
    for ell in divisors:
        residue = int(power_mod(base, (prime - 1) // ell, prime))
        assert gcd(residue - 1, prime) == 1
        values.append(residue)
    lucas[str(prime)] = values

g = gcd(p - 1, q - 1)
A = (p - 1) // g
B = (q - 1) // g
assert (n, bound, g, A, B) == (26, 676, 170, 11, 203)
assert gcd(A, B) == 1 and gcd(A * B, N - 1) == 1
assert all(gcd(t, N) == 1 for t in range(2, bound + 1))

relation_value = 3**m
assert relation_value == 1 + 2 * N
assert multiplicative_order(Mod(3, p)) == m
assert multiplicative_order(Mod(3, q)) == m
assert multiplicative_order(Mod(3, N)) == m

trajectory = []
for r in range(1, m):
    c = 3**r
    w = 3 ** (m - r)
    assert 0 < c < N and 0 < w < N
    assert int(inverse_mod(c, N)) == w
    assert c * w == relation_value
    assert gcd(c, N) == gcd(w, N) == 1
    assert gcd(c - w, N) == gcd(c + w, N) == 1
    trajectory.append({"r": r, "c": c, "w": w})

residue_to_product = {}
for e in range(bound + 1):
    c = int(power_mod(3, e, N))
    w = int(inverse_mod(c, N))
    product = c * w
    if c == 1:
        assert product == 1
    else:
        assert product == relation_value
        assert gcd(c - w, N) == gcd(c + w, N) == 1
    residue_to_product[c] = product
assert len(residue_to_product) == m
assert sum(product != 1 for product in residue_to_product.values()) == m - 1

# Every added duplicate column differs from the retained seed by a two-copy
# dependency. Its exact positive root is the common relation value, hence +1.
for _ in range(m - 2):
    root = relation_value
    assert root % N == 1
    assert gcd(root - 1, N) == N and gcd(root + 1, N) == 1

# Independently instantiate the CRT private-row construction at T=4.
T = 4
Ks = [2**e - 1 for e in range(1, T + 1)]
qs = []
for e in range(1, T + 1):
    lower = 2 ** (T + e)
    qe = int(next_prime(lower))
    assert lower < qe < 2 * lower
    qs.append(qe)
assert len(set(qs)) == T

M = 2**T
for qe in qs:
    M *= qe**2

moduli = [2**T] + [qe**2 for qe in qs]
residues = [1] + [int(((qe - 1) * inverse_mod(Ke, qe**2)) % (qe**2))
                  for Ke, qe in zip(Ks, qs)]
a = int(CRT_list(residues, moduli))
assert 0 <= a < M and gcd(a, M) == 1 and a != 1

def lifted_class(base):
    for t in range(1, 7):
        value = base + t * M
        if gcd(value, 7 * M) == 1:
            assert M < value < 7 * M
            return value
    raise AssertionError("no reduced lift")


alpha = lifted_class(1)
beta = lifted_class(a)
assert alpha != beta
Q = 7 * M

def first_prime_in_class(residue):
    for k in range(10_000):
        value = residue + k * Q
        if is_prime(value):
            return int(value), k
    raise AssertionError("sample prime search exhausted")


sample_p, p_step = first_prime_in_class(alpha)
sample_q, q_step = first_prime_in_class(beta)
assert sample_p != sample_q and sample_p > M and sample_q > M
assert sample_p % M == 1 and sample_q % M == a
sample_N = sample_p * sample_q
assert sample_N % M == a

private_rows = []
for index, (e, Ke, qe) in enumerate(zip(range(1, T + 1), Ks, qs)):
    c = 2**e
    numerator = 1 + Ke * sample_N
    assert numerator % c == 0
    w = numerator // c
    assert 0 < w < sample_N and int(inverse_mod(c, sample_N)) == w
    products = [1 + Kj * sample_N for Kj in Ks]
    assert valuation(products[index], qe) == 1
    assert all(products[j] % qe != 0 for j in range(T) if j != index)
    private_rows.append({"e": e, "q": qe, "valuation": 1})

assert (sample_N.bit_length() >= 2 * M.bit_length() - 1)

print(json.dumps({
    "status": "PASS",
    "fixed_witness": {
        "N": N,
        "factors": [p, q],
        "lucas_residues": lucas,
        "n": n,
        "bound": bound,
        "stable": {"g": g, "A": A, "B": B},
        "order_mod_p_q_N": [m, m, m],
        "unique_residues_through_bound": len(residue_to_product),
        "nontrivial_exact_relation_values": sorted(set(
            product for product in residue_to_product.values() if product != 1
        )),
        "direct_screens": "all trivial",
    },
    "crt_sample": {
        "T": T,
        "q_e": qs,
        "M_bits": M.bit_length(),
        "prime_steps": [p_step, q_step],
        "factor_bits": [sample_p.bit_length(), sample_q.bit_length()],
        "N_bits": sample_N.bit_length(),
        "private_rows": private_rows,
    },
}, indent=2, sort_keys=True, default=int))
