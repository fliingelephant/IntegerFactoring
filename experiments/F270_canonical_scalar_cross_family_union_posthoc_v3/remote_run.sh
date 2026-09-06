#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
export LC_ALL=C TZ=UTC
unset TAR_OPTIONS GZIP POSIXLY_CORRECT
umask 022

if [[ $# -ne 6 ]]; then
  echo "usage: remote_run.sh EVIDENCE BANKS CORPUS ABSOLUTE_NEW_RUN_DIR WORKERS APPROVED_FROZEN_ROOT" >&2
  exit 64
fi

SOURCE_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
EVIDENCE=$1
BANKS=$2
CORPUS=$3
RUN_DIR=$4
WORKERS=$5
APPROVED_FROZEN_ROOT=$6
VERSION=F270-D03
MEMORY_MAX=3758096384
RLIMIT_AS_KIB=4194304
PACKET_OUTPUT_CAP=536870912
PREFLIGHT_OUTPUT_BUDGET=16777216
TARGET_OUTPUT_BUDGET=201326592
OUTPUT_METADATA_ALLOWANCE=65536
RELATION_PAYLOAD_CAP=100663296
LOG_FILE_CAP=1048576
LOG_TOTAL_CAP=16777216
SIDECAR_CAP=33554432
BINARY_CAP=16777216
COMPRESSION_SLACK=4194304
MIN_DISK_BYTES=4294967296
PACKET_SECONDS=14400
CLOSURE_SECONDS=600
MANIFEST_SECONDS=120
PROCESS_SNAPSHOT_CAP=1048576
PROCESS_IDENTITY_CAP=262144
PROCESS_PID_CAP=16384
PROCESS_ANCESTOR_DEPTH_CAP=64
PROCESS_ANCESTOR_BYTE_CAP=16384
readonly SOURCE_DIR EVIDENCE BANKS CORPUS RUN_DIR WORKERS APPROVED_FROZEN_ROOT VERSION
readonly MEMORY_MAX RLIMIT_AS_KIB PACKET_OUTPUT_CAP PREFLIGHT_OUTPUT_BUDGET TARGET_OUTPUT_BUDGET OUTPUT_METADATA_ALLOWANCE
readonly RELATION_PAYLOAD_CAP LOG_FILE_CAP LOG_TOTAL_CAP SIDECAR_CAP BINARY_CAP COMPRESSION_SLACK
readonly MIN_DISK_BYTES PACKET_SECONDS CLOSURE_SECONDS MANIFEST_SECONDS
readonly PROCESS_SNAPSHOT_CAP PROCESS_IDENTITY_CAP PROCESS_PID_CAP PROCESS_ANCESTOR_DEPTH_CAP PROCESS_ANCESTOR_BYTE_CAP

[[ "$WORKERS" =~ ^[1-8]$ ]]
[[ "$APPROVED_FROZEN_ROOT" =~ ^[0-9a-f]{64}$ ]]
case "$RUN_DIR" in /*) ;; *) echo "run directory must be absolute" >&2; exit 64;; esac
[[ "$RUN_DIR" != / && "$RUN_DIR" != /root && "$RUN_DIR" != /tmp && "$RUN_DIR" != "$SOURCE_DIR" ]]
[[ ! -e "$RUN_DIR" ]] || { echo "run directory exists: $RUN_DIR" >&2; exit 73; }
for input in "$EVIDENCE" "$BANKS" "$CORPUS"; do
  [[ -f "$input" ]] || { echo "missing input: $input" >&2; exit 66; }
done
for command in awk basename cat cmp date df dirname du find flock free g++ grep gzip head mkdir mkfifo mv nice nproc \
  pkill readlink rm rmdir sed sha256sum sleep sort stat tar timeout uname wc xargs; do
  command -v "$command" >/dev/null
done
[[ -x /usr/bin/time ]]

cd -- "$SOURCE_DIR"
sha256sum -c FROZEN.sha256
FROZEN_ROOT=$(sha256sum FROZEN.sha256 | awk '{print $1}')
readonly FROZEN_ROOT
[[ "$FROZEN_ROOT" == "$APPROVED_FROZEN_ROOT" ]]
[[ -f HOSTILE_PRERUN_AUDIT.md && -f HOSTILE_PRERUN_AUDIT.sha256 ]]
sha256sum -c HOSTILE_PRERUN_AUDIT.sha256
AUDIT_SHA=$(sha256sum HOSTILE_PRERUN_AUDIT.md | awk '{print $1}')
readonly AUDIT_SHA
grep -Fqx 'verdict: PASS' HOSTILE_PRERUN_AUDIT.md
grep -Fqx "frozen_manifest_sha256: $FROZEN_ROOT" HOSTILE_PRERUN_AUDIT.md

[[ $(sha256sum "$EVIDENCE" | awk '{print $1}') == a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc ]]
[[ $(sha256sum "$BANKS" | awk '{print $1}') == c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6 ]]
[[ $(sha256sum "$CORPUS" | awk '{print $1}') == 8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5 ]]

monotonic_seconds() {
  awk '{print int($1)}' /proc/uptime
}

remaining_until() {
  local deadline=$1 now remaining
  now=$(monotonic_seconds)
  remaining=$((deadline-now-16))
  [[ $remaining -gt 0 ]] || { echo "RESOURCE_STOP reason=packet_deadline" >&2; exit 124; }
  printf '%s\n' "$remaining"
}

LOCK_PATH=/tmp/integer_factoring.production.lock
readonly LOCK_PATH
exec 9>>"$LOCK_PATH"
flock -n 9 || { echo "RESOURCE_STOP reason=production_lock" >&2; exit 73; }

CPUS=$(nproc)
LOAD=$(awk '{print $1}' /proc/loadavg)
MEM_AVAILABLE_KIB=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
RUN_PARENT=$(dirname -- "$RUN_DIR")
DISK_AVAILABLE_KIB=$(df -Pk "$RUN_PARENT" | awk 'NR==2 {print $4}')
readonly CPUS LOAD MEM_AVAILABLE_KIB RUN_PARENT DISK_AVAILABLE_KIB
awk -v load="$LOAD" -v cpus="$CPUS" -v workers="$WORKERS" 'BEGIN {exit !(load+workers<=cpus)}' || {
  echo "RESOURCE_STOP reason=load load=$LOAD cpus=$CPUS workers=$WORKERS" >&2; exit 75;
}
[[ "$MEM_AVAILABLE_KIB" -ge 8388608 ]] || {
  echo "RESOURCE_STOP reason=memory available_kib=$MEM_AVAILABLE_KIB" >&2; exit 75;
}
[[ $((DISK_AVAILABLE_KIB*1024)) -ge $MIN_DISK_BYTES ]] || {
  echo "RESOURCE_STOP reason=disk available_kib=$DISK_AVAILABLE_KIB" >&2; exit 75;
}

CGROUP_PARENT_REL=$(awk -F: '$1=="0" {print $3}' /proc/$$/cgroup)
CGROUP_PARENT="/sys/fs/cgroup${CGROUP_PARENT_REL}"
CGROUP="$CGROUP_PARENT/f270_d03_$$"
readonly CGROUP_PARENT_REL CGROUP_PARENT CGROUP
[[ -f /sys/fs/cgroup/cgroup.controllers && -w "$CGROUP_PARENT/cgroup.procs" ]]
mkdir -- "$CGROUP"
[[ -w "$CGROUP/memory.max" && -w "$CGROUP/memory.swap.max" && -w "$CGROUP/cgroup.procs" && -w "$CGROUP/cgroup.kill" ]]
[[ -r "$CGROUP/memory.current" && -r "$CGROUP/memory.peak" && -r "$CGROUP/memory.events" ]]
printf '%s\n' "$MEMORY_MAX" >"$CGROUP/memory.max"
printf '0\n' >"$CGROUP/memory.swap.max"
if [[ -w "$CGROUP/memory.oom.group" ]]; then printf '1\n' >"$CGROUP/memory.oom.group"; fi
[[ $(<"$CGROUP/memory.max") == "$MEMORY_MAX" && $(<"$CGROUP/memory.swap.max") == 0 ]]

START_SECONDS=$(monotonic_seconds)
HARD_DEADLINE=$((START_SECONDS+PACKET_SECONDS))
ACTIVE_DEADLINE=$((HARD_DEADLINE-CLOSURE_SECONDS))
ARCHIVE_DEADLINE=$((HARD_DEADLINE-MANIFEST_SECONDS))
readonly START_SECONDS HARD_DEADLINE ACTIVE_DEADLINE ARCHIVE_DEADLINE

(
  exec 9>&-
  remaining=$((HARD_DEADLINE-$(monotonic_seconds)))
  [[ $remaining -gt 0 ]] && sleep "$remaining"
  printf '1\n' >"$CGROUP/cgroup.kill" || true
  sleep 1
  rmdir -- "$CGROUP" 2>/dev/null || true
) &
WATCHDOG_PID=$!
readonly WATCHDOG_PID

cleanup() {
  set +e
  pkill -TERM -P "$WATCHDOG_PID" 2>/dev/null
  kill "$WATCHDOG_PID" 2>/dev/null
  wait "$WATCHDOG_PID" 2>/dev/null
  if [[ -d "$CGROUP" ]]; then
    printf '%s\n' $$ >"$CGROUP_PARENT/cgroup.procs" 2>/dev/null
    printf '1\n' >"$CGROUP/cgroup.kill" 2>/dev/null
    for _ in 1 2 3 4 5 6 7 8 9 10; do
      rmdir -- "$CGROUP" 2>/dev/null && break
      sleep 0.1
    done
  fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
printf '%s\n' $$ >"$CGROUP/cgroup.procs"

ulimit -Sv "$RLIMIT_AS_KIB"
ulimit -Hv "$RLIMIT_AS_KIB"
ulimit -Sf 393216
ulimit -Hf 393216

mkdir -m 0755 -- "$RUN_DIR" "$RUN_DIR/bin" "$RUN_DIR/logs"
{
  printf 'version\t%s\nfrozen_manifest_sha256\t%s\naudit_sha256\t%s\n' "$VERSION" "$FROZEN_ROOT" "$AUDIT_SHA"
  printf 'start_monotonic_seconds\t%s\nhard_deadline_monotonic_seconds\t%s\n' "$START_SECONDS" "$HARD_DEADLINE"
  date -u '+utc=%Y-%m-%dT%H:%M:%SZ'
  uname -a
  uptime
  free -h
  df -h "$RUN_PARENT"
} | head -c "$LOG_FILE_CAP" >"$RUN_DIR/resource_before.txt"

read_proc_stat() {
  local pid=$1 ppid_destination=$2 start_destination=$3 line prefix rest
  local -a fields
  [[ "$pid" =~ ^[0-9]+$ ]] || return 1
  IFS= read -r line <"/proc/$pid/stat" || return 1
  prefix=${line%% (*}
  [[ "$prefix" == "$pid" && "$line" == *') '* ]] || return 1
  rest=${line##*) }
  read -r -a fields <<<"$rest"
  [[ ${#fields[@]} -ge 20 ]] || return 1
  [[ "${fields[1]}" =~ ^[0-9]+$ && "${fields[19]}" =~ ^[0-9]+$ ]] || return 1
  printf -v "$ppid_destination" '%s' "${fields[1]}"
  printf -v "$start_destination" '%s' "${fields[19]}"
}

declare -A EXCLUDED_START EXCLUDED_PPID EXCLUDED_KIND
ANCESTOR_CHAIN=
ancestor=$$
ancestor_depth=0
while :; do
  ((ancestor_depth < PROCESS_ANCESTOR_DEPTH_CAP)) || {
    echo "RESOURCE_STOP reason=ancestor_depth_cap_before_pid1" >&2
    exit 76
  }
  [[ -z "${EXCLUDED_START[$ancestor]+x}" ]] || {
    echo "RESOURCE_STOP reason=ancestor_cycle" >&2
    exit 76
  }
  read_proc_stat "$ancestor" ancestor_ppid ancestor_start || {
    echo "RESOURCE_STOP reason=ancestor_proc_read" >&2
    exit 76
  }
  EXCLUDED_START[$ancestor]=$ancestor_start
  EXCLUDED_PPID[$ancestor]=$ancestor_ppid
  EXCLUDED_KIND[$ancestor]=ANCESTOR
  ancestor_record="$ancestor:$ancestor_start:$ancestor_ppid"
  if [[ -n "$ANCESTOR_CHAIN" ]]; then ANCESTOR_CHAIN+=","; fi
  ANCESTOR_CHAIN+="$ancestor_record"
  (( ${#ANCESTOR_CHAIN} <= PROCESS_ANCESTOR_BYTE_CAP )) || {
    echo "RESOURCE_STOP reason=ancestor_byte_cap_before_pid1" >&2
    exit 76
  }
  ancestor_depth=$((ancestor_depth+1))
  if [[ "$ancestor" -eq 1 ]]; then
    [[ "$ancestor_ppid" -eq 0 ]] || {
      echo "RESOURCE_STOP reason=pid1_parent_inconsistent" >&2
      exit 76
    }
    break
  fi
  [[ "$ancestor_ppid" -gt 0 ]] || {
    echo "RESOURCE_STOP reason=ancestor_chain_did_not_reach_pid1" >&2
    exit 76
  }
  ancestor=$ancestor_ppid
done
readonly ANCESTOR_CHAIN ancestor_depth

read_proc_stat "$WATCHDOG_PID" watchdog_ppid WATCHDOG_STARTTIME || {
  echo "RESOURCE_STOP reason=watchdog_proc_read" >&2
  exit 76
}
[[ "$watchdog_ppid" -eq $$ && -z "${EXCLUDED_START[$WATCHDOG_PID]+x}" ]] || {
  echo "RESOURCE_STOP reason=watchdog_identity_inconsistent" >&2
  exit 76
}
EXCLUDED_START[$WATCHDOG_PID]=$WATCHDOG_STARTTIME
EXCLUDED_PPID[$WATCHDOG_PID]=$watchdog_ppid
EXCLUDED_KIND[$WATCHDOG_PID]=WATCHDOG
WATCHDOG_IDENTITY="$WATCHDOG_PID:$WATCHDOG_STARTTIME:$watchdog_ppid"
readonly WATCHDOG_STARTTIME WATCHDOG_IDENTITY

PID_LIST_A="$RUN_DIR/.process_pids_a"
PID_LIST_B="$RUN_DIR/.process_pids_b"
PID_LIST_C="$RUN_DIR/.process_pids_c"
LINK_SCRATCH="$RUN_DIR/.process_link"
readonly PID_LIST_A PID_LIST_B PID_LIST_C LINK_SCRATCH

capture_pid_list() {
  local output=$1 path pid count=0 bytes=0
  local -a proc_paths
  shopt -s nullglob
  proc_paths=(/proc/[0-9]*)
  shopt -u nullglob
  [[ ${#proc_paths[@]} -gt 0 && ${#proc_paths[@]} -le PROCESS_PID_CAP ]] || return 1
  : >"$output" || return 1
  for path in "${proc_paths[@]}"; do
    pid=${path##*/}
    [[ "$pid" =~ ^[0-9]+$ ]] || return 1
    count=$((count+1))
    bytes=$((bytes+${#pid}+1))
    (( count <= PROCESS_PID_CAP && bytes <= PROCESS_SNAPSHOT_CAP )) || return 1
    printf '%s\n' "$pid" >>"$output" || return 1
  done
  sort -n -o "$output" "$output" || return 1
}

read_proc_link() {
  local pid=$1 name=$2 destination=$3 fd value
  : >"$LINK_SCRATCH" || return 1
  readlink -z -- "/proc/$pid/$name" >"$LINK_SCRATCH" || return 1
  exec {fd}<"$LINK_SCRATCH" || return 1
  value=
  if ! IFS= read -r -d '' value <&"$fd"; then
    exec {fd}<&-
    return 1
  fi
  exec {fd}<&-
  (( ${#value} <= PROCESS_IDENTITY_CAP )) || return 1
  printf -v "$destination" '%s' "$value"
}

has_remote_run_name() {
  local value=$1
  [[ "$value" =~ (^|[^[:alnum:]_])remote_run([.]sh)?([^[:alnum:]_.]|$) ]]
}

scan_processes() {
  local pid_list=$1 output=$2 pid ppid_before ppid_after start_before start_after
  local PROC_EXE PROC_CWD exe_q cwd_q cmd_q arg arg_q previous_arg line disposition fd
  local count=0 bytes=0 argc raw_cmd_bytes remote_name semantic_mode identity_ftag identity_workload
  local overlap=0 header
  local -A excluded_seen
  header=$'pid\tppid\tstarttime\tdisposition\texecutable_q\tcwd_q\targc\targv_q\n'
  bytes=${#header}
  (( bytes <= PROCESS_SNAPSHOT_CAP )) || return 1
  printf '%s' "$header" >"$output" || return 1
  while IFS= read -r pid; do
    [[ "$pid" =~ ^[0-9]+$ ]] || return 1
    count=$((count+1))
    (( count <= PROCESS_PID_CAP )) || return 1
    read_proc_stat "$pid" ppid_before start_before || return 1
    read_proc_link "$pid" exe PROC_EXE || return 1
    read_proc_link "$pid" cwd PROC_CWD || return 1

    argc=0
    raw_cmd_bytes=0
    cmd_q=
    remote_name=0
    semantic_mode=0
    identity_ftag=0
    identity_workload=0
    previous_arg=
    exec {fd}<"/proc/$pid/cmdline" || return 1
    while :; do
      arg=
      if IFS= read -r -d '' arg <&"$fd"; then
        argc=$((argc+1))
        raw_cmd_bytes=$((raw_cmd_bytes+${#arg}+1))
        (( raw_cmd_bytes <= PROCESS_IDENTITY_CAP )) || {
          exec {fd}<&-
          return 1
        }
        printf -v arg_q '%q' "$arg"
        if [[ -n "$cmd_q" ]]; then cmd_q+=' '; fi
        cmd_q+="$arg_q"
        has_remote_run_name "$arg" && remote_name=1
        if [[ "$previous_arg" == --mode && "$arg" =~ ^(target|discovery|heldout|complete|production)$ ]]; then
          semantic_mode=1
        fi
        [[ "$arg" =~ ^--(target|discovery|heldout|complete|production)$ ]] && semantic_mode=1
        [[ "$arg" =~ ^--mode=(target|discovery|heldout|complete|production)$ ]] && semantic_mode=1
        [[ "$arg" =~ (^|[[:space:]])--mode[[:space:]]+(target|discovery|heldout|complete|production)([[:space:]]|$) ]] && semantic_mode=1
        [[ "$arg" =~ (^|[[:space:]])--(target|discovery|heldout|complete|production)([[:space:]]|$) ]] && semantic_mode=1
        [[ "$arg" =~ (^|[[:space:]])--mode=(target|discovery|heldout|complete|production)([[:space:]]|$) ]] && semantic_mode=1
        [[ "$arg" =~ [Ff][0-9][0-9][0-9][-_] ]] && identity_ftag=1
        [[ "$arg" =~ (remote_run|search|union|multirow|lift|factor|production) ]] && identity_workload=1
        previous_arg=$arg
      else
        [[ -z "$arg" ]] || {
          exec {fd}<&-
          return 1
        }
        break
      fi
    done
    exec {fd}<&-
    [[ -n "$cmd_q" ]] || cmd_q=-

    has_remote_run_name "$PROC_EXE" && remote_name=1
    has_remote_run_name "$PROC_CWD" && remote_name=1

    read_proc_stat "$pid" ppid_after start_after || return 1
    [[ "$ppid_before" == "$ppid_after" && "$start_before" == "$start_after" ]] || return 1
    printf -v exe_q '%q' "$PROC_EXE"
    printf -v cwd_q '%q' "$PROC_CWD"

    disposition=CLEAR
    if [[ -n "${EXCLUDED_START[$pid]+x}" ]]; then
      [[ "$start_before" == "${EXCLUDED_START[$pid]}" && "$ppid_before" == "${EXCLUDED_PPID[$pid]}" ]] || return 1
      disposition="EXCLUDED_${EXCLUDED_KIND[$pid]}"
      excluded_seen[$pid]=1
    elif (( remote_name )); then
      disposition=OVERLAP_REMOTE_RUN
      overlap=1
    elif (( semantic_mode || (identity_ftag && identity_workload) )); then
      disposition=OVERLAP_SEMANTIC
      overlap=1
    fi

    line="$pid"$'\t'"$ppid_before"$'\t'"$start_before"$'\t'"$disposition"$'\t'"$exe_q"$'\t'"$cwd_q"$'\t'"$argc"$'\t'"$cmd_q"$'\n'
    (( ${#line} <= PROCESS_IDENTITY_CAP )) || return 1
    bytes=$((bytes+${#line}))
    (( bytes <= PROCESS_SNAPSHOT_CAP )) || return 1
    printf '%s' "$line" >>"$output" || return 1
  done <"$pid_list"

  for pid in "${!EXCLUDED_START[@]}"; do
    [[ -n "${excluded_seen[$pid]+x}" ]] || return 1
  done
  PROCESS_SCAN_COUNT=$count
  PROCESS_SCAN_BYTES=$bytes
  PROCESS_SCAN_OVERLAP=$overlap
}

if ! capture_pid_list "$PID_LIST_A" ||
   ! scan_processes "$PID_LIST_A" "$RUN_DIR/process_before.tsv"; then
  echo "RESOURCE_STOP reason=process_snapshot_a_read_or_cap" >&2
  exit 76
fi
PROCESS_A_COUNT=$PROCESS_SCAN_COUNT
PROCESS_A_BYTES=$PROCESS_SCAN_BYTES
PROCESS_A_OVERLAP=$PROCESS_SCAN_OVERLAP
[[ $(stat -c %s "$RUN_DIR/process_before.tsv") -eq "$PROCESS_A_BYTES" ]] || {
  echo "RESOURCE_STOP reason=process_snapshot_a_byte_inconsistency" >&2
  exit 76
}
if ! capture_pid_list "$PID_LIST_B" || ! cmp -s "$PID_LIST_A" "$PID_LIST_B" ||
   ! scan_processes "$PID_LIST_B" "$RUN_DIR/process_verify.tsv"; then
  echo "RESOURCE_STOP reason=process_snapshot_b_read_cap_or_pid_inconsistency" >&2
  exit 76
fi
PROCESS_B_COUNT=$PROCESS_SCAN_COUNT
PROCESS_B_BYTES=$PROCESS_SCAN_BYTES
PROCESS_B_OVERLAP=$PROCESS_SCAN_OVERLAP
[[ $(stat -c %s "$RUN_DIR/process_verify.tsv") -eq "$PROCESS_B_BYTES" ]] || {
  echo "RESOURCE_STOP reason=process_snapshot_b_byte_inconsistency" >&2
  exit 76
}
if ! capture_pid_list "$PID_LIST_C" || ! cmp -s "$PID_LIST_B" "$PID_LIST_C" ||
   ! cmp -s "$RUN_DIR/process_before.tsv" "$RUN_DIR/process_verify.tsv" ||
   [[ "$PROCESS_A_COUNT" -ne "$PROCESS_B_COUNT" || "$PROCESS_A_BYTES" -ne "$PROCESS_B_BYTES" ]]; then
  echo "RESOURCE_STOP reason=process_snapshot_identity_or_pid_inconsistency" >&2
  exit 76
fi
rm -f -- "$PID_LIST_A" "$PID_LIST_B" "$PID_LIST_C" "$LINK_SCRATCH"
if [[ "$PROCESS_A_OVERLAP" -ne 0 || "$PROCESS_B_OVERLAP" -ne 0 ]]; then
  echo "RESOURCE_STOP reason=production_process_overlap" >&2
  exit 76
fi
PROCESS_FIREWALL=PASS
RESOURCE_BEFORE_SHA=$(sha256sum "$RUN_DIR/resource_before.txt" | awk '{print $1}')
PROCESS_BEFORE_SHA=$(sha256sum "$RUN_DIR/process_before.tsv" | awk '{print $1}')
PROCESS_VERIFY_SHA=$(sha256sum "$RUN_DIR/process_verify.tsv" | awk '{print $1}')
readonly RESOURCE_BEFORE_SHA PROCESS_BEFORE_SHA PROCESS_VERIFY_SHA PROCESS_FIREWALL
{
  printf 'key\tvalue\nfirewall\t%s\nscan_algorithm\tprocfs_pid_sorted_double_snapshot_v1\n' "$PROCESS_FIREWALL"
  printf 'process_snapshot_sha256\t%s\nprocess_verify_sha256\t%s\nprocess_count\t%s\nprocess_snapshot_bytes\t%s\n' \
    "$PROCESS_BEFORE_SHA" "$PROCESS_VERIFY_SHA" "$PROCESS_A_COUNT" "$PROCESS_A_BYTES"
  printf 'excluded_ancestor_chain_pid_starttime_ppid\t%s\nexcluded_ancestor_count\t%s\n' \
    "$ANCESTOR_CHAIN" "$ancestor_depth"
  printf 'excluded_watchdog_pid_starttime_ppid\t%s\nlock_path\t%s\n' "$WATCHDOG_IDENTITY" "$LOCK_PATH"
} >"$RUN_DIR/process_ack.tsv"
PROCESS_ACK_SHA=$(sha256sum "$RUN_DIR/process_ack.tsv" | awk '{print $1}')
readonly PROCESS_ACK_SHA

regular_bytes() {
  find "$RUN_DIR" -type f -printf '%s\n' | awk '{s+=$1} END {printf "%.0f\n",s+0}'
}

du_gate() {
  local phase=$1 regular apparent
  [[ -z $(find "$RUN_DIR" -type l -print -quit) ]]
  [[ -z $(find "$RUN_DIR" -type f -links +1 -print -quit) ]]
  find "$RUN_DIR" -type f -printf '%b\t%s\n' | awk '$2>0 && $1*512<$2 {bad=1} END {exit bad}'
  regular=$(regular_bytes)
  apparent=$(du -sb --apparent-size -- "$RUN_DIR" | awk '{print $1}')
  [[ "$regular" -le "$PACKET_OUTPUT_CAP" && "$apparent" -le "$PACKET_OUTPUT_CAP" ]]
  printf 'DU_PASS phase=%s regular=%s apparent=%s\n' "$phase" "$regular" "$apparent"
}

component_gate() {
  local logs sidecars binary
  logs=$(find "$RUN_DIR/logs" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  binary=$(find "$RUN_DIR/bin" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  sidecars=$(find "$RUN_DIR" -maxdepth 1 -type f ! -name '*.tar.gz' -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  [[ "$logs" -le "$LOG_TOTAL_CAP" && "$binary" -le "$BINARY_CAP" && "$sidecars" -le "$SIDECAR_CAP" ]]
}

RUN_SERIAL=0
run_logged() {
  local deadline=$1 requested=$2 log=$3 remaining stdout_fifo stderr_fifo stdout_pid stderr_pid status stdout_status stderr_status
  shift 3
  remaining=$(remaining_until "$deadline")
  if [[ "$requested" -gt 0 && "$requested" -lt "$remaining" ]]; then remaining=$requested; fi
  RUN_SERIAL=$((RUN_SERIAL+1))
  stdout_fifo="$RUN_DIR/.phase_${RUN_SERIAL}.stdout"
  stderr_fifo="$RUN_DIR/.phase_${RUN_SERIAL}.stderr"
  mkfifo -- "$stdout_fifo" "$stderr_fifo"
  head -c "$LOG_FILE_CAP" <"$stdout_fifo" >"${log}.stdout" &
  stdout_pid=$!
  head -c "$LOG_FILE_CAP" <"$stderr_fifo" >"${log}.stderr" &
  stderr_pid=$!
  set +e
  timeout --signal=TERM --kill-after=15s "${remaining}s" nice -n 15 "$@" >"$stdout_fifo" 2>"$stderr_fifo"
  status=$?
  wait "$stdout_pid"
  stdout_status=$?
  wait "$stderr_pid"
  stderr_status=$?
  set -e
  rm -f -- "$stdout_fifo" "$stderr_fifo"
  [[ "$status" -eq 0 && "$stdout_status" -eq 0 && "$stderr_status" -eq 0 ]]
}

write_run_metadata() {
  local mode=$1 raw=$2 output_budget=$3
  {
    printf 'key\tvalue\nversion\t%s\nmode\t%s\nworkers\t%s\n' "$VERSION" "$mode" "$WORKERS"
    printf 'frozen_manifest_sha256\t%s\naudit_sha256\t%s\nresource_before_sha256\t%s\n' \
      "$FROZEN_ROOT" "$AUDIT_SHA" "$RESOURCE_BEFORE_SHA"
    printf 'process_before_sha256\t%s\nprocess_verify_sha256\t%s\nprocess_ack_sha256\t%s\nprocess_firewall\t%s\n' \
      "$PROCESS_BEFORE_SHA" "$PROCESS_VERIFY_SHA" "$PROCESS_ACK_SHA" "$PROCESS_FIREWALL"
    printf 'evidence_sha256\ta0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc\n'
    printf 'banks_sha256\tc908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6\n'
    printf 'corpus_sha256\t8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5\n'
    printf 'raw_output_budget\t%s\nanalyzer_output_budget\t%s\nrelation_payload_cap\t%s\n' \
      "$output_budget" "$((output_budget-OUTPUT_METADATA_ALLOWANCE))" "$RELATION_PAYLOAD_CAP"
  } >"$raw/RUN_METADATA.tsv"
}

hash_output_tree() {
  local raw=$1 mode=$2 expected actual
  expected=$'RUN_METADATA.tsv\naggregates.tsv\nblocks.tsv\ncases.tsv\nmetadata.tsv\npeeling.tsv\nrelations.tsv\nrows.tsv\nsummary.tsv\nwitness.tsv'
  actual=$(find "$raw" -maxdepth 1 -type f -printf '%f\n' | sort)
  [[ "$actual" == "$expected" ]]
  (
    cd -- "$raw"
    find . -maxdepth 1 -type f ! -name "$VERSION.outputs.sha256" -printf '%P\0' | \
      sort -z | xargs -0 sha256sum
  ) >"$raw/$VERSION.outputs.sha256"
  (
    cd -- "$raw"
    sha256sum -c "$VERSION.outputs.sha256"
  ) >"$RUN_DIR/logs/${mode}_output_hash_check.log"
  printf '%s  %s\n' "$(sha256sum "$raw/$VERSION.outputs.sha256" | awk '{print $1}')" \
    "$VERSION.outputs.sha256" >"$raw/$VERSION.outputs.manifest.sha256"
  (
    cd -- "$raw"
    sha256sum -c "$VERSION.outputs.manifest.sha256"
  ) >>"$RUN_DIR/logs/${mode}_output_hash_check.log"
}

compress_tree() {
  local raw=$1 archive=$2 deadline=$3 mode=$4 current raw_bytes largest allowance error_fifo error_pid remaining status_tar status_gzip
  local -a compression_status
  du_gate "${mode}_hashed"
  current=$(regular_bytes)
  raw_bytes=$(find "$raw" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  largest=$(find "$raw" -type f -printf '%s\n' | awk '$1>m {m=$1} END {print m+0}')
  allowance=$((raw_bytes/100+COMPRESSION_SLACK))
  [[ $((current+largest+allowance)) -le "$PACKET_OUTPUT_CAP" ]]
  [[ ! -e "$archive" && ! -e "${archive}.tmp" ]]
  remaining=$(remaining_until "$deadline")
  error_fifo="$RUN_DIR/.compression_${mode}.stderr"
  mkfifo -- "$error_fifo"
  head -c "$LOG_FILE_CAP" <"$error_fifo" >"$RUN_DIR/logs/${mode}_compression.stderr" &
  error_pid=$!
  set +e
  timeout --signal=TERM --kill-after=15s "${remaining}s" \
    nice -n 15 tar --format=ustar --sort=name --mtime='UTC 1970-01-01' --owner=0 --group=0 --numeric-owner \
      --remove-files -cf - -C "$RUN_DIR" "$(basename -- "$raw")" 2>"$error_fifo" |
    timeout --signal=TERM --kill-after=15s "${remaining}s" nice -n 15 gzip -n -6 >"${archive}.tmp" 2>"$error_fifo"
  compression_status=("${PIPESTATUS[@]}")
  status_tar=${compression_status[0]}
  status_gzip=${compression_status[1]}
  wait "$error_pid"
  set -e
  rm -f -- "$error_fifo"
  [[ "$status_tar" -eq 0 && "$status_gzip" -eq 0 ]]
  [[ ! -e "$raw" ]] || rmdir -- "$raw"
  mv -- "${archive}.tmp" "$archive"
  run_logged "$deadline" 120 "$RUN_DIR/logs/${mode}_gzip_test" gzip -t "$archive"
  run_logged "$deadline" 120 "$RUN_DIR/logs/${mode}_tar_list" tar -tzf "$archive"
  du_gate "${mode}_compressed"
  component_gate
}

du_gate initial
component_gate

run_logged "$ACTIVE_DEADLINE" 600 "$RUN_DIR/logs/compile" \
  g++ -O3 -DNDEBUG -std=c++17 -pthread f270_union.cpp -o "$RUN_DIR/bin/f270_union"
[[ $(stat -c %s "$RUN_DIR/bin/f270_union") -le "$BINARY_CAP" ]]
sha256sum "$RUN_DIR/bin/f270_union" >"$RUN_DIR/executable.sha256"
du_gate compile
component_gate

run_logged "$ACTIVE_DEADLINE" 300 "$RUN_DIR/logs/self_test" "$RUN_DIR/bin/f270_union" --self-test
grep -Fqx 'SELF_TEST_OK' "$RUN_DIR/logs/self_test.stdout"
du_gate self_test
component_gate

PREFLIGHT_RAW="$RUN_DIR/preflight.raw"
PREFLIGHT_TIME="$RUN_DIR/preflight.time.tsv"
readonly PREFLIGHT_RAW PREFLIGHT_TIME
run_logged "$ACTIVE_DEADLINE" 3600 "$RUN_DIR/logs/preflight" \
  /usr/bin/time -f '%e\t%M' -o "$PREFLIGHT_TIME" "$RUN_DIR/bin/f270_union" \
    --mode preflight --evidence "$EVIDENCE" --banks "$BANKS" --corpus "$CORPUS" \
    --out-dir "$PREFLIGHT_RAW" --workers "$WORKERS" --output-budget "$((PREFLIGHT_OUTPUT_BUDGET-OUTPUT_METADATA_ALLOWANCE))"
grep -Fq 'F270_OK mode=preflight cases=8' "$RUN_DIR/logs/preflight.stdout"
grep -Fqx $'status\tPREFLIGHT_ONLY' "$PREFLIGHT_RAW/summary.tsv"
read -r PREFLIGHT_SECONDS PREFLIGHT_RSS_KIB <"$PREFLIGHT_TIME"
write_run_metadata preflight "$PREFLIGHT_RAW" "$PREFLIGHT_OUTPUT_BUDGET"
hash_output_tree "$PREFLIGHT_RAW" preflight
PREFLIGHT_BYTES=$(find "$PREFLIGHT_RAW" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
readonly PREFLIGHT_SECONDS PREFLIGHT_RSS_KIB PREFLIGHT_BYTES
[[ "$PREFLIGHT_BYTES" -le "$PREFLIGHT_OUTPUT_BUDGET" ]]
compress_tree "$PREFLIGHT_RAW" "$RUN_DIR/F270-D03.preflight.tar.gz" "$ACTIVE_DEADLINE" preflight

PROJECTED_SECONDS=$(awk -v value="$PREFLIGHT_SECONDS" 'BEGIN {printf "%.6f",value*188/8*4}')
PROJECTED_RSS_KIB=$((PREFLIGHT_RSS_KIB*4))
PROJECTED_BYTES=$((PREFLIGHT_BYTES*188/8*4))
REMAINING_ACTIVE=$(remaining_until "$ACTIVE_DEADLINE")
readonly PROJECTED_SECONDS PROJECTED_RSS_KIB PROJECTED_BYTES REMAINING_ACTIVE
{
  printf 'metric\tobserved\tprojected_factor4\tgate\n'
  printf 'wall_seconds\t%s\t%s\t%s\n' "$PREFLIGHT_SECONDS" "$PROJECTED_SECONDS" "$REMAINING_ACTIVE"
  printf 'max_rss_kib\t%s\t%s\t%s\n' "$PREFLIGHT_RSS_KIB" "$PROJECTED_RSS_KIB" "$((MEMORY_MAX/1024))"
  printf 'output_bytes\t%s\t%s\t%s\n' "$PREFLIGHT_BYTES" "$PROJECTED_BYTES" "$TARGET_OUTPUT_BUDGET"
} >"$RUN_DIR/projection.tsv"
awk -v value="$PROJECTED_SECONDS" -v gate="$REMAINING_ACTIVE" 'BEGIN {exit !(value<=gate)}'
[[ "$PROJECTED_RSS_KIB" -le $((MEMORY_MAX/1024)) ]]
[[ "$PROJECTED_BYTES" -le "$TARGET_OUTPUT_BUDGET" ]]
du_gate projection
component_gate

CURRENT_LOAD=$(awk '{print $1}' /proc/loadavg)
CURRENT_MEM_KIB=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
CURRENT_DISK_KIB=$(df -Pk "$RUN_PARENT" | awk 'NR==2 {print $4}')
awk -v load="$CURRENT_LOAD" -v cpus="$CPUS" -v workers="$WORKERS" 'BEGIN {exit !(load+workers<=cpus)}'
[[ "$CURRENT_MEM_KIB" -ge 4194304 && $((CURRENT_DISK_KIB*1024)) -ge "$MIN_DISK_BYTES" ]]
printf 'load\t%s\nmem_available_kib\t%s\ndisk_available_kib\t%s\n' \
  "$CURRENT_LOAD" "$CURRENT_MEM_KIB" "$CURRENT_DISK_KIB" >"$RUN_DIR/target_admission.tsv"

TARGET_RAW="$RUN_DIR/target.raw"
TARGET_TIME="$RUN_DIR/target.time.tsv"
readonly TARGET_RAW TARGET_TIME
run_logged "$ACTIVE_DEADLINE" 0 "$RUN_DIR/logs/target" \
  /usr/bin/time -f '%e\t%M' -o "$TARGET_TIME" "$RUN_DIR/bin/f270_union" \
    --mode target --evidence "$EVIDENCE" --banks "$BANKS" --corpus "$CORPUS" \
    --out-dir "$TARGET_RAW" --workers "$WORKERS" --output-budget "$((TARGET_OUTPUT_BUDGET-OUTPUT_METADATA_ALLOWANCE))"
grep -Fq 'F270_OK mode=target cases=188' "$RUN_DIR/logs/target.stdout"
grep -Fqx $'interpretation\tFINITE_POSTHOC_HYPOTHESIS_GENERATION_NOT_A_THEOREM' "$TARGET_RAW/summary.tsv"
write_run_metadata target "$TARGET_RAW" "$TARGET_OUTPUT_BUDGET"
hash_output_tree "$TARGET_RAW" target
TARGET_BYTES=$(find "$TARGET_RAW" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
[[ "$TARGET_BYTES" -le "$TARGET_OUTPUT_BUDGET" ]]
compress_tree "$TARGET_RAW" "$RUN_DIR/F270-D03.target.tar.gz" "$ARCHIVE_DEADLINE" target

{
  date -u '+utc=%Y-%m-%dT%H:%M:%SZ'
  uptime
  free -h
  df -h "$RUN_PARENT"
  printf 'cgroup_memory_current\t%s\n' "$(<"$CGROUP/memory.current")"
  printf 'cgroup_memory_peak\t%s\n' "$(<"$CGROUP/memory.peak")"
  cat "$CGROUP/memory.events"
} | head -c "$LOG_FILE_CAP" >"$RUN_DIR/resource_after.txt"
[[ "$(awk '$1=="oom" {print $2}' "$CGROUP/memory.events")" == 0 ]]
[[ "$(awk '$1=="oom_kill" {print $2}' "$CGROUP/memory.events")" == 0 ]]
[[ "$(<"$CGROUP/memory.peak")" -le "$MEMORY_MAX" ]]

PREFLIGHT_ARCHIVE_SHA=$(sha256sum "$RUN_DIR/F270-D03.preflight.tar.gz" | awk '{print $1}')
TARGET_ARCHIVE_SHA=$(sha256sum "$RUN_DIR/F270-D03.target.tar.gz" | awk '{print $1}')
EXECUTABLE_SHA=$(sha256sum "$RUN_DIR/bin/f270_union" | awk '{print $1}')
{
  printf 'key\tvalue\nversion\t%s\nfrozen_manifest_sha256\t%s\naudit_sha256\t%s\n' "$VERSION" "$FROZEN_ROOT" "$AUDIT_SHA"
  printf 'resource_before_sha256\t%s\nprocess_before_sha256\t%s\nprocess_verify_sha256\t%s\nprocess_ack_sha256\t%s\nprocess_firewall\t%s\n' \
    "$RESOURCE_BEFORE_SHA" "$PROCESS_BEFORE_SHA" "$PROCESS_VERIFY_SHA" "$PROCESS_ACK_SHA" "$PROCESS_FIREWALL"
  printf 'executable_sha256\t%s\n' "$EXECUTABLE_SHA"
  printf 'preflight_archive_sha256\t%s\npreflight_archive_bytes\t%s\n' \
    "$PREFLIGHT_ARCHIVE_SHA" "$(stat -c %s "$RUN_DIR/F270-D03.preflight.tar.gz")"
  printf 'target_archive_sha256\t%s\ntarget_archive_bytes\t%s\n' \
    "$TARGET_ARCHIVE_SHA" "$(stat -c %s "$RUN_DIR/F270-D03.target.tar.gz")"
  printf 'target_raw_bytes\t%s\nhard_deadline_monotonic_seconds\t%s\n' "$TARGET_BYTES" "$HARD_DEADLINE"
} >"$RUN_DIR/F270-D03.run_manifest.tsv"
du_gate before_final_hashes
component_gate
remaining_until "$HARD_DEADLINE" >/dev/null
(
  cd -- "$RUN_DIR"
  find . -type f ! -name 'F270-D03.final.sha256' -printf '%P\0' | sort -z | \
    xargs -0 sha256sum
) >"$RUN_DIR/F270-D03.final.sha256"
du_gate final
component_gate
remaining_until "$HARD_DEADLINE" >/dev/null
FINAL_MANIFEST_SHA=$(sha256sum "$RUN_DIR/F270-D03.final.sha256" | awk '{print $1}')
echo "F270_D03_COMPLETE run_dir=$RUN_DIR frozen_root=$FROZEN_ROOT final_manifest_sha256=$FINAL_MANIFEST_SHA"
