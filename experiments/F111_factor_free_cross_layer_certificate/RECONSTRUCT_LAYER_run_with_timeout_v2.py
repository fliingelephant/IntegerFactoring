#!/usr/bin/env python3
"""Named hard-timeout wrapper for frozen-layer decoder version 2."""

from __future__ import annotations

import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


HARD_TIMEOUT_SECONDS = 3600


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def main() -> int:
    directory = Path(__file__).resolve().parent
    decoder = directory / "RECONSTRUCT_LAYER_decoder_v2.py"
    public_input = directory / "RECONSTRUCT_INPUT.json"
    output = directory / "RECONSTRUCT_LAYER_OUTPUT.json"
    log = directory / "RECONSTRUCT_LAYER_RUN_V2.log"
    command = [sys.executable, str(decoder), "--input", str(public_input), "--output", str(output)]
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write("named_timeout=F111_FROZEN_LAYER_HARD_TIMEOUT_V2\n")
        stream.write(f"hard_timeout_seconds={HARD_TIMEOUT_SECONDS}\n")
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
            failed = directory / f"RECONSTRUCT_LAYER_FAILED_{utc_stamp()}_V2_TIMEOUT.log"
            stream.flush()
            shutil.copyfile(log, failed)
            print(f"TIMEOUT after {elapsed:.3f}s; preserved {failed}")
            return 124
        elapsed = time.monotonic() - started
        stream.write(f"exit_code={completed.returncode}\nelapsed_seconds={elapsed:.6f}\n")
        if completed.returncode != 0:
            stream.write("status=FAILED\n")
            failed = directory / f"RECONSTRUCT_LAYER_FAILED_{utc_stamp()}_V2_EXIT_{completed.returncode}.log"
            stream.flush()
            shutil.copyfile(log, failed)
            print(f"FAILED with exit {completed.returncode}; preserved {failed}")
            return completed.returncode
        stream.write("status=PASS\n")
    print(f"PASS in {elapsed:.3f}s; log={log}; output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
