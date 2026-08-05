#!/bin/zsh
set -euo pipefail

ROOT=/Users/zhou/autoresearch/IntegerFactoring
RUN_DIR="$ROOT/experiments/F15_hurwitz_bias_kill"
LOG="$RUN_DIR/logs/F15-B01.log"
OUTPUT="$RUN_DIR/output/F15-B01.json"

mkdir -p "$RUN_DIR/logs" "$RUN_DIR/output"

{
  echo "RUN F15-B01"
  echo "FAMILY F15_hurwitz_bias_kill"
  echo "TIMEOUT 120s"
  echo "STARTED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  /opt/homebrew/bin/timeout 120s python3 "$RUN_DIR/scripts/F15_B01_coordinate_slice.py" --output "$OUTPUT"
  echo "FINISHED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} 2>&1 | tee "$LOG"
