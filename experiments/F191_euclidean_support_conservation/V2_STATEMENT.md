# F191 V2 candidate — Euclidean normalization conserves hidden-prime support

## Status and exact scope

This is a proof-only named-model obstruction for the attempted transition
from P164 to P163. No mathematical computation is used. V2 preserves the
exact congruence law, canonical counterexample, and finite permutation-bank
theorem from V1. It repairs only the failed direct-handoff conditions and the
roughness-cap quantifier.

Let

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\tag{0}
\]

P163 needs a public QP list of positive integers with at most \(n-1\) bits
whose rational-prime supports cover every surviving local-order prime. A
proposed shortcut is to construct a huge, possibly binary-succinct or
high-degree, integer \(X\) known to be divisible by such a prime \(\ell\),
and then replace \(X\) by a Euclidean quotient, a residue, or a centered
residue below \(N/2\).

F191 proves that this normalization step supplies no support transfer by
itself. If the division modulus is a unit modulo \(\ell\), the remainder
contains \(\ell\) exactly when the discarded quotient already contains
\(\ell\). If a nonzero division modulus is not a unit, that modulus has
\(\ell\)-support, but it is a direct P163 auxiliary only after the required
nonzero and size bounds are also proved. Thus any successful route must
separately force an admissible \(\ell\)-divisible quotient or carry, or prove
a support-preserving size-localization theorem.

The theorem does not rule out an \((N,w)\)-correlated floor theorem that
forces such an admissible quotient, a non-Euclidean integer selector, or a
direct factor or common-order construction.

## 1. Exact support-conservation law

Let \(\ell\) be a prime, let \(X,D,Q,R\in\mathbb Z\), and suppose

\[
\ell\mid X,
\qquad
X=QD+R.
\tag{1}
\]

If \(\ell\nmid D\), then

\[
\boxed{\ell\mid R\quad\Longleftrightarrow\quad\ell\mid Q.}
\tag{2}
\]

If \(\ell\mid D\) and \(D\ne0\), then \(D\) has the required prime support.
This is only a support statement. It makes \(|D|\) a direct P163 auxiliary
only when

\[
0<|D|<N/2.
\tag{3}
\]

The degenerate value \(D=0\) is not called a support carrier and supplies no
usable auxiliary.

Consequently, for \(\gcd(\ell,N)=1\), every ordinary or centered division

\[
X=QN+R,
\qquad |R|<N/2,
\tag{4}
\]

obeys (2). Recursively factoring \(|R|\) cannot recover \(\ell\) when the
quotient misses \(\ell\). If \(|R|\) does contain \(\ell\), then the quotient
already did so before centering.

This statement is independent of how \(X\) was represented or constructed.
It applies equally to an explicitly written integer, a high-degree
polynomial value, a resultant, a factorial or cyclotomic value, and a
binary-succinct power, provided the proposed localization step is the
Euclidean decomposition (1).

## 2. Universal canonical counterexample

Let \(N\ge7\), and let \(\ell\) be an odd prime such that

\[
\gcd(\ell,N)=1,
\qquad
3\le\ell<N/2.
\tag{5}
\]

Let \(c\) be the unique balanced representative of \(-N\bmod\ell\):

\[
c\equiv-N\pmod\ell,
\qquad
0<|c|\le{\ell-1\over2}.
\tag{6}
\]

Put

\[
X=N+c.
\tag{7}
\]

Then

\[
\ell\mid X,
\qquad
N/2<X<3N/2,
\tag{8}
\]

but the canonical centered decomposition is

\[
X=1\cdot N+c.
\tag{9}
\]

Both possible smaller children satisfy

\[
1<N/2,
\qquad
0<|c|<N/2,
\qquad
\ell\nmid1,
\qquad
\ell\nmid c.
\tag{10}
\]

Thus even an exact \(\ell\)-multiple lying within \(N/2\) of \(N\) can lose
all \(\ell\)-support when it is replaced by its centered quotient and
remainder.

## 3. A QP permutation-bank obstruction

Let \(N\) be odd, let \(\ell<N/2\) be a prime coprime to \(N\), and let

\[
\pi_1,\ldots,\pi_B
\tag{11}
\]

be arbitrary permutations of \(\{0,1,\ldots,N-1\}\). This model grants the
normalizer more information than P164 supplies: for a public parameter
\(u\), it is handed the \(B\) exact \(\ell\)-multiples

\[
X_i(u)=\ell\,\pi_i(u).
\tag{12}
\]

For each \(i\), use nearest-integer centered division

\[
X_i(u)=Q_i(u)N+R_i(u),
\qquad
|R_i(u)|<N/2.
\tag{13}
\]

For one selector, the number of parameters for which its quotient or
remainder retains \(\ell\)-support is at most

\[
\#\{u:\ell\mid Q_i(u)\}
=\#\{u:\ell\mid R_i(u)\}
\le {N\over\ell}+2.
\tag{14}
\]

Hence

\[
\#\left\{u:
\exists i,\ \ell\mid Q_i(u)R_i(u)
\right\}
\le B\left({N\over\ell}+2\right).
\tag{15}
\]

If

\[
\ell\ge4B,
\qquad
N\ge8B,
\tag{16}
\]

then the right side of (15) is at most \(N/2\). Therefore at least one
parameter \(u\) makes every quotient and every centered remainder miss
\(\ell\), although every pre-normalized \(X_i(u)\) is an exact multiple of
\(\ell\). For such a parameter,

\[
1\le Q_i(u)\le\ell-1<N/2,
\qquad
0<|R_i(u)|<N/2,
\tag{17}
\]

and none of these \(2B\) valid smaller children has \(\ell\) in its prime
support.

Here is the noncircular QP specialization. Fix, before choosing the P161
roughness cap, an integer-valued bank bound \(B_\star(n)\ge1\), independent
of that cap, such that for some fixed constants \(c,C>0\),

\[
B_\star(n)\le
2^{c(\log_2(n+2))^C}
\tag{18}
\]

for all \(n\). Set

\[
T(n)=4B_\star(n)+1.
\tag{19}
\]

For every bank with \(B\le B_\star(n)\), each surviving P161 order prime
\(\ell>T(n)\) satisfies \(\ell>4B\). In the P161--P164 composite branch one
also has \(\ell<N/2\), so \(N>2\ell>8B\). Thus (16) holds. Both
\(B_\star\) and \(T\) are numerical QP.

If instead a proposed bank bound is a function \(B_\star(n,T)\) of the
roughness cap, the same conclusion is conditional on exhibiting in advance
a numerical-QP function \(T(n)\) satisfying

\[
4B_\star(n,T(n))<T(n).
\tag{20}
\]

F191 does not assert that such a dominating choice always exists.

## 4. Exact surviving interface

F191 closes only this named route:

\[
\text{large known }\ell\text{-multiple}
\longrightarrow
\text{Euclidean or centered normalization}
\longrightarrow
\text{claimed }<N/2\text{ support child}.
\tag{21}
\]

The exact direct P163 interface is:

> Construct, at total numerical-QP cost, a public numerical-QP list of
> integers \(A_1,\ldots,A_s\) such that
> \[
> 0<|A_j|<N/2
> \]
> for every \(j\), and prove that every surviving local-order prime divides
> at least one \(A_j\).

Then \(|A_1|,\ldots,|A_s|\) is a positive P163-admissible list; entries equal
to one may be skipped. A quotient or carry that lacks the displayed nonzero
and size bounds is not a direct handoff. Such a route must instead prove a
separate numerical-QP transformation to admissible integers that preserves
the required prime support. The support-conservation law shows that ordinary
or centered reduction alone is not that theorem.
