#!/usr/bin/env python3
"""Run the full nonadaptive all-seed-pair menu on the seven F112 n=46 nulls."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import importlib.util
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
F110_SOURCE = ROOT / "experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py"
EXPECTED_F110_SHA256 = "2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131"
CASES = [
    (5_000_111, 9_999_931),
    (5_000_251, 9_999_823),
    (5_000_339, 9_999_667),
    (5_000_389, 9_999_653),
    (5_000_503, 9_999_511),
    (5_000_473, 9_999_593),
    (5_000_543, 9_999_463),
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(F110_SOURCE) == EXPECTED_F110_SHA256
SPEC = importlib.util.spec_from_file_location("f113_pinned_f110", F110_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned F110 source")
F110 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F110)


def compact_case(pair: tuple[int, int]) -> dict[str, object]:
    result = F110.run_case(*pair)
    provenance = result.get("dependency_provenance")
    if provenance is not None:
        result["dependency_provenance"] = {
            key: value
            for key, value in provenance.items()
            if key != "relation_indices_zero_based"
        }
    result["elapsed_seconds_worker"] = result.pop("elapsed_seconds", None)
    return result


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
                str(F110_SOURCE.relative_to(ROOT)): sha256_file(F110_SOURCE),
            },
            "cases": sorted(completed, key=lambda row: row["N"]),
            "elapsed_seconds": time.monotonic() - started,
        }
        temporary = args.checkpoint.with_suffix(args.checkpoint.suffix + ".tmp")
        temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        temporary.replace(args.checkpoint)

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(compact_case, pair) for pair in CASES]
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
            str(F110_SOURCE.relative_to(ROOT)): sha256_file(F110_SOURCE),
        },
        "factor_cases": sum(row["status"] == "factor" for row in completed),
        "null_cases": [row["N"] for row in completed if row["status"] != "factor"],
        "all_successful_pairs_leave_two_v_prefix": all(
            row["successful_pair"] is None or row["successful_pair"][0] > 2
            for row in completed
        ),
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
