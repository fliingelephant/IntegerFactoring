#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

if [[ $# -ne 1 ]]; then
  echo "usage: remote_run.sh ABSOLUTE_NEW_TARGET" >&2
  exit 64
fi

TARGET=$1
SOURCE_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
VERSION=F268-D01
WORKERS=8
MIN_MEM_KIB=8388608
MIN_DISK_KIB=4194304
FAMILY_SHA=aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce
readonly TARGET SOURCE_DIR VERSION WORKERS MIN_MEM_KIB MIN_DISK_KIB FAMILY_SHA

case "$TARGET" in
  /*) ;;
  *) echo "target must be absolute" >&2; exit 64 ;;
esac
[[ "$TARGET" != "/" && "$TARGET" != "/root" && "$TARGET" != "/tmp" ]]
[[ ! -e "$TARGET" ]] || { echo "refuse existing target: $TARGET" >&2; exit 73; }

for command in g++ sha256sum timeout nice awk sed grep sort find xargs du df date dirname wc ps nproc head; do
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

ulimit -v 4194304
ulimit -f 1677728
HARD_DEADLINE=$((SECONDS + 14400))
DEADLINE=$((HARD_DEADLINE - 300))
readonly HARD_DEADLINE DEADLINE

remaining_seconds() {
  local remaining=$((DEADLINE - SECONDS))
  [[ "$remaining" -gt 0 ]] || {
    echo "RESOURCE_STOP reason=packet_deadline" >&2
    exit 124
  }
  printf '%s\n' "$remaining"
}

run_phase() {
  local requested=$1 remaining
  shift
  refuse_overlap
  remaining=$(remaining_seconds)
  if [[ "$requested" -gt 0 && "$requested" -lt "$remaining" ]]; then
    remaining=$requested
  fi
  timeout "${remaining}s" "$@"
}

refuse_overlap() {
  if ps -eo args | grep -E 'F265-D0[12].*(search|remote_run)|f265_search' | \
      grep -v grep >/dev/null; then
    echo "RESOURCE_STOP reason=F265_active" >&2
    exit 73
  fi
}

capacity_gate() {
  local phase=$1 load mem disk cpus
  refuse_overlap
  remaining_seconds >/dev/null
  cpus=$(nproc)
  load=$(awk '{print $1}' /proc/loadavg)
  mem=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk=$(df -Pk "$(dirname -- "$TARGET")" | awk 'NR==2 {print $4}')
  awk -v observed="$load" -v cpus="$cpus" 'BEGIN {exit !(observed <= 2*cpus)}' || {
    echo "RESOURCE_STOP phase=$phase reason=load observed=$load cpus=$cpus" >&2
    exit 75
  }
  [[ "$mem" -ge "$MIN_MEM_KIB" ]] || {
    echo "RESOURCE_STOP phase=$phase reason=memory available_kib=$mem" >&2
    exit 75
  }
  [[ "$disk" -ge "$MIN_DISK_KIB" ]] || {
    echo "RESOURCE_STOP phase=$phase reason=disk available_kib=$disk" >&2
    exit 75
  }
  echo "RESOURCE_PASS phase=$phase load=$load mem_kib=$mem disk_kib=$disk"
}

record_resources() {
  local path=$1
  {
    date -u +%Y-%m-%dT%H:%M:%SZ
    nproc
    awk '{print $0}' /proc/loadavg
    awk '/MemTotal:|MemAvailable:/ {print $0}' /proc/meminfo
    df -h "$(dirname -- "$TARGET")"
    ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,32p'
  } >"$path"
}

check_output_cap() {
  local bytes
  bytes=$(du -sb "$TARGET" | awk '{print $1}')
  [[ "$bytes" -le 805306368 ]] || {
    echo "RESOURCE_STOP reason=output bytes=$bytes" >&2
    exit 75
  }
}

capacity_gate compile
mkdir -m 0755 -- "$TARGET"
mkdir -m 0755 -- "$TARGET/bin" "$TARGET/logs" "$TARGET/preflight"
record_resources "$TARGET/logs/resource_before.txt"

run_phase 600 nice -n 15 g++ -std=c++17 -O3 -DNDEBUG -pthread corpus.cpp \
  -o "$TARGET/bin/f268_corpus" >"$TARGET/logs/compile_corpus.log" 2>&1
run_phase 600 nice -n 15 g++ -std=c++17 -O3 -DNDEBUG -pthread search.cpp \
  -o "$TARGET/bin/f268_search" >"$TARGET/logs/compile_search.log" 2>&1
run_phase 600 nice -n 15 g++ -std=c++17 -O3 -DNDEBUG -pthread label_audit.cpp \
  -o "$TARGET/bin/f268_label_audit" >"$TARGET/logs/compile_label_audit.log" 2>&1

run_phase 120 nice -n 15 "$TARGET/bin/f268_corpus" --self-test \
  >"$TARGET/logs/corpus_self_test.log" 2>&1
run_phase 120 nice -n 15 "$TARGET/bin/f268_search" --self-test \
  "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  >"$TARGET/logs/search_self_test.log" 2>&1
run_phase 120 nice -n 15 "$TARGET/bin/f268_label_audit" --self-test \
  >"$TARGET/logs/label_self_test.log" 2>&1

capacity_gate corpus_preflight
GEN_TIME="$TARGET/preflight/corpus.time.tsv"
readonly GEN_TIME
run_phase 1800 /usr/bin/time -f 'wall_seconds\t%e\nmaxrss_kib\t%M' -o "$GEN_TIME" \
  nice -n 15 "$TARGET/bin/f268_corpus" --generate "$TARGET/corpus" \
  >"$TARGET/logs/corpus_generation.log" 2>&1

DISC_PUBLIC="$TARGET/corpus/F268-D01.discovery.public.tsv"
HELD_PUBLIC="$TARGET/corpus/F268-D01.heldout.public.tsv"
DISC_LABELS="$TARGET/corpus/F268-D01.discovery.labels.tsv"
HELD_LABELS="$TARGET/corpus/F268-D01.heldout.labels.tsv"
DISC_SHA=$(sha256sum "$DISC_PUBLIC" | awk '{print $1}')
HELD_SHA=$(sha256sum "$HELD_PUBLIC" | awk '{print $1}')
readonly DISC_PUBLIC HELD_PUBLIC DISC_LABELS HELD_LABELS DISC_SHA HELD_SHA

capacity_gate bank_preflight
run_phase 1800 /usr/bin/time -f 'wall_seconds\t%e\nmaxrss_kib\t%M' \
  -o "$TARGET/preflight/banks.time.tsv" \
  nice -n 15 "$TARGET/bin/f268_search" --preflight \
  "$DISC_PUBLIC" "$DISC_SHA" "$HELD_PUBLIC" "$HELD_SHA" \
  "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  "$TARGET/preflight/banks" "$WORKERS" \
  >"$TARGET/logs/bank_preflight.log" 2>&1

run_phase 60 nice -n 15 "$TARGET/bin/f268_search" --gate \
  "$GEN_TIME" "$TARGET/preflight/banks.time.tsv" \
  "$TARGET/preflight/banks/F268-D01.preflight.metrics.tsv" \
  "$TARGET/preflight/resource_gate.tsv" \
  >"$TARGET/logs/resource_gate.log" 2>&1

capacity_gate discovery
check_output_cap
run_phase 12600 nice -n 15 "$TARGET/bin/f268_search" --discovery \
  "$DISC_PUBLIC" "$DISC_SHA" "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  "$TARGET/discovery" "$WORKERS" \
  >"$TARGET/logs/discovery.log" 2>&1

SELECTION="$TARGET/discovery/F268-D01.selection.tsv"
SELECTION_SHA=$(sed -n 's/.*selection_sha256=\([0-9a-f]\{64\}\).*/\1/p' \
  "$TARGET/logs/discovery.log")
[[ $(printf '%s\n' "$SELECTION_SHA" | wc -l) -eq 1 && ${#SELECTION_SHA} -eq 64 ]]
readonly SELECTION SELECTION_SHA
printf '%s  %s\n' "$SELECTION_SHA" "$SELECTION" | sha256sum -c -

capacity_gate discovery_validation
check_output_cap
run_phase 3600 nice -n 15 "$TARGET/bin/f268_search" --validate \
  "$DISC_PUBLIC" discovery "$DISC_SHA" "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  "$TARGET/discovery/F268-D01.discovery.evidence.tsv" \
  >"$TARGET/logs/discovery_validation.log" 2>&1

capacity_gate heldout
check_output_cap
run_phase 12600 nice -n 15 "$TARGET/bin/f268_search" --heldout \
  "$HELD_PUBLIC" "$HELD_SHA" "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  "$SELECTION" "$SELECTION_SHA" "$DISC_SHA" "$TARGET/heldout" "$WORKERS" \
  >"$TARGET/logs/heldout.log" 2>&1

printf '%s  %s\n' "$SELECTION_SHA" "$SELECTION" | sha256sum -c -
capacity_gate heldout_validation
check_output_cap
run_phase 3600 nice -n 15 "$TARGET/bin/f268_search" --validate \
  "$HELD_PUBLIC" heldout "$HELD_SHA" "$SOURCE_DIR/FAMILY_SYNTAX.tsv" "$FAMILY_SHA" \
  "$TARGET/heldout/F268-D01.heldout.evidence.tsv" \
  >"$TARGET/logs/heldout_validation.log" 2>&1

# Hidden labels enter only after selection, heldout evaluation, lead generation,
# and public replay validation have all closed.
capacity_gate label_audit
check_output_cap
run_phase 300 nice -n 15 "$TARGET/bin/f268_label_audit" --audit \
  "$DISC_PUBLIC" "$DISC_LABELS" "$TARGET/discovery/F268-D01.discovery.banks.tsv" \
  "$TARGET/corpus/F268-D01.marker_shortfalls.tsv" \
  "$TARGET/F268-D01.discovery.label_audit.tsv" \
  >"$TARGET/logs/discovery_label_audit.log" 2>&1
run_phase 300 nice -n 15 "$TARGET/bin/f268_label_audit" --audit \
  "$HELD_PUBLIC" "$HELD_LABELS" "$TARGET/heldout/F268-D01.heldout.banks.tsv" \
  "$TARGET/corpus/F268-D01.marker_shortfalls.tsv" \
  "$TARGET/F268-D01.heldout.label_audit.tsv" \
  >"$TARGET/logs/heldout_label_audit.log" 2>&1

record_resources "$TARGET/logs/resource_after.txt"

TOTAL_BYTES_BEFORE_MANIFEST=$(du -sb "$TARGET" | awk '{print $1}')
readonly TOTAL_BYTES_BEFORE_MANIFEST
[[ "$TOTAL_BYTES_BEFORE_MANIFEST" -le 805306368 ]] || {
  echo "RESOURCE_STOP phase=final reason=output bytes=$TOTAL_BYTES_BEFORE_MANIFEST" >&2
  exit 75
}

find "$TARGET" -type f ! -name 'F268-D01.final.sha256' -print0 | sort -z | \
  xargs -0 sha256sum >"$TARGET/F268-D01.final.sha256"
TOTAL_BYTES=$(du -sb "$TARGET" | awk '{print $1}')
readonly TOTAL_BYTES
[[ "$TOTAL_BYTES" -le 805306368 ]] || {
  echo "RESOURCE_STOP phase=manifest reason=output bytes=$TOTAL_BYTES" >&2
  exit 75
}
echo "F268_RUN_PASS target=$TARGET selection_sha256=$SELECTION_SHA bytes=$TOTAL_BYTES"
