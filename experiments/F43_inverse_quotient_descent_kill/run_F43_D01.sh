#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

cd "$(dirname "$0")"
mkdir -p logs output
/opt/homebrew/bin/timeout 120s /usr/local/bin/sage scripts/F43_D01_scan.sage 2>&1 | tee logs/F43-D01.log
