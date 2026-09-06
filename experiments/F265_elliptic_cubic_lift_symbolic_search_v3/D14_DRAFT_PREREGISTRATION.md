# F265-D14 draft preregistration amendment — exact serialized-width repair

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

Read all twelve authenticated bytes in full. Apply only the two arithmetic
paragraph replacements and the mechanical D14 composition rules below. Every
D09--D13 clause not explicitly replaced by D14 survives literally. Preserve
every predecessor byte.

The triggering fresh hostile theory/interface review was performed in Codex
task `/root/hostile_f277` against the exact D13 hashes above and all nine
predecessor bytes explicitly imported by the D13 algebra amendment. Its exact
verdict text was:

```text
Verdict: FAIL — REVISE.
```

The review reported exactly two non-safety arithmetic errors, both caused by
using the seven-byte split spelling `heldout` where the nine-byte spelling
`discovery` is longer. It reported no deeper blocker and found every hard cap
safe. The PASS-only review instruction prohibited creation of
`D13_HOSTILE_THEORY_AUDIT.md`; no such file or audit SHA exists. This message
provenance triggers D14 but is not an authenticated artifact or a D14 audit.

## 1. Replacement of the D13 event-width paragraph

Replace only the paragraph in D13 Section 4.3 beginning `The inherited D09 raw
event cap` and ending `explicit slack.` with the following paragraph. The
change from D13 to D14 in the wrapper name is the mechanical version change.

The inherited D09 raw event cap is 192 bytes including LF. The D14 wrapper adds
at most 8 version bytes, 9 split bytes (`discovery`), 2 factor-bit bytes, 9
shape bytes, 2 index bytes, and 5 tabs, for at most 227 bytes. The literal
header is 157 bytes. Thus the 256-byte line cap has 29 bytes of explicit slack.

No other sentence, formula, cap, or total in D13 Section 4.3 changes.

## 2. Replacement of the D13 scalar-row-width paragraph

Replace only the D13 Section 5 calculation beginning `For the maximum data
row` and ending `before using any scalar row.` with the following text.

For the maximum data row, `version` has 8 bytes, `discovery` 9, factor bits 2,
`safe-safe` 9, index 2, original row 3, curve 1, scalar 3, `u,v` 30 each,
`a,peel_g,peel_b` 91 each, carry at most 62 including a sign, two Booleans 1
each, and the 15 tabs plus LF use 16. Therefore

```text
8+9+2+9+2+3+1+3+2*30+3*91+62+2+16 = 450 bytes.
```

The literal 512-byte row cap has 62 bytes of slack. The D09 bank-summary cap
remains 16,384 bytes. The two-byte index bound is the maximum authenticated
spelling among the retained rows of both pinned public corpus files. Replay
regenerates both coefficients and requires exact agreement with the bank row
before using any scalar row.

No other sentence, schema, field, or order in D13 Section 5 changes.

## 3. Mechanical D14 composition and roots

D14 replaces every future source-version token `F265-D13`, executable prefix
`f265_d13_`, artifact prefix `F265-D13.`, and fixture-root placeholder prefix
`F265_D13_` by the corresponding D14 token. This replacement applies only to
future artifacts and source. It does not rename or modify a predecessor file.
The version text `F265-D14` remains eight bytes.

The D14 materializer theory root is the SHA-256 of thirteen LF-terminated
lines. The first twelve lines are the import table above in displayed order.
The thirteenth line is the final SHA-256 of this D14 preregistration as
authenticated by a future D14 theory audit. Each line is `filename`, tab,
hash, LF. The materializer and independently authored verifier pin all
thirteen values. This thirteen-line rule replaces each inherited reference to
the eleven-line D13 rule.

All fixture filenames, manifests, payload roots, verification roots, replay
roots, sealed-decision roots, and diagnostic roots retain their D13
construction with D14 prefixes. The public and private source drafts each use
one occurrence of each corresponding invalid D14 fixture-root placeholder,
for four occurrences total. Their later one-edit replacement rule is
unchanged. No other root construction changes.

## 4. Explicitly unchanged schemas, caps, totals, and algorithms

The event schema and 256-byte event-row cap are unchanged. These D13 totals
remain exact and unchanged:

```text
(60,372 data rows + 1 header) * 256 = 15,455,488 bytes.
(60,372 data rows + 2 headers) * 256 = 15,455,744 bytes.
210,632,704 + 15,455,744 = 226,088,448 bytes.
```

The `226,088,448*rho_io` term, 262,400-byte one-bank temporary cap, and
309,990,912-byte directory-peak cap are unchanged. The 128 MiB per-file cap,
128 MiB worker arena, 256 MiB scheduler/writer allowance, 1.25 GiB static
allowance, and 3.5 GiB measured RSS cap are unchanged.

The bank schema, scalar-row schema, 512-byte scalar-row cap, and 16,384-byte
bank-summary cap are unchanged. Every other file cap, line cap, packet cap,
counter cap, operation cap, timer cap, output cap, temporary cap, and resource
limit is unchanged.

All algorithms, mathematical laws, random streams, field encodings, schemas,
orders, counters, sticky-event semantics, replay rules, factor checks, private
firewall rules, path-object contracts, process chronology, source-only
authorization boundaries, and containment gates are unchanged.

## 5. Authorization boundary

No D14 mode is authorized to execute under this draft. A fresh no-context D14
theory audit must authenticate all twelve inputs and audit the complete
D09--D14 additive composition. This document does not perform that audit and
makes no D14 PASS claim.

A future D14 theory PASS may authorize only drafting the four source roles. It
does not authorize source freezing, a source PASS, compilation, a fixture
byte, preflight, local or remote execution, a result, packaging, or a ledger
edit. Pending approved hard dynamic containment remains an absolute gate.
