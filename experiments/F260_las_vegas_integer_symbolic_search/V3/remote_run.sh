#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C
export PATH=/usr/sbin:/usr/bin:/sbin:/bin
unset CDPATH GZIP PYTHONHOME PYTHONPATH AWKPATH AWKLIBPATH

work_dir=/root/IntegerFactoring_F260_V3/F260-D03
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
output_cap_bytes=1073741824
manifest_reserve_bytes=16777216
live_cap_bytes=$((output_cap_bytes - manifest_reserve_bytes))

cd "$work_dir"
sha256sum -c FROZEN.sha256

if [[ ! -s HOSTILE_PRERUN_AUDIT.md || ! -s HOSTILE_PRERUN_AUDIT.sha256 ]]; then
  echo 'REFUSE_MISSING_HOSTILE_AUDIT' >&2
  exit 78
fi
if [[ $(wc -l <HOSTILE_PRERUN_AUDIT.sha256) -ne 1 ]] ||
   ! awk '$1 ~ /^[0-9a-f][0-9a-f]*$/ && length($1) == 64 &&
          $2 == "HOSTILE_PRERUN_AUDIT.md" && NF == 2 {ok=1}
          END {exit !ok}' HOSTILE_PRERUN_AUDIT.sha256; then
  echo 'REFUSE_HOSTILE_AUDIT_SIDECAR' >&2
  exit 78
fi
sha256sum -c HOSTILE_PRERUN_AUDIT.sha256
grep -Fqx 'Verdict: **PASS — CLEARED FOR LAUNCH**' HOSTILE_PRERUN_AUDIT.md || {
  echo 'REFUSE_HOSTILE_AUDIT_VERDICT' >&2
  exit 78
}
frozen_manifest_sha=$(sha256sum FROZEN.sha256 | cut -d' ' -f1)
grep -Fqx "FROZEN_SHA256=$frozen_manifest_sha" HOSTILE_PRERUN_AUDIT.md || {
  echo 'REFUSE_STALE_HOSTILE_AUDIT' >&2
  exit 78
}

if [[ -e "$out_dir" || -e "$log_dir" || -e "$work_dir/search" ]]; then
  echo 'REFUSE_EXISTING_OUTPUT_LOG_OR_BINARY' >&2
  exit 77
fi
mkdir "$out_dir" "$log_dir"

run_start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
stage=initialization
final_status=1
projection=
projected_peak_bytes=
projected_output_bytes=

owned_bytes() {
  find "$out_dir" "$log_dir" -type f -printf '%s\n' 2>/dev/null |
    awk '{sum += $1} END {print sum+0}'
}

write_runner_manifest() {
  local shell_status=$?
  local status=$final_status
  if (( status == 1 && shell_status != 0 )); then status=$shell_status; fi
  {
    echo 'experiment=F260-D03'
    echo "start_utc=$run_start_utc"
    echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "last_stage=$stage"
    echo "exit_status=$status"
    echo "projected_seconds=$projection"
    echo "projected_peak_bytes=$projected_peak_bytes"
    echo "projected_output_bytes=$projected_output_bytes"
    echo "combined_bytes_before_manifest=$(owned_bytes 2>/dev/null || echo unknown)"
    sha256sum ALGEBRA.md PREREGISTRATION.md search.cpp remote_run.sh \
      PROVENANCE.md VALIDATION_PENDING.md STATIC_REVIEW.md AUDIT_REQUEST.md \
      PRELAUNCH_MANIFEST.md FROZEN.sha256 2>/dev/null || true
    sha256sum HOSTILE_PRERUN_AUDIT.md HOSTILE_PRERUN_AUDIT.sha256 2>/dev/null || true
    sha256sum search 2>/dev/null || true
    find "$out_dir" "$log_dir" -type f ! -name F260-D03.runner.manifest \
      -print0 2>/dev/null | sort -z | xargs -0 -r sha256sum 2>/dev/null || true
  } >"$log_dir/F260-D03.runner.manifest"
}
trap write_runner_manifest EXIT

