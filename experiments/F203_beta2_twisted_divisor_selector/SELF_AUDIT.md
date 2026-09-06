# F203 self-audit

## Algebra and promises

1. The balance promise is used only to place \(p\) in
   \((B/2,B]\) and \(q\) above \(B\).
2. The selector algebra needs a correct prefix
   \(u=p^{-1}\bmod m\). F203 does not construct this prefix.
3. The condition \(2m<p\) makes all canonical child residues positive and
   below both hidden primes. It is satisfied throughout the P175
   quarter-precision range for sufficiently large balanced inputs.
4. The sibling relation uses the exact identity
   \((r+am)^{-1}=r^{-1}+am\bmod2m\). It needs \(m\) even and \(r\) odd.
5. The value \(c_0=N(r^{-1}\bmod2m)\bmod2m\) is public. The definition of
   \(\lambda\) is used only when its reduction modulo \(m\) is \(r\).
6. The divisor coefficient includes all four divisors
   \(1,p,q,N\). The definition of \(T\) removes exactly the two public ones.
7. In the opposite-sign case, \(T=\epsilon(p-q)\), so the next bit is the
   negative of the sign of \(T\). This sign reversal is explicit.
8. Exact square roots are followed by parity, product, and ordering checks in
   an implementation. The promise proof makes those checks pass.

## Quotient checks

9. The quotient \(K=(N-rc)/m\) is integral because the product residues are
   correct modulo \(m\).
10. The proof of \(\gcd(K,N)=1\) uses \(r,c<m<p\), not an unjustified
    cancellation by an unknown factor.
11. The parity relation is \(\delta=a+b\bmod2\), hence
    \(b=a\mathbin{\mathsf{xor}}\delta\).
12. Both candidate values \(K'_a\) are integers. Their positivity and
    coprimality use \(2m<p\).
13. For \(\delta=1\), the two values differ by \((r-c)/2\), and coalesce
    exactly when \(r=c\).
14. At \(m=2,N\equiv3\bmod4\), the common value is
    \((N-3)/4\), not \((N-1)/4\).

## Complexity and scope

15. The one-child recurrence is stated as a conditional accounting fact.
    F203 does not claim that factoring \(K\) or \(K'_a\) reveals the bit.
16. No fixed-ratio contraction is required or asserted.
17. Coalescence is not a general lower bound. It applies to the displayed
    quotient state and proves only that this state is identical under the two
    orientations.
18. The Lambert series is a formal coefficient identity. No truncation,
    modular-form, theta-series, or coefficient-computation algorithm is
    inferred from it.
19. At \(m=2\), \(w=\chi_4\), but the weighted coefficient
    \(\sum d\chi_4(d)\) is not confused with the standard unweighted
    sum-of-two-squares coefficient.
20. The factoring equivalence is promise-specific. It does not cover prime
    powers, more than two factors, an unknown factor ordering, or arbitrary
    composites.
21. P165 is cited only for its established scope: it closes uniform-base
    return after factoring \((N-1)/2\), not every adaptive deterministic use.
22. No computation, cross-family audit, human audit, or publication-level
    literature review has been run.

