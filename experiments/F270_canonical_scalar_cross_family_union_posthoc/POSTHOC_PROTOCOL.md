# F270-D01 post-hoc protocol — canonical scalar cross-family union

## Status and provenance

This is a discovery-only, post-hoc hypothesis-generation experiment. It is
not a preregistered test, a held-out test, an asymptotic statement, or a
factoring theorem.

The input is the authenticated F268-D04 discovery evidence. F268-D04 tested
each source family as a separate bank. Its independent result audit found a
nonsquare private parity pivot for every row in every separate bank. The same
audit explicitly left a same-modulus cross-family union open and required the
opaque block system to be rebuilt from the union row values.

The hostile theory review of this follow-up was conversation-only. It has no
artifact hash. Its verdict was `REVISE`, with the following mandatory repair:

- A union can create a dependency even when every component bank is full
  rank. At `N=697=17*41`, the rows `(U,Y)=(2,550)` and `(8,403)` are each
  privately pivoted alone, but their union has the square relation
  `2*8=4^2`. The supplied-root product is `550*403 = 4 (mod 697)`, so this
  particular cross-family dependency is a global `+1` decoy.
- For family matrices `V_f`, the cross-family quotient obeys

  ```text
  K_union / direct_sum_f K_f
      ~= {(s_f) in direct_sum_f im(V_f) : sum_f s_f = 0},
  dim gain = sum_f rank(V_f) - rank(V_union).
  ```

- Exact roots must be compared before exact-value deduplication.
- Per-family F268 `BLOCK` records must never be concatenated. The union must
  be refined from its `ROW` integer values.
- The union must undergo exhaustive simultaneous degree-one peeling to its
  fixed point before singleton, support-two, and residual P66 decoding.

The closest promoted routes are P66, P106, P108, and P109. This experiment
differs materially from F268 because it unites all twelve independently
generated row layers before refinement. It differs from P108/P109 because it
tests the canonical scalar-section source rather than their prior relation
layers.

## Frozen inputs

The exact local inputs are:

```text
F268-D04 discovery evidence
  SHA-256 a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc
F268-D04 discovery bank table
  SHA-256 c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6
F268-D04 discovery public corpus
  SHA-256 8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5
F268-D04 hostile result audit
  SHA-256 75597f68751d20ff599d68724c06182e964d935132917214a06cf653c778ee97
```

Only `ROW` records from the evidence enter the arithmetic search. The bank
table supplies the already-public `earlier_factor` control label. The public
corpus supplies `N`. Hidden factor labels do not enter this process.

The program must authenticate all 188 cases, all twelve families per case,
and exactly

```text
11*24 + 20 = 284
```

original rows per case. It must find exactly 125 cases with no earlier factor
in any family. These are the preferred clean cohort. It must also process the
remaining 63 factor-bearing cases as controls. A mismatch aborts the packet.

## Frozen arithmetic chronology

For each modulus, process all families together in family-ID and row-ID order.

1. Validate every serialized row identity, canonical range, digit
   decomposition, and supplied square-root congruence.
2. Group equal exact integer values across all families. Before deleting any
   copy, compare every pair of supplied roots as an exact support-two square
   relation. Record its exact positive root, supplied root, normalized root,
   both signed gcds, root class, and full provenance. A non-global mismatch is
   a valid P66 factor certificate. Retain the first occurrence only after all
   pair comparisons finish. Attach every discarded occurrence to its retained
   row as provenance.
3. Starting only from the deduplicated union integer values, repeatedly use
   gcd and exact division until all opaque blocks are pairwise coprime. Never
   read or concatenate an F268 per-family `BLOCK` list. Verify exact row
   reconstruction from the new blocks.
4. Build one parity equation for every nonsquare opaque block. Compute the
   original/deduplicated union rank and nullity. Independently restrict the
   same global equations to each original family, verify all twelve separate
   ranks, and compute the cross-family dimension gain.
5. Apply saturated private-primary peeling. In one round, mark every active
   row that is the unique odd incident row of at least one nonsquare opaque
   block. Delete all marked rows simultaneously. Repeat until no such row
   remains. Record every round, row, and witnessing block. This is exhaustive
   degree-one peeling, not a greedy heuristic.
6. On the fixed core only, recompute and authenticate a complete factor-free
   P66 decoder. Enumerate every singleton and every support-two rational
   square relation. Put only verified `GLOBAL_PLUS` and `GLOBAL_MINUS` low
   relations into the low-support decoy span.
7. If a useful low-support relation exists, record the terminal certificate
   and authenticate the complete core kernel; no residual quotient is needed.
   Otherwise, extend the global low-support span to a basis of the complete
   kernel and compare the root of every quotient-basis vector. This is the
   complete P66 test for the fixed core.

