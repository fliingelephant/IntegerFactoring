#!/usr/bin/env python3
"""Named hard-timeout runner that preserves every failed F106 audit attempt."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path


BASE = Path(__file__).resolve().parent
ATTEMPT_OUTPUT = BASE / "AUDIT_ATTEMPT_OUTPUT.json"
ATTEMPT_LOG = BASE / "AUDIT_ATTEMPT_RUN.log"
OUTPUT = BASE / "AUDIT_OUTPUT.json"
LOG = BASE / "AUDIT_RUN.log"
TIMEOUT_SECONDS = 60
COMMAND = [
    sys.executable,
    str(BASE / "audit_independent_verifier.py"),
    "--candidate-dir",
    str(BASE),
    "--f98",
    str(BASE.parent / "F98_multiseed_presentation_closure_kill" / "PUBLIC_REPLAY_OUTPUT.json"),
    "--f100",
    str(BASE.parent / "F100_f98_dependency_structure" / "OUTPUT.json"),
    "--output",
    str(ATTEMPT_OUTPUT),
]


for stale_attempt in (ATTEMPT_OUTPUT, ATTEMPT_LOG):
    if stale_attempt.exists():
        stamp = time.strftime("%Y%m%dT%H%M%S") + f"_{time.time_ns() % 1_000_000_000:09d}"
        os.replace(stale_attempt, BASE / f"AUDIT_FAILED_STALE_{stamp}_{stale_attempt.name}")

started = time.monotonic()
timed_out = False
try:
    completed = subprocess.run(
        COMMAND,
        cwd=BASE,
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
    ATTEMPT_OUTPUT.write_text(
        json.dumps(
            {
                "status": "failed",
                "verifier_status": "FAIL",
                "failures": [f"hard timeout after {TIMEOUT_SECONDS} seconds"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

elapsed = time.monotonic() - started
ATTEMPT_LOG.write_text(
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
    + stderr,
    encoding="utf-8",
)

if exit_code == 0:
    os.replace(ATTEMPT_OUTPUT, OUTPUT)
    os.replace(ATTEMPT_LOG, LOG)
else:
    stamp = time.strftime("%Y%m%dT%H%M%S") + f"_{time.time_ns() % 1_000_000_000:09d}"
    if ATTEMPT_OUTPUT.exists():
        os.replace(ATTEMPT_OUTPUT, BASE / f"AUDIT_FAILED_{stamp}.json")
    os.replace(ATTEMPT_LOG, BASE / f"AUDIT_FAILED_{stamp}.log")

raise SystemExit(exit_code)
