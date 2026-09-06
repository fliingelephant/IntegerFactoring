#!/usr/bin/env bash
set -euo pipefail
umask 077
ulimit -v 4194304
ulimit -f 1048576

work_dir=/root/IntegerFactoring_F266/F266-D04
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
      echo "F266-D04 refuses overlap with pid=$pid cwd=$cwd cmd=$cmd" >&2
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

sidecar_record_matches() {
  local record=$1
  local digest=$2
  local filename=$3
  [[ $record == "$digest  $filename" ]]
}

verify_sidecar_record() {
  local sidecar=$1
  local digest=$2
  local filename=$3
  local record bytes lines expected_bytes
  IFS= read -r record <"$sidecar"
  sidecar_record_matches "$record" "$digest" "$filename"
  bytes=$(stat -c '%s' "$sidecar")
  lines=$(wc -l <"$sidecar")
  expected_bytes=$((${#digest} + 2 + ${#filename} + 1))
  [[ $bytes -eq $expected_bytes && $lines -eq 1 ]]
}

sidecar_parser_self_test() {
  local digest=0000000000000000000000000000000000000000000000000000000000000000
  local other=1111111111111111111111111111111111111111111111111111111111111111
  sidecar_record_matches "$digest  fixed.tsv" "$digest" fixed.tsv
  ! sidecar_record_matches "$digest  other.tsv" "$digest" fixed.tsv
  ! sidecar_record_matches "$other  fixed.tsv" "$digest" fixed.tsv
  ! sidecar_record_matches "$digest *fixed.tsv" "$digest" fixed.tsv
}

direct_schema_string() {
  local first=1 stage outcome
  for stage in source base transformed projective resultant carry singleton \
               equal_or_template; do
    for outcome in tests unit full proper; do
      if [[ $first -eq 0 ]]; then printf '\t'; fi
      printf 'direct_%s_%s' "$stage" "$outcome"
      first=0
    done
  done
}

verify_direct_counter_schema() {
  local bank_file=$1 expected observed
  expected=$(direct_schema_string)
  observed=$(awk -F '\t' 'NR==1 {
    separator=""
    for (i=1;i<=NF;i++) if ($i ~ /^direct_/) {
      printf "%s%s",separator,$i
      separator="\t"
    }
  }' "$bank_file")
  [[ $observed == "$expected" ]]
  awk -F '\t' '
    NR==1 {
      split("source base transformed projective resultant carry singleton equal_or_template",stage," ")
      for (i=1;i<=NF;i++) column[$i]=i
      for (s=1;s<=8;s++) {
        tests[s]=column["direct_" stage[s] "_tests"]
        unit[s]=column["direct_" stage[s] "_unit"]
        full[s]=column["direct_" stage[s] "_full"]
        proper[s]=column["direct_" stage[s] "_proper"]
        if (!tests[s] || !unit[s] || !full[s] || !proper[s]) exit 91
      }
      next
    }
    {
      for (s=1;s<=8;s++) {
        if ($(tests[s]) !~ /^[0-9]+$/ || $(unit[s]) !~ /^[0-9]+$/ ||
            $(full[s]) !~ /^[0-9]+$/ || $(proper[s]) !~ /^[0-9]+$/) exit 92
        if ($(tests[s]) != $(unit[s]) + $(full[s]) + $(proper[s])) exit 93
      }
    }
  ' "$bank_file"
}

sidecar_parser_self_test

for path in "$out_dir" "$log_dir" "$preflight_dir" "$archive_dir" "$work_dir/search"; do
  if [[ -e $path ]]; then
    echo "F266-D04 refuses to overwrite $path" >&2
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
    "$preflight_dir/F266-D04.preflight.json" 1
) >"$log_dir/preflight.stdout" 2>"$log_dir/preflight.stderr"
preflight_files=$(find "$preflight_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $preflight_files == 'F266-D04.preflight.json' ]]
grep -q '"pass":true' "$preflight_dir/F266-D04.preflight.json"
write_manifest "$log_dir/preflight.manifest.tsv" \
  "$preflight_dir/F266-D04.preflight.json" \
  "$log_dir/preflight.stdout" "$log_dir/preflight.stderr"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
discovery_stdout=$(
  (
    ulimit -v 4194304
    ulimit -f 1048576
    timeout "${remaining}s" nice -n 15 ./search --discovery "$out_dir" 8
  ) 2>"$log_dir/discovery.stderr"
)
printf '%s\n' "$discovery_stdout" >"$log_dir/discovery.stdout"
if [[ $discovery_stdout =~ corpus_sha256=([0-9a-f]{64})[[:space:]]selection_sha256=([0-9a-f]{64}) ]]; then
  corpus_sha=${BASH_REMATCH[1]}
  selection_sha=${BASH_REMATCH[2]}
else
  echo 'F266-D04 could not authenticate discovery-emitted digests.' >&2
  exit 76
fi
readonly corpus_sha selection_sha

expected_discovery=$'F266-D04.discovery.banks.tsv\nF266-D04.discovery.certificates.jsonl\nF266-D04.discovery.corpus.sha256\nF266-D04.discovery.corpus.tsv\nF266-D04.discovery.families.tsv\nF266-D04.discovery.manifest.tsv\nF266-D04.discovery.opaque.jsonl\nF266-D04.selection.sha256\nF266-D04.selection.tsv'
actual_discovery=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $actual_discovery == "$expected_discovery" ]]
(
  cd "$out_dir"
  timeout "$(remaining_seconds)s" sha256sum -c F266-D04.discovery.corpus.sha256
  timeout "$(remaining_seconds)s" sha256sum -c F266-D04.selection.sha256
)
verify_program_manifest "$out_dir/F266-D04.discovery.manifest.tsv" "$out_dir"
observed_selection_sha=$(timeout "$(remaining_seconds)s" sha256sum \
  "$out_dir/F266-D04.selection.tsv" | cut -d' ' -f1)
observed_corpus_sha=$(timeout "$(remaining_seconds)s" sha256sum \
  "$out_dir/F266-D04.discovery.corpus.tsv" | cut -d' ' -f1)
[[ $observed_selection_sha == "$selection_sha" ]]
[[ $observed_corpus_sha == "$corpus_sha" ]]
verify_sidecar_record "$out_dir/F266-D04.selection.sha256" "$selection_sha" \
  F266-D04.selection.tsv
verify_sidecar_record "$out_dir/F266-D04.discovery.corpus.sha256" "$corpus_sha" \
  F266-D04.discovery.corpus.tsv
verify_direct_counter_schema "$out_dir/F266-D04.discovery.banks.tsv"
write_manifest "$log_dir/discovery.manifest.tsv" \
  "$log_dir/discovery.stdout" "$log_dir/discovery.stderr" \
  "$out_dir/F266-D04.discovery.manifest.tsv" \
  "$out_dir/F266-D04.selection.tsv" "$out_dir/F266-D04.selection.sha256"
check_uncompressed_cap

refuse_overlap
remaining=$(remaining_seconds)
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --heldout "$out_dir" \
    "$out_dir/F266-D04.selection.tsv" "$selection_sha" \
    "$out_dir/F266-D04.discovery.corpus.tsv" "$corpus_sha" 8
) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"

