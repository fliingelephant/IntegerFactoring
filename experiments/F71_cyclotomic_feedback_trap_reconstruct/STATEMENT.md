# Proof-blind reconstruction target: order-three endpoint-feedback trap

Work only from this statement. Do not read any other F71 artifact, audit,
project registry, progress note, durable theorem file, or git history.
Reconstruct every proof independently. Report PASS only if all stated claims
and scope boundaries follow.

## Setup

Let \(c\) be an odd prime and let

\[
N=c^2+c+1
\]

be composite with \(3\nmid N\). Start from

\[
c\cdot c^2=c^3=1+(c-1)N. \tag{1}
\]

The endpoint presentation has the sole prime block \(c\).

## Local order and subgroup

Prove that, for every prime power \(p^a\Vert N\), the residue of \(c\) has
exact order three. Deduce

\[
H=\langle c\rangle=\{1,c,c^2\}\pmod N,
\]

with the three displayed canonical representatives. Prove that \(H\) contains
no direct sign separator.

## Endpoint-only feedback

Allow any finite transcript built by the following operations:

1. form a positive product or power of authorized occurrences of the current
   endpoint block;
2. either retain the raw power or reduce it canonically modulo \(N\);
3. take the canonical inverse;
4. append the resulting inverse relation;
5. apply exact integer gcd refinement and exact perfect-power extraction.

Under canonical reduction, prove that the identity state is either discarded
by \(1<g<N\) or adds only \(1\cdot1=1\), while every nontrivial feedback
relation repeats \(c^3\).

If an oversized raw endpoint \(G=c^e\) is retained, prove that its relation
value has the form \(c^{3t}\). Deduce by induction that every endpoint and
relation value remains a power of \(c\) and no second gcd-free block appears.

## Screens and complete decoder

Prove that every direct sign, inverse-pair difference, and discriminant screen
is trivial or global. For the discriminant, include the identity

\[
(G-w)^2+4\equiv(G+w)^2\pmod N.
\]

For any finite list of raw relation values \(c^{3t_i}\), characterize every
rational-square product, including integer relation coefficients and complete
\(2\)-saturation. Prove that every exact positive decoded root is
\(1\pmod N\). Thus the full decoder image is \(\{1\}\).

Check that exact perfect-power roots and the public square

\[
4N-3=(2c+1)^2
\]

do not split \(N\) or escape the declared endpoint-only source.

## Infinite robust family

For each \(B\ge3\), prove that infinitely many odd primes \(c\) satisfy:

1. \(N=c^2+c+1\) is composite and \(3\nmid N\);
2. \(N\) has at least two distinct prime divisors;
3. every prime divisor of \(N\) is greater than \(B\);
4. two prescribed prime divisors have valuation exactly one, so \(N\) is not
   a perfect power.

Use this construction:

- choose distinct primes \(\ell_1,\ell_2>B\), each \(1\pmod3\);
- choose a nontrivial cube root \(r_i\pmod{\ell_i}\);
- among its lifts modulo \(\ell_i^2\), choose \(a_i\) that is a root modulo
  \(\ell_i\) but not modulo \(\ell_i^2\);
- impose \(c\equiv a_i\pmod{\ell_i^2}\),
  \(c\equiv1\pmod2\), \(c\equiv2\pmod3\), and
  \(c\equiv1\pmod q\) for every prime \(5\le q\le B\);
- apply CRT and Dirichlet's theorem.

Prove all compatibility, simple-root, exact-valuation, small-prime exclusion,
and non-perfect-power assertions.

## Witness and scope

Verify the example

\[
c=11,\qquad N=133=7\cdot19,
\]

including the global root from two duplicate relations.

Decide whether the proof establishes this narrow classification:

> Unlimited occurrence amplification inside one endpoint block can be trapped
> at the full subgroup level, even after exact gcd refinement and complete
> square decoding.

State explicitly that it does not cover a relation quotient such as \(c-1\),
an independent seed or block, non-endpoint integer data, additive operations,
order or period methods, arbitrary algorithms, or general factoring.
