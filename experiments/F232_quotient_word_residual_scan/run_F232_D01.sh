#!/usr/bin/env bash
set -euo pipefail

mkdir -p /root/F232
/usr/bin/g++ -O3 -std=c++17 /root/F232/F232_D01.cpp -o /root/F232/F232_D01
/usr/bin/timeout 600s /root/F232/F232_D01 \
  /root/F232/D01_OUTPUT.tsv \
  /root/F232/D01_SUMMARY.txt \
  /root/F232/D01_HOSTILE.tsv \
  > /root/F232/D01_RUN.stdout 2> /root/F232/D01_RUN.stderr
/usr/bin/sha256sum \
  /root/F232/F232_D01.cpp \
  /root/F232/run_F232_D01.sh \
  /root/F232/D01_OUTPUT.tsv \
  /root/F232/D01_SUMMARY.txt \
  /root/F232/D01_HOSTILE.tsv \
  /root/F232/D01_RUN.stdout \
  /root/F232/D01_RUN.stderr \
  > /root/F232/D01_SHA256SUMS

