# F137 manifest

## Claim

For canonical parent and child anchor positions, one complete
release-and-reanchor generation obeys an exact recenter-or-descend law. A
small Euclidean quotient makes the parent relation one virtual digit of the
next star and blocks all other observed large parent-complement overlaps in
that digit window. A large quotient strictly decreases the chosen block; two
consecutive large quotients contract it by \(C/(C+1)\).

## Relation to prior work

- X73/P120 shows that one unary feedback step does not force closure.
- X74/P122 gives only the within-star overlap obstruction.
- P70/P80 already give the divisor-carry remainder law.
- F137 adds the exact cross-star recentering comparison and the two-step
  contraction. It does not prove closure.

## Files and hashes

| File | SHA-256 | Role |
|---|---|---|
| STATEMENT.md | 2126e93be2be3abbca52ccb46615d3be8a2319c4dd064d8a5fa7705cd8084098 | Exact theorem, certificate, and scope |
| PROOF.md | 2f973e801b849693d9f5f0951556bb6978eb6f4e0236387b17fc38a686deeecc | Algebraic and quantitative proof |
| HOSTILE_REAUDIT.md | c44e91c038e1d2e762abd616cfb4d0baa032a72e61f64f4196c4545e0eeb8aeb | Passing hostile re-audit of the corrected frozen theorem and proof |
| BLIND_RECONSTRUCTION.md | 5e389f0b8084e964bea1359f8477c3ad78ff756e1aab8fa1f5d5ee821894aad5 | Passing statement-only independent reconstruction |

## Evidence class

Proof-only result. Its first frozen version failed hostile audit on
canonical-generation scope; that report is preserved. The corrected frozen
version passed a fresh hostile re-audit and a statement-only blind
reconstruction. It is eligible for narrow promotion. It is not a closure
theorem or a factoring algorithm.
