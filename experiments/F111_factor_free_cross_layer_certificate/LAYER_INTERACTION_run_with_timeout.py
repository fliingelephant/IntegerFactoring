#!/usr/bin/env python3
"""Hard-timeout wrapper for the F111 layer-interaction analysis."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VERIFIER = HERE / "LAYER_INTERACTION_independent_verifier.py"
CERTIFICATE = HERE / "CERTIFICATE.json"
PUBLIC_BASIS = (
    ROOT
    / "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py"
)
OUTPUT = HERE / "LAYER_INTERACTION_OUTPUT.json"
LOG = HERE / "LAYER_INTERACTION_RUN.log"
TIMEOUT_SECONDS = 300


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    attempt_output = HERE / f"LAYER_INTERACTION_ATTEMPT_{stamp}.json"
    attempt_log = HERE / f"LAYER_INTERACTION_ATTEMPT_{stamp}.log"
    command = [
        sys.executable,
        str(VERIFIER),
        "--certificate",
        str(CERTIFICATE),
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
        failed_output = HERE / f"LAYER_INTERACTION_FAILED_{stamp}_TIMEOUT.json"
        failed_log = HERE / f"LAYER_INTERACTION_FAILED_{stamp}_TIMEOUT.log"
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
            attempt_output.replace(failed_output)
        else:
            failed_output.write_text(
                json.dumps({"status": "TIMEOUT", "verdict": "FAIL"}, indent=2) + "\n"
            )
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
    if completed.returncode != 0 or parsed.get("status") != "PASS" or parsed.get("verdict") != "PASS":
        reason = f"EXIT_{completed.returncode}" if completed.returncode else "CLAIM"
        failed_output = HERE / f"LAYER_INTERACTION_FAILED_{stamp}_{reason}.json"
        failed_log = HERE / f"LAYER_INTERACTION_FAILED_{stamp}_{reason}.log"
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
