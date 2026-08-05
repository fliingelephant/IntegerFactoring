#!/usr/bin/env sage
"""Validate PRS zero indexing against the fixed canonical determinants.

Approach-family ID: F04_psc_coefficient_hard.

This is a small exact-algebra validation, not evidence about the degree-2953
instance.  It constructs every defining matrix directly and compares its
determinant with Sage's subresultant-polynomial coefficients.
"""

import argparse
import hashlib
import json
import time
from pathlib import Path


FAMILY = "F04_psc_coefficient_hard"


def canonical_determinant(polynomial_p, polynomial_q, index):
    ring = polynomial_p.parent()
    degree_p = polynomial_p.degree()
    degree_q = polynomial_q.degree()
    columns = []
    for shift in range(degree_q - index):
        columns.append(ring.gen()**shift * polynomial_p)
    for shift in range(degree_p - index):
        columns.append(ring.gen()**shift * polynomial_q)
    rows = range(index, degree_p + degree_q - index)
    defining_matrix = matrix(
        ring.base_ring(),
        [[polynomial[row] for polynomial in columns] for row in rows],
    )
    return defining_matrix.det()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    field = GF(7)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    polynomial_p = x**6 - 1
    examples = [
        x**5 + 2*x**4 + 3*x**3 + x**2 + 4*x + 2,
        (x - 1) * (x**4 + 2*x**3 + 3*x + 1),
        x**5 + 3*x**2 + 2,
    ]
    records = []
    for polynomial_q in examples:
        dividend = polynomial_p
        divisor = polynomial_q
        euclidean_degrees = [int(dividend.degree()), int(divisor.degree())]
        while divisor:
            remainder = dividend % divisor
            if remainder:
                euclidean_degrees.append(int(remainder.degree()))
            dividend, divisor = divisor, remainder
        determinants = [
            canonical_determinant(polynomial_p, polynomial_q, index)
            for index in range(polynomial_q.degree() + 1)
        ]
        subresultants = polynomial_p.subresultants(polynomial_q)
        records.append(
            {
                "P": str(polynomial_p),
                "Q": str(polynomial_q),
                "gcd_degree": int(polynomial_p.gcd(polynomial_q).degree()),
                "euclidean_remainder_degrees": euclidean_degrees,
                "indices_missing_from_euclidean_degrees": [
                    index
                    for index in range(polynomial_q.degree() + 1)
                    if index not in euclidean_degrees
                ],
                "canonical_D": [int(value) for value in determinants],
                "canonical_zero_indices": [
                    index for index, value in enumerate(determinants) if value == 0
                ],
                "subresultants": [str(value) for value in subresultants],
                "subresultant_count": len(subresultants),
                "subresultant_degrees": [int(value.degree()) for value in subresultants],
                "subresultant_diagonal_coefficients": [
                    int(subresultants[index][index])
                    for index in range(len(subresultants))
                ],
                "subresultant_diagonal_zero_indices": [
                    index
                    for index in range(len(subresultants))
                    if subresultants[index][index] == 0
                ],
            }
        )

    coprime_records = [record for record in records if record["gcd_degree"] == 0]
    for record in coprime_records:
        assert record["subresultant_count"] == 5
        assert record["canonical_D"][:5] == record[
            "subresultant_diagonal_coefficients"
        ]
        assert record["canonical_D"][5] == 1
    gcd_record = [record for record in records if record["gcd_degree"] > 0][0]
    assert gcd_record["canonical_D"][:gcd_record["gcd_degree"]] == [0]
    for record in records:
        assert record["canonical_zero_indices"] == record[
            "indices_missing_from_euclidean_degrees"
        ]

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "purpose": "canonical determinant versus Sage PRS zero-index validation",
        "field_characteristic": 7,
        "records": records,
        "coprime_canonical_values_match_sage_diagonal": True,
        "top_index_leading_coefficient_formula_matches": True,
        "gcd_forces_initial_canonical_zeros": True,
        "canonical_zero_indices_equal_missing_euclidean_degrees": True,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
