#!/usr/bin/env python3
"""Run the F97 bounded family test under a hard wall-clock timeout."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 120
COMMAND = [
    sys.executable,
    str(BASE / "search_square_inverse_seed_family.py"),
    "--x-min",
    "3",
    "--x-max",
    "2001",
    "--control-x",
    "43",
    "--output",
    str(BASE / "OUTPUT.json"),
]


def main() -> int:
    log_path = BASE / "RUN.log"
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"timeout_seconds={TIMEOUT_SECONDS}\n")
        log.write("command=" + " ".join(COMMAND) + "\n")
        log.flush()
        try:
            result = subprocess.run(
                COMMAND,
                cwd=BASE,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT_SECONDS,
                check=False,
                text=True,
            )
        except subprocess.TimeoutExpired:
            log.write("runner_status=timeout\n")
            return 124
        log.write(f"runner_exit_code={result.returncode}\n")
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
