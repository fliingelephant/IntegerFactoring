#!/usr/bin/env python3
"""Run the F98 factor-assisted discovery search with a hard timeout."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 120
COMMAND = [
    sys.executable,
    str(BASE / "search_factor_assisted.py"),
    "--prime-min",
    "1000003",
    "--prime-max",
    "1200000",
    "--pair-cap",
    "30",
    "--pairs-per-p",
    "1",
    "--output",
    str(BASE / "DISCOVERY_1M_OUTPUT.json"),
]


def main() -> int:
    with (BASE / "DISCOVERY_1M_RUN.log").open("w", encoding="utf-8") as log:
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
