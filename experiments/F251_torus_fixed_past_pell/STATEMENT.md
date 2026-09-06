# F251: a fixed-past Pell bound for torus rows

## Setup

Let

\[
N=pq
\]

for distinct odd primes, and let (D,Y\) be positive integers. For
(0\le y<Y\), put

\[
A_y=1+Dy^2.
\]

An **admitted row** also has a supplied unit (x_y\bmod N\) such that

\[
x_y^2\equiv A_y\pmod N.
\]

Fix a positive integer (P\) before (y\) is chosen. Assume that (P\) is a
unit modulo (N\), and that a supplied unit (X\bmod N\) satisfies

\[
X^2\equiv P\pmod N.
\]

If (PA_y=R^2\) as integers, define the normalized root

\[
\zeta_y\equiv R(Xx_y)^{-1}\pmod N.
\]

Then (\zeta_y^2\equiv1\pmod N\). Call the square **useful** when
(\zeta_y\not\equiv\pm1\pmod N\). In that case one of
(\gcd(\zeta_y-1,N)\) and (\gcd(\zeta_y+1,N)\) is a proper factor of
(N\).

Define

\[
\Lambda=2+\sqrt2,
\qquad
B(D,Y)=1+\left\lfloor
\frac{\log(1+2Y\sqrt D)}{\log\Lambda}
\right\rfloor.
\]

## Theorem

For every fixed (P\),

\[
\#\{0\le y<Y:PA_y\text{ is an exact integer square}\}
\le B(D,Y).
\]

The same bound therefore holds for useful exact squares and for any subset
of admitted rows.

The bound is independent of the size and squarefree kernel of (P\). In
particular,

\[
B(D,Y)=O(\log Y+\log D).
\]

For the canonical torus range (Y=N\), this is (O(n)\) when
(n=\lceil\log_2N\rceil\) and (1\le D<N\). It remains polynomial in (n\)
when (D\) has polynomially many bits.

## Conditional sampling consequences

Let a fresh canonical coordinate (y\) have maximum point mass (\mu\),
conditional on the full past. If (P\) and its supplied root are fixed by
that past, then

\[
\Pr[PA_y\text{ is a useful exact square}\mid\text{past}]
\le \mu B(D,Y).
\]

Thus a uniform fresh (y\in\{0,\ldots,Y-1\}\) has conditional probability
at most (B(D,Y)/Y\).

Let (\mathcal Y\subseteq\{0,\ldots,N-1\}\) be a set of admitted canonical
coordinates. If (y,z\) are independent and uniform on (\mathcal Y\), then

\[
\Pr[A_yA_z\text{ is an exact square}]
\le \frac{B(D,N)}{|\mathcal Y|}.
\]

The same bound holds for a useful normalized root relative to (x_yx_z\).
More generally, if a uniform point set has (H\) points and every canonical
(y\)-fibre has at most (c\) points, then two independent uniform points
satisfy

\[
\Pr[A_yA_z\text{ is an exact square}]
\le \frac{cB(D,N)}H.
\]

For the clean raw norm-one torus, (c=4\). For a clean powered image whose
canonical fibres have size at most two, (c=2\).

For (T\) independent rows, a union bound controls every two-row product by

\[
\binom T2\frac{cB(D,N)}H.
\]

Consequently this probability is (2^{-\Omega(n)}\) when
(T=2^{(\log n)^{O(1)}}\), (B(D,N)=n^{O(1)}\), and (H=2^{\Omega(n)}\).

## Exact scope

The theorem controls:

1. one fresh torus row against one product fixed before that row;
2. every pair among an independent bank, by a quadratic-size union bound;
3. any prescribed sequence of fixed-past closures.

It does not control a P66 procedure that sees a fresh row and then chooses
one of exponentially many past subset products. It also does not control a
general product of three or more rows selected retrospectively.
