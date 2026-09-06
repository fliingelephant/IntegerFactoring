#!/usr/bin/env bash
set -euo pipefail
umask 077
ulimit -v 4194304
ulimit -f 1048576

work_dir=/root/IntegerFactoring_F266/F266-D02
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
preflight_dir="$work_dir/preflight"
archive_dir="$work_dir/archive"
cd "$work_dir"

deadline=$((SECONDS + 14400))

remaining_seconds() {
  local left=$((deadline - SECONDS))
  [[ $left -gt 0 ]] || exit 124
  echo "$left"
}

sha256sum -c FROZEN.sha256
frozen_manifest_sha=$(sha256sum FROZEN.sha256 | cut -d' ' -f1)
test -f HOSTILE_PRERUN_AUDIT.md
grep -qx '# Verdict: PASS' HOSTILE_PRERUN_AUDIT.md
grep -Fqx "frozen_manifest_sha256: $frozen_manifest_sha" HOSTILE_PRERUN_AUDIT.md

refuse_overlap() {
  local proc pid cwd cmd
  for proc in /proc/[0-9]*; do
    pid=${proc##*/}
    [[ $pid == $$ || $pid == $PPID ]] && continue
    cwd=$(readlink "$proc/cwd" 2>/dev/null || true)
    case "$cwd" in
      *F258*|*F259*|*F260*|*F261*|*F262*|*F263*|*F264*|*F265*|*F266*) ;;
      *) continue ;;
    esac
    cmd=$(tr '\0' ' ' <"$proc/cmdline" 2>/dev/null || true)
    if [[ $cmd =~ search|symbolic_search|remote_run|validate ]]; then
      echo "F266-D02 refuses overlap with pid=$pid cwd=$cwd cmd=$cmd" >&2
      exit 73
    fi
  done
}

write_manifest() {
  local manifest=$1
  shift
  [[ ! -e $manifest ]]
  {
    echo -e 'filename\tbytes\tlines\tsha256'
    local path bytes lines digest
    for path in "$@"; do
      [[ -f $path ]]
      bytes=$(stat -c '%s' "$path")
      lines=$(wc -l <"$path")
      digest=$(timeout "$(remaining_seconds)s" sha256sum "$path" | cut -d' ' -f1)
      echo -e "$path\t$bytes\t$lines\t$digest"
    done
  } >"$manifest"
}

verify_program_manifest() {
  local manifest=$1
  local directory=$2
  local filename bytes lines digest observed_bytes observed_lines observed_digest
  {
    IFS= read -r header
    [[ $header == $'filename\tbytes\tlines\tsha256' ]]
    while IFS=$'\t' read -r filename bytes lines digest; do
      [[ -f "$directory/$filename" ]]
      observed_bytes=$(stat -c '%s' "$directory/$filename")
      observed_lines=$(wc -l <"$directory/$filename")
      observed_digest=$(timeout "$(remaining_seconds)s" sha256sum "$directory/$filename" |
                        cut -d' ' -f1)
      [[ $observed_bytes == "$bytes" && $observed_lines == "$lines" &&
         $observed_digest == "$digest" ]]
    done
  } <"$manifest"
}

check_uncompressed_cap() {
  local bytes
  bytes=$(
    {
      du -sb "$out_dir" "$preflight_dir" "$log_dir" | awk '{print $1}'
      stat -c '%s' ALGEBRA.md PREREGISTRATION.md PRELAUNCH_MANIFEST.md \
        FROZEN.sha256 search.cpp remote_run.sh HOSTILE_PRERUN_AUDIT.md
    } | awk '{sum+=$1} END {print sum}'
  )
  [[ $bytes -le 1073741824 ]]
}

for path in "$out_dir" "$log_dir" "$preflight_dir" "$archive_dir" "$work_dir/search"; do
  if [[ -e $path ]]; then
    echo "F266-D02 refuses to overwrite $path" >&2
    exit 74
  fi
done

refuse_overlap
mkdir "$out_dir" "$log_dir" "$preflight_dir" "$archive_dir"

