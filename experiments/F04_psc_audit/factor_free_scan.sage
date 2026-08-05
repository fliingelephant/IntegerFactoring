#!/usr/bin/env sage
"""Factor-free reconstruction and prefix scan for candidate C13.

Approach-family ID: F04_psc_audit.

This source intentionally contains no prime divisor of the input.  It forms
the AKS error as a dense cyclic coefficient vector, scans the fixed
determinant convention in increasing j, and stops at the first nontrivial
gcd.  Exact integer determinants of canonical coefficient lifts are used as
an implementation-independent way to evaluate the determinant polynomial.
"""

import argparse
import hashlib
import json
import math
import os
import time


FAMILY = "F04_psc_audit"


def cyclic_product(left, right, modulus, length):
    product = [0] * length
    for left_index, left_value in enumerate(left):
        if left_value:
            for right_index, right_value in enumerate(right):
                if right_value:
                    position = (left_index + right_index) % length
                    product[position] = (
                        product[position] + left_value * right_value
                    ) % modulus
    return product


def aks_error_coefficients(N, r, shift):
    result = [0] * r
    result[0] = 1
    base = [0] * r
    base[0] = shift % N
    base[1] = 1
    exponent = N
    while exponent:
        if exponent & 1:
            result = cyclic_product(result, base, N, r)
        exponent >>= 1
        if exponent:
            base = cyclic_product(base, base, N, r)
    result[N % r] = (result[N % r] - 1) % N
    result[0] = (result[0] - shift) % N
    return result


def defining_matrix(lifted_h, m, n, j):
    row_degrees = list(range(j, m + n - j))
    columns = []
    for column_shift in range(n - j):
        column = []
        for degree in row_degrees:
            source_degree = degree - column_shift
            if source_degree == 0:
                column.append(ZZ(-1))
            elif source_degree == m:
                column.append(ZZ(1))
            else:
                column.append(ZZ(0))
        columns.append(column)
    for column_shift in range(m - j):
        column = []
        for degree in row_degrees:
            source_degree = degree - column_shift
            if 0 <= source_degree < len(lifted_h):
                column.append(ZZ(lifted_h[source_degree]))
            else:
                column.append(ZZ(0))
        columns.append(column)
    dimension = m + n - 2 * j
    assert len(row_degrees) == dimension
    assert len(columns) == dimension
    return matrix(
        ZZ,
        dimension,
        dimension,
        lambda row, column: columns[column][row],
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--r", type=int, required=True)
    parser.add_argument("--shift", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    h_coefficients = aks_error_coefficients(args.N, args.r, args.shift)
    global_degree = max(
        index for index, coefficient in enumerate(h_coefficients) if coefficient
    )
    scan = []
    first_separator = None
    for j in range(global_degree + 1):
        determinant = defining_matrix(
            h_coefficients, args.r, global_degree, j
        ).det()
        residue = int(determinant % args.N)
        divisor = math.gcd(residue, args.N)
        row = {
            "index": j,
            "matrix_dimension": args.r + global_degree - 2 * j,
            "determinant_mod_N": residue,
            "gcd_with_N": divisor,
            "integer_determinant_bit_length": int(abs(determinant).nbits()),
            "integer_determinant_sha256": hashlib.sha256(
                str(determinant).encode("ascii")
            ).hexdigest(),
        }
        scan.append(row)
        print(
            f"family={FAMILY} index={j} gcd={divisor} dimension={row['matrix_dimension']}",
            flush=True,
        )
        if 1 < divisor < args.N:
            first_separator = row
            break

    assert first_separator is not None
    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "factor_free_inputs": {
            "N": args.N,
            "r": args.r,
            "shift": args.shift,
        },
        "convention": (
            "columns x^u*(X^m-1), u=0..n-j-1, then x^v*H, "
            "v=0..m-j-1; rows degrees j..m+n-j-1; all increasing"
        ),
        "global_degree_H": global_degree,
        "global_H_leading_coefficient_mod_N": h_coefficients[global_degree],
        "global_H_coefficients_mod_N": h_coefficients,
        "global_H_sha256": hashlib.sha256(
            b"".join(
                int(coefficient).to_bytes(4, "big")
                for coefficient in h_coefficients
            )
        ).hexdigest(),
        "tested_index_interval": [0, scan[-1]["index"]],
        "scan": scan,
        "first_nontrivial_gcd": first_separator,
        "recovered_divisor": first_separator["gcd_with_N"],
        "recovered_cofactor": args.N // first_separator["gcd_with_N"],
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")
    print(
        json.dumps(
            {
                "status": "passed",
                "output": args.output,
                "first_nontrivial_gcd": first_separator,
            },
            sort_keys=True,
            default=int,
        ),
        flush=True,
    )


main()
