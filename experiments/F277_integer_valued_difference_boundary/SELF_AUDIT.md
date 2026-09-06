# F277 author self-audit

## Status

This is the author's own proof check. It is not a hostile audit, blind
reconstruction, outside-family review, or computational result.

## Range checks

1. The packet separates \(s=0\), where \(\gcd(B,N)=p\), before every
   central-Stirling orbit count.
2. From \(B^2\le pq\), positive \(s\), and the even prime gap, the proof
   gets \(d\ge2s+2\), not merely \(d>2s\).
3. The inequalities \(q-B\ge s+2\) and \(2s+1<p\) are used separately.
4. Positive \(s\) excludes \(p=3,5\), so the numerical inequality used to
   prove \(2s+1<p\) starts at \(p=7\).

## Integer-valued basis checks

5. The coefficient in the Newton expansion is \(\Delta^jf(0)\), with no
   missing factorial.
6. The theorem concerns polynomials integer-valued on all integers. It
   does not silently extend to arbitrary rational functions.
7. Applying \(\Delta^k\) shifts \(\binom Xj\) to
   \(\binom X{j-k}\); terms with \(j<k\) vanish.
8. Equation (7) is exact integer division. It does not authorize inversion
   of \(B!\) modulo \(N\).

## Shifted-binomial checks

9. The upper-argument Pascal identity proves (9) before any reduction.
10. For \(k\le s\), the lower index has base-\(p\) digits
    \((1,s-k)\); recursive Lucas expansion leaves \(\binom q1=q\).
11. The matching integer \(q\binom{c-1}{s-k}\) is automatically zero
    modulo \(q\), so CRT is valid.
12. For \(k>s\), the two local residues are equal. The packet does not
    claim that a large public binomial is automatically QP-evaluable.
13. At \(c=1\), every nonterminal value except \(k=s\) is literally zero
    modulo \(N\), so the hidden spike is exact.

## Short-side and Kummer checks

14. The short side is chosen after binomial symmetry. The denominator is
    a unit because \(w<p<q\).
15. In this range, every hidden-prime valuation comes from a displayed
    numerator factor. Screening the complete product can be saturated if
    different factors contain different hidden primes; screening the
    individual factors then exposes them.
16. The QP cost statement assumes the public endpoints have QP bit length
    and \(w\) is numerical QP.
17. For \(\binom{2B}{B}\), \(2s<p\) prevents a base-\(p\) carry, while
    \(B<q<2B<2q\) gives exactly one base-\(q\) carry.

## Central-Stirling congruence checks

18. Reduction of powers modulo \(q\) is applied inside the
    inclusion-exclusion numerator only because \(B!\) is a unit modulo
    \(q\).
19. The reduced exponents in (32) are strictly below \(B\), so the two
    smaller Stirling numbers are zero.
20. In the \(C_p\) orbit count, an invariant partition can have zero or
    one moving block orbit because \(p+s<2p\).
21. A fixed point cannot lie in a moving block. An element \(p\)-cycle is
    either intact in a fixed block or split one point per moving block.
22. When both element cycles split, their relative phase gives exactly a
    multiple of \(p\); its precise remaining factor is unnecessary.
23. The all-fixed-block cases are impossible by atom counts, not assumed
    absent.
24. The exact saturated examples verify the products, floor square roots,
    and divisibilities without a primality oracle. The four displayed
    factors 19, 29, 37, and 47 are elementary primes.
25. The packet does not infer joint nonvanishing from the absence of a
    displayed simultaneous counterexample. It records (23)--(24) as open.

## Evaluator and scope checks

26. Inclusion-exclusion, the ordinary Stirling recurrence, and exact
    materialization are costs of named literal representations only.
27. The bit-length lower bound uses only pair partitions, a subset of all
    set partitions.
28. No claim says that every modular central-Stirling algorithm must form
    \(B!\), visit \(B\) states, or materialize the exact integer.
29. The no-search conclusion is scoped to the exact classified families.
    It is not a theorem that every symbolic search is futile.
30. No factorer, numerical-QP evaluator, probability law, circuit lower
    bound, empirical theorem, or all-input result is claimed.
