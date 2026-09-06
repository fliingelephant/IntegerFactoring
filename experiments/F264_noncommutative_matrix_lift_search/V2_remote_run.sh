#!/usr/bin/env bash
set -euo pipefail

experiment=F264-D02
work_dir=/root/IntegerFactoring_F264/F264-D02
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"

run_start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))
stage=initialization
final_status=1

owned_output_bytes() {
  find "$out_dir" "$log_dir" -type f -printf '%s\n' 2>/dev/null \
    | awk '{sum += $1} END {print sum+0}'
}

write_manifest() {
  local shell_status=$?
  local status=$final_status
  if (( status == 1 && shell_status != 0 )); then status=$shell_status; fi
  {
    echo "experiment=$experiment"
    echo "start_utc=$run_start_utc"
    echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "last_stage=$stage"
    echo "exit_status=$status"
    sha256sum V2_ALGEBRA.md V2_PREREGISTRATION.md V2_symbolic_search.cpp \
      V2_remote_run.sh V2_PRELAUNCH_MANIFEST.md V2_VALIDATION_PENDING.md \
      V2_AUDIT_REQUEST.md V2_STATIC_VALIDATION.md V2_FROZEN.sha256 \
      2>/dev/null || true
    sha256sum V2_symbolic_search 2>/dev/null || true
    find "$out_dir" "$log_dir" -type f ! -name F264-D02.manifest -print0 \
      2>/dev/null | sort -z | xargs -0 sha256sum 2>/dev/null || true
  } >"$log_dir/F264-D02.manifest"
}
trap write_manifest EXIT

sha256sum -c V2_FROZEN.sha256

incompatible_active() {
  local proc pid args cwd identity
  for proc in /proc/[0-9]*; do
    [[ -d "$proc" ]] || continue
    pid=${proc##*/}
    [[ "$pid" == "$$" || "$pid" == "$PPID" ]] && continue
    args=$(tr '\0' ' ' <"$proc/cmdline" 2>/dev/null || true)
    cwd=$(readlink "$proc/cwd" 2>/dev/null || true)
    identity="$args $cwd"
    case "$identity" in
      *F258-D01*|*F258-D02*|*F259-D01*|*F259-D02*|\
      *F260-D01*|*F260-D02*|*F261-D01*|*F261-D02*|\
      *F262-D01*|*F262-D02*|*F263-D01*|*F263-D02*|\
      *F258_pell_resultant_ticket_scan*|\
      *F259_full_pell_lift_symbolic_search*|\
      *F260_las_vegas_integer_symbolic_search*|\
      *F261_beta2_centered_carry_scaling*|\
      *F262_polynomial_frobenius_lift_symbolic_search*|\
      *F263_hypergeometric_evaluator_symbolic_search*)
        echo "INCOMPATIBLE_PROCESS pid=$pid" >&2
        return 0
        ;;
    esac
  done
  return 1
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
  (( cpus >= 8 )) || { final_status=76; exit 76; }
  (( available_kib >= 8388608 )) || { final_status=76; exit 76; }
  (( disk_kib >= 5242880 )) || { final_status=76; exit 76; }
  awk -v load="$load1" -v cpus="$cpus" \
    'BEGIN {exit !(load <= 3*cpus)}' || { final_status=76; exit 76; }
}

run_monitored() {
  local label=$1 stdout_path=$2 stderr_path=$3
  shift 3
  refuse_overlap "before_$label"
  resource_gate "before_$label"
  local remaining=$((deadline - SECONDS))
  (( remaining > 0 )) || return 124
  (
    ulimit -v 4194304
    exec timeout --foreground "${remaining}s" nice -n 15 "$@"
  ) >"$stdout_path" 2>"$stderr_path" &
  local run_pid=$! monitor_status=0
  while kill -0 "$run_pid" 2>/dev/null; do
    if incompatible_active; then
      monitor_status=73
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    local bytes
    bytes=$(owned_output_bytes)
    if (( bytes > 1073741824 )); then
      monitor_status=74
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    sleep 2
  done
  local command_status=0
  if wait "$run_pid"; then command_status=0; else command_status=$?; fi
  (( monitor_status == 0 )) || return "$monitor_status"
  (( command_status == 0 )) || return "$command_status"
  refuse_overlap "after_$label"
  local bytes
  bytes=$(owned_output_bytes)
  (( bytes <= 1073741824 )) || return 74
}

stage=compile
run_monitored compile "$log_dir/compile.stdout" "$log_dir/compile.stderr" \
  /usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread -Wall -Wextra -Wconversion \
  V2_symbolic_search.cpp -o V2_symbolic_search || { final_status=$?; exit "$final_status"; }

