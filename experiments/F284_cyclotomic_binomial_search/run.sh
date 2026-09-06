#!/usr/bin/env bash
set -euo pipefail

packet_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

python3 "$packet_dir/run_with_timeout.py" \
  --run-id D05 \
  --timeout-seconds 60 \
  --log "$packet_dir/logs/D05.log" \
  --status "$packet_dir/output/D05.status.json" \
  -- /usr/local/bin/sage "$packet_dir/verify_cyclotomic_binomial_jets.sage" \
  --output "$packet_dir/output/D05.json"
