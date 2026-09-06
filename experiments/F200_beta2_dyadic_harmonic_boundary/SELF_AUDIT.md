# Self-audit of F200

## Verdict

PASS as a narrow proof-only candidate.  It is not ready for promotion.  It
needs a fresh hostile audit and a statement-only reconstruction.

## Checks performed

1. **Unique exceptional index.**  The inequalities \(p\leq B<q\) and
   \(B<2p\) leave exactly one index in \([1,B]\) sharing a factor with
   \(N\), namely \(p\).
2. **Sign of the recurrence.**  Direct substitution into
   \(A_j=(-1)^j\binom{N-1}{j}\) gives
   \(j(A_j-A_{j-1})=-NA_{j-1}\), and therefore
   \(A_{j-1}/j=(A_{j-1}-A_j)/N\).
3. **Exceptional fractional part.**  P171 gives
   \(A_{p-1}\equiv1\pmod N\), so division by \(p\) gives fractional part
   \(+1/p\), not \(-1/p\).
4. **Root floor sign.**  The root sum is
   \((1-A_B)/N=1/p-h\).  Its floor is \(-h\).
5. **Active gcd orientation.**  An active subset has
   \(D_I\equiv q\pmod N\), so \(\gcd(D_I,N)=q\).  The corresponding index
   product has gcd \(p\).
6. **Transform scope.**  Full support is asserted for the delta in the
   quotient coefficient group.  It is not asserted for a particular
   efficiently evaluable numerical transform of the original integer
   sequence.
7. **Gauge scope.**  The symmetry concerns additive residues and existence
   of integer representatives.  False paths need not satisfy the true
   Archimedean sizes or floors.  Those are explicitly left open.
8. **Run-count scope.**  The exponential count applies only to the literal
   summation-by-parts endpoint evaluator for residue cells.  No general
   circuit lower bound is claimed.
9. **Mahler scope.**  The density argument excludes a value-local continuous
   integrality indicator.  It does not exclude functions using \(N\), a
   succinct rational presentation, discontinuous order operations, or
   correlations special to the integer parts.
10. **Cyclotomic scope.**  The extension-degree statement is conditional on
    the relevant local order \(\operatorname{ord}_p(2)\) exceeding the cap.
    It does not cover complex approximation or implicit symbolic phases.

## Highest-risk claims for hostile review

1. Confirm the P159--P161 interface used in the optional cyclotomic
   corollary.  The asserted implication uses only that the final rough
   element is a power of two and its order divides
   \(\operatorname{ord}_p(2)\).  If that interface is not exact, delete the
   corollary; none of Theorems 1--5 depends on it.
2. Check the asymptotic wording for \(B/2^t\) at the P175 threshold when
   the precision deficit is a general fixed numerical polylogarithm.
3. Check the algebraic-integrality formulation of the Fourier coefficient
   in \(K/\mathcal O_K\).  The Walsh and Haar claims do not depend on it.
4. Keep the distinction between an exact support oracle and an approximate
   phase estimator.  Only the exact equality reduction is used as a proof.

## Computation and sources

No computation and no new external source were used.  The only imported
premises are the promoted P171 recurrence/jump, the P173 power-of-two
binomial interface, P175's reciprocal target, and the elementary local-field
fact that prime-to-residue-characteristic roots of unity reduce injectively.
