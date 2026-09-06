# F243 preregistration — torus collision sources

## Purpose

Test public integer and quadratic-algebra sources for modular aliasing at the
shifted residual primes in F242.  The computation is for discovery and
counterexample search.  It is not proof.

## Frozen input set

Use the deterministic odd-prime list in the half-open interval
`[2^12,2^14)`.  Form distinct semiprimes from pairs selected by the fixed
SHA-256 seed

`F243-torus-collision-source-v1`.

Take the first 20,000 distinct ordered index pairs after sorting the hashes
of `seed || ":" || p || ":" || q`, with `p<q`.  Also enumerate all pairs of
odd primes below 512 as an edge-case set.  No input is selected after seeing
the measured statistics.

For each `N=pq` and each sign pair `(epsilon_p,epsilon_q)`, use

`m_p=p-epsilon_p`, `m_q=q-epsilon_q`, and
`d=gcd(m_p,m_q)`.

For each side, start with `s_i=m_i/d`.  Remove every primary whose rational
prime divides `N^2-1`.  Call the remaining part `s_i^ext`.  Record every
rational prime `ell` dividing either exterior part.

## Frozen sources and statistics

For every target `ell`, compute exact finite-support statistics where
possible.  Use Monte Carlo only for the stated discriminant law.

1. Uniform divisors of `N-1`, `N+1`, and `N^2-1`.  Record the generated
   subgroup size `h_ell`, the exact distinct-integer collision probability
   `kappa_ell`, support size, and exact-equality mass.
2. The factor-free gcd-divisor law `Z=gcd(X,N^2-1)` for uniform
   `X mod N^2-1`.  Compute its exact divisor probabilities from the known
   factorization available to the verifier.  Record exact `kappa_ell` and
   equality mass.  The algorithm under study does not receive that
   factorization.
3. Pell/Chebyshev powers in the public algebra
   `Z[w]/(w^2-(N^2-1))`, with `eta=N+w`.  For exponent windows
   `T in {8,16,32,64,128}`, compute the exact order of `eta mod ell`, the
   distinct collision probability of coefficient pairs, and the distinct
   trace-collision probability.  Exact equal integer coefficients and exact
   equal integer traces are excluded.
4. Hilbert--90 coefficient sources for the fixed public discriminants
   `D in {-1,2,3,5,N-1,N+1}`.  For boxes
   `B in {8,16,32,64}`, use all primitive signed pairs
   `(a,b)` with `0<=a,b<B`, not both zero, and construct the projective
   determinant and trace-resultant words.  Exclude an integer word when it
   is exactly zero.  Record exact modular zero probabilities and exact-zero
   masses.
5. Uniform discriminants `D in {1,...,N-1}` conditioned on
   `gcd(D,N)=1` and each public Jacobi sign.  Estimate distinct-integer
   collision probabilities modulo `ell` from 200,000 seeded independent
   pairs per aggregate bit-size bucket.  Use seed
   `F243-discriminant-monte-carlo-v1`.

## Frozen summaries

For every source, report quantiles and maxima of `ell*kappa_ell`, the count
of zero-collision targets, and the worst target for the hoped-for lower
bound.  For divisor sources, also report quantiles of `h_ell/ell`.  For
Pell powers, report quantiles of `ord_ell(eta)/ell`.

The useful-pattern threshold is `kappa_ell >= 1/sqrt(ell)` or
`h_ell <= sqrt(ell)`.  This threshold is only a search signal.  It is not a
QP claim.  A generic-scale obstruction signal is a family of targets with
`kappa_ell <= 4/ell`, or with zero distinct collision, for every tested
source.

## Interpretation rules

- Finite success does not imply an asymptotic lower bound.
- Finite failure does not imply an impossibility theorem.
- The proof section must derive every claimed local collision law without
  using these measurements.
- A source feature may use only public data.  Hidden factors and the
  verifier factorization may label targets and evaluate exact statistics,
  but may not define the source.
- The theorem and numerical report remain separate artifacts.
