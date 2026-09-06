#!/usr/bin/env bash
set -euo pipefail

experiment=F261-D02
workers=4
if [[ ${F261_V2_WORKERS:-} =~ ^[1-8]$ ]]; then
  workers=$F261_V2_WORKERS
fi

mkdir -p output logs
exec > >(tee "logs/${experiment}.stdout") 2> >(tee "logs/${experiment}.stderr" >&2)

echo "START_UTC $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "HOST $(uname -a)"
echo "CPUS $(getconf _NPROCESSORS_ONLN)"
echo "LOAD $(cat /proc/loadavg)"
free -h
df -h .
echo "GXX $(g++ -dumpfullversion -dumpversion)"

if pgrep -af '/root/IntegerFactoring_F258|/root/IntegerFactoring_F259|/root/IntegerFactoring_F260|F258-D|F259-D|F260-D' > "logs/${experiment}.incompatible.txt"; then
  echo "INCOMPATIBLE_PROCESS_ACTIVE"
  cat "logs/${experiment}.incompatible.txt"
  exit 20
fi

available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
free_kib=$(df -Pk . | awk 'NR==2 {print $4}')
if (( available_kib < 8388608 )); then
  echo "INSUFFICIENT_MEMORY_KIB ${available_kib}"
  exit 21
fi
if (( free_kib < 5242880 )); then
  echo "INSUFFICIENT_DISK_KIB ${free_kib}"
  exit 22
fi

load_integer=$(cut -d. -f1 /proc/loadavg)
if (( load_integer >= 64 && workers > 2 )); then
  workers=2
fi
echo "WORKERS ${workers}"

g++ -std=c++17 -O3 -pthread -Wall -Wextra -Wconversion V2_search.cpp -o V2_search
./V2_search --self-test
(
  ulimit -v 4194304
  exec timeout 3600s nice -n 15 ./V2_search --preflight "${workers}"
) | tee "logs/${experiment}.preflight.txt"

(
  ulimit -v 4194304
  exec timeout 14400s nice -n 15 ./V2_search "${workers}" \
    "output/${experiment}.summary.json" \
    "output/${experiment}.rows.tsv" \
    "output/${experiment}.inverse.tsv" \
    "output/${experiment}.consecutive.tsv"
)

output_bytes=$(du -sb output | awk '{print $1}')
if (( output_bytes >= 1073741824 )); then
  echo "OUTPUT_CAP_EXCEEDED ${output_bytes}"
  exit 23
fi
echo "OUTPUT_BYTES ${output_bytes}"
sha256sum \
  "output/${experiment}.summary.json" \
  "output/${experiment}.rows.tsv" \
  "output/${experiment}.inverse.tsv" \
  "output/${experiment}.consecutive.tsv"
echo "END_UTC $(date -u +%Y-%m-%dT%H:%M:%SZ)"
