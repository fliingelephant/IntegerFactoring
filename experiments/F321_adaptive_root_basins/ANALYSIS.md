# Adaptive basin analysis: additive overlap, survival, and an overshoot guard

Status: author-derived analysis. No independent reconstruction. This file is
separate from the numerical pilot and claims no experimental result.

## Scope and the unknown growth mechanism

P63 was read before this analysis. It treats a fixed polynomial and affine
conjugates with a uniform start, not parameters sampled from the current
pushforward. Its inverse-basin example does not settle this adaptation.

Let r be an odd prime, let mu be the law of H(X) for uniform X in F_r,
and put alpha=mu(0), s=1-alpha, beta=sum_{x!=0}mu(x)^2. A forced accepted
parameter has law mu(a)/s for a!=0. The update is f_a(y)=y(y-a).
The zero mass increases by mu(a), as in the root's seed identity.

The decisive question is whether the *nonzero* distribution repeatedly
develops enough additive reflection overlap to make logarithmic root-mass
growth large. Formal degree doubling alone does not supply this overlap.

## Exact nonzero-energy recurrence

Define C(a)=sum_x mu(x)mu(a-x). The equality f_a(x)=f_a(y) holds exactly
when y=x or y=a-x. The two cases intersect only at x=y=a/2. Thus the full
collision energy Q=sum_x mu(x)^2 satisfies

    Q_next = Q+C(a)-mu(a/2)^2.

Subtracting (alpha+mu(a))^2 gives the sharper identity

    beta_next-beta
      = sum_{x!=0,a}mu(x)mu(a-x)-mu(a/2)^2-mu(a)^2.        (1)

Consequently the exact expected increment under a forced accepted parameter
is

    E Delta beta = [sum_{a!=0} mu(a)
        (sum_{x!=0,a}mu(x)mu(a-x)-mu(a/2)^2)
        -sum_{a!=0}mu(a)^3] / s.                         (2)

The first term is an additive-triple statistic on the nonzero population.
The subtracted cubic term is the energy removed when the selected fiber
joins zero. Equations (1)-(2) retain fixed points and do not assume random
map behavior or independence between values of H.

If the current nonzero support is sum-free in the additive sense, the first
term in (1) vanishes and beta decreases. This is a conditional statement
about distributions, not a claim that such a support occurs in this process.
At the opposite extreme, a support with many reflected pairs can increase
beta substantially. For broadly spread supports the heuristic C(a)~1/r
suggests additive, rather than multiplicative, energy gains. That heuristic
is not used as a theorem.

## The correct potential and a caution about mean growth

For alpha>0 the exact logarithmic drift is

    L(mu) = E[log(alpha_next/alpha)]
          = (1/s) sum_{a!=0} mu(a) log(1+mu(a)/alpha).     (3)

Writing mstar=max_{a!=0}mu(a), elementary logarithm bounds give

    beta/[s(alpha+mstar)] <= L(mu) <= beta/(s alpha).     (4)

Thus an expected increment proportional to alpha is not by itself evidence
of a comparable logarithmic drift. A distribution can have one nonzero
atom of mass sqrt(alpha), with its other nonzero mass diffuse. Its beta
is at least alpha, but the contribution of that atom to (3) is only
O(sqrt(alpha) log(1/alpha)). The remaining diffuse contribution can be
arbitrarily small if the ambient field is correspondingly large. This
example refutes an inference from the scalar drift alone; it is not a
reachable-distribution claim about H.

A sufficient conditional mechanism is a uniform lower bound L(mu)>=ell
on all relevant states before a bounded-overshoot interior hit. An additive
drift argument for log(alpha), whose total range is at most log(r), then
bounds the expected accepted-stage count by log(r)/ell. Markov truncation
gives a finite public stage cap with constant hitting probability. One
must prove the lower bound for actual reachable distributions, and also
control overshoot and the cost of obtaining accepted parameters. None of
these conditions is established here.

## Forced chain versus actual survival on pq

For distinct primes p,q, at fixed current field populations with zero masses
a,b, a raw uniform probe is a unit, a full zero, or a proper-gcd success
with respective probabilities

    u=(1-a)(1-b),    z=ab,    f=a+b-2ab.

Conditioning the probe on being a unit gives independent local parameters
from the two nonzero pushforwards. However a surviving history is reweighted:
after ignoring full-zero retries the probability of advancing is u/(1-z),
and the factor hazard is

    h=f/(1-z) >= max(a,b).                               (5)

The inequality follows, for example, from
h-a=b(1-a)^2/(1-ab)>=0. Generate the forced-unit chain first and independently
kill each transition with its state-dependent hazard. This constructs the
actual uncapped process, including the nonfactorized survival weight
product_j(1-h_j). Conditioning on survival generally destroys independence
of the two population histories.

