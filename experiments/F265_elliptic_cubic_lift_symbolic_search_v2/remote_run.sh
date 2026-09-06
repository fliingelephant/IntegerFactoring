#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F265/F265-D02
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
preflight_dir="$work_dir/preflight"
cd "$work_dir"

if [[ -e "$out_dir" || -e "$log_dir" || -e "$preflight_dir" || -e search ]]; then
  echo 'F265-D02 refuses to overwrite an existing binary, output, log, or preflight directory.' >&2
  exit 74
fi
mkdir "$out_dir" "$log_dir" "$preflight_dir"

ulimit -v 4194304
ulimit -f 1048576

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
hard_deadline=$((SECONDS + 14400))
deadline=$((hard_deadline - 300))
compile_status=125
selftest_status=125
preflight_status=125
discovery_status=125
selection_status=125
heldout_status=125
summary_status=125

remaining_seconds() {
  local remaining=$((deadline - SECONDS))
  if [[ $remaining -le 0 ]]; then
    echo 'F265-D02 exhausted the complete-packet deadline.' >&2
    exit 124
  fi
  printf '%s\n' "$remaining"
}

run_phase() {
  local requested=$1
  shift
  local remaining
  remaining=$(remaining_seconds)
  if [[ $requested -gt 0 && $requested -lt $remaining ]]; then
    remaining=$requested
  fi
  timeout "${remaining}s" nice -n 15 "$@"
}

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D0[12]|F260-D01|F261-D0[12]|F262-D01|F263-D0[12]|F264-D01|F265-D0[12].*search' | grep -v grep >/dev/null; then
    echo 'F265-D02 refuses to overlap F258-D01 through F265-D01 production.' >&2
    exit 73
  fi
}

assert_host_capacity() {
  local cpus load_one mem_available_kib disk_available_kib
  cpus=$(nproc)
  load_one=$(awk '{print $1}' /proc/loadavg)
  mem_available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  disk_available_kib=$(df -Pk /root | awk 'NR==2 {print $4}')
  awk -v load="$load_one" -v cpus="$cpus" 'BEGIN {exit !(load <= 2*cpus)}' || {
    echo 'F265-D02 host load gate failed.' >&2
    exit 82
  }
  [[ $mem_available_kib -ge 8388608 ]] || {
    echo 'F265-D02 requires at least 8 GiB available memory.' >&2
    exit 83
  }
  [[ $disk_available_kib -ge 4194304 ]] || {
    echo 'F265-D02 requires at least 4 GiB available disk.' >&2
    exit 84
  }
}

record_resources() {
  local path=$1
  {
    date -u +%Y-%m-%dT%H:%M:%SZ
    nproc
    cat /proc/loadavg
    free -h
    df -h /root
    ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32
  } >"$path"
}

check_output_cap() {
  local output_bytes binary_bytes=0
  output_bytes=$(du -sb "$out_dir" "$preflight_dir" "$log_dir" | awk '{s+=$1} END {print s}')
  if [[ -e search ]]; then binary_bytes=$(stat -c %s search); fi
  output_bytes=$((output_bytes + binary_bytes))
  if [[ $output_bytes -gt 1073741824 ]]; then
    echo 'F265-D02 aggregate binary, output, preflight, and log bytes exceed 1 GiB.' >&2
    exit 80
  fi
}

phase_gate() {
  refuse_overlap
  assert_host_capacity
  remaining_seconds >/dev/null
}

finalize() {
  local status=$?
  trap - EXIT
  set +e
  record_resources "$log_dir/resource_after.txt"
  local output_bytes
  output_bytes=$(du -sb "$out_dir" "$preflight_dir" "$log_dir" 2>/dev/null | awk '{s+=$1} END {print s+0}')
  if [[ -e search ]]; then output_bytes=$((output_bytes + $(stat -c %s search))); fi
  {
    echo "start_utc=$start_utc"
    echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "compile_status=$compile_status"
    echo "selftest_status=$selftest_status"
    echo "preflight_status=$preflight_status"
    echo "discovery_status=$discovery_status"
    echo "selection_status=$selection_status"
    echo "heldout_status=$heldout_status"
    echo "summary_status=$summary_status"
    echo "output_bytes=$output_bytes"
    sha256sum PREREGISTRATION.md ALGEBRA.md search.cpp remote_run.sh \
      PRELAUNCH_MANIFEST.md VALIDATION_PENDING.md AUDIT_REQUEST.md \
      FROZEN.sha256 search 2>/dev/null
    find "$out_dir" "$preflight_dir" "$log_dir" -type f \
      ! -name F265-D02.manifest -print0 | sort -z | xargs -0 sha256sum
  } >"$log_dir/F265-D02.manifest"
  exit "$status"
}
trap finalize EXIT

