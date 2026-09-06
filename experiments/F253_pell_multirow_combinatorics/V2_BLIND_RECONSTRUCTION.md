# F253 V2 blind reconstruction

## Provenance

This reconstruction uses only `V2_STATEMENT.md`. Its authenticated SHA-256 is

```text
53c7f59bc3f2a2e1b2f38d77661abfe94465945f5ce8691516e5c5c76ec277ba
```

No other F253 artifact, history, or ledger was consulted.

## Setup

Let \(\mathcal D\) be a finite set of positive integers. For every
\(D\in\mathcal D\), the available coordinates satisfy

\[
0\le y<Y_D,
\qquad
A_{D,y}=1+Dy^2.
\]

The bank contains \(m\) rows. Coordinates do not repeat within a fixed
\(D\), and every row whose \(A_{D,y}\) is already an integer square has been
removed. In the positive rational square-class group

\[
\mathcal V=\mathbb Q_{>0}^{\!*}/\mathbb Q^{\!*2},
\]

write the class of row \(i\) as \(v_i=[A_i]\), and put

\[
r=\dim_{\mathbb F_2}\langle v_1,\ldots,v_m\rangle,
\qquad
d=m-r.
\]

Define

\[
B_D=
1+\left\lfloor
\frac{\log(1+2Y_D\sqrt D)}{\log(2+\sqrt2)}
\right\rfloor,
\qquad
B_\Sigma=\sum_{D\in\mathcal D}B_D.
\]

The singleton cleanup means that no retained row has the zero square class.

## 1. Square-class fibres

Fix \(D\) and one nonzero square class. Let \(q\) be its positive squarefree
integer representative. Every row in this fibre has

\[
1+Dy^2=q a^2
\]

for some positive integer \(a\). Associate to it the positive real number

\[
\alpha_y=a\sqrt q+y\sqrt D
=\sqrt{1+Dy^2}+y\sqrt D.
\]

If \(0<y_1<y_2\) are two members of the fibre, then

\[
\frac{\alpha_{y_2}}{\alpha_{y_1}}
=u+v\sqrt{qD},
\]

where

\[
u=q a_1a_2-Dy_1y_2,
\qquad
v=a_1y_2-a_2y_1>0,
\]

and

\[
u^2-qDv^2=1.
\]

The ratio is greater than one. If \(qD\) is a square, this equation has no
solution with \(v>0\), so the fibre has at most one member. Otherwise
\(u\ge2\), and hence

\[
\frac{\alpha_{y_2}}{\alpha_{y_1}}
=u+\sqrt{u^2-1}
\ge2+\sqrt3
>2+\sqrt2.
\]

For \(n\) fibre members in increasing order, consecutive ratios therefore
give

\[
(2+\sqrt2)^{n-1}
\le \alpha_{y_n}
\le 1+2Y_D\sqrt D.
\]

Thus \(n\le B_D\). Summing the fixed-\(D\) bounds shows that every nonzero
class occurs in the whole bank at most

\[
B_\Sigma
\]

times.

## 2. Rank and nullity

An \(r\)-dimensional binary vector space has \(2^r-1\) nonzero vectors. All
retained row classes are nonzero, and each such class has at most
\(B_\Sigma\) representatives. Therefore

\[
\boxed{m\le B_\Sigma(2^r-1)}.
\]

Inverting this inequality and using that \(r\) is an integer gives

\[
\boxed{
r\ge
\left\lceil\log_2\left(1+\frac m{B_\Sigma}\right)\right\rceil
}.
\]

Consequently

\[
\boxed{
d\le
m-\left\lceil\log_2\left(1+\frac m{B_\Sigma}\right)\right\rceil
}.
\]

The fibre cap alone gives no positive deterministic lower bound on \(d\).
For arbitrarily large \(m\), take \(m\) independent abstract square classes,
each with multiplicity one. They obey every fibre cap \(B_\Sigma\ge1\), but
have \(r=m\) and \(d=0\). This is a limitation of the class-fibre information;
it is not a claim that every abstract example is realized by the Pell bank.

## 3. Fixed-size and unrestricted square-subset bounds

Let \(Z_k\) be the number of \(k\)-row subsets whose exact integer product is
an integer square. This counts every dependency, not only minimal circuits.

Count pairs \((S,i)\), where \(S\) is such a \(k\)-subset and \(i\in S\).
Deleting \(i\) leaves a \((k-1)\)-subset \(T\), and the deleted class must be

\[
v_i=\sum_{t\in T}v_t.
\]

For each fixed \(T\), there are at most \(B_\Sigma\) possible completing
rows. If the target class is zero, there are none because singleton squares
were removed. Since every square \(k\)-subset is counted once for each of
its \(k\) rows,

