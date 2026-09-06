#!/usr/bin/env python3
"""Run F124-D01 through its preregistered 1,800-second hard timeout."""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


BASE = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 1800
COMMAND = [
    sys.executable,
    str(BASE / "scan_full_subgroup.py"),
    "--output",
    str(BASE / "OUTPUT.json"),
]


def main() -> int:
    log_path = BASE / "RUN.log"
    if log_path.exists():
        raise FileExistsError(log_path)
    started = time.monotonic()
    with log_path.open("x", encoding="utf-8") as log:
        log.write(f"timeout_seconds={TIMEOUT_SECONDS}\n")
        log.write("command=" + " ".join(COMMAND) + "\n")
        log.flush()
        try:
            completed = subprocess.run(
                COMMAND,
                cwd=BASE,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT_SECONDS,
                check=False,
                text=True,
            )
        except subprocess.TimeoutExpired:
            log.write(f"elapsed_seconds={time.monotonic() - started:.6f}\n")
            log.write("runner_status=timeout\n")
            return 124
        log.write(f"elapsed_seconds={time.monotonic() - started:.6f}\n")
        log.write(f"runner_exit_code={completed.returncode}\n")
        return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
