# F102 — the F98 pool has a large lossless parity core

**Status:** factor-assisted finite diagnosis. This is not an all-input source
law and not a factoring algorithm.

## Lossless peeling theorem

Let a binary matrix have relation columns and parity rows. Suppose an active
row occurs in exactly one active column (j). In every kernel vector, the
coefficient of column (j) must be zero. Therefore column (j) can be
deleted without changing the kernel, apart from restoring a zero coordinate.
Repeating this operation gives a unique remaining parity core and preserves
the full kernel and its nullity.

This theorem applies to a frozen relation batch. It does not justify deleting
a column during streaming collection. A later column can reuse a row that is
currently private.

## Fixed-input result

For the 9,414 distinct exact values in the F98 pool at

\[
N=202{,}537{,}109,
\]

the factor-assisted prime-parity matrix has 11,034 rows, rank 8,926, and
nullity 488. It has 7,884 degree-one rows before peeling. Lossless peeling
deletes 7,633 columns and leaves one connected core with

\[
1{,}781\text{ columns},\qquad
1{,}299\text{ rows},\qquad
\operatorname{rank}=1{,}293,
\qquad
\operatorname{nullity}=488.
\]

The 166-value circuit from P105 lies entirely inside this core. The core
contains three seed relations and 1,778 feedback relations from eight
active-pair families and both trajectory orientations. Thus the selected
circuit is not an isolated component created by post-selection.

For the distinct values first seen within the first 5,616 raw records, the
matrix has 4,293 columns, 5,658 rows, rank 4,291, and nullity two. Peeling
leaves one connected core with 373 columns, 387 rows, rank 371, and the same
nullity two. This prefix shows that column surplus is sufficient but not
necessary for a dependency: its core has more rows than columns but still
has rank defect two.

## Meaning and limit

The useful mechanism now has a sharper description. Feedback creates many
integer presentations. Most have a private parity row and can never enter a
dependency in the frozen batch. The surviving core is the part where parity
rows are reused, and all useful dependencies live there.

This is only a structural compression and diagnostic. The computation uses
factorization of the relation values, so it is not a public algorithm step.
It does not prove that another input has a nonempty core, a rank defect, or a
non-global root. An all-input theorem must force a polynomial-size public
analogue of this core and must also prove that the root image contains more
than global \(\pm1\).
