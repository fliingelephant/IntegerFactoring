# F270-D03 post-hoc protocol — canonical scalar cross-family union

## Status and provenance

This is a discovery-only, post-hoc hypothesis-generation experiment. It is
not a preregistered test, a held-out test, an asymptotic statement, or a
factoring theorem.

The input is the authenticated F268-D04 discovery evidence. F268-D04 tested
each source family as a separate bank. Its independent result audit found a
nonsquare private parity pivot for every row in every separate bank. The same
audit explicitly left a same-modulus cross-family union open and required the
opaque block system to be rebuilt from the union row values.

The hostile theory review of this follow-up was conversation-only. It has no
artifact hash. Its verdict was `REVISE`, with the following mandatory repair:

- A union can create a dependency even when every component bank is full
  rank. At `N=697=17*41`, the rows `(U,Y)=(2,550)` and `(8,403)` are each
  privately pivoted alone, but their union has the square relation
  `2*8=4^2`. The supplied-root product is `550*403 = 4 (mod 697)`, so this
  particular cross-family dependency is a global `+1` decoy.
- For family matrices `V_f`, the cross-family quotient obeys

  ```text
  K_union / direct_sum_f K_f
      ~= {(s_f) in direct_sum_f im(V_f) : sum_f s_f = 0},
  dim gain = sum_f rank(V_f) - rank(V_union).
  ```

- Exact roots must be compared before exact-value deduplication.
- Per-family F268 `BLOCK` records must never be concatenated. The union must
  be refined from its `ROW` integer values.
- The union must undergo exhaustive simultaneous degree-one peeling to its
  fixed point before singleton, support-two, and residual P66 decoding.

The closest promoted routes are P66, P106, P108, and P109. This experiment
differs materially from F268 because it unites all twelve independently
generated row layers before refinement. It differs from P108/P109 because it
tests the canonical scalar-section source rather than their prior relation
layers.

F270-D01 froze the same arithmetic design under manifest root
`4fe9f85f7a52f7e6fce505d6165cd223e4ec394de5c536dfca6bc474398efe2f`.
Its hostile pre-run audit, SHA-256
`74c9c078b94a89f81db7891c2d51546978087895c8265b23196aa2c870c3f730`,
passed the mathematical and specification checks but prohibited launch. D01
reserved neither global relation bytes nor the complete packet resources
before use. It also lacked a whole-packet deadline and hard containment. D02
preserved the D01 arithmetic chronology and repaired only these resource and
evidence-lifecycle defects. D02 froze under manifest root
`91468b7190d3b1feb88f644fd3b1d7f95d1dbb462c41a980d8b88d2c1fbeccdf8c`.
Its hostile audit, SHA-256
`1a5b62fec6ab10c411a1f60270f866dd9bd6d8a3ab8b40919032758344c23739`,
accepted the arithmetic and resource repairs but prohibited launch because
the process firewall could miss a generically named legacy `remote_run.sh`
and could silently truncate its ancestor exclusion at depth 16.

D03 preserves the D02 analyzer's arithmetic and resource code. Its only
analyzer edit changes the serialized version label from `F270-D02` to
`F270-D03`. D03 changes no arithmetic, workload, containment, deadline, or
output budget. It replaces only the prelaunch process firewall and the
evidence fields that authenticate that firewall.

## Frozen inputs

The exact local inputs are:

```text
F268-D04 discovery evidence
  SHA-256 a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc
F268-D04 discovery bank table
  SHA-256 c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6
F268-D04 discovery public corpus
  SHA-256 8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5
F268-D04 hostile result audit
  SHA-256 75597f68751d20ff599d68724c06182e964d935132917214a06cf653c778ee97
```

Only `ROW` records from the evidence enter the arithmetic search. The bank
table supplies the already-public `earlier_factor` control label. The public
corpus supplies `N`. Hidden factor labels do not enter this process.

The program must authenticate all 188 cases, all twelve families per case,
and exactly

```text
11*24 + 20 = 284
```

original rows per case. It must find exactly 125 cases with no earlier factor
in any family. These are the preferred clean cohort. It must also process the
remaining 63 factor-bearing cases as controls. A mismatch aborts the packet.

## Frozen arithmetic chronology

For each modulus, process all families together in family-ID and row-ID order.

1. Validate every serialized row identity, canonical range, digit
   decomposition, and supplied square-root congruence.
2. Group equal exact integer values across all families. Before deleting any
   copy, compare every pair of supplied roots as an exact support-two square
   relation. Record its exact positive root, supplied root, normalized root,
   both signed gcds, root class, and full provenance. A non-global mismatch is
   a valid P66 factor certificate. Retain the first occurrence only after all
   pair comparisons finish. Attach every discarded occurrence to its retained
   row as provenance.
3. Starting only from the deduplicated union integer values, repeatedly use
   gcd and exact division until all opaque blocks are pairwise coprime. Never
   read or concatenate an F268 per-family `BLOCK` list. Verify exact row
   reconstruction from the new blocks.
