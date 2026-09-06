# F244 self-audit

## Result

PASS as a self-audited candidate.  No hostile audit or blind reconstruction
has run.

## Algebra checks

1. The sign convention is fixed: `a=+1` means `p-1`, and the torus Jacobi
   sign is `J=ab`.  Thus `(N-J)(N+J)=N^2-1` in every orientation.
2. For odd primes, one sign on each hidden factor carries the complete
   valuation.  This makes the lcm valuation `min(v_ell(A),v_ell(B))` and
   the residual valuation `|v_ell(A)-v_ell(B)|`.
3. At two, one shifted order has valuation one and the other has valuation
   `v_2(p^2-1)-1`.  The common lcm loses one factor two.  The residual
   product loses an additional factor two exactly when the two total
   valuations differ.  This checks the indicator `delta` in (6).
4. A prime cannot occur in two residuals.  In particular, when the total
   two-adic valuations differ, only the side with the larger valuation can
   retain a factor two.
5. The product bound gives only `sqrt(N)/sqrt(G)`.  Nothing in the proof
   changes this into `N^(1/4)`.
6. The averaged probability uses F242's factor `1/(2 min(x,y))` and the
   one-quarter orientation probability.  The constants in (9) are
   `1/8`, then `1/2` after AM--GM.

## Infinite-family quantifier checks

7. The four selected primes are chosen first.  The first Linnik application
   chooses `p` in one reduced class.  The second application occurs only
   after the complete factorization support of `p^2-1` is fixed.  There is
   no simultaneous-prime requirement.
8. Primitive roots are imposed as residue classes, not obtained from a
   claim that a fixed integer is primitive for infinitely many primes.
   Artin's conjecture is not used.
9. The `rho` primes are coprime to `p^2-1` because `p` has order
   `rho-1>2` modulo each.  Hence the second CRT system has coprime moduli.
10. Every second-stage residue is a unit.  Both Linnik invocations are in
    reduced residue classes.
11. Exact common support is checked prime by prime.  At two, the residues
    `p=5 (mod 8)` and `q=3 (mod 8)` give total valuation three on both
    sides.  At three, `p=1 (mod 3)` and `q=2 (mod 9)` give common valuation
    one.  Every prime `s>=5` in `p^2-1` is explicitly assigned a `q`
    residue different from both signs.  Thus no unspecified common divisor
    remains, and `G=24` exactly.
12. The sign locations give the exact table `(2,12,2,2)`, not only upper
    bounds.
13. Linnik bounds `p` by a fixed power of `X`.  Its second modulus is
    `O(p^2X^2)`, so it also bounds `q` by a fixed power of `X`.  Conversely,
    the selected divisibilities force `p,q>X`.  Hence `n=Theta(log X)` and
    every selected prime is at least `2^(c n)` for one absolute `c>0`.
14. Letting `X` increase makes the selected prime divisors unbounded, so
    the semiprimes cannot repeat infinitely often.

## Signed-word checks

15. If the opposite hidden prime is primitive modulo a selected divisor,
    multiplying it by `-1` can reduce its order by at most two.  This gives
    the uniform lower bound `(ell-1)/2`.
16. A divisor of `N^k+1` has order at most `2k`; this accounts for the
    factor four in condition (33).
17. A positive product has bit length at least that of every factor, and
    `N^k-1` has at least `k` bits on this family.  Thus a QP-bit word cannot
    hide an exponential exponent.
18. The no-hit statement is pointwise for every exponent below the bound.
    It is therefore unaffected by adaptive selection inside the stated
    grammar.  It says nothing about factors found by other adaptive
    operations.
19. The F242 base `N-ab` also misses the selected divisor, because a
    primitive root modulo a prime above five is not either sign.
20. Common exact orders can only divide their local-order gcd.  Even
    granting every orientation and its hidden sign label, their lcm is at
    most `12`.  This makes the quarter-terminal conclusion an upper bound
    on a strengthened oracle model.
21. A split local quadratic algebra has at most `2r-1` zero-norm pairs and
    a nonsplit algebra has one.  Together with F242's constant clean
    acceptance probability, this keeps incidental sampler factor exits at
    `O(1/p+1/q)`, which is exponential on the constructed family.

## Scope checks

22. The family is existential.  It is not claimed to be generated in
    polynomial or quasipolynomial time from its index.
23. The obstruction covers only products of `N^k-1` and `N^k+1`, together
    with exact common-order accumulation.  It does not cover difference
    words, quotient or carry data, arbitrary discriminant-dependent words,
    or general factoring algorithms.
24. The F242 probability bridge is used as a candidate dependency until
    F242 completes its own verification cadence.  The algebraic identities,
    the CRT--Linnik family, and the signed-support obstruction do not depend
    on F242.
25. No computation, public search, or unproved distribution assumption is
    used.
