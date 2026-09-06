# F286: retained modular tangent exclusions

Status: new proof candidate and exact finite survivor certificates. Not promoted.
No all-input factoring algorithm or novelty claim is established.

## Question and closest priors

Can joint constraints on the short linear forms `a p+b q`, retained across
binary modular refinement, prune factor candidates before an explicit
square-root-scale state layer forms?

The initial object was the modular hyperbola `uv=N (mod M)`, with coupled
linear forms and square discriminants. Rust-reader navigation inspected
routes F11, F15, F19, F24, F26, and bodies P10 and P26. P10 counts raw binary
histories without these geometric cuts. P26 treats literal trace wheels and
direct useful-square scans. This packet instead retains *nonsquare tangent
exclusions*, intersects their surviving real arcs, and studies the resulting
branch population. The exclusions can prune a state without finding a square.
This is a material model difference, but not a new general factoring barrier.
The local paper index was absent; no external result is used in the proof.

## Exact construction

Let N be odd, let B,A be positive integers, and suppose

    2 B^2 <= N <= 9 B^2/4.

Let M=2^k, k>=1. A modular state is an odd u modulo M and
v=N/u modulo M. There are M/2 states. Each has exactly two children at the
next binary depth. The child formula follows by writing

    (u+M e)(v+M f) = uv + M(e v+f u) (mod 2M):

each choice e in {0,1} determines exactly one f. Arbitrarily many jointly
consistent modular linear forms and their discriminants add no restriction
to this identity. Two forms with invertible coefficient determinant recover
the original pair; their joint labels are not independent square tests.

For each state, round the coordinate interval [B,2B] inward to the first and
last integers in the appropriate residue class. Denote those four bounds by
x_low,x_high,y_low,y_high. The first relaxation retains real x,y satisfying
those bounds and xy=N. These are convex-hull coordinate bounds, not the
original discrete congruences imposed on real x,y.

For every 1<=a,b<=A define T_ab as the least integer at least 2 sqrt(abN)
that is congruent to a u+b v modulo M. Retain the necessary inequality

    a x + b y >= T_ab.

Every integer factor pair in this modular state satisfies it. On y=N/x it
forbids the open interval where

    a x^2 - T_ab x + bN < 0.

These are global-tangent cuts: their lower threshold uses the minimum over
the full positive hyperbola. No local-minimum iteration is included.

## Proof candidate: all branches survive a long initial layer

**Claim.** If M<=B/(4096 A^3), every one of the M/2 states has a real point
satisfying its rounded coordinate bounds, xy=N, and all A^2 tangent cuts.

**Proof.** Since M<=B/8, every rounded coordinate interval contains
[B+M,2B-M]. The common hyperbola arc

    5B/4 <= x <= 3B/2,  y=N/x

has 4B/3<=y<=9B/5. Thus the full arc lies in every state's rounded rectangle.
Its x-length is B/4.

Write s=2 sqrt(abN). The choice of T gives 0<=T-s<M. Its excluded interval
has length sqrt(T^2-4abN)/a, hence length strictly less than

    2 N^(1/4) sqrt(M) b^(1/4) a^(-3/4) + M/a.

The elementary bounds sum_(a=1)^A a^(-3/4)<=4 A^(1/4),
sum_(b=1)^A b^(1/4)<=A^(5/4), and sum_(a=1)^A 1/a<=A give total excluded
length less than

    8 sqrt(3/2) A^(3/2) sqrt(BM) + M A^2.

Under the claimed bound on M this is less than

    (10/64 + 1/4096) B < B/4.

The finite union of excluded intervals therefore cannot cover the common
arc. A remaining point satisfies every cut. The argument is uniform in u,v
and includes the complete coefficient menu, so it also covers any adaptive
subset of that menu at this depth. QED.

The same point passes every earlier-depth version of these cuts on its
ancestral branch: the allowed residue class at depth k is contained in the
earlier allowed class, so its rounded lower threshold can only increase.
The rounded coordinate intervals are nested for the same reason.

For B=Theta(sqrt(N)) and a numerically quasipolynomial coefficient cap A in
the input length, a modulus of order B/A^3 is still exponential in input
length. Literal branch retention encounters that many states. The whole
modular graph nevertheless has a short formula; this is **not** a lower bound
against compressed representation, a different access operation, recursively
recomputed local minima, upper cuts, or arbitrary factoring algorithms.

## Finite experiment

`search.py` uses the 43 coprime pairs 1<=a,b<=8. Public cuts depend only on
N,B,M,u,v and this menu. Factors only construct labelled test inputs:
p is the first prime >=5B/4, and q the first prime >=floor(sqrt(2p^2)). This
avoids the deliberately easy near-small-rational ratio used in an initial
smoke test. No factor label chooses a cut or a proposed survivor.

Floating roots propose surviving intervals. Every reported survivor is then
checked using exact rational arithmetic. The output retains certificates as
`[u, x_numerator, x_denominator]`; y=N/x is implicit. Empty floating proposals
are only numerical observations. A special exact-root pass preserves isolated
rational endpoints, which a floating open-interval subtraction can drop.
Without that pass, true factor points could falsely disappear. No emptiness
claim or proof depends on the floating stage.

Selected results (`product_window` is the baseline count):

| B | M | Product window | Exactly certified tangent survivors |
|---:|---:|---:|---:|
| 4096 | 1024 | 512 | 4 |
| 65536 | 1024 | 512 | 227 |
| 1048576 | 1024 | 512 | 512 |
| 16777216 | 4096 | 2048 | 2048 |
| 268435456 | 4096 | 2048 | 2048 |

The finite pruning is real, and its onset moves with numerical scale. These
examples do not establish the asymptotic claim; the length proof does that
for its much more conservative explicit range. Conversely, the proof does
not assert that pruning cannot begin above its range.

## Resource and workflow record

The preflight observed 74% memory free and load averages 2.12,2.00,1.99.
Process inspection, after a read-only sandbox escalation, showed one OS
`suggestd` core at 100% and no competing intensive numerical job. The script
uses one process, an internal 55-second alarm, standard Python only, and an
estimated peak memory below 64 MB. The pilot completed in about two seconds.
`output.json` retains the final exact certificates and elapsed time.
`run.log` is stderr and is empty on success. No Sage, external service, or
shared ledger was used or changed.

## Next mathematical question

A promising genuine change is to recompute minima on each *retained local arc*
and round them in the same modular class. That can make cuts propagate from
already excluded regions, so the present global-window length bound does not
cover it. The concrete next experiment is interval-local cut propagation with
exact isolated-root preservation, recording both branch count and number of
arc components per branch. It must distinguish new pruning from direct
square discovery at a cut endpoint. A proof would need to control that joint
state complexity; counting modular states or adding more global tangent
forms alone does not do so.

Fresh blind reconstruction is still required before promotion.
