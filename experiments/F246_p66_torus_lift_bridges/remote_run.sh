#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/F246_p66_torus_lift_bridges
output_dir="$work_dir/output"
mkdir -p "$output_dir"

test "$(python3 -c 'import sys; print(int(sys.version_info >= (3, 11)))')" = 1
command -v nice >/dev/null
command -v timeout >/dev/null
command -v sha256sum >/dev/null

expected_prereg_sha256=$1
actual_prereg_sha256=$(sha256sum "$work_dir/PREREGISTRATION.md" | cut -d ' ' -f 1)
test "$actual_prereg_sha256" = "$expected_prereg_sha256"

ulimit -v 4194304
/usr/bin/time -v -o "$output_dir/TIME.txt" \
  timeout --signal=TERM --kill-after=30s 10800s \
  nice -n 15 python3 "$work_dir/scan.py" \
    --output-dir "$output_dir" \
    --prereg-sha256 "$expected_prereg_sha256" \
    >"$output_dir/RUN.stdout" 2>"$output_dir/RUN.stderr"

test -s "$output_dir/TRAIN.jsonl"
test -s "$output_dir/HELDOUT.jsonl"
test -s "$output_dir/SUMMARY.json"
test "$(wc -l < "$output_dir/TRAIN.jsonl")" -eq 24
test "$(wc -l < "$output_dir/HELDOUT.jsonl")" -eq 24

sha256sum \
  "$work_dir/PREREGISTRATION.md" \
  "$work_dir/G_MINUS_LEMMA.md" \
  "$work_dir/scan.py" \
  "$work_dir/remote_run.sh" \
  "$output_dir/TRAIN.jsonl" \
  "$output_dir/HELDOUT.jsonl" \
  "$output_dir/SUMMARY.json" \
  "$output_dir/RUN.stdout" \
  "$output_dir/RUN.stderr" \
  "$output_dir/TIME.txt" \
  >"$output_dir/REMOTE_SHA256SUMS"