incompatible_active() {
  local scan_status
  if python3 -c '
import os, sys
runner = int(sys.argv[1])
needles = tuple(x.encode() for x in (
    "F258-D01", "F259-D01", "F260-D01", "F260-D02", "F261-D01",
    "F262-D01", "F263-D01", "F264-D01"))
for entry in os.scandir("/proc"):
    if not entry.name.isdigit():
        continue
    pid = int(entry.name)
    if pid in (runner, os.getpid()):
        continue
    pieces = []
    try:
        with open(entry.path + "/cmdline", "rb") as stream:
            pieces.append(stream.read().replace(b"\0", b" "))
    except OSError:
        pass
    for suffix in ("cwd", "exe"):
        try:
            pieces.append(os.readlink(entry.path + "/" + suffix).encode(
                errors="surrogateescape"))
        except OSError:
            pass
    identity = b" ".join(pieces)
    if any(needle in identity for needle in needles):
        print(f"INCOMPATIBLE_PROCESS pid={pid}", file=sys.stderr)
        sys.exit(0)
sys.exit(1)
' "$$"; then
    return 0
  else
    scan_status=$?
  fi
  if (( scan_status == 1 )); then return 1; fi
  echo "FIREWALL_SCAN_FAILED status=$scan_status" >&2
  return 0
}

refuse_overlap() {
  local gate=$1
  if incompatible_active; then
    echo "REFUSE_INCOMPATIBLE stage=$gate" >&2
    final_status=73
    exit 73
  fi
}

resource_gate() {
  local gate=$1
  local cpus available_kib disk_kib load1
  cpus=$(nproc)
  available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk_kib=$(df -Pk "$work_dir" | awk 'NR==2 {print $4}')
  load1=$(awk '{print $1}' /proc/loadavg)
  {
    echo "stage=$gate"
    echo "visible_cpus=$cpus"
    echo "memory_available_kib=$available_kib"
    echo "disk_available_kib=$disk_kib"
    echo "load1=$load1"
    cat /proc/loadavg
    free -h
    df -h "$work_dir"
    ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,40p'
  } >"$log_dir/resource_${gate}.txt"
  (( cpus >= 8 )) || { echo "REFUSE_CPUS=$cpus" >&2; final_status=76; exit 76; }
  (( available_kib >= 8388608 )) || {
    echo "REFUSE_MEMORY_KIB=$available_kib" >&2
    final_status=76
    exit 76
  }
  (( disk_kib >= 2097152 )) || {
    echo "REFUSE_DISK_KIB=$disk_kib" >&2
    final_status=76
    exit 76
  }
  awk -v load="$load1" -v cpus="$cpus" \
    'BEGIN {exit !(load <= 4*cpus)}' || {
      echo "REFUSE_LOAD=$load1/$cpus" >&2
      final_status=76
      exit 76
    }
}

run_monitored() {
  local label=$1
  local timeout_seconds=$2
  local stdout_path=$3
  local stderr_path=$4
  shift 4
  refuse_overlap "before_$label"
  (
    ulimit -v 4194304
    ulimit -f 1966080
    exec timeout -k 30s "${timeout_seconds}s" nice -n 15 "$@"
  ) >"$stdout_path" 2>"$stderr_path" &
  local run_pid=$!
  local monitor_status=0
  while kill -0 "$run_pid" 2>/dev/null; do
    if incompatible_active; then
      echo "REFUSE_INCOMPATIBLE stage=during_$label" >&2
      monitor_status=73
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    local bytes
    bytes=$(owned_bytes)
    if (( bytes > live_cap_bytes )); then
      echo "REFUSE_COMBINED_BYTES=$bytes stage=during_$label" >&2
      monitor_status=74
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    sleep 1
  done
  local command_status=0
  if wait "$run_pid"; then command_status=0; else command_status=$?; fi
  if (( monitor_status != 0 )); then return "$monitor_status"; fi
  if (( command_status != 0 )); then return "$command_status"; fi
  refuse_overlap "after_$label"
  local bytes
  bytes=$(owned_bytes)
  if (( bytes > live_cap_bytes )); then
    echo "REFUSE_COMBINED_BYTES=$bytes stage=after_$label" >&2
    return 74
  fi
}

