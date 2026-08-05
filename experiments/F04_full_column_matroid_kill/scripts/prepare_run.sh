#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
files=(parameters.json manifests/run_001.plan.json src/compute_exchange.cpp src/audit_outputs.py \
       scripts/build.sh scripts/prepare_run.sh scripts/run_all.sh build/compute_exchange)
shasum -a 256 "${files[@]}" > manifests/run_001.inputs.sha256
shasum -a 256 -c manifests/run_001.inputs.sha256

