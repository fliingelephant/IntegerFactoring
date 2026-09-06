#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C
export PATH=/usr/sbin:/usr/bin:/sbin:/bin
unset CDPATH GZIP PYTHONHOME PYTHONPATH AWKPATH AWKLIBPATH

work_dir=/root/IntegerFactoring_F259/F259-D02
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
output_cap_bytes=1073741824
manifest_reserve_bytes=1048576
live_output_cap_bytes=$((output_cap_bytes - manifest_reserve_bytes))
mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"
existing_output=$(find "$out_dir" "$log_dir" -mindepth 1 -print -quit)
if [[ -n "$existing_output" ]]; then
  echo "REFUSE_NONEMPTY_OUTPUT path=$existing_output" >&2
  exit 77
fi
if [[ ! -s HOSTILE_PRERUN_AUDIT.md ]]; then
  echo "REFUSE_MISSING_HOSTILE_AUDIT" >&2
  exit 78
fi
audit_verdict=$(awk '
  NF == 0 || $0 ~ /^#/ {next}
  {gsub(/\*/, ""); print; exit}
' HOSTILE_PRERUN_AUDIT.md)
case "$audit_verdict" in
  "Verdict: PASS"*|PASS*) ;;
  *)
    echo "REFUSE_HOSTILE_AUDIT verdict=$audit_verdict" >&2
    exit 78
    ;;
esac

run_start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
stage=initialization
final_status=1

write_manifest() {
  local shell_status=$?
  local status=$final_status
  if (( status == 1 && shell_status != 0 )); then status=$shell_status; fi
  {
    echo "experiment=F259-D02"
    echo "start_utc=$run_start_utc"
    echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "last_stage=$stage"
    echo "exit_status=$status"
    echo "benchmark_projection_seconds=${projection:-}"
    echo "predicted_output_bytes=${predicted_bytes:-}"
    echo "owned_output_bytes=$(owned_output_bytes 2>/dev/null || echo unknown)"
    sha256sum PREREGISTRATION.md ALGEBRA.md symbolic_search.cpp remote_run.sh \
      PRELAUNCH_MANIFEST.md VALIDATION_PENDING.md STATIC_VALIDATION.md \
      AUDIT_REQUEST.md \
      FROZEN.sha256 2>/dev/null || true
    sha256sum HOSTILE_PRERUN_AUDIT.md 2>/dev/null || true
    sha256sum symbolic_search 2>/dev/null || true
    find "$out_dir" "$log_dir" -type f ! -name F259-D02.manifest -print0 \
      2>/dev/null | sort -z | xargs -0 -r sha256sum 2>/dev/null || true
  } >"$log_dir/F259-D02.manifest"
}
trap write_manifest EXIT

sha256sum -c FROZEN.sha256

incompatible_active() {
  local scan_status
  if python3 -c '
import os, sys
runner_pid = int(sys.argv[1])
needles = (b"F258", b"F260", b"F261", b"F263", b"F264")
for entry in os.scandir("/proc"):
    if not entry.name.isdigit():
        continue
    pid = int(entry.name)
    if pid in (runner_pid, os.getpid()):
        continue
    parts = []
    try:
        with open(entry.path + "/cmdline", "rb") as stream:
            parts.append(stream.read().replace(b"\0", b" "))
    except OSError:
        pass
    for suffix in ("cwd", "exe"):
        try:
            parts.append(os.readlink(entry.path + "/" + suffix).encode(
                errors="surrogateescape"))
        except OSError:
            pass
    identity = b" ".join(parts)
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
    echo "allowed_cpus=$cpus"
    echo "mem_available_kib=$available_kib"
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
  (( disk_kib >= 4194304 )) || {
    echo "REFUSE_DISK_KIB=$disk_kib" >&2
    final_status=76
    exit 76
  }
  awk -v load="$load1" -v cpus="$cpus" \
    'BEGIN {exit !(load <= 3*cpus)}' || {
      echo "REFUSE_LOAD=$load1/$cpus" >&2
      final_status=76
      exit 76
    }
}

