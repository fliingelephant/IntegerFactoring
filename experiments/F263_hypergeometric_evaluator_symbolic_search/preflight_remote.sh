#!/usr/bin/env bash
set -euo pipefail

cd /root/IntegerFactoring_F263/F263-D01
mkdir -p preflight

: >preflight/compile_final.stdout
: >preflight/compile_final.stderr
/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread symbolic_search.cpp \
  -o symbolic_search >preflight/compile_final.stdout \
  2>preflight/compile_final.stderr

: >preflight/selftest_final.stdout
: >preflight/selftest_final.stderr
timeout 180s nice -n 15 ./symbolic_search --self-test \
  >preflight/selftest_final.stdout 2>preflight/selftest_final.stderr

: >preflight/benchmark_final.stdout
: >preflight/benchmark_final.stderr
start_ns=$(date +%s%N)
timeout 180s nice -n 15 ./symbolic_search --benchmark \
  >preflight/benchmark_final.stdout 2>preflight/benchmark_final.stderr &
wrapper_pid=$!
peak_rss_kib=0
while kill -0 "$wrapper_pid" 2>/dev/null; do
  rss_kib=$(ps -o rss= -p "$wrapper_pid" --ppid "$wrapper_pid" \
    2>/dev/null | awk '{s+=$1} END{print s+0}')
  if (( rss_kib > peak_rss_kib )); then peak_rss_kib=$rss_kib; fi
  sleep 0.05
done
set +e
wait "$wrapper_pid"
benchmark_status=$?
set -e
end_ns=$(date +%s%N)
{
  echo "status=$benchmark_status"
  echo "elapsed_ns=$((end_ns-start_ns))"
  echo "peak_rss_kib=$peak_rss_kib"
} >preflight/benchmark_final.monitor

sha256sum symbolic_search.cpp symbolic_search \
  preflight/compile_final.stdout preflight/compile_final.stderr \
  preflight/selftest_final.stdout preflight/selftest_final.stderr \
  preflight/benchmark_final.stdout preflight/benchmark_final.stderr \
  preflight/benchmark_final.monitor >preflight/final.sha256

cat preflight/selftest_final.stdout
cat preflight/benchmark_final.stdout
cat preflight/benchmark_final.monitor
cat preflight/final.sha256
exit "$benchmark_status"
