# F181 candidate — the coprime local orders can be made rough

## Status and scope

This is a proof-only constructive postprocessor for the promoted P160 hard
branch. It applies to arbitrary odd composites, including repeated prime
factors. It strengthens P160's large-primary conclusion to the absence of
all small prime support. It is not an all-input factoring algorithm.

Let

\[
N=\prod_{j=1}^s R_j,
\qquad
n=\lceil\log_2(N+1)\rceil,
\tag{1}
\]

be the hidden prime-power decomposition. Suppose P160 has returned a public
unit \(y\) with local orders

\[
f_j=\operatorname{ord}_{R_j}(y)
\tag{2}
\]

such that

\[
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T
\tag{3}
\]

for every \(j\). Here \(T\ge2\) is any fixed integer-valued numerical
quasipolynomial bound in \(n\), and \(\sigma(f)\) is the largest prime-power
divisor of \(f\).

Construct, together with its complete factorization,

\[
\Lambda_T=\operatorname{lcm}(1,\ldots,T),
\qquad
Q=\Lambda_T^n,
\qquad
w=y^Q\bmod N,
\tag{4}
\]

and compute

\[
H=\gcd(w-1,N).
\tag{5}
\]

For every hidden component, define

\[
g_j=\prod_{\substack{\ell^a\parallel f_j\\ \ell>T}}\ell^a.
\tag{6}
\]

Then

\[
\boxed{\operatorname{ord}_{R_j}(w)=g_j.}
\tag{7}
\]

The procedure returns exactly one of the following outcomes.

1. **Factor.** If \(1<H<N\), then \(H\) is a proper factor of \(N\).
2. **Exact common-order state.** If \(H=N\), factor-first stripping from
   the fully factored annihilator \(Q\) either returns a proper factor, or
   proves that \(y\) has one exact common local order
   \[
   m=f_j>T
   \qquad(1\le j\le s).
   \tag{8}
   \]
3. **Rough descendant.** If \(H=1\), then every local order of \(w\)
   satisfies
   \[
   \boxed{
   g_j>T,
   \qquad
   \gcd(g_j,N)=1,
   \qquad
   P^-(g_j)>T,
   }
   \tag{9}
   \]
   where \(P^-(g)\) is the least prime divisor of \(g\).

Thus P160's final branch can be replaced by

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }T
\quad\lor\quad
\text{a public unit with nontrivial }T\text{-rough local orders}.
}
\tag{10}
\]

All construction, modular powering, gcd, and factor-first work has uniform
deterministic quasipolynomial bit cost.

## Separate corollary: remove F180's nonunit alternative

Let \(w\) be the rough descendant in (9), and let

\[
K=\lceil(\log_2(n+1))^c\rceil
\tag{11}
\]

for one fixed constant \(c\ge1\). Define

\[
A_0=\prod_{k=1}^K(N^k-1),
\qquad
B_3=(N+3)\prod_{k=1}^K((N+3)^k-1).
\tag{12}
\]

The powers \(w^{A_0^n}\) and \(w^{B_3^n}\) give the F180 two-shift
trichotomy with a stronger last branch: every prime in the surviving local
order is a unit for the relevant public base and has multiplicative order
above \(K\). The shift-three nonunit alternative is deleted by the explicit
factor \(N+3\) in \(B_3\).

If both filters return the identity globally, every order prime divides one
of the following nonzero integers:

\[
S_k=3^k-(-1)^k
\qquad(1\le k\le K)
\tag{13}
\]

or

\[
R_{k,l}=
\left|\operatorname{Res}_X
\bigl(X^k-1,(X+3)^l-1\bigr)\right|
\qquad(1\le k,l\le K).
\tag{14}
\]

Factoring these integers by trial division and raising their product to the
\(n\)-th power gives a fully factored quasipolynomial-size annihilator.
Factor-first stripping then returns a factor or an exact common-order state
above \(T\). This corollary removes only the nonunit escape. It does not
force the remaining long-action branch to factor.