stage=self_test
run_monitored self_test "$log_dir/self_test.stdout" "$log_dir/self_test.stderr" \
  ./V2_symbolic_search --self-test || { final_status=$?; exit "$final_status"; }
grep -F 'SELF_TEST_PASS' "$log_dir/self_test.stdout" >/dev/null
grep -F 'assoc_rank=5/6' "$log_dir/self_test.stdout" >/dev/null
grep -F 'ternary_nulls=1,1,1,1,1' "$log_dir/self_test.stdout" >/dev/null

stage=benchmark
run_monitored benchmark "$log_dir/benchmark.stdout" "$log_dir/benchmark.stderr" \
  ./V2_symbolic_search --benchmark || { final_status=$?; exit "$final_status"; }
projection=$(sed -n \
  's/.*projected_8thread_seconds_1.75x=\([0-9.]*\).*/\1/p' \
  "$log_dir/benchmark.stdout")
predicted_bytes=$(sed -n 's/.*predicted_output_bytes=\([0-9]*\).*/\1/p' \
  "$log_dir/benchmark.stdout")
if [[ -z "$projection" ]] || \
   ! awk -v x="$projection" 'BEGIN {exit !(x <= 14400)}'; then
  final_status=75
  exit 75
fi
if [[ -z "$predicted_bytes" ]] || (( predicted_bytes > 1073741824 )); then
  final_status=74
  exit 74
fi

stage=describe
run_monitored describe "$log_dir/describe.stdout" "$log_dir/describe.stderr" \
  ./V2_symbolic_search --describe || { final_status=$?; exit "$final_status"; }
grep -F 'F264_D02_DESCRIPTION families=30' "$log_dir/describe.stdout" >/dev/null
grep -F 'tsv_columns=2541' "$log_dir/describe.stdout" >/dev/null

for split in discovery heldout; do
  stage=$split
  run_monitored "$split" "$log_dir/${split}.stdout" "$log_dir/${split}.stderr" \
    ./V2_symbolic_search 8 "$split" \
    "$out_dir/F264-D02.${split}.summary.json" \
    "$out_dir/F264-D02.${split}.rows.tsv" \
    "$out_dir/F264-D02.${split}.anomalies.tsv" \
    || { final_status=$?; exit "$final_status"; }

  stage="validate_${split}"
  run_monitored "validate_${split}" "$log_dir/validate_${split}.stdout" \
    "$log_dir/validate_${split}.stderr" python3 -c \
    'import csv,json,sys
split=sys.argv[1]; rows=sys.argv[2]; summary=sys.argv[3]
expected={"discovery":2208,"heldout":3072}[split]
with open(rows,newline="") as f:
 r=csv.reader(f,delimiter="\t"); h=next(r); assert len(h)==2541
 n=0
 for row in r: assert len(row)==2541 and row[1]==split; n+=1
 assert n==expected
d=json.load(open(summary)); assert d["experiment"]=="F264-D02"
assert d["split"]==split and d["inputs"]==expected
assert len(d["decoy_summaries"])==10
assert len(d["family_summaries"])==({"discovery":3,"heldout":4}[split])*3*30
assert len(d["p205_summaries"])==({"discovery":3,"heldout":4}[split])*3*467
assert len(d["candidate_summary"])>11000' \
    "$split" "$out_dir/F264-D02.${split}.rows.tsv" \
    "$out_dir/F264-D02.${split}.summary.json" \
    || { final_status=$?; exit "$final_status"; }
done

stage=compression
run_monitored compression "$log_dir/compression.stdout" \
  "$log_dir/compression.stderr" gzip -9 \
  "$out_dir/F264-D02.discovery.rows.tsv" \
  "$out_dir/F264-D02.discovery.anomalies.tsv" \
  "$out_dir/F264-D02.heldout.rows.tsv" \
  "$out_dir/F264-D02.heldout.anomalies.tsv" \
  || { final_status=$?; exit "$final_status"; }

stage=final_output_gate
bytes=$(owned_output_bytes)
(( bytes <= 1073741824 )) || { final_status=74; exit 74; }
for split in discovery heldout; do
  [[ -s "$out_dir/F264-D02.${split}.summary.json" ]]
  [[ -s "$out_dir/F264-D02.${split}.rows.tsv.gz" ]]
  [[ -s "$out_dir/F264-D02.${split}.anomalies.tsv.gz" ]]
done

final_status=0
stage=complete
echo "F264_D02_RUNNER_PASS projection_seconds=$projection output_bytes=$bytes"
