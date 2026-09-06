# F270-D01 hostile static pre-run audit

## Verdict

**FAIL — DO NOT LAUNCH THIS FROZEN PACKET.**

`audit_request_disposition: REVISE`

The arithmetic design survives hostile inspection, but the frozen runner does
not enforce its resource contract. The failure is immutable. Repair requires a
new packet version and a new hostile pre-run audit.

`frozen_manifest_sha256: 4fe9f85f7a52f7e6fce505d6165cd223e4ec394de5c536dfca6bc474398efe2f`

No compile, self-test, preflight, target, or remote command ran during this
audit. No hidden factor-label file was opened. The frozen files were not
edited.

## Authentication and scope

The exact `FROZEN.sha256` root matched the required root above. Every record in
that manifest authenticated before claim inspection:

| Frozen file | SHA-256 | Result |
|---|---|---|
| `POSTHOC_PROTOCOL.md` | `c983b861c2de2cf8a75d059e2856cc53b5d35fff901ae2ed9b0f497b2fcdb3a7` | OK |
| `RESOURCE_ESTIMATE.md` | `32674bfab63eb65db72fa45f8a51ee657f96584a9fe40d58a818df82af38ed59` | OK |
| `f270_union.cpp` | `0760af3777d2a5f2ba3f338da86e02c245869605927e296714d734d83955ea54` | OK |
| `remote_run.sh` | `b71f9a84bd38e19b0777efd455078a48664749de2237473116b5cf8b111b33db` | OK |
| `PRELAUNCH_MANIFEST.md` | `5ebfd577d158c0bf2215540f18668ee37b5c0c74e920d9fe698c4c04d01faeba` | OK |
| `STATIC_AUDIT_REQUEST.md` | `5e1ff9b867b6728394b0e1133898668d5b748341e3b0a7b56d531166cabfa645` | OK |

The three arithmetic inputs matched their frozen hashes:

- evidence: `a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc`;
- banks: `c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6`;
- public corpus: `8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5`.

The relevant F268-D04 packet root was
`de76f2e3fbb264b917cedb5639fde75c979f272e43841452c6f642b8132cdbf4`.
Its result audit matched the protocol-pinned hash
`75597f68751d20ff599d68724c06182e964d935132917214a06cf653c778ee97`.
Its 44-record final manifest, whose SHA-256 is
`bdc96777472722a05cd6ef22eb710d03bc1249fe6bda09cf03ef10514e058afc`,
authenticated in full.

The authenticated input counts are exact: 188 corpus cases, 2,256 banks, and
124,213 evidence records, comprising 53,392 `ROW` and 70,821 `BLOCK` records.
Every case has eleven 24-row families and one 20-row family, for 284 rows. The
public bank label gives 125 clean and 63 control cases. There are no exact-value
duplicate groups in the frozen discovery rows; the duplicate path was still
audited statically.

## Blocking findings

### B1. The four-hour firewall is not a whole-packet deadline

`STATIC_AUDIT_REQUEST.md:27-28` requires that the runner cannot exceed four
hours. `remote_run.sh:72-81` runs compile, self-test, and the complete preflight
without a timeout. `remote_run.sh:108-113` then grants the target a fresh 14,400
seconds, plus a 30-second kill grace. Final resource capture and manifest
generation at `remote_run.sh:115-127` are also outside any timeout.

Therefore a normal successful invocation can exceed four hours by the duration
of compile, self-test, preflight, kill grace, and finalization. Any pre-target
phase can also hang indefinitely. The preflight only predicts target time; it
does not reserve time remaining in the packet deadline. This contradicts the
literal runner firewall and makes checklist item 11 false.

The next packet must start one absolute, monotonic deadline before compilation.
That same deadline must cover compile, self-test, preflight, target, termination
grace, resource capture, and final manifest creation. Each phase must receive
only the remaining budget. The target must not start unless its projected time
fits in that remaining budget. Timeout termination and manifest failure must
abort without a mathematical result.

### B2. Global relation and payload caps are enforced only after retention

`f270_union.cpp:373-386` checks only the 50,000-relation per-case limit before
appending a `RelationRecord`. Eight workers retain all case results in memory at
`f270_union.cpp:637-642`. In the worst allowed per-case state, this permits

```text
188 * 50,000 = 9,400,000
```

