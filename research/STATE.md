# Research State

Updated 2026-09-07 after the fourteenth authorized Astra cycle. All jobs are terminal; no expected-quasipolynomial factoring algorithm is established.

## Target and sufficient interface

The target remains complete factorization of every integer by one classical
Las Vegas algorithm with a uniform expected quasipolynomial bit bound. Failures
and restarts are allowed. Deterministic completion, exact counting, uniformly
short paths, and fast performance for every auxiliary parameter are optional.

P249 is the broadest current sufficient contract. For each fixed odd composite
with at least two distinct prime divisors, a public FacRoot procedure on a
uniform Jacobi-positive unit may have arbitrary cost-success correlation. A
uniform quasipolynomial bound on mean verified cost divided by valid-output
probability gives all-input Las Vegas factoring by uncapped two-engine
dovetailing. This is sufficient, not restrictive: other sources,
transformations, partial solvers, and input shaping remain allowed.

## Promoted cycle result

P250 proves source-specific structure for count descent. Canonical
continued-fraction digit sums are invariant under negation and inversion,
their fixed-denominator Jacobi-positive mean is polylogarithmic, and
\[
 |2Q_a(t)-t|\leq10S(a,N).
\]
It gives complete fixed-start dyadic eligibility and balanced-cofactor bounds,
including all large-defect and generation events. Its named uniform, fresh,
uniform-start, and inverse-start policies have
\(O((\log N)^3/\sqrt H)\) factor probability on the covered balanced inputs.
Literal fixed-\(h\), fixed-\(a\), smaller-child descent returns no factor when
the least prime exceeds \(5\min(a,N-a)^2\).

They do not rule out biased rational sources, random branches, shifted thresholds,
rank collisions, added screens, roots, or other procedures in general. The
small-$A$ clause applies only under its exact hypothesis.
## Fourteenth-cycle evidence

F334 tested fixed, fresh, and inverse-start min descent on twelve scale inputs.
Fixed returned 0/3,072; fresh returned 52/3,072 only through added generation
gcds; inverse-start returned thirteen later count factors. None returned a
count factor at 44, 60, or 92 bits. Direct dyadic menus became expensive and
supplied no scale success law.

F336 tested 21,504 fixed-h attempts from fourteen biased and uniform profiles.
Minimum branching had four generation and 48 count factors. Uniform had
0/1,536; every profile had zero factors on both 44-, 60-, and 92-bit inputs.
Repeated small parameters explain much of the 20-bit concentration.

Fair branching has an author-derived, unpromoted work primitive: screen both
children, then take a fair branch. Expected reached queries are at most
\(\lceil\log_2h\rceil+1\), although realized paths need not shrink. Exact
small-state DP rescued 818 parameters from min-branch failure, but complete
unit-set success was higher on 28 inputs, lower on 22, and equal on 39. F338
replayed all F336 rows: fair branching had four generation and 47 count
factors, rescuing 21 rows and losing 22. It used higher pooled charged work
and again had no hit above 28 bits. This does not bound another fair source.

F337 finitely validated author-derived polynomial-bit random-threshold and
three-gap-class rank samplers. On 459 cells, both gap laws had lower mean useful
off-diagonal energy and higher duplicate energy than uniform ranks. Some
post hoc cells reversed pair energy, but a heavy shared endpoint erased the
batch gain or admitted a direct no-floor-sum sampler. The inverse-boundary
transfer passed its guarded finite checks. No larger-input inference follows.

F339 adds an unpromoted return-map representation. Deleting an interval from a
full rotation expresses a coupled rank jump as the public jump minus deleted
visits. Fixed jumps have a \(2(d+1)\)-entry direct menu for deletion size
\(d\). Uniform jumps collapse to uniform distinct ranks for every \(d\), and
one manufactured large-\(d\) source is covered by six direct gcds. General
large-\(d\), nonuniform jump sources remain open.

## Current gap and evidence

No public procedure is proved to meet P249's per-input expected cost/success
contract. P250 rules out only its named uniform min-descent policies on covered
balanced families. F334--F338 are finite evidence; they do not close
randomized, biased, shifted, partial, approximate-with-verification, or
variable-duration procedures.

P250 preserves statement, author-proof, and reconstruction hashes
75c092be..., 5a698ed6..., and 33125e52.... C292--C297 retain the cycle's
proof comparison, rows, repairs, censors, costs, provenance, designs, and
manifests. The Aistleitner--Borda--Hauke paper is cached in full; the
Rosser--Schoenfeld DOI remains metadata only.

The catalog has 637 records, 34 routes, and 554 experiments, with 248
supported experiment-route assignments and 306 explicit unknowns.

## Restart point

Execute F339's bounded identity checks, then run the six public nonuniform
jump rules in COUPLING_SEARCH.md on every retained F337 cell. Keep endpoint
failures, duplicate rules, generation/setup work, direct gcd controls, the
uniform-distinct-rank control, and feasible small-\(d\) menus. Test whether a
repeatable coupled displacement survives those controls with useful source
mass. A post hoc best cell is only a candidate for a later public source and
charged cost/success proof.
