# F265-D17 draft preregistration amendment — final status bit and granted reservation

## Status and exact imports

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

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

Read all nineteen authenticated bytes in full. Apply only the replacements
and additions below. Every D09--D16 clause not explicitly replaced by D17
survives literally. Preserve every predecessor byte.

D17 replaces every future source-version token `F265-D16`, executable prefix
`f265_d16_`, artifact prefix `F265-D16.`, and fixture-root placeholder prefix
`F265_D16_` by the corresponding D17 token. The four source roles, eight modes,
ten invocation grammars, option names, schemas except for the exact semantic
replacements below, caps, and role restrictions otherwise survive exactly.

## 1. Immutable basis evidence and final hit

### 1.1 Replacement basis-transition payload

D16's two commit flags, three legal commit pairs, peel transition, two basis
branches, and atomicity rules survive. D17 replaces only D16 Section 1.3's
immutable basis-transition payload by:

```text
kernel_dimension singleton_count support_two_count L_dimension Q_dimension
quotient_defined all_Q_images_global low_hit
basis rows basis_sha256
```

Every item in this payload is independent of final bank status. The canonical
`L` and `Q` records contain every inherited arithmetic value and exact D13 root
class. A later recoverable non-basis record or writer outcome can select
`RESOURCE_REJECT 1 1`, but it cannot change a payload byte. Post-public-core
diagnostics retain their inherited noninterference rule.

`decoder_strict_structural_hit` is not in this transition payload. No
transition-time value for that field exists. Its bank-summary value is derived
only after the inherited status precedence fixes final bank status.

### 1.2 Exact status-independent record predicates

For every `basis_committed=1` bank, define these logical predicates from the
complete committed basis records:

```text
all_L_images_global = 1
    iff every L record has root_class GLOBAL_PLUS or GLOBAL_MINUS

basis_has_nonglobal_Q = 1
    iff at least one Q record has root_class STRUCTURAL_Q_NON_GLOBAL
```

The universal condition is true for empty `L`. The existential condition is
false for empty `Q`. The inherited D13 root-class map remains authoritative:
`STRUCTURAL_Q_NON_GLOBAL` is a non-global `Q` image on the branch where all
`L` images are global. `STRUCTURAL_ONLY_LOW_IMAGE` does not satisfy the second
predicate. Neither predicate is a new bank field, basis field, row, event,
counter, or digest input.

The record predicates, `all_Q_images_global`, `low_hit`, and every basis row
remain immutable after basis commit. They do not depend on final status.

### 1.3 Exact final serialized bit

For every `basis_committed=1` bank, serialize

```text
decoder_strict_structural_hit = 1
```

if and only if all four conditions hold:

```text
final status is ELIGIBLE
quotient_defined = 1
all_L_images_global = 1
basis_has_nonglobal_Q = 1
```

Serialize zero otherwise. In particular, every `RESOURCE_REJECT 1 1` bank
serializes zero even if its immutable basis stream contains one or more
`STRUCTURAL_Q_NON_GLOBAL` records. The zero is a final eligibility-gated
claim; it does not rewrite the records or their digest.

For `basis_committed=0`, the field is still the literal absent value `-`.
The complete empty core has no `Q` record and therefore serializes zero after
an `ELIGIBLE 1 1` outcome. Reaching basis commit already excludes an inherited
generation-stage stop, so this formula is equivalent to D09's exact
decoder-strict definition rather than a relaxation of it.

The heldout finite-label computation counts only the final serialized bit.
An ineligible bank cannot contribute a decoder-strict hit. Its sticky factor
events still contribute to the inherited other-factor and null decisions.

## 2. Exact 34-field schema and presence

The D16 bank header survives byte-for-byte:

```text
version	split	factor_bits	shape	index	N	A_0	B_0	A_1	B_1	status	K	row_count	peel_committed	basis_committed	survivor_count	kernel_dimension	singleton_count	support_two_count	L_dimension	Q_dimension	quotient_defined	all_Q_images_global	decoder_strict_structural_hit	low_hit	observed_factor	event_count	event_sha256	row_stream_sha256	peel_sha256	basis_sha256	decoder_reservation	decoder_call_count	bank_nonce
```

It has exactly 34 fields and 33 tabs. No `all_L_images_global` or
`basis_has_nonglobal_Q` field is added.

Let `IMMUTABLE_DOWNSTREAM` denote, in header order,

```text
kernel_dimension singleton_count support_two_count L_dimension Q_dimension
quotient_defined all_Q_images_global low_hit
```

D17 replaces D16's use of the nine-field `DOWNSTREAM` bundle by this exact
presence table. All scalar-row and digest columns are repeated to make the
replacement total.

