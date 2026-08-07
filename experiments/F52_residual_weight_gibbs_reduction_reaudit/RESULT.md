# Fresh hostile re-audit of F52

## Disposition

I audited
`experiments/F52_residual_weight_gibbs_reduction/RESULT.md` at the pinned
SHA-256

```text
4b9e7191ac69298fd3f2fe3a64fba35439c67d6fb726f62aed7652480a59b351
```

and read the preserved failed audit at SHA-256

```text
4d830ab8cbcb4a5b5e6cd23b2ba2fdf9cd2c5a7a8df046a1968d700eaae24124
```

The pinned hash matches. The exact target, conditional laws, local-chain
hazard, tail bound, expectation bound, and balanced-family counts are correct.
All five corrections requested by the first audit appear in the new text.

The candidate still fails as written as an algorithmic reduction from bare
input \(N\). It takes a description of \(w_N\) as supplied input but does not
require that description to be generated uniformly from \(N\), in polynomial
time, without factor-dependent advice. The words “public” and “factor-free” do
not state this condition. A short supplied description can contain a factor.
The result is therefore an exact sampler-oracle reduction as written, not yet a
classical factoring algorithm from bare \(N\).

There is also one scope inconsistency about warm starts. The proved hazard
bound covers every safe initial law, including a nontrivial safe warm start,
for the named gcd screen. The opening says that nontrivial warm starts are not
covered. What remains outside the theorem is a factor-bearing construction of
the warm start or a different decoder, not the safe initial law itself.

## 1. Target and arbitrary-weight conditionals

Identify the multiplication graph with \(R^2\), where
\(R=\mathbb Z/N\mathbb Z\), by

\[
(k,x)\longmapsto(k,x,kx).
\]

The unnormalized state mass is \(w(kx)\). Thus

\[
Z_w=\sum_{k,x\in R}w(kx)
   =\sum_{d\in R}M_N(d)w(d).
\]

Since \(w(0)>0\), the zero-residual event has positive mass. Every state in
that event has the same mass \(w(0)\), so conditioning on it gives the uniform
law on

\[
\Omega_N=\{(k,x):kx=0\pmod N\}.
\]

Holding \(x=b\), the exact conditional is

\[
Q_{b,w}(a)=\frac{w(ab)}{Z_b},
\qquad Z_b=\sum_{y\in R}w(yb).
\]

This remains defined when \(w\) has zero values: the term \(y=0\) gives
\(Z_b\ge w(0)>0\) for every \(b\). Zero weights can remove states from the
target support, but they do not invalidate the conditional formula.

If \(b\) is a unit, multiplication by \(b\) permutes \(R\). Hence \(Z_b=W\),
where \(W=\sum_dw(d)\), and \(D=ab\) has law

\[
\nu_w(d)=w(d)/W.
\]

If \(b=0\), then every candidate residual is zero and

\[
Q_{0,w}(a)=\frac{w(0)}{Nw(0)}=\frac1N.
\]

These identities use neither stationarity nor mixing. They also distinguish
the target's residual marginal, which is proportional to \(M_N(d)w(d)\),
from the unit-held conditional residual law \(\nu_w\). The proof uses the
latter.

## 2. Direct conditional-oracle reduction

Let

\[
H_N=\{d:1<\gcd(d,N)<N\},
\qquad
\theta_w=\nu_w(H_N).
\]

At the public held coordinate \(b=1\), an exact conditional call returns
\(D\sim\nu_w\). A gcd succeeds with exact probability \(\theta_w\). Fresh
independent calls therefore use \(1/\theta_w\) calls in expectation when
\(\theta_w>0\).

If one call has expected bit cost \(T(N)\), its runtime can be correlated with
its own output. This does not change the total-cost identity. The event that
call \(i\) is reached depends only on earlier calls, so

\[
\mathbb E\!\left[\sum_{i=1}^{G}C_i\right]
=\sum_{i\ge1}(1-\theta_w)^{i-1}\mathbb E C_i
=\frac{T(N)}{\theta_w}.
\]

The candidate correctly states that point evaluation of \(w_N\), a succinct
formula, and knowledge of a normalizer are not the same as an exact sampler.
It also correctly requires almost-sure termination plus expected bit and
fair-bit bounds for the exact conditional routine.

However, lines 145--165 and 235--238 do not close the input interface. The
routine takes both \(N\) and “a finite public description of \(w_N\).” Nothing
formally requires a polynomial-time, factor-free map

\[
N\longmapsto \operatorname{desc}(w_N),
\]

nor says that the description is a fixed uniform part of the algorithm rather
than auxiliary advice.

Here is an explicit hostile instance. For each composite \(N\), select a proper
divisor \(g_N\) nonuniformly and supply the description

\[
w_N(0)=1,
\qquad w_N(g_N)=1,
\qquad w_N(d)=0\ \text{otherwise}.
\]

One uniform fair-bit routine reads the supplied \(g_N\), flips one bit, and
returns either \(0\) or \(g_N\). It is exact, public once the description is
given, and costs \(O(\log N)\) bit operations with
\(\theta_{w_N}=1/2\). The gcd reduction then factors \(N\), but only because
the supplied description already carries nonuniform factor advice. Calling
the routine “factor-free” does not formally exclude this input.

