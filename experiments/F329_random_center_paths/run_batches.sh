#!/bin/zsh
set -eu

cd "${0:A:h:h:h}"

experiment_dir="experiments/F329_random_center_paths"
source_path="$experiment_dir/random_center_paths.py"

run_scale_batch() {
  local modulus_id="$1"
  local query_start="$2"
  local tag="$3"
  env PYTHONHASHSEED=0 \
      OPENBLAS_NUM_THREADS=1 \
      OMP_NUM_THREADS=1 \
      VECLIB_MAXIMUM_THREADS=1 \
    gtimeout 30 python3 "$source_path" \
      --mode run \
      --dataset scale \
      --modulus-id "$modulus_id" \
      --query-start "$query_start" \
      --queries 8 \
      --replicates 4 \
      --max-cap 1024 \
      --run-label scale \
      --output "$experiment_dir/${tag}_output.json" \
      --status "$experiment_dir/${tag}_status.json" \
      --log "$experiment_dir/${tag}_run.log"
}

case "$1" in
  bits20)
    run_scale_batch b20_i0 0 scale_b20_i0_q00_07
    run_scale_batch b20_i0 8 scale_b20_i0_q08_15
    run_scale_batch b20_i1 0 scale_b20_i1_q00_07
    run_scale_batch b20_i1 8 scale_b20_i1_q08_15
    ;;
  bits28)
    run_scale_batch b28_i0 0 scale_b28_i0_q00_07
    run_scale_batch b28_i0 8 scale_b28_i0_q08_15
    run_scale_batch b28_i1 0 scale_b28_i1_q00_07
    run_scale_batch b28_i1 8 scale_b28_i1_q08_15
    ;;
  bits36)
    run_scale_batch b36_i0 0 scale_b36_i0_q00_07
    run_scale_batch b36_i0 8 scale_b36_i0_q08_15
    run_scale_batch b36_i1 0 scale_b36_i1_q00_07
    run_scale_batch b36_i1 8 scale_b36_i1_q08_15
    ;;
  *)
    print -u2 "usage: $0 {bits20|bits28|bits36}"
    exit 2
    ;;
esac
