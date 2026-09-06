# F265-D16 draft preregistration amendment — total bank-stage serialization

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

Read all seventeen authenticated bytes in full. Apply only the replacements
and additions below. Every D09--D15 clause not explicitly replaced by D16
survives literally. Preserve every predecessor byte.

D16 replaces every future source-version token `F265-D15`, executable prefix
`f265_d15_`, artifact prefix `F265-D15.`, and fixture-root placeholder prefix
`F265_D15_` by the corresponding D16 token. The four source roles, eight modes,
ten invocation grammars, option names, non-bank schemas, caps, and role
restrictions otherwise survive exactly.

## 1. Exact bank-stage state

### 1.1 Two commit flags

Every bank starts with

```text
peel_committed=0 basis_committed=0.
```

The flags are `BOOL`. They change only through the monotone transitions

```text
0 0  ->  1 0  ->  1 1.
```

No transition is reversed. `0 1` is illegal. A repeated transition, partial
flag write, or disagreement between internal and public flags is a split-fatal
invariant failure and permits no success manifest or finite label.

The flags record bank-local evidence stages, not the final bank status. The
inherited status precedence remains authoritative. In particular,
`RESOURCE_REJECT` can occur at any of the three legal evidence stages when an
inherited recoverable resource outcome occurs before public core commit.

### 1.2 Peel commit

The `0 0 -> 1 0` transition occurs atomically only after both complete source
orbits reach the inherited peel boundary and all simultaneous-peel values over
the original admitted row set have been constructed and checked in bank-local
temporary state. The immutable transition payload is:

- every row's `peel_g`, `peel_b`, `peel_b_square`, and `survivor` value;
- the exact `survivor_count`; and
- the complete D15 peel-suffix stream and `peel_sha256`.

No computed prefix or abandoned temporary enters that payload. A later
decoder, reservation, basis, record, writer, or other recoverable non-peel
resource outcome cannot erase or change it.

### 1.3 Basis commit

The `1 0 -> 1 1` transition occurs atomically only after one of these two
chronological branches completes.

1. If `survivor_count=0`, commit the inherited exact empty-core certificate,
   empty `L` and `Q`, vacuous classifications, and empty basis stream.
2. If `1<=survivor_count<=64`, complete the admitted F271 decoder, full kernel,
   canonical low basis `L`, canonical complement `Q`, every root
   classification in ordinal order, every basis record, and the complete D15
   basis-suffix stream.

A residual above 64 and a denied packet reservation never enter either branch.
They leave `basis_committed=0`. Any invariant failure after F271 admission is
still split-fatal under D10; D16 does not convert it to a stage absence or a
resource result.

The second flag is named `basis_committed`, not `decoder_committed`. The empty
branch takes no decoder reservation and executes no F271 decoder, while both
branches reach the same downstream mathematical-publication boundary. The flag
therefore names that common boundary and does not falsely claim decoder work in
the empty case.

The immutable basis transition payload is:

```text
kernel_dimension singleton_count support_two_count L_dimension Q_dimension
quotient_defined all_Q_images_global decoder_strict_structural_hit low_hit
basis rows basis_sha256
```

A later recoverable non-basis record or writer outcome before public core
commit can select `RESOURCE_REJECT`, but it cannot erase or change this
payload. After public core commit, diagnostics retain their inherited
noninterference rule: timeout, detail omission, or writer failure does not
change bank status, either stage flag, or any core byte.

## 2. Replacement bank schema and field presence

### 2.1 Literal 34-field header

This header replaces the D13 bank header and every inherited prefixed copy:

```text
version	split	factor_bits	shape	index	N	A_0	B_0	A_1	B_1	status	K	row_count	peel_committed	basis_committed	survivor_count	kernel_dimension	singleton_count	support_two_count	L_dimension	Q_dimension	quotient_defined	all_Q_images_global	decoder_strict_structural_hit	low_hit	observed_factor	event_count	event_sha256	row_stream_sha256	peel_sha256	basis_sha256	decoder_reservation	decoder_call_count	bank_nonce
```

It has exactly 34 fields and 33 tabs. The two commit fields are `BOOL`.
`survivor_count` is `DEC or -`. The five dimension/count fields beginning with
`kernel_dimension` are `DEC or -`. The four fields beginning with
`quotient_defined` are `BOOL or -`. These are the only new bank-field absence
permissions. D13's coefficient-pair absence rule survives unchanged.

The following fields are always present and retain their inherited exact
types and meanings:

```text
version split factor_bits shape index N A_0 B_0 A_1 B_1 status K row_count
peel_committed basis_committed observed_factor event_count event_sha256
row_stream_sha256 peel_sha256 basis_sha256 decoder_reservation
decoder_call_count bank_nonce
```

In particular, `observed_factor`, event evidence, reservation and actual-call
counts, and all counter rows are never `-`. They retain every operation and
sticky event actually committed before a later outcome. A zero in one of these
operational fields keeps its inherited operational meaning; it is not a
substitute for an absent mathematical object.

### 2.2 Exact presence table

Let `DOWNSTREAM` denote, in header order,

