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
VERSION=F270-D02
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
readonly SOURCE_DIR EVIDENCE BANKS CORPUS RUN_DIR WORKERS APPROVED_FROZEN_ROOT VERSION
readonly MEMORY_MAX RLIMIT_AS_KIB PACKET_OUTPUT_CAP PREFLIGHT_OUTPUT_BUDGET TARGET_OUTPUT_BUDGET OUTPUT_METADATA_ALLOWANCE
readonly RELATION_PAYLOAD_CAP LOG_FILE_CAP LOG_TOTAL_CAP SIDECAR_CAP BINARY_CAP COMPRESSION_SLACK
readonly MIN_DISK_BYTES PACKET_SECONDS CLOSURE_SECONDS MANIFEST_SECONDS

[[ "$WORKERS" =~ ^[1-8]$ ]]
[[ "$APPROVED_FROZEN_ROOT" =~ ^[0-9a-f]{64}$ ]]
case "$RUN_DIR" in /*) ;; *) echo "run directory must be absolute" >&2; exit 64;; esac
[[ "$RUN_DIR" != / && "$RUN_DIR" != /root && "$RUN_DIR" != /tmp && "$RUN_DIR" != "$SOURCE_DIR" ]]
[[ ! -e "$RUN_DIR" ]] || { echo "run directory exists: $RUN_DIR" >&2; exit 73; }
for input in "$EVIDENCE" "$BANKS" "$CORPUS"; do
  [[ -f "$input" ]] || { echo "missing input: $input" >&2; exit 66; }
done
for command in awk basename cat date df dirname du find flock free g++ grep gzip head mkdir mkfifo mv nice nproc \
  pkill ps readlink rm rmdir sed sha256sum sleep sort stat tar timeout uname wc xargs; do
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
CGROUP="$CGROUP_PARENT/f270_d02_$$"
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
ANCESTOR_PIDS=",$$,"
ancestor=$PPID
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  [[ "$ancestor" =~ ^[0-9]+$ && "$ancestor" -gt 1 ]] || break
  ANCESTOR_PIDS+="$ancestor,"
  ancestor=$(ps -o ppid= -p "$ancestor" | awk '{$1=$1;print}')
done
readonly ANCESTOR_PIDS
if ps -eo pid=,ppid=,ni=,pcpu=,pmem=,rss=,etime=,args= --sort=pid | \
  awk -v ancestors="$ANCESTOR_PIDS" -v watchdog="$WATCHDOG_PID" -v cap="$LOG_FILE_CAP" '
    {line=$0 ORS; bytes+=length(line); if(bytes<=cap) printf "%s",line; else overflow=1}
    index(ancestors,"," $1 ",")==0 && $1!=watchdog &&
    ($0 ~ /[[:space:]]--mode[[:space:]]+(target|discovery|heldout|complete|production)([[:space:]]|$)/ ||
     $0 ~ /[[:space:]]--(target|discovery|heldout|complete|production)([[:space:]]|$)/ ||
     $0 ~ /[Ff][0-9][0-9][0-9][-_].*(remote_run|search|union|multirow|lift|factor|production)/) {overlap=1}
    END {exit overlap?2:(overflow?3:0)}
  ' >"$RUN_DIR/process_before.tsv"; then
  PROCESS_FIREWALL=PASS
else
  echo "RESOURCE_STOP reason=production_process_overlap_or_snapshot_cap" >&2
  exit 76
fi
RESOURCE_BEFORE_SHA=$(sha256sum "$RUN_DIR/resource_before.txt" | awk '{print $1}')
PROCESS_BEFORE_SHA=$(sha256sum "$RUN_DIR/process_before.tsv" | awk '{print $1}')
readonly RESOURCE_BEFORE_SHA PROCESS_BEFORE_SHA PROCESS_FIREWALL
printf 'firewall\t%s\nprocess_snapshot_sha256\t%s\nexcluded_ancestor_pids\t%s\nexcluded_watchdog_pid\t%s\nlock_path\t%s\n' \
  "$PROCESS_FIREWALL" "$PROCESS_BEFORE_SHA" "$ANCESTOR_PIDS" "$WATCHDOG_PID" "$LOCK_PATH" >"$RUN_DIR/process_ack.tsv"
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
    printf 'process_before_sha256\t%s\nprocess_ack_sha256\t%s\nprocess_firewall\t%s\n' \
      "$PROCESS_BEFORE_SHA" "$PROCESS_ACK_SHA" "$PROCESS_FIREWALL"
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
compress_tree "$PREFLIGHT_RAW" "$RUN_DIR/F270-D02.preflight.tar.gz" "$ACTIVE_DEADLINE" preflight

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
compress_tree "$TARGET_RAW" "$RUN_DIR/F270-D02.target.tar.gz" "$ARCHIVE_DEADLINE" target

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

PREFLIGHT_ARCHIVE_SHA=$(sha256sum "$RUN_DIR/F270-D02.preflight.tar.gz" | awk '{print $1}')
TARGET_ARCHIVE_SHA=$(sha256sum "$RUN_DIR/F270-D02.target.tar.gz" | awk '{print $1}')
EXECUTABLE_SHA=$(sha256sum "$RUN_DIR/bin/f270_union" | awk '{print $1}')
{
  printf 'key\tvalue\nversion\t%s\nfrozen_manifest_sha256\t%s\naudit_sha256\t%s\n' "$VERSION" "$FROZEN_ROOT" "$AUDIT_SHA"
  printf 'resource_before_sha256\t%s\nprocess_before_sha256\t%s\nprocess_ack_sha256\t%s\nprocess_firewall\t%s\n' \
    "$RESOURCE_BEFORE_SHA" "$PROCESS_BEFORE_SHA" "$PROCESS_ACK_SHA" "$PROCESS_FIREWALL"
  printf 'executable_sha256\t%s\n' "$EXECUTABLE_SHA"
  printf 'preflight_archive_sha256\t%s\npreflight_archive_bytes\t%s\n' \
    "$PREFLIGHT_ARCHIVE_SHA" "$(stat -c %s "$RUN_DIR/F270-D02.preflight.tar.gz")"
  printf 'target_archive_sha256\t%s\ntarget_archive_bytes\t%s\n' \
    "$TARGET_ARCHIVE_SHA" "$(stat -c %s "$RUN_DIR/F270-D02.target.tar.gz")"
  printf 'target_raw_bytes\t%s\nhard_deadline_monotonic_seconds\t%s\n' "$TARGET_BYTES" "$HARD_DEADLINE"
} >"$RUN_DIR/F270-D02.run_manifest.tsv"
du_gate before_final_hashes
component_gate
remaining_until "$HARD_DEADLINE" >/dev/null
(
  cd -- "$RUN_DIR"
  find . -type f ! -name 'F270-D02.final.sha256' -printf '%P\0' | sort -z | \
    xargs -0 sha256sum
) >"$RUN_DIR/F270-D02.final.sha256"
du_gate final
component_gate
remaining_until "$HARD_DEADLINE" >/dev/null
FINAL_MANIFEST_SHA=$(sha256sum "$RUN_DIR/F270-D02.final.sha256" | awk '{print $1}')
echo "F270_D02_COMPLETE run_dir=$RUN_DIR frozen_root=$FROZEN_ROOT final_manifest_sha256=$FINAL_MANIFEST_SHA"
