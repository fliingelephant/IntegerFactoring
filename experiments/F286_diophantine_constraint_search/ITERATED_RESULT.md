# F286: iterated local minima

Status: exact finite computation and new proof candidates; not promoted.
This packet preserves the earlier global-tangent result and artifacts.

## Positive mechanism and exact recurrence

For one modular state `(u,v) mod M`, retain closed real arcs on `y=N/x`.
For each arc I and each form f_ab(x)=a x+bN/x, compute

    m = min_(x in I) f_ab(x),
    T = min {t in Z : t>=m, t == a u+b v (mod M)},
    I <- {x in I : f_ab(x)>=T}.

Apply this separately to each current component, cycle through the menu, and
repeat. This is stronger than rounding one minimum over the entire union.
All operations are public. A true integer factor point in the state is never
removed. Every update can propagate information produced by a different form.

For I=[l,r], the minimum is at an endpoint unless sqrt(bN/a) lies in I. In
the latter case it is 2 sqrt(abN). A cut removes the open interval between
the roots of `a x^2-T x+bN=0`. This gives an exact recurrence using only
quadratic algebraic numbers.

## Component bound and finite exact closure

Each form has one stationary point. A cut can split a component only when
that stationary point lies in its interior, and that split removes the point.
It cannot split another surviving component again. Thus a menu of m forms
creates at most m+1 components from a single initial arc. This is a real
compression of the within-state geometry, independent of iteration count.

For an exact-arithmetic version, partition initially at sqrt(N) and, if
desired, the other stationary points. Suppose the menu contains

    (1,1), (1,2), (2,1).

On an arc left of sqrt(N), f_11 and f_12 are both decreasing. At a nonempty
fixed arc's right endpoint r, both values must lie in their prescribed
integer residue classes: otherwise rounding its minimum upward would remove
r. Write s=r+N/r and t=r+2N/r. Then

    y=t-s, x=2s-t

are integers congruent to v,u modulo M and xy=N. They form an exact factor
pair. On an arc right of sqrt(N), use the increasing pair f_11 and f_21 at
the left endpoint instead. Their coefficient determinant is also a unit.
The argument includes singleton arcs. Checking the resulting integers and
their product certifies the result.

This is a useful fixed-point characterization, not an efficient factoring
claim. It explains why two distinct local cuts can eventually eliminate
every false state even though all global cuts leave it alive.

Exact finite termination also follows without a convergence assumption.
Inside x,y in [B,2B], every relevant T is at most 4AB for coefficients <=A.
Each form supplies O(AB/M+1) thresholds, each with at most two roots.
All endpoints come from this finite root set and the initial endpoints.
With m forms its size is K=O(m(AB/M+1)). The ordered endpoint set partitions
the line into O(K) points and open cells. Every strict update removes at
least one previously retained atom. There are therefore O(K) strict updates.
An entire unchanged sweep is a fixed point. Comparisons of these bounded-size
quadratic algebraic endpoints are exact and have polynomial bit cost in the
operand lengths. The numerical factor B/M in this count is the remaining
cost, not a quasipolynomial bound in input length.

## A concrete slow-propagation region

There is an elementary explanation for slow sweeps away from tangencies.
Suppose 2B^2<=N<=9B^2/4 and start with the arc

    6B/5 <= x <= 13B/10.

For the three-form menu above, all derivatives have fixed signs on this arc
and absolute value at least 1/8. Each threshold round raises a minimum by
less than M, so it moves the relevant endpoint by less than 8M. One sweep
can shorten the arc by less than 24M. If an update erases the whole remaining
arc, its length was less than 8M, by the same mean-value argument.

Consequently, the arc cannot be erased in fewer than B/(240M) sweeps. If it
contains no compatible integer factor point, the fixed-point characterization
also rules out earlier nonempty exact closure. This is a scoped iteration
bound for this three-form closure procedure, not a lower bound for factoring:
an external primality check, a different form menu, or an intermediate
square-discriminant gcd may finish first.

## Exact finite pilot

`ITERATED_search.py` uses the same public local-minimum recurrence, with
outward rational root enclosures of scale 2^32. Initial endpoints and all
minimum/maximal-value comparisons use exact fractions. For a nonsquare
discriminant D, floor(sqrt(D*2^64)) gives outward enclosures of the two roots.
Only a rigorously contained forbidden interval is removed. Therefore empty
states are exact computational conclusions. Surviving arcs are conservative
enclosures; an unchanged enclosure is not an exact mathematical fixed point.
Perfect-square discriminants use their exact rational endpoints, including
singletons. This prevents loss of a true factor sitting on a boundary.

The run audits both labelled true factor points after every update. Labels
do not affect cuts, stopping rules, or square-discriminant gcd checks.
All such audits passed. First factor hits use gcd(T +/- sqrt(D),N) and are
counted separately from state pruning. Computation continues after those
public hits to measure closure behavior.

| B | A | M | Survivors | Enclosure-fixed states / all states | Maximum sweeps |
|---:|---:|---:|---:|---:|---:|
| 4096 | 4 | 8 | 1 | 4/4 | 9 |
| 4096 | 8 | 32 | 2 | 16/16 | 2 |
| 65536 | 4 | 32 | 16 | 0/16 | 24 (cap) |
| 65536 | 8 | 32 | 2 | 16/16 | 8 |
| 1048576 | 4 | 128 | 64 | 0/64 | 24 (cap) |
| 1048576 | 8 | 128 | 61 | 0/64 | 24 (cap) |

For the last row the code visited 549,456 arc/form pairs. A low final state
count can conceal substantial iteration and component processing. Some
factor hits precede closure, and some are induced by the first sweep; they
must not be presented as a new source without comparison to direct scanning.

`ITERATED_output.json` records every state's sweep counts, component counts,
updates, arc visits, first factor-hit sweep, and final rational endpoints.
The full run took 14.92 seconds, one Python process, with an internal
25-second alarm and estimated memory below 128 MB. Preflight found 73%
available memory and load 4.66; the root's recent shared process snapshot was
used to coordinate with its independent Sage work. `ITERATED_run.log` is empty
on success. No floating arithmetic is used in this experiment.

## Next gap

The new positive fact is that local propagation has bounded geometric
complexity per state and its exact fixed points reveal integer factors.
The unresolved issue is accelerating the monotone rounding iteration across
many distinct trace levels. A next construction should batch those levels or
jump over a certified empty block. Another coefficient sweep alone has no
demonstrated improvement in total state-times-iteration cost.

Blind reconstruction should separately verify the component bound, the
fixed-point endpoint claim, and the exact finite termination accounting.