cpu_count=$(nproc)
memory_available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
disk_available_kib=$(df -Pk "$work_dir" | awk 'NR==2 {print $4}')
load_one=$(awk '{print $1}' /proc/loadavg)
[[ $cpu_count -ge 8 ]]
[[ $memory_available_kib -ge 8388608 ]]
[[ $disk_available_kib -ge 4194304 ]]
awk -v load="$load_one" -v cpus="$cpu_count" 'BEGIN {exit !(load <= 2*cpus)}'

{
  date -u +%Y-%m-%dT%H:%M:%SZ
  echo "cpu_count=$cpu_count"
  echo "memory_available_kib=$memory_available_kib"
  echo "disk_available_kib=$disk_available_kib"
  echo "load_one=$load_one"
  cat /proc/loadavg
  free -h
  df -h "$work_dir"
  ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,32p'
} >"$log_dir/resource_before.txt"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread \
    search.cpp -o search
) >"$log_dir/compile.stdout" 2>"$log_dir/compile.stderr"
write_manifest "$log_dir/compile.manifest.tsv" \
  "$log_dir/compile.stdout" "$log_dir/compile.stderr"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --self-test
) >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"
write_manifest "$log_dir/selftest.manifest.tsv" \
  "$log_dir/selftest.stdout" "$log_dir/selftest.stderr"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --preflight \
    "$preflight_dir/F266-D02.preflight.json" 1
) >"$log_dir/preflight.stdout" 2>"$log_dir/preflight.stderr"
preflight_files=$(find "$preflight_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $preflight_files == 'F266-D02.preflight.json' ]]
grep -q '"pass":true' "$preflight_dir/F266-D02.preflight.json"
write_manifest "$log_dir/preflight.manifest.tsv" \
  "$preflight_dir/F266-D02.preflight.json" \
  "$log_dir/preflight.stdout" "$log_dir/preflight.stderr"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --discovery "$out_dir" 8
) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"

expected_discovery=$'F266-D02.discovery.banks.tsv\nF266-D02.discovery.certificates.jsonl\nF266-D02.discovery.corpus.sha256\nF266-D02.discovery.corpus.tsv\nF266-D02.discovery.families.tsv\nF266-D02.discovery.manifest.tsv\nF266-D02.discovery.opaque.jsonl\nF266-D02.selection.sha256\nF266-D02.selection.tsv'
actual_discovery=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $actual_discovery == "$expected_discovery" ]]
(
  cd "$out_dir"
  timeout "$(remaining_seconds)s" sha256sum -c F266-D02.discovery.corpus.sha256
  timeout "$(remaining_seconds)s" sha256sum -c F266-D02.selection.sha256
)
verify_program_manifest "$out_dir/F266-D02.discovery.manifest.tsv" "$out_dir"
selection_sha=$(cut -d' ' -f1 "$out_dir/F266-D02.selection.sha256")
corpus_sha=$(cut -d' ' -f1 "$out_dir/F266-D02.discovery.corpus.sha256")
write_manifest "$log_dir/discovery.manifest.tsv" \
  "$log_dir/discovery.stdout" "$log_dir/discovery.stderr" \
  "$out_dir/F266-D02.discovery.manifest.tsv" \
  "$out_dir/F266-D02.selection.tsv" "$out_dir/F266-D02.selection.sha256"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --heldout "$out_dir" \
    "$out_dir/F266-D02.selection.tsv" "$selection_sha" \
    "$out_dir/F266-D02.discovery.corpus.tsv" "$corpus_sha" 8
) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"

expected_complete=$'F266-D02.discovery.banks.tsv\nF266-D02.discovery.certificates.jsonl\nF266-D02.discovery.corpus.sha256\nF266-D02.discovery.corpus.tsv\nF266-D02.discovery.families.tsv\nF266-D02.discovery.manifest.tsv\nF266-D02.discovery.opaque.jsonl\nF266-D02.heldout.banks.tsv\nF266-D02.heldout.certificates.jsonl\nF266-D02.heldout.corpus.tsv\nF266-D02.heldout.families.tsv\nF266-D02.heldout.lead_gate.tsv\nF266-D02.heldout.manifest.tsv\nF266-D02.heldout.opaque.jsonl\nF266-D02.selection.sha256\nF266-D02.selection.tsv'
actual_complete=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $actual_complete == "$expected_complete" ]]
verify_program_manifest "$out_dir/F266-D02.heldout.manifest.tsv" "$out_dir"
write_manifest "$log_dir/heldout.manifest.tsv" \
  "$log_dir/heldout.stdout" "$log_dir/heldout.stderr" \
  "$out_dir/F266-D02.heldout.manifest.tsv" \
  "$out_dir/F266-D02.heldout.lead_gate.tsv"
