#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F258/F258-D01
mkdir -p "$work_dir/output" "$work_dir/logs"
cd "$work_dir"

/root/miniconda3/bin/python scan.py --self-test

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
set +e
(
  ulimit -v 4194304
  timeout 14400s nice -n 15 /root/miniconda3/bin/python scan.py \
    --workers 8 \
    --summary output/F258-D01.summary.json \
    --rows output/F258-D01.rows.jsonl.gz
) >logs/F258-D01.stdout 2>logs/F258-D01.stderr
status=$?
set -e
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "exit_status=$status"
  sha256sum PREREGISTRATION.md scan.py remote_run.sh 2>/dev/null || true
  sha256sum output/F258-D01.summary.json output/F258-D01.rows.jsonl.gz 2>/dev/null || true
  sha256sum logs/F258-D01.stdout logs/F258-D01.stderr 2>/dev/null || true
} >logs/F258-D01.manifest

exit "$status"

