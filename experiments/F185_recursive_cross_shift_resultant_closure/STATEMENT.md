# F185 candidate — fixed-contraction recursive cross-shift closure

## Status and scope

This is a proof-only candidate postprocessor for the promoted P161
rough-order branch. It applies to arbitrary odd composites, including prime
powers and repeated prime factors. It is not an all-input factoring
algorithm.

Let

\[
N=\prod_{j=1}^sR_j,
\qquad
n=\left\lceil\log_2(N+1)\right\rceil,
\tag{1}
\]

be the hidden decomposition into pairwise coprime prime powers. Suppose P161
has returned a public unit \(w\) with local orders

\[
g_j=\operatorname{ord}_{R_j}(w)>1,
\qquad
\gcd(g_j,N)=1,
\qquad
P^-(g_j)>T
\tag{2}
\]

for every \(j\), where \(T\ge2\) is a fixed numerical quasipolynomial
roughness cap.

F185 uses strong induction only in its double-extinction branch: every
positive auxiliary integer strictly below \(N\) may be sent to the same
complete factoring procedure on a smaller input. This is a recursive call,
not a free factoring oracle. The fixed bit contraction and the full recursive
cost are stated below.

## Exact parameter range

Fix one constant

\[
0<\rho<1.
\tag{3}
\]

Let \(L=L(n)\ge1\) be integer-valued and numerical quasipolynomial, so for
fixed constants \(C_L>0\) and \(d_L\ge1\),

\[
L(n)\le
2^{C_L(\log_2(n+1))^{d_L}}.
\tag{4}
\]

Put

\[
\lambda=\left\lceil\log_2(2L+2)\right\rceil,
\qquad
m=\lfloor\rho n\rfloor.
\tag{5}
\]

Choose an integer \(K\ge1\) satisfying the exact contraction condition

\[
\boxed{K(1+K\lambda)\le m.}
\tag{6}
\]

Equivalently, the complete admissible range is

\[
1\le K\le
\left\lfloor
\frac{\sqrt{1+4\lambda m}-1}{2\lambda}
\right\rfloor.
\tag{7}
\]

The range is nonempty exactly when \(m\ge1+\lambda\). For every fixed
numerical-QP \(L\), it is nonempty for all sufficiently large \(n\), and
the largest admissible value satisfies

\[
K=\Theta\!\left(\sqrt{\frac{n}{\log_2(L+1)}}\right).
\tag{8}
\]

Inputs below the fixed threshold at which (7) becomes nonempty belong to a
finite recursion base; F185 makes no claim that (6) holds there.

## Two exact menu filters

Use the separated shift menus

\[
\mathcal A=\{0,1,\ldots,L-1\},
\qquad
\mathcal B=\{L+2,L+3,\ldots,2L+1\}.
\tag{9}
\]

For every shift \(\delta\), define

\[
C_\delta=(N+\delta)
\prod_{k=1}^K\bigl((N+\delta)^k-1\bigr).
\tag{10}
\]

For \(\mathcal S\in\{\mathcal A,\mathcal B\}\), put

\[
P_\mathcal S=\prod_{\delta\in\mathcal S}C_\delta,
\qquad
z_\mathcal S=w^{P_\mathcal S^n}\bmod N,
\qquad
H_\mathcal S=\gcd(z_\mathcal S-1,N).
\tag{11}
\]

Both filters act on the original unit \(w\). For each hidden component,

\[
\operatorname{ord}_{R_j}(z_\mathcal S)
=
\prod_{\substack{\ell^a\parallel g_j\\
\forall\delta\in\mathcal S:\ \ell\nmid N+\delta\\
\forall\delta\in\mathcal S:\ 
\operatorname{ord}_\ell(N+\delta)>K}}
\ell^a.
\tag{12}
\]

Thus the linear factor \(N+\delta\) deletes every nonunit case. The
multiplicative-order condition in (12) is read only after
\(\ell\nmid N+\delta\).

Run the \(\mathcal A\) filter first. Return a proper \(H_\mathcal A\), or
return \(z_\mathcal A\) if \(H_\mathcal A=1\). Only when
\(H_\mathcal A=N\), run the \(\mathcal B\) filter and apply the same two
tests. The remaining case is

