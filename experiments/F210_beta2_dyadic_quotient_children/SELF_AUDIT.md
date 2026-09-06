# F210 self-audit

## Promise and imports

1. The parent promise is exactly the balanced squarefree semiprime promise
   (N=pq), with distinct odd primes (p<q<2p).
2. The dyadic state assumes a correct P179 reciprocal prefix and
   (2m<p). F210 does not construct that prefix.
3. P172 is used only after factor-first stripping supplies a fully known
   exact common local order coprime to (N).
4. P183 is used only for one decrement spine plus fixed-ratio late-stage
   side children. It is not applied to an early two-near-child tree.

## Child arithmetic

5. The relation (b=a\mathsf{xor}\delta) is derived from the exact integer
   expansion of (N=(r+mP)(c+mQ)), not guessed from samples.
6. Both candidate numerators are divisible by (2m).
7. Positivity uses (r_a,c_a<2m<p), hence (r_ac_a<p^2<N).
8. Coprimality uses (gcd(2m,N)=1) and the strict bound
   (r_a,c_a<p). No hidden primality test is used.
9. The two tables distinguish the cases (delta=0) and (delta=1).
10. The sign in (D=(c-r)/2) is fixed by the convention
    (D=K_0-K_1).
11. Coalescence is exactly (delta=1,r=c). The first
    (N\equiv3\pmod4) stage is a special case, not the converse for every
    later stage.
12. The bound on common support applies only outside coalescence.
13. Every common prime power divides (|D|), but private prime support of
    either child is unrestricted by this theorem.
14. The lcm formula is exact in both the coalesced and noncoalesced cases.

## Half-translation and local scope

15. The translation is
    ((P,Q)\mapsto(P-1/2,Q-\sigma/2)), with
    (sigma=(-1)^\delta). Both signs were expanded directly.
16. The matrix identity uses the same half-translation and has determinant
    (N) on both sides.
17. The physical coordinate identity is (XY-N=hF_a). Division by (h)
    is used only where two is a unit.
18. Over every odd modulus, the coordinate changes and the half-translation
    are invertible. Thus the claimed solution-set bijection is exact.
19. The odd-local obstruction covers only invariants under public affine
    coordinate isomorphism. It does not say that the raw coefficient lists
    or child prime supports are equal.
20. In particular, F210 does not claim equality of Jacobi symbols,
    higher-residue symbols, exact orders, smoothness profiles, or other raw
    statistics computed on the different prime divisors of (K_0,K_1).
21. The genus and class statement concerns the abstract split curve after
    odd-local coordinate change. It does not cover class groups of new
    integral orders constructed asymmetrically from (K_a).
22. At a child prime power, the square root is explicitly scaled by
    (r_ac_a^{-1}). No unscaled square root of (N) is asserted.
23. The character identity is only multiplicativity applied to
    (N=r_ac_a); it supplies no orientation theorem.
24. The (2)-adic count enumerates lifts of the fixed (X)-class. Each
    one determines a unique (Y=NX^{-1}), whose class modulo (h) is
    forced. The count is valid for both children.
25. In a coalesced state, the other chart can contain the swapped point
    ((q,p)). The statement claims uniqueness only after imposing the
    orientation (X<\sqrt N<Y).

## Order bridge and resultants

26. Complete factorization of (K_a) really gives complete factorization
    of (H_a=2mK_a), since (2m) is a known power of two.
27. The exact common annihilator is
    (G=\gcd(H_0,H_1)=2m\gcd(K_0,K_1)), including coalescence.
28. Simultaneous global return is an explicit condition. It is not inferred
    from either child being the true one.
29. Factor-first stripping tests every prime multiplicity of the known
    annihilator. Without a proper gcd, every retained prime multiplicity is
    required in both local orders, so the final orders are equal exactly.
30. The final common order is coprime to (N) because it divides (G),
    while both (2m) and both children are coprime to (N).
31. The P172 terminal is invoked only under the explicit
    (N^{1/4}/e\le Q(n)) bound.
32. The polynomial gcd identity is exact. The ordinary resultant is zero
    for the trivial reason that (X-1) is always common; no information is
    inferred from that zero.
33. An asymmetric return is recorded only as a public feature. No direction
    is claimed to identify the true child.

## Recursion and nonclaims

34. The child bit bound is (n-t-1), up to harmless endpoint conventions.
    Fixed-ratio recursion follows only when (t\ge\eta n-O(1)).
35. At P175 precision, the child bound is
    (3n/4+(\log n)^{O(1)}); a fixed (ho>3/4) absorbs the additive
    polylogarithmic term after a finite prefix.
36. A numerical-QP number of late side calls is absorbed into the P183
    coefficient. This does not validate two early (n-o(n))-bit children.
37. The valid single-chain recurrence
    (T(n)\le T(n-1)+\operatorname{QP}(n)) is explicitly preserved.
38. F210 proves no guaranteed selector, no all-input reduction, and no
    factoring algorithm.
39. F210 does not close adaptive bases, asymmetric child-factor statistics,
    integral bounded-point algorithms, or a construction that reaches the
    late range on one spine.
40. No experimental mathematical computation, randomized evidence, or
    durable-ledger edit supports this packet.
