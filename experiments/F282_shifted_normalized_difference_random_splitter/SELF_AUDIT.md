# F282 author self-audit

## Verdict

Author check: **internally consistent; fresh external audits required**.

This file is not hostile or independent evidence.

## Mathematical checks

1. The packet assumes exactly \(N=pq\) with distinct odd primes
   \(p<q<2p\).
2. From \(p<\sqrt N<q\), it obtains \(p\le B<q\).
3. Since \(B<2p\), a nontrivial \(\gcd(B,N)\) forces \(B=p\) and returns
   \(p\).
4. On the gcd-one branch, \(B=p+s\) with \(s\ge1\).
5. Writing \(q=B+h\), the strict inequality \(B^2<N\) gives \(h>s\).
6. Odd-prime parity excludes \(h=s+1\), so \(h\ge s+2\).
7. The inequality \(q<2p\) then gives \(p\ge2s+3\).
8. The proof separately records \(h<B\) and \(B<q-1\), which are the two
   endpoint inequalities used in the \(q\)-coefficient argument.
9. The convention is the forward difference
   \(\Delta f(X)=f(X+1)-f(X)\).
10. The signs and factorials in the equally spaced divided-difference formula
    reproduce \(\Delta^B/B!\) exactly.
11. The monomial divided-difference identity uses exponent \(2B=B+B\), so
    its complete-homogeneous index is \(B\), not \(B-1\) or \(B+1\).
12. Identity (3) proves integer divisibility. No modular inverse of \(B!\) is
    used.
13. Modulo \(q\), all \(B+1\) nodes are distinct and the complement has size
    \(h-1\).
14. The full-field product is \(1-t^{q-1}\), with the correct minus sign.
15. The complement numerator has degree below \(B\), and the first
    denominator shift \(q-1\) is above \(B\). Thus the \(t^B\) coefficient
    is zero.
16. Modulo \(p\), the node multiset is one full field plus the extra
    \(a,a+1,\ldots,a+s\).
17. At degree \(B=p+s\), only shifts zero and \(p-1\) contribute. The next
    index \(s-p+2\) is negative.
18. The distinct-node formula for the short multiset uses exponent \(r+s\).
    Its two exponents differ by \(p-1\).
19. A zero node contributes zero at both positive exponents. The proof never
    divides by the node itself.
20. Node differences are nonzero because \(s<p\).
21. The leading coefficient of
    \(h_{s+1}(a,a+1,\ldots,a+s)\) counts weak compositions and is
    \(\binom{2s+1}{s}\).
22. Since \(2s+1<p\), this binomial coefficient and the factor two are units
    modulo \(p\). The reduced polynomial has exact degree \(s+1\).
23. The field root bound therefore allows at most \(s+1\) bad \(p\)-residues.
24. Uniform sampling modulo \(N\) projects exactly uniformly modulo \(p\).
25. The \(q\)-component always vanishes. A good \(p\)-residue gives gcd
    exactly \(q\); a bad one gives \(N\), not a false proper factor.
26. The probability inequality uses
    \(s+1\le(p-1)/2\), giving at least \((p+1)/(2p)>1/2\).
27. The expected independent trial count is at most \(2p/(p+1)<2\).

## Complexity and scope checks

28. The evaluator interface takes only public \((N,a)\). It receives no
    factor, \(s\), \(h\), CRT decomposition, or nonunit inverse.
29. The Las Vegas cost claim is conditional on a uniform worst-case
    numerical-QP modular evaluator. Sampling, gcd, square root, and output
    verification add polynomial expected bit cost.
30. On the unresolved branch \(p<B<q<2p\), so \(B!\) contains \(p\) exactly
    once and no \(q\). The raw difference is divisible by \(N\) for every
    shift. The factor-bearing exact normalization is the sole source of the
    useful local asymmetry.
31. The proof does not construct that normalization or the evaluator. It
    records the literal \(B+1\)-term, characteristic-range recurrence, and
    exact-materialization costs only as named-method boundaries.
32. The theorem is scoped to the balanced distinct-odd-semiprime promise.
    It does not recognize the promise or reduce arbitrary composites to it.
33. F282 removes the need for an F281 simultaneous-saturation theorem only
    for this randomized shifted family, conditional on its evaluator. It
    does not prove or refute the F281 conjecture.
34. No numerical search, C++ source, runner, remote access, empirical output,
    ledger edit, staging, or commit belongs to this packet.

## Freeze check

Before freeze, the author must verify that the packet contains exactly
STATEMENT.md, PROOF.md, SELF_AUDIT.md, PROVENANCE.md, and MANIFEST.md, then
write FROZEN.sha256 over those five files. A fresh no-context hostile audit
and a separate statement-only reconstruction remain mandatory before
promotion.
