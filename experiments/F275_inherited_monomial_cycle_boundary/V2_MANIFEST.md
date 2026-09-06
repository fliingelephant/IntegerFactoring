# F275 V2 manifest — canonical-carrier additive repair

## Status

F275 V2 is a minimal proof-only additive repair. It has no author self-audit.
Fresh hostile and statement-only audits are pending. V2 is not promoted.

No source code, checker, compilation, numerical search, benchmark, corpus,
remote run, empirical result, or durable-ledger edit belongs to V2.

## Frozen V2 artifacts

| File | SHA-256 | Role |
|---|---|---|
| `V2_STATEMENT.md` | `a9bd86b4e4515f133c3c2d7711c530d334749675e0aa75eb8bc7547f3ad0f0da` | Normative additive statement |
| `V2_PROOF.md` | `9c0ec169e6402114a0546fca5506985ff6cec6250f7f5cc73081aa946063623f` | Corrected size proof and unchanged-theorem boundary |
| `V2_PROVENANCE.md` | `ac564d1bc1f8dc1f12584c38ddbf8c1b2e8ef676cab54f4ce42fe51990bdc812` | Immutable V1 base and triggering audit |

## Imported immutable anchors

| Artifact | SHA-256 | Status |
|---|---|---|
| `FROZEN.sha256` | `6c3cebe4f34bdb439dabb9cc50990bb68d0250ae552ea5087dd4e57dc057aa9d` | Complete V1 freeze root |
| `HOSTILE_AUDIT.md` | `a839f1bd62ca2671882c6dba0270de9f901aad9f0d52e2de888f38ca196743a2` | Fresh V1 hostile verdict: `FAIL` |

The V1 freeze root authenticates `STATEMENT.md`, `PROOF.md`,
`SELF_AUDIT.md`, `PROVENANCE.md`, and `MANIFEST.md` at the hashes recorded in
`V2_PROVENANCE.md`. Every V1 byte and the hostile-audit byte stream remain
unchanged.

## Exact repair

Construction (8) now requires its input carrier to be canonical:

\[
 1\le d<N.
\]

Since `T_y(d)` is also in `[1,N)`, its exact row obeys

\[
 1\le dT_y(d)\le(N-1)^2<N^2.
\]

This is the only mathematical change.

## Preserved claims and scope

The general graph setup still permits arbitrary positive unit carriers.
Theorem A and Theorem B are unchanged. The monomial pullback, structural
global-root corollary, alternative-root screen, Eulerian square identity,
even-cycle holonomy, exact alternating gcds, and reduced-complement/F270
scope boundary are all retained exactly.

V2 proves no broader graph, canonical-section, probability, runtime, or
factoring claim. Any further mathematical change requires a new version,
new hashes, and fresh audits.

