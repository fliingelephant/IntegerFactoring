#!/usr/bin/env python3
"""Run the pinned F116 sparse-DAG discovery on one registered corpus case."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PINNED_SOURCE = HERE / "stress_sparse_dag_first_case.py"
EXPECTED_PINNED_SHA256 = "7a65e664d9cdca422da47a5d26bd22432ce2eee5c61f8b3db5541bd348e81b84"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ordinal", type=int, required=True)
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source_hash = hashlib.sha256(PINNED_SOURCE.read_bytes()).hexdigest()
    assert source_hash == EXPECTED_PINNED_SHA256
    spec = importlib.util.spec_from_file_location("f116_pinned_sparse_case", PINNED_SOURCE)
    assert spec is not None and spec.loader is not None
    candidate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(candidate)
    candidate.P = args.p
    candidate.Q = args.q
    candidate.N = args.p * args.q

    original_argv = sys.argv
    try:
        sys.argv = [str(PINNED_SOURCE), "--output", str(args.output)]
        candidate.main()
    finally:
        sys.argv = original_argv

    result = json.loads(args.output.read_text())
    assert result["status"] == "PASS"
    assert result["case"]["p"] == args.p
    assert result["case"]["q"] == args.q
    result["case"]["ordinal"] = args.ordinal
    result["registered_case_wrapper"] = {
        "pinned_source": str(PINNED_SOURCE.name),
        "pinned_source_sha256": source_hash,
        "changes_to_pinned_algorithm": "only P, Q, N, and corpus ordinal",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
