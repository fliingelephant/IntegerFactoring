# F212 self-audit

## Verdict

Self-audit passes as a proof-only candidate, subject to fresh hostile review
of the standard unknown-divisor Coppersmith dependency. No computation is
used as mathematical evidence.

## Quantifier and constant checks

1. The finite full-torsor theorem assumes both \(N\geq1024\) and
   \(s(m)\leq\sqrt N/8\). The proof uses \(t=\sqrt N\geq32\) in all four
   interval and product inequalities.
2. The asymptotic corollary quantifies over sequences \(N_i\to\infty\). It
   does not claim that a fixed finite ratio such as the smallest F209-D01
   observation already lies in the uniform finite range.
3. The implication \(m=o(\sqrt N)\Rightarrow s=o(\sqrt N)\) uses
   \(s\leq2m\).
4. The singleton theorem uses the exact progression step \(s\), not merely
   \(m\). Its finite hypothesis is exact and its super-square-root corollary
   uses only \(s\geq m\).
5. The phase transition leaves the entire constant band
   \(m=\Theta(\sqrt N)\) open. The packet does not claim a sharp optimal
   constant inside that band.

## Arithmetic checks

1. Every unit residue has an odd lift progression. For even \(m\), units are
   odd and the step is \(m\). For odd \(m\), parity alternates and the step is
   \(2m\).
2. Since \(m\) is coprime to \(N\), \(Nx^{-1}\) is again a unit.
3. The endpoint inequalities are uniform in the residue. They use only that
   the first lift is within \(s\) of the lower endpoint and the last lift is
   within \(s\) of the upper endpoint.
4. In the singleton range, \(P^-Q^-\leq N\leq P^+Q^+\) becomes the equality
   \(XY=N\); no continuous-rectangle relaxation remains.
5. At \(m=K\), the proof establishes the stronger exact bound
   \(N-K<XY<N+K\). Thus congruence modulo \(K\) forces equality without an
   unproved uniqueness assumption.
6. A divisor \(X\in[L,B]\) has complementary divisor in \(Q\). The upper
   bound follows from \(X^2\geq(N+1)/2\), not from an unsafe replacement of
   \(L\) by \(\sqrt{N/2}\).
7. Even summation indices in the divisor-jump identity vanish because an odd
   \(N\) has no even divisor.
8. The quotient values \(\lfloor N/X\rfloor\) are strictly decreasing on the
   declared shell because \(X(X+1)\leq B(B-1)<B^2\leq N\).

## Coppersmith checks

1. The packet invokes only the proved univariate unknown-divisor theorem,
   with a monic degree-one polynomial. It does not invoke a general
   bivariate heuristic.
2. The listed modulus is coprime to \(N\), so \(m^{-1}\bmod N\) exists.
3. If \(p=r+mt\), then \(t<N^{1/4-\varepsilon}\) under
   \(m\geq N^{1/4+\varepsilon}\).
4. Balance gives \(p>\sqrt{N/2}\), which exceeds
   \(N^{1/2-\varepsilon/4}\) for all sufficiently large \(N\).
5. The exponent gap

   \[
   \left(\frac12-\frac\varepsilon4\right)^2
   -\left(\frac14-\frac\varepsilon2\right)
   =\frac{\varepsilon}{4}+\frac{\varepsilon^2}{16}
   \]

   is positive, leaving one fixed lattice margin that covers both
   \(p<\sqrt N\) and \(q<\sqrt{2N}\).
6. The polynomial \(T+r m^{-1}\bmod N\) vanishes modulo the hidden divisor,
   and the returned integer is verified by a public gcd.
7. The upper bound \(m\leq N^{O(1)}\) ensures polynomial-size encodings. It
   holds for the F207 child modulus but is stated explicitly for the abstract
   terminal.
8. The theorem is conditional only on receiving a QP-size correct list. It
   does not assert that F209 constructs that list.

## Scope checks

1. The full-torsor theorem is a no-signal result for F209's exact three
   interval tests. It is not a lower bound against all uses of the factored
   child modulus.
2. The singleton theorem identifies the remaining predicate with factoring;
   it does not prove factoring hard.
3. The exact Kloosterman formula covers the two separable interval
   indicators, not the endpoint product predicate.
4. Dense displayed Fourier support and square-root analytic errors are named
   route boundaries only. No arithmetic-circuit or oracle lower bound is
   claimed.
5. The CRT-order conclusion covers F209's explicit expansion and full
   interval scan. It leaves compressed, adaptive, nonlinear, and
   meet-in-the-middle representations open.
6. The finite F209-D01 measurements motivate the theorem but prove none of
   its unbounded claims.
7. No statement is made about unbalanced semiprimes or arbitrary composite
   inputs beyond the standard Coppersmith terminal once a suitable divisor
   residue is supplied.

## Fresh-audit targets

1. Recheck the explicit \(1/8\) and \(1024\) constants without using decimal
   approximations.
2. Check the exact definition of interval span versus inclusive cardinality.
3. Reconstruct the complementary-divisor-in-\(Q\) argument at \(m=K\).
4. Verify the stated unknown-divisor Coppersmith exponent and the monic
   normalization modulo \(N\).
5. Reject any reading of the Fourier and CRT sections as unconditional lower
   bounds.
