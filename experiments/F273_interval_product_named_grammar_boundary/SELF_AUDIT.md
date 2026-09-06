# F273 author self-audit

## Status

This is the author's check of the frozen proof-only candidate. It is not a
hostile audit or an independent reconstruction.

## Theorem 1 checks

1. The coefficient ring is an integral domain and the theorem is an exact
   characteristic-zero symbolic statement. It does not infer an identity
   from finite modular data.

2. The variables \(e_0,o_0,z_1,\ldots,z_r\) are algebraically
   independent. Actual affine jets can lie on a smaller variety. The
   theorem explicitly leaves identities on that variety open.

3. Vanishing on one full generic axis removes every monomial with zero
   degree in the corresponding child variable. Vanishing on both axes
   leaves only monomials divisible by \(e_0o_0\).

4. The rational extension requires a denominator that is defined and
   nonzero on both axes. It does not cancel a child zero through an
   undefined \(0/0\) expression.

5. The result is algebraic. Divisibility by \(e_0o_0\) does not prove a
   general circuit lower bound or force a circuit to materialize the two
   factors as separate registers.

6. Corollary 1.1 assumes that the public descriptors are independent of
   the formal leaves. It proves only that a literal summary dependency cone
   must cover every independent leaf. The affine specialization
   \(y_j=x+j\) is expressly outside that formal independence argument.

## Theorem 2 checks

7. Rank at least \(k\) over a field is equivalent to one nonzero
   \(k\)-minor. The minor used modulo \(p\) need not be the same as the
   minor used modulo \(q\); either existence statement separately excludes
   that prime from the gcd of all minors.

8. At \(k=m\), there is one determinant. The two rank hypotheses say
   exactly that \(p\) divides it and \(q\) does not.

9. For the diagonal interval, \(p\leq B<q\) and \(B<2p\). Therefore
   \(p\) is the sole \(p\)-multiple and there is no \(q\)-multiple. The
   matrix has local nullity exactly one.

10. A larger local nullity can move prime support into an earlier
    determinantal divisor. F273 makes no claim in that case.

11. The theorem says where the guaranteed prime occurs in the Smith
    invariants. It gives no lower bound for a hypothetical algorithm on a
    different succinct matrix representation.

## Theorem 3 checks

12. The resultant of a monic polynomial with its derivative differs from
    the discriminant only by the standard sign. Taking absolute value
    removes the sign.

13. A difference \(d\) occurs in exactly \(m-d\) root pairs. The same
    multiplicity occurs for \(d\) in
    \(1!2!\cdots(m-1)!\). This proves both forms of \(D_m\).

14. Dividing the two positive integer formulas for \(D_{m+1}\) and
    \(D_m\) gives \((m!)^2\). This is an exact integer ratio, not a
    modular inverse operation.

15. The lower bit-length bound uses \(\Theta(m)\) terms with weight
    \(\Theta(m)\) and logarithm \(\Theta(\log m)\). The upper bound is
    immediate. Small \(m\) is absorbed by constants.

16. If \(\gcd(B,N)>1\), the balanced inequalities make it a proper factor.
    Otherwise \(B\ne p\), and \(p\leq B\) sharpens to
    \(p\leq B-1<q\). Hence \(p\), but not \(q\), occurs among the bases of
    \(D_B\).

17. The discriminant is a valid new-looking factor-bearing scalar, but its
    displayed formula is a weighted remote product. No evaluation
    algorithm is inferred from its short description.

## Theorem 4 checks

18. In \(R_c(m)\), the smallest factor is
    \(cm-(m-1)=(c-1)m+1>0\). The resultant has no omitted sign.

19. Splitting both length-\(2m\) blocks gives separations
    \(2c,2c+1,2c-1,2c\). Resultant multiplicativity gives exponents
    \(1,1,1,1\), hence the middle \(R_{2c}\) is squared.

20. The offset union starts at \(\{1,2,3\}\). Consecutive triples overlap,
    and induction gives every integer through \(2^{t+1}-1\). The count is
    for literal recursive expansion with memoization, not for every
    algorithm.

21. With \(S(k)=1!2!\cdots(k-1)!\), the numerator factorial range in
    \(R_c(m)\) is \(cm!,\ldots,((c+1)m-1)!\), and the denominator range is
    \(((c-1)m)!,\ldots,(cm-1)!\). Their prefix ratios give (22) with the
    stated indexing. The \(c=1\) endpoint uses \(0!=1\).

22. The formula for \(R_c\) is known to be an integer because it was
    derived from the product definition. That fact does not make
    \(S(cm)\) invertible modulo a composite modulus.

23. On the unresolved balanced branch, \(S(B)\) contains \(p!\) and no
    factor at least \(q\), so its gcd with \(N\) is exactly \(p\).

24. For \(M=2^tq_0\), a direct expansion of \(R_1(M)\) has
    \(2M/q_0-1\) base offsets. The cross term in \(D_M\) starts at
    \(R_1(M/2)\) and has \(M/q_0-1\) base offsets. Both are
    \(\Theta(M/q_0)\).

25. A fixed numerical quasipolynomial satisfies
    \(\log Q(n)=o(n)\). Thus dividing an exponential remote length by a
    quasipolynomial base length remains exponential in \(n\).

26. The storage bound assumes one explicit residue word per memoized
    offset. The streaming bound counts explicit distinct-state processing.
    Neither applies to a new implicit representation.

## Provenance and exclusion checks

27. P173, P174, and P177 are context only. Their exact statement and proof
    hashes are recorded. No F273 theorem depends on them.

28. The packet contains no source code, finite dataset, benchmark,
    compilation, local computation, remote computation, or empirical
    extrapolation.

29. The result is not an interval-product lower bound. The highest-risk
    audit point is any sentence that accidentally upgrades a literal
    recursion count or coordinate-ring divisibility statement into a claim
    about all succinct circuits. The statement and proof repeatedly exclude
    that upgrade.

30. The correct search consequence is a named-grammar kill only. A
    finite-dimensional transition with independently quasipolynomial
    coefficients, an affine-specific identity, a characteristic-specific
    identity, or a nonlinear Archimedean statistic remains open.