```text
kernel_dimension singleton_count support_two_count L_dimension Q_dimension
quotient_defined all_Q_images_global decoder_strict_structural_hit low_hit.
```

Every bank row satisfies exactly one table row:

| `peel_committed` | `basis_committed` | `survivor_count` | `DOWNSTREAM` | Scalar-row peel fields | `peel_sha256` | Basis rows | `basis_sha256` |
|---:|---:|---|---|---|---|---|---|
| 0 | 0 | `-` | all nine `-` | all four `-` on every row | empty hash | none | empty hash |
| 1 | 0 | exact `DEC` | all nine `-` | all four exact on every row | exact full stream | none | empty hash |
| 1 | 1 | exact `DEC` | all nine exact | all four exact on every row | exact full stream | complete canonical stream | exact full stream |

No other presence combination is legal. In particular, a zero value is legal
in a mathematical field only after that field's stage commits and its exact
mathematical value is zero.

Because peel commit requires both complete inherited orbits,
`peel_committed=1` also requires both coefficient pairs present and
`row_count=2*K`. A `1 0` bank requires `survivor_count>=1`; a committed
zero-survivor peel must take the complete empty-core transition in Section 2.3.
A `1 1` bank requires `survivor_count<=64`.

For `basis_committed=1`, require

```text
kernel_dimension = L_dimension + Q_dimension
basis data-row count = L_dimension + Q_dimension.
```

The basis rows are `L` then `Q` in inherited canonical order. If both
dimensions are zero, the complete basis stream has zero lines and its digest
is the empty hash.

### 2.3 Complete empty core

A committed peel with zero survivors immediately takes the empty branch in
Section 1.3. Its exact state is:

```text
peel_committed                    1
basis_committed                   1
survivor_count                    0
kernel_dimension                  0
singleton_count                   0
support_two_count                 0
L_dimension                       0
Q_dimension                       0
quotient_defined                  1
all_Q_images_global               1
decoder_strict_structural_hit     0
low_hit                           0
decoder_reservation               0
decoder_call_count                0
```

It publishes no basis row and uses the empty basis hash. This is the inherited
D10 empty-core certificate. It is distinct from `0 0`, which has no peel, and
from `1 0`, which has no committed kernel or basis evidence.

This section replaces D15's no-peel assignment `survivor_count=0` by the
literal absence assignment `survivor_count=-`. All other D15 scalar-row and
digest rules survive.

## 3. Reachable terminal circumstances and status

The evidence flags and the inherited final status are validated together:

| Terminal circumstance | Final status | Commit pair |
|---|---|---|
| Curve, affine, or `ROW_ROOT` generation factor stops source, with no later resource override | `DIRECT_STOP` | `0 0` |
| Full row gcd, infinity, or unresolved affine exception stops source, with no later resource override | `BANK_SKIP` | `0 0` |
| Sampler, proposal, source, pre-peel arena, record, or writer resource outcome | `RESOURCE_REJECT` | `0 0` |
| Complete peel leaves more than 64 survivors | `RESOURCE_REJECT` | `1 0` |
| Nonempty residual is denied its packet reservation | `RESOURCE_REJECT` | `1 0` |
| Recoverable decoder, basis, record, or writer outcome before basis commit | `RESOURCE_REJECT` | `1 0` |
| Complete zero core and all required core records commit | `ELIGIBLE` | `1 1` |
| Complete nonempty F271/basis/classification core commits | `ELIGIBLE` | `1 1` |
| Basis commits, then an inherited recoverable non-basis outcome occurs before public core commit | `RESOURCE_REJECT` | `1 1` |

The inherited resource-first precedence also permits `RESOURCE_REJECT 0 0`
after an earlier generation factor if a later pre-core resource outcome is
reached. The generation factor remains sticky. A low or structural factor can
be followed by a recoverable outcome before basis commit, giving
`RESOURCE_REJECT 1 0`, or after basis commit, giving `RESOURCE_REJECT 1 1`.
Every reached event remains public in either case.

`DIRECT_STOP` and `BANK_SKIP` require `0 0`. `ELIGIBLE` requires `1 1`.
`RESOURCE_REJECT` alone does not identify a commit stage; the two flags do.
An invariant, authentication failure, packet-output overflow, containment
failure, signal, abnormal child exit, or common-deadline failure still aborts
the applicable process and produces no success manifest or finite label. Such
failures do not serialize a synthetic bank status or commit pair.

## 4. Flag-driven TSV reconstruction and replay

D15's exact row, peel, and basis suffix preimages survive byte-for-byte. D16
replaces only the presence inference in D15 Section 1.4 by this flag-driven
validation.

For each bank, evaluation groups public data rows by the exact five wrapper
fields `version,split,factor_bits,shape,index` and requires one matching bank
summary. Every scalar and basis row must be consumed by exactly one such group;
an unmatched row, duplicate row, or duplicate bank summary is fatal. Evaluation
then independently projects the rendered TSV records:

1. Select the seven D15 source fields from exactly `row_count` scalar rows.
   Reconstruct `row_stream_sha256` regardless of either commit flag.
