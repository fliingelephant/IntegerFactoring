#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F264/F264-D01
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"

sha256sum -c FROZEN.sha256

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D01|F260-D01|F261-D01|F262-D01|F263-D01' \
      | grep -v grep >/dev/null; then
    echo 'F264 refuses to overlap F258 through F263 production or validation.' >&2
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

refuse_overlap
timeout 900s nice -n 15 ./symbolic_search --self-test \
  >"$log_dir/self_test.stdout" 2>"$log_dir/self_test.stderr"
timeout 1800s nice -n 15 ./symbolic_search --benchmark \
  >"$log_dir/benchmark.stdout" 2>"$log_dir/benchmark.stderr"

projection=$(sed -n 's/.*projected_8thread_seconds_1.75x=\([0-9.]*\).*/\1/p' \
  "$log_dir/benchmark.stdout")
if [[ -z "$projection" ]] || ! awk -v x="$projection" 'BEGIN {exit !(x <= 14400)}'; then
  echo "F264 refuses runtime projection: $projection" >&2
  exit 75
fi

description=$(./symbolic_search --describe)
candidates=$(sed -n 's/.*candidates=\([0-9]*\).*/\1/p' <<<"$description")
predicted_bytes=$((5280 * 32768 + candidates * 1536 + 33554432))
if (( predicted_bytes > 1073741824 )); then
  echo "F264 refuses predicted output bytes: $predicted_bytes" >&2
  exit 74
fi

deadline=$((SECONDS + 14400))
start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
refuse_overlap
set +e
(
  ulimit -v 4194304
  timeout "$((deadline - SECONDS))s" nice -n 15 ./symbolic_search 8 \
    "$out_dir/F264-D01.summary.json" "$out_dir/F264-D01.rows.tsv" \
    "$out_dir/F264-D01.anomalies.tsv"
) >"$log_dir/cohorts.stdout" 2>"$log_dir/cohorts.stderr"
status=$?
set -e
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

output_bytes=$(du -sb "$out_dir" | cut -f1)
if (( output_bytes > 1073741824 )); then
  echo "F264 output exceeded 1 GiB: $output_bytes" >&2
  exit 74
fi
for file in "$out_dir/F264-D01.rows.tsv" "$out_dir/F264-D01.anomalies.tsv"; do
  if [[ -f "$file" ]]; then gzip -9 "$file"; fi
done

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "exit_status=$status"
  echo "benchmark_projection_seconds=$projection"
  echo "predicted_bytes=$predicted_bytes"
  echo "output_bytes=$output_bytes"
  sha256sum PREREGISTRATION.md ALGEBRA.md symbolic_search.cpp remote_run.sh \
    FROZEN.sha256 VALIDATION_PENDING.md 2>/dev/null || true
  find "$out_dir" "$log_dir" -type f ! -name F264-D01.manifest -print0 \
    | sort -z | xargs -0 sha256sum
} >"$log_dir/F264-D01.manifest"

exit "$status"
