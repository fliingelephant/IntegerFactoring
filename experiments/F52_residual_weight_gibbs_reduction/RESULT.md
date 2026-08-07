# F52 — residual-only local Gibbs cannot amplify beyond two explicit sources

## Status and scope

**Status:** twice-corrected candidate exact oracle reduction and pathwise
obstruction. The first hostile audit passed the core theorem and required five
scope and wording corrections. A fresh re-audit then found that the bare-input
algorithmic corollary did not require the weight description itself to be
generated uniformly from \(N\). Both failed audits are preserved, and all
corrections are included below.

**Family:** F23, as a direct extension of P59/X53.

This result allows an arbitrary nonnegative residual weight \(w(d)\). It does
not assume the two-sector scalar form treated by P59. The exact conclusion is
that the local Gibbs wrapper adds no per-step coordinate-gcd success beyond the
larger of two sources: factor mass already present in the weighted residual law,
and the raw proper-nonunit density exposed by a zero-held uniform refresh. If
the first source has useful mass and its conditional has a uniform public
polynomial-cost implementation, that conditional already factors directly.

The theorem concerns one-free-coordinate Gibbs updates and coordinate or
residual gcd extraction. It covers every safe warm-start law for those screens.
It does not cover a joint block move, a weight that depends on \((k,x)\) beyond
their product, several interacting residuals, valuation-amplifying lifts,
transcript decoders, a warm-start construction which already exposes a factor,
or a different decoder applied to a warm start.

## 1. Target and exact conditional law

Let \(N\ge2\), let \(R=\mathbb Z/N\mathbb Z\), and let

\[
w:R\longrightarrow\mathbb R_{\ge0}
\]

satisfy \(w(0)>0\). Put

\[
W=\sum_{d\in R}w(d)>0.
\]

Use the graph of multiplication

\[
\widehat\Omega_N=\{(k,x,d)\in R^3:d=kx\}.
\]

The free coordinates are \(k,x\); the residual \(d\) is recomputed after every
refresh. Give a state unnormalized weight \(w(d)\). Its normalizer is

\[
Z_w=\sum_{k,x\in R}w(kx)
    =\sum_{d\in R}M_N(d)w(d),
\]

where

\[
M_N(d)=|\{(k,x)\in R^2:kx=d\}|.
\]

Conditioned on \(d=0\), every state has the same positive weight \(w(0)\).
Therefore the conditional target is exactly uniform on

\[
\Omega_N=\{(k,x):kx=0\pmod N\}.
\tag{1.1}
\]

Holding \(x=b\), the exact Gibbs conditional for a refreshed \(k\) is

\[
Q_{b,w}(a)
=\frac{w(ab)}{Z_b},
\qquad
Z_b=\sum_{y\in R}w(yb).
\tag{1.2}
\]

The \(x\)-refresh is symmetric. The theorem below is mathematical for every
such weight. An algorithmic claim requires an exact implementation of the
conditional sampler; no generic method for summing or sampling an arbitrary
succinctly described \(w\) is assumed.

## 2. Unit and zero conditionals

Define the normalized residual law

\[
\nu_w(d)=\frac{w(d)}W.
\tag{2.1}
\]

If \(b\in R^\times\), multiplication by \(b\) is a permutation of \(R\).
Thus \(Z_b=W\), and under (1.2) the residual

\[
D=Kb
\]

has exactly the law \(\nu_w\). Equivalently, one may first sample
\(D\sim\nu_w\) and then set \(K=Db^{-1}\). In particular, at the public held
coordinate \(b=1\), the refreshed coordinate itself has law \(\nu_w\).

If \(b=0\), then \(ab=0\) for every \(a\in R\). Since \(w(0)>0\), (1.2) is
exactly uniform on \(R\), independently of every other value of \(w\).

These two identities are exact and require no mixing or asymptotic argument.

## 3. Factor mass and direct reduction

Let

\[
H_N=\{a\in R:1<\gcd(a,N)<N\},
\qquad h_N=|H_N|,
\]

and put

\[
\theta_w=\nu_w(H_N)
=\frac{\sum_{d\in H_N}w(d)}W.
\tag{3.1}
\]

Multiplication by a unit preserves gcd with \(N\). Therefore a refresh while
holding a unit creates a proper-nonunit coordinate, or equivalently a
proper-nonunit residual, with exact probability \(\theta_w\). A refresh while
holding zero creates a proper-nonunit coordinate with exact probability

\[
\frac{h_N}{N}.
\tag{3.2}
\]

There is also an immediate oracle reduction. Suppose an exact implementation
of \(Q_{1,w}\) has expected bit and fair-bit cost \(T(N)\). Repeatedly draw

\[
D\sim Q_{1,w}=\nu_w
\]

and compute \(g=\gcd(D,N)\). Every return with \(1<g<N\) is a verified factor.
If \(\theta_w>0\), independent calls need exactly \(1/\theta_w\) draws in
expectation.

