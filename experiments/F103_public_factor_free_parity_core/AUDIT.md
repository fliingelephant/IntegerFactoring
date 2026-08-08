# F103 hostile audit

## Verdict: PASS

The candidate claims in `DESIGN.md`, `RESULT.md`, `RUN_MANIFEST.md`,
`public_core_replay.py`, `OUTPUT.json`, and `RUN.log` survive independent
replay and hostile scope review.

The candidate artifacts were not edited. The independent verifier does not
import the candidate or the pinned F98 module. It locally regenerates the
relation stream, reconstructs the seed gcd basis, runs the P66 refinement,
computes rank and kernel data, peels the matrix, checks connectedness, and
verifies the exact root certificate.

The authoritative audit completed 122 strict checks with no failures. It ran
for 67.84 seconds under a hard 240-second timeout and exited with code zero.

## Independent artifacts

- `AUDIT_VERIFY.py`: independent verifier.
- `AUDIT_RUNNER.py`: named hard-timeout runner.
- `AUDIT_OUTPUT.json`: structured PASS result.
- `AUDIT_RUN.log`: command, timeout, progress, exit code, and output.
- `AUDIT_MANIFEST.md`: input and audit hashes.

The first audit attempt failed because the independent FIFO seed refinement
did not discard a quotient equal to one. The runner preserved that failure as
`AUDIT_FAILED_20260808T092223.json` and
`AUDIT_FAILED_20260808T092223.log`. It was an audit implementation failure,
not a candidate failure. The corrected authoritative run starts again from
the public input and passes.

## Replayed fixed-input evidence

| Claim | Independent result |
|---|---:|
| `N`, `n`, `B` | 202,537,109; 28; 784 |
| Trial-screen proper gcds | 0 |
| Canonical-inverse direct sign factors | 0 |
| Active seed pairs | 27, exact list match |
| Retained raw relations | 12,549 |
| Removed `P = 1` values | 1 |
| Removed repeated exact values | 3,134 |
| Distinct nontrivial values | 9,414 |
| Public P66 rows | 11,015 |
| P66 square blocks omitted | 0 |
| Full rank; nullity | 8,926; 488 |
| Initial degree-one rows | 7,866 |
| Peeled columns | 7,633 |
| Core columns; rows | 1,781; 1,298 |
| Core rank; nullity | 1,293; 488 |
| Core components | one component of 1,781 columns |
| Full P66 refinements | 62,643 |
| Full P66 gcd tests | 814,589,842 |

The independent full-core hash is

```text
5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8
```

It equals both the F103 candidate hash and the F102 factor-assisted
prime-matrix hash.

The independent prefix selects distinct values whose first raw index is less
than 5,616. This is exactly the first 5,616 raw records. It finds:

| Prefix claim | Independent result |
|---|---:|
| Distinct values | 4,293 |
| Public P66 rows | 5,607 |
| Rank; nullity | 4,291; 2 |
| Initial degree-one rows | 4,012 |
| Peeled columns | 3,920 |
| Core columns; rows | 373; 387 |
| Core rank; nullity | 371; 2 |
| Core components | one component of 373 columns |
| Prefix P66 refinements | 27,865 |
| Prefix P66 gcd tests | 193,286,162 |

The prefix core hash is

```text
9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df
```

It also equals the F102 prime-matrix hash.

## P66 construction and kernel correctness

An initial endpoint entry is `(x,s)`, where `x` is its positive integer value
and `s` is its relation-column bit mask. For two overlapping entries `(x,s)`
and `(y,t)`, put `d = gcd(x,y)`. P66 replaces them by the nontrivial entries

```text
(d, s xor t), (x/d, s), (y/d, t).
```

An entry with value one or zero mask is discarded. This is exact parity
bookkeeping. For every hidden prime `p`, the coefficient of `s` after the
split is

```text
v_p(d) + v_p(x/d) = v_p(x)  modulo 2,
```

and the coefficient of `t` is similarly unchanged. Repeated splits therefore
preserve every prime-parity row without factoring.

At termination the stable integer blocks are pairwise coprime. A square block
has only even prime valuations, so it contributes no parity row. A nonsquare
block has at least one odd prime valuation, so its stable mask is a necessary
parity row. Thus the public nonsquare-block matrix has exactly the same square
kernel as the hidden prime-parity matrix.

The verifier independently checks pairwise coprimality, computes rank with a
lowest-pivot GF(2) elimination, and confirms rank-nullity. It does not accept
the candidate rank or kernel as input.

## Degree-one peeling and order independence

If a row has one active column `j`, every kernel vector has coefficient zero
at `j`. Deleting `j` therefore preserves the complete kernel after a zero
coordinate is restored. Repeating this step preserves rank defect and
nullity.

The final column set is independent of deletion order. Let `T` be the terminal
set from one exhaustive schedule. Consider another schedule in deletion order.
Assume every earlier deletion is absent from `T`. If its next column `j` is
the sole active column of a row, then `T` is a subset of that active set. If
`j` belonged to `T`, the same row would have degree one in `T`, contradicting
terminality. Thus `j` is also absent from `T`. Induction, followed by the
symmetric argument, proves that all exhaustive schedules have the same core.

The audit verifies the theorem computationally with three materially different
schedules: simultaneous fixed-point deletion, smallest-row-first sequential
deletion, and largest-row-first sequential deletion. All three return the
same full and prefix column sets. The full simultaneous peel takes nine
rounds. The prefix peel takes eleven rounds.

