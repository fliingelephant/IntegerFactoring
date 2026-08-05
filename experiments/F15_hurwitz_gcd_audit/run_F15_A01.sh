#!/bin/zsh
set -euo pipefail

ROOT=/Users/zhou/autoresearch/IntegerFactoring
AUDIT_DIR="$ROOT/experiments/F15_hurwitz_gcd_audit"
LOG="$AUDIT_DIR/logs/F15-A01.log"
OUTPUT="$AUDIT_DIR/output/F15-A01.json"

{
  echo "RUN F15-A01"
  echo "FAMILY F15_hurwitz_gcd_audit"
  echo "TIMEOUT 60s"
  echo "STARTED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  /opt/homebrew/bin/timeout 60s python3 "$AUDIT_DIR/scripts/F15_A01_exact_small.py" --output "$OUTPUT"
  echo "FINISHED $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} 2>&1 | tee "$LOG"
