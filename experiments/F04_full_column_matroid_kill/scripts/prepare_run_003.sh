#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.."&&pwd);cd "$root";files=(src/rescan_patterns.cpp manifests/run_003.plan.json scripts/build_run_003.sh scripts/prepare_run_003.sh scripts/run_003.sh build/rescan_patterns outputs/C_p.bin outputs/C_q.bin outputs/two_by_two_zeros.csv)
shasum -a 256 "${files[@]}" > manifests/run_003.inputs.sha256;shasum -a 256 -c manifests/run_003.inputs.sha256

