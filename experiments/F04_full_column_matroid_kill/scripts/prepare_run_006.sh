#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
shasum -a 256 manifests/run_006.plan.json scripts/finalize_manifest.sh scripts/prepare_run_006.sh scripts/run_006.sh > manifests/run_006.inputs.sha256
shasum -a 256 -c manifests/run_006.inputs.sha256

