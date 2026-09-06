# F261-D02 V2 preregistration — centered-carry scaling and prefix search

## Status

This file fully freezes the repaired V2 experiment before its first compile
or cohort run. The exact theorem is in `V2_ALGEBRA.md`. Computation is for
conjecture discovery, counterexample search, and finite scaling evidence
only. V2 is a new immutable hash set. It does not modify or supersede the V1
record.

F261-D02 is incompatible with F258, F259, and F260. It must not compile,
benchmark, generate cohorts, or scan while any of those experiments is
running on `seetacloud`.

## Exact source family and convention

Every generated row has distinct odd primes

\[
2^{f-1}\le p<q<2^f,\qquad q<2p,
\]

with `f` in

```text
16,20,24,28,32,36,40,44,48,52,56,60.
```

For `N=pq`, set `n=bit_length(N)`, `m=floor(n/2)`, and `B=2^m`.
The row is retained only when `B | N-1`.  Put `H=(N-1)/B`.

For every multiplier, the two centers are independently defined by

```text
Kp = floor((u*p + B/2)/B)
Kq = floor((u*q + B/2)/B)
```

using exact round-half-up.  A tie maps to residue `-B/2`.  The scan never
calls a forced common-center carry a nearest-center carry.

## Frozen deterministic cohorts

The source uses the 64-bit SplitMix function and the literal cohort tags in
`V2_search.cpp`. For each `(factor_bits,cohort,serial)` value in one frozen
cell stream, it hashes one odd exact-bit candidate `p`. It tests primality
with the deterministic 64-bit Miller--Rabin bases in the source. For each possible product bit
length `2f-1,2f`, it computes the unique exact-`f`-bit candidate congruent to
`p^{-1}` modulo the corresponding `B`.  It then checks all displayed domain
conditions and the cohort predicate.

The counts at every factor size are:

```text
random balanced zero-defect:                 64
close-ratio zero-defect, q/p <= 33/32:        24
edge-ratio zero-defect, q/p >= 63/32:         24
safe-safe zero-defect:                         2
```

`safe-safe` means that `p,q,(p-1)/2,(q-1)/2` are all prime.  The generator
has these frozen total attempt caps per `(factor_bits,cohort)` cell:

```text
random:      20,000,000
close:       50,000,000
edge:        20,000,000
safe-safe:  200,000,000.
```

For the edge cohort only, the deterministic SplitMix word is reduced modulo
the number of odd integers in the exact interval in which `q/p>=63/32` is
possible. All other cohorts use the same deterministic modulo map on the
complete exact-bit odd interval. This is a frozen pseudorandom ordering rule,
not a claim of exact statistical uniformity. Exhausting a cap aborts the run.
It does not replace the cohort.  All 1,368 generated moduli must be globally
distinct; a collision is skipped within the same frozen attempt stream.

Exact consecutive-prime zero-defect pairs are too sparse to prescribe a
tail count without bias.  A separate frozen audit enumerates every adjacent
prime pair with equal factor bit length `8<=f<=22`, checks the same balance
and zero-defect conditions, and writes every survivor.  Its count can be
zero.  It is not replaced by the close-ratio cohort and is not included in
the train or heldout scores.

Factor sizes through 40 bits are `train`.  Sizes 44 through 60 bits are
`heldout`.  The split is disjoint by construction.  Predictor selection
uses only train rows.  The heldout rows are evaluated after selection.

## Frozen multiplier and carry scales

For each row put

```text
U1 = n
U2 = n^2
U3 = min(n^3, 2^20).
```

Scan every `1<=u<=U3`.  Compute the exact nearest-center carry and abort on
failed carry integrality, trace divisibility, or the weighted-trace identity.
The small self-test checks the discriminant and decoder endpoints with Boost
Multiprecision; expanding that square identity at every scan point would not
add an independent check.

The hidden-label true-carry thresholds are

```text
C1 = n
C2 = n^2
C3 = n^3.
```

Also score the exact theory-scale threshold

```text
Cqp = 2^((ceil(log2 n))^2).
```