Thus the mathematical implication is presently:

> Given an exact \(Q_{1,w_N}\) sampler and its description, useful
> \(\theta_{w_N}\) gives a direct factoring sampler relative to that supplied
> resource.

For a classical bare-\(N\) factoring conclusion, the candidate must also
require that the description is fixed uniformly or is produced from \(N\) by
a public factor-free polynomial-time algorithm, with its size and construction
cost included in the bit bound. This is not cosmetic: it separates a sampler
construction from sampler advice.

## 3. Pathwise hazard, tail, and expectation

Assume the initial state is safe for the named coordinate and residual gcd
screens. Before the first success, every free coordinate is either zero or a
unit. Indeed, failure of the gcd screen means
\(\gcd(a,N)\in\{1,N\}\), and the second case is exactly \(a=0\) in \(R\).

Conditional on every complete survival history:

- a unit-held refresh succeeds with exact probability \(\theta_w\), because
  unit multiplication preserves gcd;
- a zero-held refresh succeeds with exact probability \(h_N/N\), where
  \(h_N=|H_N|\); the residual itself remains zero.

Therefore every next-step conditional hazard is at most

\[
\rho_w=\max\{\theta_w,h_N/N\}.
\]

This argument allows deterministic scan, random scan, any past-measurable scan
choice, and laziness. It does not allow a choice made after inspecting a
proposal, because that changes the kernel. Induction gives

\[
\Pr(\tau>t)\ge(1-\rho_w)^t,
\qquad
\Pr(\tau\le t)\le1-(1-\rho_w)^t\le t\rho_w.
\]

For \(\rho_w>0\), tail summation gives

\[
\mathbb E\tau\ge\sum_{t\ge0}(1-\rho_w)^t=1/\rho_w.
\]

No independence between successive chain states is used. If \(N\) is prime,
then \(h_N=\theta_w=0\), and the stopping time is infinite, as it must be.

The statement “for every safe initial law” proves more than the scope sentence
at line 23. A special but safe warm start cannot defeat this coordinate-gcd
hazard. A warm start remains open only if its construction already reveals a
factor or if another decoder reads factor information from it.

## 4. Balanced families and endpoint regimes

For distinct primes \(p<q\), the nonzero multiples of \(p\) and \(q\) are
disjoint, so

\[
h_{pq}=(q-1)+(p-1)=p+q-2.
\]

If \(q/p\le C\), this gives \(h_N/N=O_C(N^{-1/2})\). For \(N=p^2\), the
proper nonunits are the \(p-1\) nonzero multiples of \(p\), so

\[
h_N=p-1,
\qquad h_N/N<N^{-1/2}.
\]

The formulas include \(p=2\): \(H_4=\{2\}\), and for a distinct semiprime
\(N=2q\), \(h_N=q\). For \(N=2\), \(H_N\) is empty, as covered by the prime
case.

On either growing balanced composite family, \(h_N/N\) is negligible in the
input length. Hence negligible \(\theta_{w_N}\) gives negligible success in
every polynomial number of named local updates and a superpolynomial
expectation lower bound. If

\[
\theta_{w_N}=O(N^{-1/2}\operatorname{poly}(\log N)),
\]

then

\[
\mathbb E\tau
=\Omega\!\left(N^{1/2}/\operatorname{poly}(\log N)\right).
\]

The candidate now says “at least,” so it no longer asserts an unproved matching
upper bound. It also labels the useful-mass and negligible-mass cases as two
endpoint regimes and explicitly leaves intermediate, oscillating, and
nonuniform cases to the pointwise bound. The false dichotomy is repaired.

## 5. No-amplification scope

The corrected title and conclusion state the exact narrow result. The named
one-coordinate Gibbs wrapper adds no monitored per-step gcd hazard beyond

\[
\max\{\theta_w,h_N/N\}.
\]

The second term matters. For example, if \(w\) is supported only at zero, then
\(\theta_w=0\), but a zero-held refresh is uniform and can hit a proper
nonunit. The candidate now includes this exception and no longer claims that
the chain cannot create any factor mass absent from \(\nu_w\).

The proof does not rule out a useful residual law. If such a law is uniformly
constructible and exactly sampleable from bare \(N\), it is already a direct
positive factoring sampler. The proof only removes extra amplification by the
named local wrapper. It does not cover joint moves, joint \((k,x)\)-dependent
weights, interacting residuals, lifts, nonlocal proposals, transcript
decoders, or other arithmetic tests. It makes no mixing claim.

## Required repair

1. Separate the exact sampler-oracle reduction from a bare-input algorithm.
   For the latter, require a fixed uniform public rule for \(w_N\), or a public
   factor-free polynomial-time construction of \(\operatorname{desc}(w_N)\)
   from \(N\). Bound the description size and include its construction cost.
2. Replace the broad warm-start exclusion with the exact boundary: the hazard
   theorem covers every safe warm start for the named gcd screens; only its
   factor-bearing construction or a different decoder is outside scope.

The first repair is necessary for the claimed classical factoring conclusion.
The second removes an internal scope contradiction.

## Final verdict

**FAIL AS WRITTEN**
