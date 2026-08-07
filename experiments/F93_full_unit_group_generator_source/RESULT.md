# F93 — bare N already gives constant-probability generators of the full unit group

**Status:** proof-only candidate. No research computation, hostile audit,
proof-blind reconstruction, cross-family audit, human audit, or literature
audit has run. This is a source theorem and a correction to the subgroup-gain
interpretation of feedback. It is not a factor-localization decoder or a
factoring algorithm.

## 1. Closest prior route and material difference

P83 proves that any supplied polynomial-size subgroup has an easy
near-uniform sampler, but separator existence need not give useful density.
P97 gives two constant-probability generators of the cyclic powered
rectangle for a distinct odd semiprime.

The present result is more basic and has wider scope. For every \(N\), a
fixed batch of \(n=\lceil\log_2(N+1)\rceil\) raw residues either exposes a
factor or, with one absolute constant probability, generates the complete
unit group. For a distinct semiprime, three raw units suffice with one
absolute constant probability.

Therefore canonical feedback is not fundamentally needed to enlarge the
abstract multiplicative subgroup. Its possible gain is stronger access: it
can make a useful residue a named public block, provide an integer
factorization presentation, or create a short known relation. Those are
algorithmic changes even when the residue was already an unknown word in
the sampled generators.

## 2. A uniform generation bound for finite abelian groups

Let \(H\) be a finite abelian group. For each prime \(\ell\mid |H|\), put

\[
r_\ell=\dim_{\mathbb F_\ell}(H/\ell H).
\]

This is the minimum number of generators of the Sylow \(\ell\)-subgroup.

### Theorem 1

For \(d\) independent uniform elements of \(H\), the exact probability that
they generate \(H\) is

\[
\boxed{
\prod_{\ell\mid |H|}
\prod_{i=0}^{r_\ell-1}
\left(1-\ell^{\,i-d}\right).
}
\tag{1}
\]

### Proof

The Sylow coordinates of a uniform element are independent and uniform.
The \(d\) elements generate the Sylow \(\ell\)-subgroup exactly when their
images generate its Frattini quotient \(H/\ell H\). This quotient is the
vector space \(\mathbb F_\ell^{r_\ell}\). A uniformly random
\(r_\ell\times d\) matrix has full row rank with probability

\[
\prod_{i=0}^{r_\ell-1}(1-\ell^{i-d}).
\]

Generation must hold independently in every Sylow component, which gives
(1). \(\square\)

Define the absolute constant

\[
c_0=
\prod_{\ell\ {\rm prime}}
\prod_{k=2}^{\infty}(1-\ell^{-k}).
\tag{2}
\]

This product is strictly positive. Indeed, every
\(\ell^{-k}\le1/4\), so

\[
-\log(1-\ell^{-k})\le\frac43\ell^{-k}.
\]

Also,

\[
\sum_{\ell\ {\rm prime}}\sum_{k=2}^{\infty}\ell^{-k}
=
\sum_{\ell\ {\rm prime}}\frac1{\ell(\ell-1)}
<
\sum_{m=2}^{\infty}\frac1{m(m-1)}
=1.
\]

Hence \(c_0>e^{-4/3}>0\).

### Corollary 2

If

\[
|H|<2^n,
\]

then \(n\) independent uniform elements generate \(H\) with probability at
least \(c_0\).

### Proof

Since \(\ell^{r_\ell}\le |H|<2^n\), one has

\[
r_\ell\le n-1.
\]

With \(d=n\), every factor in (1) is of the form

\[
1-\ell^{-k}
\qquad(k\ge2).
\]

The finite product in (1) omits factors from the positive infinite product
(2), so it is at least \(c_0\). \(\square\)

## 3. A public all-input unit-group source

Let

\[
G_N=(\mathbb Z/N\mathbb Z)^\times,
\qquad
n=\lceil\log_2(N+1)\rceil.
\]

Sample \(n\) independent integers uniformly from
\(\{1,\ldots,N-1\}\). For each sample \(a_i\), compute

\[
d_i=\gcd(a_i,N).
\]

If some \(d_i>1\), it is automatically a proper factor because
\(a_i<N\). Otherwise all samples are units.

### Theorem 3

One batch has probability at least \(c_0\) of doing one of the following:

1. returning a proper factor of \(N\); or
2. supplying a public list that generates the complete unit group \(G_N\).

The batch uses deterministic polynomial bit complexity after its random
bits are drawn.

