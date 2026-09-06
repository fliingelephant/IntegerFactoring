# Preserved local compile attempt

The local Mac command

```text
clang++ -std=c++17 -fsyntax-only symbolic_search.cpp
```

failed before parsing the source because the local toolchain does not contain
`boost/multiprecision/cpp_int.hpp`. No source conclusion follows. The
authoritative target compile uses `/usr/bin/g++` on `seetacloud`, where Boost
is available. No mathematical mode was run locally.
