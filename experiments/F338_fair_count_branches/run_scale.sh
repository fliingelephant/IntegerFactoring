#!/bin/sh
set -eu

export PYTHONDONTWRITEBYTECODE=1

for modulus_id in \
  b20_i0 b20_i1 b28_i0 b28_i1 b36_i0 b36_i1 \
  b44_i0 b44_i1 b60_i0 b60_i1 b92_i0 b92_i1
do
  for trial_range in 0_64 64_128
  do
    start=${trial_range%_*}
    stop=${trial_range#*_}
    prefix="experiments/F338_fair_count_branches/scale_${modulus_id}_${trial_range}"
    /opt/homebrew/bin/timeout 30s python3 \
      experiments/F338_fair_count_branches/fair_count_branches.py \
      --mode scale \
      --modulus-id "$modulus_id" \
      --start "$start" \
      --stop "$stop" \
      --output "${prefix}_output.json" \
      --status "${prefix}_status.json" \
      --rows "${prefix}_rows.jsonl.gz" \
      --witnesses "${prefix}_witnesses.jsonl.gz" \
      > "${prefix}_run.log" 2>&1
  done
done
