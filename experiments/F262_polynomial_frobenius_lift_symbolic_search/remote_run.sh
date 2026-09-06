#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F262/F262-D01
mkdir -p "$work_dir/output" "$work_dir/logs"
cd "$work_dir"

sha256sum -c FROZEN.sha256

conflict_pattern='F258-D01|F259-D01|F260-D01|F261-D01|F258_|F259_|F260_|F261_'
if pgrep -af "$conflict_pattern" >/dev/null; then
  echo 'REFUSE_INCOMPATIBLE_ACTIVE_PRECOMPILE' >&2
  exit 73
fi

/usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread symbolic_search.cpp -o symbolic_search

if pgrep -af "$conflict_pattern" >/dev/null; then
  echo 'REFUSE_INCOMPATIBLE_ACTIVE_PREVALIDATION' >&2
  exit 73
fi

timeout 900s nice -n 15 ./symbolic_search --self-test \
  >logs/F262-D01.self_test.log 2>&1
timeout 1800s nice -n 15 ./symbolic_search --benchmark \
  >logs/F262-D01.benchmark.log 2>&1

projection=$(sed -n 's/.*projected_8thread_seconds_1.75x=\([0-9.]*\).*/\1/p' logs/F262-D01.benchmark.log)
if [[ -z "$projection" ]] || ! awk -v x="$projection" 'BEGIN {exit !(x <= 14400)}'; then
  echo "REFUSE_RUNTIME_PROJECTION=$projection" >&2
  exit 75
fi

description=$(./symbolic_search --describe)
candidate_count=$(sed -n 's/.*candidates=\([0-9]*\).*/\1/p' <<<"$description")
predicted_bytes=$((5280 * 32768 + candidate_count * 1024 + 10485760))
if (( predicted_bytes > 1073741824 )); then
  echo "REFUSE_PREDICTED_OUTPUT_BYTES=$predicted_bytes" >&2
  exit 74
fi

if pgrep -af "$conflict_pattern" >/dev/null; then
  echo 'REFUSE_INCOMPATIBLE_ACTIVE_PRECOHORT' >&2
  exit 73
fi

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
(
  ulimit -v 4194304
  timeout 14400s nice -n 15 ./symbolic_search 8 \
    output/F262-D01.summary.json output/F262-D01.rows.tsv \
    output/F262-D01.anomalies.tsv
) >logs/F262-D01.stdout 2>logs/F262-D01.stderr
status=$?
set -e
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

for file in output/F262-D01.rows.tsv output/F262-D01.anomalies.tsv; do
  if [[ -f "$file" ]]; then
    bytes=$(stat -c %s "$file")
    if (( bytes > 1073741824 )); then
      echo "REFUSE_OUTPUT_BYTES=$bytes file=$file" >&2
      status=74
    fi
    gzip -9 "$file"
  fi
done

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "exit_status=$status"
  echo "predicted_bytes=$predicted_bytes"
  echo "benchmark_projection_seconds=$projection"
  sha256sum PREREGISTRATION.md ALGEBRA.md symbolic_search.cpp remote_run.sh FROZEN.sha256 VALIDATION_PENDING.md 2>/dev/null || true
  sha256sum output/F262-D01.summary.json output/F262-D01.rows.tsv.gz output/F262-D01.anomalies.tsv.gz 2>/dev/null || true
  sha256sum logs/F262-D01.* 2>/dev/null || true
} >logs/F262-D01.manifest

exit "$status"
