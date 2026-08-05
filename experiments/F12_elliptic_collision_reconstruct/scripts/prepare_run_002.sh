#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
shasum -a 256 manifests/run_002.plan.json scripts/finalize_manifest.sh scripts/prepare_run_002.sh scripts/run_002.sh > manifests/run_002.inputs.sha256
shasum -a 256 -c manifests/run_002.inputs.sha256

