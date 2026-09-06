#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F263/F263-D01
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"

sha256sum -c FROZEN.sha256

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D01|F260-D01|F261-D01|F262-D01' | grep -v grep >/dev/null; then
    echo 'F263 refuses to overlap F258 through F262 production.' >&2
    exit 73
  fi
}

refuse_overlap
date -u +%Y-%m-%dT%H:%M:%SZ >"$log_dir/resource_before.txt"
nproc >>"$log_dir/resource_before.txt"
cat /proc/loadavg >>"$log_dir/resource_before.txt"
free -h >>"$log_dir/resource_before.txt"
df -h /root >>"$log_dir/resource_before.txt"
ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32 \
  >>"$log_dir/resource_before.txt"

/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread symbolic_search.cpp -o symbolic_search
timeout 180s nice -n 15 ./symbolic_search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))
refuse_overlap
set +e
(
  ulimit -v 4194304
  timeout "$((deadline - SECONDS))s" nice -n 15 \
    ./symbolic_search --discovery "$out_dir" 8 full
) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"
discovery_status=$?
set -e

if [[ $discovery_status -ne 0 ]]; then
  heldout_status=125
else
  sha256sum "$out_dir/F263-D01.selection.tsv" \
    >"$out_dir/F263-D01.selection.sha256"
  expected=$(cut -d' ' -f1 "$out_dir/F263-D01.selection.sha256")
  observed=$(sha256sum "$out_dir/F263-D01.selection.tsv" | cut -d' ' -f1)
  if [[ "$expected" != "$observed" ]]; then
    echo 'F263 selection hash mismatch.' >&2
    exit 74
  fi
  refuse_overlap
  remaining=$((deadline - SECONDS))
  set +e
  if [[ $remaining -le 0 ]]; then
    heldout_status=124
  else
    (
      ulimit -v 4194304
      timeout "${remaining}s" nice -n 15 \
        ./symbolic_search --heldout "$out_dir" \
        "$out_dir/F263-D01.selection.tsv" 8 full
    ) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"
    heldout_status=$?
  fi
  set -e
fi

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
output_bytes=$(du -sb "$out_dir" | cut -f1)
if [[ $output_bytes -gt 1073741824 ]]; then
  echo 'F263 output exceeded the frozen 1 GiB cap.' >&2
  exit 75
fi

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "discovery_status=$discovery_status"
  echo "heldout_status=$heldout_status"
  echo "output_bytes=$output_bytes"
  sha256sum PREREGISTRATION.md ALGEBRA.md symbolic_search.cpp \
    remote_run.sh FROZEN.sha256 symbolic_search 2>/dev/null || true
  find "$out_dir" "$log_dir" -type f \
    ! -name F263-D01.manifest -print0 | sort -z | xargs -0 sha256sum
} >"$log_dir/F263-D01.manifest"

if [[ $discovery_status -ne 0 ]]; then exit "$discovery_status"; fi
exit "$heldout_status"
