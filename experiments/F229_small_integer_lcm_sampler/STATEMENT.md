# F229 candidate — fixed-gap collapse of small-integer lcm sampling

## Status

This is a frozen, self-audited, proof-only candidate. It is an exact
obstruction for three precisely named \((N-1)\)-annihilator sampling laws.
It is not a factoring lower bound and it does not cover arbitrary nonuniform
modular words in small rational primes.

## Conventions

Let

\[
n=\lceil\log _2(N+1)\rceil.
\tag{0.1}
\]

A numerical-QP function is bounded by

\[
2^{C(\log _2(n+1))^k}
\tag{0.2}
\]

for fixed constants \(C>0\) and \(k\ge 1\), independent of the input,
its hidden factors, the stage, and the history.

The bounded-prime-gap theorem implies that there is one fixed even integer
\(d\ge 2\) and infinitely many pairs of odd primes

\[
q=p+d.
\tag{0.3}
\]

In all statements below, \((p,q)\) runs through this one infinite family,
\(N=pq\), and the pair is sufficiently large. In particular,

\[
p<q<2p,
\qquad
n=2\log _2p+O(1).
\tag{0.4}
\]

Put \(A=N-1\). The negative results grant the complete factorization of
\(A\) for free. For a unit \(a\bmod N\), a stage computes

\[
G_A(a)=\gcd(a^A-1,N).
\tag{0.5}
\]

A proper value factors \(N\). On a global return \(G_A(a)=N\), the stage
may run the P197 primary gcd-one tests and their factor-first stripping using
the complete factorization of \(A\), and may lcm-accumulate all blocks which
those tests certify. A sample is called useful if its initial gcd screen or
return gives a proper factor, or if its primary tests certify a block which
strictly enlarges the current common modulus.

## Theorem A — exact fixed-gap collapse

For every integer \(X\) with \(\gcd(X,N)=1\),

\[
\boxed{
\gcd(X^{N-1}-1,N)=\gcd(X^d-1,N).
}
\tag{A.1}
\]

If the common value is \(N\), then both local orders divide \(d\). Every
common primary block certified from the factored annihilator \(A=N-1\)
therefore divides \(d\). Consequently, the lcm of the blocks certified from
an arbitrary number of such global returns also divides \(d\).

The nonunit cases are exact. If \(\gcd(X,N)\) is proper, the input is
already factored. If \(N\mid X\), the gcd screen is the trivial value \(N\)
and the annihilator test is not a unit test. The residue \(X=1\) gives a
global return of exact order one and certifies no nontrivial block.

## Theorem B — bounded-height and short-word zero law

Let \(H(n)\) be any fixed numerical-QP function. Eventually

\[
H(n)^d<p.
\tag{B.1}
\]

For every integer \(X\) with \(2\le X\le H(n)\),

\[
\gcd(X,N)=1,
\qquad
G_A(X)=1.
\tag{B.2}
\]

Thus every adaptive, history-dependent law supported on
\(\{0,1,\ldots,H(n)\}\) has useful-event probability exactly zero at every
history, apart from a proper initial gcd which is itself the factor output.
On this family, that proper branch is absent for all supported positive
bases because \(H(n)<p\); zero gives only the full gcd, and one gives only
the order-one return.

More generally, let a positive integer word in small rational primes or
ordinary integer generators have unreduced value

\[
X=\prod_{j=1}^k b_j,
\qquad b_j\ge2.
\tag{B.3}
\]

If

\[
\sum_{j=1}^k\log _2b_j<\frac{\log _2p}{d},
\tag{B.4}
\]

then \(G_A(X)=1\). Hence a word can first evade the literal height
obstruction only after total log-height

\[
\boxed{
\sum_j\log _2b_j\ge \frac{n}{2d}+O(1).
}
\tag{B.5}
\]

This condition is necessary, not sufficient.

## Theorem C — uniform integer intervals remain exponentially sparse

At a stage, choose an arbitrary integer \(H\ge2\), possibly as a function
of the prior history, and then draw \(X\) conditionally uniformly from
\(\{2,\ldots,H\}\). Run the initial gcd screen and the complete declared
return/primary-test stage.

If \(H^d<p\), the useful probability is zero. For every other \(H\), it is
at most

\[
\boxed{
\frac{4+4d}{p}+\frac{4d}{H}
\le (4+8d)p^{-1/d}.
}
\tag{C.1}
\]

Therefore one trial has useful probability

\[
2^{-n/(2d)+O(1)}=2^{-\Omega(n)}
\tag{C.2}
\]

uniformly over every reached history and every choice of \(H\). Any adaptive
bank of numerical-QP many such fresh conditional interval samples has total
useful probability \(2^{-\Omega(n)}\).

