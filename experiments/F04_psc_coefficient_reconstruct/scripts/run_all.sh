#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
timeout_bin=/opt/homebrew/bin/timeout

if [[ ! -f manifests/run_001.inputs.sha256 ]]; then
  echo "missing pre-run source manifest" >&2
  exit 1
fi
shasum -a 256 -c manifests/run_001.inputs.sha256 > logs/run_001_manifest_check.log 2>&1

run_stage() {
  local stage=$1
  local seconds=$2
  shift 2
  local log="logs/run_001_${stage}.log"
  local failure="outputs/run_001_${stage}.failure.txt"
  rm -f "$failure"
  set +e
  "$timeout_bin" --signal=TERM --kill-after=30s "${seconds}s" "$@" > "$log" 2>&1
  local status=$?
  set -e
  if [[ $status -ne 0 ]]; then
    printf 'run_id=run_001\nstage=%s\nexit_status=%s\ntimeout_seconds=%s\ndisposition=failed; preserve artifacts and do not infer the finite claim\n' \
      "$stage" "$status" "$seconds" > "$failure"
    echo "stage $stage failed with status $status" >&2
    exit "$status"
  fi
}

run_stage preflight 120 \
  python3 src/preflight.py --input inputs/parameters.json --output outputs/preflight.json

run_stage theorem_exhaustive 600 \
  python3 src/theorem_exhaustive.py --output outputs/theorem_exhaustive.json

run_stage generate_global 7200 \
  build/generate_global --output outputs/global_vectors.bin \
  --summary outputs/generator_summary.json --threads 10

run_stage verify_complete 14400 \
  build/verify_complete --input outputs/global_vectors.bin \
  --summary outputs/verifier_summary.json --per-shift outputs/per_shift.csv --threads 10

run_stage spot_audit 3600 \
  build/spot_audit --input outputs/global_vectors.bin --output outputs/spot_audit.json

find outputs -type f ! -name 'artifact_audit.json' -print | LC_ALL=C sort | xargs shasum -a 256 \
  > manifests/run_001.outputs.sha256

run_stage artifact_audit 900 \
  python3 src/artifact_audit.py --root "$root" --output outputs/artifact_audit.json

find outputs logs manifests -type f -print | LC_ALL=C sort | xargs shasum -a 256 \
  > manifests/run_001.final.sha256

