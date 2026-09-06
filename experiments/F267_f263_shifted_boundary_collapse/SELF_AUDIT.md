# F267 self-audit

## Verdict

PASS for the statement and proof before freeze. This is a self-audit only.
Fresh hostile and strict statement-only audits are still required.

## Checks

1. The six candidate definitions match the frozen F263 V2 source.
2. The jet formulas use coefficients `R''/2`, not raw second derivatives.
3. Both transfer divided-difference identities are proved without assuming
   that `B` or `B+1` is invertible.
4. Invertibility modulo `p` is invoked only after `s<H` gives `p>=s+2`.
5. The left-edge blocks exclude `s` by one or two positions.
6. The right-edge congruences are separated from the support-exclusion
   condition `s<H-L`.
7. Both parities of `B` are handled for `u1` and `v1`.
8. The `v1` conclusion includes its needed equation
   `q=p+2(s+1)`; it is derived only under `s^2<p`.
9. Near-square rigidity uses both floor inequalities and the even prime
   gap. The threshold is exactly `s^2<p`.
10. The Fermat statement starts at `B+1`, because a product of distinct
    primes is not a square.
11. The finite `s` sets, incidence total, union size, and factor bounds are
    copied from the authenticated F263 result audit and row file.
12. Exact coverage is claimed only for the frozen query bank. No converse
    zero classification is claimed.
13. The result outside the finite data is a kill: every listed boundary
    makes `p=B-s` a public descriptor, even when `s^2>=p`.

## Exclusions

The packet proves no exhaustive classification of candidate zeros, no
lower bound, no numerical-quasipolynomial block evaluator, no impossibility
result for other grammars, and no all-input factoring algorithm.
