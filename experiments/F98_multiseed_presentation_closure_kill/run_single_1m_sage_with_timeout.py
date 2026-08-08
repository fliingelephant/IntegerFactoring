#!/usr/bin/env python3
"""Run the F98 1M Sage replay with a hard timeout."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 120
COMMAND = ["sage", "-python", str(BASE / "run_single_1m_sage.py")]


def main() -> int:
    environment = dict(os.environ)
    environment["DOT_SAGE"] = "/private/tmp/f98_sage"
    with (BASE / "SINGLE_1M_SAGE_RUN.log").open("w", encoding="utf-8") as log:
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
                env=environment,
            )
        except subprocess.TimeoutExpired:
            log.write("runner_status=timeout\n")
            return 124
        log.write(f"runner_exit_code={result.returncode}\n")
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
