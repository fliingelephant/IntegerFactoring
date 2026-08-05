#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
manifest=manifests/run_001.complete.sha256
temporary=$(mktemp /tmp/f04-reconstruct-manifest.XXXXXX)
trap 'rm -f "$temporary"' EXIT

find . -type f \
  ! -path './manifests/run_001.complete.sha256' \
  ! -path './logs/audit_fix_001.log' \
  ! -path './outputs/audit_fix_001_manifest_check.txt' \
  -print | LC_ALL=C sort | sed 's#^./##' | xargs shasum -a 256 > "$temporary"
mv "$temporary" "$manifest"
trap - EXIT
shasum -a 256 -c "$manifest" > outputs/audit_fix_001_manifest_check.txt

