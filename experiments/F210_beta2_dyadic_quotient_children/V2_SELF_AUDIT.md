# F210 V2 self-audit

## Version boundary and repaired defect

1. V1 remains frozen byte-for-byte. Its fresh hostile audit returned FAIL on
   one exact claim: \(X<\sqrt N<Y\), together with \(XY=N\), does not
   exclude the trivial pair \((1,N)\).
2. V2 replaces that claim everywhere by the nontrivial balanced condition
   \(1<X<\sqrt N<Y<N\), together with \(XY=N\).
3. V2 states \(t\ge1\) explicitly in the dyadic state, the first-stage
   specialization, the finite \(2\)-adic theorem, and the recursion bound
   where the domain matters.
4. No other mathematical mechanism was strengthened. In particular, V2
   does not claim that a false chart has no integer point.

## Promise and imports

5. The parent promise is exactly the balanced squarefree semiprime promise
   \(N=pq\), with distinct odd primes \(p<q<2p\).
6. The dyadic state assumes a correct P179 reciprocal prefix, \(t\ge1\),
   and \(2m<p\). F210 V2 does not construct that prefix.
7. P172 is used only after factor-first stripping supplies a fully known
   exact common local order coprime to \(N\).
8. P183 is used only for one decrement spine plus fixed-ratio late-stage
   side children. It is not applied to an early two-near-child tree.

## Child arithmetic

9. The relation \(b=a\mathsf{xor}\delta\) follows from the exact expansion
   \(N=(r+mP)(c+mQ)\). The parity reduction uses that \(t\ge1\), hence
   \(m\) is even.
10. Both candidate numerators are divisible by \(2m\).
11. Positivity uses \(r_a,c_a<2m<p\), hence
    \(r_ac_a<p^2<N\).
12. Coprimality uses \(\gcd(2m,N)=1\) and
    \(0<r_a,c_a<p\). No hidden primality test is used.
13. The two tables distinguish \(\delta=0\) and \(\delta=1\).
14. The sign in \(D=(c-r)/2\) is fixed by \(D=K_0-K_1\).
15. Coalescence is exactly \(\delta=1,r=c\). The first permitted stage is
    \(t=1,m=2\); the \(N\equiv3\pmod4\) formula is a special case, not a
    converse for every later stage.
16. The bound on common support applies only outside coalescence.
17. Every common prime power divides \(|D|\), but private prime support of
    either child is unrestricted by this theorem.
18. The lcm formula is exact in both the coalesced and noncoalesced cases.

## Half-translation and local scope

19. The translation is
    \((P,Q)\mapsto(P-1/2,Q-\sigma/2)\), with
    \(\sigma=(-1)^\delta\). For \(\delta=1\), its second component is
    \(Q+1/2\). Both signs were expanded directly.
20. The matrix identity uses the same half-translation and has determinant
    \(N\) on both sides.
21. The physical-coordinate identity is \(XY-N=hF_a\). Division by \(h\)
    is used only where two is a unit.
22. Over every odd modulus, the coordinate changes and half-translation are
    invertible. Thus the claimed solution-set bijection is exact.
23. The odd-local obstruction covers only invariants under public affine
    coordinate isomorphism. It does not equate the raw coefficient lists or
    child prime supports.
24. F210 V2 does not claim equality of Jacobi symbols, higher-residue
    symbols, exact orders, smoothness profiles, or other raw statistics
    computed on the different prime divisors of \(K_0,K_1\).
25. The genus and class statement concerns the abstract split curve after
    odd-local coordinate change. It does not cover class groups of new
    integral orders constructed asymmetrically from \(K_a\).
26. At a child prime power, the displayed square root is explicitly scaled
    by \(r_ac_a^{-1}\). No unscaled square root of \(N\) is asserted.
27. The character identity is only multiplicativity applied to
    \(N\equiv r_ac_a\); it supplies no orientation theorem.

## Finite 2-adic lifts and the repaired integer boundary

28. The \(2\)-adic count assumes \(t\ge1\) and \(s\ge t+1\). It enumerates
    the \(2^{s-t-1}\) lifts of the fixed odd \(X\)-class. Each determines a
    unique \(Y=NX^{-1}\), whose class modulo \(h\) is forced.
29. The old condition \(X<\sqrt N<Y\) is intentionally not used for
    uniqueness. The V1 audit's example \(N=77,m=2\) places \((1,77)\) in
    a false chart while satisfying that old condition.
30. Under \(1<X<\sqrt N<Y<N\) and \(XY=N\), the divisor list
    \(1,p,q,N\) forces \((X,Y)=(p,q)\). This proves uniqueness without an
    algorithmic bounded-point assumption.
31. The two charts have distinct first residue classes modulo \(h\), so
    only the true chart contains \((p,q)\).
32. In coalescence, the other chart contains \((q,p)\), but that point
    reverses \(X<\sqrt N<Y\). The V1 audit's example \(N=91,m=2\) also
    shows that this other chart can contain \((1,91)\). V2 excludes that
    endpoint by both \(1<X\) and \(Y<N\).
33. V2 makes no claim that the true chart is the only chart with any
    integer point. It also makes no uniqueness claim under the old
    orientation condition with the endpoint bounds removed.
34. The nontrivial balanced point is an exact distinction, not an efficient
    selector. An algorithmic test for it remains open.

## Order bridge and resultants

35. Complete factorization of \(K_a\) gives complete factorization of
    \(H_a=2mK_a\), since \(2m\) is a known power of two.
36. The exact common annihilator is
    \(G=\gcd(H_0,H_1)=2m\gcd(K_0,K_1)\), including coalescence.
37. Simultaneous global return is an explicit condition. It is not inferred
    from either child being true.
38. Factor-first stripping tests every prime multiplicity of the known
    annihilator. Without a proper gcd, every retained prime multiplicity is
    required in both local orders, so the final orders are equal exactly.
39. The final common order is coprime to \(N\) because it divides \(G\),
    while both \(2m\) and both children are coprime to \(N\).
40. The P172 terminal is invoked only under the explicit
    \(N^{1/4}/e\le Q(n)\) bound.
41. The polynomial gcd identity is exact. The ordinary resultant is zero
    because \(X-1\) is always common; no information is inferred from that
    zero.
42. An asymmetric return is recorded only as a public feature. No direction
    is claimed to identify the true child.

## Recursion and nonclaims

43. For every permitted \(t\ge1\), the child bit bound is \(n-t-1\), up to
    harmless endpoint conventions. Fixed-ratio recursion follows only when
    \(t\ge\eta n-O(1)\).
44. At P175 precision, the child bound is
    \(3n/4+(\log n)^{O(1)}\); a fixed \(\rho>3/4\) absorbs the additive
    polylogarithmic term after a finite prefix.
45. A numerical-QP number of late side calls is absorbed into the P183
    coefficient. This does not validate two early \(n-o(n)\)-bit children.
46. The valid single-chain recurrence
    \(T(n)\le T(n-1)+\operatorname{QP}(n)\) is explicitly preserved.
47. F210 V2 proves no guaranteed selector, no all-input reduction, and no
    factoring algorithm.
48. F210 V2 does not close adaptive bases, asymmetric child-factor
    statistics, integral bounded-point algorithms, or a construction that
    reaches the late range on one spine.
49. No experimental mathematical computation, randomized evidence, or
    durable-ledger edit supports this packet.

