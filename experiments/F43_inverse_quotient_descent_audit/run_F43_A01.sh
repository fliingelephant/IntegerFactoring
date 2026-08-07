#!/bin/sh
set -eu

BASE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
LOG="$BASE_DIR/logs/F43-A01.log"

{
  python3 --version
  echo "timeout_seconds=120"
  /opt/homebrew/bin/timeout 120s python3 "$BASE_DIR/audit_artifacts.py"
  status=$?
  echo "EXIT $status"
  exit "$status"
} >"$LOG" 2>&1
