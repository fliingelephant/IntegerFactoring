# F103 proof-blind reconstruction report

## Result

**PASS.** The universal frozen-batch theorem is valid. All stated fixed-input
claims for `N = 202537109` were reproduced from the public input and the one
allowed public source.

The executable did not use a factorization routine, primality test, target
residue, selected dependency, root, or factor as input. The root and divisors
below are outputs of an ascending public-kernel scan.

## Audit scope

- Read `RECONSTRUCTION_STATEMENT.md`.
- Read only the allowed external source
  `../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py`.
- Verified the allowed source SHA-256 as
  `5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b`.
- Did not read another F98 or F103 source, output, candidate, or audit artifact.
- Created only the proof-blind reconstruction artifacts named in the manifest.
- Preserved failed reconstruction attempts.

The fixed replay covers one input. The theorem covers every frozen finite
batch that satisfies the statement's endpoint and mask conditions.

## General factor-free theorem

Let the batch have `m` columns. Treat each mask as a vector in
`F_2^m`. For a prime `p`, define its hidden row by

```text
h_p = xor over entries (x,s) of ((v_p(x) mod 2) times s).
```

### Refinement invariant and termination

Take two entries `(x,s)` and `(y,t)`. Let `d = gcd(x,y)`. Put
`a = v_p(x)`, `b = v_p(y)`, and `c = v_p(d) = min(a,b)`. The old
contribution to `h_p` is

```text
(a mod 2)s xor (b mod 2)t.
```

The three replacement entries contribute

```text
(c mod 2)(s xor t)
xor ((a-c) mod 2)s
xor ((b-c) mod 2)t.
```

This expression is the old contribution. Thus every hidden prime row is an
invariant. Entries of value one and entries with zero mask contribute zero,
so discarding them is valid.

The process terminates. Let `Omega(x)` count prime factors with
multiplicity. A refinement has `d > 1`. Before refinement, the two selected
entries contribute `Omega(x) + Omega(y)` to the sum over active entries. If
the `d` entry remains, the three new values contribute

```text
Omega(x) + Omega(y) - Omega(d).
```

Discarding an entry only decreases this value more. Therefore each step
strictly decreases a nonnegative integer.

### Exact terminal row set

At termination, each prime divides at most one remaining block. If `p`
divides block `(b,s)`, its hidden row is either zero or `s`. It is `s`
exactly when `v_p(b)` is odd.

A block is nonsquare exactly when at least one of its prime valuations is
odd. Therefore:

- Every nonsquare block mask occurs as a nonzero hidden prime row.
- Every nonzero hidden prime row occurs as a nonsquare block mask.

The sets of distinct nonzero public and hidden rows are equal. Their
multiplicities can differ.

Duplicate rows and zero rows do not change a row span. The public and hidden
matrices therefore have the same rank and kernel. They also have the same
row supports. Thus they have the same degree-one core columns and the same
column-incidence components.

### Degree-one peeling

Suppose an active row contains only active column `c`. Every active kernel
vector has coordinate `c = 0`. Deleting `c` therefore gives a kernel
isomorphism. The inverse map extends a new kernel vector with zero at `c`.
This proves that each deletion is lossless.

Call a column set stable when every row meets it in zero or at least two
columns. Let `T` be any stable subset of the current active set `S`. If a
row makes `c` the next deletion from `S`, that row meets `S` only in `c`.
It cannot contain `c` in `T`, because that would make its degree in `T`
equal to one. Therefore every stable set survives as a subset through every
deletion.

An exhaustive terminal set is itself stable and contains every stable set.
It is the unique greatest stable set. Hence every exhaustive deletion order
has the same final columns.

This result is for a frozen batch. It is not safe as a permanent streaming
deletion rule. For example, the prefix row `[1]` deletes its only column.
Adding a later column to the same row gives `[1 1]`, whose kernel contains
`(1,1)`. Permanent prefix deletion would lose that dependency.

## Fixed public replay

The reconstruction reproduced the public generator control flow. It used
`n = 28` and `B = n^2 = 784`.

- All 783 trial gcd screens failed. Every result was one.
- All 25,098 executed direct sign screens failed.
- The generator made 42,417 candidate attempts.
- It retained 12,549 raw relations.
- Deduplication removed one value-one relation and 3,134 repeated exact
  relation values.
- It retained 9,414 distinct nontrivial values.
- The reconstructed raw-stream SHA-256 is
  `84571c6bc1949b9e9711bb3bd9e15da2b667b0f884b338b6b5ce90f4b15ca76b`.

The table gives the independently computed matrix results.

| Metric | Full batch | Frozen prefix |
|---|---:|---:|
| Distinct values | 9,414 | 4,293 |
| Public rows | 11,015 | 5,607 |
| Rank | 8,926 | 4,291 |
| Nullity | 488 | 2 |
| Initial degree-one rows | 7,866 | 4,012 |
| Peeled columns | 7,633 | 3,920 |
| Core columns | 1,781 | 373 |
| Core rows | 1,298 | 387 |
| Core rank | 1,293 | 371 |
| Core nullity | 488 | 2 |
| Core component sizes | `[1781]` | `[373]` |

The prefix selects a distinct value exactly when its first zero-based raw
index is less than 5,616. Its distinct public row set also equals the full
public row set restricted to those prefix columns.

The ordered core hash encoding is the ASCII decimal, zero-based,
distinct-value column indices joined by commas, with no trailing newline.

- Full core:
  `5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8`
- Prefix core:
  `9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df`

FIFO, LIFO, and descending batch schedules produced the same full core. Their
deletion-order hashes were distinct:

```text
FIFO              4e47078b7940b5f9853c4236c1ef1fc92a47c487e0f1e8d090a99b9f07887d9e
LIFO              4b9b36405a91434debeae861ec9198d20482c40df78ec812732eb623b6517bba
batch descending  7b97b7141a0b1e7a1ff72e6070efa02fb092f67f75336fced515d9d129a94d40
```

The three prefix deletion-order hashes were also distinct. They are in the
JSON output.

The full core provenance matched the statement:

- Three seed relations with values `2`, `11`, and `27`.
- 1,778 feedback relations.
- Eight active-pair families.
- 1,138 `u_power_times_v` records.
- 640 `u_times_v_power` records.

## Public useful certificate

The declared scan performs highest-column-pivot row elimination. It then
visits free columns in ascending order. It has no target input.

The core kernel dimension was 488. The first scanned basis dependency gave a
global `+1` root. The second gave the first useful dependency.

```text
support                       166
exact product is a square    yes
R mod N                       132013085
gcd(R - 1, N)                 19727
gcd(R + 1, N)                 10267
```

The two derived divisors multiply to `N`. The selected-column SHA-256 is
`bcdc7a7ad7ea44631ddcc98a99fe744aae060a4a09fbc231a015d1a82851b3c4`.
The generated indices are in the JSON output. None is hard-coded in the
program.

## Refutation checks and limits

The proof handles the cases most likely to break the claim:

- Unequal prime valuations in two gcd-overlapping entries.
- A zero mask created by `s xor t`.
- Composite terminal blocks with both even and odd prime valuations.
- Duplicate public masks and different row multiplicities.
- Different sequential and batched peel schedules.
- Restricting the full row set to a frozen prefix.
- A global root before the useful kernel dependency.

No counterexample was found. The result does not say that every composite
input has a nonempty core, a rank defect, or a non-global square root. Core
connectedness does not imply usefulness. The replay gives no density bound
for useful dependencies. Online deletion is unsafe. This is not an all-input
factoring algorithm.
