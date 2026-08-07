#!/bin/zsh
set -euo pipefail

experiment_dir=${0:A:h}
log_path="$experiment_dir/logs/F65-A01.log"
output_path="$experiment_dir/output/F65-A01.json"

if [[ -e "$log_path" || -e "$output_path" ]]; then
  print -u2 "refusing to overwrite F65-A01 artifacts"
  exit 2
fi

/opt/homebrew/bin/timeout 60s /opt/homebrew/bin/python3 \
  "$experiment_dir/scripts/F65_A01_audit.py" 2>&1 | tee "$log_path"

