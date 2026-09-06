# F233 strict statement-only reconstruction

## Verdict

**PASS.**  Every displayed mathematical implication was reconstructed from
`STATEMENT.md` alone.  No candidate input was edited and no computation was
run.

## Reconstructed checks

1. `N=BH+1` gives exact quotient `uH` and remainder `u` for every
   `1<=u<B`.  The bounds `C<H` and `U<B` make all shifted children positive
   and below `N`.
2. If `ell|s_p`, then `BH=g mod ell`; if `ell|s_q`, then `BH=-g mod ell`.
   Hence the two incidence laws have the displayed opposite signs.  The
   symmetric shift set identifies both with the same ratio cover.
3. Paired shifts `(u,c)` and `(u,-c)` put both oriented captured-prime
   products into the one integer `|ug+cB|`.  Coprimality of `s_p,s_q`
   justifies multiplying the squarefree parts.
4. Raising every exposed prime to exponent `n` saturates all hidden
   primary valuations.  This gives the exact residual products, including
   primes whose support overlaps the common part through `H`.
5. Independent uniform odd projections give return probabilities
   `1/r_p,1/r_q`.  Exact equal local order `d|M` is the complete stale atom,
   of probability `sum_{d|M} phi(d)^2/(PQ)`.
6. Circular pigeonhole gives the universal coverage implication
   `ell<=C(U+1)`.  The ratio set has at most `2CU` values, giving the
   avoidance implication when `ell-1>2CU`.
7. A prime above `2UC` dividing two children forces their projective
   determinant to vanish as an integer.  Deduplicating slopes preserves its
   incidence.
8. Therefore every residue-independent guaranteed prime lies below the
   numerical-QP smooth cutoff `max(Y,2UC+1)`.  No claim about the actual gap
   ratio beyond that cutoff follows.
9. The child size, branching, word height, puncture count, and modular
   arithmetic are numerical QP under the stated external all-input
   recursive dispatcher.

## Wording note

The statement called the two elementary coverage bounds “sharp.”  That
adjective is not literally an optimal-threshold claim.  The first displayed
implication is only sufficient; for example `U=1,C=2,ell=5` has full cover
although `5>C(U+1)`.  This does not invalidate the implication, the
avoidance theorem, or the downstream smooth-cutoff conclusion.

