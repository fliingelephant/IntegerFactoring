#!/usr/bin/env sage
"""Fresh exhaustive P11 scan: global H first, then two exact field chains."""

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
import time


N = ZZ(20000000499999937)
FACTOR_1 = ZZ(100000007)
FACTOR_2 = ZZ(199999991)
R = 2953
SHIFT_BOUND = 2942


def encoded_sha256(values):
    encoding = json.dumps(values, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoding).hexdigest()


def euclidean_degrees(characteristic, global_coefficients):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    dividend = x**R - 1
    divisor = ring(global_coefficients)
    degrees = [int(dividend.degree()), int(divisor.degree())]
    while divisor:
        remainder = dividend % divisor
        if remainder:
            degrees.append(int(remainder.degree()))
        dividend, divisor = divisor, remainder
    return degrees


def exact_endpoint(characteristic, global_coefficients):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    first = x**R - 1
    second = ring(global_coefficients)
    n = second.degree()
    subresultants = first.subresultants(second)
    assert n == R - 1
    assert len(subresultants) == n
    residues = [int(subresultants[index][index]) for index in range(n)]
    residues.append(int(second[n] ** (R - n)))
    return {
        "characteristic": int(characteristic),
        "residues": residues,
        "residue_sha256": encoded_sha256(residues),
        "zero_indices": [index for index, value in enumerate(residues) if value == 0],
        "prefix": residues[:8],
        "suffix": residues[-8:],
    }


