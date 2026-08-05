#!/bin/zsh
set -euo pipefail

ROOT=/Users/zhou/autoresearch/IntegerFactoring
AUDIT_DIR="$ROOT/experiments/F15_hurwitz_bias_audit"
CANDIDATE_OUTPUT="$ROOT/experiments/F15_hurwitz_bias_kill/output/F15-B01.json"
LOG="$AUDIT_DIR/logs/F15-BA01.log"
OUTPUT="$AUDIT_DIR/output/F15-BA01.json"

mkdir -p "$AUDIT_DIR/logs" "$AUDIT_DIR/output"

{
  echo "RUN F15-BA01"
  echo "FAMILY F15_hurwitz_bias_audit"
  echo "TIMEOUT 120s"
  echo "STARTED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  /opt/homebrew/bin/timeout 120s python3 "$AUDIT_DIR/scripts/F15_BA01_independent.py" \
    --candidate-output "$CANDIDATE_OUTPUT" \
    --output "$OUTPUT"
  echo "FINISHED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} 2>&1 | tee "$LOG"
