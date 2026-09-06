# F186 candidate — one-child sequential support peeling

## Status and scope

This is a proof-only strengthening of the promoted P162/F185 recursive
cross-resultant transition. It applies to arbitrary odd composites, including
prime powers and repeated prime factors. It is not an all-input factoring
algorithm.

The new point is recursive cost. A QP list of smaller support-covering
integers need not create one recursive child per list entry. Sequential
exponent filtering selects at most one entry for recursive factorization.
That child may lose only one input bit.

## 1. General one-child peeling theorem

Let

\[
N=\prod_{j=1}^s R_j,
\qquad
n=\left\lceil\log_2(N+1)\right\rceil,
\tag{1}
\]

be the hidden decomposition into pairwise coprime prime powers. Let \(w\) be
a public unit whose local orders satisfy

\[
g_j=\operatorname{ord}_{R_j}(w)>1,
\qquad
\gcd(g_j,N)=1,
\qquad
P^-(g_j)>T
\tag{2}
\]

for every \(j\), where \(T\ge2\).

Suppose a deterministic public procedure constructs an ordered list

\[
A_1,\ldots,A_B\in\mathbb Z_{>0}
\tag{3}
\]

with these properties:

1. \(B\) and the total construction cost are numerical QP in \(n\);
2. every \(A_i>1\) has
   \[
   \operatorname{bitlen}(A_i)\le n-1;
   \tag{4}
   \]
3. the list covers every rational prime in every local order:
   \[
   \ell\mid g_j
   \quad\Longrightarrow\quad
   \ell\mid A_i\text{ for some }i.
   \tag{5}
   \]

Set \(v_0=w\). Process the list in order. Values \(A_i=1\) are skipped.
For every remaining value, first compute \(\gcd(A_i,N)\). A proper gcd is a
factor. On the no-factor branch compute

\[
v_i=v_{i-1}^{A_i^n}\bmod N,
\qquad
H_i=\gcd(v_i-1,N).
\tag{6}
\]

If \(1<H_i<N\), return the factor. If \(H_i=1\), retain \(v_i\) and
continue. At the first index for which \(H_i=N\), recursively factor the
single integer \(A_i\). Use the resulting complete factorization of
\(A_i^n\) to run factor-first order stripping on \(v_{i-1}\).

The process must reach such an index, unless it returned a factor earlier.
It returns exactly one of

\[
\boxed{
\text{proper factor of }N
\quad\lor\quad
\text{one fully factored exact common local order }m>T.}
\tag{7}
\]

There is at most one recursive child. Its bit length is at most \(n-1\).
If this is the only recursive call made by the enclosing complete procedure,
and its nonrecursive work is bounded by a nondecreasing numerical-QP
function \(Q(n)\), then

\[
\mathcal T(n)
\le \mathcal T(n-1)+Q(n)
\le nQ(n)
=2^{(\log n)^{O(1)}}.
\tag{8}
\]

The theorem makes no claim when the enclosing procedure creates additional
recursive children whose total recursion-tree volume is not QP.

## 2. Cross-resultant corollary

Use the P162/F185 setup with two separated menus

\[
\mathcal A=\{0,1,\ldots,L-1\},
\qquad
\mathcal B=\{L+2,L+3,\ldots,2L+1\},
\tag{9}
\]

and

\[
F_{\delta,0}(X)=X+\delta,
\qquad
F_{\delta,k}(X)=(X+\delta)^k-1
\quad(1\le k\le K).
\tag{10}
\]

Put

\[
\lambda=\left\lceil\log_2(2L+2)\right\rceil
\tag{11}
\]

and replace F185's fixed-ratio contraction by the weaker one-bit condition

\[
\boxed{K(1+K\lambda)\le n-1.}
\tag{12}
\]

When both menu filters are globally extinct on the same P161 unit, list all
positive cross-resultants

\[
A_i=\left|\operatorname{Res}_X
\bigl(F_{\delta,k},F_{\epsilon,l}\bigr)\right|,
\qquad
\delta\in\mathcal A,
\quad
\epsilon\in\mathcal B,
\quad
0\le k,l\le K,
\tag{13}
\]

in public lexicographic order. Every value is nonzero, every value has at
most \(n-1\) bits, and the list covers every rational prime in every local
order. Applying the general theorem therefore resolves double extinction
with at most one recursive call.

The exact output remains

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\text{fully factored exact common order above }T
\quad\lor\quad
\text{one wide-shift-hard rough descendant}.}
\tag{14}
\]

F186 improves the recursive interface and removes F185's many-child
requirement. It does not close the wide-shift-hard descendant, does not force
a useful non-global root, and does not by itself give a complete factoring
algorithm.
