#!/usr/bin/env sage
"""Scan canonical principal Sylvester minors for the P14 AKS witness.

Family: F04_psckill.

For P=X^269-1 (degree m=269) and an AKS error Q=H_a of globally
observable degree n, define D_j(P,Q), 0 <= j <= n, as the
determinant of the coefficient matrix of

    (U,V) |--> U P + V Q,

where deg(U)<n-j and deg(V)<m-j, after projecting the output onto the
coefficients of X^j,...,X^(m+n-j-1).  Rows and columns are in increasing
degree, with the U columns before the V columns.  This fixes the sign as
well as the zero pattern.  D_j is the usual determinant-form principal
subresultant coefficient up to convention-dependent sign.

The local scan uses Sage's subresultant PRS to find zero positions.  Any
reported first mismatch is then checked by constructing the defining
matrix itself over each local field and, optionally, over Z/NZ through an
integer lift.  The latter computation uses only N and the requested shift.
"""

import argparse
import hashlib
import json
import math
import os
import time


FAMILY = "F04_psckill"
N = 79403
P_FACTOR = 271
Q_FACTOR = 293
R = 269
STANDARD_SHIFT_BOUND = 266
M = R


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def aks_error(base_ring, shift):
    polynomial_ring = PolynomialRing(base_ring, "x")
    x = polynomial_ring.gen()
    modulus = x**R - 1
    error = quotient_power(x + base_ring(shift), N, modulus)
    error -= x ** (N % R)
    error -= base_ring(shift)
    return modulus, error


def principal_matrix(polynomial_p, polynomial_q, j, formal_n, base_ring):
    """Return the fixed increasing-degree coefficient matrix defining D_j."""
    row_degrees = range(j, M + formal_n - j)
    u_shifts = range(formal_n - j)
    v_shifts = range(M - j)
    columns = []
    for shift in u_shifts:
        columns.append([base_ring(polynomial_p[d - shift]) if d >= shift else base_ring(0)
                        for d in row_degrees])
    for shift in v_shifts:
        columns.append([base_ring(polynomial_q[d - shift]) if d >= shift else base_ring(0)
                        for d in row_degrees])
    dimension = M + formal_n - 2 * j
    assert len(columns) == dimension
    return matrix(base_ring, dimension, dimension,
                  lambda row, column: columns[column][row])


def psc_zero_mask_via_prs(characteristic, shift, formal_n):
    field = GF(characteristic)
    polynomial_p, polynomial_q = aks_error(field, shift)
    assert polynomial_p.degree() == M
    actual_q_degree = int(polynomial_q.degree())
    assert actual_q_degree <= formal_n
    assert gcd(polynomial_p, polynomial_q).degree() == 0
    subresultants = polynomial_p.subresultants(polynomial_q)
    if len(subresultants) != actual_q_degree:
        raise RuntimeError(
            f"unexpected subresultant count {len(subresultants)} at "
            f"characteristic={characteristic}, shift={shift}"
        )
    # For j<deg(Q), specialization from formal degree n to actual degree d
    # preserves the PSC zero pattern (P is monic).  At j=d the defining
    # determinant is a nonzero power of lc(Q), and at j>d it is structurally
    # zero.  Include j=n because that top determinant can itself expose a
    # local degree drop when the global leading coefficient is a zero divisor.
    zero_mask = []
    residues_where_prs_applies = []
    for j in range(formal_n + 1):
        if j < actual_q_degree:
            residue = int(subresultants[j][j])
            zero_mask.append(residue == 0)
            residues_where_prs_applies.append(residue)
        elif j == actual_q_degree:
            zero_mask.append(False)
        else:
            zero_mask.append(True)
    return polynomial_p, polynomial_q, zero_mask, residues_where_prs_applies


def residue_digest(residues):
    digest = hashlib.sha256()
    for value in residues:
        digest.update(int(value).to_bytes(4, "big"))
    return digest.hexdigest()


def defining_determinant_local(characteristic, polynomial_p, polynomial_q, j, formal_n):
    field = GF(characteristic)
    defining_matrix = principal_matrix(polynomial_p, polynomial_q, j, formal_n, field)
    return int(defining_matrix.det()), int(defining_matrix.nrows())


