#!/usr/bin/env sage

import json
from math import gcd
from pathlib import Path
import sys
import time


if len(sys.argv) != 3:
    raise SystemExit("usage: sage local_certificate.sage GLOBAL_JSON OUTPUT_JSON")

global_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
global_result = json.loads(global_path.read_text(encoding="utf-8"))
N = int(global_result["inputs"]["N"])
R = int(global_result["inputs"]["r"])
A = int(global_result["inputs"]["a"])
n = int(global_result["global_degree_n"])
witness_j = int(global_result["determinant_discovery"]["j"])
discovered_factor = int(global_result["determinant_discovery"]["gcd_with_N"])
cofactor = N // discovered_factor

if discovered_factor * cofactor != N:
    raise RuntimeError("the global gcd does not divide N")
if gcd(discovered_factor, cofactor) != 1:
    raise RuntimeError("the two discovered factors are not coprime")


def independent_local_h(prime):
    field = GF(prime)
    polynomial_ring = PolynomialRing(field, "x")
    x = polynomial_ring.gen()
    quotient = polynomial_ring.quotient(x**R - 1, "xbar")
    xbar = quotient.gen()
    representative = ((xbar + field(A))**N - xbar**N - 1).lift()
    return [field(representative[index]) for index in range(R)]


def coefficient_matrix(field, h, formal_n, j):
    p_columns = formal_n - j
    h_columns = R - j
    dimension = p_columns + h_columns
    rows = [[field.zero()] * dimension for _ in range(dimension)]
    for row, output_degree in enumerate(range(j, R + formal_n - j)):
        for shift in range(p_columns):
            if output_degree == shift:
                rows[row][shift] = -field.one()
            elif output_degree == shift + R:
                rows[row][shift] = field.one()
        for shift in range(h_columns):
            h_degree = output_degree - shift
            if 0 <= h_degree <= formal_n:
                rows[row][p_columns + shift] = h[h_degree]
    return matrix(field, rows)


started = time.monotonic()
local_results = []
for prime in (discovered_factor, cofactor):
    field = GF(prime)
    h = independent_local_h(prime)
    actual_degree = max(index for index, coefficient in enumerate(h) if coefficient)
    reduced_global_h = [
        field(coefficient)
        for coefficient in global_result["h_coefficients_low_to_high"]
    ]
    if h != reduced_global_h:
        raise RuntimeError(f"H reduction failed to commute modulo {prime}")

    determinant_rows = []
    for global_row in global_result["determinants"]:
        j = int(global_row["j"])
        determinant_started = time.monotonic()
        determinant = coefficient_matrix(field, h, n, j).det()
        residue = int(determinant)
        expected = int(global_row["determinant_mod_N"]) % prime
        if residue != expected:
            raise RuntimeError(f"determinant reduction failed at prime={prime}, j={j}")
        determinant_rows.append({
            "j": j,
            "dimension_with_global_formal_degree": int(R + n - 2 * j),
            "determinant_residue": residue,
            "global_residue_reduced": expected,
            "elapsed_seconds": time.monotonic() - determinant_started,
        })
        print(json.dumps({
            "event": "local_determinant",
            "prime": int(prime),
            "j": j,
            "dimension": int(R + n - 2 * j),
            "residue": residue,
            "elapsed_seconds": determinant_rows[-1]["elapsed_seconds"],
        }, sort_keys=True), flush=True)

    local_results.append({
        "modulus": int(prime),
        "is_prime": bool(is_prime(prime)),
        "h_coefficients_low_to_high": [int(coefficient) for coefficient in h],
        "actual_degree": int(actual_degree),
        "formal_degree_used_for_matrices": n,
        "reduction_commutes_coefficientwise": True,
        "determinants": determinant_rows,
        "witness_j": witness_j,
        "witness_determinant_residue": determinant_rows[-1]["determinant_residue"],
    })

first_residue = local_results[0]["witness_determinant_residue"]
second_residue = local_results[1]["witness_determinant_residue"]
crt_residue = int(CRT_list(
    [Integer(first_residue), Integer(second_residue)],
    [Integer(discovered_factor), Integer(cofactor)],
) % N)
global_witness_residue = int(global_result["determinant_discovery"]["determinant_mod_N"])
if crt_residue != global_witness_residue:
    raise RuntimeError("CRT reconstruction disagrees with the global determinant")

result = {
    "phase": "factor_dependent_local_certificate",
    "factor_source": "gcd returned by the preceding global increasing-j scan",
    "N": N,
    "factorization": [discovered_factor, cofactor],
    "factors_coprime": True,
    "factors_prime": [bool(is_prime(discovered_factor)), bool(is_prime(cofactor))],
    "global_formal_degree_n": n,
    "witness_j": witness_j,
    "local_results": local_results,
    "crt_witness_residue_mod_N": crt_residue,
    "global_witness_residue_mod_N": global_witness_residue,
    "global_witness_gcd_with_N": gcd(global_witness_residue, N),
    "elapsed_seconds": time.monotonic() - started,
}
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "event": "local_result",
    "output": str(output_path),
    "factorization": result["factorization"],
    "degrees": [row["actual_degree"] for row in local_results],
    "witness_residues": [first_residue, second_residue],
    "crt_residue": crt_residue,
    "elapsed_seconds": result["elapsed_seconds"],
}, sort_keys=True), flush=True)
