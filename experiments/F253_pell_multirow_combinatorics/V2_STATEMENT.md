# F253 V2: fixed-past Pell sparsity and a retrospective P66 bank

## Status and setup

This V2 statement replaces the frozen V1 statement. It repairs the
two-column scope of the odd-multiple theorem. The polynomial identity needs
only odd \(k\), but a P66 pair requires two distinct retained columns.

Let \(\mathcal D\) be a finite menu of positive integers. For each
\(D\in\mathcal D\), let

\[
0\le y<Y_D,\qquad A_{D,y}=1+Dy^2.
\]

Take a bank of \(m\) such rows. Assume:

1. within each fixed \(D\), no coordinate \(y\) is repeated;
2. exact-square singleton rows have been removed.

Write

\[
\mathcal V=\mathbb Q_{>0}^{\!*}/\mathbb Q^{\!*2}
\]

for the positive rational square-class group, viewed as a vector space over
\(\mathbb F_2\). Let \(v_i=[A_i]\), let

\[
r=\dim_{\mathbb F_2}\langle v_1,\ldots,v_m\rangle,
\qquad d=m-r,
\]

and define

\[
B_D=
1+\left\lfloor
{\log(1+2Y_D\sqrt D)\over\log(2+\sqrt2)}
\right\rfloor,
\qquad
B_\Sigma=\sum_{D\in\mathcal D}B_D.
\]

## Theorem A: class fibres, rank, nullity, and square subsets

Every nonzero square class occurs in the bank at most \(B_\Sigma\) times.
Consequently

\[
\boxed{m\le B_\Sigma(2^r-1)}
\]

and

\[
\boxed{
r\ge
\left\lceil\log_2\left(1+{m\over B_\Sigma}\right)\right\rceil,
\qquad
d\le
m-\left\lceil\log_2\left(1+{m\over B_\Sigma}\right)\right\rceil.}
\]

There is no positive deterministic lower bound on \(d\) from P214 alone.
Arbitrarily many independent abstract square classes satisfy the same fibre
cap and have \(d=0\).

Let \(Z_k\) be the number of \(k\)-element row subsets whose exact product is
an integer square. This includes circuits and nonminimal dependencies. For
\(1\le k\le m\),

\[
\boxed{kZ_k\le B_\Sigma {m\choose k-1}.}
\]

Thus a uniform \(k\)-element subset is an exact-square subset with probability
at most

\[
\boxed{{B_\Sigma\over m-k+1}.}
\]

A uniform subset of all \(m\) rows, with each row selected independently with
probability \(1/2\), is an exact-square subset with exact probability
\(2^{-r}\), and therefore with probability at most

\[
\boxed{{B_\Sigma\over m+B_\Sigma}.}
\]

These bounds also apply to useful P66 subsets, because utility first requires
an exact-square product. They do not imply that a dependency exists or that
an existing dependency has a non-global normalized root.

## Sharpness and the retrospective barrier

The rank inequality is best possible from a class-fibre cap alone. For any
\(r\ge1\) and \(B\ge1\), take \(B\) labelled copies of every nonzero vector
of \(\mathbb F_2^r\). Then

\[
m=B(2^r-1),
\]

the maximum fibre size is \(B\), and the rank is \(r\).

Ordering the rows does not remove the loss. If the last row of a dependent
set is exposed last, its class equals one product selected from the previous
rows. P214 bounds closure against each one fixed previous product, but the
previous span can contain \(2^r\) products. The abstract sharp example
attains this exponential menu. A circuit-pivot or greedy-basis ordering
therefore does not convert fixed-past sparsity into an inverse-QP
retrospective bound.

## Theorem B: distinct clean odd-multiple columns are global decoys

Fix a positive nonsquare \(D\), and let

\[
\epsilon=S_1+T_1\sqrt D>1,\qquad S_1^2-DT_1^2=1.
\]

Write

\[
\epsilon^j=S_j+T_j\sqrt D.
\]

For every odd integer \(k>1\), there are explicit integer polynomials
\(F_{k,D},G_{k,D}\) such that

\[
(X+Y\sqrt D)^k
=XG_{k,D}(Y)+F_{k,D}(Y)\sqrt D
\]

