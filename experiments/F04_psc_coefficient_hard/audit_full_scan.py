#!/usr/bin/env python3
"""Audit the retained F04 coefficient-hard canonical-PSC scan artifacts.

Approach-family ID: F04_psc_coefficient_hard.
"""

import argparse
import hashlib
import json
from pathlib import Path


FAMILY = "F04_psc_coefficient_hard"
N = 20000000499999937
P_FACTOR = 100000007
Q_FACTOR = 199999991
R = 2953
SHIFT_BOUND = 2942


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--exact-first", required=True)
    parser.add_argument("--exact-last", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    summary_path = Path(args.summary).resolve()
    rows_path = Path(args.rows).resolve()
    exact_first_path = Path(args.exact_first).resolve()
    exact_last_path = Path(args.exact_last).resolve()
    with summary_path.open() as handle:
        summary = json.load(handle)
    with rows_path.open() as handle:
        rows = [json.loads(line) for line in handle]
    with exact_first_path.open() as handle:
        exact_first = json.load(handle)
    with exact_last_path.open() as handle:
        exact_last = json.load(handle)

    assert summary["approach_family"] == FAMILY
    assert summary["inputs"] == {
        "N": N,
        "p": P_FACTOR,
        "q": Q_FACTOR,
        "r": R,
        "shift_start": 1,
        "shift_stop_requested": SHIFT_BOUND,
        "standard_shift_bound": SHIFT_BOUND,
    }
    assert summary["shifts_completed"] == list(range(1, SHIFT_BOUND + 1))
    assert summary["first_mismatch"] is None
    assert not summary["stopped_after_first_mismatch"]
    assert summary["records"] == rows
    assert len(rows) == SHIFT_BOUND

    full_degree_sequence = list(range(R, -1, -1))
    degree_sha256 = hashlib.sha256(
        json.dumps(full_degree_sequence, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    for expected_shift, row in enumerate(rows, start=1):
        assert row["approach_family"] == FAMILY
        assert row["shift"] == expected_shift
        assert row["global_degree_Q"] == R - 1
        assert row["raw_coefficient_zero_count_mod_p"] == 0
        assert row["raw_coefficient_zero_count_mod_q"] == 0
        assert row["raw_coefficient_nonunit_count_mod_N"] == 0
        assert row["psc_mismatch_indices"] == []
        for label, characteristic in (
            ("local_mod_p", P_FACTOR),
            ("local_mod_q", Q_FACTOR),
        ):
            local = row[label]
            assert local["characteristic"] == characteristic
            assert local["gcd_degree"] == 0
            assert local["euclidean_degree_count"] == R + 1
            assert local["euclidean_degree_sha256"] == degree_sha256
            assert local["euclidean_degree_prefix"] == full_degree_sequence[:8]
            assert local["euclidean_degree_suffix"] == full_degree_sequence[-8:]
            assert local["psc_zero_indices"] == []

    exact_by_shift = {1: exact_first, SHIFT_BOUND: exact_last}
    for shift, exact in exact_by_shift.items():
        assert exact["approach_family"] == FAMILY
        assert exact["shifts_completed"] == [shift]
        assert exact["first_mismatch"] is None
        exact_row = exact["records"][0]
        scan_row = rows[shift - 1]
        assert exact_row["global_H_coefficient_sha256"] == scan_row[
            "global_H_coefficient_sha256"
        ]
        for label in ("local_mod_p", "local_mod_q"):
            assert exact_row[label]["gcd_degree"] == 0
            assert exact_row[label]["psc_count"] == R
            assert exact_row[label]["psc_zero_indices"] == []

    for artifact in (summary_path, rows_path, exact_first_path, exact_last_path):
        assert artifact.is_file()
    scan_source = Path(summary["source"])
    assert file_sha256(scan_source) == summary["source_sha256"]
    source_path = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "audit_passed": True,
        "shifts_exhausted": SHIFT_BOUND,
        "indices_per_shift": R,
        "canonical_determinants_checked_per_field": SHIFT_BOUND * R,
        "canonical_determinants_checked_both_fields": 2 * SHIFT_BOUND * R,
        "all_euclidean_chains_consecutive_from_2953_to_0": True,
        "all_canonical_pscs_nonzero_both_fields": True,
        "all_raw_coefficients_units_mod_N": True,
        "exact_full_subresultant_crosscheck_shifts": [1, SHIFT_BOUND],
        "degree_sequence_sha256": degree_sha256,
        "artifacts": {
            str(path): {
                "bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
            for path in (summary_path, rows_path, exact_first_path, exact_last_path)
        },
        "source": str(source_path),
        "source_sha256": file_sha256(source_path),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")


main()
