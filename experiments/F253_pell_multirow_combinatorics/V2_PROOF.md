# Proof of the F253 V2 multirow and odd-multiple theorems

## 1. A P214 bound for every square-class fibre

Every positive integer has a unique squarefree kernel. Thus every square
class \(v\) represented by a positive integer has a unique positive
squarefree representative \(a_v\). For another positive integer \(A\),

\[
[A]=v
\quad\Longleftrightarrow\quad
A=a_vu^2\ \hbox{for some integer }u
\quad\Longleftrightarrow\quad
a_vA=(a_vu)^2.
\]

Fix one class \(v\) and one discriminant \(D\). Apply P214 with the fixed
past product \(P=a_v\). It gives

\[
\#\{0\le y<Y_D:[1+Dy^2]=v\}\le B_D.
\]

The bank has no repeated coordinate within this \(D\), so the same bound
holds for its rows. Sum over the discriminant menu:

\[
\#\{i:v_i=v\}\le\sum_D B_D=B_\Sigma. \tag{1}
\]

No row has zero square class because exact-square singleton rows were
removed.

## 2. Rank and nullity

The column span has \(2^r\) elements, at most \(2^r-1\) of which are
nonzero. By (1), each nonzero class contains at most \(B_\Sigma\) rows.
Therefore

\[
m\le B_\Sigma(2^r-1).
\]

Rearranging gives

\[
r\ge
\left\lceil\log_2\left(1+{m\over B_\Sigma}\right)\right\rceil.
\]

Since the P66 parity-kernel dimension is \(d=m-r\), subtraction gives the
stated upper bound for \(d\).

P214 cannot give a positive lower bound for \(d\). In an abstract
square-class space, choose \(m\) linearly independent nonzero vectors. Their
maximum fibre size is one, their rank is \(m\), and their nullity is zero.

The rank inequality is exact at the level of fibre information. Take \(B\)
separately labelled copies of every nonzero vector in
\(\mathbb F_2^r\). The rank is \(r\), the maximum fibre size is \(B\), and

\[
m=B(2^r-1).
\]

This is an information-theoretic example. It does not claim that one Pell
bank realizes every vector.

## 3. Counting all square subsets

Let \(Z_k\) count all \(k\)-element subsets \(C\) with

\[
\sum_{i\in C}v_i=0.
\]

Mark one element \(i\in C\). Then

\[
v_i=\sum_{j\in C\setminus\{i\}}v_j. \tag{2}
\]

There are \({m\choose k-1}\) possible unmarked sets. Once one is fixed, its
right side in (2) is one fixed square class. By (1), at most
\(B_\Sigma\) rows in the entire bank can have that class. Ignoring the
extra restriction that the marked row is outside the unmarked set only
enlarges the count. Counting the \(k\) possible marks gives

\[
kZ_k\le B_\Sigma {m\choose k-1}.
\]

Divide by \(k{m\choose k}\) to obtain

\[
{Z_k\over {m\choose k}}
\le {B_\Sigma\over m-k+1}.
\]

For a fully uniform subset, the class-sum map

\[
\mathbb F_2^m\longrightarrow
\langle v_1,\ldots,v_m\rangle
\]

is a surjective linear map of rank \(r\). Its kernel has size \(2^{m-r}\).
The exact-square probability is \(2^{-r}\). The rank bound gives

\[
2^{-r}\le {1\over1+m/B_\Sigma}
={B_\Sigma\over m+B_\Sigma}.
\]

These are existence-frequency bounds only. They do not control the
normalized-root homomorphism on the P66 kernel.

## 4. Why ordering does not fix the retrospective quantifier

Expose the members of one dependent set in any order and take its final
member. Its class is the sum of the earlier members in that set. Conditioned
on one prescribed earlier subset, P214 permits at most \(B_\Sigma\) closing
rows. But the earlier bank can represent all \(2^{r_{\rm past}}\) classes in
its span.

The labelled-copy construction realizes this exponential class menu using
only the fibre constraint. A greedy basis or a minimal-circuit pivot chooses
a representation of the retrospectively selected class; it does not reduce
the number of possible target classes. No inverse-QP retrospective estimate
therefore follows from P214 alone.

## 5. Odd-multiple Pell polynomials

Let \(k>1\) be odd. Define

\[
\begin{aligned}
F_{k,D}(Y)
&=\sum_{h=0}^{(k-1)/2}
{k\choose 2h+1}D^hY^{2h+1}
(1+DY^2)^{(k-2h-1)/2},\\
G_{k,D}(Y)
&=\sum_{h=0}^{(k-1)/2}
{k\choose 2h}D^hY^{2h}
(1+DY^2)^{(k-2h-1)/2}.
\end{aligned} \tag{3}
\]

All exponents are nonnegative integers. These are polynomials in
\(\mathbb Z[Y]\).

Expand \((X+Y\sqrt D)^k\). In every odd-index binomial term, the exponent
of \(X\) is even. Replace that even power using \(X^2=1+DY^2\). These terms
give \(F_{k,D}(Y)\sqrt D\). In every even-index term, the exponent of \(X\)
is odd. Factor one \(X\), replace the remaining even power, and obtain
\(XG_{k,D}(Y)\). Hence

\[
(X+Y\sqrt D)^k
=XG_{k,D}(Y)+F_{k,D}(Y)\sqrt D. \tag{4}
\]

Both sides have norm one, so

\[
(1+DY^2)G_{k,D}(Y)^2-D F_{k,D}(Y)^2=1. \tag{5}
\]