\[
H_\mathcal A=H_\mathcal B=N.
\tag{13}
\]

## Recursive cross-resultant closure

For every shift and every \(0\le k\le K\), define

\[
F_{\delta,0}(X)=X+\delta,
\qquad
F_{\delta,k}(X)=(X+\delta)^k-1\quad(k\ge1).
\tag{14}
\]

For \(\delta\in\mathcal A\), \(\epsilon\in\mathcal B\), and
\(0\le k,l\le K\), put

\[
R_{\delta,\epsilon;k,l}
=\left|\operatorname{Res}_X
\bigl(F_{\delta,k},F_{\epsilon,l}\bigr)\right|.
\tag{15}
\]

Every such integer is positive and satisfies

\[
\boxed{
\operatorname{bitlen}(R_{\delta,\epsilon;k,l})
\le K(1+K\lambda)\le\lfloor\rho n\rfloor<n,
}
\tag{16}
\]

where \(\operatorname{bitlen}(q)=\lceil\log_2(q+1)\rceil\). Hence every
resultant greater than one is strictly below \(N\) and is a valid
fixed-contraction recursive input. A resultant equal to one is skipped; a
zero resultant never occurs.

In case (13), recursively factor all resultants greater than one. Merge the
returned prime factorizations and define the fully factored integer

\[
U=\prod_{\delta\in\mathcal A}
\prod_{\epsilon\in\mathcal B}
\prod_{k=0}^K\prod_{l=0}^K
R_{\delta,\epsilon;k,l},
\qquad
M=U^n.
\tag{17}
\]

Then

\[
\boxed{g_j\mid M\qquad(1\le j\le s).}
\tag{18}
\]

Factor-first stripping from \((w,M)\) returns a proper factor of \(N\), or
proves one exact common local order

\[
\boxed{g_j=q>T\qquad(1\le j\le s),}
\tag{19}
\]

together with the complete factorization of \(q\).

## Result and exact surviving branch

Under the strong-induction premise, F185 returns exactly one of

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\text{fully factored exact common order above }T
\quad\lor\quad
\text{one wide-shift-hard rough descendant}.}
\tag{20}
\]

For a returned descendant \(z_\mathcal S\), every hidden local order is
nontrivial, coprime to \(N\), and \(T\)-rough. For every prime \(\ell\) in
every such local order and every \(\delta\in\mathcal S\),

\[
\ell\nmid N+\delta,
\qquad
\operatorname{ord}_\ell(N+\delta)>K.
\tag{21}
\]

F185 does not close (21), so it is not a QP factoring theorem.

## Total recursive cost

There are at most

\[
B(n)=L(n)^2(K(n)+1)^2
\tag{22}
\]

recursive resultant calls at one node. All F185 work outside those calls is
bounded by one fixed numerical quasipolynomial \(A(n)\).

If the enclosing strong-induction procedure has no other recursive calls,
or its other calls satisfy the same call-count and contraction bounds, its
worst-case expected cost obeys

\[
\mathcal T(n)
\le A(n)+B(n)\mathcal T(\lfloor\rho n\rfloor)
\tag{23}
\]

above a fixed finite base. Since \(A\) and \(B\) are numerical QP and
\(\rho<1\) is fixed, (23) gives

\[
\boxed{
\mathcal T(n)=2^{(\log_2(n+1))^{O(1)}}.}
\tag{24}
\]

The same statement holds for deterministic cost. For Las Vegas recursive
calls, it holds in expectation and preserves almost-sure termination.
Merely requiring each auxiliary to be less than \(N\), without the fixed
contraction (16), does not imply (24).

## Narrow canonical-carry boundary

If canonical inverse representatives \(1\le x,y<N\) satisfy

\[
xy=1+cN,
\tag{25}
\]

then either \(c=0\) and \(x=y=1\), or

\[
0<c<\min(x,y)<N,
\qquad
\gcd(c,xy)=1.
\tag{26}
\]

Thus strong induction can factor a positive inverse carry, but none of its
prime factors divides either endpoint of that same inverse relation. This
is only a direct-endpoint boundary. It is not a claim that all nonlinear
uses of carry data are impossible.
