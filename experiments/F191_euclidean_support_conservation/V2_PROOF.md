# Proof of the F191 V2 Euclidean support-conservation theorem

## 1. Exact support conservation

Reduce

\[
X=QD+R
\tag{1.1}
\]

modulo \(\ell\). Since \(\ell\mid X\),

\[
R\equiv-QD\pmod\ell.
\tag{1.2}
\]

If \(\ell\nmid D\), multiplication by \(D\) is invertible in
\(\mathbb F_\ell\). Therefore

\[
R\equiv0\pmod\ell
\quad\Longleftrightarrow\quad
Q\equiv0\pmod\ell.
\tag{1.3}
\]

If \(\ell\mid D\) and \(D\ne0\), the public integer \(D\) contains the
desired prime support. This does not by itself make \(D\) a valid smaller
child: the direct P163 handoff additionally requires \(0<|D|<N/2\). If
\(D=0\), the identity reads \(X=R\), and zero is not a usable support
auxiliary. No carrier conclusion is claimed in that degenerate branch.

The proof of (1.3) uses neither a size bound nor a representation of \(X\).
Thus a short arithmetic circuit for a huge \(X\), or the fact that \(X\)
arose as a resultant, factorial, cyclotomic value, or power, does not change
(1.3). What matters is the quotient congruence. Centering chooses one
particular quotient; it does not alter the congruence law.

If both \(Q\) and \(|R|\) are admissible recursive candidates, (1.3) has
only two possibilities:

1. both contain \(\ell\), in which case \(Q\) already supplies a support
   child before the remainder is used;
2. neither contains \(\ell\), in which case recursively factoring either
   child cannot reveal \(\ell\).

This is the precise sense in which Euclidean normalization conserves rather
than creates prime support.

## 2. Canonical counterexample

Because \(\gcd(\ell,N)=1\), the residue \(-N\bmod\ell\) is nonzero. Since
\(\ell\) is odd, it has a unique representative \(c\) satisfying

\[
0<|c|\le(\ell-1)/2.
\tag{2.1}
\]

By definition,

\[
N+c\equiv0\pmod\ell.
\tag{2.2}
\]

The hypothesis \(\ell<N/2\) gives

\[
|c|<N/4.
\tag{2.3}
\]

In particular,

\[
N/2<N+c<3N/2.
\tag{2.4}
\]

The nearest multiple of \(N\) to \(X=N+c\) is therefore \(N\) itself, so
the canonical centered quotient and remainder are exactly

\[
Q=1,
\qquad R=c.
\tag{2.5}
\]

Neither is divisible by \(\ell\): this is clear for one, while
\(0<|c|<\ell\) handles the remainder. Both absolute values are below
\(N/2\). This proves the universal counterexample.

Notice that the example grants the strongest possible input fact for this
normalization strategy: the original integer is an exact multiple of the
target prime. Its failure is not caused by approximate annihilation or by a
polynomial root bound.

## 3. One centered selector in the permutation-bank model

Fix one permutation \(\pi_i\). Because it is bijective, counting parameters
\(u\) is the same as counting

\[
b=\pi_i(u)\in\{0,1,\ldots,N-1\}.
\tag{3.1}
\]

Write the centered division as

\[
\ell b=Q(b)N+R(b),
\qquad |R(b)|<N/2.
\tag{3.2}
\]

Since \(N\) is odd, \(\ell b/N\) is never a half-integer. Indeed,
\(2\ell b=(2t+1)N\) would equate an even integer with an odd integer. Thus
the nearest integer \(Q(b)\) is unique.

The range

\[
0\le {\ell b\over N}<\ell
\tag{3.3}
\]

implies

\[
Q(b)\in\{0,1,\ldots,\ell\}.
\tag{3.4}
\]

By the support-conservation law,

\[
\ell\mid R(b)
\quad\Longleftrightarrow\quad
\ell\mid Q(b).
\tag{3.5}
\]

Within (3.4), the latter event is exactly

\[
Q(b)=0
\quad\text{or}\quad
Q(b)=\ell.
\tag{3.6}
\]

The first case requires

\[
0\le b<{N\over2\ell},
\tag{3.7}
\]

and the second requires

\[
N-{N\over2\ell}<b<N.
\tag{3.8}
\]

Each interval contains at most \(N/(2\ell)+1\) integers. Hence

\[
\#\{b:\ell\mid Q(b)\}
=\#\{b:\ell\mid R(b)\}
\le {N\over\ell}+2.
\tag{3.9}
\]

Pulling the set back through \(\pi_i\) preserves its cardinality, which
proves (14).

## 4. The bank union bound

For \(B\) permutations, the union bound and (3.9) give

