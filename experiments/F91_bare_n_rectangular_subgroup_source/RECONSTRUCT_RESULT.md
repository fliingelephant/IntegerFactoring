# PASS

The SHA-256 of RECONSTRUCT_STATEMENT.md is
547f538367abef228c387761fb1f67a4c778d127c0c69b8ce013e96ae211b07c,
as required. All rectangle, sampling, generation-probability, reduction,
edge-case, and fixed-instance claims are correct.

## 1. The full-unit powered image

Put

\[
P=p-1,\qquad Q=q-1,\qquad M=N-1=pq-1.
\]

CRT and cyclicity of finite-field unit groups give

\[
G\simeq C_P\times C_Q.
\]

Since

\[
M=q(p-1)+(q-1),
\]

one has

\[
\gcd(M,P)=\gcd(P,Q)=g.
\]

Symmetrically,

\[
\gcd(M,Q)=g.
\]

The \(M\)-th power image of a cyclic group of order \(r\) is cyclic of
order \(r/\gcd(r,M)\). Powering the full direct product acts coordinatewise,
so

\[
S_N=G^{N-1}\simeq C_{P/g}\times C_{Q/g}
=C_A\times C_B.
\]

Dividing two integers by their gcd leaves coprime quotients:

\[
\gcd(A,B)=1.
\]

Therefore

\[
\boxed{S_N\simeq C_A\times C_B\simeq C_{AB}}.
\]

If \(A=B=1\), then \(P=Q=g\), so \(p-1=q-1\) and \(p=q\), contrary to the
distinct-prime premise. Hence

\[
\boxed{AB>1}.
\]

## 2. Exact separator count and edge cases

Under the rectangle identification, a positive separator has one coordinate
equal to the identity and the other nonidentity. There are

\[
B-1
\]

elements of the form \((1,y)\) with \(y\ne1\), and

\[
A-1
\]

elements of the form \((x,1)\) with \(x\ne1\). The two sets are disjoint.
Thus the exact count is

\[
\boxed{A+B-2}.
\]

Since \(|S_N|=AB\), the uniform density is

\[
\boxed{
\frac{A+B-2}{AB}
=\frac1A+\frac1B-\frac2{AB}
}.
\]

If \(A=1\), distinctness forces \(B>1\). The first local image is trivial,
and all \(B-1\) nonidentity elements are separators. Their density is
\(1-1/B\), which agrees with the formula. The case \(B=1\) is symmetric.
The case \(A=B=1\) is impossible by Section 1.

In particular, \(S_N\) is always nontrivial and always contains a positive
separator for distinct odd primes.

## 3. Exact accepted-unit sampling

The integers

\[
1,\ldots,N-1
\]

are exactly the nonzero residue classes modulo \(N\). Every unit class
occurs once in this set. Conditioning a uniform choice from the set on
\(\gcd(a,N)=1\) therefore gives the exact uniform distribution on \(G\).

Because \(N=pq\), any sampled nonunit in this range has gcd \(p\) or \(q\)
with \(N\): the gcd cannot be \(N\), since \(a\ne0\pmod N\). Thus a rejected
sample already supplies a verified proper factor. If unit samples are still
needed, independent resampling gives independent accepted units.

The acceptance probability is

\[
\frac{\varphi(N)}{N-1}
=\frac{(p-1)(q-1)}{pq-1}.
\]

The claimed strict lower bound is equivalent to

\[
2(p-1)(q-1)>pq-1,
\]

or

\[
(p-2)(q-2)>1.
\]

Distinct odd primes have unordered minimum pair at least \(3,5\), for which
the left side is at least \(1\cdot3>1\). Hence

\[
\boxed{\frac{\varphi(N)}{N-1}>\frac12}.
\]

The expected number of draws per accepted unit is less than two. A nonunit
draw terminates with a factor instead, so it cannot worsen the factorer's
expected cost.

The power map

\[
\theta:G\to S_N,\qquad u\mapsto u^{N-1}
\]

