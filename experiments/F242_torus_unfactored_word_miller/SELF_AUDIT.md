# F242 self-audit

## Checks

1. The exponent uses the public Jacobi sign `J=(D/N)`, not either hidden
   Legendre sign.
2. The identity `gcd(N-J,p-epsilon_p)=gcd(p-epsilon_p,q-epsilon_q)` was
   checked algebraically in all four orientations.
3. No local square root of `D` is used by the algorithm.  The proof uses one
   only to count fibres in the split algebra.
4. A nonunit `D` is screened before the Jacobi symbol or torus algebra is
   used.
5. The Hilbert--90 sampler is proved uniform by exact constant fibre counts
   in both the split product algebra and the nonsplit field.
6. The sampler includes both signed identity points.  It does not inherit
   the Cayley chart's omission of `-1`.
7. The coefficient gcd detects local zero elements.  The norm gcd also
   detects split zero divisors.  The only inverse is taken after this norm
   is certified as a unit.
8. The accepted global unit law is a product conditioning event, so local
   independence is preserved.
9. The chosen `D` is kept while coefficient pairs are resampled.  This
   avoids orientation bias from unequal split and nonsplit unit densities.
10. Multiplication and the complete square chain use coefficient pairs and
    no division.
11. Every equality screen uses both coefficients.  A gcd of only one
    coefficient would admit false local equality tests.
12. Both conditional two-primary kernel sizes are at least two because
    `m_p,m_q,N-J` are even.  The identity itself remains the `K=0` atom.
13. Unequal two-primary kernel sizes use the exact P205 distribution, not
    the equal-kernel specialization.
14. Formula (6) is exact only for the clean powered phase on a squarefree
    semiprime.  Sampler gcd factors are additional successes.
15. The four-orientation average assumes one fixed word.  A word depending
    on the full discriminant is explicitly classified as a new source
    problem.
16. P158 is used only to obstruct the bare `W=1` orientation menu on its
    constructed family.  It is not claimed to obstruct residual absorption
    by a nontrivial word.
17. The theorem remains a conditional reduction.  It supplies no all-input
    quasipolynomial word source.

## Status

Self-audited only.  A fresh hostile audit and a strict statement-only
reconstruction are required before promotion.

