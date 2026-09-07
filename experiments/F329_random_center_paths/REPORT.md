# F329 random-center and lazy-matching paths

**Family:** route:F31

Status: bounded seeded experiment passed. The data does not establish an
asymptotic success bound or a faster factoring algorithm.

## Result

F329 compares three F326 arithmetic paths: reflection around rank `L`,
reflection around a uniform center, and P247's uniform-start lazy matching.
Every sampled trajectory supplies paired results for the baseline F326 decoder
and a static whole-F-edge gcd screen. The static screen tests the six distinct
arguments invariant under exchanging the edge endpoints: both endpoint values
plus or minus one, the edge difference, and the edge sum.

The random-center reflection did not show a consistent short-path improvement
over the lazy-matching benchmark. Its deviations changed sign across moduli,
screens, and caps. The static screen increased short factor counts, but it adds
exactly six gcd calls per visited F edge. Its improved F-call ratios therefore
did not consistently improve total-gcd cost per factor.

## Exact controls

The generic control covers every odd `d<=9`, every odd fixed count `q`, every
absorbing size `b=q+2g`, every singleton start, and every perfect matching of
the remaining ranks. All 35 scenarios and 15,325 enumerated paths agree exactly
with P247 for capped survival, capped mean calls, and the conditional uniform
absorbing-rank law. Every comparison uses `Fraction` arithmetic.

The sparse-pool control exhausts all 5,913 deletion orders through size seven,
checks 40,319 active-set states, and completes 248 seeded pop-all runs through
size 31. The small arithmetic control covers every unit square for
`N=15,21,35`, 11 `(N,a)` instances in total, and every reflection center. It
retains every cap through `min(d,64)`, all three fixed-point branch counts,
exact `q,b`, screened factors, valid roots, and full hidden-root-fibre outer
decoding counts. Every `q_unit` equals `2^s-1`.

For the separate generic example `F(i)=-i mod d`, the control verifies `H=1`
at center zero and `H=(d+1)/2` at every nonzero center for
`d=3,5,7,11,13`. This example is not an F326 arithmetic counterexample.

## Pilot and P247 comparison

The pilot retains 16 conditional unit-square inputs for each of
`N=209,1333,10807`. Each square has one rank-L path, four independent uniform
centers, and four independent lazy matchings. The exact offline diagnostic
finds `q=23..31, b=65..87` for `N=209` and `q=51..59, b=201..231` for
`N=1333`. The `N=10807` labels remain unknown as designed.

At cap 256, verified factor successes are:

| N | rank-L baseline/static | uniform center baseline/static | lazy matching baseline/static |
|---:|---:|---:|---:|
| 209 | 15/16; 15/16 | 64/64; 64/64 | 60/64; 63/64 |
| 1,333 | 15/16; 15/16 | 64/64; 64/64 | 64/64; 64/64 |
| 10,807 | 16/16; 16/16 | 64/64; 64/64 | 63/64; 64/64 |

The next table compares the two 64-trajectory random methods with the exact
P247 expectations. `Complete` counts any valid fixed or screened endpoint;
factor success can be lower after a root-decoding failure.

| N | Screen | Cap | P247 complete | Center complete | Lazy complete | P247 F calls | Center F calls | Lazy F calls |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 209 | baseline | 4 | 32.50 | 29 | 32 | 200.64 | 211 | 214 |
| 209 | baseline | 16 | 61.09 | 61 | 61 | 364.04 | 371 | 358 |
| 209 | static | 4 | 59.73 | 63 | 61 | 121.67 | 115 | 133 |
| 209 | static | 16 | 64.00 | 64 | 64 | 130.35 | 120 | 136 |
| 1,333 | baseline | 4 | 13.29 | 14 | 14 | 235.13 | 234 | 235 |
| 1,333 | baseline | 16 | 39.07 | 40 | 31 | 684.42 | 671 | 738 |
| 1,333 | baseline | 64 | 62.80 | 63 | 61 | 1,081.04 | 1,003 | 1,294 |
| 1,333 | static | 4 | 40.45 | 35 | 43 | 183.00 | 188 | 163 |
| 1,333 | static | 16 | 62.88 | 63 | 61 | 283.58 | 332 | 276 |
| 1,333 | static | 64 | 64.00 | 64 | 64 | 288.51 | 334 | 296 |

The lazy observations fluctuate around their exact expectations with only four
matching replicates per square. The center observations are sometimes above and
sometimes below both. This finite pilot gives no stable amplification signal.

