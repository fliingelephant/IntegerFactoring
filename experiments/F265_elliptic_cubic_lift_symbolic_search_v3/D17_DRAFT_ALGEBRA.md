# F265-D17 draft algebra amendment — final hit and granted quota

## Status and exact construction

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

D17 has exactly these authenticated predecessor bytes:

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

Read all eighteen authenticated bytes in full. Apply only the replacements and
additions in this file and in `D17_DRAFT_PREREGISTRATION.md`. Every D09--D16
clause not explicitly replaced by D17 survives literally. Preserve every
predecessor byte.

The D11 and D14 hostile PASS artifacts remain evidence only for their exact
authenticated compositions. They do not transfer to D15, D16, or D17. No D15
or D16 hostile-audit artifact is imported.

## 1. Exact repair scope

D17 repairs exactly two unresolved D16 interface meanings.

First, a decoder-strict structural hit is a final eligible-bank claim. It is
not an immutable basis-stage fact. D17 removes
`decoder_strict_structural_hit` from the D16 basis-transition payload. The
complete canonical basis rows and their root classes remain immutable. The
existing bank field is derived from those records only after final bank status
is fixed.

For a committed basis, define the status-independent logical predicates

```text
all_L_images_global
basis_has_nonglobal_Q
```

directly from the committed canonical basis records. The first is true exactly
when every required `L` image is global under the inherited root semantics.
The second is true exactly when at least one `Q` record has root class
`STRUCTURAL_Q_NON_GLOBAL`. These predicates are not new serialized fields.

The final serialized bank bit is one exactly when

```text
status == ELIGIBLE
and quotient_defined == 1
and all_L_images_global
and basis_has_nonglobal_Q
```

It is zero for every `RESOURCE_REJECT 1 1` bank. That final zero does not
change or erase a basis row, root class, basis digest, event, factor, or
counter. For a bank without a committed basis, the field remains the literal
absent value `-` under D16.

Second, `decoder_reservation` means the bank's historically granted F271
scalar-gcd quota. It starts at zero and changes atomically to exactly `91111`
only when the inherited packet ledger grants that nonempty residual's request.
A denial leaves it zero. Returning unused active quota changes the packet
ledger but never changes this bank field back to zero. Thus the field records
a grant, not a request, an active balance, actual calls, or final status.

Always require

```text
0 <= decoder_call_count <= decoder_reservation
decoder_reservation in {0,91111}
```

Source stops, residuals above 64, denied requests, and empty cores have zero
reservation and zero decoder calls. Every admitted nonempty decoder that
received a grant retains `91111`, including after unused quota is returned or
a later recoverable resource outcome occurs. Its actual call count can be
zero.

## 2. Preserved mathematics, chronology, and evidence

D17 changes no source law, random stream, factor-first chronology, affine
operation, prospective-row test, simultaneous peel, F271 V2 operation, kernel,
low basis, structural complement, normalized root, root-class map, fixture
operand, operation counter, packet-ledger cap, rate denominator, projection
formula, finite-label precedence, diagnostic, private firewall, containment
gate, theorem boundary, or scope claim.

The inherited fact that reaching basis commit excludes a generation-stage
stop makes D17's final formula equivalent to D09's four-part eligible-bank
definition. A later low or structural factor remains sticky, but it does not
turn an ineligible bank into a decoder-strict hit. The finite structural label
counts only final serialized hit bits.

D15's row, peel, and basis digest preimages remain exact. In particular, the
status-independent `STRUCTURAL_Q_NON_GLOBAL` record stays in the basis suffix
even when a later resource outcome makes the final bank bit zero. D17 adds no
field, row, file, digest input, counter, allocation, operation, or deadline.

## 3. Mechanical D17 composition

D17 replaces every future source-version token `F265-D16`, executable prefix
`f265_d16_`, artifact prefix `F265-D16.`, and fixture-root placeholder prefix
`F265_D16_` by the corresponding D17 token. This replacement applies only to
future artifacts and source. It does not rename or modify a predecessor file.
The version text `F265-D17` remains eight bytes.

The D17 materializer theory root includes the eighteen predecessor hashes
above, the final hash of this D17 algebra amendment, and the final hash of the
D17 preregistration amendment. The D17 preregistration fixes their exact line
order. No other root construction changes.

The unchanged 34-field bank header and its 529-byte maximum row remain exact.
The value `91111` has the already registered five-byte reservation width.
Consequently, every D16 row, file, temporary, directory, arena, RSS, operation,
timer, process, and deadline cap survives unchanged.

## 4. Authorization boundary

A fresh no-context D17 theory PASS may authorize only source drafting for the
four D17 roles. It does not authorize source freezing, a source PASS,
compilation, fixture materialization, fixture verification, preflight,
evaluation, replay, sealing, diagnostics, private classification, packaging,
result release, remote execution, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D17 contains no
source, fixture byte, runner, launch command, containment fallback, or
execution authorization.
