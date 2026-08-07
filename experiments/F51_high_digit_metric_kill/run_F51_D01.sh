#!/bin/sh
set -eu

ROOT=/Users/zhou/autoresearch/IntegerFactoring/experiments/F51_high_digit_metric_kill
mkdir -p "$ROOT/logs" "$ROOT/output"
LOG="$ROOT/logs/F51-D01.log"
OUTPUT="$ROOT/output/F51-D01.json"

{
  date -u '+STARTED %Y-%m-%dT%H:%M:%SZ'
  python3 --version
  echo 'TIMEOUT 180s'
} > "$LOG"

/opt/homebrew/bin/timeout 180s python3 "$ROOT/scripts/F51_D01_enumerate.py" --output "$OUTPUT" >> "$LOG" 2>&1
echo 'EXIT 0' >> "$LOG"