phase_gate
record_resources "$log_dir/resource_before.txt"
run_phase 300 sha256sum -c FROZEN.sha256 \
  >"$log_dir/authenticate.stdout" 2>"$log_dir/authenticate.stderr"
check_output_cap

phase_gate
set +e
run_phase 0 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread search.cpp -o search \
  >"$log_dir/compile.stdout" 2>"$log_dir/compile.stderr"
compile_status=$?
set -e
[[ $compile_status -eq 0 ]] || exit "$compile_status"
check_output_cap

phase_gate
set +e
run_phase 300 ./search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"
selftest_status=$?
set -e
[[ $selftest_status -eq 0 ]] || exit "$selftest_status"
check_output_cap

assert_preflight_outputs() {
  local expected actual
  expected=$'F265-D02.preflight.json\nF265-D02.preflight.json.banks.tsv\nF265-D02.preflight.json.blocks.tsv\nF265-D02.preflight.json.cells.tsv\nF265-D02.preflight.json.certificates.jsonl\nF265-D02.preflight.json.labels.tsv\nF265-D02.preflight.json.metrics.tsv\nF265-D02.preflight.json.patterns.tsv'
  actual=$(find "$preflight_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265-D02 preflight output-set gate failed.' >&2; exit 75; }
  for name in F265-D02.preflight.json F265-D02.preflight.json.banks.tsv \
    F265-D02.preflight.json.cells.tsv F265-D02.preflight.json.labels.tsv \
    F265-D02.preflight.json.metrics.tsv; do
    [[ -s "$preflight_dir/$name" ]] || exit 76
  done
}

assert_discovery_outputs() {
  local expected actual
  expected=$'F265-D02.discovery.banks.tsv\nF265-D02.discovery.blocks.tsv\nF265-D02.discovery.cells.tsv\nF265-D02.discovery.certificates.jsonl\nF265-D02.discovery.cohort.tsv\nF265-D02.discovery.labels.tsv\nF265-D02.discovery.metrics.tsv\nF265-D02.discovery.patterns.tsv'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265-D02 discovery output-set gate failed.' >&2; exit 77; }
  for name in F265-D02.discovery.banks.tsv F265-D02.discovery.cells.tsv \
    F265-D02.discovery.cohort.tsv F265-D02.discovery.labels.tsv \
    F265-D02.discovery.metrics.tsv; do
    [[ -s "$out_dir/$name" ]] || exit 78
  done
}

assert_complete_outputs() {
  local expected actual
  expected=$'F265-D02.discovery.banks.tsv\nF265-D02.discovery.blocks.tsv\nF265-D02.discovery.cells.tsv\nF265-D02.discovery.certificates.jsonl\nF265-D02.discovery.cohort.tsv\nF265-D02.discovery.labels.tsv\nF265-D02.discovery.metrics.tsv\nF265-D02.discovery.patterns.tsv\nF265-D02.heldout.banks.tsv\nF265-D02.heldout.blocks.tsv\nF265-D02.heldout.cells.tsv\nF265-D02.heldout.certificates.jsonl\nF265-D02.heldout.cohort.tsv\nF265-D02.heldout.labels.tsv\nF265-D02.heldout.metrics.tsv\nF265-D02.heldout.patterns.tsv\nF265-D02.heldout.summary.json\nF265-D02.selection.txt'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265-D02 complete output-set gate failed.' >&2; exit 79; }
  for name in F265-D02.discovery.banks.tsv F265-D02.discovery.cells.tsv \
    F265-D02.discovery.cohort.tsv F265-D02.discovery.labels.tsv \
    F265-D02.discovery.metrics.tsv F265-D02.heldout.banks.tsv \
    F265-D02.heldout.cells.tsv F265-D02.heldout.cohort.tsv \
    F265-D02.heldout.labels.tsv F265-D02.heldout.metrics.tsv \
    F265-D02.heldout.summary.json F265-D02.selection.txt; do
    [[ -s "$out_dir/$name" ]] || exit 81
  done
}

phase_gate
set +e
run_phase 0 ./search --preflight \
  --output "$preflight_dir/F265-D02.preflight.json" --workers 8 \
  >"$log_dir/preflight.stdout" 2>"$log_dir/preflight.stderr"
preflight_status=$?
set -e
[[ $preflight_status -eq 0 ]] || exit "$preflight_status"
assert_preflight_outputs
grep -q '"pass":true' "$preflight_dir/F265-D02.preflight.json"
check_output_cap

phase_gate
set +e
run_phase 0 ./search --discovery --workers 8 \
  --cohort "$out_dir/F265-D02.discovery.cohort.tsv" \
  --metrics "$out_dir/F265-D02.discovery.metrics.tsv" \
  --cells "$out_dir/F265-D02.discovery.cells.tsv" \
  --banks "$out_dir/F265-D02.discovery.banks.tsv" \
  --blocks "$out_dir/F265-D02.discovery.blocks.tsv" \
  --patterns "$out_dir/F265-D02.discovery.patterns.tsv" \
  --labels "$out_dir/F265-D02.discovery.labels.tsv" \
  --certificates "$out_dir/F265-D02.discovery.certificates.jsonl" \
  >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"
discovery_status=$?
set -e
[[ $discovery_status -eq 0 ]] || exit "$discovery_status"
assert_discovery_outputs
check_output_cap

phase_gate
discovery_cohort_sha=$(run_phase 60 sha256sum "$out_dir/F265-D02.discovery.cohort.tsv" | cut -d' ' -f1)
set +e
run_phase 300 ./search --select \
  --metrics "$out_dir/F265-D02.discovery.metrics.tsv" \
  --cohort-sha256 "$discovery_cohort_sha" \
  --output "$out_dir/F265-D02.selection.txt" \
  >"$log_dir/selection.stdout" 2>"$log_dir/selection.stderr"
selection_status=$?
set -e
[[ $selection_status -eq 0 ]] || exit "$selection_status"
selection_sha=$(run_phase 60 sha256sum "$out_dir/F265-D02.selection.txt" | cut -d' ' -f1)
printf '%s  %s\n' "$selection_sha" 'F265-D02.selection.txt' \
  >"$log_dir/F265-D02.selection.sha256"
actual_selection_sha=$(run_phase 60 sha256sum "$out_dir/F265-D02.selection.txt" | cut -d' ' -f1)
[[ "$actual_selection_sha" == "$selection_sha" ]]
check_output_cap

phase_gate
set +e
run_phase 0 ./search --heldout --workers 8 \
  --selection "$out_dir/F265-D02.selection.txt" \
  --cohort "$out_dir/F265-D02.heldout.cohort.tsv" \
  --metrics "$out_dir/F265-D02.heldout.metrics.tsv" \
  --cells "$out_dir/F265-D02.heldout.cells.tsv" \
  --banks "$out_dir/F265-D02.heldout.banks.tsv" \
  --blocks "$out_dir/F265-D02.heldout.blocks.tsv" \
  --patterns "$out_dir/F265-D02.heldout.patterns.tsv" \
  --labels "$out_dir/F265-D02.heldout.labels.tsv" \
  --certificates "$out_dir/F265-D02.heldout.certificates.jsonl" \
  >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"
heldout_status=$?
set -e
[[ $heldout_status -eq 0 ]] || exit "$heldout_status"
actual_selection_sha=$(run_phase 60 sha256sum "$out_dir/F265-D02.selection.txt" | cut -d' ' -f1)
[[ "$actual_selection_sha" == "$selection_sha" ]]
check_output_cap

phase_gate
set +e
run_phase 300 ./search --summarize \
  --selection "$out_dir/F265-D02.selection.txt" \
  --metrics "$out_dir/F265-D02.heldout.metrics.tsv" \
  --cells "$out_dir/F265-D02.heldout.cells.tsv" \
  --output "$out_dir/F265-D02.heldout.summary.json" \
  >"$log_dir/summarize.stdout" 2>"$log_dir/summarize.stderr"
summary_status=$?
set -e
[[ $summary_status -eq 0 ]] || exit "$summary_status"
assert_complete_outputs
check_output_cap

exit 0
