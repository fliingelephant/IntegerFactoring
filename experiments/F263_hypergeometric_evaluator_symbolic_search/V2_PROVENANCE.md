# F263-D02 V2 validation provenance

## Scope

This record covers compile, algebra-only self-test, and one public synthetic
benchmark.  No discovery or held-out cohort was generated, opened, or
hashed.  F263-D01 files and its hostile audit were not edited or deleted.

The exact hostile-audit hash remained:

```text
2e5801933e3eb26b6aa1c3f8cb3e23d5d199297051ae451484cf26d791446099
```

## Host and resource check

The target was `seetacloud`.  Immediately before the final validation it
reported:

```text
UTC:             2026-08-13T16:01:30Z
visible CPUs:    32
load average:    60.81 58.72 58.31
memory:          503 GiB total, 367 GiB available
disk /root:      22 GiB available
```

F258-D01 used one low-priority core and 31,180 KiB RSS.  V2 validation used
one low-priority core.  It did not overlap any other discovery or held-out
process.

## Compile and self-test

The exact source hash was:

```text
05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827
```

The compile command was:

```text
/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread \
  V2_symbolic_search.cpp -o V2_symbolic_search.final
```

Both compiler streams were empty.  The binary hash was:

```text
d8ce872f62c3c488bf22b29899423caad2f287279db144a6488227771766420a
```

The exact self-test output was:

```text
SELF_TEST_PASS controls=12 columns=70 ranks=58,58 nullities=12,12 halves=9801 sparse=14 basis=12,12 shortcuts=0 adjacent=4 dyadic=0 candidates=148 rows=848,1152
```

Status was zero.  Elapsed time was 1.972386473 seconds.  Peak process-tree
RSS was 32,120 KiB.  Stderr was empty.

The targeted checks include:

- both central-binomial parities and the `B=p` cleanup edge;
- the full 9,801-half two-prime sparse search and both nullspaces;
- exact authentication on all 192 generic affine rows;
- four adjacent recurrences authenticated at both primes and exact held-back
  starts;
- both affine families in the dyadic recurrence search;
- typed unit-target dependency acceptance and recursive-merge rejection;
- public `bitlength(N)` query lengths `n` and `n^2`;
- bounded, globally distinct random, safe-safe, and bounded-capacity rows;
- exact cohort counts 848 and 1,152;
- SHA-256 selection-byte acceptance and altered-digest rejection;
- direct-support classification and all four lead gates; and
- exact non-operational oracle/recomputation counts on a small tree.

## Public synthetic benchmark

The exact benchmark output was:

```text
BENCHMARK_PASS seconds=4.995265 modulus_bits=120 blocks=390 leaf_touches=926880 candidates=148 symbolic_columns=70 symbolic_relations=14 shortcuts=0 projected_rows=2000
```

Status was zero.  Wrapper elapsed time was 5.031588949 seconds.  Peak
process-tree RSS was 32,024 KiB.  Stderr was empty.

The fixed public pair has 60-bit factors and a 120-bit product.  The output
therefore authenticates the corrected production query constructor.  V1
incorrectly passed the factor-bit label 60.  V2 passed public
`bitlength(N)=120` and touched 926,880 leaves.

## Conservative resource projection

The exact V2 bank has 848 discovery and 1,152 held-out rows, 2,000 total.
The maximum-size synthetic row took 4.995265 seconds on one core.  The
symbolic search is once per phase, not once per row, but charge it to every
row for a conservative bound:

```text
2000 * 4.995265 / 8 = 1248.82 seconds = 20.82 minutes
```

A factor of eight for host load, deterministic prime generation, output,
and imperfect scaling gives 166.5 minutes.  This remains below the shared
four-hour cap.

The measured one-process peak was 32,120 KiB.  Eight workers at that entire
peak plus 128 MiB for main-thread state, rows, and output buffers is below
385 MiB.  A further factor of four remains below 1.6 GiB.  This is below the
4 GiB virtual-memory cap.  Output contains 2,000 compact row records, two
small summaries, one 64-row selection, and one 64-row lead gate.  It is far
below 1 GiB, and both executable and runner apply the cap.

## Retained evidence

Exact final streams, process-tree monitors, resource snapshot, and remote
hash record are in `V2_TARGET_CHECKS/`.  The local hash of the downloaded
remote `final.sha256` is:

```text
6c478770c9bac50fa2001c5660006aba6cb571fb95943f26d1601a9634c15a43
```

This validation is not a hostile audit and does not authorize a cohort.
