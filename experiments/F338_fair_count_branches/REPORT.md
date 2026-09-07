# Fair count branches on the F336 source corpus

**Family:** route:F31

Status: complete finite comparison. This packet proves no uniform success
probability, asymptotic advantage, or quasipolynomial factoring result.

## Protocol and accounting

F338 reuses all 21,504 frozen F336 standalone source rows: twelve moduli,
fourteen profiles, and 128 trials per profile. It keeps all four
generation-factor rows from the two shared direct/inverse source draws. No row
was selected by an outcome.

For each accepted unit, F338 retains the same public multiplier and start
t=(N-1)/2. It preserves F336's t, q, and t-q gcd screens and their exact
both-child charge. If both children are positive and no screen succeeds, bit
zero selects q and bit one selects t-q. Each row has an independently derived
branch stream from seed 33820260907 and its frozen row ID. The run applies no
Jacobi filter, added screen, root routine, or per-attempt path cap.

Every frozen minimum-child result was replayed with F334. Status, output,
stopping reason, stage, count sequence, and defects matched all 21,500 accepted
unit rows. For each such row, subtracting the replayed additive descent
counters from the frozen standalone counters gave a nonnegative
source-generation and transform vector. F338 adds its fair-descent counters to
that vector. Maximum fields are retained separately and combined by max. No
wall-clock time is subtracted. Because a source-only maximum cannot in general
be recovered by subtraction, each combined maximum_* value is a conservative
envelope max(original combined maximum, fair-descent maximum), not a newly
measured exact maximum for the fair standalone run. The original standalone
time remains labeled as an undecomposed minimum-policy measurement.

All failed work, source randomness, transforms, floor-sum Euclid iterations,
gcd Euclid divisions, and branch bits are charged. A zero-success cell has no
cost-per-success value.

## Pilot

The pilot passed in 0.075 seconds at 41,058,304 bytes peak RSS. Its exact branch
trees matched the repaired active DP:

| N,a | Fair success | Expected queries | Expected gcd calls | Expected branch bits | Maximum queries |
|---|---:|---:|---:|---:|---:|
| 25,8 | 1/2 | 5/2 | 15/2 | 2 | 3 |
| 35,4 | 1/2 | 5/2 | 7 | 3/2 | 3 |

The minimum-child path fails in both examples. The pilot also retained full
minimum and fair traces for all 56 rows at source indices 0 and 1 on b20_i0
and b20_i1. Every replay and counter split matched.

## Finite outcomes

The table reports minimum -> fair as generation factors + count factors. Direct
and inverse each have denominator 640 per input, ratio has 384, and uniform has
128.

| input | bits | direct | inverse | ratio | uniform |
|---|---:|---:|---:|---:|---:|
| b20_i0 | 20 | 1+4 -> 1+7 | 1+11 -> 1+7 | 0+0 -> 0+2 | 0+0 -> 0+0 |
| b20_i1 | 20 | 0+5 -> 0+8 | 0+19 -> 0+12 | 0+7 -> 0+7 | 0+0 -> 0+0 |
| b28_i0 | 28 | 0+0 -> 0+0 | 0+1 -> 0+2 | 0+0 -> 0+1 | 0+0 -> 0+0 |
| b28_i1 | 28 | 1+0 -> 1+0 | 1+0 -> 1+0 | 0+0 -> 0+1 | 0+0 -> 0+0 |
| b36_i0 | 36 | 0+0 -> 0+0 | 0+1 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b36_i1 | 36 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b44_i0 | 44 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b44_i1 | 44 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b60_i0 | 60 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b60_i1 | 60 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b92_i0 | 92 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |
| b92_i1 | 92 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 | 0+0 -> 0+0 |

Minimum branches have 48 count factors. Fair branches have 47. At the paired
row level, fair branching rescues 21 minimum failures, loses 22 minimum
successes, and preserves 26 count successes with the same factor. The four
generation-factor rows are unchanged and represent two shared draws, not four
independent discoveries.

All 47 fair count hits occur on the two 20-bit inputs and the two 28-bit
inputs. Their first-hit stages range from 0 through 8, with mean 2.596.
Uniform remains zero on every input. The fair stopping totals are 12,261 empty
sides, 9,192 selected children at most one, 47 child-count factors, and four
paired generation-factor rows.

Without a path cap, the largest observed count-query totals at 20, 28, 36, 44,
60, and 92 bits were 23, 30, 37, 45, 61, and 93. These are finite observations,
not deterministic bounds.

