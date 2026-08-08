#!/usr/bin/env python3

import subprocess
import time
from pathlib import Path


base = Path(__file__).resolve().parent
command = [
    "/usr/local/bin/sage",
    str(base / "analyze_dependency.sage"),
    "--input",
    str(base.parent / "F98_multiseed_presentation_closure_kill" / "PUBLIC_REPLAY_OUTPUT.json"),
    "--output",
    str(base / "OUTPUT.json"),
]
started = time.monotonic()
completed = subprocess.run(command, capture_output=True, text=True, timeout=120, check=False)
elapsed = time.monotonic() - started
(base / "RUN.log").write_text(
    "timeout_seconds=120\n"
    + "command=" + " ".join(command) + "\n"
    + f"elapsed_seconds={elapsed:.6f}\n"
    + f"exit_code={completed.returncode}\n"
    + "stdout:\n" + completed.stdout
    + "stderr:\n" + completed.stderr
)
raise SystemExit(completed.returncode)
