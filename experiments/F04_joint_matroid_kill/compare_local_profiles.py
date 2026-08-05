#!/usr/bin/env python3
"""Compare two local canonical joint-matrix profile certificates.

Approach-family ID: F04_joint_matroid_kill.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path


FAMILY = "F04_joint_matroid_kill"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = [Path(args.left).resolve(), Path(args.right).resolve()]
    records = []
    for path in paths:
        with path.open() as handle:
            records.append(json.load(handle))
    left, right = records
    assert left["approach_family"] == right["approach_family"] == FAMILY
    assert left["scan_id"] == right["scan_id"]
    assert left["instance"] == right["instance"]
    assert left["inputs"]["N"] == right["inputs"]["N"]
    assert left["inputs"]["r"] == right["inputs"]["r"]
    assert left["global_matrix_sha256"] == right["global_matrix_sha256"]
    assert left["global_row_sha256"] == right["global_row_sha256"]
    p = left["inputs"]["characteristic"]
    q = right["inputs"]["characteristic"]
    assert {p, q} == {left["inputs"]["p"], left["inputs"]["q"]}
    N = left["inputs"]["N"]
    determinant_p = left["canonical_prefix_determinant"]
    determinant_q = right["canonical_prefix_determinant"]
    inverse_p_mod_q = pow(p, -1, q)
    determinant_mod_N = (
        determinant_p
        + p * (((determinant_q - determinant_p) * inverse_p_mod_q) % q)
    ) % N
    source_path = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "scan_id": left["scan_id"],
        "instance": left["instance"],
        "same_global_matrix_verified": True,
        "local_characteristics": [p, q],
        "local_ranks": [left["full_matrix_rank"], right["full_matrix_rank"]],
        "rank_mismatch": left["full_matrix_rank"] != right["full_matrix_rank"],
        "local_prefix_determinants": [determinant_p, determinant_q],
        "prefix_zero_mismatch": (determinant_p == 0) != (determinant_q == 0),
        "global_prefix_determinant_mod_N_from_CRT": determinant_mod_N,
        "global_prefix_determinant_gcd_with_N": math.gcd(determinant_mod_N, N),
        "local_lexicographic_pivot_columns_equal": (
            left["lexicographic_pivot_columns"]
            == right["lexicographic_pivot_columns"]
        ),
        "local_lexicographic_pivot_columns": [
            left["lexicographic_pivot_columns"],
            right["lexicographic_pivot_columns"],
        ],
        "raw_local_zero_counts": [
            left["raw_local_zero_count"],
            right["raw_local_zero_count"],
        ],
        "raw_global_nonunit_counts": [
            left["raw_global_nonunit_count"],
            right["raw_global_nonunit_count"],
        ],
        "source_artifacts": [str(path) for path in paths],
        "source_artifact_sha256": [
            hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
        ],
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")


main()
