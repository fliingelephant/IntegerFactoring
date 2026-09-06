#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F259/F259-D01
mkdir -p "$work_dir/output" "$work_dir/logs"
cd "$work_dir"

sha256sum -c FROZEN.sha256

if pgrep -af 'F258-D01.*scan.py|scan.py.*F258-D01.summary' >/dev/null; then
  echo 'REFUSE_F258_ACTIVE' >&2
  exit 73
fi

/usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread symbolic_search.cpp -o symbolic_search
./symbolic_search --self-test

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
(
  ulimit -v 4194304
  timeout 14400s nice -n 15 ./symbolic_search 8 \
    output/F259-D01.summary.json output/F259-D01.rows.tsv
) >logs/F259-D01.stdout 2>logs/F259-D01.stderr
status=$?
set -e
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

if [[ -f output/F259-D01.rows.tsv ]]; then
  row_bytes=$(stat -c %s output/F259-D01.rows.tsv)
  if (( row_bytes > 1073741824 )); then
    echo "REFUSE_OUTPUT_BYTES=$row_bytes" >&2
    status=74
  fi
  gzip -9 output/F259-D01.rows.tsv
fi

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "exit_status=$status"
  sha256sum PREREGISTRATION.md ALGEBRA.md symbolic_search.cpp FROZEN.sha256 remote_run.sh 2>/dev/null || true
  sha256sum output/F259-D01.summary.json output/F259-D01.rows.tsv.gz 2>/dev/null || true
  sha256sum logs/F259-D01.stdout logs/F259-D01.stderr 2>/dev/null || true
} >logs/F259-D01.manifest

exit "$status"
