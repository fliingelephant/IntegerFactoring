#!/usr/bin/env python3
"""Independent small-case check of the F123 determinant congruence."""

from itertools import permutations
import json
from math import gcd


def determinant(matrix: list[list[int]]) -> int:
    total = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = 1
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += -term if inversions & 1 else term
    return total


checked = 0
for N in range(3, 500, 2):
    for a in range(2, min(N, 30)):
        if gcd(a * (a * a - 1), N) != 1:
            continue

        rows: list[list[int]] = []
        carries: list[int] = []
        for j in range(1, 5):
            c = pow(a, j, N)
            w = pow(c, -1, N)
            kappa = (c * w - 1) // N
            rows.append([1, c, w, kappa])
            carries.append(kappa)

        det = determinant(rows)
        omega = (
            carries[3]
            - carries[0]
            + (1 + a + rows[0][2]) * (carries[1] - carries[2])
        )
        prefactor = (a - 1) ** 3 * (a + 1) * rows[0][2] ** 2

        assert (det - prefactor * omega) % N == 0
        assert gcd(det, N) == gcd(omega, N)
        checked += 1

assert checked == 3_571

certificate_N = 4_840_987
proper_hits: list[list[int]] = []
for a in range(2, 93):
    carries = []
    first_inverse = 0
    for j in range(1, 5):
        c = pow(a, j, certificate_N)
        w = pow(c, -1, certificate_N)
        if j == 1:
            first_inverse = w
        carries.append((c * w - 1) // certificate_N)
    omega = (
        carries[3]
        - carries[0]
        + (1 + a + first_inverse) * (carries[1] - carries[2])
    )
    divisor = gcd(abs(omega), certificate_N)
    if divisor not in (1, certificate_N):
        proper_hits.append([a, divisor])

assert proper_hits == [[68, 2_621]]
print(
    json.dumps(
        {
            "status": "pass",
            "checked_cases": checked,
            "certificate_seed_hits": proper_hits,
        },
        sort_keys=True,
    )
)
