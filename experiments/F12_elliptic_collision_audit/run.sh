#!/usr/bin/env bash
set -euo pipefail

audit_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
project_dir=$(CDPATH= cd -- "$audit_dir/../.." && pwd)
log_path="$audit_dir/logs/R01_artifact_and_certificate_audit.log"
output_path="$audit_dir/output/R01_artifact_and_certificate_audit.json"

: >"$log_path"
{
  echo "approach_family=F12_elliptic_collision_audit"
  echo "status=STARTED"
  echo "timeout_seconds=60"
  python3 --version
} >>"$log_path" 2>&1

set +e
/opt/homebrew/bin/timeout 60s python3 "$audit_dir/audit_artifacts.py" \
  --source-dir "$project_dir/experiments/F12_elliptic_collision_kill" \
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
