#!/usr/bin/env python3
"""Run F113's all-seed-pair control on the seven F112 n=50 nulls."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import importlib.util
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
F113_SOURCE = ROOT / "experiments/F113_all_seed_pairs_n46_rescue/test_all_seed_pairs.py"
EXPECTED_F113_SHA256 = "c254ba6ec5b8bcc1ce816b60865ae0bce0cd9725aee2bdee1144acd03df290ab"
CASES = [
    (20_000_003, 39_999_983),
    (20_000_047, 39_999_931),
    (20_000_059, 39_999_919),
    (20_000_077, 39_999_901),
    (20_000_159, 39_999_823),
    (20_000_171, 39_999_811),
    (20_000_243, 39_999_779),
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(F113_SOURCE) == EXPECTED_F113_SHA256
SPEC = importlib.util.spec_from_file_location("f114_pinned_f113", F113_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned F113 source")
F113 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F113)


def run_pair(pair: tuple[int, int]) -> dict[str, object]:
    return F113.compact_case(pair)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--checkpoint", type=Path, required=True)
    args = parser.parse_args()
    assert 1 <= args.workers <= 7
    started = time.monotonic()
    completed = []

    def checkpoint(status: str) -> None:
        payload = {
            "status": status,
            "role": "factor-assisted bounded menu control; N-only replay required for positives",
            "case_count": len(CASES),
            "completed_cases": len(completed),
            "pinned_source": {
                str(F113_SOURCE.relative_to(ROOT)): sha256_file(F113_SOURCE),
            },
            "cases": sorted(completed, key=lambda row: row["N"]),
            "elapsed_seconds": time.monotonic() - started,
        }
        temporary = args.checkpoint.with_suffix(args.checkpoint.suffix + ".tmp")
        temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        temporary.replace(args.checkpoint)

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(run_pair, pair) for pair in CASES]
        for future in as_completed(futures):
            completed.append(future.result())
            checkpoint("running")

    completed.sort(key=lambda row: row["N"])
    result = {
        "status": "complete",
        "role": "factor-assisted bounded menu control; N-only replay required for positives",
        "case_count": len(CASES),
        "completed_cases": len(completed),
        "pinned_source": {
            str(F113_SOURCE.relative_to(ROOT)): sha256_file(F113_SOURCE),
        },
        "factor_cases": sum(row["status"] == "factor" for row in completed),
        "null_cases": [row["N"] for row in completed if row["status"] != "factor"],
        "cases": completed,
        "elapsed_seconds": time.monotonic() - started,
    }
    args.checkpoint.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "factor_cases": result["factor_cases"],
        "null_cases": result["null_cases"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
