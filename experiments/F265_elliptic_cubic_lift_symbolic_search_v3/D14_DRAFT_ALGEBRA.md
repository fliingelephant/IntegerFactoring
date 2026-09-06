# F265-D14 draft algebra amendment — exact serialized-width repair

## Status and exact construction

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

D14 has exactly these authenticated predecessor bytes:

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

Read all eleven authenticated bytes in full. Apply only the explicit
replacements and additions in this file and in
`D14_DRAFT_PREREGISTRATION.md`. Every D09--D13 clause not explicitly replaced
by D14 survives literally. Preserve every predecessor byte.

The D11 hostile PASS remains evidence only for the authenticated D09+D10+D11
composition. It does not transfer to D12, D13, or D14.

## 1. Bound D13 hostile disposition

The triggering review was the fresh hostile theory/interface audit performed
in Codex task `/root/hostile_f277` against the two authenticated D13 hashes in
the table and all nine explicitly imported D09--D12/D11-PASS bytes. Its exact
verdict text was:

```text
Verdict: FAIL — REVISE.
```

The returned finding said that the only defects were two non-safety arithmetic
errors in `D13_DRAFT_PREREGISTRATION.md`; every hard cap remained safe and no
deeper interface blocker was found. Under the review instruction permitting
`D13_HOSTILE_THEORY_AUDIT.md` only on PASS, no D13 hostile-audit file was
created and its audit SHA was reported as `N/A`. This message provenance is
the historical trigger for D14, not an authenticated predecessor artifact and
not a PASS for D14.

## 2. Preserved contract and exact repair scope

D14 changes no mathematical object, source law, random stream, algorithm,
schema, field, order, path contract, process role, command-line grammar,
fixture, root class, event semantics, sticky-event rule, counter, digest,
timer boundary, finite decision, diagnostic, theorem boundary, firewall,
containment gate, or authorization boundary.

D14 replaces exactly two D13 preregistration calculations:

1. D13 Section 4.3 used the seven-byte spelling `heldout` as the maximum split
   width. D14 uses the nine-byte spelling `discovery`, so the maximum wrapped
   event row is 227 bytes and the 256-byte cap has 29 bytes of slack.
2. D13 Section 5 made the same split-width substitution in the public scalar
   row. D14 uses `discovery`, so the maximum row is 450 bytes and the 512-byte
   cap has 62 bytes of slack.

The literal 256-byte event-row cap, 512-byte scalar-row cap, all file and
packet caps, all output and temporary caps, every projection coefficient, and
all aggregate resource limits are unchanged. All algorithms and all schemas
are unchanged. The D14 preregistration gives the complete replacement text.

## 3. Mechanical D14 composition

D14 replaces every future source-version token `F265-D13`, executable prefix
`f265_d13_`, artifact prefix `F265-D13.`, and fixture-root placeholder prefix
`F265_D13_` by the corresponding D14 token. This replacement applies only to
future artifacts and source. It does not rename or modify a predecessor file.

The D14 materializer theory root includes the eleven predecessor hashes above,
the final hash of this D14 algebra amendment, and the final hash of the D14
preregistration amendment. The D14 preregistration specifies their exact line
order. No other root construction changes.

## 4. Authorization boundary

A fresh no-context D14 theory PASS may authorize only source drafting for the
four D14 roles. Every source, fixture, audit, compile, execution, result,
packaging, and ledger restriction inherited through D13 survives with D14
tokens. Pending hard dynamic containment remains an absolute gate.

D14 contains no source, fixture byte, runner, launch command, containment
fallback, execution authorization, or hostile audit of D14.
