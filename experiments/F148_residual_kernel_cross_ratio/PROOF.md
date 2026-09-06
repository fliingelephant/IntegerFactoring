# F148 proof — residual square classes and cross-ratio separation

## 1. One cycle

For an edge in a directed containment cycle,

\[
q_ea_e^2\equiv r_eT_e\pmod N.
\]

Multiplying around the cycle cancels the product of the unit centers because
the heads are the next tails. Thus

\[
\alpha_i^2\equiv T_i\pmod N,
\qquad
\alpha_i=\prod_ea_e,
\quad
T_i=\prod_eT_e.
\tag{1}
\]

The exact bridge product is a square times `T_i`. The same is true for the
actual matched canonical/lifted P128 columns because the change from a
bridge to that pair multiplies by the exact square of the canonical inverse
endpoint. Hence the parity boundary of the cycle vector is exactly the
square class of `T_i`.

## 2. Pairing equal residual square classes

Suppose

\[
T_i=d s_i^2,
\qquad
T_j=d s_j^2.
\tag{2}
\]

Then `T_i*T_j=(d*s_i*s_j)^2`. The sum of the two binary cycle vectors is
therefore in the exact square-class kernel. P131's indexed-cycle root formula
gives its normalized root

\[
\rho_{ij}
\equiv
{\alpha_i\alpha_j\over d s_i s_j}
\pmod N.
\tag{3}
\]

Every displayed denominator is a unit: all centers, residues, and residual
cofactors are units on the nonfactor branch.

From (1)--(2),

\[
\alpha_j^2\equiv d s_j^2\pmod N.
\]

Multiply the right side of

\[
{\alpha_i s_j\over\alpha_j s_i}
\]

by `alpha_j^2/(d*s_j^2)=1 mod N`. This proves

\[
\rho_{ij}
\equiv
{\alpha_i s_j\over\alpha_j s_i}
\pmod N.
\tag{4}
\]

Since `alpha_j*s_i` is a unit, clearing it does not change a gcd with `N`.
Equation (4) gives

\[
\gcd(\rho_{ij}-1,N)
=
\gcd(\alpha_i s_j-\alpha_j s_i,N)
\]

and the analogous plus formula.

## 3. Metric separation

Put

\[
X=\alpha_i s_j-\alpha_j s_i,
\qquad
Y=\alpha_i s_j+\alpha_j s_i.
\]

Equations (1)--(2) imply

\[
X Y
=(\alpha_i s_j)^2-(\alpha_j s_i)^2
\equiv0\pmod N.
\tag{5}
\]

If the slopes differ, `X` is nonzero. If `Y<N`, then

\[
0<|X|<Y<N.
\]

Neither `X` nor `Y` is divisible by `N`. If `gcd(X,N)=1`, (5) would imply
`N|Y`, a contradiction. Thus `1<gcd(X,N)<N`. The same argument with `X`
and `Y` exchanged proves `1<gcd(Y,N)<N`.

This proof uses the cross-products, not the much larger product
`alpha_i*alpha_j`.

## 4. Exact root-class obstruction

For one common core `d`, define

\[
z_i=\alpha_i s_i^{-1}\pmod N.
\]

Then `z_i^2=d mod N`. Equation (4) says

\[
\rho_{ij}=z_i z_j^{-1}.
\]

Therefore every pair root is global if and only if

\[
z_i\equiv\pm z_j\pmod N
\]

for every pair. Equivalently, all `z_i` lie in one class after quotienting by
the global sign. Under the strict metric bound, a global plus relation forces
the integer equality `alpha_i*s_j=alpha_j*s_i`, while a global minus relation
would force a positive integer sum to be divisible by `N`, which is
impossible. Hence a metric-safe bucket can fail only by exact equality of
all rational slopes.

## 5. Quasipolynomial corollary

If `T_i<=R`, its positive squarefree kernel is at most `R`, and there are at
most `R` possible kernels. More than `R` cycles force two equal kernels.
For this pair,

\[
s_i,s_j\le\sqrt R.
\]

If both anchor products are at most `H`, then

\[
\alpha_i s_j+\alpha_j s_i
\le2H\sqrt R<N.
\]

Slope deduplication makes the slopes unequal. Section 3 now factors `N`.

P66's gcd-free refinement supplies exact pairwise-coprime blocks and exponent
vectors for all `T_i`. Equality of their parity vectors detects the common
square class. If that parity vector is `epsilon`, set

\[
d=\prod_h h^{\epsilon_h},
\qquad
s_i=\prod_h h^{(e_{hi}-\epsilon_h)/2}.
\]

These are exact integers. The blocks need not be rational primes. Thus the
grouping and the `s_i` values require no integer factorization. Standard
sorting, exact multiplication, binary linear algebra, and gcd keep the cost
quasipolynomial for an explicit quasipolynomial-size compact source.

## 6. Certificate check

For `N=745`,

\[
119^2-6=19N,
\qquad
179^2-6=43N.
\]

Multiplication by the two centers gives the stated self-containment edges.
The canonical inverses satisfy

\[
342\cdot403\equiv1\pmod{745},
\qquad
552\cdot193\equiv1\pmod{745}.
\]

Direct multiplication gives the four values, their square product, and its
positive root in the statement. Finally,

\[
179-119=60,
\qquad
179+119=298,
\]

so their gcds with `745=5*149` are `5` and `149`.

The registered V3 search checks all remaining distinctness, nonsquare, and
endpoint-screen claims. V1 and V2 are preserved because they exposed two
important certificate degeneracies: exact-value duplication and an already
useful one-column canonical square.
