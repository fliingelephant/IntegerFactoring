#!/usr/bin/env sage
"""Hostile local audit of the C13 determinant and PRS claims.

Approach-family ID: F04_psc_audit.

The local determinant matrices are built from coefficient-wise reductions of
the saved factor-free global H artifact.  A separate quotient-ring powering
reconstruction is used only as a cross-check.  Every formal determinant is
computed directly; Sage's subresultant sequence is used only to test the
claimed PSC zero-pattern correspondence.
"""

import argparse
import hashlib
import json
import math
import os
import time


FAMILY = "F04_psc_audit"


def coefficient_matrix(base_ring, h_coefficients, m, formal_n, j):
    row_degrees = list(range(j, m + formal_n - j))
    columns = []
    for column_shift in range(formal_n - j):
        columns.append([
            base_ring(-1) if degree - column_shift == 0
            else base_ring(1) if degree - column_shift == m
            else base_ring(0)
            for degree in row_degrees
        ])
    for column_shift in range(m - j):
        columns.append([
            base_ring(h_coefficients[degree - column_shift])
            if 0 <= degree - column_shift < len(h_coefficients)
            else base_ring(0)
            for degree in row_degrees
        ])
    dimension = m + formal_n - 2 * j
    assert len(row_degrees) == dimension
    assert len(columns) == dimension
    return matrix(base_ring, columns).transpose()


