# F180 V2 candidate — primary-period filtering closes synchronized two-shift extinction

## Status and scope

This is the self-contained repair of F180 V1. V1 omitted the definition of
the input-length parameter (n). The V1 files and failed blind reconstruction
remain frozen.

Let (N>1) be an odd composite and define

\[
n=\lceil\log_2(N+1)\rceil.
\tag{0}
\]

Write the hidden prime-power decomposition and local orders as

\[
N=\prod_{j=1}^sR_j,
\qquad
f_j=\operatorname{ord}_{R_j}(y),
\tag{1}
\]

where (y) is the public P160 unit and

\[
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T\ge n
\tag{2}
\]

for every hidden component. Here \(\sigma(f)\) is the largest prime-power
divisor of \(f\). Choose

\[
K=\lceil(\log_2(n+1))^c\rceil
\tag{3}
\]

for one fixed constant \(c\ge1\).

## 1. Exact primary filters

For \(\delta\in\{0,3\}\), define

\[
A_\delta=\prod_{k=1}^K\bigl((N+\delta)^k-1\bigr),
\qquad
z_\delta=y^{A_\delta^n}\bmod N,
\tag{4}
\]

and compute

\[
H_\delta=\gcd(z_\delta-1,N).
\tag{5}
\]

For every prime power \(\ell^a\parallel f_j\), the full \(\ell^a\) part
is deleted from the order of \(z_\delta\) exactly when

\[
\ell\nmid N+\delta
\quad\text{and}\quad
\operatorname{ord}_\ell(N+\delta)\le K.
\tag{6}
\]

Equivalently,

\[
\boxed{
\operatorname{ord}_{R_j}(z_\delta)
=
\prod_{\substack{\ell^a\parallel f_j\\
\ell\mid N+\delta\ \text{or}\
\operatorname{ord}_\ell(N+\delta)>K}}
\ell^a.
}
\tag{7}
\]

A proper \(H_\delta\) factors \(N\). If \(H_\delta=1\), every hidden
component retains at least one primary part in (7). If \(H_\delta=N\), all
the local orders in (7) are one.

For \(\delta=0\), equation (2) excludes the nonunit alternative. Hence

\[
H_0=1
\quad\Longrightarrow\quad
\boxed{
\operatorname{ord}_\ell(N)>K
\text{ for every prime }\ell
\text{ in every surviving local order.}}
\tag{8}
\]

## 2. Synchronized extinction closes exactly

Suppose

\[
H_0=H_3=N.
\tag{9}
\]

For \(1\le k,l\le K\), put

\[
R_{k,l}
=
\left|\operatorname{Res}_X
\bigl(X^k-1,(X+3)^l-1\bigr)\right|.
\tag{10}
\]

Every \(R_{k,l}\) is nonzero and

\[
\log_2R_{k,l}<k(2l+1)=O(K^2).
\tag{11}
\]

Let

\[
M=\left(\prod_{k=1}^K\prod_{l=1}^K R_{k,l}\right)^n.
\tag{12}
\]

Then

\[
\boxed{f_j\mid M\qquad(1\le j\le s).}
\tag{13}
\]

All resultants, and hence \(M\), can be factored completely by trial
division in QP time. Factor-first order stripping from \(M\) either factors
\(N\), or recovers one exact common order \(m=f_j>T\ge n\) and the state
\((y,m)\).

## 3. Final trichotomy

Run the \(\delta=0\) filter first. On \(H_0=N\), run the \(\delta=3\)
filter. The procedure returns exactly one of

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }n
\quad\lor\quad
\text{a primary-period-hard descendant.}
}
\tag{14}
\]

The last branch is one of the following.

1. \(H_0=1\), and (8) holds for \(z_0\).
2. \(H_0=N\) and \(H_3=1\). Every prime in an original \(f_j\) has
   (N)-action period at most \(K\), while every prime in the surviving
   order of \(z_3\) either divides \(N+3\) or has \((N+3)\)-action period
   above \(K\).

Thus synchronized extinction is no longer an escape. The only remaining
branch contains a nontrivial primary component with a genuinely long or
nonunit public action.

## 4. Complexity and exact boundary

Each \(A_\delta^n\) has \(O(n^2K^2)\) bits. There are \(K^2\)
resultants, each with \(O(K^2)\) bits. Exact resultant computation, trial
division, modular exponentiation, gcds, and factor-first stripping have total

\[
2^{O(K^2)}=2^{(\log n)^{O(1)}}
\]

bit cost.

F180 does not force either filtered descendant to vanish. It does not turn
the primary-period-hard branch into a factor, and it does not prove QP
integer factoring.
