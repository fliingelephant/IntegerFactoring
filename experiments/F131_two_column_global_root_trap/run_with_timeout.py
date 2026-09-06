#!/usr/bin/env python3
"""Run the frozen F131 certificate verifier and preserve its output."""

import json
from pathlib import Path
import subprocess
import sys
import time


root = Path(__file__).resolve().parent
command = [sys.executable, str(root / "verify_certificates.py")]
started = time.monotonic()
completed = subprocess.run(command, capture_output=True, text=True, timeout=60)
elapsed = time.monotonic() - started

(root / "RUN.log").write_text(
    "command: " + " ".join(command) + "\n"
    + f"exit_code: {completed.returncode}\n"
    + f"elapsed_seconds: {elapsed:.6f}\n"
    + "stdout:\n" + completed.stdout
    + "stderr:\n" + completed.stderr,
    encoding="utf-8",
)

if completed.returncode != 0:
    raise SystemExit(completed.returncode)

payload = json.loads(completed.stdout)
(root / "OUTPUT.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

