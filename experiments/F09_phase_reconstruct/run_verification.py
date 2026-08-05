#!/usr/bin/env python3
"""Run the finite verifier with a hard timeout and record its artifacts."""

from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


TIMEOUT_SECONDS = 60


def main() -> None:
    experiment_dir = Path(__file__).resolve().parent
    command = [
        sys.executable,
        str(experiment_dir / "verify_phase_reconstruction.py"),
        "--prime-bound",
        "2000",
    ]
    started = datetime.now(timezone.utc)
    timed_out = False
    try:
        completed = subprocess.run(
            command,
            cwd=experiment_dir,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
        return_code = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
    except subprocess.TimeoutExpired as error:
        timed_out = True
        return_code = 124
        stdout = error.stdout or ""
        stderr = error.stderr or ""

    finished = datetime.now(timezone.utc)
    (experiment_dir / "certificate_output.json").write_text(stdout)
    (experiment_dir / "timeout_status.txt").write_text(
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"timed_out={str(timed_out).lower()}\n"
        f"exit_code={return_code}\n"
    )
    (experiment_dir / "run.log").write_text(
        f"started_utc={started.isoformat()}\n"
        f"finished_utc={finished.isoformat()}\n"
        f"elapsed_seconds={(finished - started).total_seconds():.6f}\n"
        f"command={' '.join(command)}\n"
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"timed_out={str(timed_out).lower()}\n"
        f"exit_code={return_code}\n"
        "stderr_begin\n"
        f"{stderr}"
        "stderr_end\n"
    )
    if return_code != 0:
        raise SystemExit(return_code)


if __name__ == "__main__":
    main()
