#!/bin/sh
set -eu

export PYTHONDONTWRITEBYTECODE=1

for modulus_id in \
  b20_i0 b20_i1 b28_i0 b28_i1 b36_i0 b36_i1 \
  b44_i0 b44_i1 b60_i0 b60_i1 b92_i0 b92_i1
do
  /opt/homebrew/bin/timeout 30s python3 \
    experiments/F334_count_descent/count_descent.py \
    --mode scale \
    --modulus-id "$modulus_id" \
    --start 0 \
    --stop 256 \
    --output "experiments/F334_count_descent/scale_${modulus_id}_output.json" \
    --status "experiments/F334_count_descent/scale_${modulus_id}_status.json" \
    --traces "experiments/F334_count_descent/scale_${modulus_id}_traces.jsonl.gz" \
    > "experiments/F334_count_descent/scale_${modulus_id}_run.log" 2>&1
done
