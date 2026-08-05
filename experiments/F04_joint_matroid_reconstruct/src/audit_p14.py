#!/usr/bin/env python3
"""Independent P14 formula and pure-Python elimination audit."""

import argparse
from array import array
import hashlib
import json
import math
import os
from pathlib import Path
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--matrix", required=True)
args = parser.parse_args()
N, r, A = 79403, 269, 266
p, q = 271, 293
matrix_path = Path(args.matrix)
raw = matrix_path.read_bytes()
values = array("Q")
values.frombytes(raw)
if sys.byteorder != "little":
    values.byteswap()
global_rows = [list(values[i * r:(i + 1) * r]) for i in range(A)]


def formula_271(a):
    row = [0] * r
    for k in range(23):
        coefficient = math.comb(22, k) * pow(a, 22 - k, p) % p
        row[2 * k + 4] = (row[2 * k + 4] + coefficient) % p
        row[2 * k] = (row[2 * k] + a * coefficient) % p
    row[48] = (row[48] - 1) % p
    row[0] = (row[0] - a) % p
    return row


def formula_293(a):
    row = [0] * r
    for k in range(272):
        column = 24 * k % r
        coefficient = math.comb(271, k) * pow(a, 271 - k, q) % q
        row[column] = (row[column] + coefficient) % q
    row[48] = (row[48] - 1) % q
    row[0] = (row[0] - a) % q
    return row


formula_matches = {
    str(p): all(
        formula_271(a) == [entry % p for entry in global_rows[a - 1]]
        for a in range(1, A + 1)
    ),
    str(q): all(
        formula_293(a) == [entry % q for entry in global_rows[a - 1]]
        for a in range(1, A + 1)
    ),
}


def eliminate(rows, modulus):
    work = [row[:] for row in rows]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    determinant = 1 if row_count == column_count else None
    for column in range(column_count):
        pivot = next(
            (index for index in range(pivot_row, row_count) if work[index][column]),
            None,
        )
        if pivot is None:
            if determinant is not None:
                determinant = 0
            continue
        if pivot != pivot_row:
            work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
            if determinant is not None:
                determinant = -determinant % modulus
        pivot_value = work[pivot_row][column]
        if determinant is not None:
            determinant = determinant * pivot_value % modulus
        inverse = pow(pivot_value, -1, modulus)
        pivot_entries = work[pivot_row]
        for target in range(pivot_row + 1, row_count):
            target_entries = work[target]
            if target_entries[column]:
                factor = target_entries[column] * inverse % modulus
                target_entries[column] = 0
                for j in range(column + 1, column_count):
                    target_entries[j] = (
                        target_entries[j] - factor * pivot_entries[j]
                    ) % modulus
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row, determinant


local = {}
for prime in (p, q):
    reduced = [[entry % prime for entry in row] for row in global_rows]
    base_rank, base_determinant = eliminate(
        [row[:A] for row in reduced], prime
    )
    full_rank, _ = eliminate(reduced, prime)
    local[str(prime)] = {
        "base_rank": base_rank,
        "full_rank": full_rank,
        "base_determinant": base_determinant,
    }

payload = {
    "schema": 1,
    "global_matrix_sha256": hashlib.sha256(raw).hexdigest(),
    "formula_matches_every_entry": formula_matches,
    "local": local,
}
run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
(run_dir / "p14_independent_audit.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(payload, sort_keys=True))
