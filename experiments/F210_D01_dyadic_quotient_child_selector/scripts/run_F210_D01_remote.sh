#!/usr/bin/env bash
set -euo pipefail

run_root=/root/IntegerFactoring_F210/F210-D01
source_file="$run_root/scripts/F210_D01_dyadic_quotient_selector.py"
expected_source_sha=32d0b4f8ad5141433e7f6d547242620df421f53702ade39d27587ba2079e5648

mkdir -p "$run_root/logs" "$run_root/output"
exec > >(tee "$run_root/logs/F210-D01.log") 2>&1

actual_source_sha=$(sha256sum "$source_file" | awk '{print $1}')
if [[ "$actual_source_sha" != "$expected_source_sha" ]]; then
  echo "source hash mismatch: expected=$expected_source_sha actual=$actual_source_sha"
  exit 40
fi

python_runtime=/root/miniconda3/bin/python
if [[ ! -x "$python_runtime" ]]; then
  echo "preflight abort: missing runtime $python_runtime"
  exit 41
fi

cpu_count=$(nproc)
load_one=$(awk '{print $1}' /proc/loadavg)
memory_available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
disk_available_kib=$(df -Pk "$run_root" | awk 'NR==2 {print $4}')

echo "preflight cpu_count=$cpu_count load_one=$load_one memory_available_kib=$memory_available_kib disk_available_kib=$disk_available_kib"
"$python_runtime" -c 'import sys, sympy; print("python=" + sys.version.replace("\n", " ")); print("sympy=" + sympy.__version__)'
ps -eo pid,ppid,pcpu,pmem,rss,etime,comm --sort=-pcpu

awk -v load="$load_one" -v cpus="$cpu_count" 'BEGIN { if (load > 2 * cpus) exit 1 }' || {
  echo "preflight abort: one-minute load exceeds twice CPU count"
  exit 42
}
if (( memory_available_kib < 16777216 )); then
  echo "preflight abort: available memory below 16 GiB"
  exit 43
fi
if (( disk_available_kib < 5242880 )); then
  echo "preflight abort: free disk below 5 GiB"
  exit 44
fi

ulimit -v 8388608

timeout 1800 "$python_runtime" \
  "$source_file" \
  --output "$run_root/output/F210-D01.json" \
  --rows "$run_root/output/F210-D01.rows.jsonl.gz" \
  --train-count 2000 \
  --holdout-count 1000 \
  --small-p-limit 500
