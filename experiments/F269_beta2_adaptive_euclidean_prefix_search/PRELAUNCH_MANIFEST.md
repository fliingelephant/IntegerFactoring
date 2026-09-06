# F269-D01 prelaunch manifest

## Status

This is an unexecuted C++17 packet. The bytes listed in `FROZEN.sha256` are
the only bytes proposed for the static hostile audit. A `PASS` audit must name
the SHA-256 of `FROZEN.sha256` in `HOSTILE_PRERUN_AUDIT.md`. The runner refuses
to compile without that exact authentication.

## Entry points

The source has these modes:

```text
--self-test BASELINES
--grammar-once
--max-work-round W ROUND
--serialization-write EVIDENCE ABSOLUTE_PATH
--splitmix-stream-write EVIDENCE ABSOLUTE_PATH
--checked-truncate EVIDENCE ABSOLUTE_PATH
--gate METRICS E_GATE_NS EVIDENCE OUTPUT
--discovery BASELINES EVIDENCE W
--heldout BASELINES EVIDENCE W SELECTION SELECTION_SHA DISCOVERY_CORPUS_SHA
```

The runner has two explicit modes:

```text
remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY preflight
remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY complete
```

`preflight` stops after compile, exact self-tests, seven grammar timings, four
maximum-work rounds, seven maximum serializations, seven compression timings,
and the readiness gate. `complete` performs the same gates and continues to
discovery and heldout. It does not provide a shortened cohort mode.

## Exact finite work

```text
root syntax attempts                         444
tuple attempts                            5,120
maximum final syntax count                5,564
selector orientations                    11,128
direct discovery families                 1,024
selected selector rules                     192
selected heldout direct families             64
discovery primary moduli                     896
heldout primary moduli                     1,280
all primary moduli                         2,176
discovery stage rows                      10,752
heldout stage rows                        30,720
all primary stage rows                    41,472
discovery direct-ticket cap           44,040,192
heldout direct-ticket cap              7,864,320
all direct-ticket cap                  51,904,512
child factorizations                           0
characteristic-size scans                       0
```

The source asserts grammar partitions, stage counts, selection counts, ticket
partitions, baseline counts, witness caps, certificate replay, and label
conversion. The cohort generator is stateless. Its word is the seven-field
fold from the preregistration. It uses the exact random, close-hard, edge, and
safe-safe constructors and their registered caps.

## Selection orders

Selector order is exactly: invalid rows ascending; minimum shape balanced
accuracy descending; exact cells descending; total balanced accuracy
descending; errors ascending; typed layer ascending; node count ascending;
canonical syntax ascending; orientation ascending. Accuracy comparisons use
integer cross-products.

Direct order is exactly: hit moduli descending; hit factor sizes descending;
hit shapes descending; proper ticket count descending; invalid ticket count
ascending; typed layer ascending; node count ascending; canonical syntax
ascending.

The heldout mode authenticates the 256 selection rows, reconstructs each
selected syntax from the frozen grammar, authenticates the discovery corpus,
and only then generates the heldout cohort.

## Evidence schemas

The complete mode writes the thirteen registered semantic outputs from
Preregistration Section 10. It also writes the frozen grammar table, the
worker choice, preflight measurements, logs, compression map, and final hash
list under one evidence directory. Corpus rows contain both root-valid masks,
packed-root-reason digests and histograms, tail-alias IDs and digests,
expression-reason digests and histograms, value-alias digests, and
invalid-reason-mask digests. Rule rows contain complete exact cell aggregates.
Direct rows contain the complete six-way ticket partition. Witnesses use only
the registered bounded retention rules. Every retained proper certificate is
replayed from public `(N,t,u,syntax)` before evidence closes.

Record-size assertions are 2,048 bytes for primary corpus and certificate
records, 8,192 bytes for rule and selection records, and 1,024 bytes for
registered small records. The maximum serialization fixture is exactly
277,979,136 bytes.

## Whole-run resource gate

The runner requires a delegated cgroup-v2 leaf. It writes and reads back:

```text
memory.max      3758096384
memory.swap.max 0
```

It sets exact process limits:

```text
RLIMIT_AS       4294967296 bytes
RLIMIT_FSIZE     536870912 bytes
```

It starts a 14,400-second cgroup watchdog. Every source invocation receives
the remaining time to the 14,370-second source deadline. It chooses one
worker count from `{1,2,4,8}` before validation and reuses it. It rejects an
active F265 process before every phase. It checks load, memory, five GiB free
disk, symlinks, hard links, sparse evidence, per-component budgets, regular
bytes, and GNU `du --apparent-size`.

The measured gate uses integer nanoseconds and the exact formulas in
Preregistration Section 11. It requires the 10,800-second engineering total,
the five-quarters memory projection below 3.5 GiB, process RSS agreement
within 64 MiB, the 512 MiB evidence cap, and five GiB free disk.

## Execution state

```text
local compile                 NOT RUN
remote compile                NOT RUN
exact self-tests              NOT RUN
stress preflight              NOT RUN
discovery cohort              NOT RUN
heldout cohort                NOT RUN
static hostile pre-run audit  PENDING
```

