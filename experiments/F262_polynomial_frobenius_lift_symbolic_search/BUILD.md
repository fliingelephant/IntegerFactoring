# Target compile status

Read-only target inspection at `2026-08-13T15:11:24Z` found:

```text
32 allowed CPUs (96-127); load average 57.54,57.99,57.76
503 GiB RAM; 367 GiB available; no swap
22 GiB free disk
F258-D01 active at nice 15
```

The corrected F262 source compiled successfully on `seetacloud` with:

```text
nice -n 15 /usr/bin/g++ -std=c++17 -O2 -pthread symbolic_search.cpp -o symbolic_search
```

Compilation emitted no diagnostic. Because F258-D01 was active and F262 is
declared incompatible with F258-F261, the binary was not executed. No
self-test, benchmark, discovery input, or held-out input was opened.
