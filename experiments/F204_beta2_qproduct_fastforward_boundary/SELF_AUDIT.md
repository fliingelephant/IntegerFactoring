# F204 self-audit

## Exact identities

1. The sign in the logarithmic derivative is negative:
   `L=-q d(log P)/dq`.
2. The binary product uses only odd supported indices, so
   `(1-q^a)(1+q^a)=1-q^(2a)` applies to every nonzero character term.
3. Differentiating `P(q^2)` contributes the chain-rule factor two.
4. In the abstract formal norm, odd logarithmic coefficients are genuinely
   free. The relation determines only their repeated doublings.
5. The theorem makes no claim that the coefficients of `P` itself are free;
   the freedom statement concerns all formal solutions of the norm and proves
   what can and cannot follow from that norm alone.

## Scalar modularity boundary

6. The q-gamma rearrangement has exponent `+1/2`:
   `P=(1-Q)^(1/2) Gamma_Q(3/4)/Gamma_Q(1/4)`.
7. The constant in `P(e^(-t))` is nonzero, and the binary norm gives the
   nonzero limit `sqrt(2)` at the cusp one-half.
8. The modular claim is only for a nonzero scalar meromorphic modular form of
   one fixed weight, with a multiplier and ordinary meromorphic cusp
   expansions on a finite-index subgroup.
9. A nonzero local cusp order gives exponential radial behavior. The observed
   polynomial behavior therefore forces local order zero before the weight is
   compared.
10. The factor `exp(2 pi i alpha tau)` tends to a nonzero constant at both
    tested cusps and does not alter their powers of `y`.
11. Negative integers `a,b` cause polynomial poles rather than zeros; the same
    exponent comparison applies.
12. The proof establishes the necessary condition `a=b`. It does not assert
    that `a=b` makes the monomial modular.
13. The result does not cover sums, arbitrary rational functions of the two
    orbit elements, vector-valued forms, mock or quantum modular forms,
    nonholomorphic completions, or transformation laws without the stated cusp
    behavior.
14. The odd coefficient of the logarithmic derivative is `(a-b)A(N)`, not
    `(a+b)A(N)`.

## Mahler boundary

15. Modulo two, `d chi(d)` is one for odd `d` and zero for even `d`, even
    when `chi(d)=-1` over the integers.
16. `tau(m)` is odd exactly when `m` is a square.
17. In the kernel witness, `e>=2` makes `2^(e-1)+1` odd and makes the final
    strict inequality valid.
18. Restricting to even `e` ensures any later selected index differs by at
    least two, so the witnesses prove pairwise distinct kernel sequences.
19. The primitive reduction clears rational-function denominators and poles
    before reduction. Dividing total integer content guarantees a nonzero
    reduced relation.
20. If only the inhomogeneous polynomial survived modulo two, the reduced
    identity would already be impossible. Hence a Mahler multiplier survives.
21. Distinct Frobenius powers make the resulting polynomial in `B(q)`
    nonzero.
22. The proof invokes two standard external results: the finite-kernel
    characterization of automatic sequences and Christol's theorem.
23. The conclusion excludes only fixed finite linear base-two Mahler equations
    over `Q(q)`. It does not exclude nonlinear equations or growing systems.

## Odd-prime norm and algorithmic scope

24. For `ell` not dividing `a`, the root product is `1-q^(ell a)`; for
    `ell` dividing `a`, it is `(1-q^a)^ell`.
25. The exponent `chi(ell d)=epsilon chi(d)` is valid because `ell` is odd.
26. Logarithmic differentiation contributes factors `ell` and `ell^2` on
    the two dilations.
27. The coefficient recurrence includes its correction term only when
    `ell` divides `k`.
28. The contraction statement is restricted to a fixed public prime `ell`.
    No claim is made against adaptive root banks or different identities.
29. F204 does not evaluate the F203 selector, factor an integer, or prove a
    complexity lower bound.
30. The obstruction is at one coefficient node. It does not use weak
    contraction as an objection. A single bit-descending recursive chain
    remains QP.
31. No numerical experiment, benchmark, computer algebra proof, or
    cross-family audit was used.
