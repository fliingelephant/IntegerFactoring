#!/usr/bin/env sage

import hashlib
import json
from math import gcd
from pathlib import Path
import sys
import time


N = 79403
R = 269
A = 1


def cyclic_multiply(left, right):
    product = [0] * R
    for i, left_coefficient in enumerate(left):
        if left_coefficient:
            for k, right_coefficient in enumerate(right):
                if right_coefficient:
                    index = (i + k) % R
                    product[index] = (
                        product[index] + left_coefficient * right_coefficient
                    ) % N
    return product


def compute_h():
    value = [0] * R
    value[0] = 1
    base = [0] * R
    base[0] = A
    base[1] = 1
    exponent = N
    while exponent:
        if exponent & 1:
            value = cyclic_multiply(value, base)
        exponent >>= 1
        if exponent:
            base = cyclic_multiply(base, base)
    value[N % R] = (value[N % R] - 1) % N
    value[0] = (value[0] - 1) % N
    return value


def coefficient_matrix(h, n, j):
    p_columns = n - j
    h_columns = R - j
    dimension = p_columns + h_columns
    rows = [[0] * dimension for _ in range(dimension)]
    for row, output_degree in enumerate(range(j, R + n - j)):
        for shift in range(p_columns):
            if output_degree == shift:
                rows[row][shift] = -1
            elif output_degree == shift + R:
                rows[row][shift] = 1
        for shift in range(h_columns):
            h_degree = output_degree - shift
            if 0 <= h_degree <= n:
                rows[row][p_columns + shift] = h[h_degree]
    return matrix(ZZ, rows)


if len(sys.argv) != 2:
    raise SystemExit("usage: sage global_discovery.sage OUTPUT_JSON")

output_path = Path(sys.argv[1])
started = time.monotonic()
h = compute_h()
n = max(index for index, coefficient in enumerate(h) if coefficient)
h_encoding = json.dumps([int(coefficient) for coefficient in h], separators=(",", ":"))
coefficient_separators = [
    {
        "degree": int(index),
        "coefficient_mod_N": int(coefficient),
        "gcd_with_N": int(gcd(int(coefficient), N)),
    }
    for index, coefficient in enumerate(h)
    if 1 < gcd(int(coefficient), N) < N
]

print(json.dumps({
    "event": "h_computed",
    "N": int(N),
    "r": int(R),
    "a": int(A),
    "n": int(n),
    "h_sha256": hashlib.sha256(h_encoding.encode()).hexdigest(),
    "coefficient_separator_count": len(coefficient_separators),
    "first_coefficient_separator": coefficient_separators[0],
}, sort_keys=True), flush=True)

determinants = []
determinant_discovery = None
for j in range(min(n, R) + 1):
    determinant_started = time.monotonic()
    integer_matrix = coefficient_matrix(h, n, j)
    determinant = integer_matrix.det()
    residue = int(determinant % N)
    common_divisor = gcd(residue, N)
    row = {
        "j": int(j),
        "p_shift_columns": int(n - j),
        "h_shift_columns": int(R - j),
        "first_output_degree": int(j),
        "last_output_degree": int(R + n - j - 1),
        "dimension": int(R + n - 2 * j),
        "determinant_exact": str(determinant),
        "determinant_exact_bits": int(abs(determinant).nbits()),
        "determinant_mod_N": residue,
        "gcd_with_N": int(common_divisor),
        "elapsed_seconds": time.monotonic() - determinant_started,
    }
    determinants.append(row)
    print(json.dumps({
        "event": "determinant",
        "j": row["j"],
        "dimension": row["dimension"],
        "determinant_exact_bits": row["determinant_exact_bits"],
        "determinant_mod_N": residue,
        "gcd_with_N": int(common_divisor),
        "elapsed_seconds": row["elapsed_seconds"],
    }, sort_keys=True), flush=True)
    if 1 < common_divisor < N:
        determinant_discovery = {
            "j": int(j),
            "determinant_mod_N": residue,
            "gcd_with_N": int(common_divisor),
        }
        break

if determinant_discovery is None:
    raise RuntimeError("the increasing-j scan found no proper divisor")

result = {
    "phase": "global_discovery_without_known_factorization",
    "inputs": {"N": int(N), "r": int(R), "a": int(A)},
    "h_definition": "(X+a)^N-X^N-1 in (Z/NZ)[X]/(X^r-1), with a=1",
    "h_coefficients_low_to_high": [int(coefficient) for coefficient in h],
    "h_coefficients_sha256": hashlib.sha256(h_encoding.encode()).hexdigest(),
    "global_degree_n": int(n),
    "ordinary_coefficient_scan_order": "increasing degree from 0 through n",
    "ordinary_coefficient_separators": coefficient_separators,
    "first_ordinary_coefficient_separator": coefficient_separators[0],
    "determinant_scan_order": "increasing j from 0; stop at first proper gcd",
    "determinants": determinants,
    "determinant_discovery": determinant_discovery,
    "factorization_used_as_input": False,
    "elapsed_seconds": time.monotonic() - started,
}
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "event": "global_result",
    "output": str(output_path),
    "determinant_discovery": determinant_discovery,
    "elapsed_seconds": result["elapsed_seconds"],
}, sort_keys=True), flush=True)