exact_output_set() {
  local expected=$1
  local actual
  actual=$(find "$out_dir" -mindepth 1 -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]]
}

check_tsv() {
  local path=$1
  local fields=$2
  local lines=${3:-0}
  awk -F '\t' -v fields="$fields" -v lines="$lines" '
    NF != fields {exit 1}
    END {if (lines != 0 && NR != lines) exit 1; if (NR == 0) exit 1}
  ' "$path"
}

verify_phase_manifest() {
  local path=$1
  local records=$2
  check_tsv "$path" 4 $((records+1))
  local seen=0
  while IFS=$'\t' read -r name bytes lines digest; do
    if (( seen == 0 )); then
      [[ "$name" == filename && "$bytes" == bytes && "$lines" == lines &&
         "$digest" == sha256 ]]
      seen=1
      continue
    fi
    [[ "$name" =~ ^F260-D03\.[A-Za-z0-9._-]+$ ]]
    [[ "$bytes" =~ ^[0-9]+$ && "$lines" =~ ^[0-9]+$ &&
       "$digest" =~ ^[0-9a-f]{64}$ ]]
    [[ -f "$out_dir/$name" ]]
    [[ $(stat -c '%s' "$out_dir/$name") == "$bytes" ]]
    [[ $(wc -l <"$out_dir/$name") == "$lines" ]]
    [[ $(sha256sum "$out_dir/$name" | cut -d' ' -f1) == "$digest" ]]
    seen=$((seen+1))
  done <"$path"
  (( seen == records+1 ))
  local listed
  listed=$(awk -F '\t' 'NR>1 {print $1}' "$path" | sort)
  if [[ "$path" == *discovery.manifest.tsv ]]; then
    local expected
    expected=$(printf '%s\n' \
      F260-D03.discovery.aggregates.tsv \
      F260-D03.discovery.certificates.tsv \
      F260-D03.discovery.collisions.tsv \
      F260-D03.discovery.corpus.sha256 \
      F260-D03.discovery.corpus.tsv \
      F260-D03.discovery.oracle.tsv \
      F260-D03.grammar.tsv \
      F260-D03.selection.sha256 \
      F260-D03.selection.tsv | sort)
    [[ "$listed" == "$expected" ]]
  else
    local expected
    expected=$(printf '%s\n' \
      F260-D03.heldout.aggregates.tsv \
      F260-D03.heldout.certificates.tsv \
      F260-D03.heldout.collisions.tsv \
      F260-D03.heldout.corpus.tsv \
      F260-D03.heldout.lead_gate.tsv | sort)
    [[ "$listed" == "$expected" ]]
  fi
}

stage=precompile
refuse_overlap "$stage"
resource_gate "$stage"
/usr/bin/g++ --version >"$log_dir/compiler.txt"
if run_monitored compile 600 "$log_dir/compile.stdout" \
    "$log_dir/compile.stderr" /usr/bin/g++ -std=c++17 -O3 -DNDEBUG \
    -pthread search.cpp -o search; then
  :
else
  final_status=$?
  exit "$final_status"
fi

stage=self_test
if run_monitored self_test 900 "$log_dir/self_test.stdout" \
    "$log_dir/self_test.stderr" ./search --self-test; then
  :
else
  final_status=$?
  exit "$final_status"
fi
grep -Fq 'SELF_TEST_OK ' "$log_dir/self_test.stdout" || {
  final_status=79
  exit 79
}