`Cqp` is a fixed numerical-QP value. Its candidate-bound arithmetic is
evaluated exactly. No candidate tuple is iterated at any threshold. Every
cap event uses the hidden true carry and is named `oracle_hit_*`. It is not
an executed or verified factor-bank hit. For every `Ui`, report `min |c_u|`
and its first multiplier. For every threshold, report the oracle hit count
and first oracle hit through `U3`. Preserve every cell maximum and its exact
row.

The program reports the theorem-only candidate-bank upper bound obtained from
equation (10), using the exact public center interval sizes and each prefix
schedule, at `(U2,C2)` and at the theory-scoring pair `(U2,Cqp)`.  It does
not enumerate the `O(u^2)` center pairs, direct `T` values, quadratic or
linear decoder roots, or verified candidates. Other caps use the proved
formula and are not separately aggregated. No factorization claim can be
derived from an oracle hit or a reported cost bound.

## Frozen beta-two prefix schedules

For `m=log2 B`, use these four schedules:

```text
none:       t=0
eighth:     t=floor(m/4)
three8:     t=floor(3m/8)
quarter:    t=floor(m/2).
```

For `t=0`, set `R=1` and define `a=b=0`. Do not call a modular inverse. For
`t>0`, set `R=2^t`, `a=p mod R`, and compute the operational companion
`b=N*a^{-1} mod R`. The full hidden labels are used only to verify that
these values are correct. Report the exact filter upper bound

```text
sum_{u<=U} (#Kp(u) * #Kq(u)) * (1 + floor(2C/(uR))).
```

For each schedule, also report whether the prefix alone meets the
known-residue terminal with the fixed slack `S=n^2`, checked without real
arithmetic by `R^4*S^4 >= N`.  Any such row is labelled `prefix_terminal`.

The raw event `|c_u|<=C` does not depend on which prefix is revealed.
Prefix-dependent changes can arise only because a public predictor chooses
different multipliers or because the verified bank has fewer candidates.

## Frozen public multiplier predictors

Each predictor sees only `(N,B,H,R,a,b,n)` and searches the universe
`1<=u<=U2`.  It returns at most `n` distinct multipliers, with score ties
broken by smaller `u`.

```text
first             u=1,...,n
hash              n deterministic SplitMix samples
prefix_linf       minimize max(|center_R(ua)|,|center_R(ub)|)
prefix_l1         minimize |center_R(ua)|+|center_R(ub)|
prefix_product    minimize |center_R(ua)*center_R(ub)-u^2|
sqrt_distance     minimize |center_B(u*floor(sqrt(N)))|
H_distance        minimize |center_B(uH)|
product_surrogate minimize |K0^2*B-u^2H|,
                  K0=floor((u*floor(sqrt(N))+B/2)/B)
cf                for a nontrivial prefix, bounded convergents and
                  semiconvergents of a/R, b/R, (a+b mod R)/R, and
                  |a-b|/R; with no prefix, use H/B and
                  floor(sqrt(N))/B.
```

Every continued-fraction list is truncated deterministically to its first
`4n` distinct denominators at most `U2`; the final predictor retains its
smallest `n` distinct values.  An empty list falls back to `first`.

For each prefix, rank predictors on train rows by this frozen lexicographic
score:

1. larger minimum cell success fraction for `min |c|<=n^2`;
2. larger total train success count at the same threshold;
3. smaller lower median of `min |c|`;
4. predictor name.

The lower median of a sorted list of length `L` is entry
`floor((L-1)/2)`. This is an exact integer key. Because
`x -> log2(1+x)` is strictly increasing, it gives exactly the same ordering
as the lower median of `log2(1+min |c|)`. It requires no floating-point
arithmetic and has no even-sample ambiguity.

Select the first three predictors. Only these selections count as heldout
leads.  Scores for the other fixed predictors remain diagnostic multiple
comparisons.

## Frozen oracle diagnostics

These fields use hidden `p,q,Kp,Kq,c` and are never called operational.

- longest constant-first-difference run of `c_u` through `U2`;
- maximum exact `c` collision fibre through `U2`;
- zero count, displayed maximum `v2(c)`, and `gcd(c,u)` extrema; the
  displayed valuation is the maximum finite value over nonzero carries when
  no zero occurs, and the frozen sentinel `128` when any zero occurs;