owned_output_bytes() {
  find "$out_dir" "$log_dir" -type f -printf '%s\n' \
    2>/dev/null | awk '{sum += $1} END {print sum+0}'
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
    bytes=$(owned_output_bytes)
    if (( bytes > live_output_cap_bytes )); then
      echo "REFUSE_OUTPUT_BYTES=$bytes stage=during_$label" >&2
      monitor_status=74
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    sleep 2
  done
  local command_status=0
  if wait "$run_pid"; then command_status=0; else command_status=$?; fi
  if (( monitor_status != 0 )); then return "$monitor_status"; fi
  if (( command_status != 0 )); then return "$command_status"; fi
  refuse_overlap "after_$label"
  local bytes
  bytes=$(owned_output_bytes)
  if (( bytes > live_output_cap_bytes )); then
    echo "REFUSE_OUTPUT_BYTES=$bytes stage=after_$label" >&2
    return 74
  fi
  return 0
}

stage=precompile
refuse_overlap "$stage"
resource_gate "$stage"
/usr/bin/g++ --version >"$log_dir/compiler.txt"
if run_monitored compile 600 "$log_dir/compile.stdout" \
    "$log_dir/compile.stderr" /usr/bin/g++ -std=c++17 -O3 -DNDEBUG \
    -pthread symbolic_search.cpp -o symbolic_search; then
  :
else
  final_status=$?
  exit "$final_status"
fi

stage=self_test
if run_monitored self_test 600 "$log_dir/self_test.stdout" \
    "$log_dir/self_test.stderr" ./symbolic_search --self-test; then
  grep -F 'SELF_TEST_PASS' "$log_dir/self_test.stdout" >/dev/null
  grep -F 'columns=12,rank=10,nullity=2,ternary_nulls=4,primitive_controls=2' \
    "$log_dir/self_test.stdout" >/dev/null
else
  final_status=$?
  exit "$final_status"
fi

stage=benchmark
resource_gate "$stage"
if run_monitored benchmark 900 "$log_dir/benchmark.stdout" \
    "$log_dir/benchmark.stderr" ./symbolic_search --benchmark; then
  :
else
  final_status=$?
  exit "$final_status"
fi
projection=$(sed -n \
  's/.*projected_8thread_seconds_1.75x=\([0-9.]*\).*/\1/p' \
  "$log_dir/benchmark.stdout")
predicted_bytes=$(sed -n 's/.*predicted_output_bytes=\([0-9]*\).*/\1/p' \
  "$log_dir/benchmark.stdout")
if [[ -z "$projection" ]] || \
   ! awk -v value="$projection" 'BEGIN {exit !(value <= 14400)}'; then
  echo "REFUSE_RUNTIME_PROJECTION=$projection" >&2
  final_status=75
  exit 75
fi
if [[ -z "$predicted_bytes" ]] || (( predicted_bytes > live_output_cap_bytes )); then
  echo "REFUSE_PREDICTED_OUTPUT=$predicted_bytes" >&2
  final_status=74
  exit 74
fi

stage=describe
if run_monitored describe 120 "$log_dir/describe.stdout" \
    "$log_dir/describe.stderr" ./symbolic_search --describe; then
  :
else
  final_status=$?
  exit "$final_status"
fi
grep -F 'F259_D02_DESCRIPTION families=22 words=255 planned_inputs=7040 tsv_columns=634' \
  "$log_dir/describe.stdout" >/dev/null

stage=preproduction
refuse_overlap "$stage"
resource_gate "$stage"
deadline=$((SECONDS + 14400))
remaining=$((deadline - SECONDS))
if (( remaining <= 0 )); then
  final_status=124
  exit 124
fi

stage=production
if run_monitored production "$remaining" "$log_dir/cohorts.stdout" \
    "$log_dir/cohorts.stderr" ./symbolic_search 8 \
    "$out_dir/F259-D02.summary.json" "$out_dir/F259-D02.rows.tsv"; then
  :
else
  final_status=$?
  exit "$final_status"
fi

stage=report_validation
bytes=$(owned_output_bytes)
if (( bytes > live_output_cap_bytes )); then
  echo "REFUSE_OUTPUT_BYTES=$bytes stage=report_validation" >&2
  final_status=74
  exit 74