The uncapped statement is inadequate for resource bounds: a=b close to one
can make full-zero waits enormous. If both equal one, no next unit exists.
For a cap of K raw probes at a stage, the exact three outcomes are

    advance: u(1-z^K)/(1-z),
    factor:  f(1-z^K)/(1-z),
    reset:   z^K,

with the evident reset interpretation at z=1. This must be included in
any cost or success theorem.

An interior-hit condition avoids the waiting problem. Suppose the forced
chain reaches alpha_p in [epsilon,1-epsilon] by stage T with probability
delta. On every such path, monotonicity gives alpha_p<=1-epsilon before
the hit, hence z<=1-epsilon. Also one raw probe at the interior state has
factor probability f>=epsilon, regardless of alpha_q. Coupling factor
killing and capped resets to the forced path gives the lower bound

    actual success >= delta*epsilon-(T+1)(1-epsilon)^K.  (6)

One way to see the factor term is to condition on a forced path: either
the process already factors, or it survives to the interior state, where
the next factor hazard is at least epsilon. Resets subtract at most the
displayed union bound along each good path. Choosing
K=O(log((T+1)/(delta epsilon))/epsilon) makes the error small. The bound
does not assert an interior hit, and it does not cover a jump straight to
mass near one. Evaluating H at depth t costs O(t) modular operations, so
the capped attempt uses O(K T^2) such operations, plus gcd and random-bit
costs. Quasipolynomial T,K would be acceptable.

## A concrete public modification: guard the selected fiber

The following modification addresses overshoot without factors or large
polynomial expansion. After obtaining a unit parameter A=H(X), draw K fresh
uniform seeds X_j and gcd-screen H(X_j)-A before applying the update.
Return any proper divisor. If any screen is a global zero, reject this
parameter and leave H unchanged. Apply the update only when all K screens
are units. Give parameter retries a finite public cap and reset afterward.

For fixed selected local values a_p,a_q, put
w_p=mu_p(a_p), w_q=mu_q(a_q). A guard probe has probabilities

    unit=(1-w_p)(1-w_q),
    full zero=w_p w_q,
    factor=w_p+w_q-2w_p w_q.

If either selected fiber has mass greater than theta, the probability that
the parameter passes all K guard probes is at most (1-theta)^K. A union
bound over the finite total number of parameter attempts therefore controls
unsafe accepted jumps. The guard uses only evaluations of the current
straight-line program and gcds. It does not estimate a hidden field mass.

Conditioned on a guarded acceptance, the field parameter laws still
factorize at a fixed state. Each local law is proportional to

    mu(a)(1-mu(a))^K,    a!=0.                           (7)

Thus the modification is explicit and analyzable, rather than a requested
sampler oracle. It suppresses large jumps, and mismatch between a large
fiber in one field and a small one in the other is itself a factor source.
It does NOT prove accelerated growth: when both fields have very heavy
nonzero atoms, guarded acceptance can be rare and resets can dominate.
An all-input argument would need either enough guarded logarithmic drift
per total probe cost, or a new decoder for that jointly concentrated case.
Replacing (3) by its weighted version from (7) states the remaining lemma
precisely. The guard is a possible experimental branch, not a recommendation
to replace the root's current pilot without measuring this tradeoff.

## Two-sample sums do not automatically solve the overlap question

A second natural parameter rule samples independent Y,Z~mu and chooses
a=Y+Z, conditioned on a!=0. Its law is C(a)/(1-C(0)). The exact full-energy
drift becomes

    [sum_{a!=0} C(a)^2 - sum_{a!=0}C(a)mu(a/2)^2]
      /(1-C(0)),

while root-mass drift is

    sum_{a!=0}C(a)mu(a)/(1-C(0)).

This moves the unknown statistic from a weighted additive triple to the
additive energy of mu. It deliberately merges the sampled pair, but when
convolution is diffuse it gives no automatic large gain. A public N version
can sample the two outputs, gcd-screen their sum, and evaluate the same
quadratic update. No factor-aware sampling is needed. These identities give
a concrete comparison branch, but no uniform growth improvement is proved.

## Remaining all-input scope

The exact energy recurrence uses a field and odd characteristic. Over a
prime-power ring, (x-y)(x+y-a)=0 permits additional pairs, so the two-branch
collision identity cannot be imported unchanged. Field zero mass measures
nonunits, whereas a full-zero gcd modulo p^e needs valuation e. The public
gcd-screened algorithms remain well-defined on every N, but prime-power
valuation populations and repeated-prime survival require separate analysis.
Even removal, primality testing, and recursive splitting alone do not prove
the unproved splitter bound. No claim here closes that gap.
