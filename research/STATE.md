# Research State

Updated 2026-09-07 after the eleventh authorized Astra cycle. All jobs are terminal; no expected-quasipolynomial factoring algorithm is established in this repository.

## Current randomized-discovery interfaces

The target is a verified divisor with one uniform expected quasipolynomial
bit bound. Attempts may restart. For expected cost \(a(N)\) and success
probability \(p(N)>0\), it is enough to bound \(a(N)/p(N)\); exact sampling
and counting are optional.

| Record | Positive primitive | Missing bound |
| --- | --- | --- |
| P41 | A sampler within TV \(1/28\) of the quadratic energy law gives at least \(1/4\) verified-gcd success per call. | A factor-free sampler with expected quasipolynomial bit and fair-bit cost. |
| P244 | A discrete public normal and exact SUPPORT hit a divisor vertex with probability at least \(1/(8nN^{1/3})\). | A stronger normal source or support mechanism with quasipolynomial cost/success ratio. |
| F320 | A decoded two-bank difference source succeeds at constant probability at bank size \(O(\sqrt{p_{\min}})\). | A compact correlated source beating the square-root least-factor scale. |
| F321 | Output-selected roots gave strong finite success and have exact hazard identities. | A squarefree cumulative-hazard bound per total circuit-evaluation cost. |
| P245 | The fixed F321 protocol pathwise dominates its squarefree radical shadow. | It transfers a success contract to all inputs but does not prove one. |

P242 and P243 remain deterministic tools for unshifted transport and one
fixed half-box residue. P237/P239 are conditional interfaces for the exact-
counting route. None is required by direct verified-divisor routes.

## Eleventh-cycle findings

P244 is the independently reconstructed theorem from F319. Every divisor
vertex \(P=(p,q)\) of the integer hull of \(xy\geq N\) has adjacent normal
slopes \(\lambda_-<\lambda_+\) satisfying
\[
 N(\lambda_+/\lambda_--1)^3\geq4.
\]
Sampling one of \(2n\) dyadic octaves and a \(2^{-4n}\) mesh point inside
it gives a strictly interior divisor normal with probability at least
\(1/(8nN^{1/3})\), conditional on exact SUPPORT. Ties are irrelevant.
The theorem covers every composite, including prime powers and unbalanced
factors, but its expected call count is a numerical power of \(N\).

F319 also implements exact standard-lattice SUPPORT from the cached
Alcántara--Blanco--Criado--Santos NEXTPT algorithm. The author-derived
bound is polynomial per call, yielding a valid but slow
\(O(n^7N^{1/3})\) Las Vegas route. Gcd-screening returned coordinates can
have more success mass than accepting only exact product points. Reweighting
unchanged independent proposals cannot improve first discovery; the tested
state-dependent normal proposals have only censored finite evidence.

F320 removes the unit baseline and zero atom from the quadratic energy.
Estimating that residual mean at constant relative RMS still requires
\(\Theta(p+q)\) iid probes on semiprimes; this is not a factor-discovery
bound. An explicit block inherits direct useful density. A two-bank menu has
pairwise-independent indicators and
a second-moment success lower bound. Existing P34/F162 product-tree
arithmetic decodes it in near-linear bank work, giving a genuine Las Vegas
algorithm at expected \(\sqrt{p_{\min}}\operatorname{poly}(n)\) cost.
This is \(N^{1/4}\)-scale on balanced inputs.

F321 adapts the polynomial itself. A unit output \(a=H(x)\) is appended as
a root through \(H\leftarrow H(H-a)\). Over a field, its exact collision
energy increment retains reflection, midpoint, and removed-fiber terms.
Formal degree growth gives no drift bound, and surviving semiprime histories
are reweighted.

A sufficient unproved contract is cumulative: on an event of probability
\(\delta\), if \(\sum_{j<T}h_j\geq\lambda\) and every full-zero probability
is at most \(1-\epsilon\), then a capped attempt succeeds with probability
at least
\[
 \delta(1-e^{-\lambda})-T(1-\epsilon)^K.
\]
Its straight-line evaluation cost is \(O(KT^2\operatorname{poly}(n))\).
Public unit rescaling leaves this process unchanged. The first uniform
probe alone gives a weak \(1/(2p_{\min})\) success bound and finite expected
restart cost, but not the target complexity.

P245 couples this protocol modulo \(N\) to its squarefree radical shadow.
A shadow success is an actual success or follows an earlier actual split.
Thus a squarefree contract extends to all non-perfect-power inputs; exact
roots handle perfect powers. The field identity remains field-specific.

Adaptive roots succeeded in all 256 larger trials. Descriptive balanced-scale
slopes were 0.325342 for gcd stages, 0.654607 for multiplications, and 0.502728
for work-matched rho. These are finite fits. Rho used fewer multiplications
but more gcds. The \(K=8\) guard had 12 censors and no global-equality rejection.
Conditional field populations still require survival weighting.

## Evidence and counts

P244 retains the qualified frozen statement and independent proof hashes.
C277–C279 retain the support implementation, energy controls, exact adaptive
identities, all censors, corrected and failed fit runs, resource records,
and manifests. The catalog has 614 records, 34 routes, and 536 experiments.
There are 230 supported experiment-route assignments and 306 unknowns.

## Restart point

Does F321's squarefree process satisfy a cumulative-hazard contract after
all work and resets are charged? Alternatives are a nonlocal P41 sampler,
a decoded correlated F320 source, or an adaptive F319 normal law whose mass
pays for SUPPORT. Narrow uniform, independent, invariant, or fixed-map
failures do not close these mechanisms.
