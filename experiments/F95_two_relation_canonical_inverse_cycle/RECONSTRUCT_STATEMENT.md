# F95 proof-blind reconstruction statement

Reconstruct and check the claims below without reading any other F95 file.
You may write and run your own independent code. Record a strict PASS or
FAIL, a self-contained derivation, and any necessary scope correction.

## Setup

Let

\[
N=2773.
\]

For a unit \(g\) with \(1<g<N\), let \(w(g)\) be its least positive inverse
modulo \(N\), and define its canonical-inverse relation value

\[
P(g)=g\,w(g)=1+k(g)N.
\]

Consider

\[
(g_1,w_1,k_1)=(3,1849,2)
\]

and

\[
(g_2,w_2,k_2)=(842,2526,767).
\]

## Claims to reconstruct

### 1. Stable test modulus

\[
N=47\cdot59.
\]

Writing

\[
d=\gcd(47-1,59-1),\qquad
A=(47-1)/d,\qquad
B=(59-1)/d,
\]

one has

\[
d=2,\qquad A=23,\qquad B=29,\qquad
\gcd(AB,N-1)=1.
\]

Thus this modulus is in the stable two-large-order class of P98. This label
is certificate context only; the factorization is not used to select the
relations below.

### 2. Two canonical-inverse relations

All four endpoints lie strictly between one and \(N\), and

\[
\begin{aligned}
P_1
&=3\cdot1849
=5547
=1+2N
=3\cdot43^2,\\
P_2
&=842\cdot2526
=2{,}126{,}892
=1+767N
=3\cdot842^2.
\end{aligned}
\]

Therefore \(w_i\) is the least positive inverse of \(g_i\).

### 3. Public square-normalized relation columns

Using only a gcd, exact division, and exact integer square roots,

\[
\gcd(P_1,P_2)=3,\qquad
P_1/3=43^2,\qquad
P_2/3=842^2.
\]

The integers \(3,43,842\) are pairwise coprime. On this public basis, the
two exact exponent columns are

\[
u_1=(1,2,0)^T,\qquad
u_2=(1,0,2)^T.
\]

Modulo two, both reduce to the same nonzero column

\[
\bar u_1=\bar u_2=(1,0,0)^T.
\]

Against the empty relation matrix, either column alone is nonclosing: it
has rank one and its one-column kernel is zero. After the first is retained,
the second closes. The two-column matrix still has rank one and has kernel

\[
\langle(1,1)^T\rangle.
\]

Deleting the first column leaves the second nonclosing again.

### 4. The induced root factors

The kernel vector gives

\[
R=\sqrt{P_1P_2}=3\cdot43\cdot842=108{,}618,
\]

so \(R^2\equiv1\pmod N\). Furthermore,

\[
R\bmod N=471,
\]

and

\[
\gcd(R-1,N)=47,\qquad
\gcd(R+1,N)=59.
\]

Equivalently, \(43^2\equiv842^2\pmod N\), and

\[
\gcd(842-43,N)=47,\qquad
\gcd(842+43,N)=59.
\]

### 5. Exact interpretation

This is a literal two-relation canonical-inverse 2-saturation cycle on a
P98 stable test modulus. It is also exactly a congruence-of-squares
collision. It proves that retaining a first nonclosing relation can be
necessary for a later closing relation.

It does not prove that \(g_2=842\) can be selected in time polynomial in
\(\log N\). In this certificate, selecting the second relation is the same
missing task as finding a second square root of \(3^{-1}\). The claims give
no frequency law, all-input progress law, polynomial-time factoring
algorithm, or novelty claim relative to classical congruence-of-squares
factoring.

## Optional independent finite check

You may independently enumerate every \(g\) with \(2\le g\le2772\), skip
nonunits after their public gcd, pair each unit with its least positive
inverse, and deduplicate exact values \(P=gw\). If relations are sorted by
\((P,\min(g,w),\max(g,w))\), discard individual square \(P\)'s, and test
pairs \(i<j\) in nested-loop order, the claimed run statistics are:

- 2771 raw candidates;
- 2667 units and 104 nonunits;
- 634 unique canonical relation values;
- 631 nonsquare values;
- the displayed witness has relation indices 1 and 306;
- it is the first pair whose product is an exact square and whose induced
  root gives a proper factor;
- 934 eligible pairs are tested through and including it.

These finite counts are supplementary. The arithmetic certificate in
Claims 1–5 is the main reconstruction target.
