#!/usr/bin/env python3
"""Hard-timeout runner for the proof-blind F111 reconstruction."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "RECONSTRUCT_BLIND_verify.py"
ATTEMPT_OUTPUT = HERE / "RECONSTRUCT_BLIND_ATTEMPT_OUTPUT.json"
ATTEMPT_LOG = HERE / "RECONSTRUCT_BLIND_ATTEMPT_RUN.log"
OUTPUT = HERE / "RECONSTRUCT_BLIND_OUTPUT.json"
LOG = HERE / "RECONSTRUCT_BLIND_RUN.log"
TIMEOUT_SECONDS = 120


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")


def preserve(path: Path, label: str, stamp: str) -> None:
    if path.exists():
        os.replace(path, HERE / f"RECONSTRUCT_BLIND_FAILED_{stamp}_{label}{path.suffix}")


def main() -> int:
    stale_stamp = timestamp()
    preserve(ATTEMPT_OUTPUT, "STALE_OUTPUT", stale_stamp)
    preserve(ATTEMPT_LOG, "STALE_RUN", stale_stamp)
    command = [sys.executable, str(SOURCE), "--output", str(ATTEMPT_OUTPUT)]
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
        exit_code = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    except subprocess.TimeoutExpired as error:
        exit_code = 124
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else error.stderr or ""
        timed_out = True
        ATTEMPT_OUTPUT.write_text(
            json.dumps(
                {
                    "status": "FAIL",
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
        f"command={json.dumps(command)}\n"
        f"working_directory={HERE}\n"
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed:.6f}\n"
        f"timed_out={str(timed_out).lower()}\n"
        f"exit_code={exit_code}\n"
        f"stdout:\n{stdout}stderr:\n{stderr}\n",
        encoding="utf-8",
    )

    valid_pass = False
    if exit_code == 0 and ATTEMPT_OUTPUT.exists():
        try:
            valid_pass = json.loads(ATTEMPT_OUTPUT.read_text(encoding="utf-8")).get(
                "status"
            ) == "PASS"
        except json.JSONDecodeError:
            valid_pass = False
    if valid_pass:
        os.replace(ATTEMPT_OUTPUT, OUTPUT)
        os.replace(ATTEMPT_LOG, LOG)
        return 0

    failed_stamp = timestamp()
    preserve(ATTEMPT_OUTPUT, "OUTPUT", failed_stamp)
    preserve(ATTEMPT_LOG, "RUN", failed_stamp)
    return exit_code if exit_code != 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
