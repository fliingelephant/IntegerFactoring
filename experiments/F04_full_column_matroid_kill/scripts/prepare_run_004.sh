#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
shasum -a 256 manifests/run_004.plan.json scripts/finalize_manifest.sh scripts/prepare_run_004.sh scripts/run_004.sh > manifests/run_004.inputs.sha256
shasum -a 256 -c manifests/run_004.inputs.sha256

