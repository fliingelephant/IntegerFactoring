# Source context for continued-fraction gap mass

**Family:** route:F31

Scope: focused primary-source check for `CONTINUED_FRACTIONS.md`, performed
after its derivation. This is not a novelty review. No external theorem is
imported into its proof beyond the separately promoted P250 mean bound.

## Closest classical ingredients

1. Tony van Ravenstein, [*The Three Gap Theorem (Steinhaus
   Conjecture)*](https://doi.org/10.1017/S1446788700031062), J. Austral.
   Math. Soc. A 45 (1988), 360--370. Section 2 and Theorem 2.2 give the
   neighboring-point recurrence for a rotation orbit. The discussion on
   pp. 367--368 explicitly says that the first point replacing either neighbor
   of zero is the sum of their indices; Sections 3--4 and Theorem 4.1 identify
   those indices with convergent or intermediate-convergent denominators and
   describe repeated splitting of a large gap according to continued-fraction
   digits. This is a close published precedent for the updates
   `(u,v)->(u+v,v)` or `(u,u+v)` paired with subtracting one gap length. I did
   not find the exact two-channel digit-sum conservation formula stated there.

2. Andrew C. Yao and Donald E. Knuth, [*Analysis of the Subtractive Algorithm
   for Greatest Common Divisors*](https://doi.org/10.1073/pnas.72.12.4720),
   PNAS 72 (1975), 4720--4722; accessible author technical report
   STAN-CS-75-510, Section 1. They state that the number of individual
   subtraction steps for `gcd(m,n)` is precisely the sum of the regular
   continued-fraction partial quotients, up to their displayed endpoint
   convention, and prove an average asymptotic. This directly supports the
   classical subtraction-count ingredient behind
   `S(x,x+y)=E(x,y)+2`; the `+2` normalization used in the root note was not
   found as that exact displayed identity in the paper.

3. Christoph Aistleitner, Bence Borda, and Manuel Hauke,
   [*On the distribution of partial quotients of reduced fractions with fixed
   denominator*](https://arxiv.org/abs/2210.14095), arXiv:2210.14095v2.
   The locally cached Introduction, equation (1), records
   `phi(N)^(-1) sum_(a in U_N) S(a/N) ~ (6/pi^2)(log N)^2`, crediting Panov
   and Liehl. Theorem 1 gives a fixed-denominator concentration theorem whose
   typical scale is `(12/pi^2) log N log log N`. These are stronger
   distributional background results. The expected-menu argument in
   `CONTINUED_FRACTIONS.md` instead uses P250's explicit nonasymptotic bound
   on the Jacobi-positive subset, so it does not depend on the asymptotic or
   on the theorem's stated tail range.

## Other checked three-gap sources

The abstracts and accessible statements of Marklof--Strömbergsson,
[*The three gap theorem and the space of
lattices*](https://arxiv.org/abs/1612.04906), and Taha,
[*The Three Gap Theorem, Interval Exchange Transformations, and Zippered
Rectangles*](https://arxiv.org/abs/1708.04380), confirm the classical
at-most-three-gap theorem and give lattice or interval-exchange proofs.
They do not present the specific simultaneous subtractive-Euclidean mass
identity used here. No full-text download was needed for this distinction.

## Limits of this check

I did not verify the original Panov or Liehl proofs, nor perform a citation
closure over the 1950s three-gap literature. I found no checked source stating

    S(u,u+v)+S(alpha,alpha+beta)=S(a,N)+2

for every finite orbit prefix, or combining that identity with arbitrary
interval discrepancy and a marginal fixed-denominator mean to obtain the
expected-cost direct-menu consequence. Absence from this focused check is not
evidence of novelty. The exact root derivation, its finite verification, and
the scope of its expected-cost corollary must be assessed independently.
