# F243 self-audit

## Proof checks

1. The baseline uses `W=(N^2-1)^n`, not the full F242 exponent.  F242's
   identity already supplies the common shifted gcd through `N-J`; its
   residual formula depends on `W` exactly as used here.
2. Primary saturation is valid because every primary divisor of a shifted
   residual is below `N`, so its exponent is less than `n`.
3. The cross-sign support equivalence is stated only for odd `ell`.  The
   prime two always divides `N^2-1` and is stripped.
4. The conditional success constant keeps all three independent losses:
   residual saturation `1/2`, hidden orientation `1/4`, and F242 powered
   success `1/2`.
5. Exact equal integers are replaced by one in every difference word.  The
   local same-object atoms are not silently identified with exact-integer
   equality atoms.
6. The split and nonsplit quadratic-form fibre counts give the same
   norm-value collision but different norm-of-difference zero laws.
7. The canonical-coordinate bound uses full-torus uniformity from F242.
   It counts at most four points above one coordinate and is independent of
   any equidistribution assumption modulo the exterior prime.
8. The gcd-divisor harmonic bound extends the divisor sum to all positive
   integers.  This only increases the nonnegative ordered-pair sum.
9. Pell trace equality is taken inside the norm-one torus.  In the split
   algebra this restriction rules out independent component choices and
   leaves only `eta^i=eta^j` or `eta^i=eta^-j`.
10. At `h=2T-2`, the only possible sum collision is
    `i=j=T-1`, so the distinct trace collision is still zero.

## Scope that must remain explicit

- The result covers distinct odd semiprimes.  It does not cover prime
  powers, repeated factors, or arbitrary composites.
- The positive divisor bridge grants a complete factorization of
  `N^2-1`.  Producing that factorization is not supplied.
- The collision condition is hidden and existential.  The algorithm does
  not learn which orientation or side satisfies it; the random orientation
  accounts for this with a constant loss.
- The local generic laws do not classify arbitrary integer lifts.
- The canonical-coordinate proof does not cover determinants, resultants
  between different coordinates, nonlinear combinations, or adaptive carry
  words.
- The harmonic bound covers only `gcd(X,N^2-1)` with uniform `X`.  It does
  not cover `gcd(f(X),N^2-1)` for a structured polynomial or an adaptive
  gcd/lcm process.
- A per-prime generic bound is not a factoring lower bound.  Another prime
  in the same residual can still be easy.
- The Pell theorem rules out a bounded consecutive window when its exact
  order is large.  It does not bound that order on all inputs or cover
  nonconsecutive structured exponent sets.

## Numerical checks and defects

- F243-R1 is invalid as confirmatory evidence because a local five-input
  smoke violated its remote-only clause.  It is disclosed and excluded.
- F243-R2 is disjoint and preregistered.  SHA-256 and exact threshold
  arithmetic self-tests ran before its inputs.
- The verifier factors only `N-1` and `N+1`, each below `2^28`; trial primes
  through 16,384 are sufficient.
- The exact probability numerators fit the preregistered 128-bit bounds.
  The `1/sqrt(ell)` comparison uses an exact four-limb 256-bit product.
- The raw report did not print Wilson intervals.  `NUMERICAL_ANALYSIS.md`
  supplies the frozen formula and a representative interval.  Exact counts
  were present in the TSV and define the data.
- The normalized box trace resultant removes the public factor `2D`.
  A small target dividing a fixed small `D` is already a trivial public
  support hit and is not treated as a torus alias.
- No independent reimplementation, hostile audit, blind reconstruction, or
  cross-family audit has run.

## Promotion status

Do not promote F243 from this packet alone.  The statement needs a fresh
hostile audit and a statement-only reconstruction.  The numerical report is
supporting guidance and is not part of any proof.
