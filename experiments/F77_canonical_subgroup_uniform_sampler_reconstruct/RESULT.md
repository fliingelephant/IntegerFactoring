# PASS

The SHA-256 of `STATEMENT.md` is
`d07645a53bc3348d46a2addea066dae150f15ab285aa37dd8c12d40bf857882b`,
as required.

## 1. Public sampler

For analysis only, let

\[
r_j=\operatorname{ord}_N(q_j).
\]

The sampler does not need any (r_j). Since (q_j) is a unit,

\[
r_j\leq \varphi(N)\leq N-1<2^n.
\]

Consider one exponent modulo an integer (r\). Write (M=ar+b), where
(0\leq b<r). If (E) is uniform on \(\{0,\ldots,M-1\}\), then (E\bmod r)
gives (b) residues probability \((a+1)/M\) each and the other (r-b)
residues probability (a/M) each. Its total-variation distance from uniform
on \(\mathbb Z/r\mathbb Z\) is therefore

\[
\frac{b(r-b)}{Mr}\leq \frac r{4M}.
\]

Let (Y_j=E_j\bmod r_j), and let (U_j) be independent and uniform on
\(\mathbb Z/r_j\mathbb Z\). Total variation for product distributions is at
most the sum of the coordinate distances. Hence

\[
d_{\rm TV}\bigl((Y_j)_j,(U_j)_j\bigr)
 \leq \sum_{j=1}^s\frac{r_j}{4M}
 <\frac{s2^n}{4M}.
\]

The homomorphism

\[
\Phi:\prod_j\mathbb Z/r_j\mathbb Z\longrightarrow H,
\qquad
(e_j)_j\longmapsto\prod_j q_j^{e_j}
\]

is surjective. Every fiber of a surjective homomorphism of finite groups has
the same size. Thus Φ sends the uniform product distribution to the uniform
distribution on (H). A deterministic map cannot increase total variation.
Since

\[
M=2^{3n}2^{\lceil\log_2(s+1)\rceil}
 \geq 2^{3n}(s+1),
\]

the output distribution (P) satisfies

\[
d_{\rm TV}(P,U_H)
 < \frac{s}{4(s+1)}2^{-2n}
 <2^{-2n}.
\]

Each exponent is sampled with exactly (L) random bits. The random-bit cost
is

\[
sL=3sn+s\lceil\log_2(s+1)\rceil
  =O\bigl(s(n+\log s)\bigr)
\]

for (s\geq1). Binary modular exponentiation uses (O(sL)) modular
multiplications on (n)-bit values, plus (O(s)) product multiplications.
Standard integer multiplication and reduction therefore give bit complexity
polynomial in (s+n). The algorithm uses only (N,q_1,\ldots,q_s,n,s); it
does not compute an order, φ\((N)\), |H|, or the factorization of (N).

## 2. Exact density formulas

Use the Chinese remainder identification

\[
(\mathbb Z/N\mathbb Z)^\times
 \simeq \mathbb F_p^\times\times\mathbb F_q^\times.
\]

Let (A_p=\{x\in H:x_p=1\}) and define (A_q) similarly. The restricted
projection (H\to H_p) is surjective, so its kernel (A_p) has size
|H|/|H_p|. Consequently

\[
\Pr(A_p)=\frac1{|H_p|},\qquad
\Pr(A_q)=\frac1{|H_q|}.
\]

Their intersection contains only the identity, because both CRT coordinates
are (1). Thus \(\Pr(A_p\cap A_q)=1/|H|\). The gcd of (x-1) with (N=pq)
is nontrivial and proper exactly when one, but not both, of the two coordinates
is (1). The positive success set is (A_p\mathbin\triangle A_q), and

\[
\delta_+
=\Pr(A_p)+\Pr(A_q)-2\Pr(A_p\cap A_q)
=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|}.
\]

Now let (B_p=\{x\in H:x_p=-1\}). This set is empty if \(-1\notin H_p\).
If \(-1\in H_p\), it is a coset of the kernel of (H\to H_p), so it has
size |H|/|H_p|. Therefore

\[
\Pr(B_p)=\frac{\epsilon_p}{|H_p|},\qquad
\Pr(B_q)=\frac{\epsilon_q}{|H_q|}.
\]

The intersection (B_p\cap B_q) is the single CRT element ((-1,-1)) if
that element lies in (H), and is empty otherwise. Hence its probability is
ε/|H|. The gcd of (x+1) with (N) is nontrivial and proper exactly
on (B_p\mathbin\triangle B_q). It follows that

