#!/usr/bin/env python3
"""Named hard-timeout runner for the registered F118 search."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time


HARD_TIMEOUT_SECONDS = 1200


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    directory = Path(__file__).resolve().parent
    registration_path = directory / "REGISTRATION.json"
    registration = json.loads(registration_path.read_text())
    for name, expected in registration["sha256"].items():
        actual = sha256_file(directory / name)
        if actual != expected:
            raise AssertionError(f"registered artifact changed: {name}: {actual} != {expected}")
    if registration["hard_timeout_seconds"] != HARD_TIMEOUT_SECONDS:
        raise AssertionError("registered timeout changed")

    scanner = directory / "scan_full_source.py"
    corpus = directory / "CORPUS_SPEC.json"
    attempt = directory / f"ATTEMPT_{stamp()}.json"
    log = directory / "RUN.log"
    output = directory / "OUTPUT.json"
    command = [
        "/usr/local/bin/sage",
        "-python",
        str(scanner),
        "--spec",
        str(corpus),
        "--output",
        str(attempt),
    ]
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as stream:
        stream.write("named_timeout=F118_58BIT_FULL_SOURCE_NULL_HARD_TIMEOUT\n")
        stream.write(f"hard_timeout_seconds={HARD_TIMEOUT_SECONDS}\n")
        stream.write(f"registration_sha256={sha256_file(registration_path)}\n")
        stream.write(f"started_utc={datetime.now(timezone.utc).isoformat()}\n")
        stream.write("command=" + json.dumps(command) + "\n")
        stream.flush()
        try:
            completed = subprocess.run(
                command,
                cwd=directory,
                stdout=stream,
                stderr=subprocess.STDOUT,
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
            print(f"TIMEOUT after {elapsed:.3f}s; preserved {failed_log} and {failed_output}")
            return 124

        elapsed = time.monotonic() - started
        stream.write(f"returncode={completed.returncode}\nelapsed_seconds={elapsed:.6f}\n")
        parsed = json.loads(attempt.read_text()) if attempt.exists() else {"status": "NO_OUTPUT"}
        accepted = parsed.get("status") in {"NULL_FOUND", "CAP_COMPLETE_NO_NULL"}
        if completed.returncode != 0 or not accepted:
            stream.write(f"status=FAILED result_status={parsed.get('status')}\n")
            stream.flush()
            failed_log = directory / f"RUN_FAILED_{stamp()}_EXIT_{completed.returncode}.log"
            shutil.copyfile(log, failed_log)
            failed_output = directory / f"OUTPUT_FAILED_{stamp()}_EXIT_{completed.returncode}.json"
            if attempt.exists():
                attempt.replace(failed_output)
            else:
                failed_output.write_text(json.dumps(parsed) + "\n")
            print(f"FAILED; preserved {failed_log} and {failed_output}")
            return completed.returncode or 1

        attempt.replace(output)
        stream.write(f"status=PASS result_status={parsed['status']}\n")
    print(f"PASS result_status={parsed['status']} elapsed_seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
