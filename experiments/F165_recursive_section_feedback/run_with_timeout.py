#!/usr/bin/env python3
"""Named 600-second hard-timeout runner for F165-D01."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time


TIMEOUT_SECONDS = 600
TIMEOUT_NAME = "F165_DEPTH_TWO_RECURSIVE_SECTION_HARD_TIMEOUT"


def main() -> int:
    directory = Path(__file__).resolve().parent
    registration = json.loads((directory / "REGISTRATION.json").read_text())
    if registration["status"] != "FROZEN_BEFORE_AUTHORITATIVE_RUN":
        raise AssertionError("registration status changed")
    if registration["timeout_seconds"] != TIMEOUT_SECONDS:
        raise AssertionError("registered timeout changed")
    observed = {
        name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
        for name in registration["frozen_files"]
    }
    if observed != registration["frozen_files"]:
        raise AssertionError("a preregistered F165 file changed")
    if (directory / "RUN.log").exists() or (directory / "OUTPUT.json").exists():
        raise AssertionError("F165-D01 authoritative run already exists")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    attempt = directory / f"ATTEMPT_{timestamp}.json"
    log = directory / "RUN.log"
    command = [
        "/usr/local/bin/sage",
        "-python",
        str(directory / "search.py"),
        "--output",
        str(attempt),
    ]
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write(f"named_timeout={TIMEOUT_NAME}\n")
        stream.write(f"timeout_seconds={TIMEOUT_SECONDS}\n")
        stream.write(f"command={json.dumps(command)}\n")
        stream.write(f"working_directory={directory}\n")
        stream.write(f"registration={json.dumps(registration, sort_keys=True)}\n")
        stream.flush()
        try:
            environment = os.environ.copy()
            environment["DOT_SAGE"] = str(directory / ".sage_runtime")
            completed = subprocess.run(
                command,
                cwd=directory,
                env=environment,
                stdout=stream,
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
        except subprocess.TimeoutExpired:
            elapsed = time.monotonic() - started
            stream.write(f"status=TIMEOUT\nelapsed_seconds={elapsed}\n")
            stream.flush()
            shutil.copyfile(log, directory / f"RUN_FAILED_{timestamp}_TIMEOUT.log")
            return 124
        elapsed = time.monotonic() - started
        stream.write(f"exit_code={completed.returncode}\nelapsed_seconds={elapsed}\n")
        if completed.returncode:
            stream.write("status=FAIL\n")
            stream.flush()
            shutil.copyfile(
                log,
                directory / f"RUN_FAILED_{timestamp}_EXIT_{completed.returncode}.log",
            )
            return completed.returncode
        if not attempt.exists():
            stream.write("status=FAIL_MISSING_OUTPUT\n")
            stream.flush()
            shutil.copyfile(
                log, directory / f"RUN_FAILED_{timestamp}_MISSING_OUTPUT.log"
            )
            return 2
        output = json.loads(attempt.read_text())
        if output.get("status") != "PASS" or output.get("experiment_id") != "F165-D01":
            stream.write("status=FAIL_OUTPUT_STATUS\n")
            stream.flush()
            shutil.copyfile(
                log, directory / f"RUN_FAILED_{timestamp}_OUTPUT_STATUS.log"
            )
            return 3
        attempt.replace(directory / "OUTPUT.json")
        stream.write("status=PASS\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
