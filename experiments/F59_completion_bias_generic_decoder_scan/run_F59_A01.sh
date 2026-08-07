#!/bin/sh
set -eu

experiment_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$experiment_dir"

/opt/homebrew/bin/timeout 60s /opt/homebrew/bin/python3 scripts/F59_A01_audit.py 2>&1 \
  | tee logs/F59-A01.log
