#!/usr/bin/env bash
set -euo pipefail

run_root=/root/IntegerFactoring_F205/F205-D01
mkdir -p "$run_root/logs" "$run_root/output"

timeout 900 /root/miniconda3/bin/python \
  "$run_root/scripts/F205_D01_joint_selector.py" \
  --output "$run_root/output/F205-D01.json" \
  --rows "$run_root/output/F205-D01.rows.jsonl.gz" \
  --train-count 5000 \
  --holdout-count 2500 \
  --small-p-limit 1000 \
  2>&1 | tee "$run_root/logs/F205-D01.log"