2. If `peel_committed=0`, require all four peel fields absent on every scalar
   row and require the empty peel hash. If `peel_committed=1`, require all four
   fields present on every scalar row, reconstruct exactly `row_count` peel
   suffix lines, require their hash, and require `survivor_count` to equal the
   sum of survivor bits.
3. If `basis_committed=0`, require zero basis rows and the empty basis hash. If
   `basis_committed=1`, require exactly `L_dimension+Q_dimension` canonical
   basis rows and reconstruct the complete D15 basis suffix and hash.

The split meta `basis_count`, the `basis.tsv` data-row count, and the sum of
`L_dimension+Q_dimension` over exactly the banks with `basis_committed=1` must
be equal. A bank with `basis_committed=0` contributes zero. This includes basis
rows retained by a later `RESOURCE_REJECT 1 1` bank. D15's split-local row
count equation survives unchanged.

Evaluation requires equality between the logical-record digests, projected
TSV digests, and bank-summary digests before a success manifest. Replay repeats
the stage validation and both digest computations from regenerated immutable
records and from the authenticated committed TSV rows. It also requires exact
flag, field-presence, count, status, counter, event, and byte identity. Any
disagreement is fatal and permits no success manifest or finite label.

The split core manifests continue to hash the complete wrapped public files.
Event digest preimages remain distinct. No digest continues from a final digest
value.

## 5. Header width and unchanged caps

The replacement bank data row has 34 fields. In the registered corpus, the
maximum complete all-present row has these field-width bounds:

```text
version 8, split 9, factor_bits 2, shape 9, index 2, N 37,
four curve coefficients 4*30, status 1, K 3, row_count 3,
two commit flags 2, survivor_count 3,
kernel/singleton counts 2 each, support_two_count 4,
L/Q dimensions 2 each, five remaining Boolean fields 5,
event_count 3, four SHA-256 fields 4*64,
decoder reservation and call count 5 each, bank_nonce 10,
33 tabs and one LF 34.
```

Therefore its exact field-wise maximum is

```text
8+9+2+9+2+37+4*30+1+3+3+2+3+2+2+4+2+2+5+3+4*64+5+5+10+34
= 529 bytes.
```

An absent value has one byte and cannot increase this maximum. The unchanged
16,384-byte bank-summary cap therefore has at least 15,855 bytes of slack for
every data row. The literal 34-field header is exactly 405 bytes including LF.
Across both split bank files, 468 maximum data rows and two headers use at most

```text
468*529 + 2*405 = 248,382 bytes,
```

which is below the unchanged 7,667,712-byte bank-summary category. No scalar,
basis, or event row gains a field. No new data row or file is created.

Consequently, the inherited 468-bank summary category, 512-byte scalar-row
cap, 256-byte event-row cap, 226,088,448-byte total output cap, 262,400-byte
one-bank temporary cap, 309,990,912-byte directory-peak cap, 128 MiB per-file
cap, arena and RSS caps, and every operation, timer, process, and deadline cap
remain unchanged. The two flags occupy the already reserved 16,384-byte bank
summary allocation; they add no category or temporary allocation.

## 6. D16 roots, names, and source tokens

The D16 materializer theory root is the SHA-256 of eighteen LF-terminated
lines. The first seventeen lines are the import table above in displayed
order. The eighteenth line is the final SHA-256 of this
`D16_DRAFT_PREREGISTRATION.md` byte as authenticated by a future D16 theory
audit. Every line is `filename`, tab, hash, LF. The materializer and
independently authored verifier pin all eighteen names, hashes, and their
order. This eighteen-line rule replaces every inherited reference to the
sixteen-line D15 rule.

All fixture filenames, payload and verification manifests, evaluation files,
replay files, seal files, diagnostic files, private files, and their root
constructions retain their D15 rules with `F265-D16` prefixes. The four source
roles and ten invocation grammars retain their D15 rules with `f265_d16_`
prefixes.

The future public source contains exactly one occurrence of each token:

```text
@F265_D16_FIXTURE_PAYLOAD_ROOT@
@F265_D16_FIXTURE_VERIFICATION_ROOT@
```

The future private source contains one separate occurrence of each same token.
The four-occurrence one-edit replacement, fresh source evidence, and fresh
hostile source-audit requirement survive unchanged. Materializer and verifier
source contain no placeholder.

## 7. Authorization and fresh-audit gate

No D16 mode is authorized to execute under this draft. A fresh no-context D16
theory audit must authenticate all seventeen inputs and audit the complete
D09--D16 additive composition. It must try to kill the commit transitions,
all three presence rows, every status pairing and sticky-event case, the empty
core, flag-driven TSV reconstruction, replay, field count, width arithmetic,
root construction, unchanged caps, and the absolute containment boundary.

A D16 theory PASS may authorize only drafting the four D16 source roles. It
does not authorize source freezing, a source PASS, compilation, a fixture byte,
fixture verification, preflight, local or remote execution, a result,
packaging, staging, commit, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D16 supplies no
runner, launch command, or fallback.