is a surjective homomorphism. Every fibre is a coset of
\(\ker\theta\) and has the same size. The image of an exactly uniform
accepted unit is consequently exactly uniform on \(S_N\). Two independent
accepted units give two independent uniform elements of \(S_N\).

## 4. Exact two-sample generation probability

Let

\[
n=AB>1.
\]

Choose a generator of \(S_N\simeq C_n\), and represent two independent
uniform elements by independent uniform exponents
\(r_1,r_2\in\mathbb Z/n\mathbb Z\). The pair generates \(C_n\) exactly when
it generates every primary component in

\[
C_n\simeq\prod_{\ell^k\parallel n}C_{\ell^k}.
\]

In \(C_{\ell^k}\), two elements fail to generate precisely when both
exponents are divisible by \(\ell\). A uniform exponent is divisible by
\(\ell\) with probability \(1/\ell\), independent of the other sample.
Thus the primary generation probability is

\[
1-\ell^{-2}.
\]

CRT makes the primary coordinates of each uniform exponent independent
across distinct primes. Therefore

\[
\boxed{
\Pr(\langle y_1,y_2\rangle=S_N)
=\prod_{\ell\mid AB}(1-\ell^{-2})
}.
\]

Repeated powers \(\ell^k\) introduce no additional factor: at least one
exponent being nonzero modulo \(\ell\) already makes that exponent a unit
modulo \(\ell^k\), and hence a generator of the full cyclic primary
component together with the other element.

Since every factor \(1-\ell^{-2}\) lies in \((0,1)\), a product over a
finite subset of primes is at least the product over all primes. Euler's
product and \(\zeta(2)=\pi^2/6\) give

\[
\prod_{\ell\mid AB}(1-\ell^{-2})
\geq
\prod_{\ell\ {\rm prime}}(1-\ell^{-2})
=\frac1{\zeta(2)}
=\boxed{\frac6{\pi^2}}.
\]

The product is not empty because \(AB>1\). If one considered the excluded
case \(AB=1\), the empty product would correctly equal one, since two
elements generate the trivial group with probability one.

## 5. Reduction from a promised axis-localization procedure

Interpret “inverse-polynomial probability on every promised generating
list” in the standard uniform sense: there is one polynomial
\(P(\log N)\) such that every list generating \(S_N\) has success
probability at least \(1/P(\log N)\).

One factorer iteration is:

1. Draw accepted units until two are obtained, returning immediately if a
   sampling gcd is already proper.
2. Form \(y_i=a_i^{N-1}\pmod N\).
3. Run the proposed axis-localization procedure on the public list
   \((y_1,y_2)\).
4. Return only a factor verified by exact division. On failure, start a new
   iteration with fresh samples and fresh internal randomness.

The list generates \(S_N\) with probability at least \(6/\pi^2\). Conditioned
on any such list, the procedure succeeds with probability at least
\(1/P(\log N)\). Therefore every iteration succeeds with probability at
least

\[
\frac6{\pi^2P(\log N)}.
\]

The procedure has polynomial bounded work on every list, including
non-generating lists. Thus an unpromised batch cannot hang or consume
unbounded work. The number of iterations is geometrically distributed with
polynomial expectation. Accepted-unit sampling has constant expected
overhead, and all other work per iteration is polynomial.

Every returned output is verified, so the algorithm never returns an
incorrect factor. The positive per-iteration success bound gives
termination with probability one and expected-polynomial running time.
This is a classical Las Vegas factorer.

The reduction never tests whether \((y_1,y_2)\) generates \(S_N\). It simply
runs the bounded procedure on every batch. Recognition of the promise is
unnecessary.

## 6. Exact uniformity versus near uniformity

The generation formula and its \(6/\pi^2\) bound above use exact independent
uniform samples. Exactness comes from conditioning a uniform nonzero residue
on being a unit and then applying a surjective homomorphism with equal-size
fibres.

