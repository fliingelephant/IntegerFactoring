# F103 — the F98 dependency core is public and factor-free

**Status:** exact fixed-input public replay. The peeling theorem is general,
but this experiment gives no all-input core-existence or useful-root law.

## General public operation

For any explicit relation batch, the P66 gcd-refinement decoder constructs a
binary parity matrix without factoring the relation values. If one row has
degree one, its unique column has coefficient zero in every dependency.
Deleting that column and repeating therefore preserves the complete kernel.
The remaining parity core contains every possible square dependency in the
batch.

This is a frozen-batch operation. A collector cannot delete a currently
private column before it knows that later relations will not reuse its row.

## N-only replay

The executable received only

\[
N=202{,}537{,}109.
\]

It replayed the exact public F98 source and reproduced 12,549 retained
relations, 9,414 distinct nontrivial exact values, and the same factor-free
matrix rank 8,926 and nullity 488. The matrix has 11,015 public gcd-refined
rows. Degree-one peeling removes 7,633 columns and leaves one connected core
with

\[
1{,}781\text{ columns},\qquad
1{,}298\text{ rows},\qquad
\operatorname{rank}=1{,}293,
\qquad
\operatorname{nullity}=488.
\]

Two different peeling orders give the same core. The public core-column hash
is

```text
5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8
```

This is exactly the core-column hash from the factor-assisted prime matrix in
F102, although the two row representations have different sizes. The public
166-value basis certificate lies entirely inside this core and gives

\[
R\equiv132{,}013{,}085\pmod N,
\qquad
(\gcd(R-1,N),\gcd(R+1,N))=(19{,}727,10{,}267).
\]

The core contains three seed relations and 1,778 feedback relations across
eight active-pair families and both orientations.

For the 4,293 distinct values first seen in the first 5,616 raw records, a
fresh factor-free matrix has 5,607 rows, rank 4,291, and nullity two. Peeling
leaves one connected core with 373 columns, 387 rows, rank 371, and nullity
two. Its core-column hash also equals the F102 prime-matrix hash.

## Meaning and limit

The core is a public, lossless state compressor after a batch is frozen. It
turns the vague goal “amortize many relations” into an exact source target:
force reuse of public parity rows until a rank-deficient core appears.

This does not solve the harder root-label problem. A rank-deficient core can
still contain only global roots (+1) and (-1). The fixed replay also does
not show that every composite input produces a nonempty core in polynomial
work. The authoritative run used 814,589,842 gcd tests in the unoptimized
audited refinement routine; its 60-second runtime is finite verification, not
an efficiency benchmark.
