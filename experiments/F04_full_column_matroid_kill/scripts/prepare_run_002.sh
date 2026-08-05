#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd); cd "$root"
files=(manifests/run_002.plan.json src/certify_all.cpp src/audit_all_certificates.py scripts/build_run_002.sh scripts/prepare_run_002.sh scripts/run_002.sh build/certify_all manifests/run_001.primary_outputs.sha256)
shasum -a 256 "${files[@]}" > manifests/run_002.inputs.sha256
shasum -a 256 -c manifests/run_002.inputs.sha256

