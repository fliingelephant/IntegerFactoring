# F126 proof and algorithmic corollary

Write

\[
d=\beta-\alpha,
\qquad
e=\alpha\beta-1.
\]

For the four rows of \(L\), form

\[
S=-dR_{00}+eR_{10}-eR_{01}+dR_{11}.
\]

Modulo \(N\), its first entry is zero. Since
\(x_{ij}\equiv u\alpha^i\beta^j\), its second entry is

\[
u[-d+e\alpha-e\beta+d\alpha\beta]=0.
\]

Since \(y_{ij}\equiv u^{-1}\alpha^{-i}\beta^{-j}\), multiplication of
the third entry by the unit \(u\alpha\beta\) gives

\[
-d\alpha\beta+e\beta-e\alpha+d=0.
\]

The last entry is \(\Omega_{\square}\). Thus

\[
S\equiv(0,0,0,\Omega_{\square})\pmod N.
\]

Replacing the last row by \(S\) multiplies the determinant by \(d\). Expansion
along the last row gives

\[
d\det L\equiv\Omega_{\square}D\pmod N,
\]

where

\[
D=\det
\begin{pmatrix}
1&u&u^{-1}\\
1&u\alpha&(u\alpha)^{-1}\\
1&u\beta&(u\beta)^{-1}
\end{pmatrix}
={(\alpha-1)(\beta-1)(\beta-\alpha)\over\alpha\beta}.
\]

The last equality is the three-point Vandermonde determinant after cancelling
the column scales \(u\) and \(u^{-1}\). Since \(d=\beta-\alpha\) is a unit,
cancel it to obtain

\[
\det L\equiv
{(\alpha-1)(\beta-1)\over\alpha\beta}
\Omega_{\square}\pmod N.
\]

The remaining multiplier is a unit under the stated hypothesis. Congruence
and multiplication by a unit preserve a gcd with \(N\), proving the theorem.

## F123 specialization

Take \(u=\alpha=t\) and \(\beta=[t^2]_N\). The four vertices are the
canonical residues of \(t,t^2,t^3,t^4\). If their carries are
\(\kappa_1,\ldots,\kappa_4\), then

\[
\Omega_{\square}\equiv
t(t-1)
\left[
\kappa_4-\kappa_1+
(1+t+t^{-1})(\kappa_2-\kappa_3)
\right]
\pmod N.
\]

The bracket is the F123 residual because the first canonical inverse is
congruent to \(t^{-1}\). The F123 unit condition
\(\gcd(t(t^2-1),N)=1\) supplies all rectangle unit conditions. Thus F123 is
the consecutive-power slice of F126.

## Quasipolynomial rectangle closure

Let a public F26-Q word menu contain

\[
Q=2^{O((\log n)^2)}
\]

distinct canonical residues. For every ordered triple
\((u,\alpha,\beta)\) from this menu, compute the four canonical rectangle
vertices and their carries. This is at most \(Q^3\) triples and remains
quasipolynomial.

Test \(u,\alpha,\beta,\alpha-1,\beta-1\), and \(\beta-\alpha\) separately
against \(N\). A proper gcd is already success. A global degeneracy skips the
triple. For each eligible triple, compute \(\Omega_{\square}\) and its gcd
with \(N\).

Run this before exact-value deduplication. Keep canonical residues with
\(P(c)=1\). Different residues with the same exact value can occupy different
matrix rows, so P66 exact-value deduplication is not valid for this decoder.

This is a deterministic quasipolynomial extension of F26-Q. It gives no
theorem that one rectangle has asymmetric local rank.
