#!/usr/bin/env python3
"""Run the F115 independent audit and preserve every failed attempt."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "audit_independent_verifier.py"
OUTPUT = HERE / "AUDIT_OUTPUT.json"
LOG = HERE / "AUDIT_RUN.log"
TIMEOUT_SECONDS = 1800


def preserve_failure(label: str, log_text: str, stdout: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = HERE / f"AUDIT_FAILED_{stamp}_{label}"
    stem.with_suffix(".log").write_text(log_text)
    if stdout.strip():
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError:
            return
        stem.with_suffix(".json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> int:
    command = ["/usr/local/bin/sage", "-python", str(SOURCE)]
    environment = os.environ.copy()
    environment["DOT_SAGE"] = "/private/tmp/f115_hostile_audit_sage"
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=HERE.parents[1],
            env=environment,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        elapsed = time.monotonic() - started
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        log_text = (
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed}\nstatus=TIMEOUT\nstdout:\n{stdout}\nstderr:\n{stderr}"
        )
        LOG.write_text(log_text)
        preserve_failure("TIMEOUT", log_text, stdout)
        return 124

    elapsed = time.monotonic() - started
    log_text = (
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed}\nreturncode={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    LOG.write_text(log_text)
    if completed.returncode != 0:
        preserve_failure("EXECUTION", log_text, completed.stdout)
        return completed.returncode
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        preserve_failure("INVALID_JSON", log_text, completed.stdout)
        return 65
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