whenever \(X^2=1+DY^2\), and

\[
\boxed{1+D F_{k,D}(Y)^2=(1+DY^2)G_{k,D}(Y)^2.}
\]

For an odd modulus \(N\), define canonical Pell rows

\[
y_h=[T_h]_N,\qquad x_h=[S_h]_N,\qquad A_h=1+Dy_h^2.
\]

Fix \(j\ge1\). Suppose:

1. the bank contains both index-\(j\) and index-\(kj\) rows;
2. both rows survive the bank's cleanup, so in particular their supplied
   roots are units and neither is a removed singleton or duplicate;
3. \(y_{kj}\ne y_j\);
4. \(F_{k,D}(y_j)<N\).

Then

\[
y_{kj}=F_{k,D}(y_j),
\qquad
A_{kj}=A_jG_{k,D}(y_j)^2.
\]

The two distinct retained columns have the same exact integer square class,
and their two-column vector is in the P66 parity kernel:

\[
A_jA_{kj}=
\bigl(A_jG_{k,D}(y_j)\bigr)^2.
\]

Their supplied-root product satisfies

\[
x_jx_{kj}
\equiv A_jG_{k,D}(y_j)\pmod N.
\]

The normalized root is \(+1\). This two-column dependency cannot factor
\(N\).

In one fixed bank, let \(\mathcal P\) be the set of two-column vectors
\(e_j+e_{kj}\) satisfying all four hypotheses. Every vector in
\(\mathcal P\) lies in the P66 parity kernel and maps to \(+1\) under the
normalized-root homomorphism. Therefore

\[
\boxed{\langle\mathcal P\rangle\subseteq\ker\rho.}
\]

This span claim is only about the actual distinct retained pair vectors. It
does not include a modular orbit repetition with \(y_{kj}=y_j\), an absent
index, or a row removed by cleanup. It does not claim that these pairs
generate the full parity kernel.

For \(k=3\),

\[
F_{3,D}(Y)=Y(3+4DY^2),
\qquad
G_{3,D}(Y)=1+4DY^2.
\]

## Exact carried boundary

For any odd \(k>1\) and any \(j\ge1\), canonical reduction gives a unique
\(c\ge0\) such that

\[
F_{k,D}(y_j)=y_{kj}+cN.
\]

The polynomial identity becomes

\[
\boxed{
A_jG_{k,D}(y_j)^2-A_{kj}
=DcN(2y_{kj}+cN).}
\]

When \(c=0\), the exact square-class identity holds. It yields a
two-column global decoy only when both columns are present, retained, and
distinct as in Theorem B. When \(c>0\), the clean exact identity is broken
even though its congruence modulo \(N\) remains.

After quotienting the P66 parity kernel by the span
\(\langle\mathcal P\rangle\), a useful normalized root can therefore remain
only in carried specializations, other arithmetic specializations not
generated by these clean pair identities, cross-family relations, or
relations involving rows outside the hypotheses. Bounding that residual
normalized-root image is still open.

## Finite certificate

A frozen local search found a clean odd-multiple dependency inside the
fundamental \(D=2\) orbit for

\[
N=4331=61\cdot71,\qquad \epsilon=3+2\sqrt2.
\]

The frozen window was \(0\le j\le4\,\operatorname{bitlength}(N)=52\).
The selected modulus had no cleanup factor in this window, and all its
supplied roots were units. It retained the two distinct rows:

\[
\begin{array}{c|c|c|c}
j&y_j&x_j&A_j\\ \hline
17&6&1692&73\\
51&1746&3916&6097033
\end{array}
\]

Here \(51=3\cdot17\), the two indices occur in the window, the two
coordinates are distinct, and

\[
1746=F_{3,2}(6),\qquad
289=G_{3,2}(6).
\]

Thus

\[
6097033=73\cdot289^2,
\qquad
73\cdot6097033=21097^2.
\]

The supplied-root product and positive exact root agree:

\[
1692\cdot3916\equiv3773\pmod{4331},
\qquad
21097\equiv3773\pmod{4331}.
\]

The two gcds are \(4331\) and \(1\). This is an exact finite certificate of
a screen-free two-column P66 dependency with global root. It is not an
asymptotic frequency statement and not a factoring algorithm.

