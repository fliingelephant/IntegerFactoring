#!/usr/bin/env python3

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
import time


parser = argparse.ArgumentParser()
parser.add_argument("global_json")
parser.add_argument("local_json")
parser.add_argument("output_json")
args = parser.parse_args()

started = time.monotonic()
global_result = json.loads(Path(args.global_json).read_text(encoding="utf-8"))
local_result = json.loads(Path(args.local_json).read_text(encoding="utf-8"))

N = global_result["inputs"]["N"]
r = global_result["inputs"]["r"]
n = global_result["global_degree_n"]
rows = global_result["determinants"]
witness = global_result["determinant_discovery"]
assert (N, r, global_result["inputs"]["a"], n) == (79403, 269, 1, 268)
assert [row["j"] for row in rows] == list(range(witness["j"] + 1))
assert all(row["gcd_with_N"] == 1 for row in rows[:-1])
assert witness == {"j": 47, "determinant_mod_N": 30352, "gcd_with_N": 271}

for row in rows:
    j = row["j"]
    assert row["p_shift_columns"] == n - j
    assert row["h_shift_columns"] == r - j
    assert row["first_output_degree"] == j
    assert row["last_output_degree"] == r + n - j - 1
    assert row["dimension"] == r + n - 2 * j
    assert int(row["determinant_exact"]) % N == row["determinant_mod_N"]
    assert gcd(row["determinant_mod_N"], N) == row["gcd_with_N"]

ordinary = global_result["first_ordinary_coefficient_separator"]
assert ordinary == {"degree": 0, "coefficient_mod_N": 36585, "gcd_with_N": 271}
assert gcd(global_result["h_coefficients_low_to_high"][0], N) == 271

assert local_result["phase"] == "factor_dependent_local_certificate"
assert local_result["factor_source"].startswith("gcd returned")
assert local_result["factorization"] == [271, 293]
assert local_result["factors_prime"] == [True, True]
assert local_result["global_formal_degree_n"] == n
assert local_result["witness_j"] == 47
assert [entry["actual_degree"] for entry in local_result["local_results"]] == [46, 268]
assert [entry["witness_determinant_residue"] for entry in local_result["local_results"]] == [0, 173]
assert local_result["crt_witness_residue_mod_N"] == 30352
assert local_result["global_witness_gcd_with_N"] == 271

for local in local_result["local_results"]:
    prime = local["modulus"]
    assert local["reduction_commutes_coefficientwise"]
    assert local["formal_degree_used_for_matrices"] == n
    assert [coefficient % prime for coefficient in global_result["h_coefficients_low_to_high"]] == local["h_coefficients_low_to_high"]
    for global_row, local_row in zip(rows, local["determinants"], strict=True):
        assert global_row["j"] == local_row["j"]
        assert global_row["dimension"] == local_row["dimension_with_global_formal_degree"]
        assert global_row["determinant_mod_N"] % prime == local_row["determinant_residue"]

source_paths = [
    Path(__file__).with_name("global_discovery.sage"),
    Path(__file__).with_name("local_certificate.sage"),
    Path(__file__).with_name("verify_outputs.py"),
    Path(__file__).with_name("run_with_timeout.py"),
]
result = {
    "all_assertions_passed": True,
    "verified_claims": {
        "global_degree_n": n,
        "unit_determinant_range": [0, 46],
        "witness": witness,
        "factorization_certificate": local_result["factorization"],
        "local_degrees": [entry["actual_degree"] for entry in local_result["local_results"]],
        "local_witness_residues": [entry["witness_determinant_residue"] for entry in local_result["local_results"]],
        "first_ordinary_coefficient_separator": ordinary,
    },
    "source_sha256": {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in source_paths
    },
    "input_sha256": {
        Path(args.global_json).name: hashlib.sha256(Path(args.global_json).read_bytes()).hexdigest(),
        Path(args.local_json).name: hashlib.sha256(Path(args.local_json).read_bytes()).hexdigest(),
    },
    "elapsed_seconds": time.monotonic() - started,
}
Path(args.output_json).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
