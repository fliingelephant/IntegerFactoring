#!/usr/bin/env python3
"""Extract the four generalized-Cramer entries for the mandatory exchange."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import struct


parser = argparse.ArgumentParser()
parser.add_argument("--p-solution", required=True)
parser.add_argument("--q-solution", required=True)
args = parser.parse_args()
A, tail_count = 2942, 11
removed, tails = (423, 2336), (2, 6)


def extract(path, prime):
    raw = Path(path).read_bytes()
    values = struct.unpack(f"<{len(raw) // 8}Q", raw)
    block = [[values[i * tail_count + j] for j in tails] for i in removed]
    determinant = (
        block[0][0] * block[1][1] - block[0][1] * block[1][0]
    ) % prime
    return {
        "block": block,
        "determinant": determinant,
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


payload = {
    "schema": 1,
    "removed_base_columns": list(removed),
    "tail_offsets": list(tails),
    "100000007": extract(args.p_solution, 100000007),
    "199999991": extract(args.q_solution, 199999991),
}
run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
(run_dir / "exchange_blocks.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(payload, sort_keys=True))
