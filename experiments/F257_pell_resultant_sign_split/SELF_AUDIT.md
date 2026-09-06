# F257 self-audit

## Verdict

PASS for the frozen statement and proof. This is a self-audit only. No
hostile audit, strict statement-only reconstruction, computation, human
audit, or publication-level literature review has run.

## Checks

1. The odd split preserves full valuations, not only prime support.
2. The full lcm identity is not claimed. The exact two-adic correction and
   a counterexample are included.
3. The two overlap is retained for exact square-class parity, although it
   cannot affect a gcd with odd \(N\).
4. The resultant factorization is used only for equal discriminants and
   post-wrap quadratics.
5. The identities (3.1)--(3.2) prove full divisibility
   \(d_-\mid Q_-\), \(d_+\mid Q_+\). No converse is asserted.
6. The two orbit formulas use \(S_{j-i}\) in the difference identity and
   \(S_{i+j}\) in the sum identity.
7. The Jacobi-minus-one statement follows a unit screen on \(D\).
8. The short-carry threshold uses balancedness and requires a nonzero carry
   combination.
9. The Las Vegas runtime is explicitly conditional. No event probability
   is inferred from a uniform model.
10. Signed gcd refinement can retain primes with identical signatures in one
    fragment; parity decoding does not require their factorization.
11. The two exact examples have the same minus coordinate label and opposite
    normalized-root behavior.
12. The \(N=143\) example is not called a screen-free hit.

## Exclusions

The packet proves no inverse-QP resultant-zero law, no existence law for a
signed parity dependency, no non-global-root law, no cross-discriminant sign
split, and no complete factoring algorithm.
