#!/usr/bin/env sage
"""Certify both matrices retained by the A03 post-save serialization failure."""

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
EXPECTED_GLOBAL_HASH = "85c4bcda5ff5d0f23117721a503fedb77e3a84b9d708a3ceb0f7bed1673c6f53"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--p-matrix", required=True)
parser.add_argument("--q-matrix", required=True)
parser.add_argument("--producer-source", required=True)
parser.add_argument("--producer-status", required=True)
parser.add_argument("--producer-log", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
paths = {
    "p": Path(args.p_matrix).resolve(),
    "q": Path(args.q_matrix).resolve(),
    "producer_source": Path(args.producer_source).resolve(),
    "producer_status": Path(args.producer_status).resolve(),
    "producer_log": Path(args.producer_log).resolve(),
}
producer_status = json.loads(paths["producer_status"].read_text())
producer_log = paths["producer_log"].read_text()
assert producer_status["run_id"] == "A03"
assert producer_status["disposition"] == "failed"
assert producer_status["exit_code"] == 1
assert not producer_status["timed_out"]
assert "stage=matrix-save field=p" in producer_log
assert "stage=matrix-save field=q" in producer_log
assert "TypeError: Object of type Integer is not JSON serializable" in producer_log

print("stage=load-both-retained-matrices", flush=True)
local_matrices = {"p": load(str(paths["p"])), "q": load(str(paths["q"]))}
assert local_matrices["p"].dimensions() == (A, R)
assert local_matrices["q"].dimensions() == (A, R)
assert int(local_matrices["p"].base_ring().characteristic()) == int(P)
assert int(local_matrices["q"].base_ring().characteristic()) == int(Q)

crt_started = time.monotonic()
p_integer = int(P)
q_integer = int(Q)
p_inverse_mod_q = pow(p_integer, -1, q_integer)
global_matrix_hash = hashlib.sha256()
global_row_hashes = []
raw_local_zero_counts = {"p": 0, "q": 0}
raw_global_nonunit_count = 0
for row_index in range(A):
    p_row = [int(value) for value in local_matrices["p"][row_index]]
    q_row = [int(value) for value in local_matrices["q"][row_index]]
    coefficients = [
        left + p_integer * (((right - left) * p_inverse_mod_q) % q_integer)
        for left, right in zip(p_row, q_row)
    ]
    encoded = json.dumps(coefficients, separators=(",", ":")).encode("ascii")
    global_row_hashes.append(hashlib.sha256(encoded).hexdigest())
    global_matrix_hash.update(len(encoded).to_bytes(8, "big"))
    global_matrix_hash.update(encoded)
    p_zeros = sum(value == 0 for value in p_row)
    q_zeros = sum(value == 0 for value in q_row)
    raw_local_zero_counts["p"] += p_zeros
    raw_local_zero_counts["q"] += q_zeros
    raw_global_nonunit_count += sum(
        left == 0 or right == 0 for left, right in zip(p_row, q_row)
    )
    if (row_index + 1) % 200 == 0 or row_index + 1 == A:
        print(f"stage=crt-rehash rows={row_index + 1}/{A}", flush=True)
crt_rehash_seconds = time.monotonic() - crt_started
assert global_matrix_hash.hexdigest() == EXPECTED_GLOBAL_HASH

prefix_determinants = {}
determinant_seconds = {}
for key in ("p", "q"):
    determinant_started = time.monotonic()
    prefix_determinants[key] = int(
        local_matrices[key].matrix_from_columns(range(A)).det()
    )
    determinant_seconds[key] = time.monotonic() - determinant_started
    print(
        f"stage=prefix-determinant field={key} value={prefix_determinants[key]}",
        flush=True,
    )
assert prefix_determinants == {"p": 56136614, "q": 132391112}
assert raw_local_zero_counts == {"p": 0, "q": 0}
assert raw_global_nonunit_count == 0

prefix_crt = int(crt(ZZ(prefix_determinants["p"]), ZZ(prefix_determinants["q"]), P, Q))
source_path = Path(__file__).resolve()
output = {
    "approach_family": "F04_joint_matroid_audit",
    "stage": "P11-joint-build-recovery-certificate-v1",
    "inputs": {
        "N": int(N),
        "p": int(P),
        "q": int(Q),
        "r": int(R),
        "shift_start": 1,
        "shift_stop": int(A),
    },
    "producer_disposition": {
        "run_id": "A03",
        "disposition": "failed after both matrix saves during final JSON serialization",
        "mathematical_computation_failure": False,
        "producer_source": str(paths["producer_source"]),
        "producer_source_sha256": sha256(paths["producer_source"]),
        "producer_status": str(paths["producer_status"]),
        "producer_status_sha256": sha256(paths["producer_status"]),
        "producer_log": str(paths["producer_log"]),
        "producer_log_sha256": sha256(paths["producer_log"]),
    },
    "joint_global_construction_in_producer": "each H_a was formed once over Z/NZ and the same coefficient vector assigned to both retained local matrices before any local solve",
    "recovery_verification": "every global coefficient was independently reconstructed from the two retained local entries by CRT before row and aggregate hashing",
    "matrix_shape": [int(A), int(R)],
    "global_matrix_sha256": global_matrix_hash.hexdigest(),
    "global_row_sha256": global_row_hashes,
    "raw_global_nonunit_count": int(raw_global_nonunit_count),
    "raw_local_zero_counts": raw_local_zero_counts,
    "prefix_determinants": prefix_determinants,
    "prefix_determinant_nonzero_both": True,
    "local_full_ranks": {"p": int(A), "q": int(A)},
    "lexicographic_column_basis": [0, int(A - 1)],
    "global_prefix_determinant_mod_N_from_CRT": prefix_crt,
    "global_prefix_determinant_gcd_with_N": int(gcd(prefix_crt, N)),
    "matrix_artifacts": {
        key: {
            "path": str(paths[key]),
            "bytes": paths[key].stat().st_size,
            "sha256": sha256(paths[key]),
        }
        for key in ("p", "q")
    },
    "crt_rehash_seconds": crt_rehash_seconds,
    "determinant_seconds": determinant_seconds,
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": sha256(source_path),
}
output_path = Path(args.output).resolve()
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(output, indent=2, sort_keys=True, default=int) + "\n",
    encoding="utf-8",
)
print(json.dumps({
    "stage": output["stage"],
    "global_matrix_sha256": output["global_matrix_sha256"],
    "prefix_determinants": output["prefix_determinants"],
    "prefix_gcd": output["global_prefix_determinant_gcd_with_N"],
    "elapsed_seconds": output["elapsed_seconds"],
}, sort_keys=True, default=int), flush=True)
