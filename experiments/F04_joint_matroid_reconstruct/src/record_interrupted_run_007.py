#!/usr/bin/env python3
"""Attach a manifest to the deliberately interrupted generic-Sage run 007."""

import hashlib
import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
target = root / "runs" / "007_analyze_P11_local"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


files = {}
for path in (
    target / "stdout.log",
    target / "stderr.log",
    root / "src" / "analyze_local.py",
    root / "runs" / "005_generate_P11_global" / "global_matrix_u64le.bin",
):
    files[str(path.relative_to(root))] = {
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }

manifest = {
    "schema": 1,
    "name": "007_analyze_P11_local",
    "command": [
        "sage",
        "-python",
        "src/analyze_local.py",
        "--matrix",
        "runs/005_generate_P11_global/global_matrix_u64le.bin",
        "--N",
        "20000000499999937",
        "--r",
        "2953",
        "--A",
        "2942",
        "--p",
        "100000007",
        "--q",
        "199999991",
        "--mode",
        "p11",
    ],
    "timeout_seconds": 1800,
    "timed_out": False,
    "interrupted": True,
    "return_code": 130,
    "reason": (
        "Operator interrupted the generic Sage matrix backend after it made no "
        "progress output for over 14 minutes; exact child PIDs 88221 and 88223 "
        "were then terminated before the FLINT nmod replacement run."
    ),
    "files": files,
}
(target / "manifest.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(manifest, sort_keys=True))
