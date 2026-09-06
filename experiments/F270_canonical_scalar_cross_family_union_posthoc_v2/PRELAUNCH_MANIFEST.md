# F270-D02 prelaunch manifest

## Classification and lineage

`F270-D02` is a post-hoc discovery analysis. It reuses only public F268-D04
discovery records. It does not read hidden factors. It does not run a held-out
test. Its output can propose a later held-out packet only under the firewall in
`POSTHOC_PROTOCOL.md`.

D02 preserves the D01 arithmetic chronology. D01 manifest root
`4fe9f85f7a52f7e6fce505d6165cd223e4ec394de5c536dfca6bc474398efe2f`
was rejected only for the resource blockers in the D01 hostile pre-run audit,
SHA-256
`74c9c078b94a89f81db7891c2d51546978087895c8265b23196aa2c870c3f730`.

## Frozen packet

The executable packet consists of:

- `POSTHOC_PROTOCOL.md`: exact theory provenance, arithmetic order, outputs,
  interpretation, and resource gates.
- `RESOURCE_ESTIMATE.md`: static work, time, memory, and disk estimates.
- `f270_union.cpp`: C++17 authenticated replay and bounded P66 union analyzer.
- `remote_run.sh`: fail-closed Linux compile, self-test, preflight, projection,
  target, archive, and hash runner.
- `PRELAUNCH_MANIFEST.md`: this manifest.
- `STATIC_AUDIT_REQUEST.md`: hostile static review checklist.
- `FROZEN.sha256`: hashes of all files above except itself.

No frozen packet file can change after `FROZEN.sha256` is created. A required
repair creates a new packet version. Compile and self-test occur only after
freezing and after a fresh hostile audit PASS.

The hostile auditor writes `HOSTILE_PRERUN_AUDIT.md` and
`HOSTILE_PRERUN_AUDIT.sha256` as nonpacket sidecars. The runner authenticates
the sidecar, requires literal `verdict: PASS`, requires its literal frozen
manifest root, and requires the operator to supply that same root on the
command line. The audit sidecars cannot change any executable byte.

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

On the reviewed Linux host, invoke:

```text
bash remote_run.sh EVIDENCE BANKS CORPUS ABSOLUTE_NEW_RUN_DIR WORKERS APPROVED_FROZEN_ROOT
```

The runner verifies its packet, the approved root, the PASS audit sidecar, and
all three input hashes. It acquires the generic exclusive
`/tmp/integer_factoring.production.lock` and admits the host and cgroup. It
then starts one monotonic 14,400-second deadline before process capture or
compilation. It creates and hashes a bounded PID-sorted process snapshot and
rejects any recognized production overlap or snapshot overflow. This scan
occurs before any workload child exists. The exclusive lock is then the
authoritative non-overlap mechanism for the full packet lifetime.

The runner requires at least 8 GiB available RAM, 4 GiB free disk, and enough
idle load capacity for the requested workers. It creates a cgroup-v2 workload
envelope with a 3.5-GiB memory ceiling and no swap. It also applies 4-GiB
`RLIMIT_AS` and 384-MiB `RLIMIT_FSIZE`.

Compilation uses:

```text
g++ -O3 -DNDEBUG -std=c++17 -pthread f270_union.cpp
```

The runner executes the immutable self-test. It then runs the deterministic
eight-case preflight under `nice -n 15`. Factor-four projected wall time must
fit the current time remaining before the 600-second closure reserve.
Factor-four RSS must fit the cgroup, and factor-four raw output must fit
192 MiB. Only those gates can start the 188-case target.

Target arithmetic must finish by absolute deadline minus 600 seconds.
Deterministic target compression and raw-file removal must finish by deadline
minus 120 seconds. Resource capture and final hashing must finish before the
absolute deadline. The watchdog kills the workload cgroup at the hard
deadline.

## Output and evidence contract

The raw preflight and target trees each contain
`RUN_METADATA.tsv`, `metadata.tsv`, `cases.tsv`, `rows.tsv`,
`blocks.tsv`, `peeling.tsv`, `relations.tsv`, `aggregates.tsv`,
`witness.tsv`, `summary.tsv`, an exact per-file SHA-256 manifest, and a
SHA-256 record for that manifest itself.
GNU tar uses USTAR format, sorted names, epoch mtime, numeric owner zero, and
group zero. The runner fixes `umask 022`, clears archive option environments,
and uses the C locale. GNU gzip uses `-n -6`. Thus equal raw bytes produce
equal archive bytes on the frozen host toolchain.

The final run directory contains deterministic preflight and target
`.tar.gz` archives, bounded phase logs, resource and process snapshots,
process-firewall acknowledgement, timings, projections, executable hash, a run
manifest that binds both archive hashes, and `F270-D02.final.sha256` over all
prior final packet files.

The analyzer aborts instead of returning a mathematical null if an input,
arithmetic, reconstruction, rank, completeness, reservation, relation,
serialization, or resource check fails. A runner timeout, containment event,
overlap, output breach, archive error, or incomplete final manifest likewise
creates no mathematical result.
