#!/usr/bin/env python3
"""Named hard-timeout wrapper for the F117 exact counterexample check."""

from __future__ import annotations

import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


HARD_TIMEOUT_SECONDS = 600


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def main() -> int:
    directory = Path(__file__).resolve().parent
    verifier = directory / "verify_full_source_counterexample.py"
    output = directory / "OUTPUT.json"
    log = directory / "RUN.log"
    command = [sys.executable, "-B", str(verifier)]
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write("named_timeout=F117_FULL_SOURCE_COUNTEREXAMPLE_HARD_TIMEOUT\n")
        stream.write(f"hard_timeout_seconds={HARD_TIMEOUT_SECONDS}\n")
        stream.write(f"working_directory={directory}\n")
        stream.write(f"started_utc={datetime.now(timezone.utc).isoformat()}\n")
        stream.write("command=" + " ".join(command) + "\n")
        stream.flush()
        try:
            completed = subprocess.run(
                command,
                cwd=directory,
                stdout=stream,
                stderr=subprocess.STDOUT,
                timeout=HARD_TIMEOUT_SECONDS,
                check=False,
            )
        except subprocess.TimeoutExpired:
            elapsed = time.monotonic() - started
            stream.write(f"status=TIMEOUT\nelapsed_seconds={elapsed:.6f}\n")
            stream.flush()
            failed = directory / f"RUN_FAILED_{timestamp()}_TIMEOUT.log"
            shutil.copyfile(log, failed)
            print(f"TIMEOUT after {elapsed:.3f}s; preserved {failed}")
            return 124
        elapsed = time.monotonic() - started
        stream.write(f"exit_code={completed.returncode}\n")
        stream.write(f"elapsed_seconds={elapsed:.6f}\n")
        if completed.returncode != 0:
            stream.write("status=FAILED\n")
            stream.flush()
            failed = directory / f"RUN_FAILED_{timestamp()}_EXIT_{completed.returncode}.log"
            shutil.copyfile(log, failed)
            if output.exists():
                failed_output = directory / f"OUTPUT_FAILED_{timestamp()}.json"
                shutil.copyfile(output, failed_output)
            print(f"FAILED with exit {completed.returncode}; preserved {failed}")
            return completed.returncode
        if not output.exists():
            stream.write("status=FAILED_MISSING_OUTPUT\n")
            print("FAILED: verifier did not write OUTPUT.json")
            return 1
        stream.write("status=PASS\n")
    print(f"PASS in {elapsed:.3f}s; log={log}; output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
