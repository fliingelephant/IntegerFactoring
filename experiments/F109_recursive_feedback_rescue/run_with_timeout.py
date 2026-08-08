#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "test_recursive_rescue.py"
OUTPUT = HERE / "OUTPUT.json"
LOG = HERE / "RUN.log"
TIMEOUT_SECONDS = 600


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
        LOG.write_text(
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\nstatus=TIMEOUT\n"
            + (error.stdout or "")
            + (error.stderr or "")
        )
        return 124
    LOG.write_text(
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"returncode={completed.returncode}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    if completed.returncode != 0:
        return completed.returncode
    parsed = json.loads(completed.stdout)
    OUTPUT.write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
