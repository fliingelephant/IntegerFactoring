# F103 proof-blind reconstruction statement

Reconstruct and verify the theorem and fixed-input replay below without
reading any other file in this F103 directory.

## Allowed public source

The only external artifact you may read is

```text
../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py
```

Its required SHA-256 is

```text
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b
```

The reconstruction receives only the public input

```text
N = 202537109
```

Do not read an F98 or F103 output file. Do not use a factorization routine,
the factors of N, a target residue, or a selected dependency as input.

## General factor-free theorem

An explicit finite relation batch has positive integer endpoint values and
one binary column mask for each relation. Starting from the endpoint entries
`(x,s)`, apply the P66 gcd refinement. For two entries `(x,s)` and `(y,t)`,
put `d = gcd(x,y)` and replace them by the nontrivial entries

```text
(d, s xor t), (x/d, s), (y/d, t).
```

Discard entries with integer value one or zero mask. Continue until the
remaining integer blocks are pairwise coprime. Use the masks of the
nonsquare blocks as public parity rows.

Prove that, for every frozen explicit batch, the set of distinct nonzero
public rows is exactly the set of distinct nonzero hidden prime-parity rows.
Row multiplicities can differ. Conclude that the public and hidden matrices
have the same rank, kernel, degree-one core columns, and column-incidence
components.

For any binary matrix, repeatedly choose an active row of degree one and
delete its unique active column. Prove that every deletion preserves the
kernel by zero extension. Prove that every exhaustive deletion order gives
the same final column set. State the frozen-batch limit: a later streaming
column can reuse a row that is private in the current prefix, so the theorem
does not justify permanent online deletion.

## Fixed public replay

From only N and the allowed public source, regenerate the exact public F98
relation stream. Verify that all direct sign screens fail. Remove the value
one and repeated exact relation values. Construct the P66 public matrix,
peel it with at least two materially different schedules, and reconstruct:

```text
retained raw relations       12549
distinct nontrivial values    9414
public rows                  11015
rank                          8926
nullity                        488
initial degree-one rows       7866
peeled columns                7633
core columns                  1781
core rows                     1298
core rank                     1293
core nullity                   488
core components             [1781]
```

The ordered core-column SHA-256 is

```text
5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8
```

The core contains three seed relations and 1,778 feedback relations. The
seed values are 2, 11, and 27. The feedback records cover eight active-pair
families. Their orientation counts are 1,138 `u_power_times_v` and 640
`u_times_v_power`.

Also select every distinct value whose first raw occurrence is before raw
record 5,616. Rebuild the public matrix from this frozen prefix and
reconstruct:

```text
distinct values               4293
public rows                    5607
rank                           4291
nullity                           2
initial degree-one rows        4012
peeled columns                 3920
core columns                    373
core rows                       387
core rank                       371
core nullity                      2
core components               [373]
```

The ordered prefix-core SHA-256 is

```text
9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df
```

## Public useful certificate

Use only a dependency produced by the reconstructed public matrix and its
declared public kernel scan. Do not hard-code certificate indices, a root,
or factors. Verify that this scan finds a dependency of support 166 inside
the full core whose exact relation-value product is a square. Its root R
must satisfy

```text
R mod N           132013085
gcd(R - 1, N)         19727
gcd(R + 1, N)         10267
```

## Required scope

Conclude that factor-free gcd refinement is an exact decoder for every
frozen batch and that degree-one peeling is a lossless decoder preprocessor.
For this one public N-only replay, it isolates a rank-deficient core that
contains a useful square dependency.

Do not claim that every composite input produces a nonempty core, a rank
defect, or a non-global square root. Do not claim that connectedness implies
usefulness, that useful dependencies have inverse-polynomial density, that
online deletion is safe, or that this is an all-input factoring algorithm.
