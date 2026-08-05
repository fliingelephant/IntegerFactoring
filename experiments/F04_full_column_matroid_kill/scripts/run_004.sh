#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root";log=logs/run_004_combined.log;:>"$log";failure=outputs/run_004.failure.txt;rm -f "$failure"
shasum -a 256 -c manifests/run_004.inputs.sha256 >>"$log" 2>&1
set +e;/opt/homebrew/bin/timeout --signal=TERM --kill-after=10s 120s bash scripts/finalize_manifest.sh >>"$log" 2>&1;status=$?;set -e
if [[ $status -ne 0 ]];then printf 'run_id=run_004\nexit_status=%s\ndisposition=final artifact verification failed; use the earlier immutable run manifests only\n' "$status">"$failure";exit "$status";fi

