#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F260/F260-D01
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"

if ps -eo args | grep -E 'F258-D01|F259-D01|F261-D01' | grep -v grep >/dev/null; then
  echo 'F260 refuses to overlap F258, F259, or F261 production.' >&2
  exit 73
fi

date -u +%Y-%m-%dT%H:%M:%SZ >"$log_dir/resource_before.txt"
nproc >>"$log_dir/resource_before.txt"
cat /proc/loadavg >>"$log_dir/resource_before.txt"
free -h >>"$log_dir/resource_before.txt"
df -h /root >>"$log_dir/resource_before.txt"
ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32 \
  >>"$log_dir/resource_before.txt"

/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread search.cpp -o search
timeout 120s nice -n 15 ./search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))
set +e
(
  ulimit -v 4194304
  timeout "$((deadline - SECONDS))s" nice -n 15 \
    ./search --discovery "$out_dir" 8 full
) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"
discovery_status=$?
set -e

if [[ $discovery_status -ne 0 ]]; then
  heldout_status=125
else
  sha256sum "$out_dir/F260-D01.selection.tsv" \
    >"$out_dir/F260-D01.selection.sha256"
  selection_hash=$(cut -d' ' -f1 "$out_dir/F260-D01.selection.sha256")
  actual_hash=$(sha256sum "$out_dir/F260-D01.selection.tsv" | cut -d' ' -f1)
  if [[ "$selection_hash" != "$actual_hash" ]]; then
    echo 'Selection manifest hash mismatch.' >&2
    exit 74
  fi
  set +e
  remaining=$((deadline - SECONDS))
  if [[ $remaining -le 0 ]]; then
    heldout_status=124
  else
  (
    ulimit -v 4194304
    timeout "${remaining}s" nice -n 15 ./search --heldout "$out_dir" \
      "$out_dir/F260-D01.selection.tsv" 8 full
  ) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"
  heldout_status=$?
  fi
  set -e
fi

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
output_bytes=$(du -sb "$out_dir" | cut -f1)
if [[ $output_bytes -gt 1073741824 ]]; then
  echo 'F260 output exceeded the frozen 1 GiB cap.' >&2
  exit 75
fi

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "discovery_status=$discovery_status"
  echo "heldout_status=$heldout_status"
  echo "output_bytes=$output_bytes"
  sha256sum ALGEBRA.md PREREGISTRATION.md search.cpp remote_run.sh search 2>/dev/null || true
  find "$out_dir" "$log_dir" -type f \
    ! -name F260-D01.manifest -print0 | sort -z | xargs -0 sha256sum
} >"$log_dir/F260-D01.manifest"

if [[ $discovery_status -ne 0 ]]; then exit "$discovery_status"; fi
exit "$heldout_status"