relation objects to be retained before the declared 1,000,000 global limit is
examined. `f270_union.cpp:493-529` then materializes the complete relation TSV,
counts its records and payload, and checks both caps only after all relation
objects and serialized relation text already exist. The 512 MiB aggregate
output check at `f270_union.cpp:581` is likewise after all output strings are
materialized.

The process can exhaust memory before it reaches the promised cap failure. The
global count and 256 MiB relation-payload limits are therefore not generation-
time resource firewalls.

The next packet must reserve a global relation slot and its deterministic byte
budget before it retains or materializes each relation. The reservation must be
shared safely across workers. A failed reservation must stop generation and
must not append the record. Serialization must stream or remain bounded; it
must not construct content beyond the cap before testing the cap. The global
output budget needs the same before-retention or bounded-write discipline.

### B3. The promised process and hard resource containment is incomplete

The runner measures preflight RSS and output and applies factor-four projection
gates, which is a valid admission test. It does not impose a cgroup or equivalent
hard memory ceiling on compile, self-test, preflight, or target. It checks target
directory size only after the target exits, while stdout, stderr, compilation,
preflight, and run-directory artifacts can continue to grow. These omissions
compound B1 and B2: the runner has no hard containment if the projection or late
in-process accounting is wrong.

The runner also writes the process snapshot at `remote_run.sh:48-55` and then
continues without a human acknowledgement. Its automatic overlap check at
`remote_run.sh:67-70` recognizes only F265/F269, although
`POSTHOC_PROTOCOL.md:210-213` prohibits overlap with any other production run
and `PRELAUNCH_MANIFEST.md:48-51` requires a human to confirm the captured list.

If the next protocol continues to promise these hard ceilings, the next runner
must enforce them for the whole packet with cgroup/RLIMIT-equivalent memory and
file/output limits. It must also use a generic production-run lock or pause for
an explicit acknowledgement of the captured process list before compilation.

## Mathematical and specification audit

The following checks pass. They do not override the resource FAIL.

### Input joins and label firewall

The suspected global/cell-local index collision is absent. The public corpus
`index` is cell-local, while bank/evidence `case_index` is the global corpus
position. `parse_corpus` deliberately stores `out.size()` in `Case.index` and
the serialized field in `Case.cell_index` (`f270_union.cpp:179-188`). All bank,
evidence, and worker keys use the global `Case.index`; the bank join also checks
`cases[case_index]` against shape, bits, and `N` (`f270_union.cpp:192-240,639`).

The first reset proves the semantics concretely. Corpus global position 12 is
`neighbor/12`, cell-local index 0, `N=4405657`; its bank rows use
`case_index=12`. The next reset at global position 36 is `random/16`, cell-local
index 0, `N=2427502037`; its bank rows use `case_index=36`. Both join correctly.
No cell boundary fails.

Only evidence `ROW` records enter arithmetic. `BLOCK` records are skipped.
Clean/control classification uses only the allowed bank-table `earlier_factor`
field. The analyzer does not open a hidden factor-label input, and controls do
not participate in either held-out trigger.

### Deduplication, global refinement, and ranks

Rows flatten in family-ID then row-ID order. For an equal-value class of size
`k`, each new provenance is compared with every prior provenance before it is
appended, so all `C(k,2)` supplied-root comparisons occur before deletion
(`f270_union.cpp:393-407`). Exact roots, modular roots, signed gcds, root class,
and provenance are retained. Cross-family provenance remains cross-family.

The decoder starts only from deduplicated integer row values. Its gcd/exact-
division refinement preserves exponent coordinates, reaches pairwise-coprime
blocks, and verifies exact reconstruction of every row
(`f270_union.cpp:244-263`). It does not import F268 `BLOCK` arithmetic. Square
blocks are correctly omitted from the parity matrix.

Original equations expand every deduplicated column through all of its
provenance. Each family restriction independently replays full rank. The code
checks both required identities:

```text
cross_dimension_gain = sum_f rank(V_f) - rank(V_union)
                     = original_nullity
original_nullity = (284 - dedup_rows) + dedup_nullity
```

This remains correct for a duplicate that spans families
(`f270_union.cpp:409-437`).

### Peeling and complete P66 decoding

Each peeling round first identifies every row incident oddly to a current
degree-one nonsquare block, then deletes the complete marked set. It repeats to
a checked fixed point (`f270_union.cpp:439-452`). This is the simultaneous
kernel-preserving peel from P106, not a greedy order-dependent peel.

