#!/bin/sh
set -eu

uname -a
python3 --version
sage --version
/usr/bin/clang --version
otool -L artifacts/analyze_flint
otool -L artifacts/audit_all_global_rows_flint
