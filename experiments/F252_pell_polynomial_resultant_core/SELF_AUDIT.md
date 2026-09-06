# F252 self-audit

## Verdict

PASS for the exact statement and proof as frozen. This is a self-audit only.
No hostile audit, strict statement-only reconstruction, computation, or
publication-level literature review has run.

## Algebra checks

1. **Degree drop is separate.** The resultant formula is used only when
   \(k\ell\ne0\). A zero wrap count gives the constant square \(S^2\).
2. **Content is not silently assumed to be one.** The exact formula is
   \(\gcd(S^2,k^2,2k)\). The example
   \(99^2-2\cdot70^2=1,\ k=3\) has content \(3\).
3. **Irreducibility survives nontrivial content.** Dividing by the content
   gives a primitive quadratic with negative discriminant
   \(-4Dk^2/c^2\).
4. **The resultant sign and scale were checked through the complex-root
   definition.** The intermediate form
   \((Dk^2+DE\Delta^2-E\ell^2)^2+4DE^2\Delta^2\ell^2\)
   equals the displayed symmetric formula.
5. **The zero criterion uses positivity.** It requires \(D,E>0\). It does
   not claim the same classification for negative or zero discriminants.
6. **No squarefree discriminant is assumed.** Squarefree \(D,E\) are used
   only for the simplified duplicate classification. In general the exact
   conditions are \(\Delta=0\) and \(Dk^2=E\ell^2\).
7. **Association versus equality is resolved.** Equal root sets give a
   common center and common coefficient \(Dk^2\), so the special constant
   form \(1+A(X-c)^2\) forces literal equality.

## Generic-kernel and root checks

8. **Constant contents do not create a missed generic relation.** Every
   distinct post-wrap polynomial contributes its own irreducible polynomial
   valuation. A binary square product must use every equality class an even
   number of times.
9. **The root is integral.** It is explicitly the product of selected
   \(S_i\)'s and half-powers of duplicate polynomials. No appeal to a
   rational square root or a unit-denominator assumption is made.
10. **The sign is only global.** The positive specialized root is
    \(|H_c(N)|\), so comparison with \(H_c(0)\) introduces only one overall
    sign.
11. **Unit scope is explicit.** Normalized roots use the inverse of the
    supplied root product only after \(\gcd(S_i,N)=1\) is assumed.
12. **The result does not cover specialization-only vectors.** A numerical
    square relation can exist even though the cleaned generic kernel is zero.

## Resultant-core checks

13. **Duplicates are removed before products of resultants are formed.** All
    remaining resultants are nonzero.
14. **Shared-value primes imply resultant primes.** The common evaluation
    point \(N\bmod p\) makes the Sylvester matrix singular modulo \(p\), even
    if a leading coefficient vanishes modulo \(p\).
15. **The converse is not used.** A resultant prime need not divide either
    specialized value.
16. **The saturation exponent is sufficient.** For every \(p\mid a_i\),
    \(v_p(a_i)\le\log_2a_i<\lceil\log_2(a_i+1)\rceil\). Thus every shared
    prime power is removed completely from \(b_i\).
17. **Private nonsquare means a real pivot.** An odd valuation in \(b_i\)
    occurs in no other full row \(a_j\), so it forces the row coefficient to
    zero in every numerical parity dependency.
18. **A square private residual is harmless only for parity.** The theorem
    replaces its column by \(g_i\); it does not discard the separate
    supplied-root screen and makes no claim about nonlinear processing.

## Complexity and scope checks

19. **All algorithms are factor-free.** The proof uses gcd, exact division,
    exponentiation, integer square tests, and polynomial arithmetic only.
20. **Complexity is measured in explicit input length.** Materializing
    \(\mathcal R_i^{e_i}\) has polynomial bit length because both
    \(\log\mathcal R_i\) and \(e_i\) are polynomial in that length.
21. **The QP conclusion is only for an explicit QP bank.** No compression
    theorem for an implicit exponentially large Pell trajectory is claimed.
22. **P68 is not restated as new.** The specific gains are the zero cleaned
    generic kernel, integral generic roots, and explicit resultant-supported
    specialization core.
23. **F250 is not proof evidence.** Its finite null result is mentioned only
    as compatible context.

## Remaining counterexample space

The packet does not exclude any of the following:

- a post-wrap singleton that becomes an integer square only at \(X=N\);
- a numerical duplicate from two distinct Pell polynomials;
- a multirow parity dependency supported wholly on pairwise resultant primes;
- a non-global normalized root produced by such a specialization-only
  dependency; or
- an adaptive or nonlinear use of the resultant integers.

These exclusions are deliberate and appear in the statement.
