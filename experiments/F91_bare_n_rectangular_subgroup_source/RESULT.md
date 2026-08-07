# F91 — bare N gives constant-probability generators of a factor-bearing rectangle

**Status:** proof-only candidate. No research computation was run. This is
an all-input subgroup-source theorem for distinct odd semiprimes and an exact
reduction to axis localization. It is not an axis decoder or a factoring
algorithm.

## 1. Material difference

P83 shows that near-uniform sampling from any supplied public subgroup is
easy, but does not supply a factor-bearing subgroup. F89 proves that the
\((N-1)\)-power image of any supplied subgroup is a full rectangle with
coprime hidden projection orders, but does not show that a small public
generator list reaches the full image of the unit group.

The present result closes that source question for the full powered image.
Two random units, followed by the single public power \(N-1\), generate the
entire factor-bearing rectangle with probability at least

\[
\boxed{6/\pi^2>0.6.}
\]

Thus neither a novel subgroup sampler nor a large seed pool is missing. The
remaining task is to localize one of the two coordinate axes from a constant
number of public generators.

## 2. The canonical powered rectangle

Let

\[
N=pq
\]

for distinct odd primes, and write

\[
G=(\mathbb Z/N\mathbb Z)^\times
\cong\mathbb F_p^\times\times\mathbb F_q^\times.
\]

Put

\[
g=\gcd(p-1,q-1),
\qquad
A=\frac{p-1}{g},
\qquad
B=\frac{q-1}{g}.
\tag{1}
\]

Then

\[
\gcd(A,B)=1.
\tag{2}
\]

Define the public power image

\[
S_N=G^{N-1}.
\tag{3}
\]

### Theorem 1

The subgroup in (3) is exactly

\[
\boxed{S_N\cong C_A\times C_B\cong C_{AB}.}
\tag{4}
\]

It is nontrivial. It contains exactly

