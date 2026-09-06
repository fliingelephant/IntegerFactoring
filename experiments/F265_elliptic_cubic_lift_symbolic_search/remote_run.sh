#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F265/F265-D01
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
preflight_dir="$work_dir/preflight"
cd "$work_dir"

sha256sum -c FROZEN.sha256

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D01|F260-D01|F261-D01|F262-D01|F263-D0[12]|F264-D01|F265-D01.*search' | grep -v grep >/dev/null; then
    echo 'F265-D01 refuses to overlap F258-D01 through F264-D01 production.' >&2
    exit 73
  fi
}

if [[ -e "$out_dir" || -e "$log_dir" || -e "$preflight_dir" ]]; then
  echo 'F265-D01 refuses to overwrite an existing output, log, or preflight directory.' >&2
  exit 74
fi
mkdir "$out_dir" "$log_dir" "$preflight_dir"

refuse_overlap
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  nproc
  cat /proc/loadavg
  free -h
  df -h /root
  ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32
} >"$log_dir/resource_before.txt"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))

nice -n 15 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread \
  search.cpp -o search \
  >"$log_dir/compile.stdout" 2>"$log_dir/compile.stderr"
timeout 300s nice -n 15 ./search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"

assert_preflight_outputs() {
  local expected actual
  expected=$'F265-D01.preflight.json\nF265-D01.preflight.json.banks.tsv\nF265-D01.preflight.json.cells.tsv\nF265-D01.preflight.json.certificates.jsonl\nF265-D01.preflight.json.metrics.tsv'
  actual=$(find "$preflight_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265 preflight output-set gate failed.' >&2; exit 75; }
  for name in F265-D01.preflight.json F265-D01.preflight.json.banks.tsv \
    F265-D01.preflight.json.cells.tsv F265-D01.preflight.json.metrics.tsv; do
    [[ -s "$preflight_dir/$name" ]] || exit 76
  done
}

assert_discovery_outputs() {
  local expected actual
  expected=$'F265-D01.discovery.banks.tsv\nF265-D01.discovery.cells.tsv\nF265-D01.discovery.certificates.jsonl\nF265-D01.discovery.cohort.tsv\nF265-D01.discovery.metrics.tsv'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265 discovery output-set gate failed.' >&2; exit 77; }
  for name in F265-D01.discovery.banks.tsv F265-D01.discovery.cells.tsv \
    F265-D01.discovery.cohort.tsv F265-D01.discovery.metrics.tsv; do
    [[ -s "$out_dir/$name" ]] || exit 78
  done
}

assert_complete_outputs() {
  local expected actual
  expected=$'F265-D01.discovery.banks.tsv\nF265-D01.discovery.cells.tsv\nF265-D01.discovery.certificates.jsonl\nF265-D01.discovery.cohort.tsv\nF265-D01.discovery.metrics.tsv\nF265-D01.heldout.banks.tsv\nF265-D01.heldout.cells.tsv\nF265-D01.heldout.certificates.jsonl\nF265-D01.heldout.cohort.tsv\nF265-D01.heldout.metrics.tsv\nF265-D01.heldout.summary.json\nF265-D01.selection.txt'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]] || { echo 'F265 complete output-set gate failed.' >&2; exit 79; }
  for name in F265-D01.discovery.banks.tsv F265-D01.discovery.cells.tsv \
    F265-D01.discovery.cohort.tsv F265-D01.discovery.metrics.tsv \
    F265-D01.heldout.banks.tsv F265-D01.heldout.cells.tsv \
    F265-D01.heldout.cohort.tsv F265-D01.heldout.metrics.tsv \
    F265-D01.heldout.summary.json F265-D01.selection.txt; do
    [[ -s "$out_dir/$name" ]] || exit 81
  done
}

remaining=$((deadline - SECONDS))
if [[ $remaining -le 0 ]]; then exit 124; fi
refuse_overlap
set +e
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --preflight \
    --output "$preflight_dir/F265-D01.preflight.json" --workers 8
) >"$log_dir/preflight.stdout" 2>"$log_dir/preflight.stderr"
preflight_status=$?
set -e
if [[ $preflight_status -ne 0 ]]; then
  discovery_status=125
  heldout_status=125
