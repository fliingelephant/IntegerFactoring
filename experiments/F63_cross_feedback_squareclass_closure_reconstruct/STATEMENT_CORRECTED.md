# Corrected proof-blind statement — square-class closure under feedback

Reconstruct or refute every claim below. Work from this file only. Do not read
the candidate proof, any audit, the failed first reconstruction, `PROVED.md`,
`FAILED.md`, or `notes/Progress.md`.

## Setup

Assume $N$ is odd. An all-input use removes factor $2$ first. Let
$B_1,\ldots,B_m$ be indexed positive integer relation values, all coprime to
$N$. Apply complete gcd-free refinement and represent their exact square
classes by a matrix $M\in\mathbb F_2^{r\times m}$ on pairwise-coprime
nonsquare blocks. Omit perfect-square blocks from the parity matrix only;
retain the exact integers and exponent data for later refinement and root
construction.

Append one indexed feedback relation $B_{m+1}=gw$. Refine all old and new
values together. This can split old blocks. Call the refined old matrix again
$M$, and let $b$ be the new parity column. A row is `new-only` when it is zero
in every old column. This is a parity condition: the integer block can occur
to a positive even power in old values.

## Claims

1. Positive pairwise-coprime nonsquare blocks have independent rational square
   classes. Therefore $\ker M$ is exactly the indexed square-relation space,
   including when blocks are composite or prime powers.

2. Complete exact gcd-free refinement preserves the old column kernel because
   it only changes exact coordinates for the same old integers.

3. Appending the indexed column $b$ increases nullity by one exactly when

   \[
   b\in\operatorname{colspan}_{\mathbb F_2}(M).
   \]

   Otherwise nullity is unchanged. If $b$ is one on any new-only row, no
   immediate new dependency appears.

4. A sufficient arithmetic witness is a fully refined nonsquare block whose
   total exponent in $gw$ is odd and whose old parity row is zero. In
   particular, a nonzero square-class component of $w$ that is coprime to all
   old blocks and has odd total multiplicity in $gw$ supplies such a row. This
   condition is not necessary.

5. If $g$ and its canonical inverse endpoint $w$ are canonical and
   $g^{-1}\equiv g\pmod N$, then $w=g$. Appending $g^2$ creates a zero parity
   column and one indexed singleton dependency. For odd $N$, the two direct
   screens are proper exactly when $g$ is a non-global square root of one.
   Run them before batch decoding.

6. For a sequence of indexed additions, put

   \[
   d_t=(\text{number of columns})-(\text{square-class rank}).
   \]

   Refinement alone preserves $d_t$. Each appended column either raises rank
   and column count together, leaving $d_t$ fixed, or closes in the current
   span, leaving rank fixed and increasing $d_t$ by one. If every appended
   column has a private new-only nonsquare row at its insertion time, then
   $d_t=d_0$ for every finite prefix. Thus no *new* dependency appears; if
   $d_0=0$, no dependency exists at all.

## Representation and scope

- Equal relation values count separately only when the algorithm appends
  separate indexed columns. Deduplication appends no column.
- The theorem counts all exact square dependencies. A duplicate or square
  column can add a dependency with only a global root.
- `Factor base` is only a square-class analogy. Blocks can be composite and
  can split later. No smoothness law or fixed prime factor base follows.
- A block that is new-only now can recur later and participate in a closure.
- This is exact accounting, not a probability, selector, runtime, or factoring
  theorem.

## Finite checks

- At $N=21$, the old values $22=2\cdot11$ and $85=5\cdot17$ have independent
  square classes. Appending $190=10\cdot19$ introduces the private block $19$,
  so all three columns remain independent, although
  $\gcd(10-1,21)=3$ already factors the input.
- At $N=55$, the old square classes of $56=2^3\cdot7$ and
  $111=3\cdot37$ are independent. The selected self-inverse state $21$ gives
  $21^2=441=1+8\cdot55$, a zero parity column, one new dependency, and direct
  factors $5$ and $11$.

Give a self-contained proof or counterexample with a clear PASS/FAIL verdict.
