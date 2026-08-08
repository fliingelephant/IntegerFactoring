#!/usr/bin/env python3
"""Run the F98 direct-null full replays with a hard timeout."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 120
COMMAND = [sys.executable, str(BASE / "run_direct_nulls_factor_assisted.py")]


def main() -> int:
    with (BASE / "DIRECT_NULLS_10K_FULL_RUN.log").open("w", encoding="utf-8") as log:
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