### Proof

Let

\[
\alpha=\frac{\varphi(N)}{N-1}.
\]

The probability that all \(n\) samples are units is \(\alpha^n\). Conditioned
on this event, they are independent exact uniform elements of \(G_N\).
Since

\[
|G_N|=\varphi(N)<N<2^n,
\]

Corollary 2 gives conditional generation probability at least \(c_0\).
Thus the probability of a factor or a generating list is at least

\[
1-\alpha^n+\alpha^n c_0
=1-\alpha^n(1-c_0)
\ge c_0.
\]

Exact rejection sampling of each bounded integer has expected polynomial
fair-random-bit cost, with an exponentially decaying tail. Together with the
\(n\) gcd computations, the total expected bit complexity is polynomial.
\(\square\)

The algorithm does not recognize whether an all-unit list generates
\(G_N\). As in P97, this is harmless in a promise-decoder reduction: run a
polynomial-bounded decoder on every all-unit batch, verify every returned
factor, and restart after failure.

## 4. Three samples suffice for distinct semiprimes

If \(N=pq\) for distinct odd primes, then

\[
G_N\cong C_{p-1}\times C_{q-1}.
\]

Every Sylow rank \(r_\ell\) is at most two. Therefore three independent
uniform units generate \(G_N\) with exact probability

\[
\prod_{\ell:r_\ell=1}(1-\ell^{-3})
\prod_{\ell:r_\ell=2}(1-\ell^{-3})(1-\ell^{-2}),
\]

which has the absolute lower bound

\[
\boxed{
\frac1{\zeta(2)\zeta(3)}>0.
}
\]

The same factor-or-generate calculation as in Theorem 3 applies to three
raw nonzero residues.

P97 remains useful because its two powered samples generate a cyclic
coprime-order rectangle and remove every shared-order correlation. F93 does
not replace that normal form. It shows only that abstract subgroup
generation was never the hard source problem.

## 5. The complete unit group is factor-bearing

If \(N=p^e\) is a prime power with \(e\ge2\), the unit

\[
x=1+p
\]

satisfies

\[
1<\gcd(x-1,N)<N.
\]

If \(N\) has at least two distinct prime divisors, choose one odd
prime-power component \(p^e\Vert N\). CRT gives a unit \(x\) with

\[
x\equiv-1\pmod{p^e},
\qquad
x\equiv1\pmod{N/p^e}.
\]

Then \(\gcd(x-1,N)\) is nontrivial and proper. The remaining composite case
is a power of two, already covered by \(x=1+2\).

Thus \(G_N\) contains a factor-revealing element for every composite \(N\).
The theorem does not find its word in the sampled generators.

## 6. Exact feedback consequence

Condition on a batch that generates \(G_N\). On the no-factor branch, every
integer block exposed by canonical feedback is a unit. Its residue already
belongs to the generated subgroup:

\[
\langle a_1,\ldots,a_n\rangle=G_N.
\]

Therefore feedback cannot enlarge the abstract residue subgroup on this
batch.

This does not make feedback redundant. An element of \(G_N\) has some
polynomial-bit exponent-vector representation in the sampled generators,
but that representation can be unknown; this theorem supplies no recovery
algorithm.
Feedback can instead reveal the element directly as:

- one named canonical integer;
- one block in a gcd-free presentation;
- one endpoint with known relation provenance; or
- one input to a complete saturation or power decoder.

The correct framework-level distinction is therefore

\[
\boxed{
\text{abstract subgroup availability}
\ne
\text{public word and integer-presentation accessibility}.
}
\]

The \(4033\) and \(2047\) feedback witnesses prove the second kind of gain
relative to their restricted initial transcripts. They do not prove that
feedback is needed to enlarge the subgroup available to an algorithm that
retains a constant-probability full-group generator batch.

## 7. Exact reduction and scope

Suppose a polynomial-time procedure, on every public list generating
\(G_N\) for a composite \(N\), returns a verified proper factor with
inverse-polynomial probability. Suppose its work is polynomially bounded on
every list and it otherwise returns failure. Fresh batches from Theorem 3,
followed by verified repetition, give a classical Las Vegas
expected-polynomial factorer for every composite \(N\).

This reduction is deliberately not called progress toward the top-level
theorem: the promised factor-localization procedure is the full missing
problem. F93 supplies no such decoder, no useful density bound, no order
information, no classical HSP solver, and no factoring algorithm.
