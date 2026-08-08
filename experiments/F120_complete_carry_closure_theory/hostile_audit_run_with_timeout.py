#!/usr/bin/env python3
"""Named hard-timeout runner for the independent F120 hostile audit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


HARD_TIMEOUT_SECONDS = 60


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    directory = Path(__file__).resolve().parent
    registration_path = directory / "HOSTILE_AUDIT_REGISTRATION.json"
    registration = json.loads(registration_path.read_text())
    source = directory / registration["source"]
    if sha256_file(source) != registration["source_sha256"]:
        raise AssertionError("registered hostile-audit source changed")
    if registration["hard_timeout_seconds"] != HARD_TIMEOUT_SECONDS:
        raise AssertionError("registered hostile-audit timeout changed")

    output = directory / "HOSTILE_AUDIT_OUTPUT.json"
    log = directory / "HOSTILE_AUDIT_RUN.log"
    command = [
        sys.executable,
        str(source),
        "--registration",
        str(registration_path),
        "--output",
        str(output),
    ]
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write("named_timeout=F120_HOSTILE_AUDIT_HARD_TIMEOUT\n")
        stream.write(f"hard_timeout_seconds={HARD_TIMEOUT_SECONDS}\n")
        stream.write(f"registration_sha256={sha256_file(registration_path)}\n")
        stream.write("command=" + json.dumps(command) + "\n")
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
            return 124

        elapsed = time.monotonic() - started
        stream.write(f"returncode={completed.returncode}\n")
        stream.write(f"elapsed_seconds={elapsed:.6f}\n")
        status = "PASS" if completed.returncode == 0 else "FAILED"
        stream.write(f"status={status}\n")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
