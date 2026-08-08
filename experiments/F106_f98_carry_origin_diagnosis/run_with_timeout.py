#!/opt/homebrew/bin/python3
import subprocess
import sys
import time
from pathlib import Path


directory = Path(__file__).resolve().parent
command = ["/opt/homebrew/bin/python3", str(directory / "analyze_carry_origin.py")]
started = time.monotonic()
try:
    completed = subprocess.run(command, cwd=directory, capture_output=True, text=True, timeout=30)
except subprocess.TimeoutExpired as error:
    log = f"command={command!r}\ntimeout_seconds=30\nstatus=timeout\nstdout:\n{error.stdout or ''}\nstderr:\n{error.stderr or ''}\n"
    (directory / "RUN.log").write_text(log)
    raise
elapsed = time.monotonic() - started
log = f"command={command!r}\ntimeout_seconds=30\nelapsed_seconds={elapsed:.6f}\nexit_code={completed.returncode}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}\n"
(directory / "RUN.log").write_text(log)
sys.exit(completed.returncode)
