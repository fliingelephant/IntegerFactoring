#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "replay_public_certificate.py"
OUTPUT = HERE / "OUTPUT.json"
LOG = HERE / "RUN.log"
TIMEOUT_SECONDS = 120


def main() -> int:
    command = [sys.executable, str(SOURCE)]
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
        (HERE / f"RUN_FAILED_{stamp}_TIMEOUT.log").write_text(
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\nstatus=TIMEOUT\n"
            + (error.stdout or "")
            + (error.stderr or "")
        )
        return 124
    log_text = (
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"returncode={completed.returncode}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    if completed.returncode != 0:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (HERE / f"RUN_FAILED_{stamp}_EXIT_{completed.returncode}.log").write_text(log_text)
        return completed.returncode
    parsed = json.loads(completed.stdout)
    if parsed.get("status") != "PASS":
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (HERE / f"RUN_FAILED_{stamp}_CLAIM.log").write_text(log_text)
        return 1
    LOG.write_text(log_text)
    OUTPUT.write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
