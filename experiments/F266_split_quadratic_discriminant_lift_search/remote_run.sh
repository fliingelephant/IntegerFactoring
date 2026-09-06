#!/usr/bin/env bash
set -euo pipefail

work_dir=/root/IntegerFactoring_F266/F266-D01
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
preflight_dir="$work_dir/preflight"
archive_dir="$work_dir/archive"
cd "$work_dir"

sha256sum -c FROZEN.sha256
frozen_manifest_sha=$(sha256sum FROZEN.sha256 | cut -d' ' -f1)
test -f HOSTILE_PRERUN_AUDIT.md
grep -qx '# Verdict: PASS' HOSTILE_PRERUN_AUDIT.md
grep -Fqx "frozen_manifest_sha256: $frozen_manifest_sha" HOSTILE_PRERUN_AUDIT.md

refuse_overlap() {
  if ps -eo args | grep -E 'F258-D01|F259-D0[12]|F260-D0[12]|F261-D0[12]|F262-D01|F263-D0[12]|F264-D0[123]|F265-D0[12]|F266-D01.*search' | grep -v grep >/dev/null; then
    echo 'F266-D01 refuses overlap with F258-D01 through F266-D01 validation or production.' >&2
    exit 73
  fi
}

for path in "$out_dir" "$log_dir" "$preflight_dir" "$archive_dir"; do
  if [[ -e "$path" ]]; then
    echo "F266-D01 refuses to overwrite $path" >&2
    exit 74
  fi
done
mkdir "$out_dir" "$log_dir" "$preflight_dir" "$archive_dir"

refuse_overlap
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  nproc
  cat /proc/loadavg
  free -h
  df -h /root
  ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | head -n 32
} >"$log_dir/resource_before.txt"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
deadline=$((SECONDS + 14400))

nice -n 15 /usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread search.cpp -o search \
  >"$log_dir/compile.stdout" 2>"$log_dir/compile.stderr"
timeout 300s nice -n 15 ./search --self-test \
  >"$log_dir/selftest.stdout" 2>"$log_dir/selftest.stderr"

remaining=$((deadline - SECONDS))
[[ $remaining -gt 0 ]] || exit 124
refuse_overlap
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --preflight \
    "$preflight_dir/F266-D01.preflight.json" 1
) >"$log_dir/preflight.stdout" 2>"$log_dir/preflight.stderr"

preflight_files=$(find "$preflight_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ "$preflight_files" == 'F266-D01.preflight.json' ]]
grep -q '"pass":true' "$preflight_dir/F266-D01.preflight.json"

remaining=$((deadline - SECONDS))
[[ $remaining -gt 0 ]] || exit 124
refuse_overlap
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --discovery "$out_dir" 8
) >"$log_dir/discovery.stdout" 2>"$log_dir/discovery.stderr"

expected_discovery=$'F266-D01.discovery.banks.tsv\nF266-D01.discovery.certificates.jsonl\nF266-D01.discovery.corpus.sha256\nF266-D01.discovery.corpus.tsv\nF266-D01.discovery.families.tsv\nF266-D01.discovery.manifest.tsv\nF266-D01.selection.sha256\nF266-D01.selection.tsv'
actual_discovery=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ "$actual_discovery" == "$expected_discovery" ]]
(
  cd "$out_dir"
  sha256sum -c F266-D01.discovery.corpus.sha256
  sha256sum -c F266-D01.selection.sha256
)
selection_sha=$(cut -d' ' -f1 "$out_dir/F266-D01.selection.sha256")
corpus_sha=$(cut -d' ' -f1 "$out_dir/F266-D01.discovery.corpus.sha256")

remaining=$((deadline - SECONDS))
[[ $remaining -gt 0 ]] || exit 124
refuse_overlap
(
  ulimit -v 4194304
  ulimit -f 1048576
  timeout "${remaining}s" nice -n 15 ./search --heldout "$out_dir" \
    "$out_dir/F266-D01.selection.tsv" "$selection_sha" \
    "$out_dir/F266-D01.discovery.corpus.tsv" "$corpus_sha" 8
) >"$log_dir/heldout.stdout" 2>"$log_dir/heldout.stderr"

expected_complete=$'F266-D01.discovery.banks.tsv\nF266-D01.discovery.certificates.jsonl\nF266-D01.discovery.corpus.sha256\nF266-D01.discovery.corpus.tsv\nF266-D01.discovery.families.tsv\nF266-D01.discovery.manifest.tsv\nF266-D01.heldout.banks.tsv\nF266-D01.heldout.certificates.jsonl\nF266-D01.heldout.corpus.tsv\nF266-D01.heldout.families.tsv\nF266-D01.heldout.lead_gate.tsv\nF266-D01.heldout.manifest.tsv\nF266-D01.selection.sha256\nF266-D01.selection.tsv'
actual_complete=$(find "$out_dir" -maxdepth 1 -type f -printf '%f\n' | sort)
[[ "$actual_complete" == "$expected_complete" ]]

output_bytes=$(du -sb "$out_dir" "$preflight_dir" | awk '{s+=$1} END {print s}')
[[ $output_bytes -le 1073741824 ]]

remaining=$((deadline - SECONDS))
[[ $remaining -gt 0 ]] || exit 124
command -v zstd >"$log_dir/zstd.path"
(
  ulimit -f 1048576
  cd "$work_dir"
  timeout "${remaining}s" nice -n 15 tar -cf - \
    ALGEBRA.md PREREGISTRATION.md PRELAUNCH_MANIFEST.md FROZEN.sha256 \
    search.cpp remote_run.sh HOSTILE_PRERUN_AUDIT.md output logs preflight \
    | zstd -T1 -3 -o "$archive_dir/F266-D01.evidence.tar.zst"
)
archive_bytes=$(stat -c '%s' "$archive_dir/F266-D01.evidence.tar.zst")
[[ $archive_bytes -le 1073741824 ]]
sha256sum "$archive_dir/F266-D01.evidence.tar.zst" >"$archive_dir/F266-D01.evidence.tar.zst.sha256"

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  cat /proc/loadavg
  free -h
  df -h /root
} >"$log_dir/resource_after.txt"

{
  echo -e 'field\tvalue'
  echo -e "start_utc\t$start_utc"
  echo -e "end_utc\t$end_utc"
  echo -e "workers\t8"
  echo -e "output_bytes\t$output_bytes"
  echo -e "archive_bytes\t$archive_bytes"
  echo -e "selection_sha256\t$selection_sha"
  echo -e "discovery_corpus_sha256\t$corpus_sha"
  echo -e "frozen_manifest_sha256\t$frozen_manifest_sha"
} >"$log_dir/F266-D01.run_manifest.tsv"

echo "F266-D01 complete selection_sha256=$selection_sha corpus_sha256=$corpus_sha"
