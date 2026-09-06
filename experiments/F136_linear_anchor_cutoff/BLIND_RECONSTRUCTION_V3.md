# F136 blind reconstruction V3

## Source identity and verdict

The only mathematical source consulted for this reconstruction was
`STATEMENT.md`.

- Expected SHA-256: `e17c70e87c87d0893814ffb503f636087e60a373e31e06659ef524d1f8561c49`
- Computed SHA-256: `e17c70e87c87d0893814ffb503f636087e60a373e31e06659ef524d1f8561c49`
- Verdict: **VALID**. Theorems 1--3 and the exact consequence follow from the
  stated definitions. Theorem 4 is valid exactly as a conditional composition
  corollary; it does not prove its imported source guarantee.

Throughout, `log` is natural logarithm. Since (n) is an integer,
(B=\lceil12n\rceil=12n). Also

\[
2^{n-1}<N+1\le 2^n,
\qquad N<2^n.
\tag{A}
\]

## Canonical anchored endpoints

Fix an eligible prime (ell\le B), put (A=A_\ell), and set

\[
z=\frac{H_A}{\ell}=\frac{w+NA}{\ell}.
\]

The digit definition makes (z) a positive integer. Eligibility gives
(gcd(\ell q,N)=1), and (q<N/B) gives (ell q<N). Moreover,
(0\le A\le\ell-1) and (w\le N-1), so

\[
0<z\le\frac{N-1+N(\ell-1)}{\ell}<N.
\]

Finally,

\[
(\ell q)z=q(w+NA)\equiv qw\equiv1\pmod N.
\]

Thus (z=\iota_N(\ell q)), not merely an inverse representative, and

\[
P_N(\ell q)=qH_A.
\tag{B}
\]

Distinct digits give distinct (H_A), hence distinct exact integers (qH_A).
The digit (A=0), if occupied, gives the unary exact value (qw); retaining
one copy under global exact-value deduplication is therefore the correct
counting convention.

## Theorem 1

Define the elementary Chebyshev function

\[
\psi(x)=\sum_{p^k\le x}\log p
=\log\operatorname{lcm}(1,\ldots,\lfloor x\rfloor).
\]

Let (m=\lfloor x/2\rfloor). For every prime (p), Legendre's formula gives

\[
v_p\binom{2m}{m}
=\sum_{j\ge1}
\left(\left\lfloor\frac{2m}{p^j}\right\rfloor
-2\left\lfloor\frac m{p^j}\right\rfloor\right).
\]

Each summand is zero or one, and there are at most
(\lfloor\log_p(2m)\rfloor) nonzero candidate summands. This is the exponent
of (p) in (operatorname{lcm}(1,\ldots,2m)). Hence
(inom{2m}{m}) divides that least common multiple. The central binomial
coefficient is at least the average of the (2m+1) coefficients in
((1+1)^{2m}), so

\[
\psi(x)\ge\psi(2m)
\ge\log\binom{2m}{m}
\ge2m\log2-\log(2m+1)
>(x-2)\log2-\log(x+1).
\tag{C}
\]

If (K=\lfloor\log_2x\rfloor), then

\[
\psi(x)-\vartheta(x)=\sum_{k=2}^{K}\vartheta(x^{1/k}).
\]

The elementary estimate
(artheta(y)\le y\log y) gives, for every (k\ge2),

\[
\vartheta(x^{1/k})
\le x^{1/k}\frac{\log x}{k}
\le\sqrt{x}\frac{\log x}{2}.
\]

As (K-1<\log x/\log2), (C) yields

\[
\frac{\vartheta(x)}x
>\log2-\frac{2\log2}{x}-\frac{\log(x+1)}x
-\frac{(\log x)^2}{2\log2\sqrt{x}}.
\tag{D}
\]

For (x\ge X=2^{18}), all three subtracted terms in (D) are bounded by
their values at (X). For the last term, this follows because
((\log x)^2/\sqrt{x}) is decreasing when (log x>4). The middle term is
also decreasing. Using the elementary bounds

\[
0.69<\log2<0.70,
\qquad \log(X+1)<13,
\qquad \sqrt X=512,
\]

the right side of (D) is larger than

\[
0.69-\frac{1.4}{262144}-\frac{13}{262144}
-\frac{12.6^2}{1.38\cdot512}
>0.464>\frac6{25}.
\]

This proves (1) for every real (x\ge2^{18}), with substantial slack.

If (n\ge21846), then (B=12n\ge262152>2^{18}), and therefore

\[
\vartheta(B)>\frac6{25}(12n)=\frac{72}{25}n.
\]

Since (log2<7/10), (72/25>4\log2). Consequently,

\[
\prod_{\ell\le B\ {m prime}}\ell
=e^{\vartheta(B)}>e^{4n\log2}=2^{4n}>N^4,
\]

which proves (2) with the claimed threshold.

## Theorem 2

Let

\[
Q_B=\prod_{\ell\le B\ {m prime}}\ell,
\qquad
D=\prod_{\substack{\ell\le B\ {m prime}\\ \ell\mid Nq}}\ell.
\]

Then (Q_B=D G_B(N,q)), while

\[
D\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{B}.
\]

Combining this with (2) gives

\[
G_B(N,q)=\frac{Q_B}{D}>N^2B,
\]

which is (3).

Let (S) be the set of occupied digits. Every prime in the bucket for (A)
divides (H_A), so (L_A\mid H_A). If (A>0) is occupied, then
(A\le B-1), and hence