\[
\boxed{kZ_k\le B_\Sigma {m\choose k-1}},
\qquad 1\le k\le m.
\]

After division by \({m\choose k}\), a uniformly random \(k\)-subset is an
exact-square subset with probability at most

\[
\boxed{\frac{B_\Sigma}{m-k+1}}.
\]

For an unrestricted uniformly random subset, let

\[
\phi:\mathbb F_2^m\longrightarrow\mathcal V,
\qquad
\phi(z)=\sum_i z_i v_i.
\]

Its image has dimension \(r\), so its kernel has \(2^{m-r}\) elements.
Therefore independent row selection with probability \(1/2\) produces an
exact square with exact probability

\[
\boxed{2^{-r}}.
\]

The rank bound then gives

\[
2^{-r}
\le
2^{-\lceil\log_2(1+m/B_\Sigma)\rceil}
\le
\boxed{\frac{B_\Sigma}{m+B_\Sigma}}.
\]

Every useful P66 subset must first be an exact-square subset, so all of these
upper bounds also apply to useful subsets. The bounds do not prove that a
dependency exists. They also do not prove that an existing dependency has a
non-global normalized root.

## 4. Sharpness and the fixed-past barrier

The rank inequality is sharp if only a class-fibre cap is known. Given
\(r\ge1\) and \(B\ge1\), take \(B\) labelled copies of every nonzero vector
of \(\mathbb F_2^r\). Then

\[
m=B(2^r-1),
\]

the maximum fibre size is exactly \(B\), and the row classes have rank
exactly \(r\). Taking \(B=B_\Sigma\) attains the rank bound.

An ordering does not remove the obstruction. If the final row of a dependent
set is exposed last, its class is the sum of one selected subset of the
earlier classes. Fixed-past sparsity controls any one fixed earlier product,
but the earlier span can contain \(2^r\) different products. The sharp
abstract construction realizes this exponential target menu. Circuit-pivot,
greedy-basis, and similar orderings therefore cannot turn the fixed-past
bound into an inverse-quasipolynomial retrospective bound.

## 5. Odd-multiple polynomial identity

Fix a positive nonsquare \(D\), and let

\[
\epsilon=S_1+T_1\sqrt D>1,
\qquad
S_1^2-DT_1^2=1,
\qquad
\epsilon^j=S_j+T_j\sqrt D.
\]

For an odd integer \(k>1\), define the integer polynomials

\[
G_{k,D}(Y)=
\sum_{s=0}^{(k-1)/2}
{k\choose 2s}
(1+DY^2)^{(k-2s-1)/2}D^sY^{2s}
\]

and

\[
F_{k,D}(Y)=
\sum_{s=0}^{(k-1)/2}
{k\choose 2s+1}
(1+DY^2)^{(k-2s-1)/2}D^sY^{2s+1}.
\]

Expanding the odd power and replacing every even power of \(X\) by a power
of \(1+DY^2\) gives, whenever \(X^2=1+DY^2\),

\[
(X+Y\sqrt D)^k
=XG_{k,D}(Y)+F_{k,D}(Y)\sqrt D.
\]

Taking norms gives the exact identity

\[
\boxed{
1+D F_{k,D}(Y)^2
=(1+DY^2)G_{k,D}(Y)^2
}.
\]

Oddness is what leaves one factor \(X\) in the rational coefficient and
only even powers of \(X\) elsewhere.

For \(k=3\), the polynomials reduce to

\[
\boxed{F_{3,D}(Y)=Y(3+4DY^2)},
\qquad
\boxed{G_{3,D}(Y)=1+4DY^2}.
\]

## 6. Distinct retained clean pairs

Let \(N\) be odd. Use least nonnegative residues to define the canonical
rows

\[
y_h=[T_h]_N,
\qquad
x_h=[S_h]_N,
\qquad
A_h=1+Dy_h^2.
\]

Fix \(j\ge1\) and odd \(k>1\). The clean two-column conclusion requires all
four conditions below.

1. Both the index-\(j\) row and the index-\(kj\) row occur in the bank.
2. Both rows survive cleanup. In particular, their supplied roots are units,
   and neither row is a removed singleton or duplicate.
3. Their retained coordinates are distinct: \(y_{kj}\ne y_j\).
4. There is no carry: \(F_{k,D}(y_j)<N\).

The identity \(\epsilon^{kj}=(\epsilon^j)^k\), reduced modulo \(N\), yields

\[
y_{kj}\equiv F_{k,D}(y_j)\pmod N,
\qquad
x_{kj}\equiv x_jG_{k,D}(y_j)\pmod N.
\]

The fourth condition and canonical reduction turn the first congruence into
the integer equality

\[
y_{kj}=F_{k,D}(y_j).
\]

