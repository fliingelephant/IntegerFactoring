#!/usr/bin/env python3
"""Run one immutable, hard-timed experiment and retain its full provenance."""

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import signal
import subprocess
import sys
import time


parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--timeout", required=True, type=int)
parser.add_argument("command", nargs=argparse.REMAINDER)
args = parser.parse_args()

if not args.command or args.command[0] != "--":
    raise SystemExit("command must follow --")
command = args.command[1:]

root = pathlib.Path(__file__).resolve().parents[1]
run_dir = root / "runs" / args.name
run_dir.mkdir(parents=True, exist_ok=False)
stdout_path = run_dir / "stdout.log"
stderr_path = run_dir / "stderr.log"
started = datetime.datetime.now(datetime.timezone.utc)
start_clock = time.monotonic()
timed_out = False
interrupted = False

environment = os.environ.copy()
environment["F04_RECONSTRUCT_RUN_DIR"] = str(run_dir)
environment["DOT_SAGE"] = str(run_dir / "dot_sage")

with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
    process = subprocess.Popen(
        command,
        cwd=root,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=stdout_file,
        stderr=stderr_file,
        start_new_session=True,
    )
    (run_dir / "process_id.txt").write_text(f"{process.pid}\n", encoding="ascii")
    try:
        return_code = process.wait(timeout=args.timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(process.pid, signal.SIGKILL)
        return_code = process.wait()
    except KeyboardInterrupt:
        interrupted = True
        os.killpg(process.pid, signal.SIGKILL)
        return_code = process.wait()

finished = datetime.datetime.now(datetime.timezone.utc)

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


files = {}
for path in sorted(root.rglob("*")):
    if path.is_file() and path != run_dir / "manifest.json":
        files[str(path.relative_to(root))] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

manifest = {
    "schema": 1,
    "name": args.name,
    "command": command,
    "cwd": str(root),
    "timeout_seconds": args.timeout,
    "timed_out": timed_out,
    "interrupted": interrupted,
    "return_code": return_code,
    "started_utc": started.isoformat(),
    "finished_utc": finished.isoformat(),
    "elapsed_seconds": time.monotonic() - start_clock,
    "python": sys.version,
    "files": files,
}
(run_dir / "manifest.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

print(json.dumps({
    "run_dir": str(run_dir),
    "return_code": return_code,
    "timed_out": timed_out,
}, sort_keys=True))
raise SystemExit(130 if interrupted else (124 if timed_out else return_code))
