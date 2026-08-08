#!/usr/bin/env python3
"""Hard-timeout runner for the amended F108/F99 boundary replay."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path


directory = Path(__file__).resolve().parent
attempt_output = directory / "RECONSTRUCTION_REAUDIT_ATTEMPT_OUTPUT.json"
attempt_log = directory / "RECONSTRUCTION_REAUDIT_ATTEMPT_RUN.log"
command = [
    "/opt/homebrew/bin/python3",
    str(directory / "reconstruction_reaudit_f99_verifier.py"),
    "--statement",
    "RECONSTRUCT_STATEMENT.md",
    "--output",
    attempt_output.name,
]
timeout_seconds = 30
started = time.monotonic()
timed_out = False
try:
    completed = subprocess.run(
        command,
        cwd=directory,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    exit_code = completed.returncode
    stdout = completed.stdout
    stderr = completed.stderr
except subprocess.TimeoutExpired as error:
    timed_out = True
    exit_code = 124
    stdout = error.stdout or ""
    stderr = error.stderr or ""
elapsed = time.monotonic() - started
attempt_log.write_text(
    f"command={command!r}\n"
    f"working_directory={str(directory)!r}\n"
    f"timeout_seconds={timeout_seconds}\n"
    f"elapsed_seconds={elapsed:.6f}\n"
    f"timed_out={str(timed_out).lower()}\n"
    f"exit_code={exit_code}\n"
    f"stdout:\n{stdout}\n"
    f"stderr:\n{stderr}\n"
)

verifier_status = "MISSING_OUTPUT"
boundary_verdict = "UNKNOWN"
if attempt_output.is_file():
    try:
        payload = json.loads(attempt_output.read_text())
        verifier_status = payload.get("verifier_status", "MISSING_STATUS")
        boundary_verdict = payload.get("boundary_verdict", "UNKNOWN")
    except (json.JSONDecodeError, OSError):
        verifier_status = "INVALID_OUTPUT"

success = exit_code == 0 and not timed_out and verifier_status == "PASS"
if success:
    attempt_output.replace(directory / "RECONSTRUCTION_REAUDIT_OUTPUT.json")
    attempt_log.replace(directory / "RECONSTRUCTION_REAUDIT_RUN.log")
    print(f"verifier_status={verifier_status}")
    print(f"boundary_verdict={boundary_verdict}")
    sys.exit(0)

stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
reason = "TIMEOUT" if timed_out else verifier_status.replace(" ", "_").upper()
failed_output = directory / f"RECONSTRUCTION_REAUDIT_FAILED_{stamp}_{reason}.json"
failed_log = directory / f"RECONSTRUCTION_REAUDIT_FAILED_{stamp}_{reason}.log"
if attempt_output.is_file():
    attempt_output.replace(failed_output)
else:
    failed_output.write_text(json.dumps({
        "boundary_verdict": boundary_verdict,
        "exit_code": exit_code,
        "status": "failed narrow reconstruction attempt",
        "timed_out": timed_out,
        "verifier_status": verifier_status,
    }, indent=2, sort_keys=True) + "\n")
attempt_log.replace(failed_log)
print(f"preserved_failed_output={failed_output.name}")
print(f"preserved_failed_log={failed_log.name}")
sys.exit(exit_code if exit_code else 1)