expected_complete=$'F266-D04.discovery.banks.tsv\nF266-D04.discovery.certificates.jsonl\nF266-D04.discovery.corpus.sha256\nF266-D04.discovery.corpus.tsv\nF266-D04.discovery.families.tsv\nF266-D04.discovery.manifest.tsv\nF266-D04.discovery.opaque.jsonl\nF266-D04.heldout.banks.tsv\nF266-D04.heldout.certificates.jsonl\nF266-D04.heldout.corpus.tsv\nF266-D04.heldout.families.tsv\nF266-D04.heldout.lead_gate.tsv\nF266-D04.heldout.manifest.tsv\nF266-D04.heldout.opaque.jsonl\nF266-D04.selection.sha256\nF266-D04.selection.tsv'
actual_complete=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ $actual_complete == "$expected_complete" ]]
verify_program_manifest "$out_dir/F266-D04.heldout.manifest.tsv" "$out_dir"
verify_direct_counter_schema "$out_dir/F266-D04.heldout.banks.tsv"
verify_sidecar_record "$out_dir/F266-D04.selection.sha256" "$selection_sha" \
  F266-D04.selection.tsv
verify_sidecar_record "$out_dir/F266-D04.discovery.corpus.sha256" "$corpus_sha" \
  F266-D04.discovery.corpus.tsv
