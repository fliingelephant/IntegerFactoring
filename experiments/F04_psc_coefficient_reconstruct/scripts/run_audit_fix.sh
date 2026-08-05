#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
failure=outputs/audit_fix_001.failure.txt
rm -f "$failure"
shasum -a 256 -c manifests/audit_fix_001.inputs.sha256 > logs/audit_fix_001_input_check.log
set +e
/opt/homebrew/bin/timeout --signal=TERM --kill-after=10s 300s bash scripts/finalize_manifest.sh \
  > logs/audit_fix_001.log 2>&1
status=$?
set -e
if [[ $status -ne 0 ]]; then
  printf 'run_id=audit_fix_001\nexit_status=%s\ndisposition=packaging correction failed; primary run outputs remain governed by run_001.outputs.sha256\n' \
    "$status" > "$failure"
  exit "$status"
fi

