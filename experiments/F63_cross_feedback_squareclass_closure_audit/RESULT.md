# F63 hostile audit — cross-feedback square-class closure

**Candidate audited:**
`experiments/F63_cross_feedback_squareclass_closure/RESULT.md`

**Verified candidate SHA-256:**
`3097eab27e23e2ba4bd8fb544ac823a6fec63a16f026b48e52745ac0afde9f09`

**Verdict:** **PASS, with required representation and scope clarifications.**

I found no counterexample to the kernel-preservation claim, the independence
of pairwise-coprime nonsquare blocks, Theorem 1, the self-inverse case, or the
sequence accounting. The result is an exact linear-algebra statement.

Four interpretation rules are required:

1. Remove a perfect-square block only from the parity matrix. Retain the old
   relation values and their exact exponent data for later refinement and
   root construction.
2. A row is `new-only` when its parity is zero in every old column. A factor
   can occur to a positive even power in old integers and still be new-only
   in this square-class sense.
3. Kernel growth assumes that a new indexed column is appended. If equal
   relation values are deduplicated, no column was added and the claimed
   one-dimensional increase does not occur.
4. “Factor base” is exact only as a square-class vector-space analogy. The
   gcd-free blocks can be composite and can split later. The theorem proves
   neither conventional smoothness nor a useful non-global square root.

No mathematical search or research computation was run. The checks below
are symbolic.

## 1. Pairwise-coprime nonsquare blocks are independent — PASS

Let the retained blocks be pairwise coprime positive nonsquares

\[
q_1,\ldots,q_r.
\]

Take a nonzero vector `c` over `F_2`, and choose an index `j` with `c_j=1`.
Because `q_j` is not a square, some prime has odd valuation in `q_j`.
Pairwise coprimality means that this prime divides no other `q_k`. Its
valuation in

\[
\prod_k q_k^{c_k}
\]

is therefore odd. The product is not a rational square. Thus the map from
block-parity vectors to positive rational square classes is injective.

This proof does not require a block to be prime or squarefree. Composite
blocks and prime powers cause no problem. It proves exactly

\[
Mc=0
\quad\Longleftrightarrow\quad
\prod_i B_i^{c_i}\text{ is a square}.
\]

## 2. Perfect-square composite blocks — PASS with a storage guardrail

A perfect-square block has zero square class for every outer exponent, so it
may be omitted from the parity rows. This remains true when the block is
composite.

It must not be forgotten as arithmetic data. For example, suppose an old
relation value is `36`, represented initially by the single square block
`36`. If a later value `6` is added, complete refinement can represent the
two columns with the nonsquare block `6` and exact exponents `2` and `1`.
Their parity columns are `0` and `1`. The old singleton square relation is
preserved, and the new column is independent.

If deleting the parity row also deleted the value `36` and its exponent
information, the later refinement would no longer be exact. F63 is correct
when “remove” means omit from `M`, or when every refinement is recomputed
from all retained integer values. It is not a license to discard the exact
integer presentation.

## 3. Splitting old blocks preserves the old kernel — PASS

The property tested by an old kernel vector is intrinsic:

\[
c\in\ker M
\quad\Longleftrightarrow\quad
\prod_{i=1}^m B_i^{c_i}\text{ is a square}.
\]

A complete refinement changes only the exact coordinates used to express
the same integers. Since the square test is exact before and after the
change, the set of old vectors `c` that pass it is unchanged. Hence both the
old nullity and old rank are preserved.

The high-risk even-exponent case also passes. Let an old nonsquare block be
`12`. Adding the value `6` can refine the basis to `2,3`. The old value `12`
has refined parity `(0,1)`, while `6` has parity `(1,1)`. The old kernel did
not change. The row for `2` is zero on the old column even though `2`
arithmetically divides the old value. It is a new-only *parity* row.

This example also shows why “old-supported” must mean that some old matrix
entry is `1`, not merely that the integer block divides an old value.

## 4. Repeated powers and equal relations — PASS with indexed-column scope

Exact exponents reduce modulo two in the matrix, as required. A factor
`q^(2a)` contributes zero parity; `q^(2a+1)` contributes the same row as
`q`. Refinement and rank-nullity therefore handle arbitrary repeated powers.

A perfect-square relation value gives a zero column and hence a singleton
kernel vector. Two indexed copies of the same nonsquare value give equal
columns and hence a two-column kernel vector. Both are algebraically correct.

