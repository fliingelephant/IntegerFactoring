#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F263_V2/F263-D02
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
cd "$work_dir"

sha256sum -c V2_FROZEN.sha256

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D01|F260-D01|F261-D01|F262-D01|F263-D01' | grep -v grep >/dev/null; then
    echo 'F263-D02 refuses to overlap F258-D01 through F263-D01 production.' >&2
    exit 73
  fi
}

if [[ -e "$out_dir" || -e "$log_dir" ]]; then
  echo 'F263-D02 refuses to overwrite an existing output or log directory.' >&2
  exit 74
fi
mkdir "$out_dir" "$log_dir"

refuse_overlap
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  nproc
  cat /proc/loadavg
  free -h
  df -h /root
  ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32
} >"$log_dir/resource_before.txt"

nice -n 15 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread \
  V2_symbolic_search.cpp -o V2_symbolic_search \
  >"$log_dir/compile.stdout" 2>"$log_dir/compile.stderr"
timeout 300s nice -n 15 ./V2_symbolic_search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"

assert_discovery_outputs() {
  local expected actual
  expected=$'F263-D02.discovery.rows.tsv\nF263-D02.discovery.summary.json\nF263-D02.selection.tsv'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  if [[ "$actual" != "$expected" ]]; then
    echo 'F263-D02 discovery output-set gate failed.' >&2
    exit 75
  fi
  while IFS= read -r f; do [[ -s "$out_dir/$f" ]] || exit 76; done <<<"$expected"
}

assert_complete_outputs() {
  local expected actual
  expected=$'F263-D02.discovery.rows.tsv\nF263-D02.discovery.summary.json\nF263-D02.heldout.lead_gate.tsv\nF263-D02.heldout.rows.tsv\nF263-D02.heldout.summary.json\nF263-D02.selection.tsv'
  actual=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
  if [[ "$actual" != "$expected" ]]; then
    echo 'F263-D02 complete output-set gate failed.' >&2
    exit 77
  fi
  while IFS= read -r f; do [[ -s "$out_dir/$f" ]] || exit 78; done <<<"$expected"
  [[ $(wc -l <"$out_dir/F263-D02.heldout.lead_gate.tsv") -eq 65 ]] || exit 79
}

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))
refuse_overlap
set +e
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "$((deadline - SECONDS))s" nice -n 15 \
    ./V2_symbolic_search --discovery "$out_dir" 8 full
) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"
discovery_status=$?
set -e

if [[ $discovery_status -ne 0 ]]; then
  heldout_status=125
else
  assert_discovery_outputs
  selection_sha=$(sha256sum "$out_dir/F263-D02.selection.tsv" | cut -d' ' -f1)
  printf '%s  %s\n' "$selection_sha" 'F263-D02.selection.tsv' \
    >"$log_dir/F263-D02.selection.sha256"
  refuse_overlap
  remaining=$((deadline - SECONDS))
  set +e
  if [[ $remaining -le 0 ]]; then
    heldout_status=124
  else
    (
      ulimit -v 4194304
      ulimit -f 1048576
      timeout "${remaining}s" nice -n 15 \
        ./V2_symbolic_search --heldout "$out_dir" \
        "$out_dir/F263-D02.selection.tsv" "$selection_sha" 8 full
    ) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"
    heldout_status=$?
  fi
  set -e
  if [[ $heldout_status -eq 0 ]]; then assert_complete_outputs; fi
fi

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
output_bytes=$(du -sb "$out_dir" | cut -f1)
if [[ $output_bytes -gt 1073741824 ]]; then
  echo 'F263-D02 output exceeded the 1 GiB aggregate cap.' >&2
  exit 80
fi

{
  echo "start_utc=$start_utc"
  echo "end_utc=$end_utc"
  echo "discovery_status=$discovery_status"
  echo "heldout_status=$heldout_status"
  echo "output_bytes=$output_bytes"
  sha256sum V2_PREREGISTRATION.md V2_ALGEBRA.md V2_symbolic_search.cpp \
    V2_remote_run.sh V2_PRELAUNCH_MANIFEST.md V2_PROVENANCE.md \
    V2_FROZEN.sha256 V2_symbolic_search 2>/dev/null || true
  find "$out_dir" "$log_dir" -type f \
    ! -name F263-D02.manifest -print0 | sort -z | xargs -0 sha256sum
} >"$log_dir/F263-D02.manifest"

if [[ $discovery_status -ne 0 ]]; then exit "$discovery_status"; fi
exit "$heldout_status"
