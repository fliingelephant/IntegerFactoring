#!/usr/bin/env python3
"""Hard-timeout runner for the F116 Sage/Pari retry."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stress_independent_all_pairs_sage.py"
ATTEMPT = HERE / "SAGE_OUTPUT_ATTEMPT.json"
OUTPUT = HERE / "SAGE_OUTPUT.json"
LOG = HERE / "SAGE_RUN.log"
TIMEOUT_SECONDS = 1800


def preserve(label: str, log_text: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (HERE / f"SAGE_RUN_FAILED_{stamp}_{label}.log").write_text(log_text)
    if ATTEMPT.exists():
        ATTEMPT.replace(HERE / f"SAGE_OUTPUT_FAILED_{stamp}_{label}.json")


def main() -> int:
    command = [
        "/usr/local/bin/sage",
        "-python",
        str(SOURCE),
        "--checkpoint",
        str(ATTEMPT),
    ]
    environment = os.environ.copy()
    environment["DOT_SAGE"] = "/private/tmp/f116_sage_replay"
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=HERE.parents[1],
            env=environment,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        elapsed = time.monotonic() - started
        stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        log_text = (
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed}\nstatus=TIMEOUT\nstdout:\n{stdout}\nstderr:\n{stderr}"
        )
        preserve("TIMEOUT", log_text)
        return 124

    elapsed = time.monotonic() - started
    log_text = (
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed}\nreturncode={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    if completed.returncode != 0:
        preserve(f"EXIT_{completed.returncode}", log_text)
        return completed.returncode
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        preserve("INVALID_JSON", log_text)
        return 65
    if payload.get("status") not in {"PASS", "FAIL"} or payload.get("completed_cases") != 6:
        preserve("INVALID_OUTPUT", log_text)
        return 66
    LOG.write_text(log_text)
    ATTEMPT.replace(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