def quotient_ring_error(field, N, r, shift):
    polynomial_ring = PolynomialRing(field, "x")
    x = polynomial_ring.gen()
    quotient_ring = polynomial_ring.quotient(x**r - 1, "z")
    z = quotient_ring.gen()
    return polynomial_ring(
        ((z + field(shift))**N - z**N - field(shift)).lift()
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-certificate", required=True)
    parser.add_argument("--factor-free-source", required=True)
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    with open(args.global_certificate) as handle:
        global_certificate = json.load(handle)
    with open(args.factor_free_source) as handle:
        factor_free_source_text = handle.read()

    inputs = global_certificate["factor_free_inputs"]
    N = inputs["N"]
    r = inputs["r"]
    shift = inputs["shift"]
    formal_n = global_certificate["global_degree_H"]
    global_h = global_certificate["global_H_coefficients_mod_N"]
    factors = [args.p, args.q]
    assert args.p * args.q == N
    assert args.p != args.q
    assert all(is_prime(factor) for factor in factors)
    assert all(str(factor) not in factor_free_source_text for factor in factors)

    local_data = []
    for characteristic in factors:
        field = GF(characteristic)
        polynomial_ring = PolynomialRing(field, "x")
        x = polynomial_ring.gen()
        p_polynomial = x**r - 1
        reduced_coefficients = [field(value) for value in global_h]
        reduced_h = polynomial_ring(reduced_coefficients)
        independent_h = quotient_ring_error(field, N, r, shift)
        independent_coefficients = [independent_h[index] for index in range(r)]
        assert reduced_coefficients == independent_coefficients
        assert reduced_h == independent_h
        assert gcd(p_polynomial, reduced_h).degree() == 0
        subresultants = p_polynomial.subresultants(reduced_h)
        actual_degree = int(reduced_h.degree())
        assert len(subresultants) == actual_degree
        local_data.append({
            "characteristic": characteristic,
            "field": field,
            "P": p_polynomial,
            "H": reduced_h,
            "coefficients": reduced_coefficients,
            "actual_degree": actual_degree,
            "subresultants": subresultants,
            "quotient_ring_reconstruction_matches_global_reduction": True,
        })

    determinant_rows = []
    sequence_digest = hashlib.sha256()
    prs_zero_disagreements = {str(factor): [] for factor in factors}
    prs_unit_ratios = {str(factor): set() for factor in factors}
    padding_formula_disagreements = {str(factor): [] for factor in factors}
    structural_zero_failures = {str(factor): [] for factor in factors}

    for j in range(formal_n + 1):
        residues = []
        zero_predictions = []
        for item in local_data:
            field = item["field"]
            formal_matrix = coefficient_matrix(
                field, item["coefficients"], r, formal_n, j
            )
            determinant = formal_matrix.det()
            residue = int(determinant)
            residues.append(residue)
            sequence_digest.update(residue.to_bytes(4, "big"))
            actual_degree = item["actual_degree"]

            if j < actual_degree:
                prs_coefficient = item["subresultants"][j][j]
                predicted_zero = prs_coefficient == 0
                if predicted_zero != (determinant == 0):
                    prs_zero_disagreements[str(item["characteristic"])].append(j)
                if prs_coefficient != 0 and determinant != 0:
                    prs_unit_ratios[str(item["characteristic"])].add(
                        int(determinant / prs_coefficient)
                    )
            elif j == actual_degree:
                predicted_zero = False
                top_expected = item["H"][actual_degree] ** (r - actual_degree)
                actual_matrix = coefficient_matrix(
                    field, item["coefficients"], r, actual_degree, j
                )
                actual_determinant = actual_matrix.det()
                if actual_determinant != top_expected:
                    padding_formula_disagreements[
                        str(item["characteristic"])
                    ].append(j)
            else:
                predicted_zero = True
                q_shift_zero_column = formal_n - j
                if any(formal_matrix.column(q_shift_zero_column)):
                    structural_zero_failures[
                        str(item["characteristic"])
                    ].append(j)

            if j <= actual_degree:
                actual_matrix = coefficient_matrix(
                    field, item["coefficients"], r, actual_degree, j
                )
                actual_determinant = actual_matrix.det()
                padding_sign = field(
                    (-1) ** ((formal_n - actual_degree) * (r - j))
                )
                if determinant != padding_sign * actual_determinant:
                    padding_formula_disagreements[
                        str(item["characteristic"])
                    ].append(j)
            if predicted_zero != (determinant == 0):
                prs_zero_disagreements[str(item["characteristic"])].append(j)
            zero_predictions.append(bool(predicted_zero))

        zero_mismatch = (residues[0] == 0) != (residues[1] == 0)
        determinant_rows.append({
            "index": j,
            "matrix_dimension": r + formal_n - 2 * j,
            "residues": residues,
            "zero_predictions_from_prs_and_degree": zero_predictions,
            "zero_mismatch": zero_mismatch,
        })
        print(
            f"family={FAMILY} index={j}/{formal_n} residues={residues} mismatch={zero_mismatch}",
            flush=True,
        )

    first_mismatch = next(row for row in determinant_rows if row["zero_mismatch"])
    decisive_index = global_certificate["first_nontrivial_gcd"]["index"]
    decisive_row = determinant_rows[decisive_index]
    global_residue = global_certificate["first_nontrivial_gcd"][
        "determinant_mod_N"
    ]
    assert first_mismatch == decisive_row
    assert all(
        global_residue % factor == residue
        for factor, residue in zip(factors, decisive_row["residues"])
    )
    assert all(not values for values in prs_zero_disagreements.values())
    assert all(not values for values in padding_formula_disagreements.values())
    assert all(not values for values in structural_zero_failures.values())

    integer_matrix = coefficient_matrix(ZZ, global_h, r, formal_n, decisive_index)
    reduction_commutes = []
    for item in local_data:
        local_matrix = coefficient_matrix(
            item["field"], item["coefficients"], r, formal_n, decisive_index
        )
        reduction_commutes.append(
            integer_matrix.change_ring(item["field"]) == local_matrix
        )
    assert all(reduction_commutes)

    leading_coefficient = global_certificate[
        "global_H_leading_coefficient_mod_N"
    ]
    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "global_certificate": os.path.abspath(args.global_certificate),
        "factor_free_source": os.path.abspath(args.factor_free_source),
        "factor_free_source_sha256": hashlib.sha256(
            factor_free_source_text.encode("utf-8")
        ).hexdigest(),
        "factor_literals_absent_from_factor_free_source": True,
        "N": N,
        "factors_used_only_for_local_audit": factors,
        "r": r,
        "shift": shift,
        "global_formal_degree": formal_n,
        "local_degrees": [item["actual_degree"] for item in local_data],
        "local_reconstructions_match_saved_global_H": [
            item["quotient_ring_reconstruction_matches_global_reduction"]
            for item in local_data
        ],
        "integer_lift_matrix_reduces_to_local_matrices_at_decisive_index": (
            reduction_commutes
        ),
        "determinant_rows": determinant_rows,
        "first_zero_mismatch": first_mismatch,
        "decisive_global_determinant_mod_N": global_residue,
        "decisive_global_gcd": math.gcd(global_residue, N),
        "global_leading_coefficient_mod_N": leading_coefficient,
        "global_leading_coefficient_local_residues": [
            leading_coefficient % factor for factor in factors
        ],
        "global_leading_coefficient_gcd": math.gcd(leading_coefficient, N),
        "prs_zero_disagreement_indices": prs_zero_disagreements,
        "direct_over_sage_prs_nonzero_unit_ratios": {
            key: sorted(values) for key, values in prs_unit_ratios.items()
        },
        "formal_degree_padding_formula_disagreement_indices": (
            padding_formula_disagreements
        ),
        "structural_zero_column_failure_indices": structural_zero_failures,
        "residue_sequence_sha256": sequence_digest.hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
        "audit_passed": True,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")
    print(
        json.dumps(
            {
                "status": "passed",
                "output": args.output,
                "first_zero_mismatch": first_mismatch,
            },
            sort_keys=True,
            default=int,
        ),
        flush=True,
    )


main()
