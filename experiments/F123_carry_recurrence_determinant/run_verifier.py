#!/usr/bin/env python3
"""Run the preserved F123 verifier with a named timeout and artifacts."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "verify_gct_carry_obstruction.py"
SWEEP_SOURCE = ROOT / "verify_identity_sweep.py"
LOG = ROOT / "RUN.log"
OUTPUT = ROOT / "OUTPUT.json"
TIMEOUT_SECONDS = 60
EXPECTED_SOURCE_SHA256 = (
    "eb18408931a02891b3b7cb27a7e80379f487efc3756fcdff2cc291fc63b9d594"
)


source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert source_hash == EXPECTED_SOURCE_SHA256

completed = subprocess.run(
    [sys.executable, str(SOURCE)],
    cwd=ROOT,
    text=True,
    capture_output=True,
    timeout=TIMEOUT_SECONDS,
    check=False,
)
assert completed.returncode == 0

sweep = subprocess.run(
    [sys.executable, str(SWEEP_SOURCE)],
    cwd=ROOT,
    text=True,
    capture_output=True,
    timeout=TIMEOUT_SECONDS,
    check=False,
)
assert sweep.returncode == 0

log_text = completed.stdout + completed.stderr + sweep.stdout + sweep.stderr
LOG.write_text(log_text, encoding="utf-8")

prefix = "PASS: GCT carry obstruction "
line = completed.stdout.strip()
assert line.startswith(prefix)
certificate = ast.literal_eval(line[len(prefix) :])
identity_sweep = json.loads(sweep.stdout)

OUTPUT.write_text(
    json.dumps(
        {
            "status": "pass",
            "family": "F123",
            "timeout_seconds": TIMEOUT_SECONDS,
            "source_sha256": source_hash,
            "certificate": certificate,
            "identity_sweep": identity_sweep,
        },
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)