A generic public-generated-subgroup sampler that uses bounded random
exponents is only near uniform unless its exponent ranges align exactly with
hidden generator orders. Its output cannot be substituted into the displayed
equality without an error term. If each marginal is within total variation
\(\varepsilon\) of uniform, the two-sample law is within at most
\(2\varepsilon\) of the exact product law, so one obtains only a perturbed
lower bound, not the exact product formula.

This distinction does not affect the present reduction because it samples
the full unit group exactly before applying \(u\mapsto u^{N-1}\).

## 7. Why public generators do not themselves localize an axis

Inside the rectangle

\[
C_A\times C_B,
\]

the two axes are

\[
C_A\times\{1\},
\qquad
\{1\}\times C_B.
\]

Since \(\gcd(A,B)=1\), the full group is cyclic of order \(AB\). A cyclic
group has a unique subgroup of every order dividing its order. Therefore
the two axes are exactly the unique subgroups of orders \(A\) and \(B\)
inside \(C_{AB}\).

The sampled residues do not reveal the hidden CRT coordinates or the hidden
orders \(A,B\). Uniform sampling hits an axis separator with exact density

\[
\frac1A+\frac1B-\frac2{AB}.
\]

When both \(A\) and \(B\) are large, this density can be small. Producing
public generators, or sampling uniformly or near-uniformly from their
subgroup, supplies no further operation that identifies either unique hidden
order subgroup. An additional axis-localization decoder is still required.

This is an access statement, not a computational lower bound. It does not
claim that axis localization is hard, simulate order finding, or rule out
another classical method.

## 8. Fixed case \(N=4033\)

The factorization is

\[
4033=37\cdot109.
\]

Thus

\[
g=\gcd(36,108)=36,\qquad
A=36/36=1,\qquad
B=108/36=3.
\]

To verify the supplied factor identity, first \(36\mid4032\), so Fermat's
theorem gives

\[
5^{4032}\equiv1\pmod{37}.
\]

Modulo \(109\),

\[
4032=37\cdot108+36.
\]

Repeated squaring gives

\[
5^4\equiv80,\quad
5^8\equiv78,\quad
5^{16}\equiv89,\quad
5^{32}\equiv73\pmod{109},
\]

and hence

\[
5^{36}\equiv73\cdot80\equiv63\not\equiv1\pmod{109}.
\]

Exactly the \(37\)-coordinate of \(5^{4032}\) is the identity. Therefore

\[
\boxed{\gcd(5^{4032}-1,4033)=37}.
\]

This is a nonidentity element of the order-three rectangle
\(S_N\simeq C_3\).

## 9. Fixed case \(N=2047\)

Here

\[
2047=23\cdot89,
\]

so

\[
g=\gcd(22,88)=22,\qquad
A=22/22=1,\qquad
B=88/22=4.
\]

The group \(S_N\) has order four. Its \(23\)-coordinate is always the
identity, and exactly one element has identity \(89\)-coordinate. Thus
three of its four elements are positive separators:

\[
\boxed{\Pr_{y\sim U(S_N)}
\bigl(1<\gcd(y-1,2047)<2047\bigr)=\frac34}.
\]

There is no contradiction with the smaller feedback subgroup

\[
K=\langle11,2\rangle.
\]

Its exponent is \(22\): \(11\) has order \(22\), and \(2\) has order \(11\).
Since

\[
22\mid2046=N-1,
\]

every element of \(K\) is killed by \(N-1\). The full unit group has a
larger \(89\)-local order \(88\); powering by \(2046\) leaves its quotient
of order

\[
88/\gcd(88,2046)=88/22=4.
\]

The full-group image can therefore be nontrivial even though the proper
subgroup \(K\) maps to the identity.

## 10. Scope

For every distinct odd semiprime, two exact samples give a public generating
list for the nontrivial, factor-bearing subgroup \(S_N\) with probability at
least \(6/\pi^2\). This is an all-input constant-probability generator
source.

It does not identify either hidden axis, compute \(A,B\), handle prime
powers or more than two CRT components, simulate order finding, or supply
the promised axis-localization procedure. The result alone is therefore not
a complete factoring algorithm.
