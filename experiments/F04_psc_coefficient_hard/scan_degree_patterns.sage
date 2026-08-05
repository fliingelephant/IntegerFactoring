#!/usr/bin/env sage
"""Fast exact canonical-PSC zero-pattern scan for the P11 witness.

Approach-family ID: F04_psc_coefficient_hard.

The subresultant structure theorem says that, over a field, D_j is nonzero
exactly when degree j occurs in the ordinary Euclidean remainder sequence.
This source uses that criterion for the scan.  If a mismatch appears, it
materializes the exact subresultant sequences only for that shift to recover
the fixed-convention local residues.
"""

import argparse
import hashlib
import json
import time
from pathlib import Path


FAMILY = "F04_psc_coefficient_hard"
N = ZZ(20000000499999937)
P_FACTOR = ZZ(100000007)
Q_FACTOR = ZZ(199999991)
R = 2953
STANDARD_SHIFT_BOUND = 2942


def analyze_degree_pattern(characteristic, coefficients):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    dividend = x**R - 1
    divisor = ring(coefficients)
    assert divisor.degree() == R - 1
    degrees = [int(dividend.degree()), int(divisor.degree())]
    while divisor:
        remainder = dividend % divisor
        if remainder:
            degrees.append(int(remainder.degree()))
        dividend, divisor = divisor, remainder
    zero_indices = [index for index in range(R) if index not in degrees]
    encoded = json.dumps(degrees, separators=(",", ":")).encode("ascii")
    return {
        "characteristic": int(characteristic),
        "gcd_degree": degrees[-1],
        "euclidean_degree_count": len(degrees),
        "euclidean_degree_sha256": hashlib.sha256(encoded).hexdigest(),
        "euclidean_degree_prefix": degrees[:8],
        "euclidean_degree_suffix": degrees[-8:],
        "psc_zero_indices": zero_indices,
    }


def exact_canonical_residue(characteristic, coefficients, index):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    polynomial_p = x**R - 1
    polynomial_q = ring(coefficients)
    degree_q = polynomial_q.degree()
    if index == degree_q:
        return int(polynomial_q[degree_q])
    gcd_degree = polynomial_p.gcd(polynomial_q).degree()
    if index < gcd_degree:
        return 0
    subresultants = polynomial_p.subresultants(polynomial_q)
    return int(subresultants[index - gcd_degree][index])


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

            raw_zero_mod_p = [
                index for index, value in enumerate(coefficients) if value % P_FACTOR == 0
            ]
            raw_zero_mod_q = [
                index for index, value in enumerate(coefficients) if value % Q_FACTOR == 0
            ]
            raw_nonunit_positions = [
                index for index, value in enumerate(coefficients) if gcd(value, N) != 1
            ]
            assert not raw_zero_mod_p
            assert not raw_zero_mod_q
            assert not raw_nonunit_positions

            local_p = analyze_degree_pattern(P_FACTOR, coefficients)
            local_q = analyze_degree_pattern(Q_FACTOR, coefficients)
            zeros_p = set(local_p["psc_zero_indices"])
            zeros_q = set(local_q["psc_zero_indices"])
            mismatch_indices = sorted(zeros_p.symmetric_difference(zeros_q))
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
                "elapsed_seconds_before_residue_reconstruction": (
                    time.monotonic() - shift_started
                ),
            }
            if mismatch_indices:
                index = mismatch_indices[0]
                residue_p = exact_canonical_residue(P_FACTOR, coefficients, index)
                residue_q = exact_canonical_residue(Q_FACTOR, coefficients, index)
                assert (residue_p == 0) != (residue_q == 0)
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
            record["elapsed_seconds"] = time.monotonic() - shift_started
            row_handle.write(json.dumps(record, sort_keys=True, default=int) + "\n")
            row_handle.flush()
            records.append(record)
            print(
                f"family={FAMILY} shift={shift}/{args.shift_stop} "
                f"zeros=({len(zeros_p)},{len(zeros_q)}) "
                f"mismatches={len(mismatch_indices)} "
                f"seconds={record['elapsed_seconds']:.6f}",
                flush=True,
            )
            if first_mismatch is not None:
                break

    output = {
        "approach_family": FAMILY,
        "method": "canonical D_j zero iff j occurs in the Euclidean remainder degree sequence",
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
