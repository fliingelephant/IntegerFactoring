# F102 proof-blind reconstruction statement

Reconstruct and verify the following theorem and finite diagnosis without
reading any other file in this F102 directory.

## Allowed arithmetic artifact

The only external artifact you may read is

```text
../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

Its required SHA-256 is

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab
```

You may factor exact relation values because this is a factor-assisted
diagnosis. Do not treat factorization as a public algorithm step.

## General theorem

Let a binary matrix have relation columns and parity rows. Repeatedly choose
an active row of degree one and delete its unique active column. Prove that
each deletion preserves the kernel by zero extension. Prove that the final
column set is the unique greatest set in which every incident row has degree
at least two. Thus the final set and preserved kernel are independent of the
peeling order.

Explain why this applies only to a frozen batch. A later streaming column can
reuse a row that is currently private.

## Finite reconstruction

For (N=202{,}537{,}109), regenerate the F98 first-occurrence relation stream
from the public seeds, active pairs, and bound. Remove (P=1) and repeated
exact values. Factor the remaining values. Make one binary column per value
and one row per prime with odd valuation.

For the full pool, reconstruct:

```text
columns                   9414
rows                     11034
rank                      8926
nullity                    488
initial degree-one rows   7884
peeled columns            7633
core columns              1781
core rows                 1299
core rank                 1293
core nullity               488
core components          [1781]
```

The ordered core-column SHA-256 is

```text
5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8
```

All 166 columns in the pinned public useful certificate are in this core.
The core contains three seed relations and 1,778 feedback relations. The
seed values are 2, 11, and 27. The feedback records cover eight active-pair
families. The orientation counts are 1,138 `u_power_times_v` and 640
`u_times_v_power`.

Also select every distinct value whose first raw occurrence is before raw
record 5,616. Reconstruct:

```text
columns                   4293
rows                      5658
rank                      4291
nullity                      2
initial degree-one rows   4062
peeled columns            3920
core columns               373
core rows                  387
core rank                  371
core nullity                 2
core components           [373]
```

The ordered prefix-core SHA-256 is

```text
9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df
```

Use at least two materially different peeling orders and verify that they
give the same two cores.

## Required scope

Conclude only that the frozen F98 prime-parity matrix has a large unique core
that preserves its complete kernel, and that the selected useful certificate
is contained in that core. The prefix shows that column surplus is not
necessary for a finite rank defect.

Do not claim that the prime matrix is public, that connectedness implies a
useful root, that every composite input has a nonempty or rank-deficient
core, that useful circuits have inverse-polynomial density, or that this is a
factoring algorithm.
