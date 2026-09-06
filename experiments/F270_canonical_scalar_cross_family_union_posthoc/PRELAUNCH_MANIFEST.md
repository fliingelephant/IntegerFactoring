# F270-D01 prelaunch manifest

## Classification

`F270-D01` is a post-hoc discovery analysis. It reuses only public F268-D04
discovery records. It does not read hidden factors. It does not run a held-out
test. Its output can propose a later held-out packet only under the firewall in
`POSTHOC_PROTOCOL.md`.

## Frozen packet

The executable packet consists of:

- `POSTHOC_PROTOCOL.md`: exact theory provenance, arithmetic order, outputs,
  interpretation, and resource gates.
- `RESOURCE_ESTIMATE.md`: static work, time, memory, and disk estimates.
- `f270_union.cpp`: C++17 authenticated replay and P66 union analyzer.
- `remote_run.sh`: fail-closed Linux compile, self-test, preflight, projection,
  target, and hash runner.
- `PRELAUNCH_MANIFEST.md`: this manifest.
- `STATIC_AUDIT_REQUEST.md`: hostile static review checklist.
- `FROZEN.sha256`: hashes of all files above except itself.

No packet file can change after `FROZEN.sha256` is created. A required repair
creates a new packet version. Compile and self-test occur only after freezing.

## Authenticated inputs

The runner and executable independently authenticate:

```text
a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc  F268-D04.discovery.evidence.tsv
c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6  F268-D04.discovery.banks.tsv
8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5  F268-D04.discovery.public.tsv
```

The executable also requires 188 cases, 2,256 eligible full-rank banks, 284
rows per case, valid exact row replay, and exactly 125 clean cases.

## Dynamic sequence

On the reviewed remote host, invoke:

```text
bash remote_run.sh EVIDENCE BANKS CORPUS NEW_RUN_DIR 8
```

The runner verifies the packet and input hashes. It records load, memory,
disk, and processes. It stops on an F265/F269 overlap, less than 8 GiB
available RAM, or less than 4 GiB free disk. A human must also confirm that
the captured process list contains no other production run.

It compiles with:

```text
g++ -O3 -DNDEBUG -std=c++17 -pthread f270_union.cpp
```

It runs the immutable self-test. It then runs the deterministic eight-case
preflight under `nice -n 15`. It applies a factor-four projection to wall
time, live memory, and output. It stops above four hours, 4 GiB, or 512 MiB.
Only a passing preflight can start the 188-case target. The target has a hard
14,400-second timeout and uses no more than eight workers.

## Output contract

The target directory contains `metadata.tsv`, `cases.tsv`, `rows.tsv`,
`blocks.tsv`, `peeling.tsv`, `relations.tsv`, `aggregates.tsv`, `witness.tsv`,
and `summary.tsv`. The run directory also contains compile/self-test logs,
resource snapshots, measured preflight and target resources, projections,
the executable hash, and a pre-manifest hash inventory.

The analyzer aborts instead of returning a mathematical null if an input,
arithmetic, reconstruction, rank, completeness, relation, or resource check
fails.
