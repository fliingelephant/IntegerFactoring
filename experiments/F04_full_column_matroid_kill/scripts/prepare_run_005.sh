#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
shasum -a 256 manifests/run_005.plan.json scripts/finalize_manifest.sh scripts/prepare_run_005.sh scripts/run_005.sh > manifests/run_005.inputs.sha256
shasum -a 256 -c manifests/run_005.inputs.sha256

