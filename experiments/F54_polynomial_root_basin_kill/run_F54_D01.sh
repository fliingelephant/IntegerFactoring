#!/bin/sh
set -eu

BASE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
LOG="$BASE_DIR/logs/F54-D01.log"

{
  python3 --version
  echo "timeout_seconds=60"
  /opt/homebrew/bin/timeout 60s python3 "$BASE_DIR/scripts/F54_D01_exact_basins.py"
  status=$?
  echo "EXIT $status"
  exit "$status"
} >"$LOG" 2>&1
