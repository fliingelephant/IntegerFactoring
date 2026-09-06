# F247 self-audit

## Mathematical checks

1. The ordinary permutation claim requires both \(a\) and \(E\) to be
   units modulo \(N\). Without \(\gcd(E,N)=1\), the carry visits only an
   affine coset of the image of multiplication by \(E\).
2. Uniformity is conditional on a transcript computed only modulo \(N\).
   A transcript that already reads a modulo-\(N^2\) lift or an integer carry
   is outside the statement.
3. The direct-gcd count assumes \(N=pq\) with distinct primes. It is not
   stated for prime powers or arbitrary composites.
4. The exterior collision formula uses independent canonical
   representatives of uniform residue classes. It removes exact equality
   before counting a nonzero difference.
5. The bank bound is stronger than an unconditional independent-pair
   bound. After the past is fixed, a new carry is exactly uniform. Its
   unequal collision probability with each fixed old carry is exactly
   \((c_\ell(L)-1)/N\), hence at most \(1/\ell\).
6. Carries on one power chain share one affine parameter and are not
   independent. They are governed by (20) or (21), not by the fresh-bank
   law.
7. The signed local-order equivalence uses squarefreeness of \(N=pq\),
   oddness of the local prime, and \(r\nmid E\).
8. For a negative return, the signed carry is one more than the carry based
   on the least nonnegative residue \(N-1\). The packet states this section
   change explicitly.
9. The torus fibre statement requires exact norm one modulo \(N^2\).
   Without this condition, two tangent coordinates are free.
10. The torus carry is normalized by multiplication with \(X^{-1}\). The
    affine law is for this normalized carry, not for each unnormalized
    coordinate of \(U_t^E-X\).
11. The trace constraint uses \(2\) invertible modulo odd \(N\). It does
    not require the quadratic algebra to be a field in every component.
12. The F244 corollary covers only fresh gauge coordinates, positive
    products and powers, and unequal-value differences. It does not cover
    sums, determinants, Euclidean quotients, or another nonlinear map.
13. Most importantly, the lift-torsor theorem does not give a distribution
    for the canonical intercept \(K_0\). The only canonical claim is the
    explicit \(a=N-1\) null witness. The general canonical section remains
    open.

## Novelty boundary

The binomial lift action and tangent-space calculation are elementary.
The useful new item in this repository is their exact placement at the
P205/P208 source boundary:

\[
\text{modulo-}N\text{ return transcript}
\quad\text{versus}\quad
\text{canonical second digit modulo }N.
\]

No publication-level novelty claim is made.

## Promotion status

Do not promote without a fresh hostile audit and a strict statement-only
reconstruction. The reviewer must reconstruct the torus normalization and
must reject any inference that the canonical carry is uniform.
