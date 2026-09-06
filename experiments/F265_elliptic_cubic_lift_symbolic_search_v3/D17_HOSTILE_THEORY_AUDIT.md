# F265-D17 fresh hostile theory/interface audit — PASS

## Verdict

**PASS.** I found no composition defect, mutable-basis leak, final-status
ambiguity, reservation-state ambiguity, schema drift, replay gap, digest
conflict, byte-cap error, root-construction ambiguity, or authorization
expansion in the authenticated D09--D17 additive composition.

D17 closes both unresolved D16 interface defects. The final
`decoder_strict_structural_hit` bit is derived only after final status is
fixed. A `RESOURCE_REJECT 1 1` bank therefore serializes zero without changing
its committed basis records or `basis_sha256`. `decoder_reservation` is the
historical granted quota. It is exactly zero or `91111`, survives unused-quota
return and later recoverable outcomes, and always bounds the exact committed
`decoder_call_count`.

This PASS authorizes only source drafting for the four D17 roles. It does not
authorize source freezing, a source PASS, compilation, fixture
materialization, fixture verification, preflight, evaluation, replay,
sealing, diagnostics, private classification, packaging, result release,
remote execution, or a ledger edit. Approved hard dynamic containment remains
a mandatory later gate for every executable mode.

## Authenticated composition

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |
| `D10_DRAFT_ALGEBRA.md` | `aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7` |
| `D10_DRAFT_PREREGISTRATION.md` | `be7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e` |
| `D11_DRAFT_ALGEBRA.md` | `a177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27` |
| `D11_DRAFT_PREREGISTRATION.md` | `9b477799e006a9b2bb49eebcf062917f1a3c91a9852ce8fbe825fcea1a1df23e` |
| `D11_HOSTILE_THEORY_AUDIT.md` | `777ccd163959a7ec4e14bdcd3c9d12fc1d58732207f12520806e1ad2a2705246` |
| `D12_DRAFT_ALGEBRA.md` | `eae660da5a5c5344b83ccd99301cfb4f2db89d5c259cf73194f85892e2d7dcb0` |
| `D12_DRAFT_PREREGISTRATION.md` | `65682542478a2c2270f3657d2c741ea253445ad3cf160758449a0ce21e806ecd` |
| `D13_DRAFT_ALGEBRA.md` | `915ec124f6be79a1530af3df628f8c65eaa5bde845f073f67f5077e66258ea9c` |
| `D13_DRAFT_PREREGISTRATION.md` | `42667461ac3a21820f3ea1d5de545d17ff03c719a38cd405dbdb0e91ff083c17` |
| `D14_DRAFT_ALGEBRA.md` | `42690a13d5a0fade1dd644bf29d299d9bab3b5cdd6a68d08354f1e9a5c6fb4f6` |
| `D14_DRAFT_PREREGISTRATION.md` | `4b02e30cfe2986fbc04dbf8c4faf22743c18acb1a64d2a07b30eefe2c6338b9b` |
| `D14_HOSTILE_THEORY_AUDIT.md` | `b7067c104eaf96dfa81d7bd08dcc9326e7616016fb66202c078bf1c2ea5ef03e` |
| `D15_DRAFT_ALGEBRA.md` | `563293afda1cf4d183b4d70ec30da60d0339086a52d9395df8b4d70d1e7ceeb6` |
| `D15_DRAFT_PREREGISTRATION.md` | `9c3b7cc4d855e906d8c9f35bcf7846631d28d728138df07f0e812cf59c12798d` |
| `D16_DRAFT_ALGEBRA.md` | `10d0e74462aac944a32dbc68404aa30c730d1f5b919f1fb4dd9e5a76ae92f5b2` |
| `D16_DRAFT_PREREGISTRATION.md` | `8a27d1d3af5b6f46d5f90e2f3545928cde55932c8012c6829b7c67207bd556a2` |
| `D17_DRAFT_ALGEBRA.md` | `e784dfb9d151e816ef43644e480e705c7414d4af34114250da7d399c319d46d3` |
| `D17_DRAFT_PREREGISTRATION.md` | `acd92da342f2f88667a6b3cbfc3be1c13e9f8fdeabf4789020f3472319ed62d3` |

