#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root"
for manifest in manifests/run_001.inputs.sha256 manifests/run_001.primary_outputs.sha256 \
  manifests/run_002.inputs.sha256 manifests/run_002.outputs.sha256 \
  manifests/run_003.inputs.sha256 manifests/run_003.outputs.sha256;do
  shasum -a 256 -c "$manifest"
done
temporary=$(mktemp /tmp/f04-full-column-final.XXXXXX);trap 'rm -f "$temporary"' EXIT
find . -type f ! -path './manifests/final_artifacts.sha256' \
  ! -path './outputs/run_006.failure.txt' \
  ! -path './logs/run_006_combined.log' -print | LC_ALL=C sort | sed 's#^./##' | \
  xargs shasum -a 256 > "$temporary"
mv "$temporary" manifests/final_artifacts.sha256;trap - EXIT
shasum -a 256 -c manifests/final_artifacts.sha256
