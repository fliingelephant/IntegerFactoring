#!/usr/bin/env python3

import os
import subprocess
import time
from pathlib import Path


base = Path(__file__).resolve().parent
command = [
    "/usr/local/bin/sage",
    str(base / "analyze_full_core.sage"),
    "--input",
    str(base.parent / "F98_multiseed_presentation_closure_kill" / "PUBLIC_REPLAY_OUTPUT.json"),
    "--output",
    str(base / "OUTPUT.json"),
]
environment = dict(os.environ)
environment["DOT_SAGE"] = "/private/tmp/f102_sage"
started = time.monotonic()
completed = subprocess.run(
    command,
    capture_output=True,
    text=True,
    timeout=180,
    check=False,
    env=environment,
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
