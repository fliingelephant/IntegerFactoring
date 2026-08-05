#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
shasum -a 256 \
  manifests/audit_fix_001.plan.json \
  scripts/finalize_manifest.sh \
  scripts/prepare_audit_fix.sh \
  scripts/run_audit_fix.sh \
  > manifests/audit_fix_001.inputs.sha256
shasum -a 256 -c manifests/audit_fix_001.inputs.sha256

