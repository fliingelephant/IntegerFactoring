# F183 candidate — a QP small-base menu has a fully factored extinction branch

## Status and scope

This is a proof-only constructive postprocessor for the F181 rough-order
branch. It applies to arbitrary odd composites, including repeated prime
factors. Unlike F182's shifted bases \(N+\delta\), every integer in this
candidate's annihilator can be factored completely in QP time. It is not an
all-input factoring algorithm.

Let

\[
N=\prod_{j=1}^sR_j,
\qquad
n=\lceil\log_2(N+1)\rceil,
\tag{1}
\]

be the hidden prime-power decomposition. Suppose F181 has returned a public
unit \(w\) with local orders

\[
g_j=\operatorname{ord}_{R_j}(w),
\qquad
g_j>1,
\qquad
\gcd(g_j,N)=1,
\qquad
P^-(g_j)>T.
\tag{2}
\]

Choose fixed constants \(c,d,C\ge1\), and put

\[
K=\left\lceil(\log_2(n+1))^c\right\rceil,
\qquad
L=\left\lceil2^{C(\log_2(n+1))^d}\right\rceil.
\tag{3}
\]

Require the integer roughness cap to satisfy

\[
T\ge L+1.
\tag{4}
\]

For every public base \(a\in\{2,3,\ldots,L+1\}\), define

\[
C_a=a\prod_{k=1}^K(a^k-1).
\tag{5}
\]

Factor every \(C_a\) completely by trial division. Merge repeated prime
factors and their valuations to obtain the complete factorization of

\[
P=\prod_{a=2}^{L+1}C_a.
\tag{6}
\]

Compute

\[
z=w^{P^n}\bmod N,
\qquad
H=\gcd(z-1,N).
\tag{7}
\]

For every hidden component, define

\[
h_j=
\prod_{\substack{\ell^e\parallel g_j\\
\forall a\in[2,L+1]:\ \,\ell\nmid a\\
\forall a\in[2,L+1]:\ \,\operatorname{ord}_\ell(a)>K}}
\ell^e.
\tag{8}
\]

Then

\[
\boxed{\operatorname{ord}_{R_j}(z)=h_j.}
\tag{9}
\]

The procedure returns exactly one of the following outcomes.

1. **Factor.** If \(1<H<N\), then \(H\) is a proper factor of \(N\).
2. **Exact common-order state.** If \(H=N\), factor-first stripping from
   the fully factored annihilator \(P^n\) either returns a proper factor,
   or proves that \(w\) has one exact common local order
   \[
   m=g_j>T
   \qquad(1\le j\le s).
   \tag{10}
   \]
3. **Wide small-base hard descendant.** If \(H=1\), then every \(h_j\)
   is nontrivial and \(T\)-rough. For every prime \(\ell\mid h_j\) and
   every \(2\le a\le L+1\),
   \[
   \boxed{
   \ell\nmid a,
   \qquad
   \operatorname{ord}_\ell(a)>K.
   }
   \tag{11}
   \]

Thus F181 admits the deterministic trichotomy

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }T
\quad\lor\quad
\text{a }T\text{-rough descendant hard for all }L\text{ small bases}.
}
\tag{12}
\]

All trial division, product construction, modular powering, gcd, and
factor-first work has uniform deterministic quasipolynomial bit cost.

## Exact boundary

F183 replaces F182's shifted-action menu by a simpler fully factored
small-base menu. It loses the special cofactor action carried by
\(N+\delta\), but global extinction now gives an exact state rather than an
unfactored annihilator. The surviving branch can still contain unequal rough
local orders. No QP factoring theorem is claimed.
