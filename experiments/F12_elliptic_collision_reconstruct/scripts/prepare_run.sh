#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
files=(parameters.json manifests/run_001.plan.json src/verify_finite.py src/audit_finite.py scripts/prepare_run.sh scripts/run_all.sh)
shasum -a 256 "${files[@]}" > manifests/run_001.inputs.sha256
shasum -a 256 -c manifests/run_001.inputs.sha256

