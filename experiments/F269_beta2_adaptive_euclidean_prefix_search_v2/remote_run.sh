#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'
export LC_ALL=C TMPDIR=/tmp
unset GZIP POSIXLY_CORRECT
readonly LC_ALL TMPDIR

if [[ $# -ne 2 || ( $2 != preflight && $2 != complete ) ]]; then
  echo 'usage: remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY preflight|complete' >&2
  exit 64
fi

TARGET=$1
MODE=$2
SOURCE_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
VERSION=F269-D02
MEMORY_MAX=3758096384
AGGREGATE_CAP=536870912
MIN_DISK_BYTES=5368709120
readonly TARGET MODE SOURCE_DIR VERSION MEMORY_MAX AGGREGATE_CAP MIN_DISK_BYTES

case "$TARGET" in /*) ;; *) echo 'target must be absolute' >&2; exit 64;; esac
[[ "$TARGET" != / && "$TARGET" != /root && "$TARGET" != /tmp ]]
[[ ! -e "$TARGET" ]] || { echo "refuse existing evidence: $TARGET" >&2; exit 73; }

EXTERNAL_COMMANDS=(awk bash date df dirname du env find g++ grep gzip mkdir mktemp nice nproc ps rm rmdir sed sha256sum sleep sort stat timeout)
for external_command in "${EXTERNAL_COMMANDS[@]}"; do
  command -v "$external_command" >/dev/null
done
for shell_builtin in cd command echo exit export kill local printf pwd read readonly return set shift trap true type ulimit unset wait; do
  [[ $(type -t "$shell_builtin") == builtin ]]
done
[[ -x /usr/bin/env && -x /usr/bin/time ]]

for gnu_command in date df dirname du env find g++ grep gzip mkdir mktemp nice nproc ps rm rmdir sed sha256sum sleep sort stat timeout; do
  "$gnu_command" --version >/dev/null 2>&1
done
/usr/bin/time --version >/dev/null 2>&1
/usr/bin/env --version >/dev/null 2>&1
bash --version >/dev/null 2>&1
[[ ${BASH_VERSINFO[0]} -ge 4 ]]
awk -W version >/dev/null 2>&1
grep -Fq -- '--utc' <<<"$(date --help)"
grep -Fq -- '--portability' <<<"$(df --help)"
grep -Fq -- '--human-readable' <<<"$(df --help)"
grep -Fq -- '--bytes' <<<"$(du --help)"
grep -Fq -- '--summarize' <<<"$(du --help)"
grep -Fq -- '--apparent-size' <<<"$(du --help)"
grep -Fq -- '-maxdepth' <<<"$(find --help)"
grep -Fq -- '-printf' <<<"$(find --help)"
grep -Fq -- '--fixed-strings' <<<"$(grep --help)"
grep -Fq -- '--line-regexp' <<<"$(grep --help)"
grep -Fq -- '--quiet' <<<"$(grep --help)"
grep -Fq -- '--stdout' <<<"$(gzip --help)"
grep -Fq -- '--no-name' <<<"$(gzip --help)"
grep -Fq -- '--mode' <<<"$(mkdir --help)"
grep -Fq -- '--directory' <<<"$(mktemp --help)"
grep -Fq -- '--adjustment' <<<"$(nice --help)"
grep -Fq -- '--format' <<<"$(ps --help all)"
grep -Fq -- '--width' <<<"$(ps --help output)"
grep -Fq -- '--sort' <<<"$(ps --help all)"
grep -Fq -- '--force' <<<"$(rm --help)"
grep -Fq -- '--quiet' <<<"$(sed --help)"
grep -Fq -- '--check' <<<"$(sha256sum --help)"
grep -Fq -- '--format' <<<"$(stat --help)"
grep -Fq -- '--kill-after' <<<"$(timeout --help)"
grep -Fq -- '--verbose' <<<"$(/usr/bin/time --help)"
g++ -std=c++17 -O3 -DNDEBUG -pthread -o /dev/null --version >/dev/null 2>&1
gzip -n -6 -c --help >/dev/null 2>&1

cd -- "$SOURCE_DIR"
sha256sum --check FROZEN.sha256 >/dev/null
FROZEN_MANIFEST_SHA=$(sha256sum FROZEN.sha256 | awk '{print $1}')
readonly FROZEN_MANIFEST_SHA
[[ -f HOSTILE_PRERUN_AUDIT.md ]]
grep -Fqx '# Verdict: PASS' HOSTILE_PRERUN_AUDIT.md
grep -Fqx "frozen_manifest_sha256: $FROZEN_MANIFEST_SHA" HOSTILE_PRERUN_AUDIT.md

monotonic_ns() {
  awk '{split($1,a,"."); f=a[2] "000000000"; print a[1] substr(f,1,9)}' /proc/uptime
}

refuse_overlap() {
  local pid ppid arguments lowered
  while IFS=' ' read -r pid ppid arguments; do
    [[ $pid == $$ || $pid == $BASHPID ]] && continue
    lowered=${arguments,,}
    if [[ $lowered == *f265* ]]; then
      echo "RESOURCE_STOP reason=F265_active pid=$pid args=$arguments" >&2
      exit 73
    fi
  done < <(ps -ww -eo pid=,ppid=,args=)
}

refuse_overlap
START_NS=$(monotonic_ns)
HARD_DEADLINE=$((SECONDS+14400))
SOURCE_DEADLINE=$((HARD_DEADLINE-30))
readonly START_NS HARD_DEADLINE SOURCE_DEADLINE

CPUS=$(nproc)
LOAD=$(awk '{print $1}' /proc/loadavg)
MEM_AVAILABLE_KIB=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
DISK_AVAILABLE_KIB=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
TMP_AVAILABLE_KIB=$(df -Pk /tmp | awk 'NR==2 {print $4}')
awk -v load="$LOAD" -v cpus="$CPUS" 'BEGIN {exit !(load<=cpus)}' || {
  echo "RESOURCE_STOP reason=load load=$LOAD cpus=$CPUS" >&2; exit 75;
}
[[ $((DISK_AVAILABLE_KIB*1024)) -ge $MIN_DISK_BYTES ]] || {
  echo "RESOURCE_STOP reason=disk available_kib=$DISK_AVAILABLE_KIB" >&2; exit 75;
}
[[ $((TMP_AVAILABLE_KIB*1024)) -ge $MIN_DISK_BYTES ]] || {
  echo "RESOURCE_STOP reason=bootstrap_disk available_kib=$TMP_AVAILABLE_KIB" >&2; exit 75;
}

IDLE_CPUS=$(awk -v cpus="$CPUS" -v load="$LOAD" 'BEGIN{x=int(cpus-load); print x<1?1:x}')
if [[ $IDLE_CPUS -ge 8 && $MEM_AVAILABLE_KIB -ge 8388608 ]]; then W=8
elif [[ $IDLE_CPUS -ge 4 && $MEM_AVAILABLE_KIB -ge 6291456 ]]; then W=4
elif [[ $IDLE_CPUS -ge 2 && $MEM_AVAILABLE_KIB -ge 5242880 ]]; then W=2
else W=1
fi
readonly CPUS LOAD MEM_AVAILABLE_KIB DISK_AVAILABLE_KIB TMP_AVAILABLE_KIB IDLE_CPUS W

CGROUP_PARENT_REL=$(awk -F: '$1=="0" {print $3}' /proc/$$/cgroup)
CGROUP_PARENT="/sys/fs/cgroup${CGROUP_PARENT_REL}"
CGROUP="$CGROUP_PARENT/f269_d02_$$"
readonly CGROUP_PARENT_REL CGROUP_PARENT CGROUP
[[ -f /sys/fs/cgroup/cgroup.controllers && -w "$CGROUP_PARENT/cgroup.procs" ]]
mkdir -- "$CGROUP"

cgroup_setup_fail() {
  local reason=$1
  rmdir -- "$CGROUP" 2>/dev/null || true
  echo "RESOURCE_STOP reason=$reason" >&2
  exit 75
}

[[ -w "$CGROUP/memory.max" && -w "$CGROUP/memory.swap.max" &&
   -w "$CGROUP/memory.peak" &&
   -w "$CGROUP/cgroup.procs" && -w "$CGROUP/cgroup.kill" ]] || \
  cgroup_setup_fail cgroup_v2_files
printf '%s\n' "$MEMORY_MAX" >"$CGROUP/memory.max" || cgroup_setup_fail memory_max_write
printf '0\n' >"$CGROUP/memory.swap.max" || cgroup_setup_fail memory_swap_write
[[ $(<"$CGROUP/memory.max") == "$MEMORY_MAX" && $(<"$CGROUP/memory.swap.max") == 0 ]] || \
  cgroup_setup_fail memory_limit_readback
[[ $(stat -c %n "$CGROUP/cgroup.kill") == "$CGROUP/cgroup.kill" ]] || \
  cgroup_setup_fail cgroup_kill_identity

(
  remaining=$((HARD_DEADLINE-SECONDS))
  [[ $remaining -gt 0 ]] && sleep "$remaining"
  printf '1\n' >"$CGROUP/cgroup.kill"
  sleep 1
  rmdir -- "$CGROUP" 2>/dev/null || true
) &
WATCHDOG_PID=$!
readonly WATCHDOG_PID
if ! printf '%s\n' $$ >"$CGROUP/cgroup.procs"; then
  kill "$WATCHDOG_PID" 2>/dev/null || true
  wait "$WATCHDOG_PID" 2>/dev/null || true
  cgroup_setup_fail cgroup_join
fi

BOOTSTRAP_DIR=
BOOTSTRAP_BIN=
BOOTSTRAP_LOG=
LEDGER_STATE="$TARGET/.F269-D02.ledger.state"
BIN="$TARGET/bin/f269"
readonly LEDGER_STATE BIN
SUCCESS=0
LEDGER_READY=0
EVIDENCE_FROZEN=0
PHASE=bootstrap_compile

cleanup() {
  local cleanup_status=$?
  trap - ERR INT TERM EXIT
  set +e
  kill "$WATCHDOG_PID" 2>/dev/null
  wait "$WATCHDOG_PID" 2>/dev/null
  printf '%s\n' $$ >"$CGROUP_PARENT/cgroup.procs" 2>/dev/null
  rmdir -- "$CGROUP" 2>/dev/null
  if [[ -n $BOOTSTRAP_DIR ]]; then
    rm -f -- "$BOOTSTRAP_BIN" "$BOOTSTRAP_LOG"
    rmdir -- "$BOOTSTRAP_DIR" 2>/dev/null
  fi
  exit "$cleanup_status"
}
trap cleanup EXIT

BOOTSTRAP_DIR=$(mktemp -d /tmp/f269-d02-bootstrap.XXXXXX)
BOOTSTRAP_BIN="$BOOTSTRAP_DIR/f269"
BOOTSTRAP_LOG="$BOOTSTRAP_DIR/compile.log"
readonly BOOTSTRAP_DIR BOOTSTRAP_BIN BOOTSTRAP_LOG

on_error() {
  local status=$1 line=$2 report elapsed writer
  trap - ERR
  set +e
  if [[ $SUCCESS -eq 0 && $LEDGER_READY -eq 1 && $EVIDENCE_FROZEN -eq 0 ]]; then
    writer=$BIN
    [[ -x $writer ]] || writer=$BOOTSTRAP_BIN
    if [[ -x $writer ]]; then
      elapsed=$(( $(monotonic_ns)-START_NS ))
      report=$("$writer" --ledger-check "$TARGET" "$LEDGER_STATE" 2>&1)
      {
        printf 'version\t%s\nstatus\tFAIL\nphase\t%s\nexit_status\t%s\nline\t%s\nelapsed_ns\t%s\n' \
          "$VERSION" "$PHASE" "$status" "$line" "$elapsed"
        printf '%s\n' "$report"
      } | "$writer" --failure-manifest "$TARGET" "$LEDGER_STATE" \
        "$TARGET/F269-D02.failure.tsv"
    fi
  fi
  exit "$status"
}
trap 'on_error $? $LINENO' ERR

on_signal() {
  local status=$1 line=$2
  if [[ $LEDGER_READY -eq 1 ]]; then on_error "$status" "$line"; fi
  exit "$status"
}
trap 'on_signal 130 $LINENO' INT
trap 'on_signal 143 $LINENO' TERM

ulimit -Sv 4194304
ulimit -Hv 4194304
ulimit -Sf 1048576
ulimit -Hf 1048576

remaining=$((SOURCE_DEADLINE-SECONDS))
[[ $remaining -gt 0 ]]
refuse_overlap
timeout --kill-after=5s "${remaining}s" nice -n 15 g++ -std=c++17 -O3 -DNDEBUG -pthread \
  f269.cpp -o "$BOOTSTRAP_BIN" >"$BOOTSTRAP_LOG" 2>&1

PHASE=bootstrap_import
mkdir -m 0755 -- "$TARGET" "$TARGET/bin" "$TARGET/logs" "$TARGET/preflight"
"$BOOTSTRAP_BIN" --ledger-init "$TARGET" "$LEDGER_STATE"
export F269_LEDGER_STATE="$LEDGER_STATE"
LEDGER_READY=1
"$BOOTSTRAP_BIN" --checked-copy "$TARGET" "$LEDGER_STATE" "$BOOTSTRAP_LOG" \
  "$TARGET/logs/compile.log"
"$BOOTSTRAP_BIN" --checked-copy "$TARGET" "$LEDGER_STATE" "$BOOTSTRAP_BIN" "$BIN"
rm -f -- "$BOOTSTRAP_BIN" "$BOOTSTRAP_LOG"
rmdir -- "$BOOTSTRAP_DIR"

checked_text() {
  local mode=$1 path=$2
  "$BIN" --ledger-write "$TARGET" "$LEDGER_STATE" "$mode" "$path"
}

log_line() {
  printf '%s\n' "$1" | checked_text append "$TARGET/logs/runner.log"
}

log_line "version=$VERSION mode=$MODE frozen_manifest_sha256=$FROZEN_MANIFEST_SHA"
log_line "workers=$W cgroup_kill_writable=1"
printf 'workers\t%s\n' "$W" | checked_text replace "$TARGET/F269-D02.workers.tsv"

remaining_seconds() {
  local remaining_now=$((HARD_DEADLINE-SECONDS))
  [[ $remaining_now -gt 0 ]] || { echo 'RESOURCE_STOP reason=packet_deadline' >&2; return 124; }
  printf '%s\n' "$remaining_now"
}

source_deadline_seconds() {
  local remaining_now=$((SOURCE_DEADLINE-SECONDS))
  [[ $remaining_now -gt 0 ]] || { echo 'RESOURCE_STOP reason=source_deadline' >&2; return 124; }
  printf '%s\n' "$remaining_now"
}

run_plain() {
  local requested=$1 out_mode=$2 out_path=$3 err_mode=$4 err_path=$5 remaining_now source_remaining
  shift 5
  refuse_overlap
  remaining_now=$(remaining_seconds)
  source_remaining=$(source_deadline_seconds)
  [[ $source_remaining -lt $remaining_now ]] && remaining_now=$source_remaining
  if [[ $requested -gt 0 && $requested -lt $remaining_now ]]; then remaining_now=$requested; fi
  "$BIN" --checked-exec "$TARGET" "$LEDGER_STATE" "$out_mode" "$out_path" \
    "$err_mode" "$err_path" -- timeout --kill-after=5s "${remaining_now}s" \
    nice -n 15 "$@"
}

run_source() {
  local requested=$1 out_mode=$2 out_path=$3 err_mode=$4 err_path=$5
  local remaining_now source_remaining
  shift 5
  refuse_overlap
  remaining_now=$(remaining_seconds)
  source_remaining=$(source_deadline_seconds)
  [[ $source_remaining -lt $remaining_now ]] && remaining_now=$source_remaining
  if [[ $requested -gt 0 && $requested -lt $remaining_now ]]; then remaining_now=$requested; fi
  F269_DEADLINE_SECONDS=$source_remaining "$BIN" --checked-exec "$TARGET" "$LEDGER_STATE" \
    "$out_mode" "$out_path" "$err_mode" "$err_path" -- timeout --kill-after=5s \
    "${remaining_now}s" nice -n 15 "$@"
}

record_resources() {
  local path=$1
  {
    date -u +%Y-%m-%dT%H:%M:%SZ
    printf 'cpus\t%s\nload\t%s\nmem_available_kib\t%s\ndisk_available_kib\t%s\nbootstrap_disk_available_kib\t%s\nworkers\t%s\n' \
      "$CPUS" "$LOAD" "$MEM_AVAILABLE_KIB" "$DISK_AVAILABLE_KIB" "$TMP_AVAILABLE_KIB" "$W"
    awk '/MemTotal:|MemAvailable:/ {print}' /proc/meminfo
    df -h "$(dirname -- "$TARGET")"
    ps -ww -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,32p'
  } | checked_text replace "$path"
}

du_gate() {
  local phase=$1 report apparent
  report=$("$BIN" --ledger-check "$TARGET" "$LEDGER_STATE")
  LEDGER_BYTES=$(awk -F '\t' '$1=="evidence_regular_bytes" {print $2}' <<<"$report")
  apparent=$(du -sb --apparent-size -- "$TARGET" | awk '{print $1}')
  [[ $LEDGER_BYTES -le $AGGREGATE_CAP && $apparent -le $AGGREGATE_CAP ]]
  LAST_DU_BYTES=$apparent
  export LEDGER_BYTES LAST_DU_BYTES
  log_line "DU_PASS phase=$phase regular=$LEDGER_BYTES apparent=$apparent"
}

PHASE=exact_self_test
record_resources "$TARGET/logs/resource_before.tsv"
du_gate resource_before
run_source 300 replace "$TARGET/logs/self_test.log" append "$TARGET/logs/self_test.log" \
  "$BIN" --self-test "$SOURCE_DIR/F269-D02.baselines.tsv"
grep -Fq 'SELF_TEST_PASS' "$TARGET/logs/self_test.log"
du_gate self_test

metric() {
  local key=$1 path=$2
  awk -F '\t' -v key="$key" '$1==key {print $2}' "$path"
}

PHASE=grammar_preflight
GRAMMAR_SHA=
CONTROL_MASKS=
CONTROL_MASKS_SHA=
G_NS=()
ROOT_ATTEMPT_MASK=$(printf '%110s' '' | sed 's/ /f/g')0f
for i in 1 2 3 4 5 6 7; do
  path="$TARGET/preflight/grammar_${i}.tsv"
  run_source 600 replace "$path" replace "$TARGET/logs/grammar_${i}.log" \
    "$BIN" --grammar-once
  G_NS[$i]=$(metric nanoseconds "$path")
  sha=$(metric grammar_sha256 "$path")
  masks=$(metric control_case_masks "$path")
  masks_sha=$(metric control_case_masks_sha256 "$path")
  [[ $(metric root_attempt_mask "$path") == "$ROOT_ATTEMPT_MASK" ]]
  [[ $(metric control_case_mask_count "$path") == $(metric final_syntax_count "$path") ]]
  [[ $(awk -F, '{print NF}' <<<"$masks") == $(metric final_syntax_count "$path") ]]
  awk -F, '{for(i=1;i<=NF;i++)if(length($i)!=8||$i~/[^0-9a-f]/)exit 1}' <<<"$masks"
  [[ $(printf '%s' "$masks" | sha256sum | awk '{print $1}') == "$masks_sha" ]]
  [[ -z $GRAMMAR_SHA || $sha == "$GRAMMAR_SHA" ]]
  [[ -z $CONTROL_MASKS || $masks == "$CONTROL_MASKS" ]]
  [[ -z $CONTROL_MASKS_SHA || $masks_sha == "$CONTROL_MASKS_SHA" ]]
  GRAMMAR_SHA=$sha
  CONTROL_MASKS=$masks
  CONTROL_MASKS_SHA=$masks_sha
  [[ $(metric root_retained "$path") == 444 && $(metric tuple_attempts "$path") == 5120 ]]
  retained=$(metric tuple_retained "$path")
  partition=$((retained+$(metric type_reject "$path")+$(metric provenance_reject "$path")+$(metric duplicate_reject "$path")+$(metric all_chamber_control_reject "$path")))
  [[ $partition -eq 5120 ]]
  [[ $((444+retained)) -eq $(metric final_syntax_count "$path") ]]
  du_gate "grammar_$i"
done
readonly GRAMMAR_SHA CONTROL_MASKS CONTROL_MASKS_SHA ROOT_ATTEMPT_MASK

PHASE=maximum_work
printf '0\n' >"$CGROUP/memory.peak"
MAX_VMHWM=0
MAX_TIME_RSS=0
R_NS=()
for i in 1 2 3 4; do
  round=$((i-1))
  path="$TARGET/preflight/round_${i}.tsv"
  time_path="$TARGET/preflight/round_${i}.time.txt"
  source_remaining=$(source_deadline_seconds)
  remaining_now=$(remaining_seconds)
  [[ $source_remaining -lt $remaining_now ]] && remaining_now=$source_remaining
  refuse_overlap
  F269_DEADLINE_SECONDS=$source_remaining "$BIN" --checked-exec "$TARGET" "$LEDGER_STATE" \
    replace "$path" replace "$time_path" -- timeout --kill-after=5s "${remaining_now}s" \
    /usr/bin/time -v nice -n 15 "$BIN" --max-work-round "$W" "$round"
  R_NS[$i]=$(metric nanoseconds "$path")
  vm=$(metric vmhwm_bytes "$path")
  rss_kib=$(awk -F ': ' '/Maximum resident set size \(kbytes\)/ {print $2}' "$time_path")
  rss=$((rss_kib*1024))
  [[ $vm -gt $MAX_VMHWM ]] && MAX_VMHWM=$vm
  [[ $rss -gt $MAX_TIME_RSS ]] && MAX_TIME_RSS=$rss
  [[ $(metric tail_divisions "$path") -eq $((W*14*9*8)) ]]
  [[ $(metric value_checks "$path") -eq $((W*2*5564*8)) ]]
  [[ $(metric selector_updates "$path") -eq $((W*11128*8)) ]]
  [[ $(metric tickets "$path") -eq $((W*1024*4*8)) ]]
  du_gate "round_$i"
done
CGROUP_PEAK=$(<"$CGROUP/memory.peak")
readonly MAX_VMHWM MAX_TIME_RSS CGROUP_PEAK

PHASE=serialization_preflight
SERIALIZATION="$TARGET/preflight/serialization.image"
S_NS=()
for i in 1 2 3 4 5 6 7; do
  start=$(monotonic_ns)
  path="$TARGET/preflight/serialization_${i}.tsv"
  run_source 1200 replace "$path" replace "$TARGET/logs/serialization_${i}.log" \
    "$BIN" --serialization-write "$TARGET" "$SERIALIZATION"
  [[ $(stat -c %s "$SERIALIZATION") -eq 277979136 ]]
  actual_sha=$(sha256sum "$SERIALIZATION" | awk '{print $1}')
  [[ $actual_sha == $(metric serialization_sha256 "$path") ]]
  du_gate "serialization_${i}_closed"
  run_source 120 append "$path" append "$TARGET/logs/serialization_${i}.log" \
    "$BIN" --checked-truncate "$TARGET" "$SERIALIZATION"
  du_gate "serialization_${i}_truncated"
  end=$(monotonic_ns)
  S_NS[$i]=$((end-start))
done

PHASE=compression_preflight
run_plain 30 replace "$TARGET/preflight/compressor.tsv" replace "$TARGET/logs/compressor.log" gzip --version
STREAM="$TARGET/preflight/splitmix.stream"
COMPRESSED="$TARGET/preflight/splitmix.stream.gz"
Z_NS=()
for i in 1 2 3 4 5 6 7; do
  start=$(monotonic_ns)
  path="$TARGET/preflight/compression_${i}.tsv"
  run_source 600 replace "$path" replace "$TARGET/logs/compression_${i}.log" \
    "$BIN" --splitmix-stream-write "$TARGET" "$STREAM"
  [[ $(stat -c %s "$STREAM") -eq 67108864 ]]
  du_gate "compression_${i}_source_closed"
  run_plain 600 replace "$COMPRESSED" append "$TARGET/logs/compression_${i}.log" \
    gzip -n -6 -c "$STREAM"
  run_plain 120 append "$path" append "$TARGET/logs/compression_${i}.log" \
    sha256sum "$STREAM" "$COMPRESSED"
  du_gate "compression_${i}_closed"
  run_source 120 append "$path" append "$TARGET/logs/compression_${i}.log" \
    "$BIN" --checked-truncate "$TARGET" "$COMPRESSED"
  run_source 120 append "$path" append "$TARGET/logs/compression_${i}.log" \
    "$BIN" --checked-truncate "$TARGET" "$STREAM"
  du_gate "compression_${i}_truncated"
  end=$(monotonic_ns)
  Z_NS[$i]=$((end-start))
done

PHASE=readiness_gate
record_resources "$TARGET/logs/resource_after.tsv"
du_gate resource_after
FREE_DISK_BYTES=$(( $(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}') * 1024 ))
GATE_INPUT="$TARGET/preflight/gate_input.tsv"
{
  printf 'workers\t%s\n' "$W"
  for i in 1 2 3 4 5 6 7; do printf 'G%s_ns\t%s\n' "$i" "${G_NS[$i]}"; done
  for i in 1 2 3 4; do printf 'R%s_ns\t%s\n' "$i" "${R_NS[$i]}"; done
  for i in 1 2 3 4 5 6 7; do printf 'S%s_ns\t%s\n' "$i" "${S_NS[$i]}"; done
  for i in 1 2 3 4 5 6 7; do printf 'Z%s_ns\t%s\n' "$i" "${Z_NS[$i]}"; done
  printf 'cgroup_memory_peak_bytes\t%s\nprocess_vmhwm_bytes\t%s\ntime_maxrss_bytes\t%s\n' \
    "$CGROUP_PEAK" "$MAX_VMHWM" "$MAX_TIME_RSS"
  printf 'registered_serialization_bytes\t277979136\nevidence_regular_bytes\t%s\ndu_bytes\t%s\nfree_disk_bytes\t%s\n' \
    "$LEDGER_BYTES" "$LAST_DU_BYTES" "$FREE_DISK_BYTES"
} | checked_text replace "$GATE_INPUT"
du_gate gate_input
E_GATE_NS=$(( $(monotonic_ns)-START_NS ))
run_source 120 replace "$TARGET/logs/gate.log" append "$TARGET/logs/gate.log" \
  "$BIN" --gate "$GATE_INPUT" "$E_GATE_NS" "$TARGET" \
  "$TARGET/preflight/F269-D02.preflight.tsv"
grep -Fqx $'pass\t1' "$TARGET/preflight/F269-D02.preflight.tsv"
du_gate gate

close_packet() {
  local label=$1 close_remaining
  PHASE=final_resource_record
  record_resources "$TARGET/logs/resource_final.tsv"
  du_gate before_final_hashes
  PHASE=final_hashes
  close_remaining=$(source_deadline_seconds)
  timeout --kill-after=5s "${close_remaining}s" nice -n 15 \
    "$BIN" --close-logs "$TARGET" "$LEDGER_STATE"
  close_remaining=$(source_deadline_seconds)
  timeout --kill-after=5s "${close_remaining}s" nice -n 15 \
    "$BIN" --finalize-hashes "$TARGET" "$LEDGER_STATE" "$TARGET/F269-D02.final.sha256"
  EVIDENCE_FROZEN=1
  (cd -- "$TARGET"; sha256sum --check F269-D02.final.sha256 >/dev/null)
  report=$("$BIN" --ledger-check "$TARGET" "$LEDGER_STATE")
  final_regular=$(awk -F '\t' '$1=="evidence_regular_bytes" {print $2}' <<<"$report")
  final_frozen=$(awk -F '\t' '$1=="ledger_frozen" {print $2}' <<<"$report")
  final_du=$(du -sb --apparent-size -- "$TARGET" | awk '{print $1}')
  [[ $final_frozen == 1 && $final_regular -le $AGGREGATE_CAP && $final_du -le $AGGREGATE_CAP ]]
  SUCCESS=1
  echo "$label target=$TARGET workers=$W grammar_sha256=$GRAMMAR_SHA bytes=$final_regular"
}

if [[ $MODE == preflight ]]; then
  close_packet F269_PREFLIGHT_PASS
  exit 0
fi

capacity_gate() {
  local phase=$1 load_now mem_now disk_now
  refuse_overlap
  load_now=$(awk '{print $1}' /proc/loadavg)
  mem_now=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk_now=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
  awk -v load="$load_now" -v cpus="$CPUS" 'BEGIN {exit !(load<=cpus)}'
  [[ $mem_now -ge 4194304 && $((disk_now*1024)) -ge $MIN_DISK_BYTES ]]
  log_line "RESOURCE_PASS phase=$phase load=$load_now mem_kib=$mem_now disk_kib=$disk_now"
}

PHASE=discovery
capacity_gate discovery
du_gate before_discovery
run_source 0 replace "$TARGET/logs/discovery.log" append "$TARGET/logs/discovery.log" \
  "$BIN" --discovery "$SOURCE_DIR/F269-D02.baselines.tsv" "$TARGET" "$W"
grep -Fq 'DISCOVERY_PASS' "$TARGET/logs/discovery.log"
du_gate after_discovery

DISCOVERY_CORPUS="$TARGET/F269-D02.discovery.corpus.tsv"
SELECTION="$TARGET/F269-D02.selection.tsv"
DISCOVERY_CORPUS_SHA=$(sha256sum "$DISCOVERY_CORPUS" | awk '{print $1}')
SELECTION_SHA=$(sha256sum "$SELECTION" | awk '{print $1}')
readonly DISCOVERY_CORPUS SELECTION DISCOVERY_CORPUS_SHA SELECTION_SHA
grep -Fq "corpus_sha256=$DISCOVERY_CORPUS_SHA" "$TARGET/logs/discovery.log"
grep -Fq "selection_sha256=$SELECTION_SHA" "$TARGET/logs/discovery.log"

PHASE=heldout
capacity_gate heldout
du_gate before_heldout
run_source 0 replace "$TARGET/logs/heldout.log" append "$TARGET/logs/heldout.log" \
  "$BIN" --heldout "$SOURCE_DIR/F269-D02.baselines.tsv" "$TARGET" "$W" \
  "$SELECTION" "$SELECTION_SHA" "$DISCOVERY_CORPUS_SHA"
grep -Fq 'HELDOUT_PASS' "$TARGET/logs/heldout.log"
[[ $(sha256sum "$SELECTION" | awk '{print $1}') == "$SELECTION_SHA" ]]
[[ $(sha256sum "$DISCOVERY_CORPUS" | awk '{print $1}') == "$DISCOVERY_CORPUS_SHA" ]]
du_gate after_heldout

expected_outputs=$'.F269-D02.ledger.state\n.F269-D02.ledger.state.lock\nF269-D02.baseline_aggregates.tsv\nF269-D02.baselines.tsv\nF269-D02.controls.tsv\nF269-D02.discovery.certificates.jsonl\nF269-D02.discovery.control_alias.tsv\nF269-D02.discovery.corpus.tsv\nF269-D02.discovery.direct_families.tsv\nF269-D02.discovery.selector_rules.tsv\nF269-D02.grammar.tsv\nF269-D02.heldout.certificates.jsonl\nF269-D02.heldout.control_alias.tsv\nF269-D02.heldout.corpus.tsv\nF269-D02.heldout.counterexamples.tsv\nF269-D02.heldout.lead_gate.tsv\nF269-D02.heldout.rules.tsv\nF269-D02.manifest.tsv\nF269-D02.selection.tsv\nF269-D02.workers.tsv'
actual_outputs=$(find "$TARGET" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ "$actual_outputs" == "$expected_outputs" ]]

PHASE=production_compression
COMPRESSION_MANIFEST="$TARGET/preflight/F269-D02.compression.tsv"
printf 'uncompressed_name\tuncompressed_bytes\tuncompressed_sha256\tcompressed_name\tcompressed_bytes\tcompressed_sha256\n' | \
  checked_text replace "$COMPRESSION_MANIFEST"
for name in \
  F269-D02.discovery.corpus.tsv F269-D02.discovery.control_alias.tsv \
  F269-D02.discovery.selector_rules.tsv F269-D02.discovery.direct_families.tsv \
  F269-D02.discovery.certificates.jsonl F269-D02.heldout.corpus.tsv \
  F269-D02.heldout.control_alias.tsv F269-D02.heldout.rules.tsv \
  F269-D02.heldout.certificates.jsonl F269-D02.heldout.counterexamples.tsv \
  F269-D02.baseline_aggregates.tsv F269-D02.controls.tsv; do
  capacity_gate "compress_$name"
  source="$TARGET/$name"
  temporary="$TARGET/$name.gz.tmp"
  replacement="$TARGET/$name.gz"
  [[ -f "$source" && ! -e "$temporary" && ! -e "$replacement" ]]
  source_size=$(stat -c %s "$source")
  source_sha=$(sha256sum "$source" | awk '{print $1}')
  du_gate "before_compress_$name"
  run_plain 1200 replace "$temporary" append "$TARGET/logs/compression_production.log" \
    gzip -n -6 -c "$source"
  compressed_size=$(stat -c %s "$temporary")
  compressed_sha=$(sha256sum "$temporary" | awk '{print $1}')
  du_gate "compressed_closed_$name"
  "$BIN" --compression-commit "$TARGET" "$LEDGER_STATE" "$source" "$temporary" "$replacement"
  [[ $(sha256sum "$replacement" | awk '{print $1}') == "$compressed_sha" ]]
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$source_size" "$source_sha" \
    "$name.gz" "$compressed_size" "$compressed_sha" | checked_text append "$COMPRESSION_MANIFEST"
  du_gate "compressed_replacement_$name"
done

close_packet "F269_COMPLETE_PASS selection_sha256=$SELECTION_SHA"
