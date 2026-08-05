#!/usr/bin/env bash
set -euo pipefail

experiment_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
log_path="$experiment_dir/logs/R01.log"
output_path="$experiment_dir/output/R01.json"

: >"$log_path"
{
  echo "approach_family=F13_teichmuller_lift_kill"
  echo "status=STARTED"
  echo "timeout_seconds=180"
  python3 --version
} >>"$log_path" 2>&1

set +e
/opt/homebrew/bin/timeout 180s python3 "$experiment_dir/teichmuller_kill.py" \
  --output "$output_path" >>"$log_path" 2>&1
run_status=$?
set -e

if [[ $run_status -eq 0 ]]; then
  echo "status=PASS" >>"$log_path"
elif [[ $run_status -eq 124 ]]; then
  echo "status=TIMEOUT" >>"$log_path"
  exit 124
else
  echo "status=FAIL exit_code=$run_status" >>"$log_path"
  exit "$run_status"
fi
