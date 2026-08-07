#!/bin/sh
set -eu

DOT_SAGE=/Users/zhou/autoresearch/IntegerFactoring/experiments/F60_generic_specialization_decoy_reconstruct/.sage
export DOT_SAGE
mkdir -p "$DOT_SAGE"

exec /usr/local/bin/sage -python \
  /Users/zhou/autoresearch/IntegerFactoring/experiments/F60_generic_specialization_decoy_reconstruct/verify_d02_sage.py \
  --input /Users/zhou/autoresearch/IntegerFactoring/experiments/F59_completion_bias_generic_decoder_scan/output/F59-D02.json \
  --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F60_generic_specialization_decoy_reconstruct/verify_d02_sage_v4_output.json \
  --log /Users/zhou/autoresearch/IntegerFactoring/experiments/F60_generic_specialization_decoy_reconstruct/verify_d02_sage_v4.log
