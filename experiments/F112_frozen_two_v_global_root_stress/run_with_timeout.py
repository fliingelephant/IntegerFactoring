#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stress_frozen_two_v.py"
ATTEMPT = HERE / "OUTPUT_ATTEMPT.json"
OUTPUT = HERE / "OUTPUT.json"
LOG = HERE / "RUN.log"
TIMEOUT_SECONDS = 1800


def main() -> int:
    command = [
        sys.executable,
        str(SOURCE),
        "--workers",
        "4",
        "--checkpoint",
        str(ATTEMPT),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=HERE.parents[1],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        failed_log = HERE / f"RUN_FAILED_{stamp}_TIMEOUT.log"
        failed_log.write_text(
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\nstatus=TIMEOUT\n"
            + (error.stdout or "")
            + (error.stderr or "")
        )
        if ATTEMPT.exists():
            ATTEMPT.replace(HERE / f"OUTPUT_FAILED_{stamp}_TIMEOUT.json")
        return 124
    log_text = (
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"returncode={completed.returncode}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    if completed.returncode != 0:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (HERE / f"RUN_FAILED_{stamp}_EXIT_{completed.returncode}.log").write_text(log_text)
        if ATTEMPT.exists():
            ATTEMPT.replace(HERE / f"OUTPUT_FAILED_{stamp}_EXIT_{completed.returncode}.json")
        return completed.returncode
    parsed = json.loads(ATTEMPT.read_text())
    if parsed.get("status") != "PASS":
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (HERE / f"RUN_FAILED_{stamp}_CLAIM.log").write_text(log_text)
        ATTEMPT.replace(HERE / f"OUTPUT_FAILED_{stamp}_CLAIM.json")
        return 1
    LOG.write_text(log_text)
    ATTEMPT.replace(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
