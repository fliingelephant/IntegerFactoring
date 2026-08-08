#!/usr/bin/env python3
"""Run AUDIT_VERIFY.py with a hard timeout and preserve its evidence."""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import subprocess
import sys
import time


TIMEOUT_SECONDS = 120
HERE = pathlib.Path(__file__).resolve().parent
COMMAND = [sys.executable, str(HERE / "AUDIT_VERIFY.py")]
started = time.monotonic()
timestamp = dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")

try:
    completed = subprocess.run(
        COMMAND,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
except subprocess.TimeoutExpired as error:
    elapsed = time.monotonic() - started
    failure = {
        "status": "TIMEOUT",
        "timeout_seconds": TIMEOUT_SECONDS,
        "elapsed_seconds": elapsed,
        "stdout": error.stdout or "",
        "stderr": error.stderr or "",
    }
    path = HERE / f"AUDIT_FAILED_{timestamp}.json"
    path.write_text(json.dumps(failure, indent=2, sort_keys=True) + "\n")
    raise SystemExit(f"audit timed out; preserved {path.name}")

elapsed = time.monotonic() - started
log = {
    "command": COMMAND,
    "timeout_seconds": TIMEOUT_SECONDS,
    "elapsed_seconds": elapsed,
    "exit_code": completed.returncode,
    "stderr": completed.stderr,
}
(HERE / "AUDIT_RUN.log").write_text(json.dumps(log, indent=2, sort_keys=True) + "\n")

if completed.returncode != 0:
    failure_path = HERE / f"AUDIT_FAILED_{timestamp}.log"
    failure_path.write_text(completed.stdout + completed.stderr)
    raise SystemExit(f"audit failed; preserved {failure_path.name}")

try:
    output = json.loads(completed.stdout)
except json.JSONDecodeError:
    failure_path = HERE / f"AUDIT_FAILED_{timestamp}.log"
    failure_path.write_text(completed.stdout + completed.stderr)
    raise SystemExit(f"audit emitted invalid JSON; preserved {failure_path.name}")

(HERE / "AUDIT_OUTPUT.json").write_text(
    json.dumps(output, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({"status": output["status"], **log}, indent=2, sort_keys=True))