stage=benchmark
resource_gate "$stage"
if run_monitored benchmark 1800 "$log_dir/benchmark.stdout" \
    "$log_dir/benchmark.stderr" ./search --benchmark; then
  :
else
  final_status=$?
  exit "$final_status"
fi
benchmark_line=$(grep -E '^BENCHMARK_OK ' "$log_dir/benchmark.stdout")
[[ $(grep -Ec '^BENCHMARK_OK ' "$log_dir/benchmark.stdout") -eq 1 ]] || {
  final_status=75
  exit 75
}
projection=$(awk '{for(i=1;i<=NF;i++) if($i ~ /^projected_seconds=/){sub(/^[^=]*=/,"",$i); print $i}}' \
  <<<"$benchmark_line")
projected_peak_bytes=$(awk '{for(i=1;i<=NF;i++) if($i ~ /^projected_peak_bytes=/){sub(/^[^=]*=/,"",$i); print $i}}' \
  <<<"$benchmark_line")
projected_output_bytes=$(awk '{for(i=1;i<=NF;i++) if($i ~ /^projected_output_bytes=/){sub(/^[^=]*=/,"",$i); print $i}}' \
  <<<"$benchmark_line")
[[ "$projection" =~ ^[0-9]+([.][0-9]+)?([eE][+-]?[0-9]+)?$ ]] &&
  awk -v x="$projection" 'BEGIN {exit !(x <= 14400)}' || {
    echo "REFUSE_RUNTIME_PROJECTION=$projection" >&2
    final_status=75
    exit 75
  }
[[ "$projected_peak_bytes" =~ ^[0-9]+$ ]] &&
  (( projected_peak_bytes <= 4294967296 )) || {
    echo "REFUSE_MEMORY_PROJECTION=$projected_peak_bytes" >&2
    final_status=75
    exit 75
  }
[[ "$projected_output_bytes" =~ ^[0-9]+$ ]] &&
  (( projected_output_bytes <= output_cap_bytes )) || {
    echo "REFUSE_OUTPUT_PROJECTION=$projected_output_bytes" >&2
    final_status=74
    exit 74
  }
[[ -z $(find "$out_dir" -mindepth 1 -print -quit) ]] || {
  echo 'REFUSE_VALIDATION_OUTPUT' >&2
  final_status=74
  exit 74
}

stage=preproduction
refuse_overlap "$stage"
resource_gate "$stage"
deadline=$((SECONDS + 14400))

stage=discovery
remaining=$((deadline-SECONDS))
(( remaining > 0 )) || { final_status=124; exit 124; }
if run_monitored discovery "$remaining" "$log_dir/discovery.stdout" \
    "$log_dir/discovery.stderr" ./search --discovery "$out_dir" 8 full; then
  :
else
  final_status=$?
  exit "$final_status"
fi

discovery_expected=$(printf '%s\n' \
  F260-D03.discovery.aggregates.tsv \
  F260-D03.discovery.certificates.tsv \
  F260-D03.discovery.collisions.tsv \
  F260-D03.discovery.corpus.sha256 \
  F260-D03.discovery.corpus.tsv \
  F260-D03.discovery.manifest.tsv \
  F260-D03.discovery.oracle.tsv \
  F260-D03.grammar.tsv \
  F260-D03.selection.sha256 \
  F260-D03.selection.tsv | sort)
exact_output_set "$discovery_expected" || {
  echo 'REFUSE_DISCOVERY_OUTPUT_SET' >&2
  final_status=80
  exit 80
}
programs=$(awk -F '\t' 'NR>1 && $1 ~ /^[0-9]+$/ {n++} END {print n+0}' \
  "$out_dir/F260-D03.grammar.tsv")
