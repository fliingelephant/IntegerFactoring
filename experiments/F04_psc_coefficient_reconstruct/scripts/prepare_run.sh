#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
manifest=manifests/run_001.inputs.sha256

files=(
  inputs/parameters.json
  manifests/run_001.plan.json
  src/preflight.py
  src/theorem_exhaustive.py
  src/generate_global.cpp
  src/verify_complete.cpp
  src/spot_audit.cpp
  src/artifact_audit.py
  scripts/build.sh
  scripts/prepare_run.sh
  scripts/run_all.sh
  build/generate_global
  build/verify_complete
  build/spot_audit
)

shasum -a 256 "${files[@]}" > "$manifest"
shasum -a 256 -c "$manifest"

