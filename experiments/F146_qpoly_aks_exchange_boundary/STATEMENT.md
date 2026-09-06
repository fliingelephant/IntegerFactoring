# F146 — quasipolynomial AKS exchange-minor boundary

**Status:** frozen proof-only candidate.  No computation is used.

**Approach family:** F04.

## Closest prior result and material difference

P24 proves that the two local full column matroids of the fixed P11 AKS
matrix differ.  Their first verified difference replaces two columns of a
common base.  P24 gives no cost theorem for a growing exchange radius and no
reason that a small-radius difference must exist on other inputs.

F146 gives the exact quasipolynomial cost of that scan.  It also gives an
unconditional representable-matroid obstruction: for every prescribed
radius, two reductions of one matrix can agree on all exchanges through that
radius and first differ at the next radius.  Thus any positive theorem for
AKS matrices must use their arithmetic form.  Matroid axioms, a common base,
and global-before-local construction are not sufficient.

## Setup

Let \(N\) be composite and let

\[
M_N=[B\mid T]\in(\mathbb Z/N\mathbb Z)^{A\times r},
\qquad t=r-A,
\]

where \(B\) has \(A\) columns.  Assume

\[
\gcd(\det B,N)=1.
\]

Thus \(B\) is a basis after reduction modulo every prime divisor of \(N\).
Put \(C=B^{-1}T\) over \(\mathbb Z/N\mathbb Z\).

For \(I\subseteq[A]\) and \(J\subseteq[t]\), with

\[
|I|=|J|=k,
\]

replace the base columns indexed by \(I\) with the tail columns indexed by
\(J\).  The resulting maximal minor is, up to its explicit ordering sign,

\[
\det(B)\det C[I,J].
\]

## The quasipolynomial scan theorem

The exact number of exchanges of support at most \(s\) is

\[
Q_s(A,t)=
\sum_{k=0}^{\min(s,A,t)}
\binom Ak\binom tk.
\]

If \(A,r\le n^{O(1)}\) and

\[
s\le(\log(n+1))^d
\]

for a fixed \(d\), then

\[
Q_s(A,t)
\le (s+1)(At)^s
=2^{O((\log(n+1))^{d+1})}.
\]

After polynomial preprocessing, each test is the determinant of a
\(k\)-by-\(k\) matrix over \(\mathbb Z/N\mathbb Z\), followed by one gcd.
Division-free determinant evaluation gives total quasipolynomial bit
complexity.

This scan is complete for the full column-matroid comparison when

\[
t=r-A\le(\log(n+1))^d.
\]

Every \(A\)-column set then differs from \(B\) in at most \(t\) positions.
Therefore any local column-matroid mismatch is found.

### Near-threshold prime-modulus corollary

Let \(L=\log_2N\).  If an AKS modulus \(r\) is prime and

\[
0<r-1-L^2\le(\log(n+1))^d,
\]

then the standard shift count

\[
A=\lfloor L\sqrt{r-1}\rfloor
\]

satisfies

\[
r-A<(\log(n+1))^d+2.
\]

Thus a near-threshold prime modulus puts the complete exchange scan inside
quasipolynomial time.  This is only a conditional cost result.  F146 does
not prove that every input has such a modulus, a common unit base, or a local
matroid mismatch.

## Exact obstruction to a generic local-mismatch theorem

For every integer \(s\ge1\), there are odd primes \(q<p<2q\), \(N=pq\),
and one matrix

\[
M_N=[I_{s+1}\mid C]
\in(\mathbb Z/N\mathbb Z)^{(s+1)\times2(s+1)}
\]

with these properties:

1. Every exchange of support \(k\le s\) is a basis modulo both \(p\) and
   \(q\).
2. The exchange of all \(s+1\) base columns is a basis modulo \(p\) and is
   dependent modulo \(q\).
3. The input bit length satisfies

   \[
   n=\lceil\log_2(N+1)\rceil=\Theta(s^2\log(s+1)).
   \]

The construction can be padded without changing its first disagreement.
In particular, it can have

\[
A=n^2,\qquad r=A+s+1.
\]

These are of the same polynomial size and near-square shape as the P11
matrix.  The padded matrix is still not claimed to be an AKS error matrix.

Consequently, for every fixed \(d\), sufficiently large members of this
family have no mismatch at support at most \((\log(n+1))^d\), although their
full local column matroids differ.

This construction is a boundary for general matrices, even after the matrix
dimensions have the AKS-scale near-square shape above.  It is not an AKS
counterexample.  An AKS-specific theorem could still force a local mismatch,
but it must use the coefficient formula for the Frobenius errors.

## Interpretation of the P11 two-exchange certificate

On P11,

\[
A=2942,qquad t=11,qquad
\binom A2\binom t2=237{,}941{,}605.
\]

For a uniform random \(2\)-by-\(2\) matrix over \(\mathbb F_\ell\), the
singularity probability is

\[
z_\ell=1-(1-\ell^{-1})(1-\ell^{-2})
=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

With the P11 primes, the independent-random comparison model predicts about
\(2.3794\) zero minors in the first field, \(1.1897\) in the second field,
and \(3.5691\) zero-pattern mismatches in total.  P24 observed zero, two, and
two, respectively.  For one-tail exchanges, the same model predicts only
about \(0.000485\) mismatches, and P24 observed none.

Thus the location and scarcity of the P11 hit are at the random exact-zero
scale.  This does not prove that the AKS matrix is random.  It does mean that
the finite certificate is not evidence for a uniform small-support forcing
law.  On balanced asymptotic inputs, quasipolynomially many random-scale
determinants still have negligible total hit probability.

## Exact remaining target

A useful continuation of F04 must prove one of these statements for the
specific AKS error matrix:

1. a common unit base always has local disagreement radius
   \((\log(n+1))^{O(1)}\); or
2. a suitable near-threshold modulus always makes the AKS tail \(r-A\)
   polylogarithmic; or
3. a different quasipolynomial selector creates factor-correlated determinant
   zeros without scanning a local exchange ball.

No result in P11, P14, P18, P24, or F146 proves one of these statements.