They need not provide new factoring information. For example, two copies of
the same value give a square whose positive root is that value, which is
`1 mod N` for these relation values. Also, a decoder that deduplicates equal
values does not append the second column. Its nullity does not grow. Theorem
1 must therefore be read as a theorem about an indexed relation list, not
about the set of distinct integer values.

## 5. The new-only row criterion — PASS

After refinement, let a new-only row mean exactly

\[
M_{j,*}=0.
\]

If `b_j=1`, every vector in the old column span has coordinate zero at `j`,
while `b` has coordinate one. Thus `b` is outside the old span. Appending it
raises rank and column count by one, so nullity is unchanged. Conversely,
kernel dimension rises exactly when `b` is in the old column span. This is
plain rank-nullity and has no omitted arithmetic case.

The candidate correctly says that the absence of a new-only row is only
necessary for closure. Old support in each coordinate does not imply that an
arbitrary vector lies in the span of the old columns.

The feedback interpretation needs one wording restriction. The sufficient
witness is a **fully refined nonsquare block** whose total exponent in the
new relation is odd and whose old parity row is zero. An arbitrary named
factor of `w` is not enough: it can overlap another named factor, or its
total prime valuation in `w` can be even. Coprimality with all old blocks is
a clean sufficient way to obtain such a row, but it is not necessary.

## 6. Self-inverse selected states — PASS with a usefulness distinction

If `g` and `w` are canonical representatives and

\[
g^{-1}\equiv g\pmod N,
\]

uniqueness of the canonical inverse gives `w=g`. Hence the appended value is
`g^2`, its square-class column is zero, and the new coordinate vector by
itself lies in the kernel.

This proves the stated one-dimensional increase when an indexed column is
actually appended. It does not say that every self-inverse state factors
`N`. Global roots give only the trivial screens. The useful case is the
non-global self-inverse state named in Section 5 of the candidate. Direct
`g-1` and `g+1` screens should run before insertion because any available
factor then belongs to the selector, not to later batch closure.

## 7. Sequence accounting and later recurrence — PASS

At each time, complete refinement leaves the old kernel unchanged. Appending
one column can raise rank by only zero or one. Therefore

\[
d_t=(\text{columns})-(\text{rank})
\]

either stays fixed for a new square-class direction or increases by exactly
one for a closure. There is no third outcome.

A block that is new-only at one step can recur later. In square-class
notation, columns with successive classes

\[
\alpha,\quad \beta,\quad \alpha+\beta
\]

show the exact behavior. The first two additions are independent. The third
contains no fresh direction and closes the relation among all three. Thus a
block's first appearance gives no permanent protection. F63 states this
limit correctly.

The stronger sequence sentence is also correct: if **every** added column
has a row that was zero on all earlier columns and is one on that column,
then every addition raises rank and column count together. Later recurrence
does not alter the already-accounted rank. A closure can occur only at a
later step that lacks such a fresh row.

Again, `d_t` counts all square dependencies. It does not count useful
non-global root images. Duplicate or perfect-square columns can increase
`d_t` while adding no factoring power.

## 8. Factor-base and smoothness language — algebraic PASS, algorithmic caution

The condition

\[
b\in\operatorname{colspan}(M)
\]

is exactly the same linear-algebra event as a new relation closing against
previous exponent-parity vectors. In that narrow sense the factor-base
analogy is valid.

The surrounding arithmetic is different from a conventional fixed prime
factor base:

- a gcd-free block can be composite;
- a later input can split an old block;
- “new-only” means a new parity coordinate, not a newly discovered prime;
- support on old coordinates does not itself imply closure; and
- closure supplies a square relation, not necessarily a non-global root.

Therefore “enlarged the factor base” and “exact analogue” should be read as
square-class coordinate language only. They do not establish smoothness
probabilities, a fixed-base sampling law, or a bound on closure time. The
candidate's final paragraph already rejects those algorithmic conclusions,
so this is a terminology correction rather than a theorem failure.

## 9. Final verdict

The mathematical core passes hostile audit. Complete exact refinement
preserves the old kernel; pairwise-coprime nonsquare composite blocks are
independent; a nonzero new-only parity row prevents immediate closure; a
self-inverse appended state gives a zero column; and the sequential nullity
accounting is exact.

The candidate should make the four opening interpretation rules explicit.
They separate exact square-class accounting from storage loss, column
deduplication, useful-root detection, and conventional factor-base
smoothness. None changes Theorem 1.
