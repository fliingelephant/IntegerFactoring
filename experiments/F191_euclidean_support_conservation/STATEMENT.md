# F191 candidate — Euclidean normalization conserves hidden-prime support

## Status and exact scope

This is a proof-only named-model obstruction for the attempted transition
from P164 to P163. No mathematical computation is used.

P163 needs a public list of positive integers below \(N/2\) whose rational
prime supports cover every surviving local-order prime. A proposed shortcut
is to construct a huge, possibly binary-succinct or high-degree, integer
\(X\) known to be divisible by such a prime \(\ell\), and then replace
\(X\) by a Euclidean quotient, a residue, or a centered residue below
\(N/2\).

F191 proves that this normalization step supplies no support transfer by
itself. If the division modulus is a unit modulo \(\ell\), the remainder
contains \(\ell\) exactly when the discarded quotient already contains
\(\ell\). If the division modulus is not a unit, that modulus is itself an
\(\ell\)-supported auxiliary. Thus any successful route must separately
force an \(\ell\)-divisible quotient or carry.

The theorem does not rule out an \((N,w)\)-correlated floor theorem that
forces such a quotient, a non-Euclidean integer selector, or a direct factor
or common-order construction.

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

If \(\ell\mid D\), then \(D\) itself already carries the required prime
support, although a separate size/localization step may still be needed if
\(D\ge N/2\).

Consequently, for \(\gcd(\ell,N)=1\), every ordinary or centered division

\[
X=QN+R,
\qquad |R|<N/2,
\tag{3}
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
\tag{4}
\]

Let \(c\) be the unique balanced representative of \(-N\bmod\ell\):

\[
c\equiv-N\pmod\ell,
\qquad
0<|c|\le{\ell-1\over2}.
\tag{5}
\]

Put

\[
X=N+c.
\tag{6}
\]

Then

\[
\ell\mid X,
\qquad
N/2<X<3N/2,
\tag{7}
\]

but the canonical centered decomposition is

\[
X=1\cdot N+c.
\tag{8}
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
\tag{9}
\]

Thus even an exact \(\ell\)-multiple lying within \(N/2\) of \(N\) can lose
all \(\ell\)-support when it is replaced by its centered quotient and
remainder.

## 3. A QP permutation-bank obstruction

Let \(N\) be odd, let \(\ell<N/2\) be a prime coprime to \(N\), and let

\[
\pi_1,\ldots,\pi_B
\tag{10}
\]

be arbitrary permutations of \(\{0,1,\ldots,N-1\}\). This model grants the
normalizer more information than P164 supplies: for a public parameter
\(u\), it is handed the \(B\) exact \(\ell\)-multiples

\[
X_i(u)=\ell\,\pi_i(u).
\tag{11}
\]

For each \(i\), use nearest-integer centered division

\[
X_i(u)=Q_i(u)N+R_i(u),
\qquad
|R_i(u)|<N/2.
\tag{12}
\]

For one selector, the number of parameters for which its quotient or
remainder retains \(\ell\)-support is at most

\[
\#\{u:\ell\mid Q_i(u)\}
=\#\{u:\ell\mid R_i(u)\}
\le {N\over\ell}+2.
\tag{13}
\]

Hence

\[
\#\left\{u:
\exists i,\ \ell\mid Q_i(u)R_i(u)
\right\}
\le B\left({N\over\ell}+2\right).
\tag{14}
\]

If

\[
\ell\ge4B,
\qquad
N\ge8B,
\tag{15}
\]

then the right side of (14) is at most \(N/2\). Therefore at least one
parameter \(u\) makes every quotient and every centered remainder miss
\(\ell\), although every pre-normalized \(X_i(u)\) is an exact multiple of
\(\ell\). For such a parameter,

\[
1\le Q_i(u)\le\ell-1<N/2,
\qquad
0<|R_i(u)|<N/2,
\tag{16}
\]

and none of these \(2B\) valid smaller children has \(\ell\) in its prime
support.

If \(B\) is any fixed numerical-QP bound, P161 may choose its roughness cap
\(T>4B\). Every surviving order prime has \(\ell>T\). In the P161--P164
composite branch one also has \(\ell<N/2\), so \(N>2\ell>8B\). Thus (15)
holds automatically. A QP bank of permutation-based floor/center selectors
cannot obtain deterministic support coverage merely from the fact that its
preimages are \(\ell\)-multiples.

## 4. Exact surviving interface

F191 closes only this named route:

\[
\text{large known }\ell\text{-multiple}
\longrightarrow
\text{Euclidean or centered normalization}
\longrightarrow
\text{claimed }<N/2\text{ support child}.
\tag{17}
\]

The smaller live interface is:

> Construct a QP bank of integer quotients or carries and prove, from the
> specific arithmetic correlation with \((N,w)\), that every surviving
> local-order prime divides at least one of them.

Once that quotient/carry theorem is proved, P163 can use those values
directly. Centering is redundant for prime-support discovery.
