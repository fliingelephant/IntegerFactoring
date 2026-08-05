#!/usr/bin/env sage
"""Solve the exact P11 11-column tail against one retained prefix basis."""

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
EXPECTED_DETERMINANTS = {int(P): 56136614, int(Q): 132391112}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def matrix_hash(input_matrix):
    digest = hashlib.sha256()
    for row_index in range(input_matrix.nrows()):
        encoded = json.dumps(
            [int(value) for value in input_matrix[row_index]],
            separators=(",", ":"),
        ).encode("ascii")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--matrix", required=True)
parser.add_argument("--characteristic", type=int, choices=sorted(EXPECTED_DETERMINANTS), required=True)
parser.add_argument("--normalized", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
matrix_path = Path(args.matrix).resolve()
normalized_path = Path(args.normalized).resolve()
print(f"stage=load characteristic={args.characteristic}", flush=True)
local_matrix = load(str(matrix_path))
assert local_matrix.dimensions() == (A, R)
assert int(local_matrix.base_ring().characteristic()) == args.characteristic
prefix = local_matrix.matrix_from_columns(range(A))
tail = local_matrix.matrix_from_columns(range(A, R))

determinant_started = time.monotonic()
prefix_determinant = int(prefix.det())
determinant_seconds = time.monotonic() - determinant_started
assert prefix_determinant == EXPECTED_DETERMINANTS[args.characteristic]
print(
    f"stage=determinant characteristic={args.characteristic} value={prefix_determinant}",
    flush=True,
)

solve_started = time.monotonic()
normalized = prefix._solve_right_nonsingular_square(tail, check_rank=False)
solve_seconds = time.monotonic() - solve_started
print(
    f"stage=solve characteristic={args.characteristic} seconds={solve_seconds}",
    flush=True,
)

verification_started = time.monotonic()
assert prefix * normalized == tail
verification_seconds = time.monotonic() - verification_started
zero_positions = [
    [row_index, tail_index]
    for row_index in range(A)
    for tail_index in range(R - A)
    if not normalized[row_index, tail_index]
]
normalized_sha256 = matrix_hash(normalized)
normalized_path.parent.mkdir(parents=True, exist_ok=True)
save_started = time.monotonic()
save(normalized, str(normalized_path), compress=False)
save_seconds = time.monotonic() - save_started
assert normalized_path.exists()

source_path = Path(__file__).resolve()
output = {
    "approach_family": "F04_joint_matroid_audit",
    "stage": "P11-exact-tail-solve-v1",
    "inputs": {
        "N": int(N),
        "characteristic": args.characteristic,
        "matrix_shape": [A, R],
        "basis_columns": [0, A - 1],
        "tail_columns": [A, R - 1],
    },
    "matrix_artifact": {
        "path": str(matrix_path),
        "bytes": matrix_path.stat().st_size,
        "sha256": sha256(matrix_path),
    },
    "prefix_determinant": prefix_determinant,
    "normalized_shape": [A, R - A],
    "normalization": "C_l = B_l^(-1) T_l, solved exactly by row reduction of [B_l|T_l] with the already-certified nonsingular prefix",
    "exact_product_verification": True,
    "normalized_entry_sha256": normalized_sha256,
    "normalized_zero_positions": zero_positions,
    "normalized_artifact": {
        "path": str(normalized_path),
        "bytes": normalized_path.stat().st_size,
        "sha256": sha256(normalized_path),
    },
    "determinant_seconds": determinant_seconds,
    "solve_seconds": solve_seconds,
    "product_verification_seconds": verification_seconds,
    "save_seconds": save_seconds,
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
    "characteristic": args.characteristic,
    "normalized_entry_sha256": normalized_sha256,
    "normalized_zero_count": len(zero_positions),
    "elapsed_seconds": output["elapsed_seconds"],
}, sort_keys=True, default=int), flush=True)
