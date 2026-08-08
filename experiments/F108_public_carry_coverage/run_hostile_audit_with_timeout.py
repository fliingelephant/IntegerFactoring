#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "audit_independent_verifier.sage"
OUTPUT = HERE / "AUDIT_OUTPUT.json"
LOG = HERE / "AUDIT_RUN.log"
SAGE = "/usr/local/bin/sage"
TIMEOUT_SECONDS = 300


def main() -> int:
    command = [SAGE, str(SOURCE)]
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
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else error.stderr or ""
        LOG.write_text(
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
            f"status=TIMEOUT\nstdout:\n{stdout}\nstderr:\n{stderr}"
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
