# F206 self-audit

## Radial data

1. The q-gamma exponent is `+1/2`, not `-1/2`.
2. The binary norm gives `P(-e^(-t)) -> sqrt(2)` with a nonzero limit.
3. The Mellin residue at `s=1` uses `beta(0)=1/2`.
4. The `s=-1` residue is `-t/24`: the Gamma residue is `-1`, while
   `zeta(-1) beta(-2)=1/24`.
5. There is no constant term because `beta(-1)=0` cancels the Gamma pole.
6. The binary Lambert identity gives `-t/8`, not `+t/8`, at the cusp
   one-half.
7. Substitution `t=2 pi y` changes constants but not radial powers.

## Vector-valued cusp scope

8. The modular obstruction assumes one fixed weight and one fixed projection.
9. Parabolic monodromy is semisimple. Ordinary meromorphic Puiseux cusp
   expansions and finite principal parts are required.
10. Negative and positive local exponents give exponential, not polynomial,
    radial behavior.
11. A surviving zero exponent gives the unique power `y^(-k)`.
12. The conclusion does not cover parabolic Jordan blocks, logarithmic
    Fourier expansions, or a holomorphic part plus a nonholomorphic
    correction that changes the radial powers.
13. The three cusp-power rows are checked separately. No claim that one row
    implies another is used.

## Mellin reflection

14. The first Dirichlet product is `zeta(s) beta(s-1)`.
15. The transposed product is `zeta(s-1) beta(s)`.
16. For odd `n`, `A^vee(n)=chi(n)A(n)`; this identity is not asserted for
    even `n`.
17. The completed beta equation uses conductor four and odd parity.
18. The exact reflection multiplier is `2^(3-2s) tan(pi s/2)`.
19. After multiplying both components by `2^s`, the off-diagonal entries
    are `2 tan(pi s/2)` and `-(1/2) cot(pi s/2)`.
20. The no-constant-matrix claim concerns this natural two-kernel reflection.
    It is not a classification of every possible vector completion.

## Repair and algorithmic scope

21. The finite-depth claim is restricted to diagonal rational Mellin
    normalizations, Euler derivatives or antiderivatives, and finite
    period-polynomial terms.
22. Rational functions cannot cancel the infinite pole-zero pattern of
    tangent or cotangent.
23. The gamma quotient shows that a nonholomorphic archimedean repair is
    possible in principle. F206 does not claim general noncompletion.
24. In the natural Mellin/Whittaker repair, the kernel changes but the
    Dirichlet coefficients do not.
25. At odd `N`, the second coefficient is only the public sign `chi(N)`
    times the first. This is the exact circularity.
26. No lower bound is claimed for Fourier-coefficient extraction from an
    arbitrary nonholomorphic or quantum object.
27. The `Theta(N)` statement concerns direct dense truncation only. It is not
    an arithmetic circuit lower bound.
28. The result does not object to one-child recursion or require fixed-ratio
    contraction.
29. No numerical computation, external search for a factoring solution,
    cross-family audit, or publication-level literature review was run.

## Highest-risk points for hostile audit

30. Recheck the exact beta functional equation and every power of two in the
    Mellin reflection.
31. Recheck that the vector cusp lemma remains correct for arbitrary fixed
    projections after transport by the scaling matrix.
32. Keep the finite-depth and natural-Whittaker scopes explicit. Reject any
    inference to all mock, quantum, or nonholomorphic completions.