This theorem permits \(H\) to have numerical-QP bit length. It is not only
a small-value statement.

## Theorem D — even ideal uniform mixing of all small-prime words fails

Choose an integer-valued numerical-QP bound \(B=B(n)\) such that

\[
\log n=o(\log B),
\qquad
\log B=o(n).
\tag{D.1}
\]

For example, one may take

\[
B=\left\lceil\exp((\log(n+2))^3)\right\rceil.
\tag{D.2}
\]

Let

\[
\mathcal G_N(B)
=\left\langle \ell\bmod N:\ell\le B\text{ is rational prime}\right\rangle
\le(\mathbb Z/N\mathbb Z)^\times.
\tag{D.3}
\]

The generators are units because eventually \(B<p\). Grant an exact
uniform sample \(a\) from this whole subgroup, even though no QP exact
sampler is asserted. Let \(\mathcal G_p(B)\) and \(\mathcal G_q(B)\) be its
two projection images. Then

\[
\Pr(p\mid a^{N-1}-1)
=\frac{\gcd(d,|\mathcal G_p(B)|)}{|\mathcal G_p(B)|}
\le\frac d{|\mathcal G_p(B)|},
\tag{D.4}
\]

and the analogous formula holds for \(q\). No independence between the two
projections is assumed.

Writing \(\Psi(x,B)\) for the number of positive \(B\)-smooth integers at
most \(x\),

\[
|\mathcal G_p(B)|\ge\Psi(p,B),
\qquad
|\mathcal G_q(B)|\ge\Psi(q,B).
\tag{D.5}
\]

The standard smooth-number estimate used in P172 gives

\[
\Psi(p,B)=p^{1-o(1)},
\qquad
\Psi(q,B)=q^{1-o(1)}.
\tag{D.6}
\]

Hence

\[
\boxed{
\Pr(\text{proper return or any global return})
\le
\frac d{\Psi(p,B)}+\frac d{\Psi(q,B)}
=2^{-n/2+o(n)}.
}
\tag{D.7}
\]

The same conditional bound holds at every history if each next sample is
conditionally exact-uniform on \(\mathcal G_N(B)\). A numerical-QP bank
still has total return probability \(2^{-\Omega(n)}\). Moreover, by
Theorem A, all global returns together contribute an lcm dividing the fixed
integer \(d\).

## Exact surviving boundary

Theorems B and C close bounded-height and uniform-height ordinary-integer
laws. Theorem D closes the ideal fully mixed endpoint of words in all small
rational primes. They do not control an intermediate nonuniform word law.

For every positive word value \(X\), Theorem A says that its whole declared
stage is controlled by the fixed-degree integer

\[
C_X=X^d-1.
\tag{E.1}
\]

Before \(C_X\ge p\), no hidden component can divide it. A one-sided return
requires a nonzero hidden-factor-scale quotient

\[
C_X=k_p p
\quad\text{or}\quad
C_X=k_q q,
\tag{E.2}
\]

and a global return with \(X>1\) requires

\[
C_X=kN,
\qquad k\ge1.
\tag{E.3}
\]

Thus a materially new small-prime word source must do both of the following:

1. cross the linear log-height threshold in (B.5), thereby creating a real
   modular wrap or quotient in \(X^d-1\); and
2. remain strongly nonuniform enough to put inverse-QP mass on the union of
   the two local \(d\)-torsion sets, in a configuration which gives a
   one-sided return, a factor-first local-order mismatch, or a genuinely new
   block. Exact uniform mixing gives only (D.7), and all blocks still divide
   \(d\).

This identifies the first missing word/carry feature. It does not prove
that such a factor-correlated nonuniform word law cannot exist.

## Relation to the nearest prior routes

- P165/F187 proves that uniform units almost never return for the
  \((N-1)\)-annihilator on bounded-gap pairs. F229 instead proves a
  deterministic zero law for every bounded ordinary integer, an all-height
  uniform-interval bound, and an exact small-prime subgroup law.
- P172/F195 gives the low-small-prime smooth-number terminal and leaves the
  mixed high-order branch. F229 uses the same integer-specific smooth-number
  density in the opposite direction: it makes the subgroup generated by
  small rational primes so large that its fixed \(d\)-torsion is sparse.
- P197/F220 gives exact lcm drift once a source has inverse-QP progress.
  F229 supplies a history-wise obstruction for the three named sources and
  proves that every global-return block on the hostile family divides \(d\).
- P161 removes small rational-prime support from one local order. F229 makes
  no independence assumption about local orders or small-prime generator
  images.

No top-level factoring algorithm follows.
