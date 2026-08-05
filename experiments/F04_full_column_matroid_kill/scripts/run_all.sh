#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
combined=logs/run_001_combined.log
: > "$combined"

run_stage() {
  local stage=$1
  local seconds=$2
  shift 2
  local failure="outputs/run_001_${stage}.failure.txt"
  rm -f "$failure"
  printf '[%s] start timeout=%ss\n' "$stage" "$seconds" >> "$combined"
  set +e
  /opt/homebrew/bin/timeout --signal=TERM --kill-after=30s "${seconds}s" "$@" >> "$combined" 2>&1
  local status=$?
  set -e
  printf '[%s] exit=%s\n' "$stage" "$status" >> "$combined"
  if [[ $status -ne 0 ]]; then
    printf 'run_id=run_001\nstage=%s\nexit_status=%s\ntimeout_seconds=%s\ndisposition=failed; preserve all artifacts and infer no unverified zero pattern\n' \
      "$stage" "$status" "$seconds" > "$failure"
    exit "$status"
  fi
}

shasum -a 256 -c manifests/run_001.inputs.sha256 >> "$combined" 2>&1
run_stage compute_exchange 1800 build/compute_exchange \
  --global outputs/global_matrix.bin --c-p outputs/C_p.bin --c-q outputs/C_q.bin \
  --entries outputs/entry_zeros.csv --minors outputs/two_by_two_zeros.csv \
  --summary outputs/summary.json --threads 10

shasum -a 256 outputs/global_matrix.bin outputs/C_p.bin outputs/C_q.bin \
  outputs/entry_zeros.csv outputs/two_by_two_zeros.csv outputs/summary.json \
  > manifests/run_001.primary_outputs.sha256

run_stage audit_outputs 600 python3 src/audit_outputs.py --root "$root" \
  --output outputs/audit.json

find outputs logs manifests -type f ! -name 'run_001.complete.sha256' -print | \
  LC_ALL=C sort | xargs shasum -a 256 > manifests/run_001.complete.sha256

