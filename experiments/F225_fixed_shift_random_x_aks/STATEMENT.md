# F225 candidate: fixed-shift random evaluations are sparse near the upper balance edge

## Status and scope

This is a self-audited proof-only obstruction for the fixed-shift scalar

\[
H_N(x)=(x+1)^N-x^N-1\pmod N.
\]

It closes the large-gap possibility left open by F224 for a fresh uniform
evaluation point and an individual gcd with `N`.  The proof uses the
integer relation between the two hidden primes.  It is not a generic
polynomial root bound.

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes.  Put

\[
d=q-p,\qquad c=2p-q=p-d.
\]

The integer `c` is odd.

## Theorem A: exact local root decompositions

Assume `c>=3`, and put

\[
k=c-2,\qquad s={c+1\over2}.
\]

Define

\[
P_k(X)=X^k-(X+1)^k-[X(X+1)]^k\in\mathbb F_p[X]
\]

and, for `epsilon,delta` in `{+1,-1}`,

\[
Q_{\epsilon,\delta}(X)
=\epsilon(X+1)^s-\delta X^s-1\in\mathbb F_q[X].
\]

Let `chi` be the quadratic character modulo `q`.  If `A_p` and `A_q`
denote the numbers of roots of `H_N` modulo `p` and `q`, respectively,
then

\[
\boxed{
A_p=2+\#\{x\in\mathbb F_p\setminus\{0,-1\}:P_k(x)=0\}
}
\]

and

\[
\boxed{
A_q=2+\sum_{\epsilon,\delta\in\{\pm1\}}
\#\left\{
\begin{array}{c}
x\in\mathbb F_q\setminus\{0,-1\}:\\
\chi(x+1)=\epsilon,\ \chi(x)=\delta,\\
Q_{\epsilon,\delta}(x)=0
\end{array}
\right\}.
}
\]

These are disjoint exact decompositions.  They imply

\[
\boxed{A_p\le 2c-2,\qquad A_q\le 2c+2.}
\]

## Theorem B: exact proper-gcd probabilities

For a uniform residue `x mod N`, CRT makes its two local coordinates
independent and uniform.  Therefore

\[
\boxed{
\Pr(1<\gcd(H_N(x),N)<N)
={A_p\over p}\left(1-{A_q\over q}\right)
+{A_q\over q}\left(1-{A_p\over p}\right).
}
\]

In particular,

\[
\Pr(1<\gcd(H_N(x),N)<N)\le {4c\over p}.
\]

For a uniform unit `x mod N`, the local coordinates are independent and
uniform in the two multiplicative groups.  Since `0` is one of the roots
in each field, the exact probability is

\[
\boxed{
{A_p-1\over p-1}\left(1-{A_q-1\over q-1}\right)
+{A_q-1\over q-1}\left(1-{A_p-1\over p-1}\right).
}
\]

Consequently,

\[
\boxed{
\Pr(1<\gcd(H_N(x),N)<N\mid x\in U(N))
\le {4c-2\over p-1}.
}
\]

Sampling a residue and gcd-screening it gives an exact uniform unit on the
no-factor branch.  A nonunit proper gcd occurs with probability `O(1/p)`
and does not change the obstruction below.

## Theorem C: an unconditional hostile large-gap family

Let `p` run through unbounded odd primes and set

\[
X_p=2p-\lfloor p^{3/5}\rfloor.
\]

Baker--Harman--Pintz guarantees a prime

\[
q\in[X_p-X_p^{0.525},X_p]
\]

for every sufficiently large `p`.  For this choice,

\[
c=2p-q=\Theta(p^{3/5}),
\qquad
d=q-p=p-\Theta(p^{3/5})=\Theta(p).
\]

Thus this family lies in the regime

\[
d\ge p^{2/3-o(1)}.
\]

Nevertheless, one fresh uniform evaluation has proper-gcd probability

\[
O(c/p)=O(p^{-2/5})=2^{-\Omega(n)},
\qquad n=\lceil\log_2N\rceil.
\]

Any numerical-QP bank of fresh uniform evaluations therefore has total
success probability `2^(-Omega(n))` by a conditional union bound.

Hence a large value of `d` does not force inverse-QP progress for the
fixed-shift random-point scalar channel.

## Exact remaining scope

The result covers only:

- the fixed public shift `1`;
- fresh uniform residues or units;
- an individual gcd of each scalar value with `N`; and
- a numerical-QP number of such trials.

It does not cover a point distribution biased by carry information, joint
processing of typical nonzero values, coefficient vectors, quotient-ring
ranks, an adaptive point chosen from the same value, or a method that
certifies a new contribution to the common modulus `M`.
