#!/usr/bin/env bash
set -euo pipefail

source_file=${1:-scan.c}
output_file=${2:-OUTPUT.tsv}
log_file=${3:-RUN.log}
binary_file=/tmp/f224_beta2_ap_shift_phase_diagram.bin

gcc -O3 -std=c11 -Wall -Wextra -Werror "$source_file" -lm -o "$binary_file"
ulimit -v 2097152
/usr/bin/time -v timeout 600s nice -n 10 "$binary_file" >"$output_file" 2>"$log_file"
