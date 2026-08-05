#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
combined=logs/run_002_combined.log
: > "$combined"

run_stage() {
  local stage=$1 seconds=$2; shift 2; local failure="outputs/run_002_${stage}.failure.txt"; rm -f "$failure"
  printf '[%s] start timeout=%ss\n' "$stage" "$seconds" >> "$combined"; set +e
  /opt/homebrew/bin/timeout --signal=TERM --kill-after=30s "${seconds}s" "$@" >> "$combined" 2>&1; local status=$?; set -e
  printf '[%s] exit=%s\n' "$stage" "$status" >> "$combined"
  if [[ $status -ne 0 ]]; then printf 'run_id=run_002\nstage=%s\nexit_status=%s\ndisposition=failed; preserve run_001 and infer no missing certificate\n' "$stage" "$status" > "$failure"; exit "$status"; fi
}
shasum -a 256 -c manifests/run_002.inputs.sha256 >> "$combined" 2>&1
shasum -a 256 -c manifests/run_001.primary_outputs.sha256 >> "$combined" 2>&1
run_stage certify_all 600 build/certify_all --global outputs/global_matrix.bin --c-p outputs/C_p.bin --c-q outputs/C_q.bin --records outputs/two_by_two_zeros.csv --output outputs/all_exchange_certificates.csv --summary outputs/certify_all_summary.json
shasum -a 256 outputs/all_exchange_certificates.csv outputs/certify_all_summary.json > manifests/run_002.outputs.sha256
run_stage audit_all_certificates 120 python3 src/audit_all_certificates.py --root "$root" --output outputs/audit_all_certificates.json
