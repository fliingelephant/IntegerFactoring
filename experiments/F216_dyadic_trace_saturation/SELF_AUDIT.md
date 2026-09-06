# F216 self-audit

## Checks performed

1. The normalization uses `N/d`, not `N*d` as an integer. Modulo `8` these
   are equal, but the proof correctly uses the modular inverse of `d`.
2. The representative image proofs establish surjectivity, not only the
   necessary low-bit congruence.
3. The `d=5` statement starts at `t=5`; its smaller-modulus images differ.
4. The two `d=1` branches are disjoint modulo `16`.
5. The zero-valuation tail contributes one image per branch, not one source.
6. The even and odd geometric sums were checked independently against exact
   enumeration through `t=18`.
7. The asymptotic density is `1/48`, not `1/24`.
8. Multiplication by the normalizing unit preserves cardinality but does not
   preserve every displayed representative congruence. The statement only
   transfers the complete set as `aW_t(d)`.

## Scope checks

- This is stronger than a literal-list count only for the stated dyadic
  trace image. It is not a circuit lower bound.
- Constant image density does not prevent a compressed representation. In
  fact, the proof gives one with `O(t)` valuation strata for `d=1` and a
  constant number of progressions for the other classes.
- A compressed representation is not an interval selector. The theorem does
  not claim that implicit interval intersection is hard.
- The reciprocal parameter has been projected away. A method that retains
  it is not covered.
- The theorem applies to every odd `N`, but the factoring consequence only
  says that a literal list at quarter-bit scale is too large.

## Numerical audit

The preregistered remote run used one Python 3.12 process. All 168 rows
passed. These consisted of 40 training rows, 16 formula holdout rows, 96
square-class-normalization holdout rows, and 16 balanced-semiprime trace
holdout rows. The minimum observed density for `t>=8` was
`0.020843505859375`, attained in the `d=1` class near the predicted `1/48`.
The full remote JSON output has SHA-256
`ab021b50d02a92bdcaddcc091c8c95b981b0d7e2f09149ca03b61b1d30173ac0`.
Finite verification is not used as proof.

