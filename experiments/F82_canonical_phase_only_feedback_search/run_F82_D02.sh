#!/bin/zsh
set -euo pipefail

experiment_dir="$(cd "$(dirname "$0")" && pwd)"
log_path="$experiment_dir/logs/F82-D02.log"
output_path="$experiment_dir/output/F82-D02.json"

if [[ -e "$log_path" || -e "$output_path" ]]; then
  print -u2 "refusing to overwrite F82-D02 artifacts"
  exit 2
fi

/opt/homebrew/bin/timeout 120s /opt/homebrew/bin/python3 \
  "$experiment_dir/scripts/F82_D02_nonpower_search.py" 2>&1 | tee "$log_path"
