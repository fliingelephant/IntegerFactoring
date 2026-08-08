#!/usr/bin/env python3

import subprocess
import time
from pathlib import Path


base = Path(__file__).resolve().parent
command = [
    "/opt/homebrew/bin/python3",
    str(base / "public_core_replay.py"),
    "--modulus",
    "202537109",
    "--output",
    str(base / "OUTPUT.json"),
]
started = time.monotonic()
completed = subprocess.run(
    command,
    capture_output=True,
    text=True,
    timeout=180,
    check=False,
)
elapsed = time.monotonic() - started
(base / "RUN.log").write_text(
    "timeout_seconds=180\n"
    + "command=" + " ".join(command) + "\n"
    + f"elapsed_seconds={elapsed:.6f}\n"
    + f"exit_code={completed.returncode}\n"
    + "stdout:\n" + completed.stdout
    + "stderr:\n" + completed.stderr
)
raise SystemExit(completed.returncode)