4. Build one parity equation for every nonsquare opaque block. Compute the
   original/deduplicated union rank and nullity. Independently restrict the
   same global equations to each original family, verify all twelve separate
   ranks, and compute the cross-family dimension gain.
5. Apply saturated private-primary peeling. In one round, mark every active
   row that is the unique odd incident row of at least one nonsquare opaque
   block. Delete all marked rows simultaneously. Repeat until no such row
   remains. Record every round, row, and witnessing block. This is exhaustive
   degree-one peeling, not a greedy heuristic.
6. On the fixed core only, recompute and authenticate a complete factor-free
   P66 decoder. Enumerate every singleton and every support-two rational
   square relation. Put only verified `GLOBAL_PLUS` and `GLOBAL_MINUS` low
   relations into the low-support decoy span.
7. If a useful low-support relation exists, record the terminal certificate
   and authenticate the complete core kernel; no residual quotient is needed.
   Otherwise, extend the global low-support span to a basis of the complete
   kernel and compare the root of every quotient-basis vector. This is the
   complete P66 test for the fixed core.

There are no new direct screens. Gcds with `N` occur only for input
authentication or for exact square-relation root comparisons. This is a
P66-only post-hoc discovery run.

## Frozen definitions

`original_rows` is 284. `dedup_rows` is the number after global exact-value
deduplication. `peeled_rows` is the number deleted by saturated peeling.
`core_rows = dedup_rows - peeled_rows`.

The imported separate-bank baseline is also reconstructed from the global
block system by restricting its parity equations to each family. Let
`r_f` be those ranks and `r_U` the original union rank. Then

```text
cross_dimension_gain = sum_f r_f - r_U.
```

The program must verify that each family has its full F268 row rank. Exact
value duplicates contribute `original_rows-dedup_rows` kernel directions.
The post-dedup cross gain is the deduplicated nullity.

A deduplicated row is `union-private` if it has a degree-one nonsquare block
before peeling. The deduplicated private-pivot loss is

```text
private_pivot_loss = dedup_rows - union_private_rows.
```

The original-row loss expands this through each retained row's complete
provenance. Both values are serialized.

A relation is `PURE_FAMILY` only when all original provenances in its support
have one family ID. Otherwise it is `CROSS_FAMILY`. This conservative rule
keeps an exact-value group spanning families visibly cross-family.

For every tested relation `c`, serialize

```text
R = positive_integer_sqrt(product U_i),
X = product Y_i mod N,
rho = R * X^(-1) mod N,
g_minus = gcd(R-X,N),
g_plus  = gcd(R+X,N).
```

The root class is `GLOBAL_PLUS`, `GLOBAL_MINUS`, or `USEFUL`. Any other class
is a fatal arithmetic error.

## Frozen outputs

Both preflight and target modes write deterministic TSV files:

- `cases`: per-case original, deduplicated, peeled, and core row counts;
  original/deduplicated/core rank and nullity; twelve-family rank sum;
  cross-dimension gain; separate and union private coverage; both pivot-loss
  counts; relation counts; and clean/control status.
- `rows`: every retained union row with exact `U`, supplied `Y`, canonical
  source metadata, and all original family/row/base/exponent/root/syntax
  provenance.
- `blocks`: every globally recomputed opaque block, square label, complete
  sparse exponent vector, initial union degree, and final core degree.
- `peeling`: every removed row, simultaneous round, provenance, and all
  degree-one block witnesses in that round.
- `relations`: every exact-value comparison and every singleton,
  support-two, or residual P66 relation actually tested, with full support,
  family classification, roots, normalized root, and verified gcds.
- `aggregates`: exact sums by clean/control, factor bits, and shape, plus an
  all-case row.
- `witness`: the lexicographically smallest useful relation; if none, the
  smallest cross-family relation; if none, the smallest nonempty core; if
  none, the smallest pivot-loss case; otherwise `NONE`.
- `summary`: global counts and a literal finite status.

The analyzer streams these files in global case order. It holds at most one
batch of eight case results. A shared locked ledger reserves the exact final
TSV bytes of each relation and one global relation slot before the relation is
appended to any case vector. It reserves every other output line before the
line is written. The final on-disk byte total must equal the ledger exactly.

The smallest relation order is `(N, case_index, kind, support, provenance)`.
This is an output convention, not a selection rule.

## Interpretation and held-out firewall

The target processes all 188 discovery cases, while reporting the 125 clean
cases separately and first in every synthesis. Factor-bearing cases are
controls and cannot support a strict new lead.

A new held-out packet may be proposed only if at least one clean case has a
nonempty fixed core and either:

1. that clean core contains a cross-family exact square relation; or
2. private-pivot loss repeats in at least two clean cases of the same
   `(factor_bits,shape)` cell.

This run does not create or execute that held-out packet. If every union
peels to the empty core, the exact all-twelve-family union seam is killed for
these discovery rows. Any duplicate relation is still reported, but it does
not override the empty-core kill.

