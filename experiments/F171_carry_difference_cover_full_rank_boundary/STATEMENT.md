# F171 candidate — complete small-carry coverage can coexist with full rank

## Status

This is a proof-only candidate. No hostile audit, statement-only blind
reconstruction, cross-family audit, human audit, or publication-level
literature audit has run.

This result gives a selected canonical-inverse source obstruction. It does
not control the complete static source or any later adaptive source. It is
not a factoring lower bound and is not a factoring algorithm.

## Exact carry gate

Let \(N\) be odd. For a canonical inverse pair write

\[
P_k=1+kN=c\,\iota_N(c).
\]

For every prime \(r\nmid N\), put

\[
a_r=-N^{-1}\pmod r,
\qquad 1\le a_r<r.
\]

Then

\[
r\mid P_k
\quad\Longleftrightarrow\quad
k\equiv a_r\pmod r.
\]

Thus a numerical difference cover only proves that some residue class is
repeated. Row reuse requires two carries in the specific class \(a_r\), and
odd row reuse also requires odd \(r\)-adic valuation in both values.

## Full-rank carry-cover theorem

There is an infinite family of odd distinct-prime semiprimes \(N\), with

\[
n=\lceil\log_2(N+1)\rceil,
\]

and integers \(R\to\infty\), for which a selected bank of

\[
m=4R=\Theta\!\left(\frac{n}{\log n}\right)
\]

canonical inverse relations has all of the following properties.

1. The carries are exactly

   \[
   1,2,\ldots,m.
   \]

2. Every canonical first endpoint is a public prime \(g_k\le n\). Every
   exact value is

   \[
   P_k=g_k\iota_N(g_k)=1+kN,
   \qquad 1\le k\le m.
   \]

3. Every selected endpoint sign screen is null:

   \[
   \gcd(g_k-\iota_N(g_k),N)
   =\gcd(g_k+\iota_N(g_k),N)=1.
   \]

4. For every rational prime \(r\le R\), at least two distinct selected
   columns satisfy

   \[
   v_r(P_k)=1.
   \]

   This is stronger than a difference cover. It hits the unique occupied
   carry class and fixes valuation parity.

5. Every selected column \(P_k\) has its own endpoint prime \(g_k>m\) as a
   private row, with

   \[
   v_{g_k}(P_k)=1,
   \qquad
   g_k\nmid P_j\quad(j\ne k).
   \]

   The \(g_k\)-rows form an \(m\)-by-\(m\) identity submatrix. Hence the
   complete selected parity matrix has column rank \(m\) and zero kernel.
   Each private row exceeds the full carry diameter, so no nonzero selected
   carry difference can be divisible by it.

6. Both hidden prime factors exceed \(n^2\) for all sufficiently large
   family members. The inputs are trial-hard and are not perfect powers.
   No claim of \(p<q<2p\) is made.

Consequently, the restriction to rows \(r\le R\) has many formal
dependencies,

\[
\dim\ker M_{\le R}\ge m-\pi(R),
\]

while the full selected matrix satisfies

\[
\ker M=0.
\]

Complete small-row coverage therefore does not imply a square-class cycle.
It cannot by itself imply a non-global normalized root.

## Route consequence

Umans--Wang-style difference covers can compress a search for divisibility
of carry differences. They do not supply the occupied carry class, odd
valuation, final rank defect, or non-global root. In the quasipolynomial
model, a quadratic scan of a quasipolynomial explicit carry list is still
quasipolynomial, and P152 already batch-locates existing signed inverse
collisions. The missing result remains a source theorem, not a locator.

The construction does not exclude a richer complete grammar from appending
columns that reuse the private \(g_k\)-rows. Such a theorem must analyze the
complete generated source and then pass the P138 normalized-root gate.
Small carry-row coverage also has no stated implication for the P154
quotient-fingerprint group.
