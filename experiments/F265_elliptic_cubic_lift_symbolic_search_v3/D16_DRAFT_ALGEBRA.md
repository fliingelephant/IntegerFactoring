# F265-D16 draft algebra amendment — explicit bank-stage evidence

## Status and exact construction

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

D16 has exactly these authenticated predecessor bytes:

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

Read all sixteen authenticated bytes in full. Apply only the replacements and
additions in this file and in `D16_DRAFT_PREREGISTRATION.md`. Every D09--D15
clause not explicitly replaced by D16 survives literally. Preserve every
predecessor byte.

The D14 hostile PASS remains evidence only for the exact authenticated
D09--D14 composition. It does not transfer to D15 or D16. D15 received no
hostile theory PASS, and no D15 hostile-audit artifact is imported.

## 1. Exact repair scope

D15 made admitted rows and absent peel and basis streams public, but the
inherited bank schema still required mathematical fields whose objects do not
exist when peel or basis construction has not committed. D16 repairs exactly
that interface defect.

D16 adds two public evidence bits:

```text
peel_committed basis_committed
```

They record completed immutable bank stages. They are not mathematical values,
resource outcomes, eligibility claims, or substitutes for bank status. The
only legal pairs are `0 0`, `1 0`, and `1 1`. The pair `0 1` is a split-fatal
invariant failure.

No undefined mathematical object is encoded as zero. A field is exact when its
own stage committed and is the literal absent value `-` otherwise. The separate
preregistration fixes the complete presence table and the exact replacement
bank schema.

## 2. Stage meanings

`peel_committed=1` means that the complete mixed source reached the inherited
peel boundary and the full simultaneous peel over the original admitted row
set atomically committed. Every admitted row then has its exact peel values.
The flag and values remain immutable through a later decoder, record, writer,
or other recoverable non-peel resource outcome.

`basis_committed=1` means that the empty-core certificate or the complete
admitted F271 result, full kernel, canonical `L` and `Q`, every root
classification, every basis record, and the complete basis digest atomically
committed. The flag and values remain immutable through a later recoverable
non-basis resource outcome. Post-commit diagnostics retain their inherited
noninterference rule and cannot change bank status or either flag.

A complete peel with zero survivors is not an absent peel or absent basis. It
has `peel_committed=1`, `basis_committed=1`, the inherited exact empty-core
zero/true values, no basis row, and the empty basis-stream hash.

## 3. Preserved mathematics and evidence

D16 changes no source law, random stream, factor-first chronology, affine
operation, prospective-row test, simultaneous peel, F271 V2 operation, kernel,
low basis, structural complement, normalized root, fixture operand, operation
counter, rate denominator, projection formula, finite label, diagnostic,
private firewall, containment gate, theorem boundary, or scope claim.

Rows and `row_stream_sha256` always publish exactly as D15 requires. Peel and
basis digest preimages remain exactly D15's. D16 changes only the bank-level
presence evidence and its validation. Operational status, reservation and call
counts, sticky factor state, event counts, event digests, and all packet and
bank counters retain their inherited total meanings.

## 4. Mechanical D16 composition

D16 replaces every future source-version token `F265-D15`, executable prefix
`f265_d15_`, artifact prefix `F265-D15.`, and fixture-root placeholder prefix
`F265_D15_` by the corresponding D16 token. This replacement applies only to
future artifacts and source. It does not rename or modify a predecessor file.
The version text `F265-D16` remains eight bytes.

The D16 materializer theory root includes the sixteen predecessor hashes
above, the final hash of this D16 algebra amendment, and the final hash of the
D16 preregistration amendment. The D16 preregistration fixes their exact line
order. No other root construction changes.

## 5. Authorization boundary

A fresh no-context D16 theory PASS may authorize only source drafting for the
four D16 roles. It does not authorize source freezing, a source PASS,
compilation, fixture materialization, fixture verification, preflight,
evaluation, replay, sealing, diagnostics, private classification, packaging,
result release, remote execution, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D16 contains no
source, fixture byte, runner, launch command, containment fallback, or
execution authorization.
