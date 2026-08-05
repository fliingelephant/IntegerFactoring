#!/usr/bin/env python3

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


parser = argparse.ArgumentParser()
parser.add_argument("--run-id", required=True)
parser.add_argument("--timeout-seconds", type=int, required=True)
parser.add_argument("--log", required=True)
parser.add_argument("--status", required=True)
parser.add_argument("command", nargs=argparse.REMAINDER)
args = parser.parse_args()
command = args.command[1:] if args.command[:1] == ["--"] else args.command
if not command:
    parser.error("missing command")

log_path = Path(args.log).resolve()
status_path = Path(args.status).resolve()
log_path.parent.mkdir(parents=True, exist_ok=True)
status_path.parent.mkdir(parents=True, exist_ok=True)
environment = os.environ.copy()
environment["DOT_SAGE"] = "/private/tmp/f04_joint_matroid_audit_sage"
Path(environment["DOT_SAGE"]).mkdir(parents=True, exist_ok=True)
started_utc = datetime.datetime.now(datetime.timezone.utc)
started = time.monotonic()
timed_out = False
exit_code = None
disposition = "failed"

with log_path.open("w", encoding="utf-8") as log:
    log.write(json.dumps({
        "event": "start",
        "run_id": args.run_id,
        "command": command,
        "timeout_seconds": args.timeout_seconds,
        "started_utc": started_utc.isoformat(),
        "DOT_SAGE": environment["DOT_SAGE"],
    }, sort_keys=True) + "\n")
    log.flush()
    process = subprocess.Popen(
        command,
        stdout=log,
        stderr=subprocess.STDOUT,
        env=environment,
        start_new_session=True,
        text=True,
    )
    try:
        exit_code = process.wait(timeout=args.timeout_seconds)
        disposition = "completed" if exit_code == 0 else "failed"
    except subprocess.TimeoutExpired:
        timed_out = True
        disposition = "timed_out"
        os.killpg(process.pid, signal.SIGTERM)
        try:
            exit_code = process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            exit_code = process.wait()
    finished_utc = datetime.datetime.now(datetime.timezone.utc)
    duration = time.monotonic() - started
    log.write(json.dumps({
        "event": "finish",
        "run_id": args.run_id,
        "disposition": disposition,
        "timed_out": timed_out,
        "exit_code": exit_code,
        "duration_seconds": duration,
        "finished_utc": finished_utc.isoformat(),
    }, sort_keys=True) + "\n")

status = {
    "run_id": args.run_id,
    "command": command,
    "timeout_seconds": args.timeout_seconds,
    "started_utc": started_utc.isoformat(),
    "finished_utc": finished_utc.isoformat(),
    "duration_seconds": duration,
    "timed_out": timed_out,
    "exit_code": exit_code,
    "disposition": disposition,
    "log": str(log_path),
    "log_sha256": hashlib.sha256(log_path.read_bytes()).hexdigest(),
}
status_path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
sys.exit(0 if disposition == "completed" else 124 if timed_out else exit_code or 1)
