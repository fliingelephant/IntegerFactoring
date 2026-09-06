#!/usr/bin/env bash
set -euo pipefail

source_file=${1:-scan.c}
output_file=${2:-D02_OUTPUT.tsv}
log_file=${3:-D02_RUN.log}
binary_file=/tmp/f224_beta2_ap_shift_phase_diagram_d02.bin

gcc -O3 -std=c11 -Wall -Wextra -Werror "$source_file" -lm -o "$binary_file"
ulimit -v 2097152
{ time -p timeout 600s nice -n 10 "$binary_file" >"$output_file"; } 2>"$log_file"
