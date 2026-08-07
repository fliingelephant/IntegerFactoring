# F91 hostile proof audit

## Verdict: PASS, with one local precision correction

I audited RESULT.md at SHA-256

    500526bcd5f9c3bc280f9a2a7c23977e61b31ae3c1214f8a5d3b9a10c0d294d3

The digest matches the requested artifact. I ran no research search or
research computation.

The full-unit power formulas, nontriviality, exact two-sample generation
probability, \(6/\pi^2\) lower bound, accepted-unit overhead, public
execution, promise-decoder reduction, and both fixed examples are correct.

One sentence in Section 5 needs a precision correction. Exact uniform
samples have the exact density in equation (6). A sample whose law is within
total variation \(\eta\) of uniform has success probability within \(\eta\)
of that density, not exactly equal to it. Fresh accepted-unit powers give
exact uniform samples publicly, while bounded random words in the two
generators give near-uniform samples without hidden orders. This correction
does not affect any theorem or complexity conclusion.

## 1. The full-unit powered image

Write

\[
N=pq,\qquad
G=(\mathbb Z/N\mathbb Z)^\times
\cong\mathbb F_p^\times\times\mathbb F_q^\times,
\]

and put

\[
g=\gcd(p-1,q-1),\qquad
A=(p-1)/g,\qquad
B=(q-1)/g.
\]

Since \(g\) is the full gcd,

\[
\gcd(A,B)=1.
\]

The identity

\[
N-1=q(p-1)+(q-1)
\]

gives

\[
\gcd(p-1,N-1)=\gcd(p-1,q-1)=g.
\]

The symmetric identity gives the same gcd on the \(q\)-side. The
\((N-1)\)-power images of the two cyclic local unit groups therefore have
orders

\[
\frac{p-1}{\gcd(p-1,N-1)}=A,
\qquad
\frac{q-1}{\gcd(q-1,N-1)}=B.
\]

Because \(G\) is already the full direct product and powering acts
coordinatewise,

\[
G^{N-1}
=
(\mathbb F_p^\times)^{N-1}
\times
(\mathbb F_q^\times)^{N-1}
\cong C_A\times C_B.
\]

No correlation argument is needed in this full-unit case. Since \(A,B\)
are coprime, the product is cyclic of order \(AB\).

## 2. Nontriviality and all \(A=1\), \(B=1\) edge cases

If \(S_N=G^{N-1}\) were trivial, both local image orders would be one:

\[
A=B=1.
\]

Then \(p-1=g=q-1\), so \(p=q\), contrary to the distinct-prime premise.
Thus

\[
AB>1.
\]

It is possible for exactly one order to be one. If \(A=1<B\), then

\[
S_N=\{1\}\times C_B.
\]

Every nonidentity element is a positive separator. The symmetric statement
holds when \(B=1<A\). If both orders exceed one, both coordinate axes are
nontrivial. These cases exhaust the theorem.

The exact number of positive separators is

\[
(A-1)+(B-1)=A+B-2,
\]

and exact uniform density is

\[
\delta_N
=
\frac{A+B-2}{AB}
=
\frac1A+\frac1B-\frac2{AB}.
\]

If \(A=1<B\), this is \((B-1)/B\ge1/2\). If \(A,B\ge2\) and, for example,
\(A=\min\{A,B\}\), then

\[
\delta_N
=
\frac1A+\frac{A-2}{AB}
\ge
\frac1A.
\]

Thus the candidate's direct-density interpretation is correct after the
exact-versus-near-uniform distinction stated in the verdict.

## 3. Conditioning accepted units gives exact independent uniform samples

Draw \(a\) uniformly from the canonical nonzero residues
\(\{1,\ldots,N-1\}\). If \(\gcd(a,N)>1\), that gcd is automatically a proper
factor because \(0<a<N\). Otherwise \(a\) is accepted.

Conditioned on acceptance, every unit residue has the same original
probability, so \(a\) is exactly uniform in \(G\). Repeating the rejection
procedure with independent raw draws produces independent accepted units.
The random number of rejected draws introduces no dependence between the
accepted values.

The power map

\[
G\longrightarrow S_N,\qquad a\longmapsto a^{N-1}
\]