check_uncompressed_cap

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  cat /proc/loadavg
  free -h
  df -h "$work_dir"
} >"$log_dir/resource_after.txt"

{
  echo -e 'field\tvalue'
  echo -e "start_utc\t$start_utc"
  echo -e "end_utc\t$end_utc"
  echo -e 'workers\t8'
  echo -e "selection_sha256\t$selection_sha"
  echo -e "discovery_corpus_sha256\t$corpus_sha"
  echo -e "frozen_manifest_sha256\t$frozen_manifest_sha"
} >"$log_dir/F266-D02.run_manifest.tsv"

command -v zstd >"$log_dir/zstd.path"

mapfile -t evidence_files < <(
  {
    echo ALGEBRA.md
    echo PREREGISTRATION.md
    echo PRELAUNCH_MANIFEST.md
    echo FROZEN.sha256
    echo search.cpp
    echo remote_run.sh
    echo HOSTILE_PRERUN_AUDIT.md
    find output logs preflight -type f ! -name 'F266-D02.uncompressed.manifest.tsv' \
      ! -name 'F266-D02.uncompressed.manifest.tsv.sha256' -print
  } | sort
)
write_manifest "$log_dir/F266-D02.uncompressed.manifest.tsv" "${evidence_files[@]}"
timeout "$(remaining_seconds)s" sha256sum "$log_dir/F266-D02.uncompressed.manifest.tsv" \
  >"$log_dir/F266-D02.uncompressed.manifest.tsv.sha256"
check_uncompressed_cap
uncompressed_bytes=$(
  {
    du -sb "$out_dir" "$preflight_dir" "$log_dir" | awk '{print $1}'
    stat -c '%s' ALGEBRA.md PREREGISTRATION.md PRELAUNCH_MANIFEST.md \
      FROZEN.sha256 search.cpp remote_run.sh HOSTILE_PRERUN_AUDIT.md
  } | awk '{sum+=$1} END {print sum}'
)

remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 tar -cf - \
    ALGEBRA.md PREREGISTRATION.md PRELAUNCH_MANIFEST.md FROZEN.sha256 \
    search.cpp remote_run.sh HOSTILE_PRERUN_AUDIT.md output logs preflight \
    | zstd -q -T1 -3 -o "$archive_dir/F266-D02.evidence.tar.zst"
)
archive_bytes=$(stat -c '%s' "$archive_dir/F266-D02.evidence.tar.zst")
[[ $archive_bytes -le 1073741824 ]]
remaining=$(remaining_seconds)
timeout "${remaining}s" sha256sum "$archive_dir/F266-D02.evidence.tar.zst" \
  >"$archive_dir/F266-D02.evidence.tar.zst.sha256"
write_manifest "$archive_dir/F266-D02.compression.manifest.tsv" \
  "$archive_dir/F266-D02.evidence.tar.zst" \
  "$archive_dir/F266-D02.evidence.tar.zst.sha256"
timeout "$(remaining_seconds)s" sha256sum \
  "$archive_dir/F266-D02.compression.manifest.tsv" \
  >"$archive_dir/F266-D02.compression.manifest.tsv.sha256"
archive_total_bytes=$(du -sb "$archive_dir" | awk '{print $1}')
[[ $archive_total_bytes -le 1073741824 ]]

echo "F266-D02 complete selection_sha256=$selection_sha corpus_sha256=$corpus_sha uncompressed_bytes=$uncompressed_bytes archive_bytes=$archive_bytes archive_total_bytes=$archive_total_bytes"
