#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
sage_prefix=/Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/10.9/local
cxx=/usr/bin/clang++
flags=(-std=c++20 -O3 -DNDEBUG -pthread -I"$sage_prefix/include")
links=(-L"$sage_prefix/lib" -Wl,-rpath,"$sage_prefix/lib" -lflint)

"$cxx" "${flags[@]}" "$root/src/generate_global.cpp" "${links[@]}" -o "$root/build/generate_global"
"$cxx" "${flags[@]}" "$root/src/verify_complete.cpp" "${links[@]}" -o "$root/build/verify_complete"
"$cxx" "${flags[@]}" "$root/src/spot_audit.cpp" "${links[@]}" -o "$root/build/spot_audit"

