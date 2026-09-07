# Random rank gaps

**Family:** route:F31

Status: complete finite experiment. This packet establishes no QP success
law, source advantage, large-input scaling claim, or novelty claim.

## Protocol and coverage

The solver implements the frozen design in
`../F336_biased_rational_inputs/RANDOMIZED_WINDOWS.md`. For each
`N` in `{209,1333,10807}`, it makes eight public parameter attempts under
each of seven laws: uniform; direct and inverse at scales `1/4` and `1/2`;
and ratios at scales `1/4` and `3/8`. Every unit parameter is evaluated at
`floor(sqrt(N))`, `floor((N-1)/8)`, and `(N-1)/2`. Nonunit source draws are
retained as verified generation-factor outputs and supply no diagnostic cell.

The full runs contain 168 parameter attempts. They produced 153 units and
15 standalone generation-factor rows, from eight underlying source events
after identifying the paired direct/inverse draws. The 459 unit cells retain
all source parameters, duplicates, seeds, generation costs, the separate
`gcd(t,N)` and `gcd(t+1,N)` controls, and exact energies for `mu`, `nu`, and
uniform ranks. Neither control found a factor in these cells.

Every cell checked positive gaps summing to `N`, the complete three-class
successor partition, the closed duplicate-energy formula, and 18 rank queries.
This gives 8,262 independent/end-point threshold checks and 433,115 full
class-image rank checks. All three law energies in the 147 `N=209` cells also
matched direct quadratic enumeration. The larger inputs used grouped residue
sums. No check reported an anomaly.

The full arrays, class images, and factor labels are offline diagnostics. The
public `mu` sampler needs one threshold rank query per sample. The public `nu`
sampler charges its extremum setup and one rank query per sample. The output
records 11,699 setup rank queries and the exact generation/setup operation
counts. It does not charge the 433,115 offline validation queries as runtime
work.

## Useful and duplicate energy

The following are cell-wise means conditional on obtaining a unit source
parameter. Exact fractions are retained in the raw outputs. `same` is the
integer-rank duplicate energy `kappa_same`.

| N | cells | mu delta / same | nu delta / same | uniform-rank delta / same |
|---:|---:|---:|---:|---:|
| 209 | 147 | 0.057719 / 0.279740 | 0.070236 / 0.162715 | 0.080096 / 0.037743 |
| 1333 | 144 | 0.027023 / 0.258154 | 0.031287 / 0.121132 | 0.035094 / 0.011505 |
| 10807 | 168 | 0.010964 / 0.131835 | 0.011248 / 0.081509 | 0.012409 / 0.003514 |

Thus both sampled gap laws have lower mean useful energy than uniform ranks on
each tested input, while also having greater duplicate energy. Individual
cells vary: `mu` exceeds the same-cell uniform-rank delta in 8/147, 14/144,
and 34/168 cells; `nu` does so in 43/147, 32/144, and 52/168 cells. These are
fixed finite frequencies, not estimates for other inputs.

Each of the 1,377 cell-law records includes exact `kappa_p`, `kappa_q`,
`kappa_same`, direct-rank gcd mass, `delta`, `eta`, and the stated second-moment
success lower bounds for `K=2,8,32`. It also retains all 3,241 nonempty ordered
class-pair energies. The packet does not average the conditional bounds into
an asserted source theorem.

## Strongest individual cells

The strongest retained `mu` ratio is post hoc. It occurs at `N=10807`, source
`direct_1_2`, public draw `b=79`, `a=79`, and `t=103`. Its two classes have
`(size,gap)=(103,79)` and `(1,2670)`. The exact energies are

    delta_mu = 4424/1156349,
    delta_uniform = 3/5408,
    delta_mu/delta_uniform = 23924992/3469047 = 6.896704...,
    kappa_same_mu = 7771723/116791249,
    eta_mu = 581818726/1262163027943.

