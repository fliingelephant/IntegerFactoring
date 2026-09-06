# F146 V2 — quasipolynomial AKS exchange-minor boundary

**Status:** corrected proof-only candidate. No computation is used.

**Version record:** STATEMENT.md and PROOF.md are frozen V1 artifacts.
HOSTILE_AUDIT_FAILED.md records the false V1 equivalence. V2 replaces that
equivalence and repairs the empty-tail bound. It does not modify V1.

**Approach family:** F04.

## Closest prior result and material difference

P24 proves that the two local full column matroids of the fixed P11 AKS
matrix differ. Their first verified difference replaces two columns of a
common base. P24 gives no cost theorem for a growing exchange radius and no
reason that a small-radius difference must exist on other inputs.

F146 gives the exact quasipolynomial cost of that scan. It also gives an
unconditional representable-matroid obstruction: for every prescribed
radius, two reductions of one matrix can agree on all exchanges through that
radius and first differ at the next radius. Thus any positive theorem for
AKS matrices must use their arithmetic form.

## Setup and the corrected success criteria

Let \(N\) be composite, let

\[
n=\lceil\log_2(N+1)\rceil,
\]

and let

\[
M_N=[B\mid T]\in(\mathbb Z/N\mathbb Z)^{A\times r},
\qquad t=r-A,
\]

where \(B\) has \(A\) columns and

\[
\gcd(\det B,N)=1.
\]

Put \(C=B^{-1}T\). For sets \(I\subseteq[A]\) and \(J\subseteq[t]\)
with \(|I|=|J|=k\), replace the base columns in \(I\) with the tail columns
in \(J\). The resulting maximal minor is

\[
\det E_{I,J}
=\varepsilon(I,J)\det(B)\det C[I,J],
\qquad \varepsilon(I,J)\in\{1,-1\}.
\]

Define the exact gcd-success radius

\[
\gamma_B=
\min\left\{
 k:
 \begin{array}{l}
 \exists I\subseteq[A],\ \exists J\subseteq[t],\
 |I|=|J|=k,\\
 1<\gcd(\det C[I,J],N)<N
\end{array}
\right\},
\]

and set \(\gamma_B=\infty\) if the set is empty.

Define the local-field disagreement radius

\[
\delta_B=
\min\left\{
 k:
 \begin{array}{l}
 \exists I\subseteq[A],\ \exists J\subseteq[t],\
 |I|=|J|=k,\\
 \det C[I,J]\equiv0\pmod\ell
 \text{ for some but not all primes }\ell\mid N
\end{array}
\right\},
\]

and set \(\delta_B=\infty\) if the set is empty.

Then:

1. For every composite \(N\), the support-\(s\) gcd scan succeeds exactly
   when \(\gamma_B\le s\).
2. For every composite \(N\), \(\delta_B\le s\) is sufficient for success.
3. If \(N\) is squarefree, then \(\gamma_B=\delta_B\).

In particular, \(\gamma_B\le\delta_B\) for every composite \(N\).

For non-squarefree \(N\), valuation-only splits can make
\(\gamma_B<\delta_B\). V2 makes no converse claim in that case.

## The quasipolynomial scan theorem

For \(s\ge0\), the exact number of exchanges of support at most \(s\) is

\[
Q_s(A,t)=
\sum_{k=0}^{\min(s,A,t)}
\binom Ak\binom tk.
\]

For all \(A,t,s\ge0\),

\[
Q_s(A,t)
\le (s+1)\max\{1,At\}^{s}.
\]

This includes the empty-tail case \(t=0\), where \(Q_s(A,0)=1\).

If \(A,r\le n^{O(1)}\) and

\[
s\le(\log(n+1))^d
\]

for fixed \(d\), then the complete scan has bit complexity

\[
2^{O((\log(n+1))^{d+1})}.
\]

If

\[
t=r-A\le(\log(n+1))^d,
\]

then the scan includes every maximal minor. It therefore finds every local
column-matroid mismatch. For squarefree \(N\), it succeeds exactly when the
local column matroids differ. For non-squarefree \(N\), it can also succeed
through a valuation-only split.

### Near-threshold prime-modulus corollary

Let \(L=\log_2N\). If an AKS modulus \(r\) is prime and

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
quasipolynomial time. This is only a conditional cost result. It does not
prove that every input has such a modulus, a common unit base, or a local
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

Consequently, for every fixed \(d\), sufficiently large members of this
family have no mismatch at support at most \((\log(n+1))^d\), although their
full local column matroids differ.

This is a boundary for general matrices, including matrices with
AKS-scale near-square dimensions. It is not an AKS counterexample.

## Interpretation of the P11 two-exchange certificate

On P11,

\[
A=2942,\qquad t=11,\qquad
\binom A2\binom t2=237{,}941{,}605.
\]

For a uniform random \(2\)-by-\(2\) matrix over \(\mathbb F_\ell\), the
singularity probability is

\[
z_\ell
=1-(1-\ell^{-1})(1-\ell^{-2})
=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

With the P11 primes, the independent-random comparison model predicts about
\(2.3794\) zero minors in the first field, \(1.1897\) in the second field,
and \(3.5691\) zero-pattern mismatches in total. P24 observed zero, two, and
two. For one-tail exchanges, the model predicts about \(0.000485\)
mismatches, and P24 observed none.

This comparison does not assert that the AKS matrix is random. It shows
that the P11 hit is at the random exact-zero scale. The finite certificate
is not evidence for a uniform small-support forcing law.

## Exact remaining target

A useful continuation of F04 must prove one of these statements for the
specific AKS error matrix:

1. a common unit base always has \(\gamma_B\) or \(\delta_B\) at most
   \((\log(n+1))^{O(1)}\);
2. a suitable near-threshold modulus always makes \(r-A\)
   polylogarithmic; or
3. a different quasipolynomial selector creates factor-correlated determinant
   divisibility without scanning a local exchange ball.

No result in P11, P14, P18, P24, or F146 proves one of these statements.
