#!/usr/bin/env python3
"""Registered hard-timeout runner for the no-stop F122 scan."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time


HARD_TIMEOUT_SECONDS = 900


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    directory = Path(__file__).resolve().parent
    registration_path = directory / "REGISTRATION.json"
    registration = json.loads(registration_path.read_text())
    for name, expected_hash in registration["sha256"].items():
        actual_hash = sha256_file(directory / name)
        if actual_hash != expected_hash:
            raise AssertionError(f"registered artifact changed: {name}")
    if registration["hard_timeout_seconds"] != HARD_TIMEOUT_SECONDS:
        raise AssertionError("registered timeout changed")
    if registration["runner"] != Path(__file__).name:
        raise AssertionError("registered runner mismatch")

    source = directory / registration["source"]
    corpus = directory / registration["corpus"]
    attempt = directory / f"ATTEMPT_{stamp()}.json"
    output = directory / registration["authoritative_output"]
    log = directory / registration["authoritative_log"]
    command = [
        "/usr/local/bin/sage",
        "-python",
        str(source),
        "--corpus",
        str(corpus),
        "--output",
        str(attempt),
    ]
    environment = os.environ.copy()
    environment["DOT_SAGE"] = str(directory / ".sage")
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write("named_timeout=F122_STABLE_PRIVATE_FULL_SOURCE_HARD_TIMEOUT\n")
        stream.write(f"hard_timeout_seconds={HARD_TIMEOUT_SECONDS}\n")
        stream.write(f"registration_sha256={sha256_file(registration_path)}\n")
        stream.write(f"DOT_SAGE={environment['DOT_SAGE']}\n")
        stream.write("command=" + json.dumps(command) + "\n")
        stream.flush()
        try:
            completed = subprocess.run(
                command,
                cwd=directory,
                stdout=stream,
                stderr=subprocess.STDOUT,
                env=environment,
                timeout=HARD_TIMEOUT_SECONDS,
                check=False,
            )
        except subprocess.TimeoutExpired:
            elapsed = time.monotonic() - started
            stream.write(f"status=TIMEOUT\nelapsed_seconds={elapsed:.6f}\n")
            stream.flush()
            failed_log = directory / f"RUN_FAILED_{stamp()}_TIMEOUT.log"
            shutil.copyfile(log, failed_log)
            failed_output = directory / f"OUTPUT_FAILED_{stamp()}_TIMEOUT.json"
            if attempt.exists():
                attempt.replace(failed_output)
            else:
                failed_output.write_text('{"status":"TIMEOUT_NO_CHECKPOINT"}\n')
            print(f"TIMEOUT after {elapsed:.3f}s")
            return 124

        elapsed = time.monotonic() - started
        stream.write(f"returncode={completed.returncode}\n")
        stream.write(f"elapsed_seconds={elapsed:.6f}\n")
        parsed = json.loads(attempt.read_text()) if attempt.exists() else {}
        accepted = parsed.get("status") == "COMPLETE"
        if completed.returncode != 0 or not accepted:
            stream.write(f"status=FAILED result_status={parsed.get('status')}\n")
            stream.flush()
            failed_log = directory / f"RUN_FAILED_{stamp()}_EXIT_{completed.returncode}.log"
            shutil.copyfile(log, failed_log)
            failed_output = directory / f"OUTPUT_FAILED_{stamp()}_EXIT_{completed.returncode}.json"
            if attempt.exists():
                attempt.replace(failed_output)
            else:
                failed_output.write_text('{"status":"NO_OUTPUT"}\n')
            print("FAILED")
            return completed.returncode or 1

        attempt.replace(output)
        stream.write("status=PASS result_status=COMPLETE\n")
    print(f"PASS elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
