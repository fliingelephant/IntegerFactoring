#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

cd "$(dirname "$0")"
mkdir -p logs output
/opt/homebrew/bin/timeout 180s python3 scripts/F43_D02_scaling.py 2>&1 | tee logs/F43-D02.log
