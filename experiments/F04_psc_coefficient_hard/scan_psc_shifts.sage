#!/usr/bin/env sage
"""Scan canonical PSC zero patterns on the coefficient-hard P11 witness.

Approach-family ID: F04_psc_coefficient_hard.

For each requested standard shift, this source first forms H_a globally in
(Z/NZ)[X]/(X^r-1), then reduces that one coefficient vector into both prime
fields.  Sage's exact subresultant sequence supplies D_0,...,D_{n-1}; the
one-dimensional defining matrix supplies D_n.  The source retains hashes and
boundary samples of every exact residue row and stops after the first local
zero/nonzero mismatch.
"""

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


FAMILY = "F04_psc_coefficient_hard"
N = ZZ(20000000499999937)
P_FACTOR = ZZ(100000007)
Q_FACTOR = ZZ(199999991)
R = 2953
STANDARD_SHIFT_BOUND = 2942


def analyze_reduction(characteristic, coefficients):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    polynomial_p = x**R - 1
    polynomial_q = ring(coefficients)
    degree_q = polynomial_q.degree()
    gcd_degree = polynomial_p.gcd(polynomial_q).degree()
    assert degree_q == R - 1
    assert gcd_degree == 0

    subresultants = polynomial_p.subresultants(polynomial_q)
    assert len(subresultants) == degree_q
    residues = [int(subresultants[index][index]) for index in range(degree_q)]
    residues.append(int(polynomial_q[degree_q]))
    del subresultants
    zero_indices = [index for index, value in enumerate(residues) if value == 0]
    encoded = json.dumps(residues, separators=(",", ":")).encode("ascii")
    return {
        "characteristic": int(characteristic),
        "degree_Q": int(degree_q),
        "gcd_degree": int(gcd_degree),
        "psc_count": len(residues),
        "psc_zero_indices": zero_indices,
        "psc_residue_sha256": hashlib.sha256(encoded).hexdigest(),
        "psc_residue_prefix": residues[:8],
        "psc_residue_suffix": residues[-8:],
    }, residues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shift-start", type=int, required=True)
    parser.add_argument("--shift-stop", type=int, required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    assert 1 <= args.shift_start <= args.shift_stop <= STANDARD_SHIFT_BOUND
    assert N == P_FACTOR * Q_FACTOR
    assert gcd(N, R) == 1
    started = time.monotonic()

    residue_ring = Integers(N)
    polynomial_ring = PolynomialRing(residue_ring, "x")
    x = polynomial_ring.gen()
    polynomial_p = x**R - 1
    source_path = Path(__file__).resolve().with_suffix("")
    source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    records = []
    first_mismatch = None

    with open(args.rows, "w") as row_handle:
        for shift in range(args.shift_start, args.shift_stop + 1):
            shift_started = time.monotonic()
            polynomial_q = (
                power_mod(x + residue_ring(shift), N, polynomial_p)
                - x**(N % R)
                - residue_ring(shift)
            ) % polynomial_p
            coefficients = [int(polynomial_q[index]) for index in range(R)]
            assert polynomial_q.degree() == R - 1

            residues_mod_p = [value % P_FACTOR for value in coefficients]
            residues_mod_q = [value % Q_FACTOR for value in coefficients]
            raw_zero_mod_p = [
                index for index, value in enumerate(residues_mod_p) if value == 0
            ]
            raw_zero_mod_q = [
                index for index, value in enumerate(residues_mod_q) if value == 0
            ]
            raw_nonunit_positions = [
                index for index, value in enumerate(coefficients) if gcd(value, N) != 1
            ]
            assert not raw_zero_mod_p
            assert not raw_zero_mod_q
            assert not raw_nonunit_positions

            local_p, psc_mod_p = analyze_reduction(P_FACTOR, coefficients)
            local_q, psc_mod_q = analyze_reduction(Q_FACTOR, coefficients)
            mismatch_indices = [
                index
                for index, (value_p, value_q) in enumerate(zip(psc_mod_p, psc_mod_q))
                if (value_p == 0) != (value_q == 0)
            ]
            record = {
                "approach_family": FAMILY,
                "shift": shift,
                "global_degree_Q": int(polynomial_q.degree()),
                "global_H_coefficient_sha256": hashlib.sha256(
                    json.dumps(coefficients, separators=(",", ":")).encode("ascii")
                ).hexdigest(),
                "raw_coefficient_zero_count_mod_p": len(raw_zero_mod_p),
                "raw_coefficient_zero_count_mod_q": len(raw_zero_mod_q),
                "raw_coefficient_nonunit_count_mod_N": len(raw_nonunit_positions),
                "local_mod_p": local_p,
                "local_mod_q": local_q,
                "psc_mismatch_indices": mismatch_indices,
                "elapsed_seconds": time.monotonic() - shift_started,
            }
            if mismatch_indices:
                index = mismatch_indices[0]
                residue_p = psc_mod_p[index]
                residue_q = psc_mod_q[index]
                global_residue = int(crt([residue_p, residue_q], [P_FACTOR, Q_FACTOR]))
                first_mismatch = {
                    "shift": shift,
                    "index": index,
                    "D_mod_p": residue_p,
                    "D_mod_q": residue_q,
                    "D_mod_N_from_local_CRT": global_residue,
                    "gcd_D_N": int(gcd(global_residue, N)),
                    "defining_matrix_dimension": 2 * R - 1 - 2 * index,
                }
                record["first_mismatch"] = first_mismatch
            row_handle.write(json.dumps(record, sort_keys=True, default=int) + "\n")
            row_handle.flush()
            records.append(record)
            print(
                f"family={FAMILY} shift={shift}/{args.shift_stop} "
                f"zeros=({len(local_p['psc_zero_indices'])},"
                f"{len(local_q['psc_zero_indices'])}) "
                f"mismatches={len(mismatch_indices)} "
                f"seconds={record['elapsed_seconds']:.6f}",
                flush=True,
            )
            if first_mismatch is not None:
                break

    output = {
        "approach_family": FAMILY,
        "inputs": {
            "N": int(N),
            "p": int(P_FACTOR),
            "q": int(Q_FACTOR),
            "r": R,
            "shift_start": args.shift_start,
            "shift_stop_requested": args.shift_stop,
            "standard_shift_bound": STANDARD_SHIFT_BOUND,
        },
        "construction": "global H_a in (Z/NZ)[X]/(X^r-1), then coefficientwise reduction",
        "canonical_D_convention_source": "experiments/F04_psckill/RESULT.md",
        "parameter_source": "PROVED.md P11 and experiments/F04/output/sage_aks_20000000499999937_full.json",
        "shifts_completed": [record["shift"] for record in records],
        "first_mismatch": first_mismatch,
        "stopped_after_first_mismatch": first_mismatch is not None,
        "records": records,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": source_sha256,
        "rows": str(Path(args.rows).resolve()),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