Two extra outer draws found generation factors `11` for `N=209` and `43` for
`N=1333`; they remain separate outer successes. Pilot baseline root outputs,
root-factor successes, and root-decoding failures were respectively `3/1/2`
for rank-L, `1/1/0` for uniform centers, and `8/4/4` for lazy matchings. Static
screen views retained `2/0/2`, `0/0/0`, and `2/1/1`, respectively. Some static
screen factors coincide with fixed endpoints and are recorded in both fields.

## Retained 20-, 28-, and 36-bit scale

The scale reuses both F328 moduli at each bit length. Each modulus has 16
conditional square inputs and caps `16,64,256,1024`. Exact `q,b` diagnostics
remain unknown. At cap 1,024:

| Modulus | rank-L baseline/static | uniform center baseline/static | lazy matching baseline/static |
|---|---:|---:|---:|
| `b20_i0` | 14/16; 16/16 | 57/64; 64/64 | 57/64; 64/64 |
| `b20_i1` | 16/16; 16/16 | 57/64; 64/64 | 53/64; 64/64 |
| `b28_i0` | 2/16; 11/16 | 7/64; 28/64 | 10/64; 40/64 |
| `b28_i1` | 4/16; 12/16 | 13/64; 37/64 | 7/64; 38/64 |
| `b36_i0` | 0/16; 1/16 | 0/64; 2/64 | 2/64; 4/64 |
| `b36_i1` | 0/16; 1/16 | 1/64; 5/64 | 2/64; 2/64 |

All scale endpoints are verified factors; no scale trajectory returned a root.
One additional generation draw returned factor `853` for `b20_i0`.

The static screen sharply reduces F calls per factor. Its gcd charge can reverse
that comparison. For example, at `b28_i0` the lazy baseline uses 6,149.9 total
gcds per factor, while the static view uses 8,128.1. At `b28_i1` the corresponding
values are 8,845.3 and 8,339.4. The uniform-center baseline/static values are
8,874.9/12,387.2 at `b28_i0` and 4,494.0/8,432.0 at `b28_i1`. Full per-N ratios
for every cap, including floor-sum iterations, inversions, random bits, pool
size, and charged wall time, are retained in the aggregate JSON.

Zero successes occur in several 36-bit cells. Cost-per-factor fields are absent
for those cells. No probability conclusion is drawn from a finite zero.

## Isolation, randomness, and cost

The inner trajectory receives only `N`, `a`, method, cap, and an independently
derived matching seed. It never receives the hidden root or offline factors.
Hidden-root gcd decoding occurs only after a verified root output. Matching
streams use seed domains separate from hidden-root streams.

Ideal bounded sampling uses fair-bit rejection from the next power of two. The
finite implementation uses reproducible `random.Random.getrandbits` streams
and records every bounded draw, bit trial, rejection, and requested bit. The
lazy sampler draws a uniform active position directly. It never proposes a used
label. Its largest retained sparse-map size is 8,188 dictionary entries. P247's
balanced-tree expected overhead remains a separate theoretical statement; the
runtime experiment uses Python dictionaries only as authorized finite evidence.

Every cap charges failed attempts and F326 setup work. A censored cap stops
before exposing the next auxiliary edge. The static view freezes its pairing,
randomness, pool, gcd, and timing counters at first absorption while the paired
baseline may continue.

The final audit covers 10,368 screen/cap views. It verifies exact output
divisibility and root equations, hidden-root isolation, seed regeneration,
absorbing status persistence, monotone counters, exact cap censoring, six static
gcd calls per visited edge, and the lazy bounded-draw count. No retained anomaly
remains.

An earlier completed dataset exposed one accounting defect: repeated outer root
decoding at later cap views caused microsecond timing values to fluctuate after
absorption. The retained source caches one decode result and time per trajectory.
All exact, pilot, scale, and aggregate files were regenerated from the same
seeds after this fix.

## Resource and inference scope

All 12 scale batches contain eight square inputs. The longest batch took 9.497
seconds. Scale jobs used 59.072 process seconds in total and peaked at
35,749,888 bytes RSS. The largest pilot peak was 72,318,976 bytes. Every job was
single-threaded and stayed below the 28-second internal, 30-second external, and
512 MiB limits. `RESOURCE.md` retains the preflight and full run ranges.

These are finite conditional-square and matching samples. Reusing four matching
replicates per square creates the intended paired comparison; it is not 64
independent square inputs. The experiment gives no mixed-input asymptotic rate,
no structured-matching lower bound, and no quasipolynomial factoring claim.