\[
\boxed{A+B-2}
\tag{5}

positive separators, with uniform density

\[
\boxed{
\delta_N
=
\frac1A+\frac1B-\frac2{AB}.
}
\tag{6}

### Proof

The local power-image order at \(p\) is

\[
\frac{p-1}{\gcd(p-1,N-1)}.
\]

The identity

\[
N-1=q(p-1)+(q-1)
\]

gives

\[
\gcd(p-1,N-1)=\gcd(p-1,q-1)=g.
\]

The other side is symmetric. Hence the two local image orders are exactly
\(A,B\). F89's rectangularization theorem, or its direct surjective-
projection proof, gives the full product. Equation (2) makes that product
cyclic.

If \(S_N=1\), then \(A=B=1\), so \(p-1=q-1\) and \(p=q\), contrary to the
distinct-prime premise. Thus \(S_N\ne1\). The separator count and density are
the two nonidentity coordinate axes in the full product. \(\square\)

## 3. Two public samples generate the full rectangle with constant probability

Sample \(a\) uniformly from \(\{1,\ldots,N-1\}\) and compute
\(d=\gcd(a,N)\). A proper \(d\) already factors \(N\). Otherwise, conditioned
on \(d=1\), the residue \(a\) is uniform in \(G\). The homomorphism

\[
a\longmapsto a^{N-1}
\]

therefore sends it to an exactly uniform element of \(S_N\).

Take two independent accepted units and put

\[
y_1=a_1^{N-1},
\qquad
y_2=a_2^{N-1}.
\tag{7}
\]

### Theorem 2

The public pair in (7) satisfies

\[
\boxed{
\Pr\bigl(\langle y_1,y_2\rangle=S_N\bigr)
=
\prod_{\ell\mid AB}\left(1-\frac1{\ell^2}\right)
\ge
\frac6{\pi^2}.
}
\tag{8}

The empty product is not needed because \(AB>1\).

### Proof

Write the cyclic group \(S_N\) additively as \(C_{AB}\). For a prime
\(\ell\mid AB\), two uniform elements fail to generate the
\(\ell\)-primary quotient exactly when both lie in the unique subgroup of
index \(\ell\). This event has probability \(\ell^{-2}\).

The primary coordinates of uniform elements are independent under the
Chinese remainder decomposition of the cyclic group. Therefore the joint
generation probability is the product in (8). Finally,

\[
\prod_{\ell\mid AB}\left(1-\ell^{-2}\right)
\ge
\prod_{\ell\text{ prime}}\left(1-\ell^{-2}\right)
=
\frac1{\zeta(2)}
=
\frac6{\pi^2}.
\]

This proves (8). \(\square\)

Sampling accepted units has constant expected overhead. For distinct odd
primes,

\[
\frac{\varphi(N)}{N-1}
=
\frac{(p-1)(q-1)}{pq-1}
>\frac12.
\]

Every gcd, modular power, and random integer uses polynomial bit complexity.
Thus bare \(N\) produces a two-element public generating set for \(S_N\)
with constant probability and polynomial work.

## 4. Exact axis-localization reduction

Define the following promise task.

**Powered-rectangle axis localization.** Given an odd composite \(N\) and a
public list that generates \(S_N=G^{N-1}\) for a distinct-prime semiprime,
return an element \(z\) of the generated subgroup such that

\[
1<\gcd(z-1,N)<N.
\]

The output is publicly verified. On a list that does not generate the full
rectangle, an algorithm may return failure, but it must remain polynomially
bounded and may return only a verified factor.

### Corollary 3

If powered-rectangle axis localization has a polynomial-time algorithm with
inverse-polynomial success on every promised input, then distinct odd
semiprimes can be factored by a classical Las Vegas algorithm in expected
polynomial time.

### Proof

Generate fresh pairs (7), run the promised decoder, and verify every output.
By Theorem 2, each pair satisfies the promise with probability at least
\(6/\pi^2\). Conditional decoder success remains inverse polynomial, so a
fresh batch has inverse-polynomial verified success. Independent repetition
is Las Vegas and has polynomial expected cost. \(\square\)

The reduction does not need to recognize whether a sampled pair generated
\(S_N\). Failed batches are harmless because work is bounded and outputs are
verified.

## 5. Why the sampler does not already factor

Fresh accepted-unit powers are exactly uniform on \(S_N\), so their direct
gcd success is exactly (6). Once \(y_1,y_2\) generate \(S_N\), public bounded
random exponent combinations can instead sample within any requested total-
variation error \(\eta\); their success probability is within \(\eta\) of
(6). If \(A,B\ge2\), then

\[
\delta_N\ge\frac1{\min\{A,B\}},
\]

but there is no theorem here that \(\min\{A,B\}\) is polynomial in
\(\log N\). Both hidden orders can be large.

The group \(S_N\) is cyclic of order \(AB\). Its two axes are the unique
subgroups of orders \(A\) and \(B\). A short public generator list proves
that every axis element has a short exponent representation, but does not
reveal the required exponents. Finding them is an order/decomposition
problem. A fixed sparse word menu can still miss both axes, as the abstract
P85 obstruction predicts.

Thus the missing object is not a better near-uniform sampler. It is a
nonuniform decoder that localizes one hidden coordinate kernel from a small
generating set, or a new feedback/refinement step that changes this
coprime-order rectangle.

## 6. The two retained examples are globally easy for this source

### N=4033

For \(p=37,q=109\),

\[
g=36,
\qquad
A=1,
\qquad
B=3.
\]

Every nonidentity element of \(S_N\) is an axis element. The retained
feedback block 5 gives

\[
\gcd(5^{4032}-1,4033)=37.
\]

### N=2047

For \(p=23,q=89\),

\[
g=22,
\qquad
A=1,
\qquad
B=4.
\]

A uniform powered unit therefore gives a proper gcd with probability

\[
\frac34.
\]

The special feedback subgroup \(\langle11,2\rangle\) is killed by
\(N-1\), but the full unit-group image is not. Thus the phase witness remains
a valid operation witness while the integer \(2047\) itself is easy for the
broader bare-\(N\) source.

## 7. Exact scope

The theorem gives an all-input, factor-free, constant-probability source of
public generators for a subgroup that is guaranteed to contain factors on
its two axes. This is a genuine source theorem.

It does not localize an axis when both \(A\) and \(B\) are large. It does not
prove an inverse-polynomial direct-gcd density, compute \(A,B\), compute the
group order, recover a useful exponent relation, simulate Shor's order
finding, handle prime powers or more than two prime components, or give a
complete factoring algorithm. No computational lower bound or literature
novelty is claimed.
