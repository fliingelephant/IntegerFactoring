#!/usr/bin/env python3
"""Frozen 600-second runner for the F165-R03 V2 blind reconstruction."""

from __future__ import annotations

import hashlib
import os
import signal
import subprocess
import sys
from pathlib import Path


TIMEOUT_SECONDS = 600
STATEMENT_SHA256 = "1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd"
SOURCE_SHA256 = "d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1"

EXPERIMENT_DIR = Path(__file__).resolve().parent
REPOSITORY = EXPERIMENT_DIR.parent.parent
STATEMENT = EXPERIMENT_DIR / "V2_BLIND_STATEMENT.md"
SOURCE = EXPERIMENT_DIR / "f165_r02_v2_blind_reconstruct.py"
LOG = EXPERIMENT_DIR / "f165_r03_v2_blind_run.log"
OUTPUT = EXPERIMENT_DIR / "f165_r03_v2_blind_output.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    observed_statement_hash = sha256(STATEMENT)
    observed_source_hash = sha256(SOURCE)
    if observed_statement_hash != STATEMENT_SHA256:
        raise SystemExit(
            f"statement hash mismatch: {observed_statement_hash} != {STATEMENT_SHA256}"
        )
    if observed_source_hash != SOURCE_SHA256:
        raise SystemExit(
            f"source hash mismatch: {observed_source_hash} != {SOURCE_SHA256}"
        )
    if LOG.exists():
        raise SystemExit(f"refusing to overwrite log: {LOG}")
    if OUTPUT.exists():
        raise SystemExit(f"refusing to overwrite output: {OUTPUT}")

    command = [sys.executable, str(SOURCE), "--output", str(OUTPUT)]
    with LOG.open("xb") as log:
        header = (
            f"repository={REPOSITORY}\n"
            f"statement={STATEMENT}\n"
            f"statement_sha256={observed_statement_hash}\n"
            f"source={SOURCE}\n"
            f"source_sha256={observed_source_hash}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\n"
            f"output={OUTPUT}\n"
            f"command={' '.join(command)}\n"
            "estimated_peak_memory_mib=256\n"
            "process_audit=performed_externally_by_root_before_registration\n"
        )
        log.write(header.encode("utf-8"))
        log.flush()
        preflight = ["vm_stat"]
        log.write((f"preflight_command={' '.join(preflight)}\n").encode("utf-8"))
        completed = subprocess.run(
            preflight,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        log.write(completed.stdout + b"\n")
        log.flush()

        process = subprocess.Popen(
            command,
            cwd=REPOSITORY,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            return_code = process.wait(timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            log.write(f"timeout_after_seconds={TIMEOUT_SECONDS}\n".encode("utf-8"))
            log.flush()
            return 124
        log.write(f"return_code={return_code}\n".encode("utf-8"))
        log.flush()

    if return_code != 0:
        return return_code
    if not OUTPUT.is_file():
        raise SystemExit(f"source returned success without output: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