is a surjective homomorphism. Every fibre is a coset of its kernel and has
the same size. Therefore a uniform accepted unit maps to an exactly uniform
element of \(S_N\). Two independent accepted units map to two independent
uniform elements \(y_1,y_2\).

This proves the conditioning used by Theorem 2. No factorization, order, or
hidden rejection advice is used in execution.

## 4. Exact probability that two samples generate the cyclic rectangle

Put \(n=AB>1\) and identify \(S_N\) with the additive cyclic group \(C_n\).
For each prime power \(\ell^k\Vert n\), the \(\ell\)-primary component is
cyclic. Two elements generate it if and only if at least one remains
nonzero in its quotient of order \(\ell\). Equivalently, generation fails
at \(\ell\) exactly when both samples lie in the unique subgroup of index
\(\ell\).

One uniform element lies in that subgroup with probability \(1/\ell\).
For two independent elements, the failure probability is \(1/\ell^2\), so
the local success probability is

\[
1-\frac1{\ell^2}.
\]

Under the CRT decomposition of \(C_n\), the primary coordinates of a
uniform element are independent. This remains true jointly for the two
independent elements. Therefore

\[
\Pr(\langle y_1,y_2\rangle=S_N)
=
\prod_{\ell\mid n}\left(1-\frac1{\ell^2}\right).
\]

This condition handles arbitrary prime powers in \(n\): generation of a
cyclic \(\ell^k\)-group depends only on whether both elements vanish modulo
the unique order-\(\ell\) quotient. There is no missing higher-power factor.

Because the finite set of primes dividing \(n\) is a subset of all primes
and every factor lies in \((0,1)\),

\[
\prod_{\ell\mid n}\left(1-\ell^{-2}\right)
\ge
\prod_{\ell\ {\rm prime}}\left(1-\ell^{-2}\right)
=
\frac1{\zeta(2)}
=
\frac6{\pi^2}
>
0.6.
\]

The empty product case cannot occur because \(n=AB>1\). The formula also
covers \(n\) equal to a prime power, and the smallest case \(n=2\) gives
probability \(3/4\).

## 5. Accepted-unit overhead and public bit complexity

The probability that one raw nonzero residue is a unit is

\[
\frac{\varphi(N)}{N-1}
=
\frac{(p-1)(q-1)}{pq-1}.
\]

The difference needed for the claimed bound is

\[
2(p-1)(q-1)-(pq-1)
=(p-2)(q-2)-1.
\]

For distinct odd primes, the two positive odd numbers \(p-2,q-2\) are
distinct, so their product is at least \(3\). The displayed difference is
therefore positive, proving

\[
\frac{\varphi(N)}{N-1}>\frac12.
\]

One accepted unit needs fewer than two raw trials in expectation, and two
accepted units need fewer than four. Exact uniform sampling from
\(\{1,\ldots,N-1\}\) uses standard rejection from a binary range with
constant expected overhead. The sampled integers, exponent \(N-1\), and
modular residues all have \(O(\log N)\) bits. Gcd and repeated-squaring
powering have polynomial bit complexity.

The public source procedure is therefore:

1. sample a nonzero residue;
2. compute its gcd with \(N\);
3. return a factor immediately if that gcd is proper;
4. otherwise power the accepted unit by the public exponent \(N-1\); and
5. repeat until two powered units are available.

It does not use \(p,q,g,A,B\), an element order, or a group order. Those
quantities occur only in the correctness proof.

## 6. The promise-decoder Las Vegas reduction

Assume a polynomial-time randomized axis-localization decoder whose success
probability is bounded below by one inverse polynomial on every promised
input. On an unpromised list, it remains polynomially bounded and returns
only failure or a publicly verified proper factor.

For each fresh batch, the source pair generates \(S_N\) with probability at
least \(6/\pi^2\). Conditioned on any particular pair that does generate
\(S_N\), the decoder has its promised inverse-polynomial success bound.
This pointwise promise guarantee is important: no assumption about the
distribution of generating pairs is needed.

Thus one batch has inverse-polynomial verified success probability. A gcd
found during unit acceptance only increases that probability. Fresh source
randomness and fresh decoder randomness give independent trials.

Every returned divisor is checked, so the procedure never returns an
incorrect answer. Independent repetition succeeds almost surely, and the
inverse-polynomial batch probability gives polynomial expected running
time. Corollary 3 is a valid classical Las Vegas reduction.

