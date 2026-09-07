#!/bin/sh
set -eu

modulus_id="$1"
start="$2"
stop="$3"
directory="experiments/F336_biased_rational_inputs"
prefix="scale_${modulus_id}_${start}_${stop}"

exec /opt/homebrew/bin/gtimeout --preserve-status --signal=TERM 30s \
  python3 "$directory/biased_rational_inputs.py" \
  --mode scale \
  --modulus-id "$modulus_id" \
  --start "$start" \
  --stop "$stop" \
  --output "$directory/${prefix}_output.json" \
  --status "$directory/${prefix}_status.json" \
  --rows "$directory/${prefix}_rows.jsonl.gz" \
  --witnesses "$directory/${prefix}_witnesses.jsonl.gz"
