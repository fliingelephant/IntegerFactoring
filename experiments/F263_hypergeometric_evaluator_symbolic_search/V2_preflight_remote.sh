#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F263_V2/F263-D02
check_dir="$work_dir/validation_v2_final_rss"
cd "$work_dir"

if [[ -e "$check_dir" ]]; then
  echo 'F263-D02 final validation directory already exists.' >&2
  exit 81
fi
mkdir "$check_dir"

if ps -eo args | grep -E 'F259-D01.*--(discovery|heldout)|F260-D01.*--(discovery|heldout)|F261-D01.*--(discovery|heldout)|F262-D01.*--(discovery|heldout)|F263-D0[12].*--(discovery|heldout)' | grep -v grep >/dev/null; then
  echo 'F263-D02 validation refuses an active discovery or held-out process.' >&2
  exit 82
fi

{
  date -u +%Y-%m-%dT%H:%M:%SZ
  nproc
  cat /proc/loadavg
  free -h
  df -h /root
  ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 24
} >"$check_dir/resource_before.txt"

timeout 180s nice -n 15 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread \
  V2_symbolic_search.cpp -o V2_symbolic_search.final \
  >"$check_dir/compile.stdout" 2>"$check_dir/compile.stderr"

run_monitored() {
  local mode=$1 limit=$2 pid status peak rss start_ns end_ns
  start_ns=$(date +%s%N)
  timeout "$limit" nice -n 15 ./V2_symbolic_search.final "$mode" \
    >"$check_dir/${mode#--}.stdout" 2>"$check_dir/${mode#--}.stderr" &
  pid=$!
  peak=0
  while kill -0 "$pid" 2>/dev/null; do
    rss=$(ps -eo pid=,ppid=,rss= | awk -v p="$pid" '$1==p||$2==p{s+=$3}END{print s+0}')
    if [[ -n "$rss" && "$rss" -gt "$peak" ]]; then peak=$rss; fi
    sleep 0.1
  done
  set +e
  wait "$pid"
  status=$?
  set -e
  end_ns=$(date +%s%N)
  {
    echo "status=$status"
    echo "peak_rss_kib=$peak"
    echo "elapsed_ns=$((end_ns-start_ns))"
  } >"$check_dir/${mode#--}.monitor"
  [[ $status -eq 0 ]]
}

run_monitored --self-test 300s
run_monitored --benchmark 300s

sha256sum V2_symbolic_search.cpp V2_symbolic_search.final \
  "$check_dir"/* >"$check_dir/final.sha256"
