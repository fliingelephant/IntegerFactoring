# F179 candidate — two short exponent-action periods close through a small resultant

## Status and scope

This is a proof-only constructive postprocessor for the hard branch of F178.
It applies to arbitrary odd composites. It is not an all-input factoring
algorithm.

Let

\[
N=\prod_{j=1}^s R_j
\tag{1}
\]

be the hidden prime-power decomposition. Let \(y\in(\mathbb Z/N\mathbb
Z)^\times\) be public, and put

\[
f_j=\operatorname{ord}_{R_j}(y).
\tag{2}
\]

Assume the F178 hard-branch guarantees

\[
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T\ge n
\tag{3}
\]

for every \(j\). Choose

\[
K=\lceil(\log_2(n+1))^c\rceil
\tag{4}
\]

for one fixed constant \(c\ge1\).

## 1. Two public action scans

For \(\delta\in\{0,3\}\) and \(1\le k\le K\), compute

\[
D_{\delta,k}=\gcd\!\left(y^{(N+\delta)^k-1}-1,N\right).
\tag{5}
\]

A proper gcd factors \(N\). Otherwise, each scan either has a first global
return \(D_{s,k}=N\), or every displayed gcd in that scan equals one.

If the \(\delta=0\) scan has no global return, then

\[
\boxed{\operatorname{ord}_{f_j}(N)>K\qquad(1\le j\le s).}
\tag{6}
\]

If the \(\delta=3\) scan has no global return, then for every \(j\), either

\[
\gcd(N+3,f_j)>1
\tag{7}
\]

or

\[
\operatorname{ord}_{f_j}(N+3)>K.
\tag{8}
\]

## 2. Two global returns force exact closure

Suppose both scans have global returns at \(a,b\le K\). Define

\[
P(X)=X^a-1,
\qquad
Q(X)=(X+3)^b-1,
\tag{9}
\]

and the integer

\[
R=\left|\operatorname{Res}_X(P,Q)\right|.
\tag{10}
\]

Then

\[
\boxed{f_j\mid R\qquad(1\le j\le s).}
\tag{11}
\]

The resultant is nonzero and satisfies

\[
\boxed{\log_2 R<a(2b+1)=O(K^2).}
\tag{12}
\]

Therefore trial division completely factors \(R\) in

\[
2^{O(K^2)}=2^{(\log n)^{O(1)}}
\tag{13}
\]

bit operations. Factor-first order stripping from this known annihilator
either factors \(N\), or certifies one exact common order

\[
m=f_j\qquad(1\le j\le s).
\tag{14}
\]

Equation (3) gives \(m>T\ge n\), so \((y,m)\) is a factored exact
common-order state above the input length.

## 3. Final trichotomy

The two-shift procedure returns exactly one of

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }n
\quad\lor\quad
\text{a certified long or nonunit shift action}.
}
\tag{15}
\]

The last branch means (6), or the componentwise alternative (7)--(8). Thus
two short action periods cannot remain hidden behind the unfactored large
annihilators \(N^a-1\) and \((N+3)^b-1\).

## 4. Exact boundary

F179 does not force either shift to have a short period. It does not turn a
long period, or the nonunit relation in (7), into a factor. It therefore does
not complete the F178 hard branch or prove QP integer factoring.
