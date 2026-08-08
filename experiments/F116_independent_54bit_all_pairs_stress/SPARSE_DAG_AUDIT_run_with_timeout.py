#!/usr/bin/env python3
"""Run the independent F116 sparse-DAG audit under a hard timeout."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VERIFIER = HERE / "SPARSE_DAG_AUDIT_verifier.py"
INPUT = HERE / "RECONSTRUCT_INPUT.json"
STATEMENT = HERE / "RECONSTRUCT_STATEMENT.md"
CANDIDATE_SOURCE = HERE / "stress_sparse_dag_first_case.py"
CANDIDATE_OUTPUT = HERE / "SPARSE_DAG_OUTPUT.json"
CANDIDATE_LOG = HERE / "SPARSE_DAG_RUN.log"
OUTPUT = HERE / "SPARSE_DAG_AUDIT_OUTPUT.json"
LOG = HERE / "SPARSE_DAG_AUDIT_RUN.log"
TIMEOUT_SECONDS = 300


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    attempt_output = HERE / f"SPARSE_DAG_AUDIT_ATTEMPT_{stamp}.json"
    attempt_log = HERE / f"SPARSE_DAG_AUDIT_ATTEMPT_{stamp}.log"
    command = [
        sys.executable,
        str(VERIFIER),
        "--input",
        str(INPUT),
        "--statement",
        str(STATEMENT),
        "--candidate-source",
        str(CANDIDATE_SOURCE),
        "--candidate-output",
        str(CANDIDATE_OUTPUT),
        "--candidate-log",
        str(CANDIDATE_LOG),
        "--output",
        str(attempt_output),
    ]
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
        elapsed = time.monotonic() - started
    except subprocess.TimeoutExpired as error:
        elapsed = time.monotonic() - started
        failed_output = HERE / f"SPARSE_DAG_AUDIT_FAILED_{stamp}_TIMEOUT.json"
        failed_log = HERE / f"SPARSE_DAG_AUDIT_FAILED_{stamp}_TIMEOUT.log"
        failed_output.write_text(
            attempt_output.read_text()
            if attempt_output.exists()
            else json.dumps({"status": "TIMEOUT", "verdict": "FAIL"}, sort_keys=True) + "\n"
        )
        failed_log.write_text(
            f"command={json.dumps(command)}\n"
            f"working_directory={str(ROOT)!r}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed:.6f}\n"
            "timed_out=true\n"
            f"stdout:\n{error.stdout or ''}\n"
            f"stderr:\n{error.stderr or ''}\n"
        )
        if attempt_output.exists():
            attempt_output.unlink()
        print("verdict=FAIL")
        print("reason=TIMEOUT")
        return 124

    attempt_log.write_text(
        f"command={json.dumps(command)}\n"
        f"working_directory={str(ROOT)!r}\n"
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed:.6f}\n"
        "timed_out=false\n"
        f"exit_code={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}\n"
    )
    try:
        parsed = json.loads(attempt_output.read_text())
    except Exception as error:
        parsed = {"status": "INVALID_OUTPUT", "verdict": "FAIL", "error": str(error)}
    if completed.returncode != 0 or parsed.get("status") != "PASS":
        reason = f"EXIT_{completed.returncode}" if completed.returncode else "CLAIM"
        failed_output = HERE / f"SPARSE_DAG_AUDIT_FAILED_{stamp}_{reason}.json"
        failed_log = HERE / f"SPARSE_DAG_AUDIT_FAILED_{stamp}_{reason}.log"
        attempt_log.replace(failed_log)
        if attempt_output.exists():
            attempt_output.replace(failed_output)
        else:
            failed_output.write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
        print("verdict=FAIL")
        print(f"reason={reason}")
        return completed.returncode or 1

    attempt_output.replace(OUTPUT)
    attempt_log.replace(LOG)
    print("verdict=PASS")
    print(f"elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