To obtain a classical expected-polynomial factor finder from bare \(N\), require
one uniform public factor-free algorithm which takes only \(N\), constructs a
description of \(w_N\) of size \(\operatorname{poly}(\log N)\), and samples
\(Q_{1,w_N}\) exactly. The description construction and sampler must terminate
almost surely and together have one fixed expected polynomial bit and fair-bit
bound \(T(N)\). No auxiliary description or advice is supplied. If, uniformly
on the input family,

\[
\theta_{w_N}\ge\frac1{\operatorname{poly}(\log N)}
\]

then independent calls give an expected-polynomial factor finder without
running the Gibbs chain. Its expected cost is

\[
\frac{T(N)+\operatorname{poly}(\log N)}{\theta_{w_N}}.
\]

The event that a new call is reached depends only on earlier independent calls,
so correlation between one call's output and its own runtime does not invalidate
this expectation. No generic sampler follows from point evaluation or a succinct
formula for \(w_N\); the uniform implementation hypothesis is essential.

## 4. Pathwise local-chain obstruction

Monitor both free coordinates and the derived residual with gcds, and stop at
the first proper factor. Before that stopping time, every observed free
coordinate lies in

\[
C_N=R^\times\cup\{0\}.
\]

Their product is also zero or a unit. Conditional on every complete survival
history, the coordinate held fixed by the next local update is therefore zero
or a unit. Sections 2--3 give the history-independent hazard bound

\[
\rho_w=\max\left\{\frac{h_N}{N},\theta_w\right\}.
\tag{4.1}
\]

This remains valid for random scan, deterministic scan, any past-measurable
choice of which one free coordinate to refresh, and extra laziness. Let

\[
\tau=\inf\{t\ge1:\text{a monitored gcd is proper after refresh }t\}.
\]

For every safe initial law and every integer \(t\ge0\),

\[
\Pr(\tau>t)\ge(1-\rho_w)^t,
\qquad
\Pr(\tau\le t)\le1-(1-\rho_w)^t\le t\rho_w.
\tag{4.2}
\]

If \(\rho_w>0\), tail summation gives

\[
\boxed{\mathbb E\tau\ge\frac1{\rho_w}.}
\tag{4.3}
\]

No independence between chain states or successive success events is used.

## 5. Balanced adversarial families

For distinct primes \(p<q\),

\[
h_{pq}=p+q-2.
\]

If \(q/p\le C\) for one fixed \(C\ge1\), then

\[
\frac{h_N}{N}=O_C(N^{-1/2}).
\]

For \(N=p^2\),

\[
h_N=p-1,
\qquad
\frac{h_N}{N}<N^{-1/2}.
\]

Consequently, on either growing family, the two important endpoint regimes are:

1. If one uniform public factor-free algorithm constructs the weight description
   from bare \(N\), samples the exact conditional with total expected polynomial
   bit and fair-bit cost, and
   \(\theta_{w_N}\ge1/\operatorname{poly}(\log N)\) uniformly, then its
   unit-held conditional is already a direct expected-polynomial factor source.
2. If \(\theta_{w_N}\) is negligible against every inverse polynomial, then
   every polynomial number of local refreshes has negligible coordinate-gcd
   success, and the lower bound in (4.3) is superpolynomial. In the special
   case
   \(\theta_{w_N}=O(N^{-1/2}\operatorname{poly}(\log N))\), the expected hitting
   time is at least
   \(\Omega(N^{1/2}/\operatorname{poly}(\log N))\).

These implications are not exhaustive. Intermediate, oscillating, or
nonuniform regimes obey the exact pointwise bound (4.3).

## 6. Framework consequence and exact reopen condition

An arbitrary residual-only weight can reshape the local conditional, but the
named Gibbs wrapper cannot amplify coordinate-gcd success beyond

\[
\max\{\theta_w,h_N/N\}.
\]

At a unit held coordinate, the transition is only a permutation of the residual
law. At a zero held coordinate, it is the original uniform-residue draw. The
second source can create factor mass even when \(\theta_w=0\); for example,
zero-supported \(w\) still gives a raw uniform refresh after one coordinate is
zero.

This is stronger than P59's scalar-activity bound, but it is still narrow. A
material retry must change at least one operation:

- refresh \((k,x)\) jointly from a distribution that is not obtained by first
  sampling their product from one public residual law;
- let the target depend jointly on \(k,x\), not only on \(kx\);
- introduce several residuals with a cancellation or cluster move;
- use a lift or arithmetic proposal that amplifies a hidden valuation;
- decode a whole transcript by a nonlinear or global operation;
- start from a proved law whose construction or different decoder carries
  usable joint factor information.

The theorem is not a lower bound for factoring, general Markov chains, direct
samplers of \(\Omega_N\), block Gibbs, nonlocal Metropolis proposals, or
additional arithmetic tests. It does not claim that an arbitrary \(w\) or its
normalizer can be evaluated or sampled in polynomial time.

## Candidate conclusion

The local Gibbs wrapper is not an additional amplifier. If a residual
distribution can be constructed and sampled uniformly from bare \(N\) with
useful factor mass and expected polynomial total cost, the conditional at the
public unit \(1\) exposes the same mass directly and is itself a positive
factoring sampler. This theorem does not rule out finding such a residual law.
For every residual law, the monitored local chain remains limited by the larger
of its residual factor mass and the raw density of proper nonunits.
