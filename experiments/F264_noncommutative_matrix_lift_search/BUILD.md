# F264-D01 target compile status

Read-only target inspection at `2026-08-13T15:37:55Z` found:

```text
32 allowed CPUs (96-127)
load average 57.26,57.32,57.70
503 GiB RAM; 367 GiB available; no swap
22 GiB free disk
F258-D01 active at nice 15
```

The final F264 source compiled successfully on `seetacloud` with

```text
/usr/bin/g++ -std=c++17 -O2 -pthread symbolic_search.cpp \
  -o symbolic_search.compilecheck
```

Compilation emitted no diagnostic. Compilation was allowed by the preparation
protocol. Because F258-D01 was active and F264 is incompatible with F258--F263,
the binary was not executed. No describe mode, self-test, benchmark, discovery
input, or held-out input was opened.
