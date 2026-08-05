#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
shasum -a 256 -c manifests/run_001.inputs.sha256
shasum -a 256 -c manifests/run_001.primary_outputs.sha256
temporary=$(mktemp /tmp/f12-reconstruct-final.XXXXXX);trap 'rm -f "$temporary"' EXIT
find . -type f ! -path './manifests/final_artifacts.sha256' \
  ! -path './logs/run_002_combined.log' ! -path './outputs/run_002.failure.txt' \
  -print | LC_ALL=C sort | sed 's#^./##' | xargs shasum -a 256 > "$temporary"
mv "$temporary" manifests/final_artifacts.sha256;trap - EXIT
shasum -a 256 -c manifests/final_artifacts.sha256

