# F274 manifest — characteristic-shift transfer boundary

## Status

F274 is a proof-only candidate with an author self-audit.  A fresh hostile
audit and an independent statement-only reconstruction are pending.  No
outside-family or human audit has run.

No source code, compilation, benchmark, local research computation, remote
computation, cohort, dataset, or empirical result belongs to this packet.
No durable ledger was edited.

## Frozen mathematical artifacts

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | 22674281efe2fc593ef8b657bc4782f1892e118a2a193c6f5028d514a245ce47 |
| PROOF.md | 0077b4d4bea0ceed8d4771b78d02a48f67b446af7358a86273145f3215866d0b |
| SELF_AUDIT.md | 6da33d3be00a7953d5ddf2ce7a3c48a2fea5c32e943e5447731f4d3668c98b66 |
| PROVENANCE.md | e9a0203e80b2b21e16298c6dbbf02b39f71c94d8c0ce19fdf34263ee6d79a2c5 |

These four hashes freeze the mathematical content.  The hash of this
manifest and all five file hashes are recorded in FROZEN.sha256.

## Exact contents

1. The regular cyclic shift on functions
   \(\mathbb F_r\to\mathbb F_r\) has difference nilpotency index exactly
   \(r\), so the full state detects \(p\leq B<q\).
2. Every linear shift subquotient of dimension at most \(B\) has zero
   \(B\)-th difference in both CRT components.
3. Every \(B\)-th forward difference of an integer-coefficient polynomial
   is divisible by \(B!\).
4. Rational scalar shift coboundaries are classified by the limit at
   infinity and translation-orbit divisor sums.
5. A rational matrix gauge must pass the induced determinant-coboundary
   test.
6. Nonlinear, semilinear, implicit regular-state, determinant-one, and
   characteristic-dependent mechanisms remain open.

## Search disposition

No C++ search is justified for the closed grammar.  A future implementation
requires a theory candidate outside the linear-subquotient,
integer-polynomial-difference, and rational determinant-gauge boundaries.

## Exact exclusions

F274 proves no general circuit lower bound, interval-product evaluator lower
bound, nonlinear or semilinear impossibility theorem, arbitrary matrix-state
theorem, numerical quasipolynomial evaluator, integer-factoring algorithm,
or empirical claim.

Any mathematical change requires a new version, new hashes, and fresh
audits.
