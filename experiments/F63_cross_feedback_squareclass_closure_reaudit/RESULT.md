# F63 corrected square-class closure — hostile re-audit

**Candidate SHA-256:** `210198cdbc8d15a67fe84577d80a41e8d501f6df23f80ed612989ebf322405ea`

**Verdict: PASS.**

This was a proof-only audit. I used no computational search and no prior audit
or reconstruction as evidence. I found no counterexample to the corrected
claims.

## 1. Composite gcd-free blocks are independent

Let $q_1,\ldots,q_r$ be positive, pairwise-coprime, nonsquare integers. For
each $q_j$, choose a prime $p_j$ whose valuation in $q_j$ is odd. The
pairwise-coprimality condition gives

\[
v_{p_j}(q_k)=0\qquad(k\ne j).
\]

For $c_j\in\mathbb F_2$, the parity of the $p_j$-valuation of
$\prod_kq_k^{c_k}$ is therefore $c_j$. If the product is a rational
square, this parity is zero for every $j$, so every $c_j=0$. The converse
is immediate. This proof does not require the blocks to be prime or
squarefree. Thus the parity matrix represents the exact square-relation
space, and its kernel is exactly the set of indexed square subproducts.

Perfect-square blocks have zero class and can be omitted. Retaining their
integer exponents separately is sufficient for later exact roots.

## 2. Exact refinement preserves the old kernel

Refinement changes coordinates, not any old relation value. More explicitly,
when an old nonsquare block $q$ is split into pairwise-coprime refined
blocks, every refined parity row on the old columns is either zero or the old
$q$-row. At least one is the old row, because $q$ is not a square. Factors
coming from different old blocks have disjoint prime support. A split of an
omitted square block produces only zero old parity rows.

Consequently, for every old coefficient vector $c$,

\[
M_{\rm old}c=0
\quad\Longleftrightarrow\quad
\prod_i B_i^{c_i}\text{ is a square}
\quad\Longleftrightarrow\quad
M_{\rm refined}c=0.
\]

Hence complete refinement, including refinement caused by the feedback
value, preserves the old column kernel exactly.

## 3. One-step rank and indexed-column semantics

For the appended indexed column $b$, rank can increase only by zero or one.
It increases by zero exactly when $b\in\operatorname{colspan}(M)$. Since the
column count always increases by one under indexed append, nullity increases
by one in that case and otherwise stays fixed. This proves Theorem 1.

If a refined row is zero on every old column and is one in $b$, its row
functional vanishes on the old span but not on $b$. Thus $b$ cannot be in
the span. The definition correctly uses parity: the underlying integer block
may already occur in old values, but only to even powers.

Equal integer relation values give equal parity columns. If the new indexed
copy is retained, it therefore creates the dependency consisting of the old
and new copies. If an implementation deduplicates the value before append,
neither the column count nor nullity changes. The candidate states this
distinction correctly. The singleton vector occurs in the separate zero-column
case.

## 4. Total multiplicity in $gw$

For every fully refined block $r$, the new coordinate is

\[
b_r=v_r(g)+v_r(w)\pmod 2.
\]

It is this total multiplicity, not an occurrence in $w$ alone, that must be
odd. The candidate uses the total exponent in $gw$. Its stated sufficient
condition is also sound: if a nonzero square-class component of $w$ is
coprime to every old block, then it is coprime to $g$, because $g$ is
assembled from those blocks. Its odd parity cannot cancel against $g$, and
its old row is zero. It therefore supplies a new-only row with $b_r=1$.

Absence of such a row is only necessary for closure. For example, an old
matrix with sole column $(1,1)^T$ and a new column $(1,0)^T$ has no
new-only row but the new column is outside the old span. This confirms the
candidate's warning that the condition is not sufficient.

## 5. Self-inverse states and direct screens

Canonical representatives of the same residue are equal. Thus
$g^{-1}\equiv g\pmod N$ gives $w=g$, and the appended value is $g^2$.
Its column is zero, so indexed append creates the singleton kernel vector
$e_{m+1}$.

Also $g^2\equiv1\pmod N$. For every odd prime power $p^a\mid N$, the
prime $p$ cannot divide both $g-1$ and $g+1$. Hence the whole prime
power $p^a$ belongs to exactly one of

\[
\gcd(g-1,N),\qquad \gcd(g+1,N).
\]

If $g\equiv1\pmod N$ or $g\equiv-1\pmod N$, the two screens are trivial.
If $g$ is neither global root, at least one prime-power component has each
sign, so both gcds are nontrivial and proper. This remains true when $N$ is
not squarefree. The odd-$N$ hypothesis is exactly what excludes the shared
factor $2$ obstruction. The recommendation to run both direct screens
before batch decoding is therefore correct.

## 6. Sequence quantifiers

At step $t$, let $\delta_t\in\{0,1\}$ be the rank increase caused by the
new column after refining the preceding columns. Kernel preservation under
refinement and rank-nullity give

\[
d_t-d_{t-1}=1-\delta_t.
\]

A new-only row with odd new parity forces $\delta_t=1$. Therefore, if every
addition has such a row relative to all columns already present at that step,
then induction gives $d_t=d_0$ for every finite prefix. Later splitting or
recurrence of an earlier block does not invalidate an earlier step, because
refinement preserves the kernel. A later recurrence can increase nullity only
if that later column closes in the then-current span, as the candidate says.

If $d_0=0$, all collected columns remain independent, so no nonempty square
relation appears. If $d_0>0$, the initial kernel remains; only its dimension
does not grow. The candidate now makes precisely this distinction and does
not claim absolute independence in the latter case.

## 7. Stated witnesses

For $N=21$, in row order $2,5,11,17,19$, the three columns for
$22,85,190$ are

\[
(1,0,1,0,0)^T,
(0,1,0,1,0)^T,
(1,1,0,0,1)^T.
\]

The private $19$-row separates the third column, and the first two are
independent. Thus the three-column kernel is zero.

For $N=55$, the old values have square classes
$56=2^3\cdot7$ and $111=3\cdot37$, which are independent. The feedback
value is $21^2=3^2\cdot7^2$, so its column is zero and the kernel gains one
dimension. Moreover $21^2-1=8\cdot55$, while the two direct screens give
$\gcd(20,55)=5$ and $\gcd(22,55)=11$.

## 8. Scope

The result is an accounting theorem only. Closure can still yield a global
root, and an independent relation can become useful after a later recurrence.
The candidate does not claim otherwise, and it gives no frequency, runtime,
or all-input factoring conclusion. Within that stated scope, all audited
claims survive.
