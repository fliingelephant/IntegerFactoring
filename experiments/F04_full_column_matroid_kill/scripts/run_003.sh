#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root";log=logs/run_003_combined.log;:>"$log";failure=outputs/run_003.failure.txt;rm -f "$failure"
shasum -a 256 -c manifests/run_003.inputs.sha256 >>"$log" 2>&1
set +e;/opt/homebrew/bin/timeout --signal=TERM --kill-after=10s 180s build/rescan_patterns --c-p outputs/C_p.bin --c-q outputs/C_q.bin --output outputs/two_by_two_zeros_rescan.csv --summary outputs/rescan_summary.json >>"$log" 2>&1;status=$?;set -e
if [[ $status -eq 0 ]];then cmp outputs/two_by_two_zeros.csv outputs/two_by_two_zeros_rescan.csv >>"$log" 2>&1;status=$?;fi
if [[ $status -ne 0 ]];then printf 'run_id=run_003\nexit_status=%s\ndisposition=independent rescan failed or disagreed; retain run_001 but do not claim rescan confirmation\n' "$status">"$failure";exit "$status";fi
shasum -a 256 outputs/two_by_two_zeros_rescan.csv outputs/rescan_summary.json > manifests/run_003.outputs.sha256

