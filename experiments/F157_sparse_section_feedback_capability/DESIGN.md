# F157-D01 design

## Fixed inputs and source semantics

`INPUT.json` contains one F111 input and the four registered F118 inputs.
The source order is fixed by the pinned upstream programs.

For the F111 input, seed records build the frozen seed-pair basis. The base
ledger then contains the first occurrence of each nonunit exact value from
the frozen trajectories. This is the exact frozen-ledger convention of the
pinned F111 factor-free reconstruction.

For an F118 input, canonical-residue deduplication starts at the seed layer.
The base ledger contains the first occurrence of each nonunit exact value
among all retained seed and frozen records. The pinned F118 decoder kept
duplicate exact values as separate columns. Removing them adds only global
`+1` dependencies. It leaves the rank and normalized-root image unchanged.

Both modes run every old residue and endpoint sign gcd. No old proper screen
is allowed.

## Public factor-free construction

For each distinct exact value `A = c*w`, refine the labelled exact values by
gcd only. This is the exact-value construction used by the pinned F111
factor-free reconstruction. It has the same prime-parity rows as refining
the two endpoints with one common column label. The refinement is
multiplicity-aware. If two entries overlap by `d`, it
replaces them by labelled copies of `d`, `x/d`, and `y/d`. Equal labels cancel
modulo two. Exact square entries cancel. Exact odd perfect powers are replaced
by their exact root. A product/remainder tree locates overlaps in batches.

The terminal positive blocks are pairwise coprime nonsquares. Their label
sets are the complete public parity rows. For column `i`, let `Q_i` be the
product of all terminal blocks whose row contains `i`. The program verifies

```text
A_i = t_i^2 * Q_i
```

exactly. Its actual decorated lift is `(v_i,z_i)`, where `v_i` is the set of
these blocks and `z_i = t_i^(-1) mod N`.

The program runs an online decorated-group decoder. This independently checks
the old rank and confirms that every old dependency root is global.

The product/remainder tree uses GMP integers from the Sage runtime. This
keeps the registered 58-bit batches within memory. GMP supplies only exact
integer arithmetic here; the public refinement still uses no
integer-factorization routine.

The program retains `c,w` as the public endpoint presentation of each exact
value. It does not factor either endpoint or `A`.

## F156 candidates

The program selects independent base records in first-occurrence order. It
retains each selected record's actual lift.

For support one, it tests every selected lift directly.

For support two, let `C_ij` be the product of public terminal blocks common
to `v_i` and `v_j`. The public star-product is

```text
v_ij = v_i xor v_j
z_ij = z_i*z_j/C_ij mod N.
```

It tests `gcd(z_ij-w_ij,N)` and `gcd(z_ij+w_ij,N)`, where `w_ij` is the
canonical inverse of `z_ij`.

Enumerating all pairs is unnecessary for discovery. For each disclosed prime
factor `r` and sign `epsilon` in `{+1,-1}`, a pair can hit only if

```text
Q_j = epsilon*C_ij^2/Q_i mod r.
```

The program hashes the joint pair `(Q_j mod p,Q_j mod q)`. It calls a block
light if it occurs
in 2 through 256 basis records. It calls a block heavy if it occurs in more
than 256 basis records.

Pairs with a common light block are enumerated once. Their owner is their
least common light block. For all remaining pairs, the common blocks are
heavy. For each `i`, the program enumerates every subset of its heavy blocks,
uses that subset as `C`, and retrieves the matching `j` values from the hash
index. It then checks the exact heavy intersection and checks that there is
no common light block.

These two disjoint cases cover every pair. For each sign, the joint index
keeps a candidate exactly when the target congruence holds modulo one factor
but not the other. This removes the much larger set for which the same sign
holds modulo both factors; those pairs give only an improper gcd. The program
deduplicates the located candidates.

The factors affect only this index. Every retained hit is rebuilt with the
public star law and verified with direct gcds. The program fails if the index
retains a pair without a proper public gcd. The reported null count is the
full number of unordered basis pairs minus the number of publicly verified
proper-hit pairs.

## Resource boundary

The named timeout is `F157_SPARSE_SECTION_FEEDBACK_CAPABILITY_HARD_TIMEOUT`.
It is 900 seconds. The runner preserves every failed attempt. It does not
change the source, inputs, or corpus after launch.
