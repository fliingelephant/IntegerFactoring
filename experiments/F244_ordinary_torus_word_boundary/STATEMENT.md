# F244 candidate — the ordinary–torus square word has an exact conservation law, but signed power words can miss all four shifted orders

## Status and scope

This is a candidate proof packet for distinct odd semiprimes.  It has been
self-audited but has not had a hostile audit or a blind reconstruction.  It
contains one unconditional positive bridge and one infinite-family
obstruction to a named public-word grammar.  It is not an all-input factoring
algorithm and not a factoring lower bound.

Let

\[
N=pq
\]

for distinct odd primes `p` and `q`.  For signs `a,b in {+1,-1}`, put

\[
m_{p,a}=p-a,\qquad m_{q,b}=q-b,\qquad
d_{a,b}=\gcd(m_{p,a},m_{q,b}).                       \tag{1}
\]

Also put

\[
A=p^2-1,\qquad B=q^2-1,\qquad G=\gcd(A,B),           \tag{2}
\]

\[
U=v_2(A),\qquad V=v_2(B),\qquad
\delta=\mathbf 1_{U\ne V}.                          \tag{3}
\]

## 1. Exact common-capacity and residual identities

The combined capacity of all four shifted common divisors is

\[
\boxed{
\operatorname{lcm}_{a,b\in\{\pm1\}}d_{a,b}={G\over2}.
}                                                     \tag{4}
\]

Define the four square-word residuals

\[
t_{p,a}={p-a\over\gcd(p-a,B)},\qquad
t_{q,b}={q-b\over\gcd(q-b,A)}.                       \tag{5}
\]

These four positive integers are pairwise coprime, including at the prime
two, and

\[
\boxed{
\prod_{a\in\{\pm1\}}t_{p,a}
\prod_{b\in\{\pm1\}}t_{q,b}
={AB\over 2^\delta G^2}.
}                                                     \tag{6}
\]

Consequently

\[
\boxed{
\min(t_{p,+},t_{p,-},t_{q,+},t_{q,-})
< {\sqrt N\over 2^{\delta/4}\sqrt G}.
}                                                     \tag{7}
\]

This is a square-root bound.  It does not imply a quarter-power bound or a
numerical-quasipolynomial residual.

## 2. One public square exponent for all torus orientations

In the F242 quadratic-torus notation, an orientation `(a,b)` has public
Jacobi sign `J=ab` and base exponent `N-J`.  Choose the public unfactored
word

\[
W_J=N+J.
\]

Then every orientation uses the same exponent

\[
E=(N-J)W_J=N^2-1.                                    \tag{8}
\]

The two exact local residuals are `t_{p,a}` and `t_{q,b}` from (5).
For a fresh uniform discriminant retained through the clean F242 sampler,
the four orientations are equiprobable.  The clean powered factor
probability therefore obeys

\[
\Pr(\text{factor})
\ge {1\over8}\sum_{z\in
 \{t_{p,+},t_{p,-},t_{q,+},t_{q,-}\}}{1\over z}
\ge {1\over2\left(\prod z\right)^{1/4}},             \tag{9}
\]

and hence

\[
\boxed{
\Pr(\text{factor})
>{2^{\delta/4-1}\sqrt G\over\sqrt N}.
}                                                     \tag{10}
\]

This is an exact unconditional bridge from the four shifted orders to one
`O(log N)`-bit exponent.  Its worst-case bound is still exponentially small
in the input length.

## 3. Exact signed-power support law

Let `ell` be an odd prime not dividing `N`, and let

\[
h=\operatorname{ord}_\ell(N).
\]

For every positive integer `k`,

\[
v_\ell(N^k-1)=
\begin{cases}
0,&h\nmid k,\\
v_\ell(N^h-1)+v_\ell(k/h),&h\mid k,
\end{cases}                                          \tag{11}
\]

and

\[
v_\ell(N^k+1)=
\begin{cases}
v_\ell(N^{h/2}+1)+v_\ell(u),
 &h\text{ even and }k=(h/2)u\text{ with }u\text{ odd},\\
0,&\text{otherwise}.
\end{cases}                                          \tag{12}
\]

In particular, if `ell | p-a`, then `N = aq (mod ell)`.  Thus the signed
power support on that local shifted order is controlled exactly by the
order of `aq` modulo `ell`.  The analogous statement for `ell | q-b` uses
the order of `bp`.

## 4. Infinite exact obstruction to short signed-power words

There is an absolute constant `c>0` and an infinite family of distinct odd
semiprimes `N=pq`, with input length

\[
n=\lceil\log_2(N+1)\rceil,
\]

having four distinct primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{cn}             \tag{13}
\]

such that

\[
\lambda_a\mid p-a,\qquad
\rho_b\mid q-b,                                      \tag{14}
\]

\[
\operatorname{ord}_{\lambda_a}(q)=\lambda_a-1,
\qquad
\operatorname{ord}_{\rho_b}(p)=\rho_b-1,             \tag{15}
\]

and the four shifted common divisors are exactly

\[
\boxed{
d_{+,+}=2,\qquad d_{+,-}=12,\qquad
d_{-,+}=2,\qquad d_{-,-}=2.
}                                                     \tag{16}
\]

Thus `G=24`, and even the lcm of every possible exact common order from all
four ordinary or torus orientations divides `12`.

Fix any numerical-quasipolynomial function `Q`.  On every sufficiently
large member of this one family, every positive integer word of the form

\[
W=\prod_{j=1}^{s}\lvert N^{k_j}-\sigma_j\rvert^{e_j},
\qquad
k_j,e_j\ge1,\quad \sigma_j\in\{+1,-1\},              \tag{17}
\]

whose binary length is at most `Q(n)`, satisfies

\[
\boxed{
\gcd(W,\lambda_+\lambda_-\rho_+\rho_-)=1.
}                                                     \tag{18}
\]

This statement is independent of how the signed factors in (17) are
selected.  It therefore also covers adaptive selection, provided the final
word has the displayed grammar and numerical-quasipolynomial bit length.

For every F242 orientation `(a,b)`, the local residual after its base
`N-ab` and any word (17) is divisible by both `lambda_a` on the `p` side
and `rho_b` on the `q` side.  Hence its clean powered factor probability is
at most

\[
{1\over\lambda_a}+{1\over\rho_b}\le2^{1-cn}.          \tag{19}
\]

The incidental random zero-divisor screens have the same exponential scale
on this family.  A numerical-quasipolynomial number of these signed-word
trials therefore does not solve the family.

Even if all sign labels and all common capacities are granted, combining
them with a known dyadic residue modulo `2^t` gives modulus at most

\[
\operatorname{lcm}(2^t,12)=3\cdot2^t\qquad(t\ge2).    \tag{20}
\]

Thus this family permits only a constant-factor enlargement of the
quarter-bit terminal through accumulated ordinary and torus common orders.

## Exact boundary

The positive result is (4)--(10): ordinary and torus orientations collapse
to the public exponent `N^2-1`, with an exact pairwise-coprime residual
conservation law.  The negative result is restricted to products of signed
powers `N^k +/- 1` and to common-order accumulation.  It does not cover
difference words, discriminant-dependent integer data outside this grammar,
carry words, quotient words, retained multiplicative relations, or another
factoring mechanism.