write_manifest "$log_dir/heldout.manifest.tsv" \
  "$log_dir/heldout.stdout" "$log_dir/heldout.stderr" \
  "$out_dir/F266-D04.heldout.manifest.tsv" \
  "$out_dir/F266-D04.heldout.lead_gate.tsv"
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
} >"$log_dir/F266-D04.run_manifest.tsv"

command -v zstd >"$log_dir/zstd.path"

verify_sidecar_record "$out_dir/F266-D04.selection.sha256" "$selection_sha" \
  F266-D04.selection.tsv
verify_sidecar_record "$out_dir/F266-D04.discovery.corpus.sha256" "$corpus_sha" \
  F266-D04.discovery.corpus.tsv

mapfile -t evidence_files < <(
  {
    echo ALGEBRA.md
    echo PREREGISTRATION.md
    echo PRELAUNCH_MANIFEST.md
    echo FROZEN.sha256
    echo search.cpp
    echo remote_run.sh
    echo HOSTILE_PRERUN_AUDIT.md
    find output logs preflight -type f ! -name 'F266-D04.uncompressed.manifest.tsv' \
      ! -name 'F266-D04.uncompressed.manifest.tsv.sha256' -print
  } | sort
)
write_manifest "$log_dir/F266-D04.uncompressed.manifest.tsv" "${evidence_files[@]}"
timeout "$(remaining_seconds)s" sha256sum "$log_dir/F266-D04.uncompressed.manifest.tsv" \
  >"$log_dir/F266-D04.uncompressed.manifest.tsv.sha256"
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
  timeout "${remaining}s" nice -n 15 bash -o pipefail -c '
    tar -cf - \
      ALGEBRA.md PREREGISTRATION.md PRELAUNCH_MANIFEST.md FROZEN.sha256 \
      search.cpp remote_run.sh HOSTILE_PRERUN_AUDIT.md output logs preflight \
      | zstd -q -T1 -3 -o "$1"
  ' F266-D04-compression "$archive_dir/F266-D04.evidence.tar.zst"
)
archive_bytes=$(stat -c '%s' "$archive_dir/F266-D04.evidence.tar.zst")
[[ $archive_bytes -le 1073741824 ]]
remaining=$(remaining_seconds)
timeout "${remaining}s" sha256sum "$archive_dir/F266-D04.evidence.tar.zst" \
  >"$archive_dir/F266-D04.evidence.tar.zst.sha256"
write_manifest "$archive_dir/F266-D04.compression.manifest.tsv" \
  "$archive_dir/F266-D04.evidence.tar.zst" \
  "$archive_dir/F266-D04.evidence.tar.zst.sha256"
timeout "$(remaining_seconds)s" sha256sum \
  "$archive_dir/F266-D04.compression.manifest.tsv" \
  >"$archive_dir/F266-D04.compression.manifest.tsv.sha256"
archive_total_bytes=$(du -sb "$archive_dir" | awk '{print $1}')
[[ $archive_total_bytes -le 1073741824 ]]

echo "F266-D04 complete selection_sha256=$selection_sha corpus_sha256=$corpus_sha uncompressed_bytes=$uncompressed_bytes archive_bytes=$archive_bytes archive_total_bytes=$archive_total_bytes"
