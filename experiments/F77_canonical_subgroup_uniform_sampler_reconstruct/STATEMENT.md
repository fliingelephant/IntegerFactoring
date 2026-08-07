# Proof-blind reconstruction statement: canonical subgroup sampler

Work only from this statement. Do not read any F77 candidate, audit, durable
ledger, proof, or conversation context. Do not run computation. Reconstruct
all claims from first principles and return a self-contained PASS proof or the
first exact failure.

## Public sampler

Let \(N\ge3\), let \(q_1,\ldots,q_s\) be public units modulo \(N\), and put

\[
H=\langle q_1,ldots,q_s\rangle.
\]

The factorization of \(N\), the orders of the generators, and \(|H|\) are
unknown. Let

\[
n=\lceil\log_2N\rceil,
\quad
L=3n+\lceil\log_2(s+1)\rceil,
\quad
M=2^L.
\]

Choose independent uniform
\(E_j\in\{0,1,\ldots,M-1\}\) and output

\[
X=\left[\prod_jq_j^{E_j}\right]_N.
\]

Prove that the distribution of \(X\) has total-variation distance less than
\(2^{-2n}\) from uniform on \(H\), without computing any generator order.
Prove the stated \(O(s(n+\log s))\) random-bit bound and polynomial bit
complexity in \(s+n\).

## Exact density formulas

Assume for analysis that \(N=pq\) for distinct odd primes. Let \(H_p,H_q\)
be the projection images of \(H\). For uniform \(X\in H\), prove

\[
\delta_+
:=\Pr(1<\gcd(X-1,N)<N)
=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|}.
\]

Let

\[
\epsilon_p=\mathbf1_{-1\in H_p},
\quad
\epsilon_q=\mathbf1_{-1\in H_q},
\quad
\epsilon=\mathbf1_{-1\in H}.
\]

Prove

\[
\delta_-
:=\Pr(1<\gcd(X+1,N)<N)
=\frac{\epsilon_p}{|H_p|}
+\frac{\epsilon_q}{|H_q|}
-\frac{2\epsilon}{|H|}.
\]

Explain why the positive and negative success sets can overlap and should not
be added without correcting that overlap.

## Conditional Las Vegas consequence

Prove that if either \(\delta_+\) or \(\delta_-\) is at least \(n^{-c}\) for
a fixed \(c\), repeated calls to the public sampler with both sign gcds give
a Las Vegas expected-polynomial factorization of the semiprime. Address all
\(N\ge3\), including the possible small-\(n\) concern from total variation.
Every output must be verified by exact division.

## Density obstruction

Let \(C_L=\langle a\rangle\) have even order \(L\), and define the abstract
subgroup

\[
H=\langle(a,a),(1,-1)\rangle
\subseteq C_L\times C_L.
\]

Prove \(|H|=2L\), both projection images have order \(L\), and
\(\delta_+=1/L\), although \((1,-1)\) is a separator. Treat this only as an
abstract density calculation; do not assert an infinite integer family.

## Required scope

The result shows that near-uniform sampling from a public generated subgroup
is easy. It does not generate the subgroup from bare \(N\), prove an
inverse-polynomial separator density, find a sparse separator, or prove an
all-input factoring algorithm. A complete feedback theorem must instead prove
an inverse-polynomial density after refinement, a polynomial sparse word, or
another refinement that creates one of those conditions.
