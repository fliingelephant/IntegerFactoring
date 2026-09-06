#!/usr/bin/env bash
set -euo pipefail

packet_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

python3 "$packet_dir/run_with_timeout.py" \
  --run-id S01 \
  --timeout-seconds 60 \
  --log "$packet_dir/logs/S01.log" \
  --status "$packet_dir/output/S01.status.json" \
  -- /usr/local/bin/sage "$packet_dir/factor_central_symbolic_jets.sage" \
  --json-output "$packet_dir/output/S01.json" \
  --text-output "$packet_dir/output/S01.txt"
