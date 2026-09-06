# F264-D03 V3 frozen prelaunch manifest

Frozen on 2026-08-14 before the first V3 compile or any V3 execution.

## Status

**DO NOT LAUNCH pending a fresh independent hostile pre-run audit.**

F264-D03 is a narrow immutable operational repair. F258-D01 was active during
preparation. No V3 compile, self-test, benchmark, description, cohort, or score
was opened. V1, V2, and both hostile FAIL audits remain unchanged.

## Frozen V3 core hashes

```text
a102c9623b113cd28563a1d4552ed6fd8f05e32c56aa61f972d85a1f79cbdb14  V3_ALGEBRA.md
20b31fe7ddc8b3146cec16b67cceb5ebb66ac540fd3bb7ebfdda3d3f8f552370  V3_PREREGISTRATION.md
b76812ba8966eabceee4a42340910701aab89ca163e5d2a00b74494ad4df9de3  V3_symbolic_search.cpp
b10db23daa7d2401a3fb006f232a9c1239b2e4acd9cc467608a82320579320b5  V3_remote_run.sh
cb1bffb63aed35975a32a0baa27b7bc5283aaa10395cbb3c81ee987a5947c7a7  V3_VALIDATION_PENDING.md
0ea0401d4e42b7ba0d96a6042c4eb8e6405f02ff5846a02df6b1926ecfe8c6f9  V3_AUDIT_REQUEST.md
1cadb086cca3d73ec72b1f9b85dc2016b70e89cafde12b228c6821f3bda611ba  V3_STATIC_VALIDATION.md
```

`V3_FROZEN.sha256` authenticates these files and this manifest. The manifest
cannot contain its own final hash without a cycle.

## Immutable provenance

The preserved packet roots and FAIL audits authenticated before V3 work:

```text
23d7aa6bd72f9cb7cf66b63ea9680fbd3adabcd4b543150929b249d8b0a2bb22  FROZEN.sha256
f00fee9eac5fb71c9403d0f3a39b8cbf0bb0eb5682d6776f5eca1d26e21e3c9c  HOSTILE_PRERUN_AUDIT.md
52cb03a726c0ba26c79ad215971b6f72ec72199c50dac22f062f8016356255e0  V2_FROZEN.sha256
4206516a9ee14b831db4f3d9c148052f990faf209ffacf2673518f8de9eaf51a  V2_HOSTILE_PRERUN_AUDIT.md
```

## Narrow repair map

- The order scope is exactly eight main words and one cyclic control per
  profile, tested against two schedules: 36 global trials per input.
- Every trial evaluates all 14 ordered root proposals before it can return.
  Rows preserve 504 checks, 14 per-index counts, outcome totals, and a compact
  deterministic transcript hash. A proper gcd is acted on only after the full
  proposal loop.
- The row report adds exactly 19 fields, from 2,541 to 2,560. The validator
  reconstructs the full ordered header and exact nested JSON schemas, names,
  cells, candidate IDs, decoys, and root counts.
- Checksum authentication and every report parser now use the same monitored
  child envelope as compile, production, validation, and compression. Manifest
  construction is also monitored and precedes the final monitored aggregate
  size and deadline gate.

No algebraic formula, public source seed, generator, word, sparse pair/triple
scope, family atom, candidate expression, cohort, P205 program, order schedule,
lead threshold, or hidden-label boundary changed. No durable ledger was edited.

Static checks before freeze were `bash -n`, embedded-Python AST parsing,
`git diff --check`, exact schema arithmetic, full V2-to-V3 source-diff review,
and V1/V2 hash authentication. Dynamic target validation remains mandatory.
