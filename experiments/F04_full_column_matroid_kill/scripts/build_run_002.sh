#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd); prefix=/Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/10.9/local
/usr/bin/clang++ -std=c++20 -O3 -DNDEBUG -I"$prefix/include" "$root/src/certify_all.cpp" \
  -L"$prefix/lib" -Wl,-rpath,"$prefix/lib" -lflint -o "$root/build/certify_all"

