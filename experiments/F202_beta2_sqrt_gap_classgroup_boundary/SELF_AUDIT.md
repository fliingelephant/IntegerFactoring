# Self-audit of F202

## Verdict

PASS as a narrow proof-only candidate.  It is not ready for promotion.  It
needs a fresh hostile audit and an independent statement-only
reconstruction.

## Checks performed

1. **Signs and offsets.**  Expanding
   \(N=(B-a)(B+c)\) gives \(E=B(c-a)-ac\).  Both norm identities have the
   positive sign \(+E\), and \(d=c-a=p+q-2B>0\).
2. **Discriminant.**  Substitution gives
   \(d^2+4Bd-4E=(p+q)^2-4pq=(q-p)^2\).  The factor formulas use trace
   \(2B+d\), not \(2B-d\).
3. **Range.**  Balance gives \(d\leq q-p<p\), while the floor definition
   gives \(1\leq E\leq2B\).
4. **Recursive cost.**  For the promised inputs \(n\geq4\) and
   \(E<2^{n-1}\).  There is exactly one recursive complete-factorization
   call.  The theorem does not pretend that the missing postprocessor has
   been constructed.
5. **Early gcd.**  \(\gcd(E,N)=\gcd(B^2,N)\).  Any nonunit branch is a
   proper factor because \(0<B^2<N\).
6. **Mixed-root orientation.**  A mixed sign modulo \(p,q\) makes the two
   gcds with \(r\pm B\) complementary.  The converse CRT construction uses
   the factors and proves exact equivalence.
7. **Norm denominator.**  In \(x^2+Ey^2=N\), a hidden prime dividing \(y\)
   would also divide \(x\), contradicting squarefreeness.  Thus
   \(xy^{-1}\bmod N\) is valid.
8. **Congruence scope.**  The identity modulo \(m\mid E\) accepts every
   unit candidate *factor residue*.  It does not claim that every arbitrary
   \(d\bmod m\) passes, or that nonlocal auxiliary moduli are useless.
9. **Class sign.**  From
   \((\alpha)=\mathfrak p\mathfrak q\), the mixed choice is
   \(\mathfrak p\bar{\mathfrak q}\), with class \(C^2\), not \(C\) or an
   ambiguous class.  Every genus character kills this square.
10. **Principal-norm criterion.**  The mixed norm-\(N\) ideal has a generator
    \(x+y\sqrt{-E}\) exactly when \(C^2=1\).  The theorem does not claim that
    factorization of \(E\) gives the full class group.
11. **Finite certificate.**  All products, offsets, gcd orientations, the
    root congruence, and the four possible \(|x|\) values were checked
    exactly.  The mixed form reduces to \([3,-2,9]\), outside the two-element
    ramified subgroup.
12. **No inflated lower bound.**  The final section explicitly leaves open
    compressed principal-genus navigation, nonlocal congruences, integer
    size information, and direct P175 prefix selection.

## Highest-risk points for hostile review

1. Check the proper-ideal convention in the passage from a mixed CRT root
   to the class \(C^2\).  Reversing every ideal convention changes this to
   \(C^{-2}\), which has the same genus and principality consequences.
2. Check that the order \(\mathbb Z[\sqrt{-E}]\) formulation remains proper
   when \(-4E\) is nonfundamental.  The proof uses only primes \(p,q\)
   coprime to \(2E\); conductor-supported noninvertible ideals are not called
   class-group elements.
3. Keep the factor-residue congruence boundary separate from a lower bound
   on all trace-residue wheels.
4. Check the reduced-form transformations in the \(N=2627\) certificate and
   the assertion that the ramified forms for \(2\) and \(13\) give the same
   order-two class.

## Computation and sources

No numerical search, external source, or benchmark was used.  The finite
certificate is verified by the displayed exact arithmetic.  P175 is used
only to identify the reciprocal-prefix terminal; none of Theorems 1--5
depends on its proof.