All twenty hashes matched the files reviewed. I authenticated both D17 bytes
before reading them. I then authenticated and read the complete additive
D09--D16 predecessor chain and both imported hostile PASS artifacts in full.

The D11 and D14 PASS files remain evidence only for their exact authenticated
compositions. I did not transfer either verdict to D15, D16, or D17. I
independently audited the D15--D17 additions and their interaction with every
surviving predecessor clause.

For the imported decoder and corpus boundaries, I also reauthenticated the
F271 V2 freeze, manifest, statement, proof, V1 statement and proof, and V2
hostile audit at their D09/D11 hashes. I reauthenticated and read the two
public F268-D04 corpus files at hashes
`8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5`
and `b4a4c976013dd62c58376b948c51a1c5c380265a46fbf932a5e0972fb6c389d5`.
They contain 188 and 296 data rows, including eight marker rows in each file,
and therefore retain exactly 180 discovery and 288 heldout banks. I did not
open either private-label file.

## Final structural-hit derivation

The D16 basis commit payload is repaired cleanly. D17 removes only
`decoder_strict_structural_hit` from that payload. The following evidence
remains immutable at the `1 0 -> 1 1` transition:

```text
kernel_dimension singleton_count support_two_count L_dimension Q_dimension
quotient_defined all_Q_images_global low_hit
basis rows basis_sha256
```

The complete `L` and `Q` rows include the authenticated D13 root-class token.
They therefore determine both new logical predicates without adding a field,
row, counter, event, operation, or digest input:

```text
all_L_images_global
basis_has_nonglobal_Q
```

The empty-`L` universal is true. The empty-`Q` existential is false. A code-3
`STRUCTURAL_Q_NON_GLOBAL` record is the only record that satisfies the second
predicate. A code-4 `STRUCTURAL_ONLY_LOW_IMAGE` record cannot satisfy it.

After status precedence fixes the final status, the serialized hit is exactly

```text
status == ELIGIBLE
and quotient_defined == 1
and all_L_images_global
and basis_has_nonglobal_Q.
```

This formula passes the hostile boundary cases:

| Committed basis case | Final status | Serialized hit |
|---|---|---:|
| Empty core | `ELIGIBLE` | 0 |
| All `L` global and at least one code-3 `Q` | `ELIGIBLE` | 1 |
| A non-global `L` and code-4 `Q` records | `ELIGIBLE` | 0 |
| Any committed basis | `RESOURCE_REJECT` | 0 |
| No committed basis | any legal status | `-` |

In particular, take a complete basis suffix containing a
`STRUCTURAL_Q_NON_GLOBAL` record and then reach an inherited recoverable
non-basis outcome before public core commit. The legal final state is
`RESOURCE_REJECT 1 1`. D17 serializes hit zero. The code-3 basis row, its root
class, `basis_sha256`, sticky structural event, event digest, factors, and all
counters remain unchanged. Thus the final eligibility claim cannot rewrite
the status-independent mathematical evidence.

Reaching basis commit excludes every generation-stage stop. The repaired
formula is therefore equivalent to the four-part D09 eligible-bank definition.
It is not a relaxation. The heldout decision counts only the final serialized
bit. Sticky relation factors in an ineligible bank still drive the inherited
other-factor and null clauses.

## Granted reservation and actual calls

The D09 packet ledger grants one fixed `91111` scalar-gcd reservation to a
nonempty residual or grants nothing. D17 gives the bank field the matching
historical meaning. Its only transition is atomic with the ledger grant:

```text
0 -> 91111.
```

A request is not a grant. A denied request leaves both bank fields zero and
does not enter F271. Returning unused active quota changes ledger `A`; it does
not reverse the bank field. A later recoverable outcome also cannot reverse
the field. The complete reachable pairing is therefore:

| Bank chronology | Reservation | Actual calls |
|---|---:|---:|
| Stop, pre-peel rejection, residual above 64, or denied request | 0 | 0 |
| Empty committed core | 0 | 0 |
| Grant, then recoverable outcome before basis commit | 91111 | exact value in `[0,91111]` |
| Complete nonempty eligible core | 91111 | exact value in `[0,91111]` |
| Complete nonempty basis, then `RESOURCE_REJECT 1 1` | 91111 | exact value in `[0,91111]` |

