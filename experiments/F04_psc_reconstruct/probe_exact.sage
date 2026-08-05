#!/usr/bin/env sage

import json
import sys
import time
from math import gcd


N = 79403
R = 269
A = 1


def cyclic_mul(left, right, modulus, length):
    out = [0] * length
    for i, x in enumerate(left):
        if x:
            for k, y in enumerate(right):
                if y:
                    out[(i + k) % length] = (out[(i + k) % length] + x * y) % modulus
    return out


def cyclic_pow_x_plus_a(exponent, a, modulus, length):
    result = [0] * length
    result[0] = 1
    base = [0] * length
    base[0] = a % modulus
    base[1] = 1
    power = exponent
    while power:
        if power & 1:
            result = cyclic_mul(result, base, modulus, length)
        power >>= 1
        if power:
            base = cyclic_mul(base, base, modulus, length)
    return result


def make_h():
    h = cyclic_pow_x_plus_a(N, A, N, R)
    h[N % R] = (h[N % R] - 1) % N
    h[0] = (h[0] - pow(A, N, N)) % N
    return h


def coefficient_matrix(h, n, j):
    size = R + n - 2 * j
    rows = [[0] * size for _ in range(size)]
    for row, degree in enumerate(range(j, R + n - j)):
        for shift in range(n - j):
            if degree == shift:
                rows[row][shift] = -1
            elif degree == shift + R:
                rows[row][shift] = 1
        offset = n - j
        for shift in range(R - j):
            h_degree = degree - shift
            if 0 <= h_degree <= n:
                rows[row][offset + shift] = h[h_degree]
    return matrix(ZZ, rows)


h = make_h()
n = max(i for i, coefficient in enumerate(h) if coefficient)
coefficient_separators = [
    {"degree": int(i), "coefficient": int(coefficient), "gcd": int(gcd(coefficient, N))}
    for i, coefficient in enumerate(h)
    if 1 < gcd(coefficient, N) < N
]
j = int(sys.argv[1]) if len(sys.argv) > 1 else 47
started = time.monotonic()
M = coefficient_matrix(h, n, j)
constructed = time.monotonic()
d_exact = M.det()
finished = time.monotonic()
print(json.dumps({
    "N": int(N),
    "r": int(R),
    "a": int(A),
    "n": int(n),
    "first_coefficient_separator": coefficient_separators[0],
    "coefficient_separator_count": len(coefficient_separators),
    "j": j,
    "dimension": list(M.dimensions()),
    "construction_seconds": constructed - started,
    "determinant_seconds": finished - constructed,
    "determinant_bits": int(abs(d_exact).nbits()),
    "determinant_mod_N": int(d_exact % N),
    "gcd": int(gcd(int(d_exact % N), N)),
}, sort_keys=True))
