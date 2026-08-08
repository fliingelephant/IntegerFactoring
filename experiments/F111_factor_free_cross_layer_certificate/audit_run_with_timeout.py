#!/usr/bin/env python3
"""Run the independent F111 audit under a hard timeout and preserve failures."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VERIFIER = HERE / "independent_certificate_audit.py"
PUBLIC_BASIS = (
    ROOT
    / "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py"
)
FINAL_OUTPUT = HERE / "AUDIT_OUTPUT.json"
FINAL_LOG = HERE / "AUDIT_RUN.log"
TIMEOUT_SECONDS = 60


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    attempt_output = HERE / f"AUDIT_ATTEMPT_{stamp}.json"
    attempt_log = HERE / f"AUDIT_ATTEMPT_{stamp}.log"
    command = [
        sys.executable,
        str(VERIFIER),
        "--candidate-dir",
        str(HERE),
        "--public-basis-source",
        str(PUBLIC_BASIS),
        "--output",
        str(attempt_output),
    ]
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
        elapsed = time.monotonic() - started
    except subprocess.TimeoutExpired as error:
        elapsed = time.monotonic() - started
        log_text = (
            f"command={json.dumps(command)}\n"
            f"working_directory={str(ROOT)!r}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed:.6f}\n"
            "timed_out=true\n"
            f"stdout:\n{error.stdout or ''}\n"
            f"stderr:\n{error.stderr or ''}\n"
        )
        failed_log = HERE / f"AUDIT_FAILED_{stamp}_TIMEOUT.log"
        failed_output = HERE / f"AUDIT_FAILED_{stamp}_TIMEOUT.json"
        failed_log.write_text(log_text)
        if attempt_output.exists():
            attempt_output.replace(failed_output)
        else:
            failed_output.write_text(
                json.dumps(
                    {"status": "TIMEOUT", "audit_verdict": "FAIL"},
                    indent=2,
                    sort_keys=True,
                )
                + "\n"
            )
        print("audit_verdict=FAIL")
        print("reason=TIMEOUT")
        return 124

    log_text = (
        f"command={json.dumps(command)}\n"
        f"working_directory={str(ROOT)!r}\n"
        f"timeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed:.6f}\n"
        "timed_out=false\n"
        f"exit_code={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}\n"
    )
    attempt_log.write_text(log_text)
    try:
        parsed = json.loads(attempt_output.read_text())
    except Exception as error:
        parsed = {"status": "INVALID_OUTPUT", "audit_verdict": "FAIL", "error": str(error)}

    if completed.returncode != 0 or parsed.get("status") != "PASS" or parsed.get("audit_verdict") != "PASS":
        reason = f"EXIT_{completed.returncode}" if completed.returncode else "CLAIM"
        failed_log = HERE / f"AUDIT_FAILED_{stamp}_{reason}.log"
        failed_output = HERE / f"AUDIT_FAILED_{stamp}_{reason}.json"
        attempt_log.replace(failed_log)
        if attempt_output.exists():
            attempt_output.replace(failed_output)
        else:
            failed_output.write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
        print("audit_verdict=FAIL")
        print(f"reason={reason}")
        return completed.returncode or 1

    attempt_output.replace(FINAL_OUTPUT)
    attempt_log.replace(FINAL_LOG)
    print("audit_verdict=PASS")
    print(f"elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
