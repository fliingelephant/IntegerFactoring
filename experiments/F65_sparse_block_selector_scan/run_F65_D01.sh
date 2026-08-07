#!/bin/zsh
set -euo pipefail

experiment_dir=${0:A:h}
log_path="$experiment_dir/logs/F65-D01.log"
output_path="$experiment_dir/output/F65-D01.json"

mkdir -p "$experiment_dir/logs" "$experiment_dir/output"
if [[ -e "$log_path" || -e "$output_path" ]]; then
  print -u2 "refusing to overwrite F65-D01 artifacts"
  exit 2
fi

/opt/homebrew/bin/timeout 300s /opt/homebrew/bin/python3 \
  "$experiment_dir/scripts/F65_D01_scan.py" 2>&1 | tee "$log_path"