\[
\delta_-
=\frac{\epsilon_p}{|H_p|}
 +\frac{\epsilon_q}{|H_q|}
 -\frac{2\epsilon}{|H|}.
\]

Because (p,q) are odd, (1\neq-1) in both CRT factors. An element succeeds
for both signs exactly when its coordinates are ((1,-1)) or ((-1,1)), if
that element belongs to (H). Thus the overlap can contain zero, one, or two
elements. In particular, adding \(\delta_+\) and \(\delta_-\) double-counts
this overlap. The density for trying both signs is

\[
\delta_++\delta_-
-\frac{|H\cap\{(1,-1),(-1,1)\}|}{|H|}.
\]

## 3. Conditional Las Vegas consequence, including small (n)

Let (S) be whichever one of the two sign-success sets has uniform density

\[
\delta=U_H(S)\geq n^{-c}.
\]

The event (S) is nonempty. A nonempty subset of (H) has uniform mass at
least (1/|H|). Since (H\leq(\mathbb Z/N\mathbb Z)^\times),

\[
\delta\geq\frac1{|H|}\geq\frac1{\varphi(N)}>2^{-n}.
\]

Let τ be the sampler's total-variation error. Then

\[
\tau<2^{-2n}<2^{-n}\delta.
\]

For every (N\geq3), (n\geq2). Therefore a sampled trial succeeds on (S)
with probability

\[
P(S)\geq U_H(S)-\tau
>(1-2^{-n})\delta
\geq\frac34n^{-c}.
\]

This direct atomic-mass argument removes the possible small-(n) gap. It does
not rely on an asymptotic comparison between (2^{-2n}) and (n^{-c}).

On each independent trial, sample (X), compute

\[
d_+=\gcd(X-1,N),\qquad d_-=\gcd(X+1,N),
\]

and inspect both. Before returning any (d), check (1<d<N), check the exact
remainder (N\bmod d=0), and form (N/d) by exact integer division. For the
stated semiprime, a verified nontrivial divisor gives its factorization. The
expected number of trials is less than \((4/3)n^c\). Sampling, gcd, and exact
division all have polynomial bit complexity, so the expected total bit
complexity is polynomial in (s+n) for fixed (c). Verification prevents an
incorrect output, and the positive per-trial probability gives termination
with probability one. This is a Las Vegas algorithm.

## 4. Abstract density obstruction

In (C_L=\langle a\rangle), write \(-1=a^{L/2}\), the unique element of order
two. Put (g=(a,a)) and (h=(1,-1)). The diagonal group \(\langle g\rangle\)
has order (L). Also, (h) has order two and does not lie in that diagonal:
if (h=(a^k,a^k)), its first coordinate forces (k=0\pmod L), while its
second coordinate would then be (1\neq-1). Hence

\[
|H|=|\langle g,h\rangle|=2L.
\]

Both projections contain (a), because they contain the corresponding
projection of (g). Each projection is therefore all of (C_L) and has
order (L).

For a direct density count, every element has a unique form

\[
g^kh^e=(a^k,a^k(-1)^e),
\qquad 0\leq k<L,\quad e\in\{0,1\}.
\]

For (e=0), either both coordinates are (1) or neither is. For (e=1),
exactly one coordinate is (1) only at (k=0), which gives ((1,-1)), or at
(k=L/2), which gives ((-1,1)). There are exactly two positive-success
elements among (2L) elements. Thus

\[
\delta_+=\frac{2}{2L}=\frac1L.
\]

The generator ((1,-1)) is itself a separator, but its existence does not
force a large density. This is only an abstract finite-group calculation. It
does not assert any integer realization or any infinite semiprime family.

## 5. Scope

The sampler starts with public generators. It gives no procedure that creates
such a subgroup from bare (N). The density identities are exact counts, not
inverse-polynomial lower bounds. The abstract example shows why the existence
of a separator alone cannot supply such a lower bound. The sampler also does
not find a short word for a separator, and the conditional Las Vegas result
does not cover inputs for which both success densities are too small.

Therefore these results do not prove a sparse-separator theorem or an
all-input factoring algorithm. A complete feedback theorem needs an added
argument that produces inverse-polynomial success density after refinement,
produces a separator represented by a polynomial-size sparse word that can be
evaluated directly, or supplies another refinement that creates one of those
two conditions.