Its direct-rank gcd mass is `79/10807`, below the uniform-rank mass `1/104`.
The `K=2,8,32` second-moment bounds are, respectively,
`4424/1156349`, `21894376/511626175`, and `96960808/505522813`.
The only nonzero conditional class-pair energies are `4/10609` within the
103-element class and `1/103` in each direction across the two classes. The
two cross terms supply exactly `1335/1414` of `delta_mu`, so the useful energy
is concentrated on the singleton/large-class boundary.

The strongest retained `nu` ratio also occurs at `N=10807` and `t=103`, but
at source `direct_1_4`, draw `b=5`, and `a=5`. Its classes have
`(size,gap)=(103,5)` and `(1,10292)`. Here

    delta_nu = 105/21218,
    delta_uniform = 3/5408,
    delta_nu/delta_uniform = 94640/10609 = 8.920728...,
    kappa_same_nu = 26/103,
    eta_nu = 2679/2185454.

The `nu` direct-rank gcd mass is `1/206`, while the uniform-rank direct mass is
`1/104`. Its `K=2,8,32` bounds are `105/21218`, `102900/3005251`, and
`364560/2675747`. In particular the `K=32` value `0.136246...` is below the
uniform-rank value `1488/9833 = 0.151327...`: the two cross-class terms supply
`103/105` of `delta_nu`, but repeated collisions share the heavy endpoint and
raise `eta`.

Both strongest cells are unwrapped direct cases, since `a*t<N`. In any such
case, `mu` is the mixture

    (a*t/N)*Uniform{0,...,t-1} + (1-a*t/N)*point(t).

For the displayed two-class `nu` cases it is

    (1/2)*Uniform{0,...,t-1} + (1/2)*point(t).

These laws can be sampled directly without floor sums. They are therefore the
appropriate cheap controls for the two post hoc maxima; their large ratios do
not by themselves justify a larger experiment.

## Inverse-source transfer check

The separate root derivation `INVERSE_GAP_TRANSFER.md` was checked during the
same runs. For inverse-source cells with `b<=t+1`, all cluster starts, lengths,
boundary ranks, half-orbit residual identities, nonzero bounds, and gcd
transfers matched the sorted arrays. Coverage was 39 cells and 315 half-orbit
boundary pairs for `N=209`, 36 cells and 982 pairs for `N=1333`, and 44 cells
and 41,277 pairs for `N=10807`; four additional `N=10807` cells explicitly
had `b>t+1` and were not evaluated.

There were 18, 24, and 479 proper boundary-pair gcds, respectively, in cells
where the small-`b` exclusion need not apply. The guard
`p_min>2*b^2` applied to 16 half-orbit cells and 137 boundary pairs across
`N=1333` and `N=10807`; none had a proper gcd. Every pair and all guarded
statuses remain in the raw output.

## Scope

This experiment computes exact finite energies. It does not execute a
large-input randomized rank sampler or prove a charged cost/success bound.
The lower averages do not close randomized, biased, shifted, partial,
approximate-with-verification, or variable-duration procedures. No
larger-input run follows from these averages alone.

## Evidence

- Frozen design: `../F336_biased_rational_inputs/RANDOMIZED_WINDOWS.md`,
  SHA-256
  `421936d7e539483cfcb1dbf22302d166cd35e42d5c7bddb89921bcec1acfdb84`.
- Inverse diagnostic: `INVERSE_GAP_TRANSFER.md`, SHA-256
  `8254a944670559369014e2e984d69f61345e281fb0849f80a5c1a2becf12a51d`.
- Solver: `random_rank_gaps.py`, SHA-256
  `187e35a09f704ce29bdce7c42820a23551801cb835a80fc32575f4732e4e08e1`.
- Pilot: `pilot_output.json`, `pilot_status.json`, and `pilot_run.log`.
- Full data: `full_N209_output.json`, `full_N1333_output.json`,
  `full_N10807_output.json`, their status/log files, and
  `aggregate_output.json`, `aggregate_status.json`, `aggregate_run.log`.
- Resource record: `RESOURCE.md`. `SHA256SUMS.txt` covers the packet.
