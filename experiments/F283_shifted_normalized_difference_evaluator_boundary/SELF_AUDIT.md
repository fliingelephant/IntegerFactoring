# F283 author self-audit

## Verdict

Author check: **internally consistent; fresh external audits required**.

This file is not hostile or independent evidence.

## Identity checks

1. The packet uses the P230 unresolved branch only after the public
   \(\gcd(B,N)\) screen.
2. Its geometry includes \(p<B<q<2p<2B\), \(q>B+1\), and \(2s<p\).
3. The divided-difference convention includes the nodes
   \(a,a+1,\ldots,a+k\), so \(G_a(n,k)=h_{n-k}\) has \(k+1\) variables.
4. The falling-factorial basis starts at \(X-a\), and multiplication by
   \(X\) gives the coefficient \(a+k\) in the recurrence.
5. At \((n,k)=(2B,B)\), the generalized-Stirling endpoint is exactly
   \(F_B(a)\).
6. The exponential generating function has the factor \(n!/k!\), and the
   ordinary excess generating function has numerator one.
7. Over \(\mathbb Q(a)\), all \(B+1\) poles are distinct and uncancelled.
8. The recurrence and realization lower bounds apply to the full canonical
   coefficient sequence. They do not apply to an arbitrary isolated-endpoint
   circuit.
   Fixed-radix decimation retains all \(B+1\) distinct generic modes.
9. The explicit bidiagonal matrix orientation reproduces
   \(G_a(n+1,k)=G_a(n,k-1)+(a+k)G_a(n,k)\).
10. The translation coefficient is \(\binom{2B}{B-j}\), independent of
    \(j\) except through its lower index.
11. Every formal translation term is nonzero in characteristic zero.
12. Interval multiplication gives a full Cauchy convolution.
13. For an even interval endpoint \(2m\), the even block has \(m+1\)
    nodes and the odd block has \(m\) nodes. For \(2m+1\), both have
    \(m+1\) nodes.
14. Division by two in the parity formulas is safe only because \(N\) is
    odd. It does not remove the convolution cost.
15. Reflection preserves \(B\) and uniform sampling. The first shift
    difference moves to \(h_{B-1}\) on \(B+2\) nodes and does not close on
    \(F_B\).
16. The ordinary rising-factorial alias reproduces the same two-child
    parity split. It is not asserted to exclude every possible q-product
    transform.

## Divided-power checks

17. The operator identity has the structure constant
    \((m+n)!/(m!n!)\), not its reciprocal.
18. At the first monotone addition-chain index \(k\ge p\), every parent is
    below \(p\), and \(k\le B<q<2p\).
19. The binomial or multinomial structure constant has exactly one
    \(p\)-factor and no \(q\)-factor.
20. The conclusion is scoped to positive monotone binary or finite-arity
    composition. Addition--subtraction and custom quotient states are
    excluded from the claim.
21. Postponing normalization gives \(B!F_B(a)\), which is zero modulo
    \(N\) because \(p\mid B!\) and \(q\mid F_B(a)\).

## Content checks

22. Expanding \((X+a)^{2B}\) gives
    \([a^k]F_B=\binom{2B}{k}S(2B-k,B)\).
23. The leading coefficient is the central binomial coefficient.
24. For \(B+1<r<2B\), the node complement modulo \(r\) has degree below
    \(B\), and the first full-field denominator shift is above \(B\).
25. Since \(B<r\), vanishing at every field element implies coefficientwise
    divisibility by \(r\).
26. The interval product \(P_B\) therefore divides the polynomial content.
27. On the promise, \(q\) is in this interval and \(p\) is not.
28. The leading coefficient has \(p\)-valuation zero and \(q\)-valuation
    one. Higher Legendre terms vanish because \(2B<p^2,q^2\). Thus the
    full content has gcd exactly \(q\) with \(N\).
29. Dividing by \(P_B\) or by the full content leaves a polynomial with a
    nonzero leading coefficient modulo \(q\). The universal zero is gone.
30. The packet does not claim that black-box evaluation exposes content.

## Lift and search checks

31. Writing \(B!=pU\) and \(F_B=qV_B\) gives
    \(B!F_B/N=UV_B\), with \(U\) a unit modulo \(N\).
32. The quotient \(V_B\) is nonzero modulo both hidden primes. Modulo
    \(q\), this follows from the exact leading-coefficient valuation.
33. CRT therefore supplies shifts for which the immediate \(N\)-adic
    quotient is a unit. The proposed quotient-then-gcd route has no
    all-shift guarantee.
34. The packet does not rule out a custom higher-lift decoder.
    The faithful modulus \(NB!\) gives the quotient but has
    \(\Theta(B\log B)\) bits, and materializing \(B!\bmod N\) already
    exposes \(p\).
35. No finite synthesis is proposed because every named grammar already has
    characteristic width, two-child linear leaf count, a nonunit crossing,
    the raw zero, the interval-content gate, or a signal-free quotient.
36. A nonlinear or adaptive one-child fast-forward remains outside scope.
37. No code, numerical calculation, cohort, remote access, literature
    search, ledger edit, staging action, or commit belongs to F283.

## Freeze check

Before freeze, the author must verify that the packet contains exactly
STATEMENT.md, PROOF.md, SELF_AUDIT.md, PROVENANCE.md, and MANIFEST.md, then
write FROZEN.sha256 over those five files. Fresh no-context hostile and
statement-only audits remain mandatory before promotion.
