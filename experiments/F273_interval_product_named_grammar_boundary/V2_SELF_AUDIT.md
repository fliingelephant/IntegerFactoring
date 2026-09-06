# F273 V2 author self-audit

## Status and V1 preservation

This is the author's check of the additive V2 repair. It is not a fresh
hostile audit or an independent reconstruction.

All V1 theorem files, the V1 manifest, the V1 freeze, and both V1 audits
remain unchanged. The hostile V1 PASS has SHA-256

a8ff865f43d29e5af1c8956bd2c1bcb65fbf53f97339da024db4e8f2a35e0cb6.

The strict V1 blind FAIL has SHA-256

9bc7775fd05ec20c9f78923043857504a5795fef03966893d16535ae7a50cda9.

V2 addresses both blind objections mathematically rather than changing the
V1 record.

## Child-coordinate checks

1. The coefficient ring is an integral domain and the theorem is an exact
   symbolic statement. It does not infer an identity from finite modular
   data.

2. The variables \(e_0,o_0,z_1,\ldots,z_r\) are algebraically
   independent. Actual affine jets can lie on a smaller variety. The
   theorem explicitly leaves identities on that variety open.

3. Vanishing on one full generic axis removes every monomial with zero
   degree in the corresponding child variable. Vanishing on both axes
   leaves only monomials divisible by \(e_0o_0\).

4. The rational extension requires a denominator whose axis
   specialization is a nonzero polynomial. It does not cancel a child zero
   through an undefined \(0/0\) expression.

5. Divisibility by \(e_0o_0\) does not prove a general circuit lower bound
   or force a circuit to materialize two separate factor registers.

6. Corollary 1.1 assumes that public descriptors are independent of the
   formal leaves. It proves only that a literal dependency cone covers all
   independent leaves. The affine specialization \(y_j=x+j\) is outside
   that argument.

## Corrected Smith checks

7. Rank at least \(k\) over a field is equivalent to one nonzero
   \(k\)-minor. The witnesses modulo \(p\) and modulo \(q\) can differ.
   Their separate existence excludes both primes from
   \(\Delta_k\) for \(k<m\).

8. At \(k=m\), the sole minor is the determinant. It is divisible by
   \(p\) and not by \(q\), so its gcd with \(N\) is \(p\).

9. Since \(p\nmid\Delta_{m-1}\) and \(p\mid\Delta_m\), the quotient
   \(d_m=\Delta_m/\Delta_{m-1}\) is divisible by \(p\). Since
   \(q\nmid\Delta_m\), it is not divisible by \(q\). Thus
   \(\gcd(d_m,N)=p\).

10. For \(A_B=\operatorname{diag}(1,\ldots,B)\),
    \(\Delta_B=B!\). This is a determinantal-divisor statement, not a
    statement about the last invariant factor.

11. The nonzero minors of size \(B-1\) are \(B!/i\). Primewise minimum
    valuations give
    \(\Delta_{B-1}=B!/\operatorname{lcm}(1,\ldots,B)\).
    Therefore \(d_B=\operatorname{lcm}(1,\ldots,B)\).

12. Because \(p\leq B<q\), both \(B!\) and the lcm are divisible by \(p\)
    and not by \(q\). They are distinct factor-bearing gates. V2 claims no
    reduction or evaluator between them.

13. A larger local nullity can move prime support into an earlier
    determinantal divisor. A different succinct matrix can have different
    structure. Both cases remain outside the theorem.

## Discriminant checks

14. The resultant of a monic polynomial with its derivative differs from
    the discriminant only by sign. Absolute value removes the sign.

15. Difference \(d\) occurs in \(m-d\) root pairs and in the same number
    of factorials inside \(1!2!\cdots(m-1)!\). This proves both forms of
    \(D_m\).

16. The positive integer ratio \(D_{m+1}/D_m=(m!)^2\) uses no modular
    inverse.

17. The bit-length lower bound has \(\Theta(m)\) terms, each with
    \(\Theta(m)\) weight and \(\Theta(\log m)\) logarithm. Small \(m\) is
    absorbed into constants.

18. After the \(\gcd(B,N)\) cleanup, \(p\leq B-1<q\). Thus the
    discriminant bases include \(p\) and exclude every multiple of \(q\).

## Corrected cross-resultant counts

19. Splitting two length-\(2m\) blocks gives normalized separations
    \(2c-1,2c,2c,2c+1\), so the exact recursion has the middle factor
    squared.

20. With \(C_0=\{1\}\), the frontier recurrence produces
    \(C_s=\{1,\ldots,2^{s+1}-1\}\). Hence
    \(2^{t+1}-1\) is exactly the base-frontier count after \(t\)
    expansions.

21. States at different levels have different length keys. Summing all
    frontier sizes gives
    \(2^{t+2}-t-3\), the exact full memoized cross-resultant DAG count.
    V2 never calls the base count the whole DAG count.

22. With \(M=2^tq_0\), the standalone base and DAG counts become
    \(2M/q_0-1\) and \(4M/q_0-t-3\).

23. The top cross term in \(D_M\) is
    \(R_1(2^{t-1}q_0)\). For \(t\geq1\), its base and DAG counts are
    \(M/q_0-1\) and \(2M/q_0-t-2\).

24. Every lower discriminant cross term is the offset-one state already
    present at the corresponding level of the top cross-resultant DAG.
    Adding the \(t+1\) distinct discriminant states therefore gives
    \(2M/q_0-1\) total literal states. For \(t=0\), the single
    discriminant state agrees with the same formula.

25. All exact counts remain \(\Theta(M/q_0)\). The fixed-width storage and
    streaming statements apply only to the explicit keyed-state grammar.

26. The superfactorial telescope has the correct endpoints, including
    \(c=1\) where \(0!=1\). Exact integer divisibility does not authorize
    modular inversion of \(S(cm)\).

27. On the unresolved balanced branch, \(S(B)\) contains \(p!\) and no
    factor at least \(q\), so its gcd with \(N\) is exactly \(p\).

## Provenance and exclusion checks

28. P173, P174, and P177 are context only. Their exact statement and proof
    hashes are recorded. No V2 theorem depends on them.

29. The packet contains no source code, dataset, benchmark, compilation,
    local research computation, remote computation, or empirical
    extrapolation.

30. The result is not an interval-product lower bound. It does not identify
    the diagonal lcm gate with the factorial gate. It does not upgrade a
    literal DAG count into a claim about all succinct circuits.

31. A finite-dimensional transition with independently
    quasipolynomial coefficients, an affine-specific identity, a
    characteristic-specific identity, a succinct lcm evaluator, or a
    nonlinear Archimedean statistic remains open.
