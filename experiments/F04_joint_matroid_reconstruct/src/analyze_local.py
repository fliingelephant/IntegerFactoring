#!/usr/bin/env python3
"""Reduce a previously formed global matrix and compute local certificates."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from sage.all import GF, matrix


parser = argparse.ArgumentParser()
parser.add_argument("--matrix", required=True)
parser.add_argument("--N", required=True, type=int)
parser.add_argument("--r", required=True, type=int)
parser.add_argument("--A", required=True, type=int)
parser.add_argument("--p", required=True, type=int)
parser.add_argument("--q", required=True, type=int)
parser.add_argument("--mode", choices=("p14", "p11"), required=True)
args = parser.parse_args()

run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
matrix_path = Path(args.matrix).resolve()
N, r, A = args.N, args.r, args.A
assert args.p * args.q == N
assert matrix_path.stat().st_size == A * r * 8

digest = hashlib.sha256()
with matrix_path.open("rb") as stream:
    for block in iter(lambda: stream.read(1 << 20), b""):
        digest.update(block)

global_matrix = np.memmap(matrix_path, dtype="<u8", mode="r", shape=(A, r))
assert bool(np.all(global_matrix < N))


def crt_pair(x, p, y, q):
    return (x + p * (((y - x) * pow(p, -1, q)) % q)) % (p * q)


local_results = {}
solutions = {}
for prime_name, prime in (("p", args.p), ("q", args.q)):
    phase_started = time.monotonic()
    reduced = np.remainder(global_matrix, prime).astype(np.int64)
    field = GF(prime)
    base = matrix(field, reduced[:, :A].tolist())
    determinant = int(base.det())
    result = {
        "prime": prime,
        "base_determinant": determinant,
        "base_rank": int(base.rank()),
        "matrix_class": str(type(base)),
    }
    if args.mode == "p14":
        full = matrix(field, reduced.tolist())
        result["full_rank"] = int(full.rank())
    else:
        tail = matrix(field, reduced[:, A:r].tolist())
        solution = base.solve_right(tail)
        assert base * solution == tail
        solution_entries = np.array(
            [[int(solution[i, j]) for j in range(r - A)] for i in range(A)],
            dtype=np.uint64,
        )
        solution_path = run_dir / f"base_inverse_tail_{prime}.u64le.bin"
        solution_entries.astype("<u8", copy=False).tofile(solution_path)
        solutions[prime_name] = solution_entries

        removed = (423, 2336)
        tails = (2, 6)
        exchange_2_by_2 = matrix(
            field,
            [[solution[i, j] for j in tails] for i in removed],
        )
        exchange_factor = int(exchange_2_by_2.det())
        in_place_to_sorted_swaps = sum(A - 2 + s - i for s, i in enumerate(removed))
        sign = -1 if in_place_to_sorted_swaps % 2 else 1
        exchanged_determinant = (sign * determinant * exchange_factor) % prime
        result.update(
            {
                "tail_columns": list(range(A, r)),
                "exchange_removed_base_columns": list(removed),
                "exchange_tail_offsets": list(tails),
                "exchange_global_tail_columns": [A + j for j in tails],
                "in_place_to_sorted_swaps": in_place_to_sorted_swaps,
                "exchange_sign": sign,
                "exchange_factor": exchange_factor,
                "exchanged_determinant": exchanged_determinant,
                "solution_sha256": hashlib.sha256(solution_path.read_bytes()).hexdigest(),
            }
        )
    result["elapsed_seconds"] = time.monotonic() - phase_started
    local_results[prime_name] = result
    print(json.dumps({prime_name: result}, sort_keys=True), flush=True)

base_crt = crt_pair(
    local_results["p"]["base_determinant"],
    args.p,
    local_results["q"]["base_determinant"],
    args.q,
)
summary = {
    "schema": 1,
    "global_matrix": str(matrix_path),
    "global_matrix_sha256": digest.hexdigest(),
    "N": N,
    "r": r,
    "A": A,
    "local": local_results,
    "base_determinant_crt": base_crt,
    "base_determinant_gcd_N": math.gcd(base_crt, N),
}
if args.mode == "p11":
    exchange_crt = crt_pair(
        local_results["p"]["exchanged_determinant"],
        args.p,
        local_results["q"]["exchanged_determinant"],
        args.q,
    )
    summary.update(
        {
            "exchanged_determinant_crt": exchange_crt,
            "exchanged_determinant_gcd_N": math.gcd(exchange_crt, N),
        }
    )

(run_dir / "local_analysis.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(summary, sort_keys=True), flush=True)
