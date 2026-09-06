#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
export LC_ALL=C
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
unset CDPATH GZIP PYTHONHOME PYTHONPATH AWKPATH AWKLIBPATH

if [[ $# -ne 1 ]]; then
  echo 'usage: remote_run.sh ABSOLUTE_NEW_TARGET' >&2
  exit 64
fi

VERSION=F281-D01
TARGET=$1
SOURCE_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
if [[ -z ${F281_PACKET_GUARD_PARENT:-} ]]; then
  command -v timeout >/dev/null || { echo 'DEPLOYMENT_STOP missing_command=timeout' >&2; exit 69; }
  export F281_PACKET_GUARD_PARENT=$BASHPID
  exec timeout -k 5s 14395s bash "$SOURCE_DIR/remote_run.sh" "$TARGET"
fi
[[ "$F281_PACKET_GUARD_PARENT" == "$PPID" ]] || {
  echo 'DEPLOYMENT_STOP invalid_packet_deadline_guard' >&2
  exit 69
}
unset F281_PACKET_GUARD_PARENT
PACKET_START_SECONDS=$SECONDS
PACKET_DEADLINE=$((PACKET_START_SECONDS + 14400))
MANIFEST_RESERVE_SECONDS=300
WITNESS_REPLAY_RESERVE_SECONDS=1800
ADDRESS_KIB=4194304
FILE_BLOCKS=524288
NOFILE_LIMIT=128
NPROC_LIMIT=64
OUTPUT_CAP_BYTES=536870912
PROJECTED_OUTPUT_CAP_BYTES=402653184
PROJECTED_MEMORY_CAP_BYTES=3758096384
MIN_AVAILABLE_KIB=6291456
MIN_DISK_KIB=2097152
MAX_WORKERS=8
readonly VERSION TARGET SOURCE_DIR PACKET_START_SECONDS PACKET_DEADLINE
readonly MANIFEST_RESERVE_SECONDS WITNESS_REPLAY_RESERVE_SECONDS ADDRESS_KIB
readonly FILE_BLOCKS NOFILE_LIMIT NPROC_LIMIT OUTPUT_CAP_BYTES
readonly PROJECTED_OUTPUT_CAP_BYTES PROJECTED_MEMORY_CAP_BYTES MIN_AVAILABLE_KIB
readonly MIN_DISK_KIB MAX_WORKERS

case "$TARGET" in
  /*) ;;
  *) echo 'target must be absolute' >&2; exit 64 ;;
esac
case "$TARGET" in
  /|/root|/tmp|"$SOURCE_DIR") echo 'refuse broad or source target' >&2; exit 64 ;;
esac
[[ ! -e "$TARGET" ]] || { echo "refuse existing target: $TARGET" >&2; exit 73; }

for command in awk bash cut date df dirname du find g++ grep head kill mkdir mv \
  nproc pkg-config ps sed sha256sum sleep sort stat tail timeout wc xargs; do
  command -v "$command" >/dev/null || {
    echo "DEPLOYMENT_STOP missing_command=$command" >&2
    exit 69
  }
done

cd -- "$SOURCE_DIR"
[[ -f FROZEN.sha256 ]] || { echo 'REFUSE_MISSING_FROZEN_MANIFEST' >&2; exit 78; }
sha256sum -c FROZEN.sha256
FROZEN_MANIFEST_SHA=$(sha256sum FROZEN.sha256 | awk '{print $1}')
readonly FROZEN_MANIFEST_SHA

[[ -s HOSTILE_PRERUN_AUDIT.md && -s HOSTILE_PRERUN_AUDIT.sha256 ]] || {
  echo 'REFUSE_MISSING_HOSTILE_AUDIT' >&2
  exit 78
}
[[ $(wc -l <HOSTILE_PRERUN_AUDIT.sha256) -eq 1 ]] || {
  echo 'REFUSE_HOSTILE_AUDIT_SIDECAR_LINES' >&2
  exit 78
}
awk '$1 ~ /^[0-9a-f]+$/ && length($1)==64 &&
     $2=="HOSTILE_PRERUN_AUDIT.md" && NF==2 {ok=1}
     END {exit !ok}' HOSTILE_PRERUN_AUDIT.sha256 || {
  echo 'REFUSE_HOSTILE_AUDIT_SIDECAR_FORMAT' >&2
  exit 78
}
sha256sum -c HOSTILE_PRERUN_AUDIT.sha256
grep -Fqx 'Verdict: **PASS — CLEARED FOR LAUNCH**' HOSTILE_PRERUN_AUDIT.md || {
  echo 'REFUSE_HOSTILE_AUDIT_VERDICT' >&2
  exit 78
}
grep -Fqx "FROZEN_SHA256=$FROZEN_MANIFEST_SHA" HOSTILE_PRERUN_AUDIT.md || {
  echo 'REFUSE_STALE_HOSTILE_AUDIT' >&2
  exit 78
}

pkg-config --exists flint || {
  echo 'DEPLOYMENT_STOP missing_pkgconfig=flint' >&2
  exit 69
}
pkg-config --exists gmp || {
  echo 'DEPLOYMENT_STOP missing_pkgconfig=gmp' >&2
  exit 69
}
FLINT_CFLAGS_TEXT=$(pkg-config --cflags flint)
FLINT_LIBS_TEXT=$(pkg-config --libs flint)
FLINT_CFLAGS=()
FLINT_LIBS=()
if [[ -n "$FLINT_CFLAGS_TEXT" ]]; then IFS=' ' read -r -a FLINT_CFLAGS <<<"$FLINT_CFLAGS_TEXT"; fi
if [[ -n "$FLINT_LIBS_TEXT" ]]; then IFS=' ' read -r -a FLINT_LIBS <<<"$FLINT_LIBS_TEXT"; fi
readonly FLINT_CFLAGS_TEXT FLINT_LIBS_TEXT
readonly -a FLINT_CFLAGS FLINT_LIBS

rlimit_compatible() {
  (
    ulimit -S -v "$ADDRESS_KIB"
    ulimit -H -v "$ADDRESS_KIB"
    ulimit -S -c 0
    ulimit -H -c 0
    ulimit -S -f "$FILE_BLOCKS"
    ulimit -H -f "$FILE_BLOCKS"
    ulimit -S -n "$NOFILE_LIMIT"
    ulimit -H -n "$NOFILE_LIMIT"
    ulimit -S -u "$NPROC_LIMIT"
    ulimit -H -u "$NPROC_LIMIT"
    [[ $(ulimit -S -v) == "$ADDRESS_KIB" ]]
    [[ $(ulimit -H -v) == "$ADDRESS_KIB" ]]
    [[ $(ulimit -S -c) == 0 && $(ulimit -H -c) == 0 ]]
    [[ $(ulimit -S -f) == "$FILE_BLOCKS" ]]
    [[ $(ulimit -H -f) == "$FILE_BLOCKS" ]]
    [[ $(ulimit -S -n) == "$NOFILE_LIMIT" ]]
    [[ $(ulimit -H -n) == "$NOFILE_LIMIT" ]]
    [[ $(ulimit -S -u) == "$NPROC_LIMIT" ]]
    [[ $(ulimit -H -u) == "$NPROC_LIMIT" ]]
  )
}

rlimit_compatible || {
  echo 'DEPLOYMENT_STOP incompatible_hard_rlimits' >&2
  exit 69
}

CONTAINMENT_MODE=RLIMIT_AS_PRIMARY
CGROUP_PATH=unavailable
CGROUP_MEMORY_MAX=unavailable
if [[ -r /proc/self/cgroup && -r /sys/fs/cgroup/cgroup.controllers ]]; then
  CGROUP_RELATIVE=$(awk -F: '$1=="0" {print $3}' /proc/self/cgroup)
  if [[ -n "$CGROUP_RELATIVE" && "$CGROUP_RELATIVE" != *..* ]]; then
    CGROUP_PATH="/sys/fs/cgroup${CGROUP_RELATIVE}"
    if [[ -r "$CGROUP_PATH/memory.max" ]]; then
      CGROUP_MEMORY_MAX=$(<"$CGROUP_PATH/memory.max")
      if [[ "$CGROUP_MEMORY_MAX" =~ ^[0-9]+$ ]]; then
        if (( CGROUP_MEMORY_MAX <= 4294967296 )); then
          CONTAINMENT_MODE=RLIMIT_AS_PLUS_CGROUP_V2
        else
          CONTAINMENT_MODE=RLIMIT_AS_PRIMARY_CGROUP_NOT_CONTAINING
        fi
      elif [[ "$CGROUP_MEMORY_MAX" != max ]]; then
        echo "DEPLOYMENT_STOP malformed_cgroup_memory_max=$CGROUP_MEMORY_MAX" >&2
        exit 69
      fi
    fi
  fi
fi
readonly CONTAINMENT_MODE CGROUP_PATH CGROUP_MEMORY_MAX

incompatible_active() {
  ps -eo args= | grep -Eq \
    '[F](258-D|259-D|260-D|261-D|262-D|263-D|264-D|265-D|266-D|267-D|268-D|269-D|270-D|271-D|272-D|273-D|274-D|275-D|276-D|277-D|278-D|279-D|280-D)'
}

refuse_overlap() {
  local phase=$1
  if incompatible_active; then
    echo "RESOURCE_STOP phase=$phase reason=related_process" >&2
    return 73
  fi
}

remaining_seconds() {
  local reserve=${1:-0}
  local remaining=$((PACKET_DEADLINE - SECONDS - reserve))
  (( remaining > 0 )) || {
    echo "RESOURCE_STOP reason=packet_deadline reserve=$reserve" >&2
    return 124
  }
  printf '%s\n' "$remaining"
}

pretarget_resource_gate() {
  local cpus available_kib disk_kib load1
  refuse_overlap pretarget
  cpus=$(nproc)
  available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk_kib=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
  load1=$(awk '{print $1}' /proc/loadavg)
  (( cpus >= 2 )) || { echo "RESOURCE_STOP cpus=$cpus" >&2; return 75; }
  (( available_kib >= MIN_AVAILABLE_KIB )) || {
    echo "RESOURCE_STOP available_kib=$available_kib" >&2
    return 75
  }
  (( disk_kib >= MIN_DISK_KIB )) || {
    echo "RESOURCE_STOP disk_kib=$disk_kib" >&2
    return 75
  }
  awk -v load="$load1" -v cpus="$cpus" 'BEGIN {exit !(load <= 0.75*cpus)}' || {
    echo "RESOURCE_STOP load1=$load1 cpus=$cpus" >&2
    return 75
  }
}

pretarget_resource_gate
remaining_seconds "$MANIFEST_RESERVE_SECONDS" >/dev/null

mkdir -m 0755 -- "$TARGET"
mkdir -m 0755 -- "$TARGET/bin" "$TARGET/logs" "$TARGET/preflight" \
  "$TARGET/staging" "$TARGET/results" "$TARGET/replay"

RUN_START_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
STAGE=initialized
FINAL_STATUS=FAIL
FINAL_EXIT=1
ACTIVE_PID=
SELECTED_RUNG=none
SELECTED_WORKERS=none
PROJECTED_WALL_SECONDS=none
PROJECTED_MEMORY_BYTES=none
PROJECTED_OUTPUT_BYTES=none

owned_bytes() {
  du -sb "$TARGET" | awk '{print $1}'
}

record_resources() {
  local path=$1 phase=$2
  {
    echo "version=$VERSION"
    echo "phase=$phase"
    echo "utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "containment_mode=$CONTAINMENT_MODE"
    echo "cgroup_path=$CGROUP_PATH"
    echo "cgroup_memory_max=$CGROUP_MEMORY_MAX"
    echo "rlimit_as_kib=$ADDRESS_KIB"
    echo "visible_cpus=$(nproc)"
    awk '{print "loadavg=" $0}' /proc/loadavg
    awk '/MemTotal:|MemAvailable:|SwapTotal:|SwapFree:/ {print}' /proc/meminfo
    df -h "$TARGET"
    ps -eo pid,ppid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,40p'
  } >"$path"
}

write_runner_manifest() {
  local trap_status=$?
  set +e
  if [[ -n "$ACTIVE_PID" ]] && kill -0 "$ACTIVE_PID" 2>/dev/null; then
    kill -TERM "$ACTIVE_PID" 2>/dev/null
    for _ in 1 2 3 4 5; do
      kill -0 "$ACTIVE_PID" 2>/dev/null || break
      sleep 1
    done
    kill -KILL "$ACTIVE_PID" 2>/dev/null
    wait "$ACTIVE_PID" 2>/dev/null
  fi
  local manifest_partial="$TARGET/F281-D01.runner.manifest.partial"
  {
    echo "version=$VERSION"
    echo "start_utc=$RUN_START_UTC"
    echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "last_stage=$STAGE"
    echo "final_status=$FINAL_STATUS"
    echo "declared_exit=$FINAL_EXIT"
    echo "trap_status=$trap_status"
    echo "selected_rung=$SELECTED_RUNG"
    echo "selected_workers=$SELECTED_WORKERS"
    echo "projected_wall_seconds=$PROJECTED_WALL_SECONDS"
    echo "projected_memory_bytes=$PROJECTED_MEMORY_BYTES"
    echo "projected_output_bytes=$PROJECTED_OUTPUT_BYTES"
    echo "containment_mode=$CONTAINMENT_MODE"
    echo "cgroup_path=$CGROUP_PATH"
    echo "cgroup_memory_max=$CGROUP_MEMORY_MAX"
    echo "owned_bytes=$(owned_bytes 2>/dev/null || echo unavailable)"
    sha256sum "$SOURCE_DIR"/ALGEBRA.md "$SOURCE_DIR"/PREREGISTRATION.md \
      "$SOURCE_DIR"/search.cpp "$SOURCE_DIR"/remote_run.sh \
      "$SOURCE_DIR"/PROVENANCE.md "$SOURCE_DIR"/VALIDATION_PENDING.md \
      "$SOURCE_DIR"/AUDIT_REQUEST.md \
      "$SOURCE_DIR"/PRELAUNCH_MANIFEST.md "$SOURCE_DIR"/FROZEN.sha256 \
      "$SOURCE_DIR"/HOSTILE_PRERUN_AUDIT.md \
      "$SOURCE_DIR"/HOSTILE_PRERUN_AUDIT.sha256 2>/dev/null
    sha256sum "$TARGET/bin/f281_search" 2>/dev/null
    find "$TARGET" -type f \
      ! -name F281-D01.runner.manifest \
      ! -name F281-D01.runner.manifest.partial -print0 2>/dev/null |
      sort -z | xargs -0 -r sha256sum 2>/dev/null
  } >"$manifest_partial"
  mv -- "$manifest_partial" "$TARGET/F281-D01.runner.manifest"
  exit "$FINAL_EXIT"
}
trap write_runner_manifest EXIT
trap 'FINAL_STATUS=SIGNAL_INT; FINAL_EXIT=130; exit 130' INT
trap 'FINAL_STATUS=SIGNAL_TERM; FINAL_EXIT=143; exit 143' TERM

check_output_cap() {
  local bytes
  bytes=$(owned_bytes)
  (( bytes <= OUTPUT_CAP_BYTES )) || {
    echo "RESOURCE_STOP reason=output_cap bytes=$bytes" >&2
    return 74
  }
}

capacity_gate() {
  local phase=$1 cpus available_kib disk_kib load1
  refuse_overlap "$phase"
  remaining_seconds "$MANIFEST_RESERVE_SECONDS" >/dev/null
  cpus=$(nproc)
  available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk_kib=$(df -Pk "$TARGET" | awk 'NR==2 {print $4}')
  load1=$(awk '{print $1}' /proc/loadavg)
  (( cpus >= 2 )) || { echo "RESOURCE_STOP phase=$phase cpus=$cpus" >&2; return 75; }
  (( available_kib >= MIN_AVAILABLE_KIB )) || {
    echo "RESOURCE_STOP phase=$phase available_kib=$available_kib" >&2
    return 75
  }
  (( disk_kib >= MIN_DISK_KIB )) || {
    echo "RESOURCE_STOP phase=$phase disk_kib=$disk_kib" >&2
    return 75
  }
  awk -v load="$load1" -v cpus="$cpus" 'BEGIN {exit !(load <= 0.75*cpus)}' || {
    echo "RESOURCE_STOP phase=$phase load1=$load1 cpus=$cpus" >&2
    return 75
  }
  check_output_cap
  record_resources "$TARGET/logs/resource_${phase}.txt" "$phase"
}

run_compile() {
  local remaining
  remaining=$(remaining_seconds "$MANIFEST_RESERVE_SECONDS")
  (( remaining > 600 )) && remaining=600
  (
    ulimit -S -v 2097152
    ulimit -H -v 2097152
    ulimit -S -c 0
    ulimit -H -c 0
    ulimit -S -f 131072
    ulimit -H -f 131072
    exec timeout -k 5s "${remaining}s" g++ -std=c++17 -O3 -DNDEBUG -pthread \
      "${FLINT_CFLAGS[@]}" "$SOURCE_DIR/search.cpp" -o "$TARGET/bin/f281_search" \
      "${FLINT_LIBS[@]}" -lgmpxx -lgmp
  ) >"$TARGET/logs/compile.stdout" 2>"$TARGET/logs/compile.stderr"
}

terminate_scientific_pid() {
  local pid=$1 reason=$2
  echo "RESOURCE_STOP scientific_pid=$pid reason=$reason" >&2
  kill -TERM "$pid" 2>/dev/null || true
  for _ in 1 2 3 4 5; do
    kill -0 "$pid" 2>/dev/null || break
    sleep 1
  done
  kill -KILL "$pid" 2>/dev/null || true
}

run_scientific() {
  local label=$1 phase_cap=$2 stdout_path=$3 stderr_path=$4
  shift 4
  local remaining phase_deadline command_status stop_status=0
  capacity_gate "before_${label}"
  remaining=$(remaining_seconds "$MANIFEST_RESERVE_SECONDS")
  (( phase_cap < remaining )) && remaining=$phase_cap
  phase_deadline=$((SECONDS + remaining))
  (
    ulimit -S -v "$ADDRESS_KIB"
    ulimit -H -v "$ADDRESS_KIB"
    ulimit -S -c 0
    ulimit -H -c 0
    ulimit -S -f "$FILE_BLOCKS"
    ulimit -H -f "$FILE_BLOCKS"
    ulimit -S -n "$NOFILE_LIMIT"
    ulimit -H -n "$NOFILE_LIMIT"
    ulimit -S -u "$NPROC_LIMIT"
    ulimit -H -u "$NPROC_LIMIT"
    exec "$TARGET/bin/f281_search" "$@"
  ) >"$stdout_path" 2>"$stderr_path" &
  ACTIVE_PID=$!
  echo "scientific_pid=$ACTIVE_PID label=$label" >"$TARGET/logs/${label}.pid"
  while kill -0 "$ACTIVE_PID" 2>/dev/null; do
    if (( SECONDS >= phase_deadline )); then
      stop_status=124
      terminate_scientific_pid "$ACTIVE_PID" deadline
      break
    fi
    local bytes
    bytes=$(owned_bytes)
    if (( bytes > OUTPUT_CAP_BYTES )); then
      stop_status=74
      terminate_scientific_pid "$ACTIVE_PID" output_cap
      break
    fi
    if incompatible_active; then
      stop_status=73
      terminate_scientific_pid "$ACTIVE_PID" related_process
      break
    fi
    sleep 1
  done
  if wait "$ACTIVE_PID"; then command_status=0; else command_status=$?; fi
  ACTIVE_PID=
  if (( stop_status != 0 )); then return "$stop_status"; fi
  (( command_status == 0 )) || return "$command_status"
  check_output_cap
  record_resources "$TARGET/logs/resource_after_${label}.txt" "after_${label}"
}

exact_output_set() {
  local dir=$1 expected actual
  expected=$'DONE\ncheckpoints.tsv\nsummary.tsv\ntelemetry.tsv\nwitness.tsv'
  actual=$(find "$dir" -mindepth 1 -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]]
}

selftest_output_set() {
  local dir=$1 expected actual
  expected=$'DONE\nselftest.tsv'
  actual=$(find "$dir" -mindepth 1 -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]]
}

production_output_set() {
  local dir=$1 expected actual
  expected=$'DONE\nproduction.tsv'
  actual=$(find "$dir" -mindepth 1 -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]]
  [[ -d "$dir/exact" && -d "$dir/offset" ]]
  exact_output_set "$dir/exact"
  exact_output_set "$dir/offset"
}

tsv_value() {
  local path=$1 key=$2
  awk -F '\t' -v key="$key" '
    NR==1 {for (i=1;i<=NF;i++) if ($i==key) column=i; next}
    NR==2 && column {print $column; rows++}
    END {if (!column || rows!=1 || NR!=2) exit 1}
  ' "$path"
}

validate_lane_output() {
  local dir=$1 expected_lane=$2 expected_s=$3 expected_h=$4
  exact_output_set "$dir"
  [[ $(tsv_value "$dir/summary.tsv" version) == "$VERSION" ]]
  [[ $(tsv_value "$dir/summary.tsv" lane) == "$expected_lane" ]]
  [[ $(tsv_value "$dir/summary.tsv" max_s) == "$expected_s" ]]
  [[ $(tsv_value "$dir/summary.tsv" max_h) == "$expected_h" ]]
  local status witness_lines witnesses
  status=$(tsv_value "$dir/summary.tsv" status)
  witnesses=$(tsv_value "$dir/summary.tsv" witnesses)
  witness_lines=$(wc -l <"$dir/witness.tsv")
  case "$status" in
    PASS)
      [[ "$witnesses" == 0 && "$witness_lines" -eq 1 ]]
      if [[ "$expected_lane" == exact ]]; then
        [[ $(tsv_value "$dir/summary.tsv" tested) == "$expected_s" ]]
      else
        [[ $(tsv_value "$dir/summary.tsv" tested) == \
            $(tsv_value "$dir/summary.tsv" prime_pairs) ]]
      fi
      ;;
    COUNTEREXAMPLE) [[ "$witnesses" == 1 && "$witness_lines" -eq 2 ]] ;;
    *) return 1 ;;
  esac
}

replay_counterexample() {
  local lane=$1 witness_path=$2 destination=$3
  local staging="$TARGET/staging/replay_${lane}"
  [[ ! -e "$staging" && ! -e "$destination" ]]
  run_scientific "replay_${lane}" "$WITNESS_REPLAY_RESERVE_SECONDS" \
    "$TARGET/logs/replay_${lane}.stdout" "$TARGET/logs/replay_${lane}.stderr" \
    "--replay-${lane}" "$witness_path" "$staging"
  [[ $(find "$staging" -mindepth 1 -maxdepth 1 -type f -printf '%f\n' | sort) == \
      $'DONE\nsummary.tsv' ]]
  [[ $(tsv_value "$staging/summary.tsv" status) == PASS ]]
  mv -- "$staging" "$destination"
}

finish_preflight_counterexample() {
  local lane=$1 dir=$2
  replay_counterexample "$lane" "$dir/witness.tsv" "$TARGET/replay/${lane}_preflight"
  STAGE=preflight_counterexample_replayed
  FINAL_STATUS=EXACT_COUNTEREXAMPLE
  FINAL_EXIT=0
  exit 0
}

STAGE=compile
capacity_gate compile
{
  echo "gxx_version=$(g++ -dumpfullversion -dumpversion)"
  echo "flint_version=$(pkg-config --modversion flint)"
  echo "gmp_version=$(pkg-config --modversion gmp)"
  echo "flint_cflags=${FLINT_CFLAGS[*]}"
  echo "flint_libs=${FLINT_LIBS[*]}"
} >"$TARGET/logs/toolchain.txt"
run_compile
[[ -x "$TARGET/bin/f281_search" ]]

STAGE=self_test
run_scientific self_test 300 "$TARGET/logs/self_test.stdout" \
  "$TARGET/logs/self_test.stderr" --self-test "$TARGET/staging/self_test"
selftest_output_set "$TARGET/staging/self_test"
awk -F '\t' '
  NR==1 {ok=($1=="version" && $2=="test" && $3=="status" && NF==3); next}
  NF!=3 || $1!="F281-D01" || $3!="PASS" {bad=1}
  END {exit !(ok && !bad && NR==13)}
' "$TARGET/staging/self_test/selftest.tsv"
grep -Fq $'F281-D01\tdiscarded_false_h_reparameterization\tPASS' \
  "$TARGET/staging/self_test/selftest.tsv"
grep -Fq $'F281-D01\tfixed_divisor_refuted_stronger_diagnostic\tPASS' \
  "$TARGET/staging/self_test/selftest.tsv"
mv -- "$TARGET/staging/self_test" "$TARGET/preflight/self_test"

EXACT_PILOTS=(512 1024 2048)
OFFSET_PILOT_S=(2048 4096 8192)
OFFSET_PILOT_H=(64 64 64)
for index in 0 1 2; do
  s=${EXACT_PILOTS[$index]}
  label="pilot_exact_${s}"
  STAGE=$label
  run_scientific "$label" 1800 "$TARGET/logs/${label}.stdout" \
    "$TARGET/logs/${label}.stderr" --pilot-exact "$s" "$TARGET/staging/$label"
  validate_lane_output "$TARGET/staging/$label" exact "$s" 0
  mv -- "$TARGET/staging/$label" "$TARGET/preflight/$label"
  if [[ $(tsv_value "$TARGET/preflight/$label/summary.tsv" status) == COUNTEREXAMPLE ]]; then
    finish_preflight_counterexample exact "$TARGET/preflight/$label"
  fi
done

for index in 0 1 2; do
  s=${OFFSET_PILOT_S[$index]}
  h=${OFFSET_PILOT_H[$index]}
  label="pilot_offset_${s}_${h}"
  STAGE=$label
  run_scientific "$label" 1800 "$TARGET/logs/${label}.stdout" \
    "$TARGET/logs/${label}.stderr" --pilot-offset "$s" "$h" "$TARGET/staging/$label"
  validate_lane_output "$TARGET/staging/$label" offset "$s" "$h"
  mv -- "$TARGET/staging/$label" "$TARGET/preflight/$label"
  if [[ $(tsv_value "$TARGET/preflight/$label/summary.tsv" status) == COUNTEREXAMPLE ]]; then
    finish_preflight_counterexample offset "$TARGET/preflight/$label"
  fi
done

STAGE=projection
capacity_gate projection
EXACT_TIMES=()
EXACT_LIMBS=()
OFFSET_TIMES=()
OFFSET_LIMBS=()
for s in "${EXACT_PILOTS[@]}"; do
  summary="$TARGET/preflight/pilot_exact_${s}/summary.tsv"
  ns=$(tsv_value "$summary" elapsed_ns)
  EXACT_TIMES+=("$(awk -v ns="$ns" 'BEGIN {printf "%.9f", ns/1000000000}')")
  EXACT_LIMBS+=("$(tsv_value "$summary" limb_bytes)")
done
for index in 0 1 2; do
  s=${OFFSET_PILOT_S[$index]}
  h=${OFFSET_PILOT_H[$index]}
  summary="$TARGET/preflight/pilot_offset_${s}_${h}/summary.tsv"
  ns=$(tsv_value "$summary" elapsed_ns)
  OFFSET_TIMES+=("$(awk -v ns="$ns" 'BEGIN {printf "%.9f", ns/1000000000}')")
  OFFSET_LIMBS+=("$(tsv_value "$summary" limb_bytes)")
done

RUNG_EXACT=(4000 6000 8000 10000 12000 16000)
RUNG_OFFSET_S=(25000 50000 100000 150000 200000 300000)
RUNG_OFFSET_H=(32 48 64 64 64 64)
VISIBLE_CPUS=$(nproc)
PROJECTION_FILE="$TARGET/preflight/resource_gate.tsv"
echo $'version\trung\texact_s\toffset_s\toffset_h\tprojected_exact_seconds\tprojected_offset_seconds\tprojected_wall_seconds\tprojected_exact_bytes\tprojected_offset_bytes\tprojected_memory_bytes\tprojected_output_bytes\tworkers\tdecision' >"$PROJECTION_FILE"

remaining=$(remaining_seconds "$WITNESS_REPLAY_RESERVE_SECONDS")
for rung in 0 1 2 3 4 5; do
  exact_s=${RUNG_EXACT[$rung]}
  offset_s=${RUNG_OFFSET_S[$rung]}
  offset_h=${RUNG_OFFSET_H[$rung]}
  projection=$(awk \
    -v ea0="${EXACT_PILOTS[0]}" -v ea1="${EXACT_PILOTS[1]}" -v ea2="${EXACT_PILOTS[2]}" \
    -v et0="${EXACT_TIMES[0]}" -v et1="${EXACT_TIMES[1]}" -v et2="${EXACT_TIMES[2]}" \
    -v el0="${EXACT_LIMBS[0]}" -v el1="${EXACT_LIMBS[1]}" -v el2="${EXACT_LIMBS[2]}" \
    -v ob0="${OFFSET_PILOT_S[0]}" -v ob1="${OFFSET_PILOT_S[1]}" -v ob2="${OFFSET_PILOT_S[2]}" \
    -v oh0="${OFFSET_PILOT_H[0]}" -v oh1="${OFFSET_PILOT_H[1]}" -v oh2="${OFFSET_PILOT_H[2]}" \
    -v ot0="${OFFSET_TIMES[0]}" -v ot1="${OFFSET_TIMES[1]}" -v ot2="${OFFSET_TIMES[2]}" \
    -v ol0="${OFFSET_LIMBS[0]}" -v ol1="${OFFSET_LIMBS[1]}" -v ol2="${OFFSET_LIMBS[2]}" \
    -v es="$exact_s" -v os="$offset_s" -v oh="$offset_h" '
      function wa(s) {return s*s*s*log(s+1)}
      function ma(s) {return s*s*log(s+1)}
      function wb(s,h) {return h*s*s*log(s+1)}
      function mb(s,h) {return h*s*log(s+1)}
      function max(a,b) {return a>b?a:b}
      BEGIN {
        ert=max(et0/wa(ea0),max(et1/wa(ea1),et2/wa(ea2)))
        erm=max(el0/ma(ea0),max(el1/ma(ea1),el2/ma(ea2)))
        ort=max(ot0/wb(ob0,oh0),max(ot1/wb(ob1,oh1),ot2/wb(ob2,oh2)))
        orm=max(ol0/mb(ob0,oh0),max(ol1/mb(ob1,oh1),ol2/mb(ob2,oh2)))
        pe=2.5*ert*wa(es)
        po=2.5*ort*wb(os,oh)
        me=268435456+2.5*erm*ma(es)
        mo=268435456+2.5*orm*mb(os,oh)
        out=33554432+16*es*log(es+1)/log(2)+8*(os+2*oh+1)*log(os+2*oh+2)/log(2)
        printf "%.6f %.6f %.0f %.0f %.0f", pe,po,me,mo,out
      }')
  IFS=' ' read -r projected_exact projected_offset projected_exact_bytes \
    projected_offset_bytes projected_output <<<"$projection"
  workers=1
  projected_wall=$(awk -v a="$projected_exact" -v b="$projected_offset" \
    'BEGIN {printf "%.6f", a+b}')
  projected_memory=$(awk -v a="$projected_exact_bytes" -v b="$projected_offset_bytes" \
    'BEGIN {printf "%.0f", a>b?a:b}')
  if (( VISIBLE_CPUS >= 4 )); then
    parallel_memory=$(awk -v a="$projected_exact_bytes" -v b="$projected_offset_bytes" \
      'BEGIN {printf "%.0f", a+b}')
    parallel_wall=$(awk -v a="$projected_exact" -v b="$projected_offset" \
      'BEGIN {m=a>b?a:b; printf "%.6f", 1.10*m}')
    if awk -v memory="$parallel_memory" -v cap="$PROJECTED_MEMORY_CAP_BYTES" \
         -v wall="$parallel_wall" -v sequential="$projected_wall" \
         'BEGIN {exit !(memory<=cap && wall<sequential)}'; then
      workers=2
      projected_memory=$parallel_memory
      projected_wall=$parallel_wall
    fi
  fi
  decision=REJECT
  if awk -v wall="$projected_wall" -v remaining="$remaining" \
       -v memory="$projected_memory" -v memory_cap="$PROJECTED_MEMORY_CAP_BYTES" \
       -v output="$projected_output" -v output_cap="$PROJECTED_OUTPUT_CAP_BYTES" \
       'BEGIN {exit !(wall<=12600 && wall+600<=remaining && memory<=memory_cap && output<=output_cap)}'; then
    decision=SELECTABLE
    SELECTED_RUNG=$rung
    SELECTED_WORKERS=$workers
    PROJECTED_WALL_SECONDS=$projected_wall
    PROJECTED_MEMORY_BYTES=$projected_memory
    PROJECTED_OUTPUT_BYTES=$projected_output
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$VERSION" "$rung" "$exact_s" "$offset_s" "$offset_h" \
    "$projected_exact" "$projected_offset" "$projected_wall" \
    "$projected_exact_bytes" "$projected_offset_bytes" "$projected_memory" \
    "$projected_output" "$workers" "$decision" >>"$PROJECTION_FILE"
done

[[ "$SELECTED_RUNG" != none ]] || {
  echo 'RESOURCE_STOP reason=no_production_rung' >&2
  exit 75
}
(( SELECTED_WORKERS >= 1 && SELECTED_WORKERS <= MAX_WORKERS ))
SELECTED_EXACT=${RUNG_EXACT[$SELECTED_RUNG]}
SELECTED_OFFSET_S=${RUNG_OFFSET_S[$SELECTED_RUNG]}
SELECTED_OFFSET_H=${RUNG_OFFSET_H[$SELECTED_RUNG]}

STAGE=production
capacity_gate production
production_cap=$(remaining_seconds "$WITNESS_REPLAY_RESERVE_SECONDS")
(( production_cap <= 12600 )) || production_cap=12600
run_scientific production "$production_cap" "$TARGET/logs/production.stdout" \
  "$TARGET/logs/production.stderr" --production "$SELECTED_EXACT" \
  "$SELECTED_OFFSET_S" "$SELECTED_OFFSET_H" "$SELECTED_WORKERS" \
  "$TARGET/staging/production"
production_output_set "$TARGET/staging/production"
validate_lane_output "$TARGET/staging/production/exact" exact "$SELECTED_EXACT" 0
validate_lane_output "$TARGET/staging/production/offset" offset "$SELECTED_OFFSET_S" \
  "$SELECTED_OFFSET_H"
[[ $(tsv_value "$TARGET/staging/production/production.tsv" version) == "$VERSION" ]]
[[ $(tsv_value "$TARGET/staging/production/production.tsv" workers) == "$SELECTED_WORKERS" ]]
[[ $(tsv_value "$TARGET/staging/production/production.tsv" exact_status) == \
    $(tsv_value "$TARGET/staging/production/exact/summary.tsv" status) ]]
[[ $(tsv_value "$TARGET/staging/production/production.tsv" offset_status) == \
    $(tsv_value "$TARGET/staging/production/offset/summary.tsv" status) ]]
[[ $(tsv_value "$TARGET/staging/production/production.tsv" exact_tested) == \
    $(tsv_value "$TARGET/staging/production/exact/summary.tsv" tested) ]]
[[ $(tsv_value "$TARGET/staging/production/production.tsv" offset_tested) == \
    $(tsv_value "$TARGET/staging/production/offset/summary.tsv" tested) ]]
exact_maxrss_kib=$(tsv_value "$TARGET/staging/production/exact/summary.tsv" maxrss_kib)
offset_maxrss_kib=$(tsv_value "$TARGET/staging/production/offset/summary.tsv" maxrss_kib)
actual_maxrss_kib=$(( exact_maxrss_kib > offset_maxrss_kib ? exact_maxrss_kib : offset_maxrss_kib ))
actual_maxrss_bytes=$(( actual_maxrss_kib * 1024 ))
(( actual_maxrss_bytes <= PROJECTED_MEMORY_CAP_BYTES )) || {
  echo "RESOURCE_STOP reason=actual_memory_cap bytes=$actual_maxrss_bytes" >&2
  exit 75
}
awk -v actual="$actual_maxrss_bytes" -v projected="$PROJECTED_MEMORY_BYTES" \
  'BEGIN {exit !(actual<=projected)}' || {
  echo "RESOURCE_STOP reason=memory_projection_breach actual=$actual_maxrss_bytes projected=$PROJECTED_MEMORY_BYTES" >&2
  exit 75
}
mv -- "$TARGET/staging/production" "$TARGET/results/production"

exact_status=$(tsv_value "$TARGET/results/production/exact/summary.tsv" status)
offset_status=$(tsv_value "$TARGET/results/production/offset/summary.tsv" status)
if [[ "$exact_status" == COUNTEREXAMPLE ]]; then
  STAGE=replay_exact
  replay_counterexample exact "$TARGET/results/production/exact/witness.tsv" \
    "$TARGET/replay/exact"
fi
if [[ "$offset_status" == COUNTEREXAMPLE ]]; then
  STAGE=replay_offset
  replay_counterexample offset "$TARGET/results/production/offset/witness.tsv" \
    "$TARGET/replay/offset"
fi

STAGE=final_checks
capacity_gate final_checks
check_output_cap
record_resources "$TARGET/logs/resource_final.txt" final
if [[ "$exact_status" == COUNTEREXAMPLE || "$offset_status" == COUNTEREXAMPLE ]]; then
  FINAL_STATUS=EXACT_COUNTEREXAMPLE
else
  FINAL_STATUS=FINITE_NULL_EVIDENCE
fi
STAGE=complete
FINAL_EXIT=0
exit 0
