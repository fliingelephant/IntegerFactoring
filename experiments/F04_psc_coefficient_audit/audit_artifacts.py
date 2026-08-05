#!/usr/bin/env python3

import argparse
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path
import time


N = 20000000499999937
FACTOR_1 = 100000007
FACTOR_2 = 199999991
R = 2953
SHIFT_BOUND = 2942


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def encoded_sha256(values):
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode("ascii")
    ).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--theorem", required=True)
parser.add_argument("--summary", required=True)
parser.add_argument("--rows", required=True)
parser.add_argument("--endpoints", required=True)
parser.add_argument("--new-status", required=True)
parser.add_argument("--theorem-status", required=True)
parser.add_argument("--reference-rows", required=True)
parser.add_argument("--reference-first", required=True)
parser.add_argument("--reference-last", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
paths = {name: Path(value) for name, value in vars(args).items() if name != "output"}
theorem = json.loads(paths["theorem"].read_text())
summary = json.loads(paths["summary"].read_text())
endpoints = json.loads(paths["endpoints"].read_text())
new_status = json.loads(paths["new_status"].read_text())
theorem_status = json.loads(paths["theorem_status"].read_text())
reference_first = json.loads(paths["reference_first"].read_text())
reference_last = json.loads(paths["reference_last"].read_text())

assert theorem["first_counterexample"] is None
assert theorem["case_count"] == 4932
assert theorem["direct_determinant_count"] == 17556
assert theorem["abnormal_gap_case_count"] == 1788
assert theorem["positive_gcd_case_count"] == 1790
assert theorem["top_formula_checked_every_case"]
assert sha256(Path(theorem["source"])) == theorem["source_sha256"]
assert theorem_status["disposition"] == "completed"
assert not theorem_status["timed_out"]

assert summary["inputs"] == {
    "N": N,
    "factors_used_only_after_global_construction": [FACTOR_1, FACTOR_2],
    "r": R,
    "shift_start": 1,
    "shift_stop": SHIFT_BOUND,
}
assert summary["completed_shifts"] == SHIFT_BOUND
assert summary["global_coefficients_checked"] == SHIFT_BOUND * R
assert summary["local_chain_entries_checked"] == 2 * SHIFT_BOUND * (R + 1)
assert summary["determinant_statuses_per_field"] == SHIFT_BOUND * R
assert summary["determinant_statuses_both_fields"] == 2 * SHIFT_BOUND * R
assert summary["all_global_degrees"] == R - 1
assert summary["all_global_coefficients_units"]
assert sha256(paths["rows"]) == summary["rows_sha256"]
assert sha256(paths["endpoints"]) == summary["endpoints_sha256"]
assert sha256(Path(summary["source"])) == summary["source_sha256"]
assert new_status["disposition"] == "completed"
assert not new_status["timed_out"]

full_degrees = list(range(R, -1, -1))
degree_sha256 = encoded_sha256(full_degrees)
assert summary["expected_degree_sha256"] == degree_sha256
row_count = 0
with paths["rows"].open() as fresh_handle, paths["reference_rows"].open() as old_handle:
    for expected_shift, pair in enumerate(
        itertools.zip_longest(fresh_handle, old_handle), start=1
    ):
        fresh_line, old_line = pair
        assert fresh_line is not None and old_line is not None
        fresh = json.loads(fresh_line)
        old = json.loads(old_line)
        assert fresh["shift"] == expected_shift == old["shift"]
        assert fresh["global_degree"] == R - 1
        assert fresh["global_nonunit_coefficient_count"] == 0
        assert fresh["global_coefficient_sha256"] == old["global_H_coefficient_sha256"]
        for key, characteristic in (
            ("local_mod_factor_1", FACTOR_1),
            ("local_mod_factor_2", FACTOR_2),
        ):
            local = fresh[key]
            assert local["characteristic"] == characteristic
            assert local["degree_count"] == R + 1
            assert local["degree_sha256"] == degree_sha256
            assert local["prefix"] == full_degrees[:8]
            assert local["suffix"] == full_degrees[-8:]
        row_count += 1
assert row_count == SHIFT_BOUND

assert endpoints["fixed_convention"].startswith("increasing rows")
assert [record["shift"] for record in endpoints["records"]] == [1, SHIFT_BOUND]
references = {1: reference_first, SHIFT_BOUND: reference_last}
boundary_values = []
for record in endpoints["records"]:
    shift = record["shift"]
    reference = references[shift]["records"][0]
    assert record["global_coefficient_sha256"] == reference["global_H_coefficient_sha256"]
    for fresh_key, old_key in (
        ("local_mod_factor_1", "local_mod_p"),
        ("local_mod_factor_2", "local_mod_q"),
    ):
        local = record[fresh_key]
        residues = local["residues"]
        assert len(residues) == R
        assert not local["zero_indices"]
        assert encoded_sha256(residues) == local["residue_sha256"]
        assert local["residue_sha256"] == reference[old_key]["psc_residue_sha256"]
        assert local["prefix"] == reference[old_key]["psc_residue_prefix"]
        assert local["suffix"] == reference[old_key]["psc_residue_suffix"]
    global_residues = record["global_residues_from_crt"]
    assert len(global_residues) == R
    assert not record["global_nonunit_residue_indices"]
    assert encoded_sha256(global_residues) == record["global_residue_sha256"]
    for local_1, local_2, global_value in zip(
        record["local_mod_factor_1"]["residues"],
        record["local_mod_factor_2"]["residues"],
        global_residues,
        strict=True,
    ):
        assert global_value % FACTOR_1 == local_1
        assert global_value % FACTOR_2 == local_2
        assert gcd(global_value, N) == 1
    boundary_values.append({
        "shift": shift,
        "D_0": {
            "mod_factor_1": record["local_mod_factor_1"]["residues"][0],
            "mod_factor_2": record["local_mod_factor_2"]["residues"][0],
            "mod_N": global_residues[0],
        },
        "D_2952": {
            "mod_factor_1": record["local_mod_factor_1"]["residues"][-1],
            "mod_factor_2": record["local_mod_factor_2"]["residues"][-1],
            "mod_N": global_residues[-1],
        },
        "local_residue_hashes": [
            record["local_mod_factor_1"]["residue_sha256"],
            record["local_mod_factor_2"]["residue_sha256"],
        ],
        "global_residue_hash": record["global_residue_sha256"],
    })

result = {
    "audit_passed": True,
    "authoritative_theorem_stress_run": "A03",
    "authoritative_full_exhaustion_run": "A04",
    "fresh_rows_checked": row_count,
    "fresh_global_hashes_matching_reference_rows": row_count,
    "global_coefficients_checked": SHIFT_BOUND * R,
    "exact_local_determinant_statuses": 2 * SHIFT_BOUND * R,
    "endpoint_exact_residue_vectors_match_reference": True,
    "boundary_values": boundary_values,
    "artifact_sha256": {
        str(path): sha256(path)
        for path in paths.values()
    },
    "source_sha256": sha256(Path(__file__)),
    "elapsed_seconds": time.monotonic() - started,
}
Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
