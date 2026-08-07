#!/bin/sh
set -eu

experiment_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$experiment_dir"

if [ -e output/F59-A03.json ]; then
  echo "refusing to overwrite output/F59-A03.json" >&2
  exit 2
fi

set +e
/opt/homebrew/bin/timeout 60s /opt/homebrew/bin/python3 scripts/F59_A03_replay_audit.py \
  >logs/F59-A03.log 2>&1
status=$?
set -e

cat logs/F59-A03.log
exit "$status"
