#!/usr/bin/env python3
"""Run the sparse-DAG F116 replay under a hard timeout."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "stress_sparse_dag_first_case.py"
OUTPUT = HERE / "SPARSE_DAG_OUTPUT.json"
LOG = HERE / "SPARSE_DAG_RUN.log"
TIMEOUT_SECONDS = 600


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    attempt = HERE / f"SPARSE_DAG_ATTEMPT_{stamp}.json"
    command = ["/usr/local/bin/sage", "-python", str(SOURCE), "--output", str(attempt)]
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
        result = HERE / f"SPARSE_DAG_OUTPUT_FAILED_{stamp}_TIMEOUT.json"
        log = HERE / f"SPARSE_DAG_RUN_FAILED_{stamp}_TIMEOUT.log"
        result.write_text(attempt.read_text() if attempt.exists() else '{"status":"TIMEOUT"}\n')
        log.write_text(
            f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
            f"elapsed_seconds={elapsed:.6f}\ntimed_out=true\n"
            f"stdout:\n{error.stdout or ''}\nstderr:\n{error.stderr or ''}\n"
        )
        return 124
    log_text = (
        f"command={json.dumps(command)}\ntimeout_seconds={TIMEOUT_SECONDS}\n"
        f"elapsed_seconds={elapsed:.6f}\ntimed_out=false\nreturncode={completed.returncode}\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}\n"
    )
    parsed = json.loads(attempt.read_text()) if attempt.exists() else {"status": "NO_OUTPUT"}
    if completed.returncode != 0 or parsed.get("status") != "PASS":
        reason = f"EXIT_{completed.returncode}" if completed.returncode else "CLAIM"
        result = HERE / f"SPARSE_DAG_OUTPUT_FAILED_{stamp}_{reason}.json"
        log = HERE / f"SPARSE_DAG_RUN_FAILED_{stamp}_{reason}.log"
        result.write_text(attempt.read_text() if attempt.exists() else json.dumps(parsed) + "\n")
        log.write_text(log_text)
        if attempt.exists():
            attempt.unlink()
        return completed.returncode or 1
    attempt.replace(OUTPUT)
    LOG.write_text(log_text)
    print(f"verdict=PASS elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
