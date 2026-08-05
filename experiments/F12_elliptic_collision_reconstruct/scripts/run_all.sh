#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root";log=logs/run_001_combined.log;:>"$log"
run_stage(){ local stage=$1 seconds=$2;shift 2;local failure="outputs/run_001_${stage}.failure.txt";rm -f "$failure";printf '[%s] start timeout=%ss\n' "$stage" "$seconds">>"$log";set +e;/opt/homebrew/bin/timeout --signal=TERM --kill-after=10s "${seconds}s" "$@">>"$log" 2>&1;local status=$?;set -e;printf '[%s] exit=%s\n' "$stage" "$status">>"$log";if [[ $status -ne 0 ]];then printf 'run_id=run_001\nstage=%s\nexit_status=%s\ndisposition=failed; preserve outputs and infer no unchecked finite value\n' "$stage" "$status">"$failure";exit "$status";fi;}
shasum -a 256 -c manifests/run_001.inputs.sha256 >>"$log" 2>&1
run_stage verify_finite 120 python3 src/verify_finite.py --parameters parameters.json --output outputs/finite_certificate.json
shasum -a 256 outputs/finite_certificate.json > manifests/run_001.primary_outputs.sha256
run_stage audit_finite 120 python3 src/audit_finite.py --parameters parameters.json --certificate outputs/finite_certificate.json --manifest manifests/run_001.primary_outputs.sha256 --output outputs/audit.json

