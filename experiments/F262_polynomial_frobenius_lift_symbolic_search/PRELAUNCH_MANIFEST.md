# F262-D01 prelaunch manifest

Status: frozen, compile-validated, execution-validation pending.

Reserved experiment ID: `F262-D01`.

Target compile: passed with `/usr/bin/g++ -std=c++17 -O2 -pthread` on
`seetacloud`. The final compile emitted no diagnostic.

Mathematical execution: none. F258-D01 remained active. Therefore F262's
declared incompatibility gate prohibited `--self-test`, `--benchmark`, the
discovery cohorts, and the held-out cohorts.

Frozen source facts:

```text
C++ source lines: 732
static families: 48
planned inputs: 5,280
threads: at most 8
virtual-memory limit: 4 GiB
uncompressed output limit: 1 GiB
hard cohort timeout: 14,400 seconds
```

Pre-freeze target resources observed at `2026-08-13T15:11:24Z`:

```text
32 allowed CPUs (96-127)
load average 57.54,57.99,57.76
503 GiB RAM; 367 GiB available; no swap
22 GiB free disk
F258-D01 active at nice 15
```

Artifact hashes before this manifest:

```text
df6d4383fc76a8e37ef65068e057245334dc6d58489035c35dd4937f0971f78f  PREREGISTRATION.md
6b6c57cb6d1435f4121a90ab8c0fef1b833d73d72fa6875941228ba582bcd832  ALGEBRA.md
d21828bef2196188daa50dfa65875de0de67ddd0a0b7302c290ee939d8b854c6  symbolic_search.cpp
d406bff3baed85228580a35fafa98927c86dce6400bf67d9409a1004dd945e1d  remote_run.sh
964b319db85205a95520eae5361cfcfae84a75283294d40176ccf4cda3f91e44  FAILED_COMPILE.md
5339b335cb2b6e0dec5a066f740a1d736e37317a92f9157d931046b4d6497d96  BUILD.md
fcf0ba4c7dbdbb4c1f0b2d11284b8d99a1f652dc373ef3fdaeebcf66ef3c0982  VALIDATION_PENDING.md
```

The runner must satisfy every gate in `VALIDATION_PENDING.md` after all
incompatible jobs end. A failed gate invalidates the packet. It does not
authorize a source, grammar, cohort, threshold, or interpretation change.

No durable ledger was edited.
