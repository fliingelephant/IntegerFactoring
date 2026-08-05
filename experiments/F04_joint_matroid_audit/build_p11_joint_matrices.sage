#!/usr/bin/env sage
"""Construct the P11 global AKS rows once and retain both local matrices."""

import argparse
import hashlib
import json
from pathlib import Path
import time


N = ZZ(20000000499999937)
P = ZZ(100000007)
Q = ZZ(199999991)
R = 2953
A = 2942


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--p-matrix", required=True)
parser.add_argument("--q-matrix", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
assert N == P * Q
started = time.monotonic()

residue_ring = Integers(N)
polynomial_ring = PolynomialRing(residue_ring, "x")
x = polynomial_ring.gen()
modulus = x**R - 1
fields = {"p": GF(P), "q": GF(Q)}
local_matrices = {key: matrix(field, A, R) for key, field in fields.items()}
global_matrix_hash = hashlib.sha256()
global_row_hashes = []
raw_local_zero_counts = {"p": 0, "q": 0}
raw_global_nonunit_count = 0
construction_started = time.monotonic()

for row_index, shift in enumerate(range(1, A + 1)):
    error = (
        power_mod(x + residue_ring(shift), N, modulus)
        - x**(N % R)
        - residue_ring(shift)
    ) % modulus
    coefficients = [int(error[index]) for index in range(R)]
    encoded = json.dumps(coefficients, separators=(",", ":")).encode("ascii")
    global_row_hashes.append(hashlib.sha256(encoded).hexdigest())
    global_matrix_hash.update(len(encoded).to_bytes(8, "big"))
    global_matrix_hash.update(encoded)
    raw_global_nonunit_count += sum(gcd(value, N) != 1 for value in coefficients)
    for key, characteristic in (("p", P), ("q", Q)):
        raw_local_zero_counts[key] += sum(value % characteristic == 0 for value in coefficients)
        local_matrices[key][row_index] = vector(fields[key], coefficients)
    if (row_index + 1) % 100 == 0 or row_index + 1 == A:
        print(f"stage=joint-build rows={row_index + 1}/{A}", flush=True)
construction_seconds = time.monotonic() - construction_started

prefix_determinants = {}
determinant_seconds = {}
for key in ("p", "q"):
    determinant_started = time.monotonic()
    prefix_determinants[key] = int(local_matrices[key].matrix_from_columns(range(A)).det())
    determinant_seconds[key] = time.monotonic() - determinant_started
    print(
        f"stage=prefix-determinant field={key} value={prefix_determinants[key]}",
        flush=True,
    )

matrix_paths = {"p": Path(args.p_matrix).resolve(), "q": Path(args.q_matrix).resolve()}
matrix_save_seconds = {}
for key in ("p", "q"):
    matrix_paths[key].parent.mkdir(parents=True, exist_ok=True)
    save_started = time.monotonic()
    save(local_matrices[key], str(matrix_paths[key]), compress=False)
    matrix_save_seconds[key] = time.monotonic() - save_started
    assert matrix_paths[key].exists()
    print(
        f"stage=matrix-save field={key} bytes={matrix_paths[key].stat().st_size}",
        flush=True,
    )

prefix_crt = int(crt(ZZ(prefix_determinants["p"]), ZZ(prefix_determinants["q"]), P, Q))
source_path = Path(__file__).resolve()
output = {
    "approach_family": "F04_joint_matroid_audit",
    "stage": "P11-joint-build-v1",
    "inputs": {
        "N": int(N),
        "p": int(P),
        "q": int(Q),
        "r": R,
        "shift_start": 1,
        "shift_stop": A,
    },
    "joint_global_construction": "each H_a is formed once in (Z/NZ)[X]/(X^r-1), then the same coefficient vector is assigned to both local matrices before any local tail solve",
    "matrix_shape": [A, R],
    "global_matrix_sha256": global_matrix_hash.hexdigest(),
    "global_row_sha256": global_row_hashes,
    "raw_global_nonunit_count": int(raw_global_nonunit_count),
    "raw_local_zero_counts": raw_local_zero_counts,
    "prefix_determinants": prefix_determinants,
    "prefix_determinant_nonzero_both": all(prefix_determinants.values()),
    "global_prefix_determinant_mod_N_from_CRT": prefix_crt,
    "global_prefix_determinant_gcd_with_N": int(gcd(prefix_crt, N)),
    "matrix_artifacts": {
        key: {
            "path": str(matrix_paths[key]),
            "bytes": matrix_paths[key].stat().st_size,
            "sha256": sha256(matrix_paths[key]),
        }
        for key in ("p", "q")
    },
    "construction_seconds": construction_seconds,
    "determinant_seconds": determinant_seconds,
    "matrix_save_seconds": matrix_save_seconds,
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": sha256(source_path),
}
output_path = Path(args.output).resolve()
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "stage": output["stage"],
    "global_matrix_sha256": output["global_matrix_sha256"],
    "prefix_determinants": output["prefix_determinants"],
    "prefix_gcd": output["global_prefix_determinant_gcd_with_N"],
    "elapsed_seconds": output["elapsed_seconds"],
}, sort_keys=True), flush=True)
