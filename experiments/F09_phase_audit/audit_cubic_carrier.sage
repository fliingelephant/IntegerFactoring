#!/usr/bin/env sage
"""Independent hostile audit of the exact F09 cubic certificate.

This script does not import the discovery source.  It exhaustively computes
the two local order-three character exponents, their fibers, the roots of
Phi_3 modulo 91, all pairwise root-difference gcds, and the product of the
two conjugate cubic residue symbols above each split rational prime.
"""

import json
import sys


ell = 3
p = 7
q = 13
N = p * q
generators = {p: 3, q: 2}


def exponent_mod_ell(a, prime):
    generator = generators[prime]
    table = {pow(generator, e, prime): e % ell for e in range(prime - 1)}
    return table[a % prime]


phase_counts = {(x, y): 0 for x in range(ell) for y in range(ell)}
sum_counts = {s: 0 for s in range(ell)}
for a in range(1, N):
    if gcd(a, N) != 1:
        continue
    phase = (exponent_mod_ell(a, p), exponent_mod_ell(a, q))
    phase_counts[phase] += 1
    sum_counts[sum(phase) % ell] += 1

collision = {}
for a in (15, 18, 16):
    collision[a] = [exponent_mod_ell(a, p), exponent_mod_ell(a, q)]
ratio = (15 * inverse_mod(18, N)) % N

roots = [rho for rho in range(N) if (rho^2 + rho + 1) % N == 0]
root_records = [
    {
        "rho": int(rho),
        "components": [int(rho % p), int(rho % q)],
        "conjugate": int((-1 - rho) % N),
    }
    for rho in roots
]
root_gcds = [
    {
        "pair": [int(rho), int(sigma)],
        "gcd": int(gcd(rho - sigma, N)),
    }
    for i, rho in enumerate(roots)
    for sigma in roots[i + 1 :]
]


def residue_symbol_exponent(a, prime, omega):
    value = pow(a, (prime - 1) // ell, prime)
    for e in range(ell):
        if pow(omega, e, prime) == value:
            return e
    raise AssertionError("Euler value is not an ell-th root of unity")


galois_product_checks = {}
for prime in (p, q):
    omegas = [x for x in range(1, prime) if (x^2 + x + 1) % prime == 0]
    exponent_sums = {
        a: sum(residue_symbol_exponent(a, prime, omega) for omega in omegas) % ell
        for a in range(1, prime)
    }
    galois_product_checks[str(prime)] = {
        "omegas": [int(x) for x in omegas],
        "all_products_trivial": all(e == 0 for e in exponent_sums.values()),
        "exponent_sums": {str(a): int(e) for a, e in exponent_sums.items()},
    }

assert ratio == 16
assert collision == {15: [0, 1], 18: [1, 0], 16: [2, 1]}
assert set(phase_counts.values()) == {8}
assert sum_counts == {0: 24, 1: 24, 2: 24}
assert len(roots) == 4
assert sorted(tuple(record["components"]) for record in root_records) == [
    (2, 3),
    (2, 9),
    (4, 3),
    (4, 9),
]
assert sorted(record["gcd"] for record in root_gcds) == [1, 1, 7, 7, 13, 13]
assert all(record["all_products_trivial"] for record in galois_product_checks.values())

result = {
    "family": "F09_phase_audit",
    "parameters": {"ell": ell, "p": p, "q": q, "N": N},
    "phase_pair_counts": {str(key): value for key, value in phase_counts.items()},
    "diagonal_sum_counts": {str(key): value for key, value in sum_counts.items()},
    "collision": {str(key): value for key, value in collision.items()},
    "ratio_15_over_18": int(ratio),
    "roots": root_records,
    "root_difference_gcds": root_gcds,
    "galois_product_checks": galois_product_checks,
}

with open(sys.argv[1], "w") as handle:
    json.dump(result, handle, indent=2, sort_keys=True, default=int)
