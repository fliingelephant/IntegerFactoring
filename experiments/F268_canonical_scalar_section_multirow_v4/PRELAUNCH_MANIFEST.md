# F268-D04 prelaunch manifest

## Identity

- Experiment: `F268-D04`
- Parent: immutable validation-failed `F268-D03`
- Family: fixed canonical `t=0` scalar-section power residues with complete
  low-support classification and retrospective P66 decoding
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING; TARGET_VALIDATION_PENDING`
- Search result: none
- Dynamic work: forbidden before the frozen hostile audit passes and every
  F265 process has ended

F268 is finite heuristic guidance. It is not an integer-factoring theorem or
an asymptotic success claim.

## Narrow D04 repair

D03 was frozen at manifest root
`19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f`.
Its fresh hostile audit gave `PASS`; the exact audit bytes hash to
`23a3e7921fa54ee1c7048ed7fc05b116f61ee76b88af2fb2275d7b13f8bd3a04`.

The authorized D03 validation failure is recorded by `RESULT.md` with SHA-256
`399fcea77a78c26cbfdab214dc00d186474a3ed898acb3ff0ddc2ebf16e6e459`
and by `RUN_MANIFEST.md` with SHA-256
`f493a1302f44a9d3b3798156813bde2c3a88e7a1ba5225b3246c841974d295e9`.
All three C++ programs compiled and the corpus self-test passed. The search
self-test then failed with `family syntax SHA mismatch`. It stopped before the
label self-test, corpus generation, preflight, discovery, or heldout phases.
The failed target contains no search evidence.

The external family-file digest and both frozen expected digests agree. The
D03 custom SHA-256 table instead contains `0x2748774U` where standard SHA-256
requires `0x2748774cU`. Its search self-test also authenticates the family file
before it executes the existing `sha256_bytes("abc")` known-answer test.

D04 changes that one round constant to `0x2748774cU` and moves the existing
known-answer test before the first family-file authentication in the search
self-test. Apart from those two validation repairs, packet/output version
changes, and frozen provenance/status/audit/manifest metadata, the algebra,
family syntax, master seed, public grammar, marker candidates, ordinary
cohorts, screens, ranks, caps, resource projections, and target commands are
unchanged from D03.

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
| `ALGEBRA.md` | `342c9be4852da6b8dd2869d8e887a2df1de06f0b654a84f423349891b7b13acb` |
| `PREREGISTRATION.md` | `c849a12f5315e45a0ee83fc97a9fbc111134f615ecb3d68342d3e3a75f10a66a` |
| `FAMILY_SYNTAX.tsv` | `aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce` |
| `corpus.cpp` | `0c66dbcec2c44cd1ef557f98b7dddbc54632fb0bdaf9f501cefce76edddf269a` |
| `search.cpp` | `eb02d9714585d957d8ef581c92b9528638fceca914ba78bf18e6b8c21eb6e20a` |
| `label_audit.cpp` | `89c9d4a014c00e5a64934ca78de59fc830a7e1f6bd8ac4620183ce721aa178b4` |
| `remote_run.sh` | `c3d0cb56131b2295c9ba288538a0456ff7926c0d6f66b6bea4922d1cef1f7f5f` |
| `PROVENANCE.md` | `75e12ac55d20da4fe613a34adedcbceb25f155bcf923e929aa453e05830798f1` |
| `AUDIT_REQUEST.md` | `e04697b88180fa65985b0606bd5cc1d234c3109ee712bbeca2a0e5dd5a2e8d23` |
| `VALIDATION_PENDING.md` | `8edf83dfb03074e1428546128796b48ab144e6e3ba3802a761871b5ff5778890` |

## Static checks completed

- The exact family-syntax bytes hash to the digest compiled into C++ and the
  runner.
- `FAMILY_SYNTAX.tsv` advertises the real split semantics and 45/48 maxima.
- Discovery ranking has an arithmetic-only interface and no case metadata.
- The search `Case` has no factor or marker fields.
- The label auditor is a separate post-heldout C++ process and checks mode
  0600, factor construction, marker conditions, and exact marker shortfalls.
- `label_audit.cpp` directly includes `<tuple>` before using `std::tie`.
- The immutable D03 root, hostile `PASS`, failed validation result, and
  failed-run manifest were authenticated.
- SHA-256 round constant 46 is the standard `0x2748774cU`; the misspelled
  `0x2748774U` token is absent.
- The `sha256_bytes("abc")` known-answer test precedes family-file
  authentication in the search self-test.
- The named marker caps match the preregistration and retain D03's candidate
  stream.
- The runner overlap gate rejects every `F265` or `f265` process token.
- `bash -n remote_run.sh` passed.
- `git diff --check -- experiments/F268_canonical_scalar_section_multirow_v4`
  passed.
- `remote_run.sh` is executable.
- No durable research ledger was edited by this packet author.

No D04 C++ compilation, self-test, corpus generation, preflight, local search,
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
