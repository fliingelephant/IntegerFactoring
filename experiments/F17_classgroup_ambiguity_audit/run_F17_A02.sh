#!/bin/sh
set -eu

AUDIT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUTPUT="$AUDIT_DIR/artifacts/F17_A02_output.json"
LOG="$AUDIT_DIR/runs/F17_A02.log"

mkdir -p "$AUDIT_DIR/artifacts" "$AUDIT_DIR/runs"
/opt/homebrew/bin/timeout 300 /usr/local/bin/sage \
  "$AUDIT_DIR/scripts/F17_A02_exhaustive_json_fix.sage" "$OUTPUT" 2>&1 | tee "$LOG"
