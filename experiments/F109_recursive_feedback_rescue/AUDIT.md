# F109 hostile audit — finite observations pass; promotion remains open

## Verdict

**PASS for the bounded factor-assisted observations.**  The independent
replay matches every reported recursive and isolated count for all seven
inputs.  It does not import F109 code or the pinned F98 factor-assisted code.
SageMath 10.9/Pari supplies independent endpoint factorization.

This is not a factor-free promotion.  The narrow result is specific to the
declared FIFO queue and generation order.

## Exact results

`first +1` is the dimension of the exact-value-deduplicated first-round
kernel.  Every basis root in that column is `+1 mod N`.  `outside` counts
relations in the successful recursive dependency whose retained residue is
absent from the complete isolated seed-plus-trigger-pair menu.

| N | first +1 | trigger pair / round | recursive result | support / outside | isolated trigger pair |
|---:|---:|---|---|---:|---|
| 3,241,632,473 | 7 | `(2,13)` / 3 | factor 79,043, dependency | 378 / 323 | null; 284/284 basis roots `+1` |
| 12,809,029,193 | 6 | `(3,5)` / 3 | factor 80,107, dependency | 580 / 518 | null; 210/210 basis roots `+1` |
| 12,828,426,053 | 6 | `(2,7)` / 3 | factor 159,631, dependency | 418 / 394 | null; 356/356 basis roots `+1` |
| 12,854,972,153 | 13 | `(2,7)` / 3 | factor 80,687, dependency | 523 / 517 | null; 366/366 basis roots `+1` |
| 12,859,936,021 | 22 | `(2,13)` / 2 | factor 80,779, dependency | 634 / 605 | null; 312/312 basis roots `+1` |
| 12,862,140,737 | 24 | `(2,5)` / 3 | factor 159,179, dependency | 509 / 501 | null; 333/333 basis roots `+1` |
| 204,816,942,773 | 4 | `(2,13)` / 4 | factor 639,839, direct minus gcd | — | same direct factor |

The seventh direct event is identical in both runs:

```text
orientation = u_times_v_power
exponent = 44
c = 68137094950
w = 54674882390
gcd(c-w,N) = 639839
```

All seven factor pairs are Sage-prime-certified.  They are trial-hard through
`n^2` and satisfy the stated stability equation.  Every trigger-pair value is
in the numeric initial-seed interval `2..n`.

## Why the six isolated null results are complete

The isolated verifier retains the initial seeds and every distinct residue
from both trigger-pair trajectories through exponent `n^2`.  It applies both
direct endpoint screens.

Incremental elimination emits one dependency when a new column reduces to
zero.  That dependency contains the new column.  The emitted vectors are
therefore independent.  Their count is `columns - rank`, so they form a full
kernel basis.  An independent row-elimination calculation gives the same
rank.

For relation products `P_i = c_i w_i`, each `P_i` is `1 mod N`.  On the square
dependency kernel, the map

```text
x -> sqrt(product(P_i for i in support(x))) mod N
```

is multiplicative.  All isolated basis roots are `+1`.  Thus every isolated
square dependency is global.  The result is not limited to the dependencies
encountered in one online order.

The same argument applies to the exact-value-deduplicated first-round
kernels.  Their dimensions are `7, 6, 6, 13, 22, 24, 4`, and all 82 basis
roots are `+1`.

## Retained state and the trigger pair

The candidate calls the last processed pair the `causal_pair`.  The precise
term is **trigger pair**.  It is the pair being expanded when the first useful
prefix appears.

For the six dependency cases, the successful support has 378 to 634 columns.
It contains 323 to 605 retained residues that do not occur anywhere in the
complete isolated trigger-pair menu.  Therefore the exact successful
dependency is genuinely cross-batch.  The trigger pair alone has trivial root
image.

The numeric seed-range observation is weaker than a provenance claim.  In all
seven cases, the active record that selects the trigger pair is itself a
round-one feedback relation.  No trigger pair had been processed earlier.
The two selected block values happen to lie in `2..n`.  This supports a future
nonadaptive small-pair control.  It does not show that recursion selected an
initial-seed record.

## Queue and order artifacts

The source uses these exact choices:

1. scan retained relations in insertion order;
2. take the first at most `n` unexpanded nonzero relations;
3. freeze that active batch at the start of the round;
4. process active relations in FIFO order;
5. process exponents in increasing order and the two orientations in the
   declared order; and
6. stop at the first direct or dependency factor.

The queue contains substantial repeated work.  In round one, only 7 to 11
distinct pairs occur among 31 to 37 active records.  Between 22 and 29 pair
expansions add no relation because an earlier identical pair already generated
the menu.  Six completed round-two batches are complete no-ops: each contains
only repeated `(2,3)` pairs and adds zero relations.

These no-op batches explain part of the reported round labels.  The trigger
pair, round, prefix, and displayed dependency are facts about the frozen FIFO
order.  The audit did not establish invariance under another queue, pair,
exponent, orientation, or pivot order.  The isolated null statements are
set-level statements and do not have this weakness.

## Narrowest valid claim

For these seven named semiprimes, under the exact declared factor-assisted
FIFO process:

- the exact-value-deduplicated first-round kernel is nonempty and has trivial
  `+1` root image;
- the recursive process later produces a proper factor in every case;
- in six cases, the complete initial-seed-plus-trigger-pair batch has trivial
  root image, while the successful recursive dependency uses relations outside
  that batch; and
- in the seventh case, the trigger pair itself supplies a direct endpoint gcd.

This establishes a finite retained-state mechanism witness for six cases.  It
does not establish an all-input rescue theorem, a frequency law, feedback-block
necessity, or success of a nonadaptive scan of small pairs.

## What an N-only replay must establish

A promotion replay must receive only `N`.  It must not use `p`, `q`, endpoint
factorization, hidden-prime rows, or a hidden-factor-selected support.

It must do all of the following:

1. Reproduce the trial screen, initial seeds, residue deduplication, direct
   screens, and both trajectories through the declared bounds.
2. At each recursive queue boundary, construct the public gcd/perfect-power
   endpoint basis.  It must reproduce the nonzero flags, active relation
   indices, block supports, selected pairs, and FIFO sequence.
3. Use a complete factor-free parity refinement for each required frozen
   prefix.  It must construct a full kernel basis, form exact integer square
   roots, and obtain the six proper dependency gcds without a target selector.
4. Reproduce the seventh direct event from public modular arithmetic.
5. Recompute the exact-value-deduplicated first-round kernels and show that
   every basis root is `+1`.
6. Replay each complete isolated trigger-pair menu.  It must show that all
   direct screens are null and that a full kernel basis is global for the
   first six cases.
7. Record public relation indices for each useful recursive certificate and
   show which selected relations are absent from the corresponding isolated
   menu.

Factor-free gcd refinement gives a route to these checks on a frozen batch.
It does not replace the missing execution of the recursive N-only queue.

## Reproducibility

Run:

```text
python3 experiments/F109_recursive_feedback_rescue/run_F109_hostile_audit_with_timeout.py
```

The named wrapper invokes Sage, enforces a 900-second hard timeout, and writes
`AUDIT_OUTPUT.json` and `AUDIT_RUN.log`.  The authoritative audit completed
with exit code 0 in 10.057436 seconds.  The inner verifier took 7.088140
seconds.  No audit attempt failed.  Candidate artifact hashes remained
unchanged.
