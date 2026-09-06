# F165-D01 frozen design

## Source and order

- Corpus order is lexicographic in `(p,q)`.
- Prime testing uses deterministic trial division. The range is fixed.
- Base seeds use increasing `c` from `2` through `n+1`, inclusive.
- Exact records use first exact-value occurrence order.
- A duplicate is compared by its supplied modular root before deletion.
- Each feedback level scans all support-one subsets in basis order. It then
  scans all unordered support-two subsets `(i,j)` with `i<j` in lexicographic
  order.
- The section basis uses first-occurrence Gaussian elimination. The pivot row
  is the largest active row index.
- All candidates in one level use the basis frozen before that level starts.
  New records cannot change the current scan.
- The complete union decoder is rebuilt only after the level ends.

## Exact record semantics

Every retained record has exact positive value `A`, supplied root `alpha=1`,
and occurrence data. Base records have `A=c*w`. Feedback records have
`A=z*w`. In both cases `A=1 mod N`.

Factor-free gcd refinement expresses each record as

`A = s^2 * product(q_j for j in v)`.

The `q_j` are pairwise coprime nonsquare units. The actual decorated lift is
`(v,s^(-1) mod N)`. A support-two star-product divides the product of its two
lifts by every common `q_j` once.

The decoder runs Gaussian elimination on all retained parity columns. A
zero parity remainder gives a square root of one modulo `N`. A root other
than `+1` or `-1` is useful and gives a proper gcd.

## Evidence separation

The function that builds the corpus knows `p,q`. The public analysis function
accepts only `N`. It uses no factorization of `N` and no factor-assisted
candidate index. Disclosed factors are used only after public analysis to
classify a returned proper divisor.

Each reported positive certificate is replayed by a verifier whose inputs
contain `N` and public certificate data only. A direct certificate verifies
the exact relation decompositions, actual star-product, canonical inverse,
and proper gcd. A root certificate verifies an exact square product and its
non-global normalized root.

## Strict progress records

At each level, record:

- attempted subsets;
- strict new exact values;
- duplicate exact values;
- both-sign direct-screen counts;
- factor-free rows, columns, rank, nullity, and normalized-root status;
- old blocks preserved or split after the union rebuild;
- hashes of candidates, exact values, blocks, and selected columns.

## Resource estimate

For one instance, the base rank is at most 27. Level one therefore attempts
at most 378 subsets. Its union rank is at most 405. Level two therefore
attempts at most 82,215 subsets. The run processes instances in sequence.
The largest live transcript is below 83,000 records of less than 60 bits,
plus product trees and parity incidence data. The estimated peak is below
2 GB. No instance is processed in parallel. The authoritative hard timeout
is 600 seconds.

## Fixed-depth cost statement to test separately

If a base explicit source has quasipolynomial size and each layer enumerates
polylogarithmic-support subsets of the current basis, every fixed number `H`
of recursive layers still has quasipolynomial explicit size. The exponent in
the quasipolynomial bound can depend on fixed `H`. This argument does not
give a uniform quasipolynomial bound when `H` grows with `n`.
