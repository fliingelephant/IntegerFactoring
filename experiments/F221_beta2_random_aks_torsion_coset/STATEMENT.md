# F221 candidate — random affine AKS evaluations hit a common-torsion coset

## Status and scope

This is a frozen, self-audited, proof-only candidate.  It gives an exact
local root law and an exponential infinite-family obstruction for one
natural Las Vegas integer projection.  It is not a factoring algorithm or a
lower bound against arbitrary randomized coefficient algorithms.

The closest prior result is P165.  P165 proves rare global return for a
uniform unit under the factored exponent `N-1`.  F221 instead studies one
directly computable scalar value of the succinct AKS/binomial error.  Its
material new point is that, after arbitrary normalization of the evaluation
point, randomizing the affine scale searches an exact coset of the same
common predecessor torsion.

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes, and put

\[
d=\gcd(p-1,q-1).
\]

For a unit `a mod N`, define the standard scalar AKS error

\[
H_a(x)=(x+a)^N-x^N-a\pmod N.
\tag{1}
\]

## Theorem A — exact conditional torsion-coset law

Fix any unit `c mod N`.  Draw `a` uniformly from
`(Z/NZ)^times`, put

\[
x=ac\pmod N,
\]

and compute `H_a(x)`.

Write `c_p,c_q` for the hidden reductions of `c` and define

\[
D_{q,p}(z)=(z+1)^q-z^q\in\mathbb F_p,
\]

\[
D_{p,q}(z)=(z+1)^p-z^p\in\mathbb F_q.
\]

Set

\[
\epsilon_p(c)=
\begin{cases}
d/(p-1),&D_{q,p}(c_p)\ne0\text{ and }
D_{q,p}(c_p)^{-1}\in(\mathbb F_p^\times)^{q-1},\\
0,&\text{otherwise},
\end{cases}
\tag{2}
\]

and define `epsilon_q(c)` by interchanging `p,q`.
Then the two local zero events are conditionally independent and

\[
\boxed{
\Pr\bigl(1<\gcd(H_a(ac),N)<N\mid c\bigr)
=\epsilon_p(c)+\epsilon_q(c)-2\epsilon_p(c)\epsilon_q(c).}
\tag{3}
\]

In particular,

\[
\boxed{
\Pr\bigl(1<\gcd(H_a(ac),N)<N\mid c\bigr)
\le {d\over p-1}+{d\over q-1}.}
\tag{4}
\]

The local solution set in `a`, when nonempty, is not merely bounded by
`d`: it is exactly one coset of

\[
\ker\bigl(z\mapsto z^{q-1}:\mathbb F_p^\times\to
\mathbb F_p^\times\bigr),
\]

which has size `d`; the analogous statement holds modulo `q`.

The choice of `c` may depend arbitrarily on the complete preceding
transcript.  If each trial then uses a fresh conditionally uniform scale
`a`, (4) remains a conditional bound.  Therefore, if `tau` is the first
trial whose individual scalar gcd is proper and

\[
\varepsilon={d\over p-1}+{d\over q-1},
\]

then

\[
\Pr(\tau\le m)\le m\varepsilon,
\qquad
\mathbb E\tau\ge\varepsilon^{-1}.
\tag{5}
\]

The second inequality includes the case of infinite expectation.

## Theorem B — exact law for two independent uniform units

Drawing `(a,x)` independently and uniformly from the two-copy unit group is
equivalent to drawing independent uniform `(a,c)` and putting `x=ac`.
Define

\[
I_p=\#\{z\in\mathbb F_p^\times:
D_{q,p}(z)\ne0,\ 
D_{q,p}(z)^{-1}\in(\mathbb F_p^\times)^{q-1}\},
\]

and define `I_q` symmetrically.  Then

\[
\alpha_p={dI_p\over(p-1)^2},
\qquad
\alpha_q={dI_q\over(q-1)^2}
\tag{6}
\]

are the exact local-zero probabilities, and the exact useful-gcd
probability is

\[
\boxed{\alpha_p+\alpha_q-2\alpha_p\alpha_q.}
\tag{7}
\]

Thus the upper bound (4) is valid for the independent uniform-pair source
without any distributional heuristic.

## Theorem C — an infinite exponential obstruction

On P165's infinite family of balanced bounded-gap prime pairs, there is an
absolute constant `C` such that

\[
q-p\le C.
\]

Since

\[
d\mid q-p,
\]

one trial has useful-gcd probability at most

\[
{C\over p-1}+{C\over q-1}=2^{-n/2+O_C(1)}.
\tag{8}
\]

Consequently, even an adaptive numerical-QP bank of normalized points with
fresh uniform scales has total direct-gcd success probability
`2^{-Omega(n)}` on this family, and repeated trials have exponential
expected count.

This infinite family is imported exactly from P165.  F221 does not assert
that it lies in the `N = 3 mod 4` subbranch.

## Exact remaining scope

The proof uses the integer-specific Frobenius collapse `N=pq`; it is not a
generic ring-operation argument.  It closes only the following source:

1. select any normalized unit point `c`, possibly adaptively;
2. refresh a uniform multiplicative scale `a`;
3. evaluate the one scalar `H_a(ac)`; and
4. use its individual gcd with `N`.

It does not cover fixed `a` with random `x`, biased or nonuniform scales,
joint processing of typical nonzero values, coefficient vectors, quotient-
ring ranks, randomized carry bits, a factored global annihilator feeding the
F220 primary certificate, or another integer observable.  In particular,
the fixed-shift polynomial

\[
H_1(x)=(x+1)^N-x^N-1
\]

remains open.
