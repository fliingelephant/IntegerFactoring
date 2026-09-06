#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  echo "usage: remote_run.sh EVIDENCE BANKS CORPUS RUN_DIR WORKERS" >&2
  exit 2
fi

packet_dir="$(cd "$(dirname "$0")" && pwd)"
evidence="$1"
banks="$2"
corpus="$3"
run_dir="$4"
workers="$5"

if [[ ! "$workers" =~ ^[1-8]$ ]]; then
  echo "workers must be in 1..8" >&2
  exit 2
fi
if [[ -e "$run_dir" ]]; then
  echo "run directory already exists: $run_dir" >&2
  exit 2
fi
for input in "$evidence" "$banks" "$corpus"; do
  if [[ ! -f "$input" ]]; then
    echo "missing input: $input" >&2
    exit 2
  fi
done

cd "$packet_dir"
sha256sum --check FROZEN.sha256

if [[ "$(sha256sum "$evidence" | cut -d ' ' -f 1)" != "a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc" ]]; then
  echo "evidence SHA-256 mismatch" >&2
  exit 2
fi
if [[ "$(sha256sum "$banks" | cut -d ' ' -f 1)" != "c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6" ]]; then
  echo "banks SHA-256 mismatch" >&2
  exit 2
fi
if [[ "$(sha256sum "$corpus" | cut -d ' ' -f 1)" != "8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5" ]]; then
  echo "corpus SHA-256 mismatch" >&2
  exit 2
fi

mkdir -p "$run_dir"
{
  date -u '+utc=%Y-%m-%dT%H:%M:%SZ'
  uname -a
  uptime
  free -h
  df -h "$run_dir"
  ps -eo pid,ni,pcpu,pmem,etime,args --sort=-pcpu
} > "$run_dir/resource_before.txt"

available_kib="$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)"
free_bytes="$(df --output=avail -B1 "$run_dir" | tail -1 | tr -d ' ')"
if (( available_kib < 8388608 )); then
  echo "RESOURCE_STOP: less than 8 GiB memory available" | tee "$run_dir/resource_stop.txt"
  exit 3
fi
if (( free_bytes < 4294967296 )); then
  echo "RESOURCE_STOP: less than 4 GiB disk available" | tee "$run_dir/resource_stop.txt"
  exit 3
fi
if pgrep -af '(^|[/[:space:]])[^[:space:]]*(F265|f265|F269|f269)[^[:space:]]*([[:space:]]|$)' > "$run_dir/overlap.txt"; then
  echo "RESOURCE_STOP: F265/F269 process overlap" | tee "$run_dir/resource_stop.txt"
  exit 3
fi

g++ -O3 -DNDEBUG -std=c++17 -pthread f270_union.cpp -o "$run_dir/f270_union" \
  > "$run_dir/compile.stdout.txt" 2> "$run_dir/compile.stderr.txt"
sha256sum "$run_dir/f270_union" > "$run_dir/executable.sha256"
"$run_dir/f270_union" --self-test > "$run_dir/self_test.stdout.txt" 2> "$run_dir/self_test.stderr.txt"

/usr/bin/time -f '%e\t%M' -o "$run_dir/preflight.time.tsv" \
  nice -n 15 "$run_dir/f270_union" \
    --mode preflight --evidence "$evidence" --banks "$banks" --corpus "$corpus" \
    --out-dir "$run_dir/preflight" --workers "$workers" \
    > "$run_dir/preflight.stdout.txt" 2> "$run_dir/preflight.stderr.txt"

read -r preflight_seconds preflight_rss_kib < "$run_dir/preflight.time.tsv"
preflight_bytes="$(du -sb "$run_dir/preflight" | cut -f 1)"
projected_seconds="$(awk -v value="$preflight_seconds" 'BEGIN {printf "%.6f", value*188/8*4}')"
projected_rss_kib="$((preflight_rss_kib * 4))"
projected_bytes="$((preflight_bytes * 188 / 8 * 4))"
{
  echo -e 'metric\tobserved\tprojected_factor4\tgate'
  echo -e "wall_seconds\t${preflight_seconds}\t${projected_seconds}\t14400"
  echo -e "max_rss_kib\t${preflight_rss_kib}\t${projected_rss_kib}\t4194304"
  echo -e "output_bytes\t${preflight_bytes}\t${projected_bytes}\t536870912"
} > "$run_dir/projection.tsv"

if ! awk -v value="$projected_seconds" 'BEGIN {exit !(value <= 14400)}'; then
  echo "RESOURCE_STOP: projected wall exceeds four hours" | tee "$run_dir/resource_stop.txt"
  exit 3
fi
if (( projected_rss_kib > 4194304 )); then
  echo "RESOURCE_STOP: projected memory exceeds 4 GiB" | tee "$run_dir/resource_stop.txt"
  exit 3
fi
if (( projected_bytes > 536870912 )); then
  echo "RESOURCE_STOP: projected output exceeds 512 MiB" | tee "$run_dir/resource_stop.txt"
  exit 3
fi

/usr/bin/time -f '%e\t%M' -o "$run_dir/target.time.tsv" \
  timeout --signal=TERM --kill-after=30s 14400 \
  nice -n 15 "$run_dir/f270_union" \
    --mode target --evidence "$evidence" --banks "$banks" --corpus "$corpus" \
    --out-dir "$run_dir/target" --workers "$workers" \
    > "$run_dir/target.stdout.txt" 2> "$run_dir/target.stderr.txt"

target_bytes="$(du -sb "$run_dir/target" | cut -f 1)"
if (( target_bytes > 536870912 )); then
  echo "RESOURCE_STOP: target output exceeds 512 MiB" | tee "$run_dir/resource_stop.txt"
  exit 3
fi
{
  date -u '+utc=%Y-%m-%dT%H:%M:%SZ'
  uptime
  free -h
  df -h "$run_dir"
} > "$run_dir/resource_after.txt"
find "$run_dir" -type f ! -name 'all_files.pre_manifest.sha256' -print0 | sort -z | xargs -0 sha256sum > "$run_dir/all_files.pre_manifest.sha256"
echo "F270_REMOTE_OK run_dir=$run_dir"