The polynomial norm identity now gives

\[
\boxed{A_{kj}=A_jG_{k,D}(y_j)^2}.
\]

Thus the two distinct retained columns have the same exact integer square
class, and their pair vector lies in the P66 parity kernel:

\[
\boxed{
A_jA_{kj}
=\bigl(A_jG_{k,D}(y_j)\bigr)^2
}.
\]

Also \(x_j^2\equiv A_j\pmod N\), so

\[
\boxed{
x_jx_{kj}
\equiv A_jG_{k,D}(y_j)\pmod N
}.
\]

The supplied-root product equals the positive exact root modulo \(N\).
Therefore the normalized root is \(+1\), and this pair cannot factor \(N\).

To state the span conclusion precisely, let \(K\subseteq\mathbb F_2^m\) be
the P66 parity kernel. For \(z\in K\), let

\[
Q_z=\sqrt{\prod_i A_i^{z_i}}>0,
\qquad
X_z=\prod_i x_i^{z_i}\pmod N,
\qquad
\rho(z)=X_zQ_z^{-1}\pmod N.
\]

The retained unit conditions make the inverse well-defined. The usual
cancellation of rows selected twice shows that \(\rho\) is a homomorphism;
its values are square roots of one modulo \(N\).

Let \(\mathcal P\) contain exactly the vectors \(e_j+e_{kj}\) in this fixed
bank that satisfy all four conditions above. Every one has normalized root
\(+1\). Hence

\[
\boxed{\langle\mathcal P\rangle\subseteq\ker\rho}.
\]

This set includes only actual pairs of distinct retained columns. It excludes
a modular orbit repetition with \(y_{kj}=y_j\), an absent index, and any row
removed during cleanup. The assertion does not say that these pair vectors
generate all of \(K\).

## 7. Exact carry boundary

For every odd \(k>1\) and \(j\ge1\), canonical reduction gives a unique
integer \(c\ge0\) such that

\[
F_{k,D}(y_j)=y_{kj}+cN.
\]

Substitution into the polynomial identity gives

\[
\begin{aligned}
A_jG_{k,D}(y_j)^2-A_{kj}
&=D\left((y_{kj}+cN)^2-y_{kj}^2\right)\\
&=\boxed{DcN(2y_{kj}+cN)}.
\end{aligned}
\]

The cases separate exactly as follows.

- If \(c=0\), the exact square-class identity holds. It becomes a
  two-column global decoy only if both columns are present, retained, and
  distinct.
- If \(c>0\), the displayed difference is positive. The clean exact identity
  is broken, although the congruence modulo \(N\) remains. This does not rule
  out a different arithmetic relation.

Because \(\langle\mathcal P\rangle\subseteq\ker\rho\), the normalized-root
map factors through \(K/\langle\mathcal P\rangle\). Any useful normalized root
left after this quotient must come from carried specializations, other
arithmetic specializations not generated by the clean pair identities,
cross-family relations, or relations using rows outside the hypotheses. A
bound on this residual normalized-root image remains open.

## 8. Finite certificate

Take

\[
N=4331=61\cdot71,
\qquad
D=2,
\qquad
\epsilon=3+2\sqrt2.
\]

Since \(\operatorname{bitlength}(4331)=13\), the frozen search window
\(0\le j\le4\operatorname{bitlength}(N)\) is \(0\le j\le52\). It had no
cleanup factor, all supplied roots in the window were units, and it retained
these two distinct rows:

\[
\begin{array}{c|c|c|c}
j&y_j&x_j&A_j\\ \hline
17&6&1692&73\\
51&1746&3916&6097033
\end{array}
\]

Both indices are in the window, \(51=3\cdot17\), and \(6\ne1746\). For the
triple identity,

\[
F_{3,2}(6)=6(3+8\cdot36)=1746<4331,
\]

so \(c=0\), and

\[
G_{3,2}(6)=1+8\cdot36=289.
\]

The exact integer checks are

\[
A_{17}=1+2\cdot6^2=73,
\]

\[
A_{51}=1+2\cdot1746^2
=6097033
=73\cdot289^2,
\]

and

\[
A_{17}A_{51}
=(73\cdot289)^2
=21097^2.
\]

The modular supplied-root check is

\[
1692\cdot3916\equiv3773\pmod{4331},
\qquad
21097\equiv3773\pmod{4331}.
\]

Thus the supplied and positive exact roots agree. The two P66 gcds are

\[
\gcd(x_{17}x_{51}-21097,N)=4331,
\qquad
\gcd(x_{17}x_{51}+21097,N)=1.
\]

This is an exact finite certificate of a screen-free, clean, two-column P66
dependency with global normalized root. It establishes neither an
asymptotic frequency statement nor a factoring algorithm.
