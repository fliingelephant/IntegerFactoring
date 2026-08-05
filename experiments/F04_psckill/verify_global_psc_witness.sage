#!/usr/bin/env sage
"""Factor-free verifier for the F04_psckill principal-minor witness.

This source deliberately contains neither factor of N.  It builds H_1 in
(Z/NZ)[X]/(X^269-1), forms the fixed D_47 Sylvester-map matrix through
integer representatives, computes its exact integer determinant, reduces
modulo N, and takes one integer gcd.
"""

import argparse
import hashlib
import json
import math
import os
import time


FAMILY = "F04_psckill"


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=79403)
    parser.add_argument("--r", type=int, default=269)
    parser.add_argument("--shift", type=int, default=1)
    parser.add_argument("--index", type=int, default=47)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    N, r, shift, j = args.N, args.r, args.shift, args.index
    started = time.monotonic()

    residue_ring = Integers(N)
    polynomial_ring = PolynomialRing(residue_ring, "x")
    x = polynomial_ring.gen()
    p_polynomial = x**r - 1
    h = quotient_power(x + residue_ring(shift), N, p_polynomial)
    h -= x ** (N % r)
    h -= residue_ring(shift)
    n = int(h.degree())
    m = r
    assert 0 <= j <= n < m

    integer_ring = PolynomialRing(ZZ, "x")
    z = integer_ring.gen()
    lifted_p = z**r - 1
    lifted_h = integer_ring([ZZ(coefficient.lift()) for coefficient in h])
    row_degrees = range(j, m + n - j)
    columns = []
    for polynomial, shift_count in ((lifted_p, n - j), (lifted_h, m - j)):
        for column_shift in range(shift_count):
            columns.append([
                ZZ(polynomial[degree - column_shift])
                if degree >= column_shift else ZZ(0)
                for degree in row_degrees
            ])
    dimension = m + n - 2 * j
    assert len(columns) == dimension
    defining_matrix = matrix(
        ZZ, dimension, dimension,
        lambda row, column: columns[column][row],
    )
    determinant = defining_matrix.det()
    residue = int(determinant % N)
    divisor = int(math.gcd(residue, N))
    assert 1 < divisor < N and N % divisor == 0
    leading_coefficient = int(h[n].lift())
    leading_coefficient_gcd = int(math.gcd(leading_coefficient, N))

    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "inputs_only": {"N": N, "r": r, "shift": shift, "index": j},
        "global_degree_H": n,
        "global_H_leading_coefficient_mod_N": leading_coefficient,
        "global_H_leading_coefficient_gcd_with_N": leading_coefficient_gcd,
        "matrix_dimension": dimension,
        "determinant_mod_N": residue,
        "gcd_with_N": divisor,
        "cofactor_after_gcd": N // divisor,
        "integer_determinant_bit_length": int(abs(determinant).nbits()),
        "global_H_sha256": hashlib.sha256(
            b"".join(int(coefficient.lift()).to_bytes(4, "big") for coefficient in h)
        ).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")
    print(json.dumps(result, sort_keys=True, default=int), flush=True)


main()
