#!/usr/bin/env python3
"""Run the isolated first F116 case with a hard timeout."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "replay_first_case_sage.py"
OUTPUT = HERE / "SINGLE_CASE_OUTPUT.json"
LOG = HERE / "SINGLE_CASE_RUN.log"
TIMEOUT_SECONDS = 300


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    attempt = HERE / f"SINGLE_CASE_ATTEMPT_{stamp}.json"
    command = ["/usr/local/bin/sage", "-python", str(SOURCE), "--output", str(attempt)]
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
        elapsed = time.monotonic() - started
    except subprocess.TimeoutExpired as error:
        elapsed = time.monotonic() - started
        failed_output = HERE / f"SINGLE_CASE_OUTPUT_FAILED_{stamp}_TIMEOUT.json"
        failed_log = HERE / f"SINGLE_CASE_RUN_FAILED_{stamp}_TIMEOUT.log"
        failed_output.write_text(
            attempt.read_text() if attempt.exists() else json.dumps({"status": "TIMEOUT"}) + "\n"
        )
        failed_log.write_text(
            f"command={json.dumps(command)}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed:.6f}\n"
            "timed_out=true\n"
            f"stdout:\n{error.stdout or ''}\n"
            f"stderr:\n{error.stderr or ''}\n"
        )
        return 124

    log_text = (
        f"command={json.dumps(command)}\n"
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed:.6f}\n"
        "timed_out=false\n"
        f"returncode={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}\n"
    )
    if completed.returncode != 0 or not attempt.exists():
        failed_output = HERE / f"SINGLE_CASE_OUTPUT_FAILED_{stamp}_EXIT_{completed.returncode}.json"
        failed_log = HERE / f"SINGLE_CASE_RUN_FAILED_{stamp}_EXIT_{completed.returncode}.log"
        failed_output.write_text(
            attempt.read_text() if attempt.exists() else json.dumps({"status": "NO_OUTPUT"}) + "\n"
        )
        failed_log.write_text(log_text)
        return completed.returncode or 1
    parsed = json.loads(attempt.read_text())
    if parsed.get("status") != "PASS":
        failed_output = HERE / f"SINGLE_CASE_OUTPUT_FAILED_{stamp}_CLAIM.json"
        failed_log = HERE / f"SINGLE_CASE_RUN_FAILED_{stamp}_CLAIM.log"
        attempt.replace(failed_output)
        failed_log.write_text(log_text)
        return 1
    attempt.replace(OUTPUT)
    LOG.write_text(log_text)
    print(f"verdict=PASS elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