For \(k=3\), direct expansion gives

\[
F_{3,D}(Y)=Y(3+4DY^2),
\qquad
G_{3,D}(Y)=1+4DY^2.
\]

## 6. Canonical specialization

Apply (4) to \(X=S_j\), \(Y=T_j\). Since
\(\epsilon^{kj}=(\epsilon^j)^k\), coefficient comparison gives

\[
T_{kj}=F_{k,D}(T_j),
\qquad
S_{kj}=S_jG_{k,D}(T_j). \tag{6}
\]

Reduce (6) modulo \(N\). Polynomial evaluation commutes with reduction:

\[
y_{kj}\equiv F_{k,D}(y_j)\pmod N,
\qquad
x_{kj}\equiv x_jG_{k,D}(y_j)\pmod N. \tag{7}
\]

All coefficients of \(F_{k,D}\) are nonnegative, so
\(F_{k,D}(y_j)\ge0\). If \(F_{k,D}(y_j)<N\), the first congruence in (7)
is equality of canonical representatives:

\[
y_{kj}=F_{k,D}(y_j). \tag{8}
\]

The norm identity (5) now gives

\[
A_{kj}
=1+D F_{k,D}(y_j)^2
=A_jG_{k,D}(y_j)^2. \tag{9}
\]

Equation (9) is an identity of integer values, whether or not a source bank
contains both indices. To claim a P66 dependency, V2 additionally assumes
that both the \(j\) and \(kj\) rows occur as retained columns and that
\(y_{kj}\ne y_j\). These hypotheses make

\[
c_{j,k}=e_j+e_{kj}
\]

a genuine nonzero two-column vector. Since \(D>0\) and canonical
coordinates are nonnegative, \(y_{kj}\ne y_j\) also gives
\(A_{kj}\ne A_j\); this is not a duplicate-row vector.

The positive exact root of the product is

\[
R=A_jG_{k,D}(y_j).
\]

Both rows survived cleanup, so their supplied roots are units modulo \(N\).
By (7),

\[
\begin{aligned}
X
&=x_jx_{kj}\\
&\equiv x_j^2G_{k,D}(y_j)\\
&\equiv A_jG_{k,D}(y_j)\\
&\equiv R\pmod N.
\end{aligned} \tag{10}
\]

Thus \(c_{j,k}\) is in the P66 parity kernel and its normalized root is
\(\rho(c_{j,k})=RX^{-1}=+1\).

The extra hypotheses also resolve modular orbit repetitions. If
\(y_{kj}=y_j\), the two exact row values coincide. A cleanup that keeps at
most one coordinate per \(D\) removes the later occurrence, after testing
the supplied-root signs. Such a repetition is not an element of the V2
pair set. If one of the indices is outside the bank, there is only one
column and likewise no pair vector.

Now fix one bank and define \(\mathcal P\) to be its actual vectors
\(c_{j,k}\) satisfying every V2 hypothesis. P66 makes

\[
\rho:\ker M\longrightarrow\{z\bmod N:z^2=1\}
\]

a homomorphism. Every generator in \(\mathcal P\) lies in \(\ker M\) and
maps to \(+1\). Therefore every binary sum of these generators also maps to
\(+1\):

\[
\langle\mathcal P\rangle\subseteq\ker\rho.
\]

This conclusion says nothing about a kernel vector outside that span.

## 7. The exact carry equation

For every odd \(k>1\) and \(j\ge1\), (7) permits a unique integer
\(c\ge0\) such that

\[
F_{k,D}(y_j)=y_{kj}+cN.
\]

Substitute this into (5):

\[
\begin{aligned}
A_jG_{k,D}(y_j)^2
&=1+D(y_{kj}+cN)^2\\
&=A_{kj}+DcN(2y_{kj}+cN).
\end{aligned}
\]

When \(c=0\), the integer square-class identity (9) holds. It becomes a
two-column global decoy only under the presence, retention, and distinctness
hypotheses of Theorem B. When \(c>0\), the discrepancy is a positive
multiple of \(N\). The modular root relation survives, but the exact integer
square-class identity need not.

Because \(\rho\) is trivial on \(\langle\mathcal P\rangle\), any useful
kernel vector must have nonzero image in the quotient
\(\ker M/\langle\mathcal P\rangle\). V2 does not bound that quotient or its
normalized-root image.

## 8. Finite certificate

For \(D=2\), \(k=3\), \(j=17\), and canonical \(y_j=6\),

\[
F_{3,2}(6)=6(3+8\cdot36)=1746,
\qquad
G_{3,2}(6)=1+8\cdot36=289.
\]

The frozen bank contains both indices \(17\) and \(51=3\cdot17\), retains
both rows, and has \(6\ne1746\). Their values are

\[
A_{17}=1+2\cdot6^2=73,
\]

\[
A_{51}=1+2\cdot1746^2
=6097033
=73\cdot289^2.
\]

Thus

\[
A_{17}A_{51}=(73\cdot289)^2=21097^2.
\]

The supplied residues satisfy

\[
1692\cdot3916\equiv3773\pmod{4331}
\]

and

\[
21097\equiv3773\pmod{4331}.
\]

Both supplied residues are units, and

\[
\gcd(21097-3773,4331)=4331,
\qquad
\gcd(21097+3773,4331)=1.
\]

This independently verifies the distinct two-column dependency and its
global root. The window-wide cleanup classification is finite computational
evidence authenticated and replayed by the V1 hostile audit.

