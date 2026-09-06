#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

if [[ $# -ne 2 || ( $2 != preflight && $2 != complete ) ]]; then
  echo 'usage: remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY preflight|complete' >&2
  exit 64
fi

TARGET=$1
MODE=$2
SOURCE_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
VERSION=F269-D01
MEMORY_MAX=3758096384
AGGREGATE_CAP=536870912
LOG_CAP=16777216
SIDECAR_CAP=8388608
MIN_DISK_BYTES=5368709120
readonly TARGET MODE SOURCE_DIR VERSION MEMORY_MAX AGGREGATE_CAP LOG_CAP SIDECAR_CAP MIN_DISK_BYTES

case "$TARGET" in /*) ;; *) echo 'target must be absolute' >&2; exit 64;; esac
[[ "$TARGET" != / && "$TARGET" != /root && "$TARGET" != /tmp ]]
[[ ! -e "$TARGET" ]] || { echo "refuse existing evidence: $TARGET" >&2; exit 73; }

for command in awk date df du find g++ gzip head mkdir nice nproc ps readlink sed \
  sha256sum sort stat timeout truncate wc; do
  command -v "$command" >/dev/null
done
[[ -x /usr/bin/time ]]

cd -- "$SOURCE_DIR"
sha256sum -c FROZEN.sha256
FROZEN_MANIFEST_SHA=$(sha256sum FROZEN.sha256 | awk '{print $1}')
readonly FROZEN_MANIFEST_SHA
[[ -f HOSTILE_PRERUN_AUDIT.md ]]
grep -Fqx '# Verdict: PASS' HOSTILE_PRERUN_AUDIT.md
grep -Fqx "frozen_manifest_sha256: $FROZEN_MANIFEST_SHA" HOSTILE_PRERUN_AUDIT.md

monotonic_ns() {
  awk '{split($1,a,"."); f=a[2] "000000000"; print a[1] substr(f,1,9)}' /proc/uptime
}

refuse_overlap() {
  if ps -eo args= | grep -E '[F]265-D0[12].*(search|remote_run)|[f]265_search' >/dev/null; then
    echo 'RESOURCE_STOP reason=F265_active' >&2
    exit 73
  fi
}

START_NS=$(monotonic_ns)
HARD_DEADLINE=$((SECONDS+14400))
SOURCE_DEADLINE=$((HARD_DEADLINE-30))
readonly START_NS HARD_DEADLINE SOURCE_DEADLINE

refuse_overlap
CPUS=$(nproc)
LOAD=$(awk '{print $1}' /proc/loadavg)
MEM_AVAILABLE_KIB=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
DISK_AVAILABLE_KIB=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
awk -v load="$LOAD" -v cpus="$CPUS" 'BEGIN {exit !(load<=cpus)}' || {
  echo "RESOURCE_STOP reason=load load=$LOAD cpus=$CPUS" >&2; exit 75;
}
[[ $((DISK_AVAILABLE_KIB*1024)) -ge $MIN_DISK_BYTES ]] || {
  echo "RESOURCE_STOP reason=disk available_kib=$DISK_AVAILABLE_KIB" >&2; exit 75;
}

IDLE_CPUS=$(awk -v cpus="$CPUS" -v load="$LOAD" 'BEGIN{x=int(cpus-load); print x<1?1:x}')
if [[ $IDLE_CPUS -ge 8 && $MEM_AVAILABLE_KIB -ge 8388608 ]]; then W=8
elif [[ $IDLE_CPUS -ge 4 && $MEM_AVAILABLE_KIB -ge 6291456 ]]; then W=4
elif [[ $IDLE_CPUS -ge 2 && $MEM_AVAILABLE_KIB -ge 5242880 ]]; then W=2
else W=1
fi
readonly CPUS LOAD MEM_AVAILABLE_KIB DISK_AVAILABLE_KIB IDLE_CPUS W

CGROUP_PARENT_REL=$(awk -F: '$1=="0" {print $3}' /proc/$$/cgroup)
CGROUP_PARENT="/sys/fs/cgroup${CGROUP_PARENT_REL}"
CGROUP="$CGROUP_PARENT/f269_d01_$$"
readonly CGROUP_PARENT_REL CGROUP_PARENT CGROUP
[[ -f /sys/fs/cgroup/cgroup.controllers && -w "$CGROUP_PARENT/cgroup.procs" ]]
mkdir -- "$CGROUP"
[[ -w "$CGROUP/memory.max" && -w "$CGROUP/memory.swap.max" && -w "$CGROUP/cgroup.procs" ]]
printf '%s\n' "$MEMORY_MAX" >"$CGROUP/memory.max"
printf '0\n' >"$CGROUP/memory.swap.max"
[[ $(<"$CGROUP/memory.max") == "$MEMORY_MAX" && $(<"$CGROUP/memory.swap.max") == 0 ]]

(
  remaining=$((HARD_DEADLINE-SECONDS))
  [[ $remaining -gt 0 ]] && sleep "$remaining"
  if [[ -e "$CGROUP/cgroup.kill" ]]; then printf '1\n' >"$CGROUP/cgroup.kill" || true; fi
  sleep 1
  rmdir -- "$CGROUP" 2>/dev/null || true
) &
WATCHDOG_PID=$!
readonly WATCHDOG_PID
printf '%s\n' $$ >"$CGROUP/cgroup.procs"

cleanup() {
  set +e
  kill "$WATCHDOG_PID" 2>/dev/null
  wait "$WATCHDOG_PID" 2>/dev/null
  printf '%s\n' $$ >"$CGROUP_PARENT/cgroup.procs" 2>/dev/null
  rmdir -- "$CGROUP" 2>/dev/null
}
trap cleanup EXIT INT TERM

ulimit -Sv 4194304
ulimit -Hv 4194304
ulimit -Sf 1048576
ulimit -Hf 1048576

mkdir -m 0755 -- "$TARGET" "$TARGET/bin" "$TARGET/logs" "$TARGET/preflight"
exec 3>&1 4>&2
exec >>"$TARGET/logs/runner.log" 2>&1
printf 'version\t%s\nmode\t%s\nfrozen_manifest_sha256\t%s\n' \
  "$VERSION" "$MODE" "$FROZEN_MANIFEST_SHA"
printf 'workers\t%s\n' "$W" >"$TARGET/F269-D01.workers.tsv"

regular_bytes() {
  find "$TARGET" -type f -printf '%s\n' | awk '{s+=$1} END {printf "%.0f\n",s+0}'
}

du_gate() {
  local phase=$1 regular apparent
  [[ -z $(find "$TARGET" -type l -print -quit) ]]
  [[ -z $(find "$TARGET" -type f -links +1 -print -quit) ]]
  find "$TARGET" -type f -printf '%b\t%s\t%p\n' | \
    awk '$2>0 && $1*512<$2 {bad=1} END {exit bad}'
  regular=$(regular_bytes)
  apparent=$(du -sb --apparent-size -- "$TARGET" | awk '{print $1}')
  [[ $regular -le $AGGREGATE_CAP && $apparent -le $AGGREGATE_CAP ]]
  LEDGER_BYTES=$regular
  LAST_DU_BYTES=$apparent
  export LEDGER_BYTES LAST_DU_BYTES
  printf 'DU_PASS phase=%s regular=%s apparent=%s\n' "$phase" "$regular" "$apparent"
}

check_components() {
  local logs sidecars
  logs=$(find "$TARGET/logs" -type f -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  sidecars=$(find "$TARGET" -type f ! -path "$TARGET/logs/*" \
    ! -name 'serialization.image' ! -name 'splitmix.stream' ! -name 'splitmix.stream.gz' \
    -printf '%s\n' | awk '{s+=$1} END {print s+0}')
  [[ $logs -le $LOG_CAP && $sidecars -le $SIDECAR_CAP ]]
}

remaining_seconds() {
  local remaining=$((HARD_DEADLINE-SECONDS))
  [[ $remaining -gt 0 ]] || { echo 'RESOURCE_STOP reason=packet_deadline' >&2; exit 124; }
  printf '%s\n' "$remaining"
}

source_deadline_seconds() {
  local remaining=$((SOURCE_DEADLINE-SECONDS))
  [[ $remaining -gt 0 ]] || { echo 'RESOURCE_STOP reason=source_deadline' >&2; exit 124; }
  printf '%s\n' "$remaining"
}

run_plain() {
  local requested=$1 remaining
  shift
  refuse_overlap
  remaining=$(remaining_seconds)
  if [[ $requested -gt 0 && $requested -lt $remaining ]]; then remaining=$requested; fi
  timeout "${remaining}s" nice -n 15 "$@"
}

run_source() {
  local requested=$1 remaining source_remaining
  shift
  refuse_overlap
  remaining=$(remaining_seconds)
  source_remaining=$(source_deadline_seconds)
  if [[ $requested -gt 0 && $requested -lt $remaining ]]; then remaining=$requested; fi
  F269_DEADLINE_SECONDS=$source_remaining timeout "${remaining}s" nice -n 15 "$@"
}

record_resources() {
  local path=$1
  {
    date -u +%Y-%m-%dT%H:%M:%SZ
    printf 'cpus\t%s\nload\t%s\nmem_available_kib\t%s\ndisk_available_kib\t%s\nworkers\t%s\n' \
      "$CPUS" "$LOAD" "$MEM_AVAILABLE_KIB" "$DISK_AVAILABLE_KIB" "$W"
    awk '/MemTotal:|MemAvailable:/ {print}' /proc/meminfo
    df -h "$(dirname -- "$TARGET")"
    ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,32p'
  } >"$path"
}

record_resources "$TARGET/logs/resource_before.tsv"
du_gate resource_before

( ulimit -Sf 32768; run_plain 600 g++ -std=c++17 -O3 -DNDEBUG -pthread f269.cpp \
    -o "$TARGET/bin/f269" ) >"$TARGET/logs/compile.log" 2>&1
du_gate compile
check_components

run_source 300 "$TARGET/bin/f269" --self-test "$SOURCE_DIR/F269-D01.baselines.tsv" \
  >"$TARGET/logs/self_test.log" 2>&1
grep -Fq 'SELF_TEST_PASS' "$TARGET/logs/self_test.log"
du_gate self_test

metric() {
  local key=$1 path=$2
  awk -F '\t' -v key="$key" '$1==key {print $2}' "$path"
}

GRAMMAR_SHA=
for i in 1 2 3 4 5 6 7; do
  path="$TARGET/preflight/grammar_${i}.tsv"
  run_source 600 "$TARGET/bin/f269" --grammar-once >"$path" 2>"$TARGET/logs/grammar_${i}.log"
  eval "G${i}_NS=$(metric nanoseconds "$path")"
  sha=$(metric grammar_sha256 "$path")
  [[ -z $GRAMMAR_SHA || $sha == "$GRAMMAR_SHA" ]]
  GRAMMAR_SHA=$sha
  [[ $(metric root_retained "$path") == 444 && $(metric tuple_attempts "$path") == 5120 ]]
  retained=$(metric tuple_retained "$path")
  partition=$((retained+$(metric type_reject "$path")+$(metric provenance_reject "$path")+$(metric duplicate_reject "$path")+$(metric all_chamber_control_reject "$path")))
  [[ $partition -eq 5120 ]]
  [[ $((444+retained)) -eq $(metric final_syntax_count "$path") ]]
  du_gate "grammar_$i"
done
readonly GRAMMAR_SHA

printf '0\n' >"$CGROUP/memory.peak"
MAX_VMHWM=0
MAX_TIME_RSS=0
for i in 1 2 3 4; do
  round=$((i-1))
  path="$TARGET/preflight/round_${i}.tsv"
  time_path="$TARGET/preflight/round_${i}.time.txt"
  source_remaining=$(source_deadline_seconds)
  remaining=$(remaining_seconds)
  refuse_overlap
  F269_DEADLINE_SECONDS=$source_remaining timeout "${remaining}s" /usr/bin/time -v -o "$time_path" \
    nice -n 15 "$TARGET/bin/f269" --max-work-round "$W" "$round" \
    >"$path" 2>"$TARGET/logs/round_${i}.log"
  eval "R${i}_NS=$(metric nanoseconds "$path")"
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

SERIALIZATION="$TARGET/preflight/serialization.image"
for i in 1 2 3 4 5 6 7; do
  start=$(monotonic_ns)
  path="$TARGET/preflight/serialization_${i}.tsv"
  run_source 1200 "$TARGET/bin/f269" --serialization-write "$TARGET" "$SERIALIZATION" \
    >"$path" 2>"$TARGET/logs/serialization_${i}.log"
  [[ $(stat -c %s "$SERIALIZATION") -eq 277979136 ]]
  actual_sha=$(sha256sum "$SERIALIZATION" | awk '{print $1}')
  [[ $actual_sha == $(metric serialization_sha256 "$path") ]]
  du_gate "serialization_${i}_closed"
  run_source 120 "$TARGET/bin/f269" --checked-truncate "$TARGET" "$SERIALIZATION" \
    >>"$path" 2>>"$TARGET/logs/serialization_${i}.log"
  du_gate "serialization_${i}_truncated"
  end=$(monotonic_ns)
  eval "S${i}_NS=$((end-start))"
done

gzip --version | head -n 1 >"$TARGET/preflight/compressor.tsv"
STREAM="$TARGET/preflight/splitmix.stream"
COMPRESSED="$TARGET/preflight/splitmix.stream.gz"
for i in 1 2 3 4 5 6 7; do
  start=$(monotonic_ns)
  path="$TARGET/preflight/compression_${i}.tsv"
  run_source 600 "$TARGET/bin/f269" --splitmix-stream-write "$TARGET" "$STREAM" \
    >"$path" 2>"$TARGET/logs/compression_${i}.log"
  [[ $(stat -c %s "$STREAM") -eq 67108864 ]]
  du_gate "compression_${i}_source_closed"
  run_plain 600 gzip -n -6 -c "$STREAM" >"$COMPRESSED"
  sha256sum "$STREAM" "$COMPRESSED" >>"$path"
  du_gate "compression_${i}_closed"
  run_source 120 "$TARGET/bin/f269" --checked-truncate "$TARGET" "$COMPRESSED" \
    >>"$path" 2>>"$TARGET/logs/compression_${i}.log"
  run_source 120 "$TARGET/bin/f269" --checked-truncate "$TARGET" "$STREAM" \
    >>"$path" 2>>"$TARGET/logs/compression_${i}.log"
  du_gate "compression_${i}_truncated"
  end=$(monotonic_ns)
  eval "Z${i}_NS=$((end-start))"
done

record_resources "$TARGET/logs/resource_after.tsv"
du_gate resource_after
check_components
FREE_DISK_BYTES=$(( $(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}') * 1024 ))
GATE_INPUT="$TARGET/preflight/gate_input.tsv"
{
  printf 'workers\t%s\n' "$W"
  for i in 1 2 3 4 5 6 7; do eval "printf 'G%s_ns\\t%s\\n' '$i' \"\$G${i}_NS\""; done
  for i in 1 2 3 4; do eval "printf 'R%s_ns\\t%s\\n' '$i' \"\$R${i}_NS\""; done
  for i in 1 2 3 4 5 6 7; do eval "printf 'S%s_ns\\t%s\\n' '$i' \"\$S${i}_NS\""; done
  for i in 1 2 3 4 5 6 7; do eval "printf 'Z%s_ns\\t%s\\n' '$i' \"\$Z${i}_NS\""; done
  printf 'cgroup_memory_peak_bytes\t%s\nprocess_vmhwm_bytes\t%s\ntime_maxrss_bytes\t%s\n' \
    "$CGROUP_PEAK" "$MAX_VMHWM" "$MAX_TIME_RSS"
  printf 'registered_serialization_bytes\t277979136\nevidence_regular_bytes\t%s\ndu_bytes\t%s\nfree_disk_bytes\t%s\n' \
    "$LEDGER_BYTES" "$LAST_DU_BYTES" "$FREE_DISK_BYTES"
} >"$GATE_INPUT"
du_gate gate_input
E_GATE_NS=$(( $(monotonic_ns)-START_NS ))
run_source 120 "$TARGET/bin/f269" --gate "$GATE_INPUT" "$E_GATE_NS" "$TARGET" \
  "$TARGET/preflight/F269-D01.preflight.tsv" \
  >"$TARGET/logs/gate.log" 2>&1
grep -Fqx $'pass\t1' "$TARGET/preflight/F269-D01.preflight.tsv"
du_gate gate
check_components

if [[ $MODE == preflight ]]; then
  exec 1>&3 2>&4
  exec 3>&- 4>&-
  du_gate final_preflight
  echo "F269_PREFLIGHT_PASS target=$TARGET workers=$W grammar_sha256=$GRAMMAR_SHA bytes=$LEDGER_BYTES"
  exit 0
fi

capacity_gate() {
  local phase=$1 load mem disk
  refuse_overlap
  load=$(awk '{print $1}' /proc/loadavg)
  mem=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
  awk -v load="$load" -v cpus="$CPUS" 'BEGIN {exit !(load<=cpus)}'
  [[ $mem -ge 4194304 && $((disk*1024)) -ge $MIN_DISK_BYTES ]]
  printf 'RESOURCE_PASS phase=%s load=%s mem_kib=%s disk_kib=%s\n' \
    "$phase" "$load" "$mem" "$disk"
}

capacity_gate discovery
du_gate before_discovery
run_source 0 "$TARGET/bin/f269" --discovery "$SOURCE_DIR/F269-D01.baselines.tsv" \
  "$TARGET" "$W" >"$TARGET/logs/discovery.log" 2>&1
grep -Fq 'DISCOVERY_PASS' "$TARGET/logs/discovery.log"
du_gate after_discovery
check_components

DISCOVERY_CORPUS="$TARGET/F269-D01.discovery.corpus.tsv"
SELECTION="$TARGET/F269-D01.selection.tsv"
DISCOVERY_CORPUS_SHA=$(sha256sum "$DISCOVERY_CORPUS" | awk '{print $1}')
SELECTION_SHA=$(sha256sum "$SELECTION" | awk '{print $1}')
readonly DISCOVERY_CORPUS SELECTION DISCOVERY_CORPUS_SHA SELECTION_SHA
grep -Fq "corpus_sha256=$DISCOVERY_CORPUS_SHA" "$TARGET/logs/discovery.log"
grep -Fq "selection_sha256=$SELECTION_SHA" "$TARGET/logs/discovery.log"

capacity_gate heldout
du_gate before_heldout
run_source 0 "$TARGET/bin/f269" --heldout "$SOURCE_DIR/F269-D01.baselines.tsv" \
  "$TARGET" "$W" "$SELECTION" "$SELECTION_SHA" "$DISCOVERY_CORPUS_SHA" \
  >"$TARGET/logs/heldout.log" 2>&1
grep -Fq 'HELDOUT_PASS' "$TARGET/logs/heldout.log"
[[ $(sha256sum "$SELECTION" | awk '{print $1}') == "$SELECTION_SHA" ]]
[[ $(sha256sum "$DISCOVERY_CORPUS" | awk '{print $1}') == "$DISCOVERY_CORPUS_SHA" ]]
du_gate after_heldout
check_components

expected_outputs=$'F269-D01.baseline_aggregates.tsv\nF269-D01.baselines.tsv\nF269-D01.controls.tsv\nF269-D01.discovery.certificates.jsonl\nF269-D01.discovery.corpus.tsv\nF269-D01.discovery.rules.tsv\nF269-D01.grammar.tsv\nF269-D01.heldout.certificates.jsonl\nF269-D01.heldout.corpus.tsv\nF269-D01.heldout.counterexamples.tsv\nF269-D01.heldout.lead_gate.tsv\nF269-D01.heldout.rules.tsv\nF269-D01.manifest.tsv\nF269-D01.selection.tsv\nF269-D01.workers.tsv'
actual_outputs=$(find "$TARGET" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ "$actual_outputs" == "$expected_outputs" ]]

COMPRESSION_MANIFEST="$TARGET/preflight/F269-D01.compression.tsv"
printf 'uncompressed_name\tuncompressed_bytes\tuncompressed_sha256\tcompressed_name\tcompressed_bytes\tcompressed_sha256\n' \
  >"$COMPRESSION_MANIFEST"
for name in \
  F269-D01.discovery.corpus.tsv F269-D01.discovery.rules.tsv \
  F269-D01.discovery.certificates.jsonl F269-D01.heldout.corpus.tsv \
  F269-D01.heldout.rules.tsv F269-D01.heldout.certificates.jsonl \
  F269-D01.heldout.counterexamples.tsv F269-D01.baseline_aggregates.tsv \
  F269-D01.controls.tsv; do
  capacity_gate "compress_$name"
  source="$TARGET/$name"
  temporary="$TARGET/$name.gz.tmp"
  replacement="$TARGET/$name.gz"
  [[ -f "$source" && ! -e "$temporary" && ! -e "$replacement" ]]
  source_size=$(stat -c %s "$source")
  source_sha=$(sha256sum "$source" | awk '{print $1}')
  du_gate "before_compress_$name"
  run_plain 1200 gzip -n -6 -c "$source" >"$temporary"
  compressed_size=$(stat -c %s "$temporary")
  compressed_sha=$(sha256sum "$temporary" | awk '{print $1}')
  du_gate "compressed_closed_$name"
  mv -- "$temporary" "$replacement"
  rm -- "$source"
  [[ $(sha256sum "$replacement" | awk '{print $1}') == "$compressed_sha" ]]
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$source_size" "$source_sha" \
    "$name.gz" "$compressed_size" "$compressed_sha" >>"$COMPRESSION_MANIFEST"
  du_gate "compressed_replacement_$name"
done

record_resources "$TARGET/logs/resource_final.tsv"
du_gate before_final_hashes
check_components
find "$TARGET" -type f ! -name 'F269-D01.final.sha256' -print0 | sort -z | \
  xargs -0 sha256sum >"$TARGET/F269-D01.final.sha256"
du_gate final_hashes

exec 1>&3 2>&4
exec 3>&- 4>&-
du_gate final_complete
echo "F269_COMPLETE_PASS target=$TARGET workers=$W selection_sha256=$SELECTION_SHA bytes=$LEDGER_BYTES"
