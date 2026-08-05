#!/usr/bin/env sage
"""F09: enumerate cubic-character fibers for N=7*13.

The local characters are defined by discrete-log exponents modulo 3 with
primitive roots 3 (mod 7) and 2 (mod 13).  The script records one rational
unit for each local phase pair, the fibers of the product character, and the
rank of any family of symmetric scalar characters on (Z/3Z)^2.
"""

import json
import sys


N = 7 * 13
p = 7
q = 13
ell = 3
g_p = 3
g_q = 2


def character_exponent(a, prime, primitive_root):
    value = a % prime
    for exponent in range(prime - 1):
        if power_mod(primitive_root, exponent, prime) == value:
            return exponent % ell
    raise RuntimeError("unit discrete logarithm not found")


representatives = {}
fibers = {str(s): [] for s in range(ell)}
for a in range(1, N):
    if gcd(a, N) != 1:
        continue
    pair = (
        character_exponent(a, p, g_p),
        character_exponent(a, q, g_q),
    )
    representatives.setdefault(str(pair), a)
    fibers[str((pair[0] + pair[1]) % ell)].append(
        {"a": a, "local_pair": list(pair)}
    )

# A homomorphism L(x,y)=alpha*x+beta*y is invariant under swapping p and q
# iff alpha=beta.  Collect every such row and compute their span rank.
symmetric_rows = [[k, k] for k in range(ell)]
matrix_rank = Matrix(GF(ell), symmetric_rows).rank()

cyclotomic_roots = [
    x for x in range(N) if (x * x + x + 1) % N == 0
]
root_data = [
    {
        "root": x,
        "crt_pair": [x % p, x % q],
        "global_conjugate": (-1 - x) % N,
    }
    for x in cyclotomic_roots
]
root_pair_gcds = [
    {"roots": [x, y], "gcd_difference_with_N": int(gcd(x - y, N))}
    for i, x in enumerate(cyclotomic_roots)
    for y in cyclotomic_roots[i + 1 :]
]

result = {
    "family": "F09",
    "N": int(N),
    "factors": [int(p), int(q)],
    "ell": int(ell),
    "primitive_roots": {str(p): g_p, str(q): g_q},
    "representative_for_each_local_pair": representatives,
    "fiber_sizes_by_global_sum": {key: len(value) for key, value in fibers.items()},
    "first_three_per_fiber": {key: value[:3] for key, value in fibers.items()},
    "symmetric_homorphism_rows": symmetric_rows,
    "symmetric_span_rank": int(matrix_rank),
    "cyclotomic_roots_mod_N": root_data,
    "pairwise_root_difference_gcds": root_pair_gcds,
    "explicit_collision": {
        "a": representatives[str((0, 1))],
        "b": representatives[str((1, 0))],
        "local_pairs": [[0, 1], [1, 0]],
        "same_global_sum": 1,
    },
}

with open(sys.argv[1], "w") as output_file:
    json.dump(result, output_file, indent=2, sort_keys=True, default=int)