fi
remaining=$((deadline - SECONDS))
if (( remaining <= 0 )); then
  final_status=124
  exit 124
fi
if run_monitored report_tsv "$remaining" "$log_dir/report_tsv.stdout" \
    "$log_dir/report_tsv.stderr" awk -F '\t' '
  NR == 1 { if (NF != 634) exit 1; next }
  NF != 634 { exit 1 }
  {
    if (($1 <= 32 && $2 != "discovery") || ($1 > 32 && $2 != "heldout")) exit 1
    direct=0
    for (column=19; column<=124; column+=5) direct += $column
    if ($11 == 0) {
      if ($12 != 1 || index($14, "cleanup:") == 1) exit 1
    } else {
      if ($11 < 0 || $12 != 0 || index($14, "cleanup:") != 1) exit 1
    }
    expected_strict=($12 == 1 && direct == 0 ? 1 : 0)
    if ($13 != expected_strict) exit 1
    if ($12 == 1 && direct > 0 && $14 == "") exit 1
    if ($13 == 1 && $14 != "") exit 1
    key=$1 SUBSEP $3
    count[key]++
  }
  END {
    if (NR != 7041) exit 1
    split("16 24 32 40 48 56 60", bits, " ")
    for (i=1; i<=7; ++i) {
      if (count[bits[i] SUBSEP "random"] != 512) exit 1
      if (count[bits[i] SUBSEP "consecutive"] != 256) exit 1
      expected=(bits[i] == 16 ? 128 : 256)
      if (count[bits[i] SUBSEP "safe-safe"] != expected) exit 1
    }
  }
' "$out_dir/F259-D02.rows.tsv"; then
  :
else
  final_status=$?
  exit "$final_status"
fi

remaining=$((deadline - SECONDS))
if (( remaining <= 0 )); then
  final_status=124
  exit 124
fi
if run_monitored report_json "$remaining" "$log_dir/report_json.stdout" \
    "$log_dir/report_json.stderr" python3 -c \
    'import json,sys; d=json.load(open(sys.argv[1])); ok=d.get("experiment")=="F259-D02" and d.get("input_count")==7040 and "columns=12,rank=10,nullity=2,ternary_nulls=4,primitive_controls=2" in d.get("identity_mining","") and len(d.get("discovery_ranking",[]))==255 and len(d.get("family_summaries",[]))==7*3*22 and len(d.get("summaries",[]))==7*3*255 and "F259_D02_PASS inputs=7040" in open(sys.argv[2]).read(); sys.exit(0 if ok else 1)' \
    "$out_dir/F259-D02.summary.json" "$log_dir/cohorts.stdout"; then
  :
else
  final_status=$?
  exit "$final_status"
fi

remaining=$((deadline - SECONDS))
if (( remaining <= 0 )); then
  final_status=124
  exit 124
fi
stage=compression
if run_monitored compression "$remaining" "$log_dir/compression.stdout" \
    "$log_dir/compression.stderr" gzip -9 "$out_dir/F259-D02.rows.tsv"; then
  :
else
  final_status=$?
  exit "$final_status"
fi

remaining=$((deadline - SECONDS))
if (( remaining <= 0 )); then
  final_status=124
  exit 124
fi
stage=compression_validation
if run_monitored compression_test "$remaining" \
    "$log_dir/compression_test.stdout" "$log_dir/compression_test.stderr" \
    gzip -t "$out_dir/F259-D02.rows.tsv.gz"; then
  :
else
  final_status=$?
  exit "$final_status"
fi

stage=final_output_gate
bytes=$(owned_output_bytes)
if (( bytes > live_output_cap_bytes )); then
  echo "REFUSE_OUTPUT_BYTES=$bytes stage=final_output_gate" >&2
  final_status=74
  exit 74
fi
[[ -s "$out_dir/F259-D02.summary.json" && \
   -s "$out_dir/F259-D02.rows.tsv.gz" ]]

final_status=0
stage=complete
echo "F259_D02_RUNNER_PASS projection_seconds=$projection output_bytes=$bytes"
exit 0
