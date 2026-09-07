#!/bin/zsh
set -eu

cd "${0:A:h:h:h}"
experiment_dir="experiments/F332_minus_one_paths"
source_path="$experiment_dir/minus_one_paths.py"

run_job() {
  local tag="$1"
  shift
  env PYTHONHASHSEED=0 \
      OPENBLAS_NUM_THREADS=1 \
      OMP_NUM_THREADS=1 \
      VECLIB_MAXIMUM_THREADS=1 \
    gtimeout 30 python3 "$source_path" "$@" \
      --output "$experiment_dir/${tag}_output.json" \
      --status "$experiment_dir/${tag}_status.json" \
      --log "$experiment_dir/${tag}_run.log"
}

case "$1" in
  initial_remaining)
    for modulus_id in b28_i1 b36_i0 b44_i0 b44_i1 b60_i1 b92_i0; do
      run_job "initial_${modulus_id}" \
        --mode public --modulus-id "$modulus_id" \
        --fine-cap 8192 --block-cap 8192
    done
    ;;
  extended_censors)
    for modulus_id in b36_i0 b44_i0 b44_i1 b60_i1 b92_i0; do
      run_job "extended_${modulus_id}" \
        --mode public --modulus-id "$modulus_id" \
        --fine-cap 262144 --block-cap 262144
    done
    ;;
  *)
    print -u2 "usage: $0 {initial_remaining|extended_censors}"
    exit 2
    ;;
esac
