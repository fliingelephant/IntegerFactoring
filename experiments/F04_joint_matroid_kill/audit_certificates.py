#!/usr/bin/env python3
"""Audit the retained joint AKS row-matroid certificates.

Approach-family ID: F04_joint_matroid_kill.
"""

import argparse
import hashlib
import json
from pathlib import Path


FAMILY = "F04_joint_matroid_kill"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p14-left", required=True)
    parser.add_argument("--p14-right", required=True)
    parser.add_argument("--p14-comparison", required=True)
    parser.add_argument("--p11-left", required=True)
    parser.add_argument("--p11-right", required=True)
    parser.add_argument("--p11-comparison", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = {name: Path(value).resolve() for name, value in vars(args).items() if name != "output"}
    records = {}
    for name, path in paths.items():
        with path.open() as handle:
            records[name] = json.load(handle)

    p14_left = records["p14_left"]
    p14_right = records["p14_right"]
    p14_comparison = records["p14_comparison"]
    p11_left = records["p11_left"]
    p11_right = records["p11_right"]
    p11_comparison = records["p11_comparison"]
    for record in records.values():
        assert record["approach_family"] == FAMILY

    assert p14_left["global_matrix_sha256"] == p14_right["global_matrix_sha256"]
    assert p14_left["global_row_sha256"] == p14_right["global_row_sha256"]
    assert len(p14_left["global_row_sha256"]) == 266
    assert p14_left["full_matrix_rank"] == 23
    assert p14_right["full_matrix_rank"] == 266
    assert p14_left["canonical_prefix_determinant"] == 0
    assert p14_right["canonical_prefix_determinant"] == 30
    assert p14_comparison["same_global_matrix_verified"]
    assert p14_comparison["rank_mismatch"]
    assert p14_comparison["prefix_zero_mismatch"]
    assert p14_comparison["global_prefix_determinant_gcd_with_N"] == 271

    assert p11_left["global_matrix_sha256"] == p11_right["global_matrix_sha256"]
    assert p11_left["global_row_sha256"] == p11_right["global_row_sha256"]
    assert len(p11_left["global_row_sha256"]) == 2942
    assert p11_left["full_matrix_rank"] == p11_right["full_matrix_rank"] == 2942
    assert p11_left["canonical_prefix_determinant"] == 56136614
    assert p11_right["canonical_prefix_determinant"] == 132391112
    assert p11_left["lexicographic_pivot_columns"] == list(range(2942))
    assert p11_right["lexicographic_pivot_columns"] == list(range(2942))
    assert p11_left["raw_local_zero_count"] == p11_right["raw_local_zero_count"] == 0
    assert p11_left["raw_global_nonunit_count"] == p11_right["raw_global_nonunit_count"] == 0
    assert p11_comparison["same_global_matrix_verified"]
    assert not p11_comparison["rank_mismatch"]
    assert not p11_comparison["prefix_zero_mismatch"]
    assert p11_comparison["global_prefix_determinant_mod_N_from_CRT"] == 16315256998204520
    assert p11_comparison["global_prefix_determinant_gcd_with_N"] == 1
    assert p11_comparison["local_lexicographic_pivot_columns_equal"]

    scan_source = Path(p11_left["source"])
    assert file_sha256(scan_source) == p11_left["source_sha256"]
    assert p11_left["source_sha256"] == p11_right["source_sha256"]
    source_path = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "audit_passed": True,
        "P14": {
            "same_global_matrix_verified": True,
            "local_ranks": [23, 266],
            "prefix_determinants": [0, 30],
            "factor_recovered": 271,
        },
        "P11": {
            "same_global_matrix_verified": True,
            "matrix_shape": [2942, 2953],
            "local_ranks": [2942, 2942],
            "row_matroids_both_free": True,
            "prefix_determinants": [56136614, 132391112],
            "global_prefix_determinant_mod_N": 16315256998204520,
            "global_prefix_determinant_gcd_with_N": 1,
            "lexicographic_column_basis_both": [0, 2941],
            "global_matrix_sha256": p11_left["global_matrix_sha256"],
            "global_row_hash_count": 2942,
            "raw_coefficients_all_units": True,
        },
        "artifacts": {
            name: {
                "path": str(path),
                "bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
            for name, path in paths.items()
        },
        "source": str(source_path),
        "source_sha256": file_sha256(source_path),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")


main()
