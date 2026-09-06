# F193 V2 self-audit

## Verdict

V2 repairs every issue identified by the failed V1 hostile audit. The four
claims remain separate and narrow. No mathematical computation was run.

V2 still requires a fresh hostile re-audit. If that passes, it requires a
fresh statement-only blind reconstruction before promotion.

## V1 disposition

V1 is preserved unchanged with its failed hostile audit. Its false inference
was:

> conductor coprime to \(N\) implies \(\chi(N)\ne0\).

The principal character modulo \(N\) has conductor one but value zero at
\(N\). V2 retains the coefficient identity, weakens the conclusion to rank
at most one, and makes recovery conditional on one nonzero public scalar.

V2 also makes three precision repairs requested by the auditor:

1. it bounds the total sparse-chain encoding, including coefficients;
2. it says that Fricke preserves the global/hidden cusp partition;
3. it restricts the torsion theorem to an auxiliary prime, where the minimal
   polynomial is canonical, and proves the CM characteristic polynomial via
   Tate-module trace and determinant.

## A. Cusp-boundary checks

1. **Reduced endpoints.** Every denominator gcd is taken after rational
   reduction. A spurious common numerator-denominator factor cannot create a
   hidden cusp.

2. **Squarefree hypothesis.** The denominator divisor is a complete label
   only because \(\gcd(d,N/d)=1\). V2 does not extend this classification to
   nonsquarefree levels.

3. **Cancellation.** For each level prime in the old denominator, the
   transformed numerator under \(\Gamma_0(N)\) is a unit at that prime. For
   each absent level prime, the transformed denominator is a unit. Both
   directions are proved.

4. **Boundary support only.** The coefficient on
   \([c_N]-[c_1]\) can carry arbitrary arithmetic information. V2 does not
   control it, a zero-boundary class, periods, internal Hecke action, or a
   compressed dense presentation.

5. **Total input size.** The list length, coefficients, numerators, and
   denominators have numerical-QP total encoding length. The gcd scan is
   therefore numerical QP.

6. **Good Hecke restriction.** Type preservation uses
   \(\gcd(m,N)=1\). Bad-prime \(U_p,U_q\) operators are outside the theorem.

7. **Fricke.** The exact map is \(d\mapsto N/d\). It swaps \(1,N\), swaps
   \(p,q\), and preserves the two-set partition. V2 no longer suggests that
   it acts only on the global pair.

8. **Atkin--Lehner convention.** The determinant statement is only for a
   standard unnormalized integral representative. The public exact-divisor
   label is the primary factor-bearing datum. Opaque circuits and normalized
   analytic matrices are excluded.

## B. Small-modulus checks

9. **Promise.** The identity \(b_N=N+p+q+1\) is used only for distinct odd
   primes.

10. **Strict bound.** The proof gets \(b_N<2(N+1)\le2^{n+1}\) and chooses a
    CRT product strictly above it.

11. **Small bank.** The first \(O(n)\) primes have numerical size
    \(O(n\log n)\), hence \(O(\log n)\) bits. Omitting 2 and 3 does not
    change the bounds.

12. **Auxiliary collision.** Before an oracle call, a proper gcd of the
    auxiliary prime and \(N\) is returned directly. Otherwise the call uses
    a coprime modulus.

13. **Uniformity.** One algorithm takes the varying prime as input under one
    QP bound. V2 does not combine a nonuniform collection of unrelated
    algorithms.

14. **Fixed modulus.** Repetition of one residue does not meet the growing-
    product premise and is not claimed to suffice.

15. **Conditional bridge.** V2 constructs no coefficient evaluator. It
    proves that such a uniform evaluator would be a positive QP factoring
    bridge.

## C. Twist checks

16. **Imprimitive characters.** Equation
    \(a_{f\otimes\chi}(N)=\chi(N)a_f(N)\) remains valid when \(\chi(N)=0\).
    V2 explicitly allows this case.

17. **Rank zero.** A bank of only vanishing rows has rank zero. V2 claims at
    most one, not exactly one.

18. **Recovery criterion.** A nonzero Dirichlet-character value is a root of
    unity and is invertible. Only such a row is claimed to recover the base
    coefficient.

19. **Modulus versus conductor.** Coprimality of the defining modulus with
    \(N\) guarantees nonvanishing. Coprimality of the conductor alone does
    not, unless the character is presented primitively at that conductor.

20. **Coefficient fields.** The information-rank statement is made after
    placing exact values in explicitly represented compatible composita.
    It does not silently assert compatible embeddings or cheap arithmetic
    for arbitrary black-box field encodings.

21. **Algorithmic scope.** A twist can have a different evaluator. If a
    nonzero twist is easy, public division makes the base coefficient easy.
    No evaluator lower bound follows.

22. **One form and index.** Different eigenforms, Rankin products,
    nontwist operations, and unrelated indices remain open.

## D. Torsion checks

23. **Auxiliary prime.** V2 uses \(E[r]\) over the field \(\mathbb F_r\).
    The unique monic minimal polynomial is therefore well-defined. No claim
    is made for the ambiguous singular phrase “the minimal polynomial” over
    a general composite coefficient ring.

24. **Prime-to-characteristic.** Invertibility of \(r\) makes \(E[r]\)
    finite etale and lisse. Characteristic-primary torsion is excluded.

25. **Connected descent.** Etale path transport is natural in the globally
    defined endomorphism, so fiber matrices are conjugate. A disconnected
    CRT base can carry unrelated local maps and is excluded.

26. **Conjugacy invariants.** Over \(\mathbb F_r\), conjugacy preserves the
    characteristic polynomial, canonical minimal polynomial, and exact
    order when invertible.

27. **CM justification.** V2 invokes the prime-to-characteristic Tate module
    to identify trace and determinant before reduction modulo \(r\). It does
    not infer equality of characteristic polynomials from an annihilating
    quadratic alone.

28. **Reduction-only maps.** Local Frobenius, extra ordinary or supersingular
    endomorphisms, and a mixed CRT-glued map need not descend from one global
    \(\alpha\). They remain outside the theorem.

## Combined scope

29. **No general B5 obstruction.** Each named boundary has explicit live
    escapes. No section is used as a lower bound for arbitrary modular or
    torsion representations.
