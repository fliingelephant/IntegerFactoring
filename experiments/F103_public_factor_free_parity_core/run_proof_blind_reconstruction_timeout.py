#!/usr/bin/env python3
"""Run the proof-blind reconstruction with a hard timeout.

Every attempt gets distinct output and log paths. Failed and timed-out
attempts remain in proof_blind_reconstruction_attempts/.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--modulus", type=int, default=202_537_109)
    parser.add_argument("--timeout-seconds", type=int, default=1_800)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    attempts = root / "proof_blind_reconstruction_attempts"
    attempts.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    attempt_output = attempts / f"{stamp}.output.json"
    attempt_log = attempts / f"{stamp}.log"
    command = [
        sys.executable,
        str(root / "proof_blind_reconstruction.py"),
        "--modulus",
        str(args.modulus),
        "--output",
        str(attempt_output),
    ]
    header = (
        f"utc_attempt={stamp}\n"
        f"timeout_seconds={args.timeout_seconds}\n"
        f"command={json_command(command)}\n"
    )
    try:
        completed = subprocess.run(
            command,
            cwd=root,
            capture_output=True,
            text=True,
            timeout=args.timeout_seconds,
            check=False,
        )
        log = (
            header
            + f"exit_code={completed.returncode}\n"
            + "stdout:\n"
            + completed.stdout
            + "stderr:\n"
            + completed.stderr
        )
        attempt_log.write_text(log)
        if completed.returncode != 0:
            print(f"failed_attempt_log={attempt_log}")
            return completed.returncode
        shutil.copy2(attempt_output, root / "proof_blind_reconstruction_output.json")
        shutil.copy2(attempt_log, root / "proof_blind_reconstruction.log")
        print(f"successful_attempt_output={attempt_output}")
        print(f"successful_attempt_log={attempt_log}")
        return 0
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else error.stderr or ""
        attempt_log.write_text(
            header
            + "exit_code=timeout\n"
            + "stdout:\n"
            + stdout
            + "stderr:\n"
            + stderr
        )
        print(f"timed_out_attempt_log={attempt_log}")
        return 124


def json_command(command: list[str]):
    import json

    return json.dumps(command, separators=(",", ":"))


if __name__ == "__main__":
    raise SystemExit(main())
