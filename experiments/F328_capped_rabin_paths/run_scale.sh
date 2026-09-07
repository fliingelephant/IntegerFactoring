#!/bin/zsh
set -eu

cd "${0:A:h:h:h}"

experiment_dir="experiments/F328_capped_rabin_paths"
source_path="$experiment_dir/capped_rabin_paths.py"
input_path="$experiment_dir/moduli.json"

run_one() {
  local modulus_id="$1"
  local trial_start="$2"
  local trials="$3"
  local tag="$4"
  env PYTHONHASHSEED=0 \
      OPENBLAS_NUM_THREADS=1 \
      OMP_NUM_THREADS=1 \
      VECLIB_MAXIMUM_THREADS=1 \
    gtimeout 30 python3 "$source_path" \
      --mode run \
      --input "$input_path" \
      --modulus-id "$modulus_id" \
      --trial-start "$trial_start" \
      --trials "$trials" \
      --max-cap 2048 \
      --run-label scale \
      --output "$experiment_dir/${tag}_output.json" \
      --status "$experiment_dir/${tag}_status.json" \
      --log "$experiment_dir/${tag}_run.log"
}

case "$1" in
  bits20_28)
    run_one b20_i0 2 14 scale_b20_i0_02_15
    run_one b20_i1 0 16 scale_b20_i1_00_15
    run_one b28_i0 0 16 scale_b28_i0_00_15
    run_one b28_i1 0 16 scale_b28_i1_00_15
    ;;
  bits36_44)
    run_one b36_i0 0 16 scale_b36_i0_00_15
    run_one b36_i1 0 16 scale_b36_i1_00_15
    run_one b44_i0 0 16 scale_b44_i0_00_15
    run_one b44_i1 0 16 scale_b44_i1_00_15
    ;;
  bits60)
    run_one b60_i0 0 8 scale_b60_i0_00_07
    run_one b60_i0 8 8 scale_b60_i0_08_15
    run_one b60_i1 0 8 scale_b60_i1_00_07
    run_one b60_i1 8 8 scale_b60_i1_08_15
    ;;
  bits92_i0)
    run_one b92_i0 1 4 scale_b92_i0_01_04
    run_one b92_i0 5 4 scale_b92_i0_05_08
    run_one b92_i0 9 4 scale_b92_i0_09_12
    run_one b92_i0 13 3 scale_b92_i0_13_15
    ;;
  bits92_i1)
    run_one b92_i1 0 4 scale_b92_i1_00_03
    run_one b92_i1 4 4 scale_b92_i1_04_07
    run_one b92_i1 8 4 scale_b92_i1_08_11
    run_one b92_i1 12 4 scale_b92_i1_12_15
    ;;
  *)
    print -u2 "usage: $0 {bits20_28|bits36_44|bits60|bits92_i0|bits92_i1}"
    exit 2
    ;;
esac