else
  assert_preflight_outputs
  grep -q '"pass":true' "$preflight_dir/F265-D01.preflight.json"
  remaining=$((deadline - SECONDS))
  if [[ $remaining -le 0 ]]; then exit 124; fi
  refuse_overlap
  set +e
  (
    ulimit -v 4194304
    ulimit -f 1048576
    timeout "${remaining}s" nice -n 15 ./search --discovery --workers 8 \
      --cohort "$out_dir/F265-D01.discovery.cohort.tsv" \
      --metrics "$out_dir/F265-D01.discovery.metrics.tsv" \
      --cells "$out_dir/F265-D01.discovery.cells.tsv" \
      --banks "$out_dir/F265-D01.discovery.banks.tsv" \
      --certificates "$out_dir/F265-D01.discovery.certificates.jsonl"
  ) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"
  discovery_status=$?
  set -e

  if [[ $discovery_status -ne 0 ]]; then
    heldout_status=125
  else
    assert_discovery_outputs
    discovery_cohort_sha=$(sha256sum "$out_dir/F265-D01.discovery.cohort.tsv" | cut -d' ' -f1)
    ./search --select \
      --metrics "$out_dir/F265-D01.discovery.metrics.tsv" \
      --cohort-sha256 "$discovery_cohort_sha" \
      --output "$out_dir/F265-D01.selection.txt" \
      >"$log_dir/selection.stdout" 2>"$log_dir/selection.stderr"
    selection_sha=$(sha256sum "$out_dir/F265-D01.selection.txt" | cut -d' ' -f1)
    printf '%s  %s\n' "$selection_sha" 'F265-D01.selection.txt' \
      >"$log_dir/F265-D01.selection.sha256"

    actual_selection_sha=$(sha256sum "$out_dir/F265-D01.selection.txt" | cut -d' ' -f1)
    [[ "$actual_selection_sha" == "$selection_sha" ]]
    remaining=$((deadline - SECONDS))
    if [[ $remaining -le 0 ]]; then exit 124; fi
    refuse_overlap
    set +e
    (
      ulimit -v 4194304
      ulimit -f 1048576
      timeout "${remaining}s" nice -n 15 ./search --heldout --workers 8 \
        --selection "$out_dir/F265-D01.selection.txt" \
        --cohort "$out_dir/F265-D01.heldout.cohort.tsv" \
        --metrics "$out_dir/F265-D01.heldout.metrics.tsv" \
        --cells "$out_dir/F265-D01.heldout.cells.tsv" \
        --banks "$out_dir/F265-D01.heldout.banks.tsv" \
        --certificates "$out_dir/F265-D01.heldout.certificates.jsonl"
    ) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"
    heldout_status=$?
    set -e
    if [[ $heldout_status -eq 0 ]]; then
      actual_selection_sha=$(sha256sum "$out_dir/F265-D01.selection.txt" | cut -d' ' -f1)
      [[ "$actual_selection_sha" == "$selection_sha" ]]
      ./search --summarize \
        --selection "$out_dir/F265-D01.selection.txt" \
        --metrics "$out_dir/F265-D01.heldout.metrics.tsv" \
        --cells "$out_dir/F265-D01.heldout.cells.tsv" \
        --output "$out_dir/F265-D01.heldout.summary.json" \
        >"$log_dir/summarize.stdout" 2>"$log_dir/summarize.stderr"
      assert_complete_outputs
    fi
  fi
fi

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  cat /proc/loadavg
  free -h
  df -h /root
} >"$log_dir/resource_after.txt"

output_bytes=$(du -sb "$out_dir" "$preflight_dir" | awk '{s+=$1} END {print s}')
if [[ $output_bytes -gt 1073741824 ]]; then
  echo 'F265-D01 output exceeded the 1 GiB aggregate cap.' >&2
  exit 80
fi

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "preflight_status=$preflight_status"
  echo "discovery_status=$discovery_status"
  echo "heldout_status=$heldout_status"
  echo "output_bytes=$output_bytes"
  sha256sum PREREGISTRATION.md ALGEBRA.md search.cpp remote_run.sh \
    PRELAUNCH_MANIFEST.md FROZEN.sha256 search 2>/dev/null || true
  find "$out_dir" "$preflight_dir" "$log_dir" -type f \
    ! -name F265-D01.manifest -print0 | sort -z | xargs -0 sha256sum
} >"$log_dir/F265-D01.manifest"

if [[ $preflight_status -ne 0 ]]; then exit "$preflight_status"; fi
if [[ $discovery_status -ne 0 ]]; then exit "$discovery_status"; fi
exit "$heldout_status"
