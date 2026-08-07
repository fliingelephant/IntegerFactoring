# F63 — exact square-class closure criterion for feedback relations

**Status:** revised candidate proof-only theorem. No research computation was
run. The first proof-blind reconstruction found an even-input scope error and
an overstrong sequence sentence; that failed version is preserved.

Cross-relation feedback can create a new integer relation without improving
the exact square decoder. The precise distinction is whether the new relation
closes a square class already spanned by the old relation list. A genuinely
new block of odd multiplicity prevents such an immediate closure.

This is the decoder-side accounting law behind the two different F62
witnesses. At $N=21$, the relation $10\cdot19=190$ introduces the private
block $19$, so the three relation columns remain independent. At $N=55$,
the selected state $21$ is self-inverse and creates the square relation
$21^2=441$, so the kernel grows immediately.

## 1. Setup

Assume $N$ is odd; an all-input use first removes the factor $2$. Let
$B_1,\ldots,B_m$ be positive integer relation values, all coprime to $N$.
Apply complete gcd-free refinement. Omit every perfect-square block
from the parity matrix because it has zero square class, but retain the exact
relation values and exponent data for later refinement and root construction.
Let

\[
q_1,\ldots,q_r
\]

be the remaining pairwise-coprime nonsquare blocks, and write the parity of
the exponent of $q_j$ in $B_i$ as the matrix

\[
M\in\mathbb F_2^{r\times m}.
\]

Pairwise coprimality makes the block square classes independent: a product of
the $q_j$ is a rational square exactly when every selected exponent is even.
Therefore the complete exact square-relation space is

\[
\ker M.
\]

Now append one indexed feedback relation value $B_{m+1}=gw$. Refine the block list
again, including all gcds between the new value and old blocks. This
refinement can split old blocks, but it preserves the old column kernel.
Denote the refined old matrix again by $M$.

Partition the refined rows into two sets:

- old-supported rows, which occur in at least one old column; and
- new-only rows, which are zero in every old column.

Let $b$ be the parity column of $B_{m+1}$ in this refined basis. A row is
new-only when its parity is zero in every old column. This is a square-class
condition: the corresponding integer block can occur to a positive even power
in old relation values. The theorem counts indexed columns. If an
implementation deduplicates an equal relation value instead of appending it,
then no new column exists and no one-dimensional kernel increase follows.

## 2. Exact one-step criterion

### Theorem 1

Adding $B_{m+1}$ increases the square-kernel dimension by one exactly when

\[
b\in\operatorname{colspan}_{\mathbb F_2}(M).
\]

Otherwise the kernel dimension is unchanged.

In particular, if $b$ is nonzero on any new-only row, then the kernel
dimension is unchanged.

### Proof

The new parity matrix is $[M\mid b]$. If $b$ is in the old column span,
its addition does not change rank, while the number of columns increases by
one. Rank-nullity therefore increases the kernel dimension by one. If $b$
is not in the span, both rank and the number of columns increase by one, so
the kernel dimension is unchanged.

Every old column is zero on every new-only row. A column $b$ that is
nonzero on such a row cannot lie in their span. \(\square\)

## 3. Feedback interpretation

Suppose $g$ is assembled from current blocks and $w$ is its new canonical
inverse endpoint. A fully refined nonsquare block whose exponent in $gw$ is
odd and whose old parity row is zero produces a new-only row. In particular,
a factor of $w$ that is coprime to all old blocks and has odd total
square-class multiplicity is a clean sufficient condition. The new relation
then cannot create an immediate square dependency. It has enlarged the
square-class coordinate set, but it has not increased the decoder kernel.

The absence of a new-only nonsquare block is necessary, not sufficient. Even
when the new relation uses only refined old blocks modulo squares, its parity
column must still lie in the span of the old relation columns.

The strongest closure case is a self-inverse selected state. Since both
endpoints are canonical, $g^{-1}\equiv g\pmod N$ implies $w=g$. Then

\[
B_{m+1}=g^2
\]

has the zero square-class column. It gives a new singleton kernel vector. It
is factor-bearing only when $g$ is a non-global square root of one. The direct
screens of $g-1$ and $g+1$ should run before any batch decode.

## 4. Sequence accounting

For a sequence of feedback additions, let

\[
d_t=(\text{number of relation columns})-
    (\text{square-class rank})
\]

after complete refinement at time $t$. Refinement alone preserves $d_t$.
Each new relation has exactly two outcomes:

1. its square class is new, rank and column count both increase, and $d_t$
   stays fixed; or
2. its square class closes in the old span, rank stays fixed, and $d_t$
   increases by one.

Consequently, merely generating new relation values or new integer blocks
does not accumulate decoder dependencies. Any first new dependency beyond
the initial kernel must occur at a closure step. If every added relation has a
private new-only nonsquare block, the nullity stays at its initial value. In
particular, if the initial kernel is zero, no number of those additions creates
a square relation among the collected columns.

## 5. Algorithmic consequence and scope

This criterion changes the feedback objective. A selector should not be
scored only by whether it creates a new quotient or endpoint. It must create
one of these events:

- a direct proper gcd;
- a non-global self-inverse state; or
- a new relation whose square class lies in the span already collected.

The third event is the exact square-class analogue of relation closure over a
factor base. The gcd-free blocks can be composite and can split after later
refinement. This language does not assert conventional smoothness or a fixed
prime factor base. The gcd-free representation does not require prime
factorization, but the source still needs a proved all-input law that makes
closure frequent enough.

The theorem is linear-algebra accounting, not a probability bound. It does
not close iterative feedback: a block that is new-only today can recur in a
later relation and then participate in a closure. It gives no bound on when
that recurrence happens and no polynomial-time factoring algorithm.
