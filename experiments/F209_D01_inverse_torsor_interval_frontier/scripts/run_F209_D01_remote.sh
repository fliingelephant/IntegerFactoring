#!/usr/bin/env bash
set -euo pipefail

run_root=/root/IntegerFactoring_F209/F209-D01
source_file="$run_root/scripts/F209_D01_inverse_torsor_frontier.py"
expected_source_sha=61b13495b8455b2697b983668602829053c297a8fc68e08188966ea824634d6a

mkdir -p "$run_root/logs" "$run_root/output"
exec > >(tee "$run_root/logs/F209-D01.log") 2>&1

actual_source_sha=$(sha256sum "$source_file" | awk '{print $1}')
if [[ "$actual_source_sha" != "$expected_source_sha" ]]; then
  echo "source hash mismatch: expected=$expected_source_sha actual=$actual_source_sha"
  exit 40
fi

cpu_count=$(nproc)
load_one=$(awk '{print $1}' /proc/loadavg)
memory_available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
disk_available_kib=$(df -Pk "$run_root" | awk 'NR==2 {print $4}')

echo "preflight cpu_count=$cpu_count load_one=$load_one memory_available_kib=$memory_available_kib disk_available_kib=$disk_available_kib"
ps -eo pid,ppid,pcpu,pmem,rss,etime,comm --sort=-pcpu

awk -v load="$load_one" -v cpus="$cpu_count" 'BEGIN { if (load > 2 * cpus) exit 1 }' || {
  echo "preflight abort: one-minute load exceeds twice CPU count"
  exit 41
}
if (( memory_available_kib < 16777216 )); then
  echo "preflight abort: available memory below 16 GiB"
  exit 42
fi
if (( disk_available_kib < 5242880 )); then
  echo "preflight abort: free disk below 5 GiB"
  exit 43
fi

ulimit -v 8388608

timeout 1800 /root/miniconda3/bin/python \
  "$source_file" \
  --output "$run_root/output/F209-D01.json" \
  --rows "$run_root/output/F209-D01.rows.jsonl.gz" \
  --train-count 256 \
  --holdout-count 64 \
  --small-p-limit 1000 \
  --max-p-representatives 2000000