parser = argparse.ArgumentParser()
parser.add_argument("--rows", required=True)
parser.add_argument("--endpoints", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
assert N == FACTOR_1 * FACTOR_2
assert gcd(N, R) == 1
started = time.monotonic()
global_ring = Integers(N)
polynomial_ring = PolynomialRing(global_ring, "x")
x = polynomial_ring.gen()
modulus_polynomial = x**R - 1
expected_degrees = list(range(R, -1, -1))
expected_degree_sha256 = encoded_sha256(expected_degrees)
source_path = Path(__file__).resolve().with_suffix("")
endpoint_coefficients = {}
completed_shifts = 0
global_coefficients_checked = 0
local_chain_entries_checked = 0

rows_path = Path(args.rows)
rows_path.parent.mkdir(parents=True, exist_ok=True)
with rows_path.open("w", encoding="utf-8") as rows_handle:
    for shift in range(1, SHIFT_BOUND + 1):
        shift_started = time.monotonic()
        # This quotient computation is over Z/NZ and precedes either reduction.
        global_h = (
            power_mod(x + global_ring(shift), N, modulus_polynomial)
            - x**(N % R)
            - global_ring(shift)
        ) % modulus_polynomial
        global_coefficients = [int(global_h[index]) for index in range(R)]
        assert global_h.degree() == R - 1
        nonunit_indices = [
            index
            for index, coefficient in enumerate(global_coefficients)
            if gcd(coefficient, N) != 1
        ]
        assert not nonunit_indices

        degrees_1 = euclidean_degrees(FACTOR_1, global_coefficients)
        degrees_2 = euclidean_degrees(FACTOR_2, global_coefficients)
        assert degrees_1 == expected_degrees
        assert degrees_2 == expected_degrees
        coefficient_sha256 = encoded_sha256(global_coefficients)
        row = {
            "shift": int(shift),
            "global_degree": int(global_h.degree()),
            "global_coefficient_sha256": coefficient_sha256,
            "global_nonunit_coefficient_count": len(nonunit_indices),
            "local_mod_factor_1": {
                "characteristic": int(FACTOR_1),
                "degree_count": len(degrees_1),
                "degree_sha256": encoded_sha256(degrees_1),
                "prefix": degrees_1[:8],
                "suffix": degrees_1[-8:],
            },
            "local_mod_factor_2": {
                "characteristic": int(FACTOR_2),
                "degree_count": len(degrees_2),
                "degree_sha256": encoded_sha256(degrees_2),
                "prefix": degrees_2[:8],
                "suffix": degrees_2[-8:],
            },
            "elapsed_seconds": time.monotonic() - shift_started,
        }
        rows_handle.write(json.dumps(row, sort_keys=True) + "\n")
        rows_handle.flush()
        if shift in (1, SHIFT_BOUND):
            endpoint_coefficients[shift] = global_coefficients
        completed_shifts += 1
        global_coefficients_checked += R
        local_chain_entries_checked += 2 * len(expected_degrees)
        if shift == 1 or shift % 25 == 0 or shift == SHIFT_BOUND:
            print(json.dumps({
                "event": "progress",
                "shift": int(shift),
                "shift_bound": int(SHIFT_BOUND),
                "coefficient_sha256": coefficient_sha256,
                "elapsed_seconds": row["elapsed_seconds"],
            }, sort_keys=True), flush=True)

endpoint_records = []
for shift in (1, SHIFT_BOUND):
    coefficients = endpoint_coefficients[shift]
    local_1 = exact_endpoint(FACTOR_1, coefficients)
    local_2 = exact_endpoint(FACTOR_2, coefficients)
    assert not local_1["zero_indices"]
    assert not local_2["zero_indices"]
    global_residues = [
        int(CRT_list(
            [Integer(residue_1), Integer(residue_2)],
            [FACTOR_1, FACTOR_2],
        ) % N)
        for residue_1, residue_2 in zip(local_1["residues"], local_2["residues"])
    ]
    assert all(gcd(residue, N) == 1 for residue in global_residues)
    endpoint_records.append({
        "shift": int(shift),
        "global_coefficient_sha256": encoded_sha256(coefficients),
        "local_mod_factor_1": local_1,
        "local_mod_factor_2": local_2,
        "global_residues_from_crt": global_residues,
        "global_residue_sha256": encoded_sha256(global_residues),
        "global_nonunit_residue_indices": [
            index for index, residue in enumerate(global_residues)
            if gcd(residue, N) != 1
        ],
    })
    print(json.dumps({
        "event": "endpoint",
        "shift": int(shift),
        "local_hashes": [local_1["residue_sha256"], local_2["residue_sha256"]],
        "global_hash": endpoint_records[-1]["global_residue_sha256"],
    }, sort_keys=True), flush=True)

endpoints_path = Path(args.endpoints)
endpoints_path.write_text(json.dumps({
    "fixed_convention": "increasing rows; increasing P shifts before increasing H shifts",
    "records": endpoint_records,
}, indent=2, sort_keys=True) + "\n")
result = {
    "phase": "fresh_global_before_local_full_exhaustion",
    "inputs": {
        "N": int(N),
        "factors_used_only_after_global_construction": [int(FACTOR_1), int(FACTOR_2)],
        "r": int(R),
        "shift_start": int(1),
        "shift_stop": int(SHIFT_BOUND),
    },
    "construction_order": "form H_a over (Z/NZ)[X]/(X^r-1), materialize its coefficient vector, then reduce that vector",
    "completed_shifts": int(completed_shifts),
    "global_coefficients_checked": int(global_coefficients_checked),
    "local_chain_entries_checked": int(local_chain_entries_checked),
    "determinant_statuses_per_field": int(SHIFT_BOUND * R),
    "determinant_statuses_both_fields": int(2 * SHIFT_BOUND * R),
    "all_global_degrees": int(R - 1),
    "all_global_coefficients_units": True,
    "all_local_degree_chains": "2953,2952,...,0",
    "expected_degree_sha256": expected_degree_sha256,
    "endpoint_shifts": [int(1), int(SHIFT_BOUND)],
    "endpoint_file": str(endpoints_path.resolve()),
    "rows_file": str(rows_path.resolve()),
    "rows_sha256": hashlib.sha256(rows_path.read_bytes()).hexdigest(),
    "endpoints_sha256": hashlib.sha256(endpoints_path.read_bytes()).hexdigest(),
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
}
Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"event": "result", **result}, sort_keys=True), flush=True)