There are no new direct screens. Gcds with `N` occur only for input
authentication or for exact square-relation root comparisons. This is a
P66-only post-hoc discovery run.

## Frozen definitions

`original_rows` is 284. `dedup_rows` is the number after global exact-value
deduplication. `peeled_rows` is the number deleted by saturated peeling.
`core_rows = dedup_rows - peeled_rows`.

The imported separate-bank baseline is also reconstructed from the global
block system by restricting its parity equations to each family. Let
`r_f` be those ranks and `r_U` the original union rank. Then

```text
cross_dimension_gain = sum_f r_f - r_U.
```

The program must verify that each family has its full F268 row rank. Exact
value duplicates contribute `original_rows-dedup_rows` kernel directions.
The post-dedup cross gain is the deduplicated nullity.

A deduplicated row is `union-private` if it has a degree-one nonsquare block
before peeling. The deduplicated private-pivot loss is

```text
private_pivot_loss = dedup_rows - union_private_rows.
```

The original-row loss expands this through each retained row's complete
provenance. Both values are serialized.

A relation is `PURE_FAMILY` only when all original provenances in its support
have one family ID. Otherwise it is `CROSS_FAMILY`. This conservative rule
keeps an exact-value group spanning families visibly cross-family.

For every tested relation `c`, serialize

```text
R = positive_integer_sqrt(product U_i),
X = product Y_i mod N,
rho = R * X^(-1) mod N,
g_minus = gcd(R-X,N),
g_plus  = gcd(R+X,N).
```

The root class is `GLOBAL_PLUS`, `GLOBAL_MINUS`, or `USEFUL`. Any other class
is a fatal arithmetic error.

## Frozen outputs

Both preflight and target modes write deterministic TSV files:

- `cases`: per-case original, deduplicated, peeled, and core row counts;
  original/deduplicated/core rank and nullity; twelve-family rank sum;
  cross-dimension gain; separate and union private coverage; both pivot-loss
  counts; relation counts; and clean/control status.
- `rows`: every retained union row with exact `U`, supplied `Y`, canonical
  source metadata, and all original family/row/base/exponent/root/syntax
  provenance.
- `blocks`: every globally recomputed opaque block, square label, complete
  sparse exponent vector, initial union degree, and final core degree.
- `peeling`: every removed row, simultaneous round, provenance, and all
  degree-one block witnesses in that round.
- `relations`: every exact-value comparison and every singleton,
  support-two, or residual P66 relation actually tested, with full support,
  family classification, roots, normalized root, and verified gcds.
- `aggregates`: exact sums by clean/control, factor bits, and shape, plus an
  all-case row.
- `witness`: the lexicographically smallest useful relation; if none, the
  smallest cross-family relation; if none, the smallest nonempty core; if
  none, the smallest pivot-loss case; otherwise `NONE`.
- `summary`: global counts and a literal finite status.

The smallest relation order is `(N, case_index, kind, support, provenance)`.
This is an output convention, not a selection rule.

## Interpretation and held-out firewall

The target processes all 188 discovery cases, while reporting the 125 clean
cases separately and first in every synthesis. Factor-bearing cases are
controls and cannot support a strict new lead.

A new held-out packet may be proposed only if at least one clean case has a
nonempty fixed core and either:

1. that clean core contains a cross-family exact square relation; or
2. private-pivot loss repeats in at least two clean cases of the same
   `(factor_bits,shape)` cell.

This run does not create or execute that held-out packet. If every union
peels to the empty core, the exact all-twelve-family union seam is killed for
these discovery rows. Any duplicate relation is still reported, but it does
not override the empty-core kill.

Every result is finite hypothesis-generation evidence. It cannot establish
an all-input event law, an asymptotic rank theorem, a Las Vegas probability,
or quasipolynomial factoring.

## Resource gates

The implementation is C++17 with `boost::multiprecision::cpp_int`. It uses at
most eight workers, all under `nice -n 15`. Before remote execution, inspect
CPU load, memory, disk, and research processes. Do not overlap an F265, F269,
or other production run.

Compile and self-test first. Then run a capped eight-case preflight selected
deterministically from the largest cases while covering shapes and clean/
control status when available. The runner projects wall time, live memory,
and output with a factor-four safety margin. If projected wall time exceeds
14,400 seconds, projected memory exceeds 4 GiB, or projected output exceeds
512 MiB, stop with a resource result. Do not weaken the grammar.

Hard arithmetic caps are 284 input rows per case, 100,000 total input-row
bits, 65,536 opaque blocks, 1,000,000 refinement steps, 50,000 serialized
relations per case, 1,000,000 serialized relations globally, and 256 MiB of
estimated relation payload. Crossing a cap aborts the mathematical result;
it is not a null.
