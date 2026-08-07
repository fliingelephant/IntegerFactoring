# F77 — canonical subgroup sampling is easy; separator density is the gate

**Status:** proof-only candidate. No research computation was run. This is a
conditional sampler theorem and an exact density formula. It is not a
factoring algorithm.

## 1. Public subgroup and sampler

Let \(N\ge3\), and let

\[
q_1,\ldots,q_s\in(\mathbb Z/N\mathbb Z)^\times
\]

be public generators. Put

\[
H=\langle q_1,ldots,q_s\rangle.
\]

The factorization of \(N\), the generator orders, and \(|H|\) are not given.
Let

\[
n=\lceil\log_2N\rceil,
\qquad
L=3n+\lceil\log_2(s+1)\rceil,
\qquad
M=2^L.
\]

Choose independent uniform exponents

\[
E_j\in\{0,1,\ldots,M-1\},
\]

and output the canonical residue

\[
X=\left[\prod_{j=1}^s q_j^{E_j}\right]_N.
\tag{1}
\]

### Theorem 1 — near-uniform subgroup sampler

The law of \(X\) has total-variation distance less than \(2^{-2n}\) from the
uniform distribution on \(H\). The sampler uses
\(O(s(n+\log s))\) random bits and polynomial bit complexity in
\(s+n\).

### Proof

Let \(t_j\) be the order of \(q_j\). Then \(t_j<N\le2^n\). If an integer is
uniform on \(0,\ldots,M-1\), its residue modulo \(t_j\) has total-variation
distance at most

\[
\frac{t_j}{2M}
\]

from uniform on \(\mathbb Z/t_j\mathbb Z\). This follows by writing
\(M=a t_j+b\): every residue has either \(a\) or \(a+1\) preimages, and the
sum of its probability deviations is at most \(t_j/M\).

For independent coordinates, total variation from the product of the exact
uniform laws is at most the sum of the coordinate distances. Hence it is at
most

\[
\sum_{j=1}^s\frac{t_j}{2M}
<
\frac{s2^n}{2\cdot2^{3n}(s+1)}
<2^{-2n}.
\tag{2}
\]

The homomorphism

\[
\prod_j\mathbb Z/t_j\mathbb Z\longrightarrow H,
\qquad
(e_j)_j\longmapsto\prod_jq_j^{e_j}
\]

is surjective. Uniform input pushes forward to uniform output because all
fibres are cosets of its kernel. Total variation cannot increase under a
map, so (2) proves the distribution claim.

Each exponent has \(L=O(n+\log s)\) bits. Repeated squaring and modular
multiplication compute (1) in polynomial bit complexity. \(\square\)

## 2. Exact separator density on a squarefree semiprime

Now assume only for analysis that

\[
N=pq
\]

for distinct odd primes. Let \(H_p\) and \(H_q\) be the projection images of
\(H\) modulo \(p\) and \(q\).

For uniform \(X\in H\), define

\[
\delta_+
=\Pr\bigl(1<\gcd(X-1,N)<N\bigr).
\]

### Theorem 2 — positive-sign density

One has the exact formula

\[
\boxed{
\delta_+
=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|}.
}
\tag{3}
\]

### Proof

The kernel of the projection \(H\to H_p\) has size \(|H|/|H_p|\). Therefore

\[
\Pr(X\equiv1\pmod p)=\frac1{|H_p|},
\]

and similarly for \(q\). Both congruences hold only at the identity element
of \(H\), with probability \(1/|H|\). A proper gcd occurs exactly when one,
but not both, of the two congruences holds. Inclusion-exclusion for the
symmetric difference gives (3). \(\square\)

For the negative sign, let

\[
\epsilon_p=\mathbf1_{-1\in H_p},
\qquad
\epsilon_q=\mathbf1_{-1\in H_q},
\qquad
\epsilon=\mathbf1_{-1\in H}.
\]

The identical coset argument gives

\[
\boxed{
\delta_-
:=\Pr\bigl(1<\gcd(X+1,N)<N\bigr)
=\frac{\epsilon_p}{|H_p|}
+\frac{\epsilon_q}{|H_q|}
-\frac{2\epsilon}{|H|}.
}
\tag{4}
\]

The positive and negative success sets can overlap, so (3) and (4) should not
be added without subtracting that overlap.

## 3. Conditional Las Vegas consequence

Use sampler (1), then test both sign gcds. Every returned proper divisor is
verified by exact division. If either \(\delta_+\) or \(\delta_-\) is at
least \(n^{-c}\) for a fixed \(c\), the negligible sampling error in Theorem
1 leaves inverse-polynomial success probability per trial. Independent
repetition then has polynomial expected bit complexity and returns a factor
with probability one.

This is a valid conditional Las Vegas algorithm. It does not prove the
density premise.

## 4. Why subgroup expansion is not enough

Formula (3) shows the exact obstruction. A subgroup can contain a positive
separator while its density is as small as the reciprocal of a local
projection order.

For an abstract example, let \(C_L=\langle a\rangle\) have even order \(L\).
Inside \(C_L\times C_L\), let

\[
H=\langle(a,a),(1,-1)\rangle.
\]

Then \(|H|=2L\), both projection images have order \(L\), and (3) gives

\[
\delta_+=\frac1L.
\]

The element \((1,-1)\) is a separator, but a uniform sample hits a positive
separator with probability only \(1/L\). When a realizable local order \(L\)
is exponential in \(n\), uniform subgroup sampling is exponentially slow for
this target.

This abstract example is a density calculation, not an asserted infinite
integer family with the displayed public generators.

## 5. Exact consequence for feedback research

Canonical-residue closure does not need a heuristic dense-exponent beam to
sample its current subgroup. The near-uniform sampler is already public and
polynomial. The remaining theorem must prove one of the following after
feedback refinement:

1. the sign-separator density in the generated subgroup is inverse
   polynomial;
2. a polynomial sparse word menu targets a separator even when its uniform
   density is small; or
3. integer gcd refinement creates another subgroup in which one of the first
   two properties holds.

P78/F75's fixed \(N=4033\) state satisfies the second alternative by an
explicit support-two word. No all-input theorem establishes any alternative.
No classical polynomial-time factoring algorithm is proved.
