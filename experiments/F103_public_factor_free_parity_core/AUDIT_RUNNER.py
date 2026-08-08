#!/usr/bin/env python3
"""Named hard-timeout runner for the independent F103 audit."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "AUDIT_OUTPUT.json"
LOG = BASE / "AUDIT_RUN.log"
TIMEOUT_SECONDS = 240
COMMAND = [
    sys.executable,
    str(BASE / "AUDIT_VERIFY.py"),
    "--candidate-dir",
    str(BASE),
    "--f98-source",
    str(BASE.parent / "F98_multiseed_presentation_closure_kill" / "public_factorization_free_replay.py"),
    "--f102-output",
    str(BASE.parent / "F102_f98_full_parity_core" / "OUTPUT.json"),
    "--output",
    str(OUTPUT),
]


started = time.monotonic()
timed_out = False
try:
    completed = subprocess.run(
        COMMAND,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    exit_code = completed.returncode
    stdout = completed.stdout
    stderr = completed.stderr
except subprocess.TimeoutExpired as error:
    timed_out = True
    exit_code = 124
    stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else error.stdout or ""
    stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else error.stderr or ""
    timeout_output = {
        "status": "FAIL",
        "failures": [f"hard timeout after {TIMEOUT_SECONDS} seconds"],
    }
    OUTPUT.write_text(json.dumps(timeout_output, indent=2, sort_keys=True) + "\n", encoding="utf-8")

elapsed = time.monotonic() - started
log_text = (
    f"timeout_seconds={TIMEOUT_SECONDS}\n"
    + "command="
    + " ".join(COMMAND)
    + "\n"
    + f"elapsed_seconds={elapsed:.6f}\n"
    + f"timed_out={str(timed_out).lower()}\n"
    + f"exit_code={exit_code}\n"
    + "stdout:\n"
    + stdout
    + "stderr:\n"
    + stderr
)
LOG.write_text(log_text, encoding="utf-8")

if exit_code != 0:
    stamp = time.strftime("%Y%m%dT%H%M%S")
    shutil.copy2(LOG, BASE / f"AUDIT_FAILED_{stamp}.log")
    if OUTPUT.exists():
        shutil.copy2(OUTPUT, BASE / f"AUDIT_FAILED_{stamp}.json")

raise SystemExit(exit_code)
