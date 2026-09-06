# F208 self-audit

## Promise and selector normalization

1. The promise is restricted to distinct odd primes \(p<q<2p\).
2. The proof uses balance only to place \(p\) in \((B/2,B]\) and to
   exclude its higher multiples from that interval.
3. The divisor-pair and sign identities themselves need only \(p<q\), not
   the balance upper bound.
4. The public endpoint correction is \(1+\chi(N)N\). It is \(1-N\) only
   on the \(N\equiv3\pmod4\) branch.
5. The exact jump
   \(J_d(N)=\lfloor N/d\rfloor-\lfloor(N-1)/d\rfloor\) is one if and only
   if \(d\mid N\).
6. Since \(N\) is nonsquare, no divisor lies exactly at \(\sqrt N\), so
   complementary pairing has no midpoint correction.
7. For \(d\mid N\), the identity
   \(\chi(N/d)=\chi(N)\chi(d)\) uses that every divisor is odd and
   \(\chi(d)^2=1\).
8. If \(\chi(N)=-1\), then \(p-q<0\), so the corrected sign is
   \(-\chi(p)=\chi(q)\).
9. If \(\chi(N)=1\), the corrected sign is
   \(\chi(p)=\chi(q)\).
10. The signed divisor-OR identity returns only one character bit. It is not
    asserted to be factoring-equivalent by itself.

## Totalized reciprocity

11. Both \(N\) and the supported \(d\) are odd. Even \(d\) have
    \(\chi(d)=0\) and are irrelevant to the aggregate.
12. The two floor sums count opposite closed half-rectangles. Boundary
    points are counted twice, not omitted.
13. The solutions of \(id=jN\) are
    \(i=tN/g,j=td/g\), where \(g=\gcd(N,d)\).
14. Because \(g\) is odd, exactly \((g-1)/2\) such points lie in the
    half-rectangle.
15. The correction is \((g-1)/2\), not \(g/2\) or \(g-1\).
16. Balance gives \(B<2p\), while \(p<\sqrt N\) gives \(p\leq B\).
17. A number \(d\in(B/2,B]\) with nontrivial gcd cannot contain \(q\), and
    it cannot be a multiple \(kp\) with \(k\geq2\).
18. The reciprocity aggregate equals \(\chi(p)(p-1)\). Its absolute value
    plus one is \(p\).
19. This factoring equivalence applies to exact evaluation of that declared
    aggregate. The packet supplies no aggregate evaluator.
20. A literal interval scan has \(\Theta(\sqrt N)\) candidates and is
    exponential in the bit length.

## Dedekind and cotangent identities

21. The sawtooth value at an integer is zero. This special value is needed
    for the \(u=0\) inner sum.
22. The residue decomposition \(r=u+j(k/g)\) is unique.
23. The second sawtooth is independent of \(j\) because its added term is
    the integer \(h_0j\).
24. The first sawtooth inner sum equals the reduced sawtooth for both
    \(u=0\) and \(u>0\).
25. Therefore \(s(h,k)=s(h/g,k/g)\) has no missing factor of \(g\).
26. Cotangent poles occur exactly when \(k\mid hr\), at
    \(r=j k/g\) for \(1\leq j<g\).
27. The first cotangent is finite at those residues because
    \(0<r<k\).
28. The ordinary cotangent identity is used only on the coprime branch.
29. The periodic-Bernoulli definition is the stated totalization on the
    noncoprime branch.
30. The result does not exclude combinations of unit-slope sums.

## HNF and quadratic-form boundaries

31. Under the declared triangular convention, fixed \(a,d\) have exactly
    \(a\) choices of \(b\), producing the weight \(a\chi(a)\).
32. The adjacent cumulative-shell difference selects exactly \(ad=N\).
33. Hyperbola rearrangement changes the enumeration order, not the
    determinant equality.
34. The form \([p,0,q]\) is primitive because \(\gcd(p,q)=1\).
35. Its discriminant is \(-4N\), and the inequalities
    \(0\leq|b|\leq a\leq c\) make it reduced.
36. It is ambiguous because changing \(b\) to \(-b\) leaves it unchanged.
37. The only literal diagonal reduced choices are \([1,0,N]\) and
    \([p,0,q]\).
38. The nonprincipal proof is valid because proper equivalence preserves
    represented integers.
39. The principal form cannot represent \(p\): \(y\neq0\) is too large and
    \(y=0\) would require a prime square.
40. No claim is made against implicit class-group navigation or a
    character-only class statistic.

## Representation symmetry and Archimedean magnitude

41. Pair-symmetric cancellation is asserted only for weights satisfying the
    displayed exact equality \(W_N(d)=W_N(N/d)\).
42. It does not cover asymmetric, truncated, incomplete, or signed-region
    representation counts.
43. The two-square formula is used only as a standard exact comparison.
44. On the opposite-character branch, one factor
    \(1+\chi(p)\) or \(1+\chi(q)\) vanishes, so \(r_2(N)=0\).
45. On the same-character branch,
    \(4(1+\chi(p))^2=8(1+\chi(p))\) for
    \(\chi(p)\in\{\pm1\}\).
46. The exact magnitude is \(p+q\) when \(\eta=1\) and \(q-p\) when
    \(\eta=-1\).
47. Both square identities expand directly and have no sign ambiguity.
48. Exact magnitude is factoring-equivalent on the promise, but the packet
    does not compute it.
49. The sign alone remains a one-bit orientation target.
50. No numerical experiment, literature-priority claim, all-input factoring
    claim, durable-ledger edit, or complexity lower bound is part of F208.
