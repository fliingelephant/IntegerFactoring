# Proof of the F251 fixed-past Pell bound

## 1. Squarefree reduction

Write the unique squarefree decomposition

\[
P=au^2,
\]

where (a,u\) are positive integers and (a\) is squarefree. If

\[
P(1+Dy^2)=R^2,
\]

then (u\mid R\). Write (R=uw\). The equation becomes

\[
w^2=a(1+Dy^2).
\]

Since (a\) is squarefree, (a\mid w\). Writing (w=av\) gives

\[
\boxed{av^2-Dy^2=1.}
\]

Conversely, every positive integral solution of this equation makes
(P(1+Dy^2)=(auv)^2\). Thus the exact-square rows are exactly the canonical
(y\)-coordinates occurring in this generalized Pell equation.

This use of the squarefree kernel is proof-only. The sampler does not have
to compute (a\).

## 2. Any two solutions have an integral unit quotient

Put (K=aD\). For a solution ((v,y)\) with (v>0\) and (y\ge0\), define

\[
\alpha_y=av+y\sqrt K.
\]

Its norm is

\[
\operatorname N(\alpha_y)
=a^2v^2-Ky^2
=a(av^2-Dy^2)
=a.
\]

The positive real value of (\alpha_y/\sqrt a\) is

\[
\beta(y)
=\sqrt a\,v+y\sqrt D
=\sqrt{1+Dy^2}+y\sqrt D.
\]

This is strictly increasing in (y\).

Take two solutions with (y_2>y_1\). Direct multiplication gives

\[
\frac{\alpha_{y_2}}{\alpha_{y_1}}
=\frac{\alpha_{y_2}\overline{\alpha_{y_1}}}{a}
=s+t\sqrt K,
\]

where

\[
s=av_1v_2-Dy_1y_2\in\mathbb Z,
\qquad
t=v_1y_2-v_2y_1\in\mathbb Z.
\]

This quotient has norm one. It is larger than one because (\beta(y)\) is
increasing. Its conjugate is its positive reciprocal. Hence

\[
s>1,
\qquad
t>0.
\]

Since (s,t\) are integers,

\[
s\ge2,
\qquad
t\ge1.
\]

If (K\) is an integer square, the equation

\[
s^2-Kt^2=1
\]

factors over the integers. Its only solution with positive conjugate and
norm one is (s=1,t=0\). This contradicts (y_2>y_1\). Therefore at most one
canonical (y\) occurs in this case.

If (K\) is not a square, every quotient between two increasing solutions
satisfies

\[
s+t\sqrt K
\ge2+\sqrt K
\ge2+\sqrt2
=\Lambda.
\]

The integrality of this quotient is the special feature that removes the
usual multiple-seed issue for generalized Pell equations. For a general
norm equation, division by the norm need not leave integral coefficients.
Here the first coefficient of every (\alpha_y\) is divisible by (a\), so
division by the common norm (a\) is integral.

## 3. Counting the chain

The claim is immediate when there is at most one solution. Otherwise list
all solutions in the range as

\[
0\le y_1<y_2<\cdots<y_m<Y.
\]

Apply the preceding gap bound to consecutive solutions. It gives

\[
\frac{\alpha_{y_m}}{\alpha_{y_1}}
=\prod_{i=1}^{m-1}
\frac{\alpha_{y_{i+1}}}{\alpha_{y_i}}
\ge\Lambda^{m-1}.
\]

On the other hand, (\beta(y_1)\ge1\), and

\[
\frac{\alpha_{y_m}}{\alpha_{y_1}}
=\frac{\beta(y_m)}{\beta(y_1)}
\le\beta(y_m)
<\sqrt{1+DY^2}+Y\sqrt D
\le1+2Y\sqrt D.
\]

It follows that

\[
m\le1+\left\lfloor
\frac{\log(1+2Y\sqrt D)}{\log(2+\sqrt2)}
\right\rfloor
=B(D,Y).
\]

The case in which (K\) is square already has (m\le1\), so the displayed
bound is uniform in (a\) and therefore in (P\). This proves the theorem.

## 4. Roots and probability laws

For an admitted row, (Xx_y\) is a supplied square root of (PA_y\) modulo
(N\). If (PA_y=R^2\) over the integers, then

\[
\zeta_y=R(Xx_y)^{-1}\pmod N
\]

is a square root of one. Changing (R\) to (-R\) changes (\zeta_y\) by a
global sign, so whether it is mixed is unchanged. The useful rows form a
subset of the at most (B(D,Y)\) exact-square rows.

If the fresh (y\)-law has maximum atom (\mu\), any set of at most
(B(D,Y)\) coordinates has probability at most (\mu B(D,Y)\). This proves
the conditional bound even when (P\) depends arbitrarily on the past,
provided it is fixed before the fresh coordinate is sampled.

For two independent rows, condition on the first row and set (P=A_z\).
The theorem leaves at most (B(D,N)\) second coordinates. Uniformity on a
coordinate set of size (|\mathcal Y|\) gives (B(D,N)/|\mathcal Y|\).
For a uniform point set with at most (c\) points above each coordinate,
there are at most (cB(D,N)\) successful second points out of (H\). This
gives (cB(D,N)/H\). Averaging over the first row preserves the bound.

Finally, there are only (\binom T2\) unordered pairs in a bank of (T\)
rows. The stated pair-bank estimate follows by a union bound. This argument
does not enumerate or control the (2^T\) products available to a
retrospective multirow P66 selector.
