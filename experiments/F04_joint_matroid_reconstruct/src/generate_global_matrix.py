#!/usr/bin/env python3
"""Form M_N over Z/NZ, without accepting or using any factor of N."""

import argparse
import hashlib
import json
import os
from array import array
from pathlib import Path
import sys
import time

from sage.all import Integers, PolynomialRing, power_mod


parser = argparse.ArgumentParser()
parser.add_argument("--N", required=True, type=int)
parser.add_argument("--r", required=True, type=int)
parser.add_argument("--A", required=True, type=int)
args = parser.parse_args()

run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
matrix_path = run_dir / "global_matrix_u64le.bin"
N, r, A = args.N, args.r, args.A

ring = Integers(N)
polynomials = PolynomialRing(ring, "X")
X = polynomials.gen()
modulus = X**r - 1
x_power = power_mod(X, N, modulus)
digest = hashlib.sha256()
started = time.monotonic()

with matrix_path.open("wb") as output:
    for a in range(1, A + 1):
        residue = power_mod(X + a, N, modulus) - x_power - a
        coefficients = array("Q", (int(residue[j]) for j in range(r)))
        if sys.byteorder != "little":
            coefficients.byteswap()
        block = coefficients.tobytes()
        output.write(block)
        digest.update(block)
        if a == 1 or a % 100 == 0 or a == A:
            print(
                json.dumps(
                    {
                        "rows_complete": a,
                        "elapsed_seconds": time.monotonic() - started,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

metadata = {
    "schema": 1,
    "definition": "coefficients of (X+a)^N-X^N-a in (Z/NZ)[X]/(X^r-1)",
    "N": N,
    "r": r,
    "A": A,
    "row_labels": [1, A],
    "column_labels": [0, r - 1],
    "encoding": "row-major unsigned 64-bit little-endian canonical residues",
    "bytes": matrix_path.stat().st_size,
    "sha256": digest.hexdigest(),
    "elapsed_seconds": time.monotonic() - started,
    "factor_inputs": [],
}
(run_dir / "global_matrix.json").write_text(
    json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(metadata, sort_keys=True), flush=True)
