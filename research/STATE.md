# Research State

Updated 2026-09-07 after the twelfth authorized Astra cycle. All current
mathematical and computational jobs are terminal. No expected-
quasipolynomial factoring algorithm is established in this repository.

## Current Las Vegas interface

The target is one verified divisor with a uniform expected quasipolynomial
bit bound. Attempts may fail and restart. If an attempt has expected cost
\(\tau(N)\) and success probability \(\delta(N)>0\), it is enough to bound
\(\tau(N)/\delta(N)\). Deterministic completion, exact counting, and fast
behavior on every auxiliary parameter are optional.

P246 gives a direct polynomial-space FacRoot path on an exactly ranked odd
domain, but its complete traversal takes \(O(N\operatorname{poly}(\log N))\)
bit work. P02 permits a weaker fixed-\(N\) target: privately sample a uniform
unit \(r\), publish \(a=r^2\bmod N\), and run a procedure that receives only \(N,a\)
and independent coins. A quasipolynomial cost/success ratio averaged over
these random squares suffices; every Jacobi-positive \(a\) need not be fast.
Public adaptive square-unit rescalings and filters are also allowed if the
private root stays outside the transcript and every shaping cost and failure
is charged.

| Mechanism | Positive primitive | Missing bound |
| --- | --- | --- |
| P246/P02 | Exact ranked FacRoot involution and private-root decoder. | A short-attempt cost/success ratio on public square inputs. |
| P247 | Exact lazy-uniform-matching survival, mean, endpoint, and screen laws. | Its semiprime benchmark remains least-factor scale. |
| P245/F321 | Radical-shadow transfer for adaptive output-selected roots. | Squarefree cumulative hazard after total evaluation cost. |
| P41 | Approximate quadratic-energy sampling implies verified success. | A factor-free quasipolynomial sampler. |
| P244 | Discrete normals hit a divisor cone conditional on SUPPORT. | A proposal/support ratio better than \(N^{1/3}\). |
| F320 | Pair-bank decoding costs \(\sqrt{p_{\min}}\operatorname{poly}(n)\). | A stronger compact correlated source. |

P242 and P243 remain deterministic residue tools. P237/P239 remain
conditional exact-counting interfaces. None is mandatory for a direct
Las Vegas route.

## Twelfth-cycle findings

P246 promotes the exact F326 statement. The all-residue multiplication sign
equals the Jacobi symbol. Euclidean floor sums compute the odd domain size,
rank, and selection. The arithmetic involution fixes only decodable divisors
or roots. Two auxiliary involutions give terminating paths of at most
\(d\leq N\) calls. This is a rankable parity path, not a short-path theorem.

P247 analyzes a uniform singleton start and a lazy uniform matching. If the
ranked involution has \(d\) vertices and \(q\) fixed ranks, then
\[
 S_T=\prod_{k<T}\frac{d-q-2k}{d-2k},\qquad
 \mathbb EH=\frac{d+2}{q+2}.
\]
The stopped endpoint is uniform, and expected capped calls per success are
nonincreasing with the cap for fixed \(d,q\). Random matching overhead is
expected polylogarithmic. For F326 square inputs the exact capped factor
probability is \((1-1/q)(1-S_T)\). A static whole-\(F\)-edge screen replaces
\(q\) by its absorbing-set size. Uniform matching still costs
\(\Theta(p_{\min})\) local calls on squarefree semiprimes.

F322 implements Jeřábek's three-layer involution; its fractional-linear
macros still lack actual-path sign certification. F323 shows that on the
tested Blum family one Jacobi sheet is injective, repeated squaring adds no
gcd event, and a common seed cancels. A succinct cross-sheet source remains
open. F324's reflection matrices gave finite paths but no length law.

F325 exactly contracts mixed-sign translation chains after changing their
nonunit pairing. All macros matched the modified graph, but 8 of 35 endpoints
changed. The original used 1,411 calls for 35 factors; the macro used 1,474
explicit calls plus 77 integer programs for 34 factors. Gurobi checked only
finite candidates, not the arbitrary-bit Lenstra implementation.

F326 passed all small checks and 80 public complete paths. Its first corrected
private-root sample returned 160/160 factors, but F328's larger capped sample
retained only 39 factors and 153 censors among 192 attempts at cap 2,048.
Successes per 32 attempts at 20/28/36/44/60/92 bits were
31/7/1/0/0/0. Total charged work was 336,576 \(F\)-calls and 394,405,596
floor-sum iterations. These per-scale finite data prove no trend or zero
probability.

## Evidence and counts

P246 preserves statement/reconstruction hashes d672ba5f... and 7b6bc06c....
P247 preserves hashes 46a229a4... and cc4125ba.... C280--C286 retain
mechanisms, source scope, finite outputs, censors, resources, and manifests.
The Jeřábek and Lenstra papers are cached in full; KB doctor passes.

The catalog has 623 records, 34 routes, and 543 experiments. There are
237 supported experiment-route assignments and 306 explicit unknowns.

## Restart point

Run F327's proposed uniform-center reflections against its exact lazy-matching
benchmark on identical private-root inputs and screens. In parallel, derive
and test public short-path conditions suggested by F328's 7-, 25-, and
31-call seeds and its inverse-endpoint \(Q(t)\) identity. Public square-input
shaping is another allowed experiment if failed filters are charged. The
acceptance criterion for each route remains a uniform quasipolynomial
attempt-cost/success ratio for every fixed composite \(N\).