This theorem applies only after the batch is frozen. It does not justify
online deletion. A future relation can reuse a row which is degree one in the
current prefix. The candidate states this limitation correctly.

## Strengthening: exact distinct-row equivalence

The proposed strengthening is **valid**, with a row-multiplicity caveat.

For a hidden prime `p`, define its row as the xor of each entry mask weighted
by `v_p(entry) modulo 2`. The split calculation above proves that this row is
invariant through every gcd refinement.

At pairwise-coprime termination, a prime occurs in at most one stable block
`b` with mask `m`. Its hidden row is therefore either zero or `m`, according
to whether `v_p(b)` is even or odd.

- Every nonzero hidden prime row is the mask of a nonsquare stable block.
- Every nonsquare stable block has a prime of odd valuation, so its mask is a
  nonzero hidden prime row.

Therefore the set of distinct nonzero hidden prime rows equals the set of
distinct public nonsquare-block rows for every explicit finite batch. The
multisets need not agree. Several primes in one block can repeat a hidden row,
and several coprime public blocks can carry the same mask.

Duplicate rows do not change rank, kernel, degree-one forcing, core columns,
or column connectivity. The public and hidden-prime matrices consequently
have identical core columns and column components for the same frozen batch.
Their raw and core row counts can differ. F102 and F103 show this difference:

```text
full prime/public rows       = 11034 / 11015
full prime/public core rows  = 1299 / 1298
prefix prime/public rows     = 5658 / 5607
```

This general equivalence does not imply that a core is nonempty, rank
deficient, useful, or obtainable safely by online deletion. It assumes the
same explicit endpoint batch, GF(2) masks, exact gcd splitting, and terminal
pairwise-coprime blocks.

## Connectedness and provenance

The audit builds the column incidence graph independently with union-find.
Two columns are adjacent when they occur in a common nonzero parity row. The
full core has one component of size 1,781. The prefix core has one component
of size 373.

The full provenance matches both F103 and F102:

```text
initial seeds          = 3
feedback trajectories = 1778
trajectory families   = 8
u_power_times_v        = 1138
u_times_v_power        = 640
```

The three seed columns are seeds 2, 11, and 27. The exact eight family counts
in `AUDIT_OUTPUT.json` match both stored outputs.

## Useful certificate

The 166 selected zero-based columns in F103 equal the F102 list exactly. The
independent verifier confirms all of the following:

- All 166 indices are distinct and lie in the full public core.
- Their xor has zero incidence in every public row.
- Their exact relation-value product is a positive square.
- The kernel basis reconstructed with the pinned F98 pivot policy encounters
  one global `+1` root first and then this vector as basis vector 2.

The exact root evidence is:

```text
support                 = 166
exact-root digits       = 1292
exact-root SHA-256      = 43f3b0c6c08821a6fc221521783538bebbebcc4b3d623c7f2b6fd0888065bbfa
R mod N                 = 132013085
gcd(R - 1, N)           = 19727
gcd(R + 1, N)           = 10267
```

The certificate is checked only after the matrix is built. Its indices,
residue, and factors are not inputs to the public replay.

## Provenance and forbidden-operation audit

Every SHA-256 entry in the candidate `RUN_MANIFEST.md` matches its file. In
particular, the dynamically imported F98 source has hash

```text
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b
```

The hash embedded in F103 `OUTPUT.json` matches it.

The F103 source imports the pinned module only for five generic arithmetic
operations: seed gcd refinement, relation-column construction, P66 parity
refinement, binary kernel construction, and the initial batch decode. The
pinned module has no modulus, factors, target residue, selected vector,
relation table, or external-data read at module scope. Its main routine is
guarded and does not run on import.

Full source inspection and an AST allowlist find no factorization, primality,
order, discrete-logarithm, Sage, network, subprocess, or target-selection call
in either public source. The candidate source contains one integer literal at
least 1,000: the declared diagnostic prefix 5,616. The pinned F98 source
contains none. Neither public source reads F102.

The public arithmetic uses gcds, exact integer roots, modular inversion,
modular multiplication, bit operations, and exact products. The final root
and gcd scan is part of the declared public decoder; it is not a hidden
factorization call.

The phrase “received only N” is operationally correct but does not mean the
program is one self-contained file. F103 depends on the pinned, hashed F98
source, and its diagnostic prefix 5,616 is fixed in code. Neither dependency
contains nonpublic arithmetic data or selects the useful certificate.

## Complexity and scope

For an explicit batch with `m` endpoint entries of at most `L` bits, define
the refinement potential as the sum of `log2(value)` over all work and stable
entries. One nontrivial split replaces `x,y` by `d,x/d,y/d`, so the potential
drops by `log2(d)`, at least one. The initial potential is at most `mL`.
There are therefore at most `O(mL)` refinements. There are at most `O(mL)`
live/generated entries and stable blocks, so the unoptimized stable-list
implementation makes at most `O((mL)^2)` gcd comparisons. The remaining
bitset rank, kernel, and peeling work is also polynomial in the explicit
matrix size.

For the bounded F98 collector, there are `O(n^3)` candidate trajectory
positions and `O(n)`-bit endpoints. The whole declared replay therefore has
polynomial bit complexity. The 814 million observed gcd tests show that the
implementation is unoptimized; they do not make it superpolynomial.

What remains unproved is success, not computability. The finite replay does
not prove that every composite input yields a nonempty or rank-deficient core
within the bounded collector, or that a dependency gives a non-global root.
It gives no all-input factoring algorithm, density theorem, or online
collector theorem. The candidate's stated scope respects these limits.