| `peel_committed` | `basis_committed` | `survivor_count` | `IMMUTABLE_DOWNSTREAM` | `decoder_strict_structural_hit` | Scalar-row peel fields | `peel_sha256` | Basis rows | `basis_sha256` |
|---:|---:|---|---|---|---|---|---|---|
| 0 | 0 | `-` | all eight `-` | `-` | all four `-` on every row | empty hash | none | empty hash |
| 1 | 0 | exact `DEC` | all eight `-` | `-` | all four exact on every row | exact full stream | none | empty hash |
| 1 | 1 | exact `DEC` | all eight exact | exact final `BOOL` from Section 1.3 | all four exact on every row | exact full stream | complete canonical stream | exact full stream |

No other presence combination is legal. D16's coefficient-pair rules,
`survivor_count` constraints, dimension equation, basis-row count, canonical
order, empty-stream disambiguation, and all always-present fields survive.
Only the time at which the existing hit field acquires its exact Boolean value
changes.

The complete empty core retains D16's exact assignments, including

```text
peel_committed                    1
basis_committed                   1
survivor_count                    0
quotient_defined                  1
all_Q_images_global               1
decoder_strict_structural_hit     0
low_hit                           0
decoder_reservation               0
decoder_call_count                0
```

and all five zero dimension/count values. It publishes no basis row and uses
the empty basis hash.

## 3. Granted-quota meaning of `decoder_reservation`

### 3.1 Exact state transition

Every bank initializes

```text
decoder_reservation = 0
decoder_call_count  = 0
```

`decoder_reservation` is the historical amount of scalar-gcd quota granted to
that bank by the inherited D09 packet ledger. Its only possible transition is

```text
0 -> 91111
```

and that transition commits atomically when the ledger grants a nonempty
residual's fixed request. A request is not a grant. A denied request leaves
the field zero and never enters F271.

When the bank finishes or rejects after a grant, the ledger commits the actual
calls and returns the unused part of the active reservation exactly as D09
requires. That return changes packet-ledger `A`; it does not reverse the bank
field. A later resource outcome also cannot reverse it. Thus a final value of
`91111` means that the grant occurred, even when `decoder_call_count=0`.

Every bank must satisfy

```text
decoder_reservation in {0,91111}
decoder_call_count <= decoder_reservation
```

Both fields use canonical unsigned `DEC`. The inherited actual-call counter
and packet-ledger equations remain exact. In particular, a rejected or failed
post-grant decoder retains every call actually committed before returning its
unused balance.

### 3.2 Exact assignment by chronology

The assignments are:

| Chronology | `decoder_reservation` | `decoder_call_count` |
|---|---:|---:|
| Source stops or rejects before complete peel | 0 | 0 |
| Complete peel leaves more than 64 survivors | 0 | 0 |
| Nonempty residual request is denied | 0 | 0 |
| Other outcome before a grant | 0 | 0 |
| Grant occurs, then a recoverable outcome occurs before basis commit | 91111 | exact committed value in `[0,91111]` |
| Complete zero core, whether later status is `ELIGIBLE` or `RESOURCE_REJECT` | 0 | 0 |
| Complete nonempty eligible core | 91111 | exact committed value in `[0,91111]` |
| Complete nonempty basis, then a recoverable pre-core outcome | 91111 | exact committed value in `[0,91111]` |

A nonempty all-unit F271 input can legitimately have reservation `91111` and
call count zero. No rule requires a positive call count after a grant.

## 4. Replacement terminal-status table

This table replaces D16 Section 3's table. It changes no inherited status
precedence or fatal boundary.

| Terminal circumstance | Final status | Commit pair | Hit field | Reservation |
|---|---|---|---|---:|
| Curve, affine, or `ROW_ROOT` generation factor stops source, with no later resource override | `DIRECT_STOP` | `0 0` | `-` | 0 |
| Full row gcd, infinity, or unresolved affine exception stops source, with no later resource override | `BANK_SKIP` | `0 0` | `-` | 0 |
| Sampler, proposal, source, pre-peel arena, record, or writer resource outcome | `RESOURCE_REJECT` | `0 0` | `-` | 0 |
| Complete peel leaves more than 64 survivors | `RESOURCE_REJECT` | `1 0` | `-` | 0 |
| Nonempty residual is denied its packet reservation | `RESOURCE_REJECT` | `1 0` | `-` | 0 |
| Recoverable outcome after peel but before a grant or basis commit | `RESOURCE_REJECT` | `1 0` | `-` | 0 |
| Grant occurs, then a recoverable outcome occurs before basis commit | `RESOURCE_REJECT` | `1 0` | `-` | 91111 |
| Complete zero core and all required core records commit | `ELIGIBLE` | `1 1` | 0 | 0 |
| Complete nonempty F271/basis/classification core commits | `ELIGIBLE` | `1 1` | Section 1.3 formula | 91111 |
| Complete zero-survivor core, then a recoverable non-basis outcome occurs before public core commit | `RESOURCE_REJECT` | `1 1` | 0 | 0 |
| Complete nonempty basis, then a recoverable non-basis outcome occurs before public core commit | `RESOURCE_REJECT` | `1 1` | 0 | 91111 |

The inherited resource-first precedence still permits `RESOURCE_REJECT 0 0`
after an earlier generation factor. A low or structural factor remains sticky
through `RESOURCE_REJECT 1 0` or `RESOURCE_REJECT 1 1`. Every reached event,
counter, committed stage, and granted reservation remains public.