The reduction does not need to decide whether a pair generated \(S_N\).
Failure on an unpromised pair is harmless because the decoder's work is
bounded.

## 7. Exact samples, near-uniform words, and direct gcd density

There are two distinct sampling routes.

1. A fresh accepted unit followed by the \(N-1\) power is an exact uniform
   sample from \(S_N\). Its direct gcd success probability is exactly
   \(\delta_N\).
2. If \(y_1,y_2\) generate \(S_N\), public bounded exponent ranges give a
   distribution within any specified inverse-polynomial or negligible
   total variation \(\eta\) of uniform. Its direct gcd success probability
   lies in

   \[
   [\delta_N-\eta,\delta_N+\eta]\cap[0,1].
   \]

Exact uniform words in \(y_1,y_2\) would require suitable multiples of their
hidden orders, unless another exact sampler is used. This is not needed:
the accepted-unit route already supplies exact samples, and the public word
sampler supplies arbitrarily accurate near-uniform samples in polynomial
time.

Neither route gives an inverse-polynomial direct success bound when both
\(A\) and \(B\) are large. The source theorem produces the rectangle and a
constant-probability generating pair, but does not localize either axis.

## 8. A generator source is not an axis decoder

When the pair generates \(S_N\cong C_{AB}\), the two coordinate axes are the
unique subgroups of orders \(A\) and \(B\). Every element has a
representation

\[
y_1^u y_2^v
\]

with \(O(\log N)\)-bit exponents, since \(|S_N|=AB<\varphi(N)<N\). However,
the source procedure does not reveal suitable \(u,v\), the order \(AB\), or
the coprime factors \(A,B\).

Uniform sampling locates an axis only with density \(\delta_N\), which can
be exponentially small in the input length. The existence of short
representations therefore does not make them publicly findable. An axis
decoder must exploit structure beyond the constant-size generator source,
or a later refinement must change the rectangle.

This is the exact remaining gap. The candidate does not prove classical
order finding, a hidden decomposition algorithm, or a factoring algorithm.

## 9. The \(N=4033\) specialization

For

\[
p=37,\qquad q=109,
\]

one has

\[
p-1=36,\qquad q-1=108,\qquad g=36,
\]

so

\[
A=1,\qquad B=3.
\]

The rectangle has order three. Its two nonidentity elements are both
positive separators, so exact uniform direct success is \(2/3\). The
retained element \(5\) has local orders \(36\) and \(27\); hence
\(5^{4032}\) is one locally and has order three on the other side. Therefore

\[
\gcd(5^{4032}-1,4033)=37.
\]

This verifies the claimed fixed specialization. It does not make the base
five an all-input source.

## 10. The \(N=2047\) specialization

For

\[
p=23,\qquad q=89,
\]

one has

\[
p-1=22,\qquad q-1=88,\qquad g=22,
\]

and therefore

\[
A=1,\qquad B=4.
\]

The powered rectangle has order four. Its three nonidentity elements are
positive separators, giving exact uniform direct success

\[
\delta_N=\frac34.
\]

The special feedback subgroup \(K=\langle11,2\rangle\) has exponent \(22\).
Since

\[
22\mid2046=N-1,
\]

its \((N-1)\)-power image is trivial. This does not conflict with the full
unit-group image: the latter has a surviving order-four component from the
\(q\)-side. The phase witness remains valid as a subgroup-operation witness,
while bare \(N=2047\) is easy for this broader exact source.

## 11. Exact scope of the pass

For every product of two distinct odd primes, bare \(N\) supplies exact
uniform samples from a nontrivial cyclic rectangle. Two such samples
generate the full rectangle with probability at least \(6/\pi^2\). All
source operations are public and have polynomial expected bit complexity.

This is a genuine all-input generator-source theorem for that input class.
It is not an axis-localization theorem. It does not guarantee
inverse-polynomial direct gcd density, expose \(A\) or \(B\), compute group
orders or useful exponent relations, factor prime powers or composites with
more than two prime factors, simulate quantum order finding, or give a
complete factoring algorithm.

Subject to the exact-versus-near-uniform wording correction in Section 7,
the candidate's theorem and reduction pass.
