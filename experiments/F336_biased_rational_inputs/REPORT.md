# Biased rational inputs for count descent

**Family:** route:F31

Status: complete finite experiment. This packet establishes no success law,
QP factoring algorithm, or novelty claim.

## Protocol and coverage

The experiment implements the frozen `DESIGN.md`. For each of the twelve
F328 balanced semiprimes at 20, 28, 36, 44, 60, and 92 bits, it retains 128
trials for each of fourteen public source profiles: five direct odd-integer
scales, the five paired inverse scales, three reduced ratio scales, and one
uniform-nonzero control. Each accepted unit runs the unchanged F334 fixed-h,
fixed-multiplier min-count descent. A nonunit source draw returns its verified
proper gcd immediately. The resulting scale corpus has 21,504 standalone
policy rows.

Direct/inverse pairs share the same public denominator draw. Each row still
includes the full generation cost required by its standalone policy; the
inverse row also charges inversion. The ratio policy draws independent
numerator and denominator streams and charges both screens, ordinary
reduction, and inversion. Offline factors only label already verified outputs.

The tiny control compared F334's floor-sum oracle with 4,424 brute membership
counts and compared the complete fixed descent on all 230 tested units. It
also checked 112 sampled profile rows and rational identities plus forced unit
and generation-factor cases. The two-trial pilot retained all 56 full traces.
Both controls passed.

## Finite outcomes

The table groups profile outcomes by source type. Counts are
`generation factors + count-descent factors` over the shown denominators.
The same generation event appears once in each standalone direct/inverse law
when their shared draw is nonunit.

| input | bits | direct / 640 | inverse / 640 | ratio / 384 | uniform / 128 |
|---|---:|---:|---:|---:|---:|
| b20_i0 | 20 | 1+4 | 1+11 | 0+0 | 0+0 |
| b20_i1 | 20 | 0+5 | 0+19 | 0+7 | 0+0 |
| b28_i0 | 28 | 0+0 | 0+1 | 0+0 | 0+0 |
| b28_i1 | 28 | 1+0 | 1+0 | 0+0 | 0+0 |
| b36_i0 | 36 | 0+0 | 0+1 | 0+0 | 0+0 |
| b36_i1 | 36 | 0+0 | 0+0 | 0+0 | 0+0 |
| b44_i0 | 44 | 0+0 | 0+0 | 0+0 | 0+0 |
| b44_i1 | 44 | 0+0 | 0+0 | 0+0 | 0+0 |
| b60_i0 | 60 | 0+0 | 0+0 | 0+0 | 0+0 |
| b60_i1 | 60 | 0+0 | 0+0 | 0+0 | 0+0 |
| b92_i0 | 92 | 0+0 | 0+0 | 0+0 | 0+0 |
| b92_i1 | 92 | 0+0 | 0+0 | 0+0 | 0+0 |

There are 48 count-factor rows and four standalone generation-factor rows.
The latter come from two shared direct/inverse generation events. All uniform
controls failed, so the prescribed cost-per-success ratios to uniform are
absent rather than assigned a finite value.

The only nonzero individual profile cells and their charged costs are below.
Each cost divides the total work of all 128 attempts in that cell by its
observed successes. `FS iter/success` counts exact floor-sum Euclidean loop
iterations. Repeated source parameters are retained in the denominator.

| input | profile | gen | count | distinct unit a | gcd/success | FS iter/success |
|---|---|---:|---:|---:|---:|---:|
| b20_i0 | direct_1_2 | 0 | 4 | 102/128 | 962.750 | 2,998.000 |
| b20_i0 | direct_3_4 | 1 | 0 | 127/127 | 5,833.000 | 24,623.000 |
| b20_i0 | inverse_1_2 | 0 | 2 | 102/128 | 3,320.500 | 13,886.500 |
| b20_i0 | inverse_3_4 | 1 | 0 | 127/127 | 6,696.000 | 33,263.000 |
| b20_i0 | inverse_3_8 | 0 | 9 | 30/128 | 712.111 | 2,580.889 |
| b20_i1 | direct_1_2 | 0 | 5 | 99/128 | 767.200 | 2,500.400 |
| b20_i1 | inverse_1_2 | 0 | 5 | 99/128 | 1,294.200 | 5,494.400 |
| b20_i1 | inverse_1_4 | 0 | 14 | 8/128 | 422.571 | 1,086.071 |
| b20_i1 | ratio_1_4 | 0 | 7 | 48/128 | 831.286 | 2,729.000 |
| b28_i0 | inverse_3_8 | 0 | 1 | 102/128 | 9,763.000 | 44,728.000 |
| b28_i1 | direct_1_2 | 1 | 0 | 124/127 | 5,430.000 | 22,116.000 |
| b28_i1 | inverse_1_2 | 1 | 0 | 124/127 | 9,593.000 | 52,257.000 |
| b36_i0 | inverse_1_2 | 0 | 1 | 128/128 | 12,817.000 | 87,275.000 |

The concentrated 20-bit hits include repeated parameters; for example,
`inverse_1_4` on `b20_i1` has only eight distinct accepted multipliers in 128
trials. The experiment therefore preserves distinct counts and does not treat
repeated hits as independent parameter values.

## Diagnostics and limits

The compact rows retain every exact parameter, Jacobi sign, canonical CF digit
sum and largest digit, all 731,353 actual defects, stopping data, verified
output, and charged operation/time totals. The inverse periodic formula was
evaluated on 4,606 accepted rows whose denominator was at most 65,536; 3,072
larger-denominator rows were explicitly skipped. All evaluated formulas
matched. The triangular-wave bound was checked over 188,442 stages in all
4,608 ratio rows, with no violation. These checks support the implementation
and the author diagnostics; they do not turn either source into a probability
law.

Every count-factor trace and every generation event is retained in the
per-job witness artifacts. Ordinary scale failures retain compact rows and
are reproducible from the frozen source, seed, and exact parameters. The
aggregate file references the 24 row and witness artifacts without duplicating
them.

The finite samples demonstrate some short biased-source trajectories on small
fixed inputs and no hit on either tested input at 44, 60, or 92 bits. They do
not show an asymptotic improvement over uniform sampling because the uniform
control has no observed success, and they do not constrain randomized,
shifted, partial, approximate-with-verification, or variable-duration count
procedures outside this fixed-h protocol.

## Evidence

- Frozen design: `DESIGN.md`, SHA-256
  `fb07018513f000b1b70e697e4d51bcb4aa38e06f1d93a5642ad2c54dabc44e0c`.
- Root menu control: `MENU_BOUND.md`, SHA-256
  `d03683007e950dd689a3f47955b1805c8ceca589ac3c95c09917236286fe6cb7`.
- Solver: `biased_rational_inputs.py`, SHA-256
  `b660db8da032e3f514dfdfc5a4183defb5392b22d4cf8bcfa4ab9eaec57c5256`.
- Frozen arithmetic dependency: `../F334_count_descent/count_descent.py`,
  SHA-256
  `cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24`.
- Frozen input dependency: `../F328_capped_rabin_paths/moduli.json`, SHA-256
  `acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428`.
- Controls: `tiny_output.json`, `tiny_status.json`, `tiny_run.log`,
  `pilot_output.json`, `pilot_status.json`, `pilot_run.log`,
  `pilot_rows.jsonl.gz`, and `pilot_witnesses.jsonl.gz`.
- Scale and aggregate: all `scale_*` artifacts plus `aggregate_output.json`,
  `aggregate_status.json`, and `aggregate_run.log`.
- Resource record: `RESOURCE.md`. `SHA256SUMS.txt` covers the complete packet.