A nonempty all-unit input can receive the grant and make zero scalar gcd
calls. This is legal and distinct from the zero-survivor empty core. Every
serialized bank satisfies

```text
decoder_reservation in {0,91111}
0 <= decoder_call_count <= decoder_reservation.
```

The historical grant fields are not summed as active quota. Evaluation and
replay instead repeat the canonical D09 batch chronology. They use the exact
actual call counts to commit `C`, return unused active quota, and verify
`C+A<=8388608` at each transition. This preserves packet-cap reuse while
making every bank's grant history replayable.

## Status, presence, and replay closure

The legal commit pairs remain exactly `0 0`, `1 0`, and `1 1`. `DIRECT_STOP`
and `BANK_SKIP` require `0 0`; `ELIGIBLE` requires `1 1`; and
`RESOURCE_REJECT` can use all three pairs. A zero-survivor committed peel must
take the empty-basis transition. It cannot remain at `1 0`.

D17's replacement presence table is total. The eight immutable downstream
fields and final hit are all `-` before basis commit. After basis commit, the
eight fields are exact transition evidence and the hit is an exact final
Boolean. Scalar peel rows, peel and basis hashes, coefficient pairs, survivor
constraints, dimension equations, basis-row count, and canonical row order
retain their D15/D16 meanings.

Evaluation reconstructs the source, peel, and basis suffixes from the public
TSV rows. It derives both record predicates from the complete projected basis
stream, validates final status, derives the final hit, and simulates the grant
chronology. Replay repeats those checks from regenerated logical records and
from authenticated committed rows. It requires exact identity of status, hit,
grant, actual calls, flags, rows, digests, events, counters, and wrapped public
files. A mismatch is fatal and permits no success manifest or finite label.

The D15 basis suffix contains root classes but not the final hit or reservation.
The bank file digest covers the final hit and reservation. The split core
manifest covers the complete wrapped bank file. These layers are distinct and
noncircular. A final hit change cannot alter `basis_sha256`, and an unauthentic
bank-field change cannot survive the full-file and replay checks.

## Schema, bytes, caps, roots, and names

The bank header still has 34 fields and 33 tabs. Its literal length is 405
bytes including LF. D17 adds no field. The maximum all-present data row remains

```text
8+9+2+9+2+37+4*30+1+3+3+2+3+2+2+4+2+2+5+3+4*64+5+5+10+34
= 529 bytes.
```

The five one-byte values after the two dimensions are the four mathematical
Booleans and the inherited `observed_factor` Boolean. The historical grant
uses at most the five-byte spelling `91111`, and the actual call count is no
larger. Therefore the 16,384-byte bank-row cap keeps 15,855 bytes of slack.
Both bank files use at most

```text
468*529 + 2*405 = 248382 bytes.
```

No scalar, basis, event, or digest row changes width. The inherited
226,088,448-byte total-output cap, 262,400-byte one-bank temporary cap,
309,990,912-byte directory-peak cap, 128 MiB per-file cap, arena and RSS caps,
operation caps, timers, process bounds, and deadlines remain coherent.

The D17 theory root has exactly twenty LF-terminated lines. Lines 1--18 are
the D09--D16 predecessor and audit hashes in D17's displayed order. Line 19 is
the authenticated D17 algebra hash. Line 20 is the authenticated D17
preregistration hash. Every line is basename, tab, hash, LF. This agrees with
both D17 drafts and has no self-reference.

The future-only substitutions are complete and length-safe:

```text
F265-D16  -> F265-D17
f265_d16_ -> f265_d17_
F265-D16. -> F265-D17.
F265_D16_ -> F265_D17_
```

They do not change a predecessor byte. `F265-D17` remains eight bytes. The
four source roles, eight modes, ten invocation grammars, fixed filenames,
manifest roots, and four invalid public/private fixture-root placeholder
occurrences retain their exact inherited contracts with D17 prefixes.

## Review boundary

I used only read-only SHA-256 authentication and full-text inspection before
creating this report. I did not inspect private labels, modify a draft or
predecessor, create source or a runner, compile, materialize a fixture, invoke
preflight, execute an evaluator, use a remote host, stage or package a result,
or touch a ledger.

This audit is outside the normative D17 draft composition. Its SHA-256 is
reported after sealing. A self-hash is not embedded in these bytes.
