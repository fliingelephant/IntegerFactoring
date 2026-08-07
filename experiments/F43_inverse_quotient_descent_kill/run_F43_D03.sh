#!/bin/sh
set -eu

BASE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
LOG="$BASE_DIR/logs/F43-D03.log"

{
  python3 --version
  echo "timeout_seconds=120"
  /opt/homebrew/bin/timeout 120s python3 "$BASE_DIR/scripts/F43_D03_two_step_contraction.py"
  status=$?
  echo "EXIT $status"
  exit "$status"
} >"$LOG" 2>&1