`DIRECT_STOP` and `BANK_SKIP` require `0 0`. `ELIGIBLE` requires `1 1`.
`RESOURCE_REJECT` can use all three legal commit pairs. An invariant,
authentication failure, packet-output overflow, containment failure, signal,
abnormal child exit, or common-deadline failure still aborts the applicable
process and produces no success manifest or finite label. No synthetic bank
row is serialized for such a failure.

After public core commit, an inherited diagnostic timeout, detail omission, or
writer failure retains `ELIGIBLE` and every core byte. It therefore uses the
same hit and reservation assignment as the corresponding successful empty or
nonempty eligible core.

## 5. Projection, replay, and digest preimages

D15's exact row, peel, and basis suffix preimages survive byte-for-byte. The
basis suffix contains basis records and their root classes, not the final bank
hit bit. A `STRUCTURAL_Q_NON_GLOBAL` record therefore remains in the immutable
basis preimage for a later `RESOURCE_REJECT 1 1` bank. The final zero bit does
not change `basis_sha256`.

Evaluation retains D16's flag-driven row, peel, and basis reconstruction. Once
it has reconstructed the complete basis stream, it independently derives
`all_L_images_global` and `basis_has_nonglobal_Q` from the projected basis rows.
After it validates final bank status, it derives Section 1.3's bit and requires
exact equality with the bank summary.

Evaluation also requires the exact reservation state generated by the
canonical packet-ledger chronology and requires
`decoder_call_count<=decoder_reservation`. The stage, survivor, status, and
reservation constraints in Sections 2--4 are simultaneous requirements, not
alternative inferences.

Replay repeats both derivations from regenerated immutable records and from
the authenticated committed TSV rows. It requires exact identity of the final
status, hit bit, grant value, actual call count, basis rows, basis digest,
events, flags, fields, counters, and complete wrapped public files. A mismatch
is fatal and permits no success manifest or finite label.

The bank file's inherited full-file digest covers the final serialized bit and
reservation value. The split core manifests still hash the complete wrapped
public files. Event digest preimages remain distinct. No digest continues from
a final digest value, and D17 introduces no circular preimage.

## 6. Unchanged widths and caps

The literal bank header is still exactly 405 bytes including LF. The maximum
all-present data row retains D16's exact calculation:

```text
8+9+2+9+2+37+4*30+1+3+3+2+3+2+2+4+2+2+5+3+4*64+5+5+10+34
= 529 bytes.
```

The final hit remains a one-byte Boolean. `decoder_reservation` remains at
most the five-byte value `91111`. The 16,384-byte bank-row cap therefore keeps
15,855 bytes of slack. Both bank files still use at most

```text
468*529 + 2*405 = 248,382 bytes.
```

No row or file is added. Every D16 bank, scalar, basis, event, total-output,
temporary, directory-peak, per-file, arena, RSS, operation, timer, process,
and deadline cap survives unchanged.

## 7. D17 roots, names, and source tokens

The D17 materializer theory root is the SHA-256 of twenty LF-terminated lines.
The first nineteen lines are the import table above in displayed order. The
twentieth line is the final SHA-256 of this
`D17_DRAFT_PREREGISTRATION.md` byte as authenticated by a future D17 theory
audit. Every line is `filename`, tab, hash, LF. The materializer and
independently authored verifier pin all twenty names, hashes, and their order.
This twenty-line rule replaces D16's eighteen-line rule.

All fixture filenames, payload and verification manifests, evaluation files,
replay files, seal files, diagnostic files, private files, and their root
constructions retain their D16 rules with `F265-D17` prefixes. The four source
roles and ten invocation grammars retain their D16 rules with `f265_d17_`
prefixes.

The future public source contains exactly one occurrence of each token:

```text
@F265_D17_FIXTURE_PAYLOAD_ROOT@
@F265_D17_FIXTURE_VERIFICATION_ROOT@
```

The future private source contains one separate occurrence of each same token.
The four-occurrence one-edit replacement, fresh source evidence, and fresh
hostile source-audit requirement survive unchanged. Materializer and verifier
source contain no placeholder.

## 8. Authorization and fresh-audit gate

No D17 mode is authorized to execute under this draft. A fresh no-context D17
theory audit must authenticate all nineteen inputs and audit the complete
D09--D17 additive composition. It must try to kill final-status derivation,
immutability of basis records under `RESOURCE_REJECT 1 1`, root-class
projection, empty-core behavior, every reservation transition and status
pairing, actual-call bounds, two-way reconstruction, preimages, field count,
width arithmetic, root construction, unchanged caps, and the absolute
containment boundary.

A D17 theory PASS may authorize only drafting the four D17 source roles. It
does not authorize source freezing, a source PASS, compilation, a fixture byte,
fixture verification, preflight, local or remote execution, a result,
packaging, staging, commit, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D17 supplies no
runner, launch command, or fallback.
