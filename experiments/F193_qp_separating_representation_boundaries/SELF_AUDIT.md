# F193 self-audit

## Verdict

The four statements are independent and internally consistent. Each has a
strict named-model scope. Together they are not a general lower bound for B5
and do not supply an integer-factoring algorithm without one of the stated
oracle or factor-bearing premises.

No mathematical computation was run. Hashing is used only to freeze the
text. The candidate requires a fresh hostile audit and, if retained, a fresh
statement-only blind reconstruction before promotion.

## A. Explicit modular-symbol cusp boundary

1. **Reduced endpoints.** The denominator gcd is taken only after reducing
   the rational endpoint. Otherwise a common numerator-denominator factor
   could create a false hidden cusp.

2. **Infinity.** The convention \(\infty=1/0\) gives type \(N\), consistent
   with the four squarefree cusp labels.

3. **Orbit classification.** The proof establishes invariance prime by
   prime and invokes the standard cusp classification. The conclusion that
   the divisor label is complete uses squarefreeness through
   \(\gcd(d,N/d)=1\). It is false as stated for arbitrary nonsquarefree
   level, where one divisor label can contain several cusps.

4. **Cancellation under \(\Gamma_0(N)\).** If a level prime divides the old
   denominator, the transformed numerator is nonzero at that prime, so
   reducing the fraction cannot cancel it. If it misses the old denominator,
   it also misses the new denominator. This checks both directions.

5. **Sparse representation.** The theorem applies only when every rational
   endpoint is explicitly listed. A compressed vector whose hidden-cusp
   coefficients are computed without materializing endpoints is outside the
   theorem.

6. **Boundary only.** A coefficient on the global line
   \([c_N]-[c_1]\) could equal \(p+q\), \(\varphi(N)\), or another
   factor-bearing integer. The theorem excludes only hidden-cusp support; it
   does not exclude metric information in the coefficient or a class with
   zero boundary.

7. **Cuspidal subspace.** A boundary-zero cuspidal modular symbol is not
   controlled. Neither are periods, modular-symbol pairings, internal Hecke
   matrices, or a quotient whose information is not represented by sparse
   rational endpoints.

8. **Good Hecke hypothesis.** The type-preservation proof requires
   \(\gcd(m,N)=1\), so every diagonal entry in the standard branch is a unit
   at every level prime. It does not cover \(U_p,U_q\), or any bad-prime
   correspondence.

9. **Branch cancellation.** For a good branch, a level prime in the old
   denominator cannot cancel because the transformed numerator is a unit at
   that prime. A level prime absent from the old denominator cannot enter
   through multiplication by a divisor of \(m\).

10. **Fricke action.** Direct reduction of \(-c/(Na)\) toggles every level
    prime, so \(d\mapsto N/d\). On a semiprime this preserves the partition
    \(\{1,N\}\cup\{p,q\}\).

11. **Atkin--Lehner representation.** The statement concerns the standard
    exact-divisor-labeled operator. For \(Q=p,q\), the label and a standard
    integral determinant reveal a factor. It does not claim that every
    opaque circuit inducing the same endomorphism visibly prints \(Q\).

12. **QP accounting.** A QP-length explicit list with QP-bit endpoints can
    be reduced and gcd-scanned in QP bit complexity. No enumeration of all
    level-\(N\) cusps or Manin symbols is used.

## B. Uniform small-modulus amplification

13. **Coefficient identity.** The identity
    \(b_N=(1+p)(1+q)\) is restricted to distinct odd primes. The theorem does
    not claim it for repeated or even semiprimes.

14. **Coefficient bound.** Since \((p-1)(q-1)>0\),
    \(p+q<N+1\). Hence \(b_N<2(N+1)\le2^{n+1}\). The CRT modulus is chosen
    strictly larger than this bound.

