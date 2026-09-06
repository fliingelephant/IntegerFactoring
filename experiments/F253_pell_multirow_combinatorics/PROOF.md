# Proof of the F253 multirow bounds and odd-multiple decoy theorem

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

The span of the columns has \(2^r\) elements. At most \(2^r-1\) of them are
nonzero. By (1), each nonzero class contains at most \(B_\Sigma\) rows.
Therefore

\[
m\le B_\Sigma(2^r-1).
\]

Rearranging gives

\[
2^r\ge1+{m\over B_\Sigma},
\qquad
r\ge
\left\lceil\log_2\left(1+{m\over B_\Sigma}\right)\right\rceil.
\]

Since the P66 parity-kernel dimension is \(d=m-r\), subtraction gives the
stated upper bound for \(d\).

P214 cannot give a positive lower bound for \(d\). In an abstract
square-class space, choose \(m\) linearly independent nonzero vectors. Their
maximum fibre size is one, their rank is \(m\), and their nullity is zero.

The rank inequality itself is exact at the level of fibre information.
Take \(B\) separately labelled copies of every nonzero vector in
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

There are \({m\choose k-1}\) possible unmarked sets
\(S=C\setminus\{i\}\). Once \(S\) is fixed, its right side in (2) is one
fixed square class. By (1), at most \(B_\Sigma\) rows in the entire bank can
have that class. Ignoring the extra restriction \(i\notin S\) only enlarges
the count. Counting the \(k\) possible marks on every square subset gives

\[
kZ_k\le B_\Sigma {m\choose k-1}. \tag{3}
\]

Divide (3) by \(k{m\choose k}\) and use

\[
{{m\choose k-1}\over {m\choose k}}
={k\over m-k+1}
\]

to obtain

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
The exact square probability is therefore \(2^{-r}\). The rank bound gives

\[
2^{-r}\le {1\over1+m/B_\Sigma}
={B_\Sigma\over m+B_\Sigma}.
\]

These are existence-frequency bounds only. The P66 decoder examines a
kernel basis, and its normalized-root homomorphism can be trivial on the
entire kernel.

## 4. Why an ordering argument pays for the full past span

Expose the members of one dependent set in any order and take its final
member \(i\). Its class is the sum of the earlier members in that set.
Conditioned on a prescribed earlier subset, P214 permits at most
\(B_\Sigma\) closing rows. But the earlier bank can represent every one of
the \(2^{r_{\rm past}}\) classes in its span.

The labelled-copy construction above realizes this exponential class menu
using only the fibre constraint. A greedy basis puts \(r\) independent
columns first; all later columns lie in their span. A minimal-circuit pivot
only chooses one representation of the same retrospectively selected class.
Neither operation reduces the number of possible past targets. Hence no
inverse-QP retrospective estimate follows from P214 without an additional
property of the source.

## 5. Odd-multiple Pell polynomials

Let \(k\) be odd. Define

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
\end{aligned} \tag{4}
\]

All exponents in (4) are nonnegative integers, so these are polynomials in
\(\mathbb Z[Y]\).

Expand \((X+Y\sqrt D)^k\). In every odd-index binomial term, the exponent
of \(X\) is even, so replace its even power using
\(X^2=1+DY^2\). These terms give \(F_{k,D}(Y)\sqrt D\). In every
even-index term, the exponent of \(X\) is odd. Factor one \(X\) and replace
the remaining even power. These terms give \(XG_{k,D}(Y)\). Hence

\[
(X+Y\sqrt D)^k
=XG_{k,D}(Y)+F_{k,D}(Y)\sqrt D. \tag{5}
\]

Both sides of (5) have norm one. Therefore

\[
(1+DY^2)G_{k,D}(Y)^2-D F_{k,D}(Y)^2=1,
\]

which is the claimed polynomial identity.

For \(k=3\), direct expansion gives

\[
F_{3,D}(Y)=Y(3+4DY^2),
\qquad
G_{3,D}(Y)=1+4DY^2.
\]

## 6. Canonical specialization and the global root

Apply (5) to

\[
X=S_j,\qquad Y=T_j.
\]

Since \(\epsilon^{kj}=(\epsilon^j)^k\), coefficient comparison gives the
exact identities

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

All coefficients of \(F_{k,D}\) are nonnegative. Thus
\(F_{k,D}(y_j)\ge0\). If it is also smaller than \(N\), the first congruence
in (7) is equality between canonical representatives:

\[
y_{kj}=F_{k,D}(y_j).
\]

The norm identity now gives the exact integer relation

\[
A_{kj}
=1+D F_{k,D}(y_j)^2
=A_jG_{k,D}(y_j)^2. \tag{8}
\]

Because \(G_{k,D}(y_j)>0\), the positive exact root of the product of the
two rows is

\[
R=A_jG_{k,D}(y_j).
\]

The supplied modular root is, by (7),

\[
X=x_jx_{kj}
\equiv x_j^2G_{k,D}(y_j)
\equiv A_jG_{k,D}(y_j)
\equiv R\pmod N. \tag{9}
\]

If the supplied roots are units, (9) says that the normalized root
\(RX^{-1}\) is \(+1\). If a supplied root is not a unit, its gcd with
\(N\) has already left this branch.

The P66 normalized-root map is a homomorphism on the parity kernel. Every
clean odd-multiple pair lies in its kernel and maps to \(+1\). Therefore
the span of all such pair vectors also maps to \(+1\).

## 7. The exact carry equation

The first congruence in (7) permits a unique integer \(c\ge0\) such that

\[
F_{k,D}(y_j)=y_{kj}+cN.
\]

Substitute this expression into the polynomial norm identity:

\[
\begin{aligned}
A_jG_{k,D}(y_j)^2
&=1+D(y_{kj}+cN)^2\\
&=A_{kj}+DcN(2y_{kj}+cN).
\end{aligned}
\]

For \(c=0\), this is exactly (8), with global supplied root. For \(c>0\),
the discrepancy is a nonzero multiple of \(N\). The modular square-root
relation survives, but the exact integer square-class relation need not.
Thus P214 plus the clean polynomial identities leaves the carried and
arithmetic-specialization kernel uncontrolled.

## 8. Verification of the displayed finite relation

For \(D=2\), \(k=3\), and \(y=6\),

\[
F_{3,2}(6)=6(3+8\cdot36)=1746,
\qquad
G_{3,2}(6)=1+8\cdot36=289.
\]

Then

\[
A_{17}=1+2\cdot6^2=73
\]

and

\[
A_{51}=1+2\cdot1746^2
=6097033
=73\cdot289^2.
\]

Thus

\[
A_{17}A_{51}=(73\cdot289)^2=21097^2.
\]

The recorded supplied residues satisfy

\[
1692\cdot3916\equiv3773\pmod{4331}
\]

and

\[
21097\equiv3773\pmod{4331}.
\]

Hence

\[
\gcd(21097-3773,4331)=4331,
\qquad
\gcd(21097+3773,4331)=1.
\]

The recurrence and cleanup scan that located and classified these rows is
frozen separately. The displayed arithmetic independently verifies the
dependency and its global root. The claim that no earlier cleanup factor
occurred in the complete window is finite computational evidence, not an
asymptotic theorem.