- membership of each oracle minimizing `u` in continued-fraction sets of
  the hidden ratios `p/B` and `q/B`;
- modular ranks over `1000000007` and `1000000009` of all monomials in
  `(u,Kp,Kq,c)` through degree two and degree three, on 64 fixed samples.

The exact weighted-trace relation forces at least one quadratic relation,
so generic rank ceilings are 14 of 15 and 30 of 35.  Only rank below those
ceilings is an anomaly.

Three public center surrogates are also tested diagnostically: one common
`floor(sqrt(N))` center, the public lower/upper balance endpoints, and the
nearest integer center product to `u^2H/B`. Report their exact-match
frequency and raw polynomial ranks when paired with the oracle carry. The
excess rank defects are the frozen ceilings 14 and 30 minus these raw ranks.

## Frozen one-dimensional inverse-map study

After the row scan, select the unique worst `U3` row in every
`(factor_bits,cohort)` cell.  For each nontrivial prefix and its first odd
oracle-minimizing multiplier, study equations (12)--(14).

- If `B/R<=4096`, enumerate the complete map.
- Otherwise take 4096 distinct public samples from one frozen odd-step
  affine permutation of the `z` indices.
- Separately take a clipped consecutive window of at most 2048 indices
  around the hidden true `z`.  This window is labelled `oracle_window`.

Report oracle hit counts at all four carry thresholds, exact and absolute-carry
collision fibres, longest affine run in the consecutive window, valuation
extrema under the same zero sentinel, and the rank of the true `|c|` among
the public sample plus the true point. Preserve the smallest anomaly and
worst hostile witness.

The map has `B/R` candidates.  Sampling it is not a factoring algorithm.

## Output and interpretation gates

The run writes:

```text
output/F261-D02.summary.json
output/F261-D02.rows.tsv
output/F261-D02.inverse.tsv
output/F261-D02.consecutive.tsv
logs/F261-D02.stdout
logs/F261-D02.stderr
```

Dense `u` traces are forbidden.  Rows contain only exact aggregates,
predictor minima, and selected witnesses.  Total output must remain below
1 GiB.

A finite useful lead requires all of the following:

1. a predictor selected on train data improves both `first` and `hash` on
   every heldout cohort type, not only random rows;
2. the improvement persists at 52, 56, and 60 factor bits;
3. the selected bank is nonterminal and its exact candidate bound fits the
   declared numerical-QP grammar;
4. any symbolic anomaly survives both modular ranks and exact replay on its
   preserved witness.

Failure of a fixed predictor or a finite declining hit rate is not an
asymptotic lower bound.  A positive finite pattern is not an inverse-QP
theorem.

## Frozen resource and workflow gates

The implementation is `V2_search.cpp` in C++17. Deterministic 64-bit
primality and bounded signed 128-bit carry arithmetic are exact on the frozen range; Boost
Multiprecision is used for candidate-count and theory-threshold integers.
No floating-point value controls a mathematical decision.

The exact self-test must verify all of these V2 repairs before preflight:

1. `R=1` returns `a=b=0` without entering the inverse branch;
2. the lower-median integer key and its even-list convention select the
   preregistered order, including a witness on which the V1 raw mean differs;
3. `product_surrogate` uses `floor(sqrt(N))`, including the exact
   `N=11009,B=128,u=19,K0=15` regression;
4. the worker-aware projection uses the requested worker count and the
   frozen 75 percent parallel-efficiency factor; and
5. the output schema marks true-carry events as oracle diagnostics and the
   compiled constant `executes_factor_bank` is false.

Before launch:

1. inspect remote load, memory, disk, and processes;
2. require F258, F259, and F260 to be absent;
3. compile and pass the exact small self-test;
4. run the frozen public inner-loop benchmark and pass the actual launch
   worker count into its projection;
5. compute scan time with the conservative 75 percent parallel-efficiency
   factor, add the serial generator projection, and abort before cohort generation if the
   total exceeds 14,400 seconds.

The full run uses `nice -n 15`, `timeout 14400s`, at most eight workers,
projected RSS below 4 GiB, and at least 5 GiB free disk.  The default runner
uses four workers.  It may be reduced under load.  It may not be increased
above eight or overlapped with an incompatible experiment.
