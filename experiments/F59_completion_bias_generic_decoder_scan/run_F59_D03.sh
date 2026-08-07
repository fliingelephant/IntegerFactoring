#!/bin/sh
set -eu

experiment_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$experiment_dir"

if [ -e output/F59-D03.json ]; then
  echo "refusing to overwrite output/F59-D03.json" >&2
  exit 2
fi

set +e
DOT_SAGE=/private/tmp/F59-D03-sage-cache \
  /opt/homebrew/bin/timeout 120s /usr/local/bin/sage -python \
  scripts/F59_D03_symbolic_specialization.py >logs/F59-D03.log 2>&1
status=$?
set -e

cat logs/F59-D03.log
exit "$status"