def defining_determinant_global(shift, j, formal_n):
    residue_ring = Integers(N)
    polynomial_p, polynomial_q = aks_error(residue_ring, shift)
    # Lift the fixed residue representatives to ZZ.  Determinant formation over
    # ZZ and final reduction commute with the determinant polynomial over Z/NZ.
    integer_ring = PolynomialRing(ZZ, "x")
    x = integer_ring.gen()
    lifted_p = x**R - 1
    lifted_q = integer_ring([ZZ(coefficient.lift()) for coefficient in polynomial_q])
    defining_matrix = principal_matrix(lifted_p, lifted_q, j, formal_n, ZZ)
    determinant_integer = defining_matrix.det()
    determinant_mod_n = int(determinant_integer % N)
    return {
        "matrix_dimension": int(defining_matrix.nrows()),
        "determinant_mod_N": determinant_mod_n,
        "gcd_with_N": int(math.gcd(determinant_mod_n, N)),
        "integer_determinant_bit_length": int(abs(determinant_integer).nbits()),
        "global_H_degree": int(polynomial_q.degree()),
        "global_H_sha256": hashlib.sha256(
            b"".join(int(coefficient.lift()).to_bytes(4, "big")
                     for coefficient in polynomial_q.list())
        ).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first-shift", type=int, default=1)
    parser.add_argument("--last-shift", type=int, default=STANDARD_SHIFT_BOUND)
    parser.add_argument("--stop-on-first-mismatch", action="store_true")
    parser.add_argument("--compute-global-witness", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    assert 1 <= args.first_shift <= args.last_shift <= STANDARD_SHIFT_BOUND
    assert N == P_FACTOR * Q_FACTOR
    assert is_prime(P_FACTOR) and is_prime(Q_FACTOR)

    started = time.monotonic()
    rows = []
    first_mismatch = None
    for shift in range(args.first_shift, args.last_shift + 1):
        residue_ring = Integers(N)
        _, h_global = aks_error(residue_ring, shift)
        formal_n = int(h_global.degree())
        p_poly, h_mod_p, p_zero_mask, p_residues = psc_zero_mask_via_prs(
            P_FACTOR, shift, formal_n
        )
        q_poly, h_mod_q, q_zero_mask, q_residues = psc_zero_mask_via_prs(
            Q_FACTOR, shift, formal_n
        )
        assert formal_n == max(int(h_mod_p.degree()), int(h_mod_q.degree()))
        mismatch_indices = [
            j for j in range(formal_n + 1)
            if p_zero_mask[j] != q_zero_mask[j]
        ]
        row = {
            "shift": shift,
            "global_degree_H": formal_n,
            "degree_H_mod_p": int(h_mod_p.degree()),
            "degree_H_mod_q": int(h_mod_q.degree()),
            "zero_indices_mod_p": [j for j, value in enumerate(p_zero_mask) if value],
            "zero_indices_mod_q": [j for j, value in enumerate(q_zero_mask) if value],
            "mismatch_indices": mismatch_indices,
            "psc_residue_sha256_mod_p": residue_digest(p_residues),
            "psc_residue_sha256_mod_q": residue_digest(q_residues),
        }
        rows.append(row)
        print(
            f"family={FAMILY} shift={shift}/{args.last_shift} "
            f"mismatches={len(mismatch_indices)}",
            flush=True,
        )
        if mismatch_indices and first_mismatch is None:
            j = mismatch_indices[0]
            determinant_mod_p, dimension_p = defining_determinant_local(
                P_FACTOR, p_poly, h_mod_p, j, formal_n
            )
            determinant_mod_q, dimension_q = defining_determinant_local(
                Q_FACTOR, q_poly, h_mod_q, j, formal_n
            )
            first_mismatch = {
                "shift": shift,
                "index": j,
                "zero_from_PRS_or_degree_specialization_mod_p": p_zero_mask[j],
                "zero_from_PRS_or_degree_specialization_mod_q": q_zero_mask[j],
                "defining_determinant_mod_p": determinant_mod_p,
                "defining_determinant_mod_q": determinant_mod_q,
                "defining_matrix_dimension": dimension_p,
            }
            assert dimension_p == dimension_q
            assert (determinant_mod_p == 0) != (determinant_mod_q == 0)
            if args.compute_global_witness:
                first_mismatch["global_witness"] = defining_determinant_global(
                    shift, j, formal_n
                )
                witness = first_mismatch["global_witness"]
                assert witness["determinant_mod_N"] % P_FACTOR == determinant_mod_p
                assert witness["determinant_mod_N"] % Q_FACTOR == determinant_mod_q
                assert 1 < witness["gcd_with_N"] < N
            if args.stop_on_first_mismatch:
                break

    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "N": N,
        "known_factors_used_only_for_local_counterexample_scan": [P_FACTOR, Q_FACTOR],
        "r": R,
        "standard_shift_bound": STANDARD_SHIFT_BOUND,
        "tested_first_shift": args.first_shift,
        "tested_last_shift_requested": args.last_shift,
        "tested_last_shift_actual": rows[-1]["shift"],
        "degree_P": M,
        "convention": (
            "D_j=det of (U,V)->UP+VQ projected to coefficient degrees "
            "j..m+n-j-1; U shifts then V shifts, all orders increasing"
        ),
        "rows": rows,
        "first_mismatch": first_mismatch,
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")


main()
