# Second fresh hostile re-audit of F52

## Disposition

I audited
experiments/F52_residual_weight_gibbs_reduction/RESULT.md at SHA-256

    e2c9fcba130bb64b21c5f53dfac546cebf1b4a70603fb072f642518d1a8e1826

The hash matches the requested artifact. I also read both preserved failed
audits in full:

    4d830ab8cbcb4a5b5e6cd23b2ba2fdf9cd2c5a7a8df046a1968d700eaae24124
      experiments/F52_residual_weight_gibbs_reduction_audit/RESULT.md
    bbbdea3abe7373c86d50b52de3a34aed2657d5dc00a2666281dd1897f5507ec6
      experiments/F52_residual_weight_gibbs_reduction_reaudit/RESULT.md

I re-derived every displayed identity and bound. I checked the quantifiers,
the bare-input algorithm interface, expected bit and fair-bit costs, safe warm
starts, sparse weights, prime and composite edge cases, adaptive scan, both
balanced families, and the stated framework boundary. I also tried the two
earlier hostile constructions: a weight description carrying a supplied
factor, and a nontrivial safe warm start. The latest corrections close both
gaps.

The result is correct as written. There are no mandatory corrections.

## 1. Target and conditional laws

Let \(R=\mathbb Z/N\mathbb Z\). Identifying the multiplication graph with
\(R^2\), a state \((k,x)\) has unnormalized mass \(w(kx)\). Therefore

\[
Z_w=\sum_{k,x\in R}w(kx)
   =\sum_{d\in R}M_N(d)w(d).
\]

The hypothesis \(w(0)>0\) has two necessary effects. First, the zero-residual
event has positive target mass. Every state in that event has the same mass
\(w(0)\), so the conditional target is uniform on

\[
\Omega_N=\{(k,x):kx=0\pmod N\}.
\]

Second, every one-coordinate conditional is defined, including for weights
with zeros, because

\[
Z_b=\sum_{y\in R}w(yb)\ge w(0)>0.
\]

Holding \(x=b\), the conditional

\[
Q_{b,w}(a)=\frac{w(ab)}{Z_b}
\]

is exact. If \(b\) is a unit, multiplication by \(b\) permutes \(R\). Hence
\(Z_b=W\), and the new residual \(D=ab\) has law

\[
\nu_w(d)=\frac{w(d)}W.
\]

If \(b=0\), every candidate residual is zero and

\[
Q_{0,w}(a)=\frac{w(0)}{Nw(0)}=\frac1N.
\]

No stationarity, irreducibility, or mixing claim is used. An initial state can
even have zero target mass: the next conditional remains defined because
\(Z_b>0\) for every held value \(b\).

## 2. Factor mass and the direct bare-input reduction

Let

\[
H_N=\{d:1<\gcd(d,N)<N\},
\qquad
\theta_w=\nu_w(H_N).
\]

Unit multiplication preserves every common divisor with \(N\). Thus a
unit-held refresh makes both the refreshed coordinate and its residual proper
nonunits with exact probability \(\theta_w\). At the public held value \(1\),
the coordinate itself has law \(\nu_w\). Independent exact calls followed by a
gcd therefore need exactly \(1/\theta_w\) calls in expectation when
\(\theta_w>0\).

The corrected algorithmic quantifier is sufficient. One fixed uniform public
algorithm takes only \(N\). It constructs a polynomial-size description of
\(w_N\), exactly samples \(Q_{1,w_N}\), receives no auxiliary description or
advice, and has one expected polynomial bound for all construction, bit, and
fair-bit costs. Hence a short factor-bearing description cannot be inserted as
nonuniform input. Its construction time cannot be hidden either.

If

\[
\theta_{w_N}\ge 1/\operatorname{poly}(\log N)
\]

uniformly on the named input family, repeating the uniform algorithm gives a
classical expected-polynomial factor finder from bare \(N\). If \(T(N)\) is
the stated per-call cost bound, the candidate's displayed quantity

\[
\frac{T(N)+\operatorname{poly}(\log N)}{\theta_{w_N}}
\]

is a valid expected-cost bound. Reconstructing the description on every call
only makes this a conservative bound; constructing it once can be cheaper.
Correlation between one call's output and its own runtime causes no problem:
whether that call is reached depends only on prior independent calls.

The earlier hostile advice example is now excluded. If a supplied description
encodes a divisor \(g_N\), it violates both “takes only \(N\)” and “no auxiliary
description or advice.” If a uniform expected-polynomial construction from
\(N\) itself finds and encodes \(g_N\), then that construction is already an
expected-polynomial factoring algorithm, so it is not a counterexample to the
corollary.

The text also correctly avoids deriving an exact sampler from point evaluation
or from a succinct formula for an arbitrary real-valued weight.

