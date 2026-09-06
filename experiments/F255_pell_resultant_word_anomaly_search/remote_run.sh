#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F255/F255-D01
mkdir -p "$work_dir/output" "$work_dir/logs"
cd "$work_dir"

/usr/bin/g++ -O3 -std=c++17 -pthread search.cpp -o search
./search --self-test

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
timeout 14400s nice -n 15 ./search 8 output/F255-D01.json output/F255-D01.tsv \
  >logs/F255-D01.stdout 2>logs/F255-D01.stderr
status=$?
set -e
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "exit_status=$status"
  sha256sum search.cpp remote_run.sh search 2>/dev/null || true
  sha256sum output/F255-D01.json output/F255-D01.tsv 2>/dev/null || true
  sha256sum logs/F255-D01.stdout logs/F255-D01.stderr 2>/dev/null || true
} >logs/F255-D01.manifest

exit "$status"
