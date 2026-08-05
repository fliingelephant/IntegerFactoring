#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root";log=logs/run_002_combined.log;:>"$log";failure=outputs/run_002.failure.txt;rm -f "$failure"
shasum -a 256 -c manifests/run_002.inputs.sha256 >>"$log" 2>&1
set +e;/opt/homebrew/bin/timeout --signal=TERM --kill-after=10s 120s bash scripts/finalize_manifest.sh >>"$log" 2>&1;status=$?;set -e
if [[ $status -ne 0 ]];then printf 'run_id=run_002\nexit_status=%s\ndisposition=final artifact verification failed; retain immutable run-001 evidence only\n' "$status">"$failure";exit "$status";fi

