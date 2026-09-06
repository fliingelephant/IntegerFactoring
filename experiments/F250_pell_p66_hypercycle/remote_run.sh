#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/F250_pell_p66_hypercycle
output_dir="$work_dir/output"
python_bin=/root/miniconda3/bin/python
mkdir -p "$output_dir"

test "$($python_bin -c 'import sys; print(int(sys.version_info >= (3, 11)))')" = 1
command -v nice >/dev/null
command -v timeout >/dev/null
command -v sha256sum >/dev/null

expected_prereg_sha256=$1
expected_scan_sha256=$2
expected_runner_sha256=$3
test "$(sha256sum "$work_dir/PREREGISTRATION.md" | cut -d ' ' -f 1)" = "$expected_prereg_sha256"
test "$(sha256sum "$work_dir/scan.py" | cut -d ' ' -f 1)" = "$expected_scan_sha256"
test "$(sha256sum "$work_dir/remote_run.sh" | cut -d ' ' -f 1)" = "$expected_runner_sha256"

ulimit -v 2097152
start_epoch=$(date +%s)
timeout --signal=TERM --kill-after=30s 1800s \
  nice -n 15 "$python_bin" "$work_dir/scan.py" \
    --output-dir "$output_dir" \
    --prereg-sha256 "$expected_prereg_sha256" \
    >"$output_dir/RUN.stdout" 2>"$output_dir/RUN.stderr"
end_epoch=$(date +%s)
printf '%s\n' "$((end_epoch-start_epoch))" >"$output_dir/WALL_SECONDS.txt"

test -s "$output_dir/TRAIN.jsonl"
test -s "$output_dir/HELDOUT.jsonl"
test -s "$output_dir/SUMMARY.json"
test "$(wc -l < "$output_dir/TRAIN.jsonl")" -eq 64
test "$(wc -l < "$output_dir/HELDOUT.jsonl")" -eq 64

sha256sum \
  "$work_dir/PREREGISTRATION.md" \
  "$work_dir/scan.py" \
  "$work_dir/remote_run.sh" \
  "$output_dir/TRAIN.jsonl" \
  "$output_dir/HELDOUT.jsonl" \
  "$output_dir/SUMMARY.json" \
  "$output_dir/RUN.stdout" \
  "$output_dir/RUN.stderr" \
  "$output_dir/WALL_SECONDS.txt" \
  >"$output_dir/REMOTE_SHA256SUMS"

