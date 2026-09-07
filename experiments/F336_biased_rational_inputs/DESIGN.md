# Deliberate rational inputs for count descent

**Family:** route:F31

Status: root-designed experiment, not a probability or novelty claim.

## Question

Does directly sampling a prescribed rational a=r/b modulo N improve the
charged count-descent success law beyond uniform multipliers? This changes
the source; it does not condition a uniform draw for free. Numerically large
r,b still have O(log N) bits and are inexpensive to sample, even when a
literal orbit-window menu would be too large to enumerate.

F335 studies uniform-source policies, a small-A obstruction, and an
author-derived short-rational/triangular-wave model. Its uniform parameter
tail is not a bound for the sampler below. All returned outputs here are
verified divisors. Internal a may have either Jacobi sign: the count itself
is defined for every unit, and no odd-domain fixed-point assertion is used.

## Input laws

Use the F328 moduli and n=bitlength(N). For a scale gamma, set
e=max(2,floor(gamma*n)). Draw a positive odd integer uniformly from

    [2^(e-1), min(2^e-1,N-1)].

The interval contains at least one odd value for all retained inputs. Sample
it exactly by fair-bit rejection on its number of odd values. Accept any
proper generation gcd immediately; do not condition it away.

Compare these laws, preserving the same drawn b for paired direct/inverse
views when it is a unit:

- `direct`: a=b, gamma in {1/8,1/4,3/8,1/2,3/4}.
- `inverse`: a=b^(-1) mod N at the same five scales.
- `ratio`: draw independent r,b at gamma in {1/8,1/4,3/8}, screen both gcds,
  reduce r/b by their ordinary common gcd, then set a=r*b^(-1) mod N.
- `uniform`: draw a uniform nonzero residue, accept a generation gcd, or use
  its unit value as a. This is a full-unit control, not a Jacobi-positive
  conditional sample.

Keep Jacobi signs, actual r/b heights, the full CF digit sum and largest
digit as diagnostics. They do not select or reject a trajectory. Retain
repeated parameters in the sampling statistics and report their distinct
count. A direct and inverse pair share generation work as a paired experiment;
each standalone algorithm's cost must still include that generation.

## Fixed public algorithm

Use exactly F334's fixed-multiplier, fixed-h min-count descent:
t=(N-1)/2; screen t, Q_a(t), and t-Q_a(t); stop on a verified factor, an
empty side, or t<=1; otherwise continue at the smaller positive count.
Do not add a new factor screen or a root routine. Count generation, inversion,
floor-sum, gcd, randomness, and verification work, including failures.

For an inverse input with odd b, optionally compare the first counts with
F335's explicit b-period formula. For a reduced ratio r/b, the triangular-wave
model and its claimed error should be treated as an author-derived diagnostic,
not as an assumed equality or a stopping rule. Keep any violation for root
review. Large r+b can make that bound uninformative without invalidating
the actual count computation.

## Bounded plan

First validate exact sample ranges, a*b=r modulo N, unit/generation cases,
and agreement with frozen F334 count descent on tiny inputs. Use a two-trial
pilot on both 20-bit moduli. Then retain 128 outer trials per law/scale on
both F328 moduli at 20,28,36,44,60,92 bits, in fresh resource-safe batches.
The total is 14 policies per modulus; no input classes are dropped after
observing outputs. The scale can use small batches without reducing this plan.

Keep compact per-attempt rows with seeds, exact parameters, Jacobi sign,
CF statistics, maximum actual defect, stopping stage/type, verified output,
and operation/time totals. Full descent traces are needed only for the pilot,
every distinct factor-output witness, and anomalies; the frozen source and
per-attempt parameters reproduce other traces. Aggregate files should reference
per-job rows rather than duplicate them all.

Report per-N results; separate generation factors from count factors and
charge both. Compare each policy's cost per observed success with the uniform
control, leaving ratios absent on zero-success cells. A finite trend is not
a success theorem, and an exponent improvement alone is not the QP target.

Inspect current CPU/load/memory, write a resource estimate, and pilot before
scaling. Each job is single-threaded, <=512 MiB, with a 28-second internal
alarm and 30-second external timeout. At most two independent bounded local
processes may overlap after the root's current resource preflight; coordinate
with the other Sol worker. Preserve source, status, log, outputs, resource
record and a checksum manifest. No feature-development review workflow is used.