\[
\#\{u:\exists i,\ \ell\mid Q_i(u)R_i(u)\}
\le B\left({N\over\ell}+2\right).
\tag{4.1}
\]

If \(\ell\ge4B\) and \(N\ge8B\), then

\[
B{N\over\ell}\le {N\over4},
\qquad
2B\le {N\over4}.
\tag{4.2}
\]

Thus (4.1) is at most \(N/2<N\), and at least one parameter lies outside
the union.

For such a parameter, \(Q_i\) is neither zero nor \(\ell\). Equation (3.4)
therefore gives

\[
1\le Q_i\le\ell-1<N/2.
\tag{4.3}
\]

Also \(R_i\ne0\): if \(R_i=0\), (3.5) would make \(Q_i\) divisible by
\(\ell\). Centered division and odd \(N\) give

\[
0<|R_i|<N/2.
\tag{4.4}
\]

Neither child contains \(\ell\), again by (3.5). This proves the finite bank
theorem.

The permutation premise is the exact named model being obstructed. It covers
normalization banks whose multipliers are equidistributed under a public
parameter. It does not cover a nonpermutation map deliberately concentrated
on the two endpoint intervals (3.7)--(3.8). Proving that an actual
\((N,w)\)-correlated selector has such concentration would be a new quotient
or carry theorem, not a consequence of centering.

## 5. Noncircular applicability to the P161--P164 state

Let \(R=p^e\) be a hidden prime-power component and let \(g\) be one of the
P161 local orders. P161 gives \(\gcd(g,N)=1\). The kernel of reduction

\[
(\mathbb Z/p^e\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p\mathbb Z)^\times
\tag{5.1}
\]

is a \(p\)-group, so reduction is injective on the cyclic subgroup of order
\(g\). Hence

\[
g\mid p-1.
\tag{5.2}
\]

Every local-order prime \(\ell\mid g\) therefore satisfies

\[
\ell\le p-1.
\tag{5.3}
\]

On an odd composite input, either another factor accompanies \(p^e\), in
which case \(p\le N/3\), or \(N=p^e\) with \(e\ge2\), in which case
\(p\le\sqrt N<N/2\). Thus

\[
\ell<N/2.
\tag{5.4}
\]

Now fix an integer-valued numerical-QP bank budget \(B_\star(n)\ge1\)
before choosing the P161 cap, and require that the budget be independent of
that cap. Define

\[
T(n)=4B_\star(n)+1.
\tag{5.5}
\]

Multiplication by a constant and addition preserve the numerical-QP bound,
so P161 may use this \(T\). For any actual bank size
\(B\le B_\star(n)\), every surviving prime satisfies

\[
\ell>T(n)>4B_\star(n)\ge4B.
\tag{5.6}
\]

Together with (5.4), this yields

\[
N>2\ell>8B.
\tag{5.7}
\]

The hypotheses of the finite bank theorem therefore hold. There is no
quantifier cycle: \(B_\star\) is fixed first, and \(T\) is then defined from
it.

If a bank budget is instead specified as \(B_\star(n,T)\), the same proof
works only after a public numerical-QP function \(T(n)\) is exhibited with

\[
4B_\star(n,T(n))<T(n).
\tag{5.8}
\]

This is a separate uniform-dominance premise, not a consequence of F191.

The argument does not show that the actual P164 transcript is distributed
as the permutation-bank model. It proves the narrower and
stronger-information statement claimed: even when a bank is granted exact
multiples of the hidden order prime, Euclidean normalization plus
equidistribution does not force a support-covering child. A positive
P164-to-P163 bridge must prove special arithmetic concentration of an
admissible quotient or carry, prove support-preserving size localization,
or use a different mechanism.

## 6. Verification of the direct P163 interface

Suppose a public numerical-QP procedure outputs integers
\(A_1,\ldots,A_s\) satisfying

\[
0<|A_j|<N/2
\tag{6.1}
\]

and covering every surviving local-order prime. Then every \(|A_j|\) is a
positive integer. Since \(N<2^n\) under the definition
\(n=\lceil\log_2(N+1)\rceil\), (6.1) gives

\[
|A_j|<N/2<2^{n-1}.
\tag{6.2}
\]

Thus each nonunit entry has at most \(n-1\) bits, exactly as P163 requires.
Taking absolute values preserves rational-prime divisibility, and entries
equal to one may be skipped. The resulting list is therefore a direct P163
input.

By contrast, divisibility of an unrestricted quotient or carry does not
imply (6.1). It may be zero or oversized; a negative value is usable only
after its nonzero magnitude is bounded. Hence an unrestricted value needs a
separate support-preserving size-localization theorem. Section 1 proves that
ordinary or centered reduction alone cannot provide that missing inference.