## Per-input/profile charged comparisons

The aggregate JSON contains exact total operation vectors and cost per observed
success for all 168 input/profile cells. The table below lists every cell where
either policy succeeds. Each cost is Q calls/gcd calls over all 128 attempts.
The fair column also gives branch bits per success. A dash is an undefined
zero-success cost. “gen” means its only success is the shared source-generation
factor and has no path hit stage.

| input/profile | minimum: successes; Q/gcd | fair: successes; Q/gcd/branch | fair hit stages |
|---|---:|---:|---:|
| b20_i0/direct_1_2 | 4; 318.0/962.8 | 7; 188.4/570.0/173.9 | 0--5 |
| b20_i0/direct_3_4 | 1; 1929.0/5833.0 | 1; 2005.0/6041.0/1903.0 | gen |
| b20_i0/inverse_1_2 | 2; 1092.5/3320.5 | 2; 1135.0/3446.5/1111.5 | 0 |
| b20_i0/inverse_3_4 | 1; 2202.0/6696.0 | 1; 2272.0/6905.0/2233.0 | gen |
| b20_i0/inverse_3_8 | 9; 234.1/712.1 | 5; 447.4/1359.0/437.6 | 2--4 |
| b20_i0/ratio_1_4 | — | 2; 1008.5/3191.0/981.0 | 3--8 |
| b20_i1/direct_1_2 | 5; 253.0/767.2 | 8; 163.9/495.5/150.8 | 0--8 |
| b20_i1/inverse_1_2 | 5; 426.6/1294.2 | 4; 556.8/1687.8/541.2 | 0 |
| b20_i1/inverse_1_4 | 14; 138.7/422.6 | 8; 275.8/833.6/265.1 | 4--8 |
| b20_i1/ratio_1_4 | 7; 261.6/831.3 | 7; 277.3/878.3/267.9 | 0 |
| b28_i0/inverse_1_2 | — | 1; 3303.0/9987.0/3252.0 | 2 |
| b28_i0/inverse_3_8 | 1; 3227.0/9763.0 | 1; 3302.0/9980.0/3247.0 | 4 |
| b28_i0/ratio_1_4 | — | 1; 3266.0/10130.0/3213.0 | 8 |
| b28_i1/direct_1_2 | 1; 1798.0/5430.0 | 1; 1871.0/5641.0/1771.0 | gen |
| b28_i1/inverse_1_2 | 1; 3170.0/9593.0 | 1; 3248.0/9818.0/3194.0 | gen |
| b28_i1/ratio_1_4 | — | 1; 3200.0/9934.0/3149.0 | 3 |
| b36_i0/inverse_1_2 | 1; 4246.0/12817.0 | — | — |

The complete operation totals are:

| policy | successes | Q calls | floor-sum Euclid iterations | gcd calls | gcd Euclid divisions | source plus branch fair bits | branch bits |
|---|---:|---:|---:|---:|---:|---:|---:|
| minimum | 52 | 731,353 | 17,962,599 | 2,213,824 | 37,655,262 | 437,916 | 0 |
| fair | 51 | 750,607 | 18,100,900 | 2,270,280 | 37,810,996 | 1,176,215 | 738,299 |

Accordingly, total Q/gcd/floor-Euclid costs per observed success are
14,064.5/42,573.5/345,434.6 for minimum and
14,717.8/44,515.3/354,919.6 for fair. These pooled finite ratios do not replace
the per-input/profile values and do not define a mixed-input law.

## Evidence and scope

All 24 scale jobs passed in 22.854 summed process seconds. The slowest took
2.633 seconds and peak RSS stayed below 151 MiB. Aggregation found exactly
21,504 distinct row IDs, four generation rows, two shared generation events,
zero anomalies, and no resource censor.

Compact gzip rows retain every operation vector, source-row hash, branch seed,
defect list, first-hit stage, stop reason, and verified output. The pilot keeps
all full traces. Scale witness artifacts keep the first full trace for every
distinct verified output key in each batch; there are 31 retained scale
witnesses. All other rows reproduce from their frozen source row and branch
seed.

The fair branch changes which finite rows reach factors, but it has one fewer
count success and higher pooled charged cost in this sample. This does not
rule out a different fair sample, source law, adaptive multiplier rule, or
another partial-output procedure. Finite zero cells remain undefined and carry
no asymptotic conclusion.
