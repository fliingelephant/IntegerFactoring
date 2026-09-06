# F192 candidate — P164 gives hidden ACD clusters, but the standard row lattice has exact coprime shortest vectors

## Status and exact scope

This is a proof-only theorem about one elementary projection of the P164
long-action state. No mathematical computation is used.

The positive part is that one P164 action base produces a public QP-length
power word that is simultaneously distinct modulo every hidden rational
prime. Consequently, every hidden prime has a hidden cluster of public
differences that are approximate multiples of that prime.

The negative part concerns only the standard simultaneous-approximation row
lattice built from one such cluster. At the natural cluster error scale, in
every polylogarithmic dimension, a Dirichlet vector is strictly shorter than
every vector whose coefficient can reveal a factor. In the stated range,
every coordinate of every shortest vector is a unit modulo \(N\). Thus even
exact SVP plus coordinate gcd tests does not factor \(N\) through this
lattice.

This is not a lower bound for arbitrary lattices, robust ACD decoders,
source-aware use of the power recurrence, or integer factoring. A decoder
that uses the P164 recurrence to locate a hidden local cluster without a
predeclared subset bank remains open.

## 1. P164-derived locally distinct power word

Let

\[
N=PQ,
\qquad P\ge Q,
\tag{1}
\]

where \(P,Q\) are distinct odd primes. Let \(w\) be a unit modulo \(N\), and
write

\[
g_S=\operatorname{ord}_S(w)>1,
\qquad S\in\{P,Q\}.
\tag{2}
\]

Let \(a,K\ge1\) be public integers such that, for every rational prime
\(\ell\mid g_Pg_Q\),

\[
\ell\nmid a,
\qquad
\operatorname{ord}_\ell(a)>K.
\tag{3}
\]

Put \(R=K+1\), and define the public word

\[
x_j=[w^{a^j}]_N,
\qquad 0\le j<R,
\tag{4}
\]

using least nonnegative residues modulo \(N\). Then

\[
\boxed{x_0,\ldots,x_{R-1}\text{ are pairwise distinct modulo both }P
\text{ and }Q.}
\tag{5}
\]

Condition (3) is exactly the part of the P164 surviving branch used here:
any one retained P164 base has order above \(K\) modulo every rational prime
in every final local order.

## 2. Hidden all-inlier approximate-multiple clusters

Fix \(S\in\{P,Q\}\), and let \(1\le m<R\). There are distinct public-word
indices

\[
j_0,j_1,\ldots,j_m
\tag{6}
\]

such that, for \(1\le i\le m\),

\[
z_i=[x_{j_i}-x_{j_0}]_N
    =S t_i+r_i,
\qquad
0<r_i\le \left\lceil{mS\over R}\right\rceil .
\tag{7}
\]

Every \(z_i\) is a unit modulo \(N\). The indices in (6) depend on the
hidden cyclic order of the \(x_j\bmod S\); the theorem does not claim that
P164 makes them publicly identifiable.

For the lattice theorem, take \(S=P\). Let \(\widehat B\) be any integer
bound satisfying

\[
\left\lceil{mP\over R}\right\rceil
\le \widehat B<Q,
\qquad
\epsilon={\widehat B\over P}.
\tag{8}
\]

The theorem grants both the correct cluster and this valid bound. This is
strictly more information than the bare P164 transcript supplies. Under a
fixed public balance bound \(P/Q\le C\), a public constant-factor choice of
\(\widehat B\) follows from \(N,m,R,C\) whenever \(m/R\) is sufficiently
small.

## 3. Exact standard row-lattice obstruction

Form the dimension-\(D=m+1\) row lattice

\[
L=L(N,\widehat B;z_1,\ldots,z_m)
=\left\langle
(\widehat B,z_1,\ldots,z_m),
(0,N,0,\ldots,0),\ldots,(0,\ldots,0,N)
\right\rangle_{\mathbb Z}.
\tag{9}
\]

It has determinant

\[
\boxed{\det L=\widehat B N^m.}
\tag{10}
\]

The cluster equations (7) give the factor-bearing vector

\[
v_Q=(Q\widehat B,Qr_1,\ldots,Qr_m)\in L,
\tag{11}
\]

with

\[
Q\widehat B\le \|v_Q\|_2
\le Q\widehat B\sqrt D.
\tag{12}
\]

The first-coordinate scale relative to the determinant root is exactly

\[
{Q\widehat B\over(\det L)^{1/D}}
=\left(Q\epsilon^m\right)^{1/D}.
\tag{13}
\]

Assume there is an integer \(A\ge2^m\) such that

\[
\left({2\sqrt D\over\epsilon}\right)^m
<A<{Q\over\sqrt D}.
\tag{14}
\]

Then

\[
\boxed{\lambda_1(L)<Q\widehat B.}
\tag{15}
\]

More strongly, every shortest nonzero vector of \(L\) has all coordinates
coprime to \(N\). Therefore exact Euclidean SVP followed by gcd tests of the
coefficient or any output coordinate returns no factor.

For a fixed-balance semiprime, numerical-QP \(R\), and polylogarithmic
\(m\), with a constant-factor bound

\[
\widehat B/P=O(m/R),
\tag{16}
\]

condition (14) holds for all sufficiently large
\(n=\lceil\log_2N\rceil\). Indeed, the logarithm of its lower endpoint is
polylogarithmic in \(n\), whereas
\(\log_2(Q/\sqrt D)=n/2-o(n)\).

Thus the polylogarithmic-dimensional shortest-vector/coordinate-gcd decoder
for this standard lattice cannot be the missing P164-to-P163 bridge.

## 4. Unknown-cyclic-order subset-bank lower bound

Let \(2\le s<R\). Let \(\mathcal F\) be a fixed family of \(s\)-subsets of
\(\{0,\ldots,R-1\}\) with this property:

> For every oriented cyclic order of the \(R\) labels, some member of
> \(\mathcal F\) is a block of \(s\) consecutive labels.

Then

\[
\boxed{
|\mathcal F|\ge {1\over R}{R\choose s}.
}
\tag{17}
\]

With \(s=m+1\), this is an exact necessary lower bound for a predeclared
bank that is guaranteed to contain a consecutive hidden local block while
using no information beyond the unknown cyclic order.

This lower bound does not apply to a source-aware selector that exploits the
specific recurrence \(x_{j+1}=x_j^a\bmod N\). It also does not assert that
every cyclic order occurs in a P164 transcript. It isolates the information
missing from the distinctness-plus-pigeonhole argument.

## 5. Exact surviving interface

F192 leaves one precise possible bridge:

> Use the public power recurrence, or another factor-asymmetric invariant,
> to identify a locally close subset without enumerating an unknown cyclic
> order; then decode it by a method not reduced to the obstructed shortest
> vector of (9).

Any smaller integer returned for P163 must also have a proved local-order
prime-support property. Short coprime vectors in (9) have no such proved
property merely because they are short.