## 3. Pathwise obstruction and warm starts

Call an initial state safe when neither free coordinate nor its derived
residual gives a proper gcd. Before the first monitored success, failure of a
coordinate gcd screen implies

\[
\gcd(a,N)\in\{1,N\}.
\]

In \(R\), these cases mean that \(a\) is a unit or \(a=0\). Thus, conditional
on every complete survival history, the coordinate held for the next refresh
is either a unit or zero.

- If it is a unit, the next-step success probability is exactly
  \(\theta_w\).
- If it is zero, the refreshed coordinate is uniform, the residual remains
  zero, and the next-step success probability is exactly \(h_N/N\).

Therefore every conditional hazard is at most

\[
\rho_w=\max\{\theta_w,h_N/N\}.
\]

This argument remains valid for deterministic scan, random scan,
past-measurable adaptive scan, and laziness. A choice made after inspecting a
proposal would define a different kernel and is not claimed.

Induction on complete survival histories gives

\[
\Pr(\tau>t)\ge(1-\rho_w)^t,
\]

and hence

\[
\Pr(\tau\le t)
\le 1-(1-\rho_w)^t
\le t\rho_w.
\]

For \(\rho_w>0\), tail summation gives

\[
\mathbb E\tau
\ge\sum_{t\ge0}(1-\rho_w)^t
=\frac1{\rho_w}.
\]

No independence between successive chain states is needed. If \(\rho_w=0\),
the monitored hit never occurs, which is consistent with the omitted limiting
case.

The corrected scope now matches this proof. It says that every safe
warm-start law is covered for the named coordinate and residual gcd screens.
A special safe distribution cannot exceed the pathwise hazard. What remains
outside scope is the separate act of constructing a warm start that already
reveals a factor, or applying a different decoder to information in that warm
start. The earlier warm-start objection is therefore resolved.

## 4. Counts and balanced endpoint regimes

For \(N=pq\), with distinct primes \(p<q\), the proper nonunits are the
\(q-1\) nonzero multiples of \(p\) and the \(p-1\) nonzero multiples of \(q\).
These sets are disjoint, so

\[
h_{pq}=p+q-2.
\]

If \(q/p\le C\), then \(p\ge\sqrt{N/C}\), and therefore

\[
\frac{h_N}{N}=O_C(N^{-1/2}).
\]

For \(N=p^2\), the proper nonunits are the \(p-1\) nonzero multiples of \(p\),
so

\[
h_N=p-1,
\qquad
\frac{h_N}{N}<N^{-1/2}.
\]

These counts also cover \(p=2\). On either growing composite family,
\(h_N/N\) is negligible as a function of the input length. Thus negligible
\(\theta_{w_N}\) makes \(\rho_w\) negligible. The union bound gives negligible
success for every polynomial number of named local refreshes, and
\(1/\rho_w\) is superpolynomial.

If instead

\[
\theta_{w_N}
=O\!\left(N^{-1/2}\operatorname{poly}(\log N)\right),
\]

then the same estimate holds for \(\rho_w\), so

\[
\mathbb E\tau
=\Omega\!\left(
  N^{1/2}/\operatorname{poly}(\log N)
\right).
\]

The candidate states this only as a lower bound. It does not assert a matching
upper bound. It also calls the useful-mass and negligible-mass cases endpoint
regimes, not an exhaustive dichotomy. Intermediate and oscillating cases
remain governed by the exact pointwise bound.

## 5. Hostile edge cases and framework boundary

- If \(w\) is supported only at zero, then \(\theta_w=0\). A zero-held refresh
  can still hit \(H_N\) at density \(h_N/N\). The title, theorem, and conclusion
  all retain this second source.
- If \(w\) has arbitrary zero values away from zero, every denominator remains
  positive. Sparse support does not break the proof.
- If \(N\) is prime, then \(H_N\) is empty and both hazards are zero. The
  stopping time is infinite. For every composite \(N\), \(h_N>0\).
- Monitoring the residual adds no hidden event. At a unit-held update,
  coordinate and residual success are equivalent. At a zero-held update, the
  residual is zero.
- A scan that never refreshes one coordinate, or that is arbitrarily lazy, can
  make the true hitting time larger or infinite. This is compatible with the
  lower bound.

The framework consequence is no broader than the proof. It removes extra
amplification by the named one-coordinate, residual-only Gibbs wrapper. It
does not rule out finding a uniformly constructible residual law with useful
factor mass. Such a law would itself be the positive direct sampler. It also
does not cover joint moves, joint \((k,x)\)-dependent weights, interacting
residuals, lifts, nonlocal proposals, transcript decoders, or other arithmetic
tests.

## Mandatory corrections

None.

## Final verdict

**PASS**