(( programs >= 32 ))
check_tsv "$out_dir/F260-D03.grammar.tsv" 7 $((programs+2))
check_tsv "$out_dir/F260-D03.discovery.corpus.tsv" 4 8961
[[ $(wc -l <"$out_dir/F260-D03.discovery.corpus.sha256") -eq 1 ]]
check_tsv "$out_dir/F260-D03.discovery.aggregates.tsv" 45 $((programs*9+1))
check_tsv "$out_dir/F260-D03.discovery.certificates.tsv" 6
check_tsv "$out_dir/F260-D03.discovery.collisions.tsv" 11
check_tsv "$out_dir/F260-D03.discovery.oracle.tsv" 5 7
check_tsv "$out_dir/F260-D03.selection.tsv" 11 33
[[ $(wc -l <"$out_dir/F260-D03.selection.sha256") -eq 1 ]]
verify_phase_manifest "$out_dir/F260-D03.discovery.manifest.tsv" 9

read -r selection_hash selection_label selection_extra \
  <"$out_dir/F260-D03.selection.sha256"
read -r corpus_hash corpus_label corpus_extra \
  <"$out_dir/F260-D03.discovery.corpus.sha256"
[[ "$selection_hash" =~ ^[0-9a-f]{64}$ &&
   "$selection_label" == F260-D03.selection.tsv && -z "${selection_extra:-}" ]]
[[ "$corpus_hash" =~ ^[0-9a-f]{64}$ &&
   "$corpus_label" == F260-D03.discovery.corpus.tsv && -z "${corpus_extra:-}" ]]
[[ $(sha256sum "$out_dir/F260-D03.selection.tsv" | cut -d' ' -f1) ==
   "$selection_hash" ]]
[[ $(sha256sum "$out_dir/F260-D03.discovery.corpus.tsv" | cut -d' ' -f1) ==
   "$corpus_hash" ]]

stage=heldout
refuse_overlap "$stage"
remaining=$((deadline-SECONDS))
(( remaining > 0 )) || { final_status=124; exit 124; }
if run_monitored heldout "$remaining" "$log_dir/heldout.stdout" \
    "$log_dir/heldout.stderr" ./search --heldout "$out_dir" \
    "$out_dir/F260-D03.selection.tsv" "$selection_hash" \
    "$out_dir/F260-D03.discovery.corpus.tsv" "$corpus_hash" 8 full; then
  :
else
  final_status=$?
  exit "$final_status"
fi

complete_expected=$(printf '%s\n' "$discovery_expected" \
  F260-D03.heldout.aggregates.tsv \
  F260-D03.heldout.certificates.tsv \
  F260-D03.heldout.collisions.tsv \
  F260-D03.heldout.corpus.tsv \
  F260-D03.heldout.lead_gate.tsv \
  F260-D03.heldout.manifest.tsv | sort)
exact_output_set "$complete_expected" || {
  echo 'REFUSE_HELDOUT_OUTPUT_SET' >&2
  final_status=80
  exit 80
}
check_tsv "$out_dir/F260-D03.heldout.corpus.tsv" 4 24577
check_tsv "$out_dir/F260-D03.heldout.aggregates.tsv" 45 385
check_tsv "$out_dir/F260-D03.heldout.certificates.tsv" 6
check_tsv "$out_dir/F260-D03.heldout.collisions.tsv" 11
check_tsv "$out_dir/F260-D03.heldout.lead_gate.tsv" 43 33
verify_phase_manifest "$out_dir/F260-D03.heldout.manifest.tsv" 5

stage=final_output_gate
combined=$(owned_bytes)
if (( combined > live_cap_bytes )); then
  echo "REFUSE_COMBINED_BYTES=$combined stage=$stage" >&2
  final_status=74
  exit 74
fi

stage=complete
final_status=0
trap - EXIT
write_runner_manifest
combined=$(owned_bytes)
if (( combined > output_cap_bytes )); then
  echo "REFUSE_COMBINED_BYTES=$combined stage=final_manifest" >&2
  exit 74
fi
echo "F260_D03_RUNNER_PASS projected_seconds=$projection combined_bytes=$combined"
exit 0
