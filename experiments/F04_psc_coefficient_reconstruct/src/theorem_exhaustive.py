#!/usr/bin/env python3
"""Exhaustively test the determinant theorem and exact matrix convention in small fields."""

import argparse
import itertools
import json
from pathlib import Path


def trim(f: list[int]) -> list[int]:
    while f and f[-1] == 0:
        f.pop()
    return f


def rem(a: list[int], b: list[int], p: int) -> list[int]:
    a = a[:]
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p
        off = len(a) - len(b)
        for i, value in enumerate(b):
            a[off + i] = (a[off + i] - c * value) % p
        trim(a)
    return a


def euclid_degrees(f: list[int], g: list[int], p: int) -> list[int]:
    degrees = [len(f) - 1, len(g) - 1]
    while True:
        h = rem(f, g, p)
        if not h:
            return degrees
        degrees.append(len(h) - 1)
        f, g = g, h


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [row[:] for row in matrix]
    det = 1
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col] % p), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col] % p
        det = det * pivot_value % p
        inv = pow(pivot_value, -1, p)
        for row in range(col + 1, len(a)):
            c = a[row][col] * inv % p
            for k in range(col, len(a)):
                a[row][k] = (a[row][k] - c * a[col][k]) % p
    return det % p


def determinant(f: list[int], g: list[int], j: int, p: int) -> int:
    m = len(f) - 1
    n = len(g) - 1
    columns = list(range(j, m + n - j))
    rows: list[list[int]] = []
    for shift in range(n - j):
        rows.append([f[d - shift] if 0 <= d - shift <= m else 0 for d in columns])
    for shift in range(m - j):
        rows.append([g[d - shift] if 0 <= d - shift <= n else 0 for d in columns])
    assert len(rows) == len(columns)
    return det_mod(rows, p)


def polynomials_of_degree(degree: int, p: int):
    for low in itertools.product(range(p), repeat=degree):
        for lead in range(1, p):
            yield list(low) + [lead]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    cases = 0
    determinants = 0
    positive_gcd_cases = 0
    abnormal_gap_cases = 0
    top_cases = 0
    configurations = ((2, 5), (3, 4), (5, 3))
    for p, max_m in configurations:
        for m in range(1, max_m + 1):
            for n in range(m):
                for f in polynomials_of_degree(m, p):
                    for g in polynomials_of_degree(n, p):
                        chain = euclid_degrees(f, g, p)
                        nonzero_indices = set(chain[1:])
                        cases += 1
                        top_cases += 1
                        if chain[-1] > 0:
                            positive_gcd_cases += 1
                        if any(chain[k] - chain[k + 1] > 1 for k in range(1, len(chain) - 1)):
                            abnormal_gap_cases += 1
                        for j in range(n + 1):
                            actual = determinant(f, g, j, p) != 0
                            predicted = j in nonzero_indices
                            determinants += 1
                            if actual != predicted:
                                failure = {
                                    "p": p,
                                    "F": f,
                                    "G": g,
                                    "j": j,
                                    "chain": chain,
                                    "determinant_nonzero": actual,
                                    "predicted_nonzero": predicted,
                                }
                                Path(args.output).write_text(json.dumps(failure, indent=2) + "\n")
                                raise SystemExit("determinant theorem mismatch")
    result = {
        "status": "pass",
        "field_degree_configurations": configurations,
        "polynomial_pairs": cases,
        "determinants_checked": determinants,
        "top_index_cases": top_cases,
        "positive_gcd_cases": positive_gcd_cases,
        "abnormal_gap_cases": abnormal_gap_cases,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

