# F136 statement — linear anchor cutoff and wide-or-release law

## Status and material change

This is a proof-only candidate. It is not a parity-closure theorem or an
integer-factoring algorithm.

The closest prior results are P121, P122, and F135. P121 uses the safe cutoff
\(B=n^3\) and forces polynomial row multiplicity. P122 proves that the fresh
large rows of one star do not overlap. F135 proves that direct endpoint
recursion is inert and gives a release-or-wide-star boundary.

The material change is scale. The same elementary primorial method already
works at the linear cutoff

\[
B=\lceil12n\rceil.
\]

This covers every block \(q<N/B\) and every odd row at a prime \(r>B\).
On the no-release branch it still forces \(\Omega(n/\log n)\) distinct carry
digits.

## Definitions and algorithmic conventions

For a unit \(c\in\{1,\ldots,N-1\}\), let
\(\iota_N(c)\in\{1,\ldots,N-1\}\) be its least positive inverse and put

\[
P_N(c)=c\iota_N(c).
\]

A **unit block** is a positive integer below \(N\) and coprime to \(N\).
For every generated residue, the source runs

\[
\gcd(c-\iota_N(c),N),
\qquad
\gcd(c+\iota_N(c),N)
\]

before it stores the endpoint presentation
\((c,\iota_N(c))\). It keeps the first occurrence of every distinct exact
integer \(P_N(c)\).

Complete gcd-free refinement means the public deterministic operation that
refines all stored integer endpoints into pairwise-coprime blocks with exact
nonnegative exponent presentations. In particular, storing both \(q\) and
\(\ell q\), with prime \(\ell\nmid q\), names the block \(\ell\) and its
full exponent in every stored endpoint. A parity row for a rational prime
\(r\) records \(v_r(P_N(c))\bmod2\). The degree of that row is the number of
retained distinct exact values in which this parity is one. These definitions
state the mathematical objects used below; no factor of \(N\) is supplied.

## Setup

Put

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
B=\lceil12n\rceil.
\]

Let \(q\) be a unit block with

\[
1<q<\frac NB,
\qquad
w=\iota_N(q).
\]

For each eligible prime

\[
\ell\le B,
\qquad
\ell\nmid Nq,
\]

let \(A_\ell\in\{0,\ldots,\ell-1\}\) be the unique digit with

\[
w+NA_\ell\equiv0\pmod\ell.
\]

Put

\[
H_A=w+NA
\]

for each occupied digit \(A\), and define

\[
G_B(N,q)=
\prod_{\substack{\ell\le B\ {\rm prime}\\\ell\nmid Nq}}\ell.
\]

## Theorem 1 — elementary linear-scale primorial bound

For every real \(x\ge2^{18}\),

\[
\boxed{
\vartheta(x)=\sum_{\ell\le x\ {\rm prime}}\log\ell
>\frac6{25}x.
}
\tag{1}
\]

The proof uses only the central binomial coefficient, the least common
multiple of \(1,\ldots,\lfloor x\rfloor\), and elementary estimates for
prime powers. It does not use the prime number theorem.

Consequently, for every \(n\ge21846\),

\[
\prod_{\ell\le B\ {\rm prime}}\ell>N^4.
\tag{2}
\]

Inputs below this fixed bit-length threshold can be handled by a fixed finite
trial-division preprocessing step.

## Theorem 2 — linear-cutoff row reuse

For \(n\ge21846\),

\[
\boxed{
G_B(N,q)>N^2B.
}
\tag{3}
\]

Let \(r>B\) be prime with \(v_r(q)\) odd. Process the unary value \(P_N(q)\)
and every eligible anchored value

\[
P_N(\ell q)=q(w+NA_\ell).
\]

Then either a declared gcd screen already returns a factor, or the globally
deduplicated parity matrix contains at least two distinct exact values with
odd \(r\)-valuation:

\[
\boxed{\deg(r)\ge2.}
\tag{4}
\]

Thus every odd prime row larger than \(12n+1\) inside every unit block
smaller than \(N/(12n+1)\) is forced to lose privacy.

## Theorem 3 — linear-scale release or width

For each occupied digit \(A\), let

\[
\mathcal L_A=\{\ell:A_\ell=A\},
\qquad
L_A=\prod_{\ell\in\mathcal L_A}\ell.
\]

Use the empty-product convention \(L_A=1\) when \(\mathcal L_A\) is empty.

Retain every endpoint presentation before exact-value deletion and run
complete gcd-free refinement.

If

\[
A=0,\qquad L_0>B,
\]

then removing the full named anchor-prime powers from \(H_0=w\) leaves only
residual blocks smaller than \(N/B\), or no residual block.

If

\[
A>0,\qquad L_A>B^2,
\]

then the same conclusion holds for \(H_A=w+NA\).

For the width conclusion below, assume \(n\ge21846\) and that no occupied
bucket meets either release threshold:

\[
L_0\le B,
\qquad
L_A\le B^2\quad(A>0).
\tag{5}
\]

Let \(d\) be the number of occupied nonzero digits. Then

\[
\boxed{
d>
\frac{37n}{50\log(13n)}.
}
\tag{6}
\]

Here and only here, \(\log\) is natural. For a fixed prime \(r>B\) occurring
oddly in \(q\), at most one of these digits can have odd \(r\)-valuation in
\(H_A\). Hence, unless a declared screen has already factored \(N\), at least
\(d-1\) distinct retained exact values have odd \(r\)-valuation.

The exact trichotomy is therefore

\[
\boxed{
\text{an }H_A\text{-side residual block below }N/B,
\quad\text{residual exhaustion, or}\quad
\Omega(n/\log n)\text{ reused-row columns}.
}
\tag{7}
\]

## Theorem 4 — conditional quasipolynomial composition

Assume an adaptive all-block source with the following explicit imported
guarantee. With

\[
L=\lceil\log_2(n+1)\rceil,\qquad
E=2^{L^2},\qquad
T=L^2,
\]

it processes every current block against every integer anchor through \(E\)
for \(T\) frozen rounds, retains endpoints before exact-value deduplication,
and performs its complete refinements and final parity decode in deterministic
bit complexity

\[
\boxed{2^{O((\log n)^4)}}.
\tag{8}
\]

For every \(n\ge21846\), one has \(B<E\). Therefore every F136 anchor
position is a literal subposition of this assumed source. Marking and using
the linear subbank adds no source position and does not change (8). Inputs
below the fixed threshold can use ordinary finite trial division.

Theorem 4 is a conditional composition corollary. Theorems 1--3 do not
depend on this imported source guarantee.

## Exact consequence and remaining gap

The positive row-reuse region is much larger than in P121. Outside a fixed
finite input range, every small block \(q<N/(12n+1)\) has this dichotomy:

1. its squarefree kernel is \(B\)-smooth; or
2. every odd row above \(B\) is forced to reappear.

This still does not force a binary kernel. P122 permits the fresh large arm
rows to remain disjoint, and F135 gives an expanding-forest incidence model
of quasipolynomial size with zero kernel. A complete proof must use arithmetic
that forbids that forest, or it must close the residual rows by old,
same-digit, cross-star, wrapped, powered, or multi-block relations.
