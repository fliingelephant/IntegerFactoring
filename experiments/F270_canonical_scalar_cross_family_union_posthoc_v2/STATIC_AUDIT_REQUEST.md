# F270-D02 static hostile audit request

Review the frozen packet before any compile, self-test, preflight, target, or
remote execution. Authenticate every `FROZEN.sha256` record first. Give one
literal verdict: `PASS`, `REVISE`, or `INVALID`.

The D01 arithmetic audit passed, but D01 launch was prohibited by audit
SHA-256
`74c9c078b94a89f81db7891c2d51546978087895c8265b23196aa2c870c3f730`.
Confirm that D02 preserves the approved mathematics and repairs every D01
blocker.

At minimum, check these points:

1. The implementation joins F268's global evidence `case_index` to corpus
   position and does not confuse it with cell-local public `index`.
2. It reads only `ROW` records for arithmetic. It never reads or concatenates
   prior per-family `BLOCK` records.
3. It compares all supplied-root pairs in an equal exact-value class before
   deduplication.
4. It recomputes one pairwise-coprime opaque block system from global
   deduplicated values and verifies reconstruction.
5. Original union rank expands deduplicated columns through all provenance.
   Each family rank independently replays as full.
6. Peeling marks all current degree-one rows in one round, deletes them
   simultaneously, and continues to a fixed point.
7. Singleton and support-two scans use only the fixed core. The residual
   quotient is complete when no useful low relation exists.
8. Every emitted relation verifies an exact positive square root, supplied
   modular root, normalized root, both signed gcds, and root class.
9. Clean/control labels use only public bank-table `earlier_factor`.
   Controls cannot create a held-out trigger.
10. Empty core in all target cases produces the literal seam-kill status.
11. The 100,000-bit cap covers all 284 original serialized rows before
    deduplication. The 1,000,000 refinement cap is aggregate per case across
    the union and core decoders.
12. A shared lock reserves one global relation slot, its exact final TSV line
    bytes, and total output bytes before any relation-vector append. Failed
    reservations append nothing. The per-case, global-count, 96-MiB payload,
    1-MiB line/buffer, and total-output caps all fail closed under eight
    workers. A shared cancellation bit stops concurrent relation generation
    after any reservation failure.
13. Serialization retains only one batch of at most eight case results,
    streams final TSVs in deterministic global case order, reserves every
    nonrelation line before write, keeps only bounded aggregates/witnesses,
    and verifies final file bytes equal its exact ledger.
14. After fail-closed admission, one monotonic absolute 14,400-second deadline
    covers process capture, compile, self-test, preflight, target, compression,
    resource capture, and final manifest. Target arithmetic ends 600 seconds
    early; archives end 120 seconds early; a watchdog kills the cgroup at the
    deadline.
15. Cgroup-v2 `memory.max=3,758,096,384`, swap zero, 4-GiB `RLIMIT_AS`,
    384-MiB `RLIMIT_FSIZE`, exact raw-output budgets, bounded logs, packet
    byte gates, and the compression transient inequality form a fail-closed
    containment envelope.
16. The generic exclusive production lock and complete bounded process scan
    are noninteractive. The scan excludes only the exact ancestor chain and
    deadline watchdog, occurs before any workload child, rejects overlap or
    snapshot overflow, and binds its SHA/firewall PASS into evidence. The lock
    remains authoritative for cooperating packets until finalization.
17. The runner authenticates the operator-supplied frozen root and fresh PASS
    audit sidecar before compilation. Each raw tree includes exact per-file
    hashes. Tar/gzip metadata are deterministic. Archive hashes enter the run
    manifest; the final manifest hashes all prior final files.
18. No direct gcd screen exists outside input/relation authentication.

Compile mentally for C++ type, move/copy lifetime, mutex, reservation,
thread-exception, empty-core, exact-duplicate, all-global-low-span, streaming,
file-close, archive-pipeline, Bash `set -euo pipefail`, timeout, cgroup
cleanup, output-order, and witness errors. Do not compile or execute the
packet during this audit.

If and only if the verdict is PASS, write nonpacket sidecars with these exact
machine-readable lines in `HOSTILE_PRERUN_AUDIT.md`:

```text
verdict: PASS
frozen_manifest_sha256: <literal SHA-256 of FROZEN.sha256>
```

The report may contain further prose. Write
`HOSTILE_PRERUN_AUDIT.sha256` as one standard `sha256sum` record naming
`HOSTILE_PRERUN_AUDIT.md`. Dynamic work remains prohibited until both
sidecars authenticate.
