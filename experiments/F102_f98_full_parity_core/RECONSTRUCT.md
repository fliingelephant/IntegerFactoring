# F102 independent reconstruction

## Clean-room scope

This reconstruction used only `RECONSTRUCTION_STATEMENT.md` and the permitted
`../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json`. The
public JSON has SHA-256
`ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab`,
as required. I did not read another pre-existing F102 file.

The factorization step below is a factor-assisted diagnosis. It is not a
public algorithm step.

## General theorem

Let `M[S]` be the binary matrix restricted to an active column set `S`. Keep
all rows. For a row `r`, let its active degree be the number of nonzero entries
in that row among `S`.

Suppose `r` has active degree one, and let `c` be its unique active column. If
`x` is in the kernel of `M[S]`, the equation in row `r` is `x_c = 0`. Thus,
restriction from `S` to `S \ {c}` maps the kernel of `M[S]` into the kernel of
`M[S \ {c}]`. Conversely, extend a kernel vector of `M[S \ {c}]` by setting
its coordinate at `c` to zero. Every old row equation is unchanged, and the
equation in row `r` is zero. Restriction and zero extension are inverse linear
maps. One deletion therefore preserves the complete kernel, not only its
dimension. Repeating this argument proves kernel preservation for the full
peeling sequence.

Call a column set `T` admissible when every row incident to `T` has degree at
least two inside `T`. Let `S` be any active set during peeling, and assume
`T` is a subset of `S`. If a degree-one row in `S` selects column `c`, then
`c` cannot be in `T`: otherwise that row is incident to `T` but has degree at
most one there. Therefore, peeling never deletes a column of `T`. By induction,
every admissible `T` is a subset of the final set `K`. At termination, every
row incident to `K` has degree at least two, so `K` is itself admissible. Hence
`K` is the unique greatest admissible set. The final columns are independent
of the peeling order. The zero-extension isomorphisms also make the preserved
kernel independent of that order.

This result applies to a frozen batch. A new streaming column can use a row
that currently has degree one. The enlarged row can then have degree two, and
a new kernel vector can use both the old and new columns. Peeling the old
column before the batch is frozen does not preserve the kernel of the future
matrix.

## Relation-stream reconstruction

The public values are `N = 202537109`, `n = 28`, and `B = 784`.

For each seed `c = 2,...,28`, I computed

```text
w = c^(-1) mod N
P = c*w.
```

I retained each active-pair family at its first occurrence. There are eight
families. For each family `(u,v)` and exponent `e = 1,...,784`, I generated the
two orientations in this order:

```text
u_power_times_v: c = u^e*v mod N
u_times_v_power: c = u*v^e mod N
w = c^(-1) mod N
P = c*w.
```

The F98 endpoint first-occurrence rule suppresses seed endpoints `2,...,28`
and later repeats of `c` inside one family. The two inverse-pair families share
the trajectory start `c = uv = 1`; the stream retains that common start once.
An identity reached later inside another trajectory remains a raw occurrence.

This gives 12,549 raw records, 9,415 distinct exact values including `P = 1`,
3,134 repeated occurrences, and 9,414 distinct nonidentity values. As a direct
stream check, all 166 certificate witnesses replay at their stated zero-based
raw indices with the same `P`, `c`, `w`, family, exponent, and orientation.

I discarded `P = 1`. I then retained the first raw occurrence of each exact
remaining `P`. I factored each retained value. I checked that every factor is
prime and that every factorization multiplies back to the exact value. A matrix
column contains one in precisely the rows whose primes have odd valuation.

## Finite results

Rank was computed over `GF(2)` by exact bit-vector elimination. Peeling used
two materially different schedules: a FIFO degree-one queue and a seeded,
shuffled LIFO queue. Their deletion sequences have different SHA-256 digests.
They produce the same final column sets in both runs. Every final incident row
has degree at least two. Full and core nullities are equal, as the theorem
requires.

| Quantity | Full pool | Prefix before raw index 5,616 |
|---|---:|---:|
| columns | 9,414 | 4,293 |
| rows | 11,034 | 5,658 |
| rank | 8,926 | 4,291 |
| nullity | 488 | 2 |
| initial degree-one rows | 7,884 | 4,062 |
| peeled columns | 7,633 | 3,920 |
| core columns | 1,781 | 373 |
| core rows | 1,299 | 387 |
| core rank | 1,293 | 371 |
| core nullity | 488 | 2 |
| core components | `[1781]` | `[373]` |

For each hash, the payload is the ascending zero-based core column indices,
joined by ASCII commas with no spaces and no trailing comma. The hashes are:

```text
full    5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8
prefix  9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df
```

All 166 pinned certificate columns are in the full core. The core contains
three seed columns, with seed values 2, 11, and 27, and 1,778 feedback columns.
Those feedback columns cover all eight active-pair families. Their orientation
counts are 1,138 `u_power_times_v` and 640 `u_times_v_power`.

The prefix has more rows than columns, but its column kernel has dimension two.
Thus a finite rank defect does not require a column surplus.

## Exact conclusion

**PASS:** The frozen F98 prime-parity matrix has the stated unique large core.
Zero extension preserves its complete kernel. The pinned useful certificate is
contained in that core. The stated prefix diagnosis also passes.

No result here says that the prime matrix is public. Connectedness does not by
itself imply a useful root. This reconstruction does not claim that every
composite input has a nonempty or rank-deficient core. It does not establish
inverse-polynomial density of useful circuits. It is not a factoring
algorithm.

## Reproducibility and failed attempts

The final bounded command is:

```text
DOT_SAGE=/tmp/f102_blind_sage timeout 300s sage -python blind_reconstruct_f102.py --timeout 240 --write-artifacts
```

The outer process timeout is 300 seconds. The source also installs a 240-second
`SIGALRM`. `BLIND_RECONSTRUCT_OUTPUT.json` preserves three failed stream
hypotheses and their observed failures. It also preserves the unsuccessful
hash-payload encodings. `BLIND_RECONSTRUCT_RUN.log` records the final run.
`BLIND_RECONSTRUCT_MANIFEST.json` records the command, runtime, paths, and
SHA-256 hashes.
