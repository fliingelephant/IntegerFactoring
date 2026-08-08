#!/usr/bin/env python3
"""Run the F98 hostile-audit replay and independent verifier."""

from __future__ import annotations

import subprocess
import sys
import os
from pathlib import Path


BASE = Path(__file__).resolve().parent
REPLAY_TIMEOUT_SECONDS = 120
VERIFY_TIMEOUT_SECONDS = 180
REPLAY_COMMAND = [
    sys.executable,
    str(BASE / "public_factorization_free_replay.py"),
    "--modulus",
    "202537109",
    "--output",
    str(BASE / "AUDIT_PUBLIC_REPLAY_OUTPUT.json"),
]
VERIFY_COMMAND = [
    "sage",
    "-python",
    str(BASE / "hostile_audit_verify.py"),
    "--candidate-output",
    str(BASE / "PUBLIC_REPLAY_OUTPUT.json"),
    "--audit-output",
    str(BASE / "AUDIT_PUBLIC_REPLAY_OUTPUT.json"),
    "--small-support-output",
    str(BASE / "SMALL_SUPPORT_OUTPUT.json"),
    "--output",
    str(BASE / "AUDIT_VERIFY_OUTPUT.json"),
]


def run(command: list[str], timeout: int, log, environment=None) -> int:
    log.write(f"timeout_seconds={timeout}\n")
    log.write("command=" + " ".join(command) + "\n")
    log.flush()
    try:
        result = subprocess.run(
            command,
            cwd=BASE,
            stdout=log,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
            text=True,
            env=environment,
        )
    except subprocess.TimeoutExpired:
        log.write("runner_status=timeout\n")
        return 124
    log.write(f"runner_exit_code={result.returncode}\n")
    log.flush()
    return result.returncode


def main() -> int:
    with (BASE / "AUDIT_RUN.log").open("w", encoding="utf-8") as log:
        replay_code = run(REPLAY_COMMAND, REPLAY_TIMEOUT_SECONDS, log)
        if replay_code != 0:
            return replay_code
        environment = os.environ.copy()
        environment["DOT_SAGE"] = "/private/tmp/f98_hostile_audit_sage"
        return run(VERIFY_COMMAND, VERIFY_TIMEOUT_SECONDS, log, environment)


if __name__ == "__main__":
    raise SystemExit(main())
