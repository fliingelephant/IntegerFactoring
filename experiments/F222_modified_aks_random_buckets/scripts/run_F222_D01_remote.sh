#!/usr/bin/env bash
set -euo pipefail

ulimit -v 2097152
mkdir -p /root/IntegerFactoring_F222/F222-D01/output /root/IntegerFactoring_F222/F222-D01/logs
timeout 900 /root/miniconda3/bin/python \
  /root/IntegerFactoring_F222/F222-D01/scripts/F222_D01_coefficient_search.py \
  --output /root/IntegerFactoring_F222/F222-D01/output/F222-D01.json \
  --p-limit 500 \
  > /root/IntegerFactoring_F222/F222-D01/logs/F222-D01.log 2>&1