Every result is finite hypothesis-generation evidence. It cannot establish
an all-input event law, an asymptotic rank theorem, a Las Vegas probability,
or quasipolynomial factoring.

## Resource gates

The implementation is C++17 with `boost::multiprecision::cpp_int`. It uses at
most eight workers. Every compile or executable phase runs under `nice -n 15`.
Initial and target admission require one-minute load plus requested workers to
fit the host CPU count.
The remote runner holds the generic exclusive lock
`/tmp/integer_factoring.production.lock` for its full lifetime. Its firewall
uses `/proc` directly. It records PID, PPID, start time, losslessly shell-quoted
NUL-delimited command-line arguments, executable-link target, and working-
directory-link target in numeric PID order. It makes two complete snapshots,
each capped at 1 MiB, with identical PID lists before, between, and after the
two scans. The two snapshots must be byte-identical. A PID-list change,
identity change, read failure, malformed record, per-identity overflow,
process-count overflow, or snapshot-byte overflow rejects the run.

Before the snapshots, the firewall follows the runner's `/proc` parent chain
all the way to PID 1. It caps the chain at 64 identities and 16 KiB, but rejects
instead of truncating if either cap is reached before PID 1. Each exclusion is
bound as `(PID,starttime,PPID)`. The only other exclusion is the deadline
watchdog, whose `(PID,starttime,PPID)` must identify it as a direct child of
the runner. Both scans must observe every exact exclusion unchanged.

For every nonexcluded identity, a `remote_run` or `remote_run.sh` occurrence
in any command-line argument, executable path, or working directory rejects
the run without requiring an F-number, mode, argument position, or particular
path spelling. The prior semantic checks also remain: production mode options
reject directly, and an F-number together with `remote_run`, `search`,
`union`, `multirow`, `lift`, `factor`, or `production` in the command line
rejects. The two complete snapshots, their hashes, the exact
exclusion identities, and literal firewall PASS remain as final sidecars.
Their hashes enter both archived metadata files and the final run manifest.
The scan occurs before any workload child starts. After prelaunch, the held
exclusive lock is authoritative for every cooperating research packet.

After packet, hostile-audit, input, host-resource, lock, and cgroup admission,
the runner starts one absolute 14,400-second deadline from `/proc/uptime`
before process capture or compilation. The cgroup-v2 envelope leaves only the
deadline watchdog in the parent cgroup and contains the workload runner plus
all subsequent descendants:
`memory.max=3,758,096,384`, `memory.swap.max=0`, and an independent 4-GiB
`RLIMIT_AS`. The watchdog uses `cgroup.kill` at the absolute deadline. Every
phase also receives only its remaining absolute time. Compile, self-test,
deterministic eight-case
preflight, and target arithmetic must finish by deadline minus 600 seconds.
The target archive must finish by deadline minus 120 seconds. Resource capture
and the final hash manifest must finish before the absolute deadline. A
timeout, cgroup OOM event, compression error, or incomplete manifest aborts the
mathematical result.

The preflight covers large cases, all available shapes, and clean/control
status. It measures the complete eight-case raw tree, including runner metadata
and both hash manifests. The runner multiplies the target wall, RSS, and raw-
output extrapolations by four. The projected target wall must fit the time
remaining before the 600-second closure reserve. The projected RSS must fit the
3.5-GiB cgroup. The projected target analyzer output must fit 192 MiB.

The analyzer gets an exact raw-output budget of 16 MiB minus 64 KiB in
preflight and 192 MiB minus 64 KiB in target mode. The runner reserves the
64 KiB for authenticated run metadata and the per-file SHA manifest, then
verifies the complete raw tree against 16 MiB or 192 MiB. Relation payload has
a separate 96-MiB cap, and every generated output line or buffered summary
file has a 1-MiB cap. The complete packet has a 512-MiB regular
and apparent-size cap, 16-MiB total log cap, 1-MiB per phase-stream cap,
32-MiB sidecar cap, 16-MiB binary cap, and 384-MiB `RLIMIT_FSIZE`. Before
compression, the runner proves that current bytes plus the largest live input
file plus one percent of the raw tree plus 4 MiB fit the packet cap. It then
creates deterministic gzip archives while deleting raw files. Each raw tree
contains its per-file SHA manifest and a hash of that manifest. The runner
verifies both before compression, verifies gzip and tar structure afterward,
and hashes the archives.

Hard arithmetic caps are 284 original rows per case, 100,000 bits across all
284 serialized input rows before deduplication, 65,536 opaque blocks,
1,000,000 aggregate gcd-refinement steps per case across the union and core
decoders, 50,000 serialized relations per case, 1,000,000 serialized relations
globally, 96 MiB of exact serialized relation bytes, and 192 MiB of analyzer
output. Global relation count, relation bytes, and total analyzer bytes are
reserved atomically before retention or write. A failed reservation sets one
shared cancellation bit; all active relation-generation loops poll it and
abort. Crossing any cap aborts the mathematical result; it is not a null.
