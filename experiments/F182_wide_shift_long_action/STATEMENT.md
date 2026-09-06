# F182 candidate — two QP shift menus force one wide long-action descendant

## Status and scope

This is a proof-only constructive postprocessor for the F181 rough-order
branch. It applies to arbitrary odd composites, including repeated prime
factors. It strengthens F180 from one hard public action to a whole
quasipolynomial-size menu of hard public actions. It is not an all-input
factoring algorithm.

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

Use the two disjoint shift menus

\[
\mathcal A=\{0,1,\ldots,L-1\},
\qquad
\mathcal B=\{L+2,L+3,\ldots,2L+1\}.
\tag{4}
\]

Every cross-menu gap is between \(3\) and \(2L+1\). Require the F181
roughness cap to satisfy

\[
T\ge
\widehat T:=
2^{K(2+K\lceil\log_2(2L+2)\rceil)}.
\tag{5}
\]

This is still one fixed numerical quasipolynomial bound in \(n\).

For every shift \(\delta\), define

\[
C_\delta=(N+\delta)
\prod_{k=1}^K\bigl((N+\delta)^k-1\bigr).
\tag{6}
\]

For \(\mathcal S\in\{\mathcal A,\mathcal B\}\), put

\[
P_\mathcal S=\prod_{\delta\in\mathcal S}C_\delta,
\qquad
z_\mathcal S=w^{P_\mathcal S^n}\bmod N,
\qquad
H_\mathcal S=\gcd(z_\mathcal S-1,N).
\tag{7}
\]

Both menu filters act on the same original F181 unit \(w\). The second
filter does not act on \(z_\mathcal A\).

Run the \(\mathcal A\) filter. A proper \(H_\mathcal A\) factors \(N\).
If \(H_\mathcal A=1\), return \(z_\mathcal A\). Only if
\(H_\mathcal A=N\), run the \(\mathcal B\) filter. A proper
\(H_\mathcal B\) factors \(N\), and otherwise

\[
\boxed{H_\mathcal B=1.}
\tag{8}
\]

Thus the procedure returns exactly one of

\[
\boxed{
\text{a proper factor of }N
\quad\lor\quad
\text{a public wide-shift-hard descendant }z_\mathcal S.
}
\tag{9}
\]

For the returned menu \(\mathcal S\), every hidden local order is
nontrivial and \(T\)-rough. Moreover, for every prime \(\ell\) in every
local order of \(z_\mathcal S\), and for every
\(\delta\in\mathcal S\),

\[
\boxed{
\ell\nmid N+\delta,
\qquad
\operatorname{ord}_\ell(N+\delta)>K.
}
\tag{10}
\]

The encoded exponents have

\[
O\bigl(nLK^2(n+\log L)\bigr)
\tag{11}
\]

bits. The construction, two modular powers, and gcds have uniform
deterministic quasipolynomial bit cost.

## Exact boundary

F182 removes synchronized extinction for two whole QP shift menus. It does
not localize a prime divisor of a rough local order that has long public
action for every shift in the returned menu. No QP factoring theorem is
claimed.