\[
L_0\le H_0=w<N,
\qquad
L_A\le H_A=w+NA<NB.
\tag{E}
\]

The set ({0}\cup S) has at least three elements. Indeed, if there is no
occupied nonzero digit, then (G_B=L_0<N). If there is exactly one occupied
nonzero digit (A), with digit zero present or absent, (E) gives
(G_B\le L_0L_A<N^2B), where an absent zero bucket has (L_0=1). Both cases
contradict (3).

Now let (r>B) be prime with (v_r(q)) odd. Since (q) is a unit modulo
(N), (r\nmid N). If (r\mid H_A) and (r\mid H_C), then

\[
r\mid H_A-H_C=N(A-C).
\]

All candidate digits lie in ([0,B-1]). Thus (|A-C|<B<r), and (A=C).
At most one digit in ({0}\cup S) can therefore have positive
(r)-valuation. At least two distinct digits have (r)-valuation zero in
(H_A), so their exact values (qH_A) have odd (r)-valuation by (B).

If a declared gcd screen returns a nontrivial factor, that is the first
alternative. Otherwise the unary and anchored endpoints are stored. Global
deduplication can merge the anchored (A=0) presentation with the unary
presentation, but the indexing set ({0}\cup S) already counts that exact
integer only once. It cannot merge values from two different digits. Hence
at least two retained distinct exact values have odd (r)-valuation, proving
(4).

The prose versions with (q<N/(12n+1)) or primes larger than (12n+1) are
weaker subsets of the proved ranges (q<N/B) and (r>B=12n).

## Theorem 3

For an occupied digit (A), define the residual integer after removal of all
full named anchor-prime powers by

\[
R_A=\frac{H_A}
{\displaystyle\prod_{\ell\in\mathcal L_A}
\ell^{v_\ell(H_A)}}.
\tag{F}
\]

The endpoint pairs for (q) and (ell q) name each (ell) under the stated
complete gcd-free refinement convention, so (F) removes exactly the claimed
powers. Since (L_A\mid H_A),

\[
R_A\le\frac{H_A}{L_A}.
\]

For (A=0), (H_0=w<N), and (L_0>B) gives (R_0<N/B). For occupied
(A>0), the canonical-endpoint bound above gives (H_A<NB), and
(L_A>B^2) again gives (R_A<N/B). If (R_A=1), the residual is exhausted.
If (R_A>1), every pairwise-coprime block in its complete refinement divides
(R_A) and is therefore smaller than (N/B). This proves both release
claims, including their strict bounds and exhaustion cases.

For width, each eligible prime belongs to exactly one bucket, so

\[
G_B=L_0\prod_{\substack{A>0\\A\ {m occupied}}}L_A.
\tag{G}
\]

Under (5), (G) gives (G_B\le B^{2d+1}). Retain the stronger estimate used
before (3): Theorem 1, (D<N^2/B), and (N<2^n) give

\[
G_B=\frac{Q_B}{D}
>B\exp\left(\left(\frac{72}{25}-2\log2\right)n\right).
\tag{H}
\]

Combining (G)--(H) and taking logarithms yields

\[
d>
\frac{(36/25-\log2)n}{\log B}.
\]

Because (log2<7/10), (36/25-\log2>37/50). Also (B=12n<13n).
Therefore

\[
d>
\frac{37n}{50\log(13n)},
\]

which proves (6) with the stated constant.

For a fixed prime (r>B) occurring oddly in (q), the same difference
argument used in Theorem 2 shows that at most one occupied nonzero digit has
(r\mid H_A), and thus at most one can have odd (r)-valuation. The other
at least (d-1) exact values (qH_A) have odd (r)-valuation. They remain
distinct after global exact-value deduplication because their digits are
distinct.

Thus a bucket above a release threshold gives either a residual block below
(N/B) or residual exhaustion. If no bucket crosses a threshold, (6) gives
the wide branch and, for every fixed large odd row of (q), at least (d-1)
reused-row columns. This is precisely the scoped trichotomy (7).

## Theorem 4

Let (L=\lceil\log_2(n+1)\rceil). Then (n<2^L). At the stated threshold
(L\ge15), and in fact for every (L\ge3),

\[
B=12n<12\cdot2^L<2^{L^2}=E,
\]

because (12<2^{L^2-L}). Hence every prime anchor (ell\le B) used above
is among the integer anchors through (E).

Under the explicitly imported source guarantee, the relevant blocks and
anchors are already processed for the frozen rounds, endpoints are retained
before exact-value deduplication, and complete refinement and final decoding
are already included in the bound (2^{O((\log n)^4)}). Selecting the F136
positions adds no source position; its linear-size marking work is also
absorbed by that bound. Therefore the composition claim (8) is valid
conditional on that guarantee. Nothing in Theorems 1--3 uses it.

There are finitely many (N) with (n<21846). Trial division on that fixed
set has a fixed worst-case cost and does not change the asymptotic conditional
bound. This is a complexity-theoretic statement, not a practicality claim.

## Exact consequence

If (q<N/(12n+1)), then (q<N/B). Theorem 2 applies to every prime (r>B)
whose valuation in (q) is odd. Equivalently, either the parity squarefree
kernel of (q) is (B)-smooth, or every one of its odd rows above (B)
reappears in a second retained exact value. This proves the final dichotomy.
If "squarefree kernel" is instead read as the radical, the disjunction is
still valid: its second arm was proved for every odd row independently of the
smoothness of the radical.

No parity closure or factoring algorithm follows from these statements, and
none was used in this reconstruction.
