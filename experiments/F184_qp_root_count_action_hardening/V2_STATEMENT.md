# F184 candidate — root counting forces QP-wide action hardening

## Status and scope

This is a proof-only constructive postprocessor for the F181 rough-order
branch. It applies to arbitrary odd composites, including repeated prime
factors. It replaces the fixed polylogarithmic action cap in F182 and F183
by an arbitrary fixed numerical quasipolynomial cap. It is not an all-input
factoring algorithm.

Let

\[
N=\prod_{j=1}^s R_j,
\qquad
n=\lceil\log_2(N+1)\rceil,
\tag{1}
\]

be the hidden prime-power decomposition. Suppose F181 has returned a public
unit \(w_0\) whose local orders satisfy

\[
g_{0,j}=\operatorname{ord}_{R_j}(w_0)>1,
\qquad
\gcd(g_{0,j},N)=1,
\qquad
P^-(g_{0,j})>T.
\tag{2}
\]

Choose any two fixed integer-valued numerical quasipolynomial bounds
\(K=K(n)\ge1\) and \(M=M(n)\ge1\). Put

\[
D=1+\sum_{k=1}^K k
 =1+\frac{K(K+1)}2
\tag{3}
\]

and require the F181 roughness cap to satisfy

\[
T>1+M(D+1).
\tag{4}
\]

For stage \(t=0,\ldots,M-1\), use the block of \(D+1\) consecutive
positive integers

\[
\mathcal I_t=
\{2+t(D+1),\ldots,1+(t+1)(D+1)\,\}.
\tag{5}
\]

For every \(a\in\mathcal I_t\), define

\[
C_a=a\prod_{k=1}^K(a^k-1),
\qquad
z_{t,a}=w_t^{C_a^n}\bmod N,
\qquad
H_{t,a}=\gcd(z_{t,a}-1,N).
\tag{6}
\]

If \(1<H_{t,a}<N\), return that factor. Otherwise, at every stage there is
at least one \(a_t\in\mathcal I_t\) with

\[
H_{t,a_t}=1.
\tag{7}
\]

Choose the first such base and set

\[
w_{t+1}=z_{t,a_t}.
\tag{8}
\]

If no factor is returned, the final unit \(w_M\) has nontrivial local orders

\[
g_{M,j}=\operatorname{ord}_{R_j}(w_M)>1
\tag{9}
\]

that remain coprime to \(N\) and \(T\)-rough. Moreover, the selected public
bases \(a_0,\ldots,a_{M-1}\) are distinct, and for every rational prime
\(\ell\mid g_{M,j}\), every hidden component \(j\), and every selected
stage \(t\),

\[
\boxed{
\ell\nmid a_t,
\qquad
\operatorname{ord}_\ell(a_t)>K.
}
\tag{10}
\]

Thus F181 admits the deterministic QP transition

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\text{one rough descendant carrying }M
\text{ distinct public automorphisms of order }>K
\text{ on every surviving order prime}.}
\tag{11}
\]

No \(C_a\), resultant, or auxiliary annihilator is factored. The total bit
cost is uniform deterministic quasipolynomial in \(n\).

## Exact boundary

The theorem supplies simultaneous long action on the final prime support.
It does not prove that the selected actions generate independent quotient
directions. They may all lie in one large cyclic subgroup of
\((\mathbb Z/g_{M,j}\mathbb Z)^\times\). It therefore gives neither an
exact common order nor a factor in the surviving branch.
