# F274 author self-audit

## Status

This is the author's own check.  It is not a hostile audit, a blind
reconstruction, an outside-family audit, or a computational experiment.

## Threshold and regular-state checks

1. The balanced inequalities give \(p<\sqrt{pq}<q\), hence
   \(p\leq B<q\).  No stronger estimate is used.

2. The shift on delta functions is one \(r\)-cycle.  The delta function at
   zero is cyclic, so the minimal polynomial has degree \(r\), not merely a
   divisor of degree below \(r\).

3. In characteristic \(r\), \(Z^r-1=(Z-1)^r\).  Thus the minimal
   polynomial of \(\Delta_r=T_r-I\) is exactly \(Z^r\), and
   \(\Delta_q^B\ne0\) follows from \(B<q\).

4. The nonzero \(q\)-side operator need not be nonzero on a selected probe.
   The statement does not claim a public witness vector.

5. The full regular state has dimension \(r\), exponential in the input
   length on balanced semiprimes.  Calling its threshold exact does not call
   it efficient.

## Finite-state checks

6. Theorem 2 applies only to \(T_r\)-stable subspaces, quotients, and
   subquotients of the regular representation.  It does not classify an
   arbitrary matrix family over \(\mathbb F_r\).

7. Every induced difference is nilpotent.  Nilpotency index is at most the
   vector-space dimension, so \(d_r\leq B\) implies the \(B\)-th power is
   zero.  This conclusion holds separately at \(p\) and \(q\).

8. A global free state can lose rank on reduction.  This only decreases
   \(d_r\) and cannot restore the threshold.

9. The numerical-QP comparison is asymptotic.  It is asserted only for all
   sufficiently large balanced inputs.  Finitely many small inputs are not
   covered by that comparison.

10. The result concerns explicit dimension.  A circuit or compressed data
    structure can name an exponentially large operator without storing its
    full basis; that possibility remains open.

## Polynomial-difference checks

11. Cyclic \(\Delta_r\) and ordinary integer-polynomial \(\delta\) are
    different operators and are named separately.  The proof of Theorem 3
    uses no wraparound identity.

12. Inclusion-exclusion proves
    \(\delta^kX^t(0)=k!S(t,k)\).  Shifting the input and expanding by the
    binomial theorem preserves integrality of the quotient by \(k!\).

13. The coefficient ring is \(\mathbb Z[X]\).  The theorem remains valid
    for arbitrarily high degree and sparse presentation, but it does not
    cover rational monomial coefficients.

14. The integer-valued polynomial \(\binom Xk\) is an exact counterexample
    to an overbroad version: its \(k\)-th difference is one.  Its monomial
    coefficients have a \(k!\) denominator.  The packet states this
    exclusion.

15. Divisibility by \(B!\) is not an evaluator lower bound.  The remaining
    multiplier can vanish modulo \(q\), and another representation can
    compute the whole scalar without separately naming \(B!\).

16. Evaluating the normalized integer in (19) does not require modular
    inversion, but it also removes the universal \(p\)-factor.  Direct
    modular inversion of \(B!\) is invalid.

## Rational-gauge checks

17. Translation orbits are taken among monic irreducibles over
    \(\mathbb Q\), not only linear factors.  This covers irreducible
    numerator and denominator factors of every rational function.

18. A nonconstant characteristic-zero polynomial cannot be periodic under
    a nonzero integer shift.  Hence each orbit can be indexed without a
    finite cycle.

19. Necessity of the orbit sum is a telescoping valuation identity.
    Sufficiency uses finite cumulative sums.  The condition at infinity
    fixes the remaining rational constant to one.

20. The criterion is over \(\mathbb Q(X)\).  Finite-characteristic
    coboundaries can exist because translation orbits close after \(r\)
    steps.  Those characteristic-dependent gauges remain outside the
    theorem.

21. \(R=X\) fails already at infinity.  The positive control
    \((X+1)/X\) has \(h=X\) and telescopes with the stated endpoints.

22. A rational identity does not authorize inversion modulo \(N\).  Every
    evaluated denominator must be gcd-screened.  A gcd of \(N\) is not
    automatically proper; saturated gcds are explicitly not called
    factors.

## Matrix checks

23. Taking determinants in the gauge equation is legitimate in
    \(\operatorname{GL}_d(\mathbb Q(X))\).  It gives a necessary scalar
    coboundary condition.

24. The determinant criterion is not sufficient for a matrix gauge.  The
    packet makes no such claim.

25. The ordered product in (32) has the larger shift on the left.  This is
    forced by iterating \(G(X+1)=A(X)G(X)\).

26. Determinant-one systems escape the determinant obstruction.  The
    displayed unipotent system is a telescope decoy, not evidence that all
    determinant-one systems are trivial.

27. Semilinear maps, local Frobenius operators, nonlinear observables, and
    characteristic-dependent gauges do not live in
    \(\operatorname{GL}_d(\mathbb Q(X))\) as used here.

## Search and evidence checks

28. No C++ source, executable, dataset, benchmark, local research run, or
    remote run was created.  The decision not to search follows from the
    proved collapse of the proposed grammar, not from a finite null result.

29. The future admission gates require a candidate outside all three exact
    named models before implementation.  They do not assert that such a
    candidate is impossible.

30. The packet proves no numerical-QP interval evaluator, factorer, general
    circuit lower bound, or all-input statement.
