#!/bin/sh
set -eu

experiment_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$experiment_dir"

/opt/homebrew/bin/timeout 600s /opt/homebrew/bin/python3 scripts/F59_D01_scan.py 2>&1 \
  | tee logs/F59-D01.log
