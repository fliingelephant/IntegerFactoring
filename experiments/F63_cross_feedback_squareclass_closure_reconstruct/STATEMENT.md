# Proof-blind reconstruction statement — square-class closure under feedback

Reconstruct or refute every claim below. Work from this file only. Do not read
the candidate proof, its audit, `PROVED.md`, `FAILED.md`, or
`notes/Progress.md`.

## Setup

Let $B_1,\ldots,B_m$ be indexed positive integer relation values. Apply
complete gcd-free refinement and represent their exact square classes by a
matrix $M\in\mathbb F_2^{r\times m}$ on pairwise-coprime nonsquare blocks.
Perfect-square blocks are omitted from the parity matrix only; exact relation
values and exponent data remain available for later refinement and root
construction.

Append one indexed feedback relation $B_{m+1}=gw$. Refine all old and new
values together. This can split old blocks but is claimed to preserve the old
column kernel. Call the refined old matrix again $M$, and let $b$ be the new
parity column. A row is `new-only` when it is zero in every old column. This
means new in square-class parity; the underlying integer block can occur to an
even positive power in old values.

## Claims to reconstruct

1. Pairwise-coprime nonsquare blocks have independent rational square classes.
   Therefore $\ker M$ is exactly the complete square-relation space of the
   indexed list, even when a block is composite or a prime power.

2. Complete gcd-free refinement preserves the old kernel because it only
   changes exact coordinates for the same integers.

3. Appending the indexed column $b$ increases the kernel dimension by one
   exactly when

   \[
   b\in\operatorname{colspan}_{\mathbb F_2}(M).
   \]

   Otherwise the kernel dimension is unchanged. In particular, if $b$ is one
   on any new-only row, then no immediate square dependency is created.

4. The sufficient arithmetic witness for a new-only row is a fully refined
   nonsquare block whose exponent in $gw$ is odd and whose old parity row is
   zero. A factor of $w$ coprime to all old blocks and of odd total
   multiplicity is a clean sufficient case, but not a necessary one.

5. If $g$ and its canonical inverse endpoint $w$ are canonical and
   $g^{-1}\equiv g\pmod N$, then $w=g$. The appended relation is $g^2$, its
   parity column is zero, and one indexed singleton kernel vector appears.
   This is useful for factoring only when $g$ is a non-global square root of
   one; direct $g-1$ and $g+1$ screens run before batch decoding.

6. For a sequence of indexed additions, let

   \[
   d_t=(\text{number of columns})-(\text{square-class rank}).
   \]

   Refinement alone preserves $d_t$. Each appended relation either raises rank
   and column count together, leaving $d_t$ fixed, or closes in the old span,
   leaving rank fixed and increasing $d_t$ by one. A block that is new-only at
   one step can recur later and then participate in a closure. If every new
   column has a private new-only nonsquare row at its time of insertion, no
   dependency ever appears.

## Representation and scope rules

- Equal relation values remain separate only when the algorithm actually
  appends separate indexed columns. If it deduplicates them, no new column and
  no one-dimensional increase occur.
- The theorem counts all exact square dependencies. Duplicate or square
  columns can add dependencies whose roots are globally trivial.
- `Factor base` is only an analogy for a square-class coordinate space. Blocks
  can be composite and can split later. No smoothness law, fixed prime factor
  base, or useful non-global root follows.
- The theorem is exact accounting, not a probability or runtime theorem. It
  does not supply a selector, a recurrence-time bound, or a factoring
  algorithm.

## Finite interpretation checks

- At $N=21$, the feedback relation $10\cdot19=190$ introduces a new-only
  block $19$, so the three relation columns stay independent even though the
  direct screen of $10-1$ factors $21$.
- At $N=55$, a selected self-inverse state $21$ gives
  $21^2=441=1+8\cdot55$, hence a zero parity column and an immediate singleton
  dependency, while the direct screens expose both factors.

Decide whether every claim holds, and supply a self-contained proof or a
counterexample. Do not infer a polynomial-time factoring algorithm.
