# Self-audit for F249

## Scope

This audit checks the algebra, floor endpoints, probability, and complexity
wording in `STATEMENT.md` and `PROOF.md`.  It uses no computation and does
not replace a fresh hostile audit.

## Checks

1. **Small inputs.**  Distinct odd primes give \(N\ge15\), hence \(B\ge3\)
   and \(H\ge1\).  The proof of \(s<H\) includes odd \(B=3\).

2. **The case \(s=0\).**  This means \(B=p\), so the public gcd
   \(\gcd(N,B)\) already returns \(p\).  The recurrence singularity is at
   \(c=0\), outside the sampled range.  No denominator-product claim is
   applied to this case.

3. **Lucas digits.**  Both low digits satisfy \(c-1<p<q\).  The lower index
   is \(p+s\) modulo \(p\) and is below \(q\) modulo \(q\).  Recursive
   Lucas gives the high factor \(\binom{rq}{1}=rq\), even when \(rq\) has
   several base-\(p\) digits.

4. **Nonzero local binomial.**  On \(c>s\), the full range
   \(0\le s\le c-1<p\) ensures \(\binom{c-1}{s}\ne0\pmod p\).  The gcd
   claim screens \(r\) first.

5. **Endpoint.**  The strict inequality \(s<H\), not merely \(s\le H\),
   makes \(c=H\) successful.  It also places \(s\) inside the recurrence
   range when \(s\ge1\).

6. **Probability.**  The successful set has exact size \(H-s\).  The
   conservative bound \(1/3\) follows from \(3s<B\), with even and odd
   floors checked separately.

7. **Unique denominator.**  In the recurrence range, \(0<B-c<B<q\) and
   \(B-c<2p\).  The only possible nonunit is therefore the integer \(p\),
   reached exactly at \(c=s\).

8. **Factorial valuations.**  Since \(p\le B<2p\) and \(B<q\), \(B!\)
   has exactly one \(p\)-multiple and no \(q\)-multiple.  After removing
   the factor \(rN\) from the numerator, a second \(p\)-multiple exists
   exactly at \(j=c+p\), which is present exactly for \(c\le s\).

9. **Product gate.**  For \(s\ge1\), the denominator interval contains
   \(p\) exactly once and no \(q\)-multiple.  Its gcd with \(N\) is
   therefore exactly \(p\), not only a nontrivial divisor.

10. **Central-binomial collapse.**  The numerator interval of
    \(\binom BH\) contains \(p\) because \(s<H\), and contains no second
    \(p\)-multiple or any \(q\)-multiple.  For odd \(B\), the colloquial
    upper-half interval has one extra unit; the packet does not identify the
    two integer products.

11. **Equivalence wording.**  The polynomial-time equivalence is asserted
    for the promise function \(\gcd(N,C_{1,H})\), whose output is \(q\).
    Coefficient-residue evaluation reduces to this function.  The packet
    does not claim a reverse QP reduction from factorization to the entire
    remote binomial residue.

12. **Las Vegas wording.**  The constant success law is conditional on an
    unresolved coefficient oracle.  Since the endpoint is always
    successful, randomness itself is not presented as progress toward an
    evaluator.

13. **Algebraic series.**  The odd-\(B\) multiplier can be nonunit only on
    the already screened \(B=p\) branch.  The finite-prime-field algorithm
    requires a known prime characteristic and characteristic-dependent
    preprocessing.  It is not silently transferred to the composite ring.

14. **Complexity wording.**  Literal Vandermonde evaluation and the known
    holonomic product route are upper-cost boundaries for named methods.
    No general arithmetic-circuit lower bound is inferred.

## Remaining opening

A new numerical-QP method could still evaluate the central or shifted
coefficient modulo \(N\), detect its hidden divisibility, or cross the
singular recurrence without materializing the interval product.  F249 does
not rule out such a method.