The fixed core is independently refined and its rank is cross-checked against
the original union equations restricted to active columns. Every singleton and
every unordered support-two pair in that core is tested. If no useful low-
support relation exists, only authenticated global `+/-` low relations seed the
decoy span; the code extends it through a complete core-kernel basis, tests each
new quotient-basis representative, and requires final dimension equal to core
nullity (`f270_union.cpp:454-477`). If a useful low relation exists, the already
authenticated complete kernel makes a residual quotient unnecessary, as the
protocol specifies.

Each emitted relation requires an exact positive integer square root, the
supplied modular-root product, a unit inverse, normalized root, both signed
gcds, and a consistent `GLOBAL_PLUS`, `GLOBAL_MINUS`, or `USEFUL` class
(`f270_union.cpp:338-359`). No direct factor screen was added; gcds with `N`
occur only inside relation authentication.

The frozen `N=697` self-test is mathematically correct:

```text
550^2 = 2 (mod 697), 403^2 = 8 (mod 697),
2*8 = 4^2, and 550*403 = 4 (mod 697).
```

Thus both singleton banks have rank one, their union has rank one and nullity
one, and the relation is `GLOBAL_PLUS`. The `N=15` mismatched-root duplicate
fixture also correctly yields the proper factors 5 and 3.

### Output schemas, ordering, and statuses

The required TSV schemas are present. Case slots are deterministic despite
parallel analysis, because results are stored by selected slot and sorted by
global case index before serialization. Relation sequence is deterministic per
case. Witness relations use the frozen `(N, case_index, kind, support,
provenance)` ordering.

Preflight always emits `PREFLIGHT_ONLY`. For a target, an all-empty core emits
`POSTHOC_EMPTY_CORE_KILL` before any relation-based lead, so duplicate relations
cannot override the seam kill. A cross-core lead requires a clean nonempty core
with a cross-family core relation. The repeated-loss lead uses only clean cases
and requires a clean nonempty core. Controls cannot create either status
(`f270_union.cpp:565-579`). Empty vectors and zero-column ranks are handled by
the same decoder and rank code without a special invalid access.

## Secondary cap and estimate observations

- The 1,000,000 refinement-step cap is instantiated independently by the union
  decoder and the core decoder. Thus one case can execute up to two such
  budgets. The phrase “1,000,000 refinement steps” in
  `POSTHOC_PROTOCOL.md:222-225` does not state that split. The next packet must
  state and enforce whether the cap is per decoder or aggregate per case.
- The 100,000 input-row-bit check occurs after exact-value deduplication, not on
  all 284 serialized input rows. The authenticated fixed inputs are below the
  limit and contain no duplicates, so this does not change this packet’s actual
  workload. A general implementation of the stated input cap should check it
  before deduplication.
- `RESOURCE_ESTIMATE.md:29-33` says the exact workload is “far below” F268-D04,
  but its own maxima give 7,554,968 support-two tests here versus 1,294,704 in
  the comparison run, about 5.83 times as many. The target-host preflight is the
  real timing evidence; the static comparison must be corrected in the next
  version.
- The remote runner validates the files named by `FROZEN.sha256`, but does not
  itself bind that manifest to the approved root above. The pre-run audit can
  supply that external trust anchor, as this audit did. A launch procedure must
  verify the literal approved root and a PASS audit sidecar before execution.

## Separate AGENTS.md standards review

This standards assessment is independent of the mathematical/specification
assessment.

- **Efficiency: fail.** Retaining every relation object and then materializing
  every output in memory before global cap checks violates the repository’s
  efficiency-first rule. It is also the cause of blocking finding B2.
- **No helpers: concern.** The arithmetic helpers mostly encode reused or
  auditable operations. Several one-use formatting wrappers, including
  `support_text`, `relation_provenance`, and `block_list`, do not meet the local
  “extract only when reused three or more times” preference. This is a style
  issue, not a mathematical defect.
- **Let it crash: pass in substance.** External files and CLI arguments are
  validated at system boundaries. Arithmetic invariant checks abort immediately
  and do not add recovery paths or fallback semantics. Those certificate checks
  are required audit assertions, not defensive compatibility code.

## Required disposition

Do not compile or launch F270-D01. Do not repair this directory in place. Create
F270-D02 with the absolute packet deadline, generation-time global reservations,
hard resource/output containment, and process-confirmation firewall described
above. Freeze it under a new root and obtain a fresh hostile pre-run PASS before
any execution.

The SHA-256 of this report is recorded in `HOSTILE_PRERUN_AUDIT.sha256`.
