# F268-D03 prelaunch manifest

## Identity

- Experiment: `F268-D03`
- Parent: immutable failed `F268-D02`
- Family: fixed canonical `t=0` scalar-section power residues with complete
  low-support classification and retrospective P66 decoding
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING; TARGET_VALIDATION_PENDING`
- Search result: none
- Dynamic work: forbidden before the frozen hostile audit passes and every
  F265 process has ended

F268 is finite heuristic guidance. It is not an integer-factoring theorem or
an asymptotic success claim.

## Narrow D03 repair

D02 was frozen at manifest root
`31e05f0f310ff6f0b37421ccf68634bf57bce65cb708074408dec96b7801561b`.
Its fresh hostile audit failed before any dynamic work. The exact failure
record hashes to
`1b2c37510ec4680d0c8996d3654108e8727e9a44e92acf8523c550b79735a7b0`.

The D02 source allowed 128 candidates in each constrained marker-prime
request, but the prose assigned 200,000 candidates to every prime request.
D03 freezes the existing source law explicitly: two requested rows per marker
cell, 4,096 seeded pair attempts per requested row, and 128 candidates per
constrained-prime request. This leaves the unseen marker candidate stream
unchanged and bounds a requested marker row by 1,048,576 constrained-prime
candidate tests. Raising both nested requests to 200,000 would admit
1,638,400,000 tests per requested marker row.

The D02 runner also recognized only selected F265 search and runner commands.
D03 rejects every process command containing `F265` or `f265`, which covers
every named packet phase and unforeseen F265 packet command. Its bracketed
grep expressions do not match the grep process itself.

Apart from those repairs, the packet/output version change, one corrected D03
template-version sentence, and frozen provenance/status/audit metadata, the
algebra, family syntax, seed, candidate stream, ordinary cohorts, screens,
ranks, caps, projections, and target commands are unchanged. D02 generated no
corpus or numerical output.

## Exact nonduplicate seam

The P66 inputs are only

```text
U_E(a) = [a^E]_(N^2),  Y_E(a) = [a^(E/2)]_N,
E in {N-1,N+1,N^2-1,2(N-1),2(N+1)}.
```

The public source fixes the canonical `t=0` section. It has no fresh
principal lift coordinate. P211/F247 and P213/F248 bound fresh principal
coordinates and leave this fixed retrospective multirow interface open.
P212/F245 studies fresh inverse quotients and torus words. P66/P138 supply
decoding/section results but no row source. F262, F264, F265, and F266 use,
respectively, polynomial, matrix, elliptic-cubic, and quadratic-form rows.
F26 uses canonical inverse endpoint carries. F268 tests those carries only as
direct controls; none enters P66.

## Freeze-critical chronology

For every bank the source:

1. completes the factor-blind source grammar and every stage-1 gcd;
2. completes direct stages 2 through 4 without changing the retained rows;
3. tests every singleton and unordered pair for an exact rational square;
4. serializes every useful low-support factor certificate;
5. inserts only verified `GLOBAL_PLUS` or `GLOBAL_MINUS` vectors into the
   low-support basis;
6. authenticates the complete factor-free P66 kernel; and
7. only on the no-useful branch, extends the global-decoy basis to the kernel
   and tests residual representatives, each of support at least three.

A later P66 or evidence cap cannot erase a completed useful singleton or
pair. The packet preserves the complete low-support evidence, keeps the bank
`RESOURCE_REJECT`, and excludes it from eligible and null counts.

## Staged scale and resource gate

Discovery evaluates all 12 families at 20/24 rows. Heldout evaluates only the
four authenticated selected families at 45/48 rows. With all bounded marker
controls present, the exact conservative scale is:

```text
banks                                      3,440
row powers and singleton tests           110,224
unordered row-pair bundles             1,942,040
stage-3 pair gcds                      15,536,320
support-two squareclass tests           1,942,040
```

F265-D02 measured 2,369,895 pair bundles in 3,316.220420 wall seconds, or
714.637358152448 bundles per wall second. The compiled F268 floor is therefore
5,435.036324 seconds after the factor-two safety multiplier. The target gate
uses the maximum of this floor, the measured pair-scaled projection, and the
measured task-scaled projection. It adds twice complete corpus-generation
wall time and gates at 12,600 seconds, 3.5 GiB RSS, and 768 MiB output.

Preflight uses the largest real case in every available shape and all twelve
families. Ordinary samples use the heldout 45/48-row layouts. It executes and
replays source construction, every row power, every singleton, all eight
stage-3 gcds per pair, every support-two test, P66, the quotient, and
serialization. A pass requires exact count identities, zero resource rejects,
and a completed 48-row bank.

## Frozen source hashes

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `e372c8953ccdaec003b2db7885083c713ec065af73a38caa2373dbfe7d41af1b` |
| `PREREGISTRATION.md` | `919888209364123d8530af6b3e0e9023443fb08766a9c36b0c3048a691fc9523` |
| `FAMILY_SYNTAX.tsv` | `aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce` |
| `corpus.cpp` | `00b987833a508a939d4b17e798bd439839769d35a51699e43ae49c747362c822` |
| `search.cpp` | `184c1e25545a7922c5ba8c203fff5e728bee636d2d3a67515733daf6041e7bb6` |
| `label_audit.cpp` | `948753dca0d30880094b4244d99718c275742df0c5da3777dcbc0301101bc108` |
| `remote_run.sh` | `49788f707eb47798de30bcb2db554cf4fb5a9476f30defb56bd2628824a82b3a` |
| `PROVENANCE.md` | `068244ca314db5e8eef242b637a6820e214a0d2a4ab647f404ca11173c82e31b` |
| `AUDIT_REQUEST.md` | `80123b75bcc401c7937c4db38cb3a8e1b62bdb991dff1f64e98476f49a99ea74` |
| `VALIDATION_PENDING.md` | `1b8fbec12e6c94fca569d890dfb41ea0cee0c5ae0f61686335e32c79cc6b880a` |

## Static checks completed

- The exact family-syntax bytes hash to the digest compiled into C++ and the
  runner.
- `FAMILY_SYNTAX.tsv` advertises the real split semantics and 45/48 maxima.
- Discovery ranking has an arithmetic-only interface and no case metadata.
- The search `Case` has no factor or marker fields.
- The label auditor is a separate post-heldout C++ process and checks mode
  0600, factor construction, marker conditions, and exact marker shortfalls.
- `label_audit.cpp` directly includes `<tuple>` before using `std::tie`.
- The D02 manifest and post-freeze hostile failure were authenticated.
- The named marker caps match the preregistration and retain D02's candidate
  stream.
- The runner overlap gate rejects every `F265` or `f265` process token.
- `bash -n remote_run.sh` passed.
- `git diff --check -- experiments/F268_canonical_scalar_section_multirow_v3`
  passed.
- `remote_run.sh` is executable.
- No durable research ledger was edited by this packet author.

No C++ compilation, self-test, corpus generation, preflight, local search,
remote command, discovery, or heldout evaluation occurred. Static inspection
does not establish C++ syntax or runtime correctness.

## Frozen inputs

`FROZEN.sha256` authenticates exactly the ten files in the source-hash table
above plus this manifest. The manifest cannot list its own digest. The
coordinator supplies the SHA-256 of the exact `FROZEN.sha256` bytes to the
fresh auditor out of band.

The hostile audit writes only `HOSTILE_PRERUN_AUDIT.md`, which is a post-freeze
artifact. The runner requires exact `PASS` and manifest-digest lines before it
creates a target or compiles.

## Kill gates

Any digest mismatch, algebra assertion, source exhaustion, registered cap,
corpus failure, preflight reject, count mismatch, projected-resource excess,
selection mismatch, evidence replay failure, label-audit failure, output-cap
crossing, deadline, or visible `F265`/`f265` process token stops the exact
packet. A failed gate stays attached to these bytes. It does not authorize an
unchanged rerun or a silently reduced bank.
