#!/usr/bin/env python3
"""Run both F110 hostile verifiers with hard timeouts and failure retention."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATTEMPT_AUDIT = HERE / "AUDIT_ATTEMPT_OUTPUT.json"
ATTEMPT_PUBLIC = HERE / "AUDIT_ATTEMPT_PUBLIC_REPLAY_OUTPUT.json"
ATTEMPT_LOG = HERE / "AUDIT_ATTEMPT_RUN.log"
AUDIT_OUTPUT = HERE / "AUDIT_OUTPUT.json"
PUBLIC_OUTPUT = HERE / "AUDIT_PUBLIC_REPLAY_OUTPUT.json"
RUN_LOG = HERE / "AUDIT_RUN.log"
PUBLIC_TIMEOUT_SECONDS = 300
SAGE_TIMEOUT_SECONDS = 900


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")


def preserve(path: Path, label: str, run_stamp: str) -> None:
    if path.exists():
        os.replace(path, HERE / f"AUDIT_FAILED_{run_stamp}_{label}{path.suffix}")


def run(command: list[str], timeout: int, environment: dict[str, str]) -> tuple[int, str]:
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            env=environment,
        )
        code = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    except subprocess.TimeoutExpired as error:
        code = 124
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else error.stderr or ""
        timed_out = True
    elapsed = time.monotonic() - started
    log = (
        f"command={json.dumps(command)}\n"
        f"timeout_seconds={timeout}\n"
        f"elapsed_seconds={elapsed:.6f}\n"
        f"timed_out={str(timed_out).lower()}\n"
        f"exit_code={code}\n"
        f"stdout:\n{stdout}stderr:\n{stderr}\n"
    )
    return code, log


def main() -> int:
    run_stamp = stamp()
    for path, label in (
        (ATTEMPT_AUDIT, "STALE_AUDIT_OUTPUT"),
        (ATTEMPT_PUBLIC, "STALE_PUBLIC_OUTPUT"),
        (ATTEMPT_LOG, "STALE_RUN_LOG"),
    ):
        preserve(path, label, run_stamp)

    environment = os.environ.copy()
    environment["DOT_SAGE"] = "/private/tmp/f110_hostile_audit_sage"
    public_command = [
        sys.executable,
        str(HERE / "audit_n_only_certificate_replay.py"),
        "--output",
        str(ATTEMPT_PUBLIC),
    ]
    sage_command = [
        "sage",
        "-python",
        str(HERE / "audit_independent_verifier.py"),
        "--output",
        str(ATTEMPT_AUDIT),
    ]

    public_code, public_log = run(public_command, PUBLIC_TIMEOUT_SECONDS, environment)
    sage_code, sage_log = run(sage_command, SAGE_TIMEOUT_SECONDS, environment)
    ATTEMPT_LOG.write_text(
        "stage=N-only fixed-certificate replay\n"
        + public_log
        + "stage=independent Sage hidden-prime reconstruction\n"
        + sage_log,
        encoding="utf-8",
    )

    codes = [public_code, sage_code]
    for path in (ATTEMPT_PUBLIC, ATTEMPT_AUDIT):
        if path.exists():
            try:
                parsed = json.loads(path.read_text(encoding="utf-8"))
                if parsed.get("status") != "PASS":
                    codes.append(1)
            except (json.JSONDecodeError, OSError):
                codes.append(1)
        else:
            codes.append(1)

    exit_code = next((code for code in codes if code != 0), 0)
    if exit_code == 0:
        os.replace(ATTEMPT_PUBLIC, PUBLIC_OUTPUT)
        os.replace(ATTEMPT_AUDIT, AUDIT_OUTPUT)
        os.replace(ATTEMPT_LOG, RUN_LOG)
        return 0

    failure_stamp = stamp()
    preserve(ATTEMPT_PUBLIC, "PUBLIC_OUTPUT", failure_stamp)
    preserve(ATTEMPT_AUDIT, "AUDIT_OUTPUT", failure_stamp)
    preserve(ATTEMPT_LOG, "RUN_LOG", failure_stamp)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
