#!/usr/bin/env sage
"""Form the global AKS error matrix and scan its canonical maximal prefix.

Approach-family ID: F04_joint_matroid_kill.

Rows are the standard shifts in increasing order and columns are coefficient
positions 0,...,r-1.  Every H_a is first formed over Z/NZ.  This run then
reduces that same global row into one requested prime field.  The first A
columns define the canonical maximal square prefix.  If its determinant is
nonzero, the whole A-by-r matrix has full row rank and lexicographic column
basis 0,...,A-1.  If it is zero, the source computes the full exact rank and
pivot columns.
"""

import argparse
import hashlib
import json
import time
from pathlib import Path


FAMILY = "F04_joint_matroid_kill"
INSTANCES = {
    "P14": {
        "N": ZZ(79403),
        "p": ZZ(271),
        "q": ZZ(293),
        "r": 269,
        "shift_bound": 266,
    },
    "P11": {
        "N": ZZ(20000000499999937),
        "p": ZZ(100000007),
        "q": ZZ(199999991),
        "r": 2953,
        "shift_bound": 2942,
    },
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", choices=sorted(INSTANCES), required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    parameters = INSTANCES[args.instance]
    characteristic = ZZ(args.characteristic)
    assert characteristic in (parameters["p"], parameters["q"])
    assert parameters["N"] == parameters["p"] * parameters["q"]
    started = time.monotonic()

    N = parameters["N"]
    r = parameters["r"]
    shift_bound = parameters["shift_bound"]
    residue_ring = Integers(N)
    polynomial_ring = PolynomialRing(residue_ring, "x")
    x = polynomial_ring.gen()
    polynomial_p = x**r - 1
    field = GF(characteristic)
    local_matrix = matrix(field, shift_bound, r)
    global_matrix_hash = hashlib.sha256()
    row_hashes = []
    raw_zero_count = 0
    raw_nonunit_count = 0
    construction_started = time.monotonic()

    for row_index, shift in enumerate(range(1, shift_bound + 1)):
        polynomial_q = (
            power_mod(x + residue_ring(shift), N, polynomial_p)
            - x**(N % r)
            - residue_ring(shift)
        ) % polynomial_p
        coefficients = [int(polynomial_q[index]) for index in range(r)]
        encoded = json.dumps(coefficients, separators=(",", ":")).encode("ascii")
        row_hash = hashlib.sha256(encoded).hexdigest()
        row_hashes.append(row_hash)
        global_matrix_hash.update(len(encoded).to_bytes(8, "big"))
        global_matrix_hash.update(encoded)
        raw_zero_count += sum(value % characteristic == 0 for value in coefficients)
        raw_nonunit_count += sum(gcd(value, N) != 1 for value in coefficients)
        local_matrix[row_index] = vector(field, coefficients)
        if (row_index + 1) % 100 == 0 or row_index + 1 == shift_bound:
            print(
                f"family={FAMILY} instance={args.instance} "
                f"characteristic={characteristic} rows={row_index + 1}/{shift_bound}",
                flush=True,
            )

    construction_seconds = time.monotonic() - construction_started
    prefix_matrix = local_matrix.matrix_from_columns(range(shift_bound))
    determinant_started = time.monotonic()
    determinant = prefix_matrix.det()
    determinant_seconds = time.monotonic() - determinant_started
    if determinant:
        full_rank = shift_bound
        pivot_columns = list(range(shift_bound))
        rank_seconds = 0.0
    else:
        rank_started = time.monotonic()
        full_rank = local_matrix.rank()
        pivot_columns = list(local_matrix.pivots())
        rank_seconds = time.monotonic() - rank_started
        assert full_rank == len(pivot_columns)

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "scan_id": "canonical-maximal-coefficient-prefix-v1",
        "instance": args.instance,
        "inputs": {
            "N": int(N),
            "p": int(parameters["p"]),
            "q": int(parameters["q"]),
            "r": r,
            "shift_start": 1,
            "shift_stop": shift_bound,
            "characteristic": int(characteristic),
        },
        "global_construction": "all H_a formed in (Z/NZ)[X]/(X^r-1) before local reduction",
        "matrix_shape": [shift_bound, r],
        "canonical_prefix_shape": [shift_bound, shift_bound],
        "canonical_prefix_columns": [0, shift_bound - 1],
        "canonical_prefix_determinant": int(determinant),
        "canonical_prefix_determinant_nonzero": bool(determinant),
        "full_matrix_rank": int(full_rank),
        "lexicographic_pivot_columns": pivot_columns,
        "global_matrix_sha256": global_matrix_hash.hexdigest(),
        "global_row_sha256": row_hashes,
        "raw_local_zero_count": int(raw_zero_count),
        "raw_global_nonunit_count": int(raw_nonunit_count),
        "construction_seconds": construction_seconds,
        "determinant_seconds": determinant_seconds,
        "rank_seconds_after_zero_determinant": rank_seconds,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