15. **Enough small primes.** The first \(O(n)\) auxiliary primes have
    numerical size \(O(n\log n)\) and therefore \(O(\log n)\) bits. Their
    product exceeds \(2^{n+1}\). The theorem does not require an
    \(O(n)\)-bit modulus in one oracle call.

16. **Uniformity.** The same algorithm must accept the varying auxiliary
    prime as input and obey one QP bound. A separate nonuniform promise for
    each modulus is not silently combined.

17. **Fixed modulus.** Repeating one fixed residue gives no additional CRT
    information. The theorem deliberately does not close one fixed modulus
    or a fixed finite set.

18. **The factor 24.** Auxiliary primes 2 and 3 are omitted before inverting
    24. There remain \(O(n)\) primes of the same asymptotic size.

19. **QP closure.** Polynomially many QP oracle calls, polynomial-time CRT,
    exact square root, and verification remain QP. No hidden enumeration of
    \(p+q\) occurs.

20. **Not a supplied evaluator.** Section 2 is conditional. It identifies a
    positive bridge if a uniform evaluator is constructed; it does not
    construct one.

## C. Dirichlet twists

21. **Coprime conductor.** This premise makes \(\chi(N)\) a nonzero public
    root of unity. If the conductor has a proper gcd with \(N\), that gcd
    already factors. If \(\chi(N)=0\), the vanishing is not a hidden local
    separator.

22. **One base form and one index.** The rank-one identity covers twists of
    one fixed \(f\) at \(N\). It does not cover different eigenforms,
    Rankin products, additive combinations, or unrelated indices.

23. **Coefficient fields.** Different cyclotomic coefficient fields do not
    change the identity. After embedding each public character value in its
    stated field, every output is still a known scalar multiple of the same
    coefficient.

24. **Evaluation complexity.** Information equivalence is not an assertion
    that algorithms for the twist and base form have equal cost. An easy
    twist would be useful, but it would evaluate the base coefficient by one
    public scalar division rather than create independent local data.

## D. Globally defined elliptic-torsion endomorphisms

25. **Prime-to-characteristic torsion.** The premise that \(m\) is invertible
    on the base makes \(E[m]\) finite etale and lisse. The theorem does not
    apply to characteristic-primary torsion.

26. **Connected base.** Connectedness and global descent of \(\alpha\) let
    geometric path transport identify its fiber actions up to conjugacy. A
    disconnected CRT base can carry unrelated local maps and is outside the
    claim.

27. **Choice of basis.** The matrices need not be literally equal in
    arbitrary local bases. Conjugacy is sufficient for characteristic
    polynomial, minimal polynomial, and order.

28. **CM formula.** The reduced trace and norm of one global CM endomorphism
    give its fixed degree-two characteristic equation. The formula does not
    select a prime above a split rational prime in the CM field.

29. **New reduction endomorphisms.** Ordinary or supersingular reduction can
    enlarge the endomorphism ring. The theorem controls only the reduction
    of the original global endomorphism, not those new elements.

30. **Local Frobenius.** Frobenius is characteristic-dependent and does not
    descend from one characteristic-zero endomorphism across the two fibers.
    It is explicitly excluded, not proved hard to compute.

31. **Fine CRT orientation.** A pair \((\alpha_p,\alpha_q)\) can be glued
    over \(\mathbb Z/N\mathbb Z\) after the factors are known. Such a mixed
    map need not descend from the connected base and can separate. The
    theorem does not assume or refute a factor-free construction of it.

32. **No general torsion obstruction.** Families in which the curve, torsion
    level, or reduction-only operator varies with \(N\) remain open. The
    result only removes the expectation that a fixed globally defined
    endomorphism will acquire distinct conjugacy invariants in two good
    fibers.

## Combined scope check

33. **No general B5 conclusion.** The statement lists explicit surviving
    interfaces. No section is used to infer that all low-dimensional
    separating representations fail.

34. **No circular promotion claim.** A uniform small-modulus evaluator would
    be a positive factoring bridge, not an obstruction. The other three
    sections classify only named sources of purported independent local
    information.
