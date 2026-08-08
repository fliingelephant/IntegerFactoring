# Proof-blind complete cross-layer reconstruction

## Result

**PASS.** The ordered source, exact-value coordinates, complete factor-free
parity systems, all binary kernels, and the cross-layer quotient were
reconstructed from the public interaction input.

- The frozen layer alone has no useful dependency.
- The appended layer alone has no dependency at all.
- The globally deduplicated union has a useful dependency.
- Every useful union-coordinate dependency crosses the first-occurrence
  layer boundary.

The normalized root-map rank of the union and quotient is one modulo global
sign. The sole non-global basis image is
`R = 1058780986 (mod 3241632473)`. Its terminal gcds are:

```text
gcd(R - 1, N) = 79043
gcd(R + 1, N) = 41011
79043 * 41011 = 3241632473 = N
```

## Exact isolation statement

Before reconstruction, I read only these three supplied files:

1. `RECONSTRUCT_INTERACTION_STATEMENT.md`
2. `RECONSTRUCT_INTERACTION_INPUT.json`
3. `RECONSTRUCT_STATEMENT.md`

I did not read another pre-existing F111 file. I did not read an F98, F109,
F110, F115, or F116 file. I did not read any `LAYER_INTERACTION_*` code,
output, report, manifest, or log. I did not use an earlier numerical result.
After the run, I inspected only the new `RECONSTRUCT_INTERACTION_*` source,
log, output, and report artifacts. All files that I wrote have that prefix.

## Ordered source

- `gcd(t, N) = 1` for every `2 <= t <= 1024`.
- Seed records: 31.
- Frozen pairs: 31.
- Frozen trajectory attempts: 63,550.
- Frozen trajectory duplicate residues: 49,230.
- Frozen-layer records, including seeds: 14,351.
- Appended attempts before the stop: 3,432.
- Appended duplicate residues: 2,400.
- Appended records: 1,032.
- Total attempts: 67,013.
- Total duplicate residues: 51,630.
- Exact retained-record stop: 15,383.

All 30,766 direct sign screens were checked. No direct screen produced a
proper factor. One screen was nonunit but improper. At retained record 6,166,
`c = w = 1`, so `gcd(c - w, N) = gcd(0, N) = N`.

## Exact-value coordinates

| System | Raw | Units | Duplicate occurrences | Distinct nonunit values |
|---|---:|---:|---:|---:|
| Frozen standalone | 14,351 | 1 | 2,465 | 11,885 |
| Appended standalone | 1,032 | 0 | 195 | 837 |
| Global union | 15,383 | 1 | 2,813 | 12,569 |

The standalone frozen and appended sets share 153 distinct nonunit exact
values. The union therefore has 11,885 frozen-owned coordinates and 684
newly appended coordinates. A shared value stays frozen-owned because the
union keeps its first source occurrence.

## Factor-free union basis

The union gcd refinement produced 13,864 blocks and 74,058 exact signature
entries. The blocks are pairwise coprime and perfect-power-free. They
reconstruct all 12,569 union values with no mismatch. The parity reduction
has 13,864 distinct nonzero rows, no zero row, and no repeated row.

The computation used exact gcd refinement and exact perfect-power extraction.
It did not factor an endpoint, relation value, block, or `N`. It used no
primality test or known factor of `N`.

## Complete systems

| System | Columns | Rows | Rank | Kernel dimension | Normalized root rank | Useful dependency |
|---|---:|---:|---:|---:|---:|---|
| Frozen standalone / frozen-owned union | 11,885 | 13,288 | 11,878 | 7 | 0 | No |
| Appended standalone | 837 | 1,143 | 837 | 0 | 0 | No |
| Globally new appended coordinates | 684 | 978 | 684 | 0 | 0 | No |
| Global union | 12,569 | 13,864 | 12,551 | 18 | 1 | Yes |

Every kernel basis is complete because its vectors are independent,
orthogonal to every public row, and have count `columns - rank`.

### Frozen kernel roots

All seven frozen basis vectors select six columns. Every exact product is a
positive square. Every root is `1 mod N`. For each vector from 0 through 6:

```text
gcd(R - 1, N) = 3241632473
gcd(R + 1, N) = 1
```

The appended standalone and globally new appended systems have kernel
dimension zero, so they have no basis roots.

### Union kernel roots

| Vector | Selected columns | Root class | Root mod N | gcd(R - 1, N) | gcd(R + 1, N) |
|---:|---:|---|---:|---:|---:|
| 0 | 367 | non-global | 1058780986 | 79043 | 41011 |
| 1 | 8 | +1 | 1 | 3241632473 | 1 |
| 2 | 6 | +1 | 1 | 3241632473 | 1 |
| 3 | 6 | +1 | 1 | 3241632473 | 1 |
| 4 | 8 | +1 | 1 | 3241632473 | 1 |
| 5 | 6 | +1 | 1 | 3241632473 | 1 |
| 6 | 6 | +1 | 1 | 3241632473 | 1 |
| 7 | 6 | +1 | 1 | 3241632473 | 1 |
| 8 | 6 | +1 | 1 | 3241632473 | 1 |
| 9 | 6 | +1 | 1 | 3241632473 | 1 |
| 10 | 6 | +1 | 1 | 3241632473 | 1 |
| 11 | 6 | +1 | 1 | 3241632473 | 1 |
| 12 | 6 | +1 | 1 | 3241632473 | 1 |
| 13 | 8 | +1 | 1 | 3241632473 | 1 |
| 14 | 6 | +1 | 1 | 3241632473 | 1 |
| 15 | 8 | +1 | 1 | 3241632473 | 1 |
| 16 | 10 | +1 | 1 | 3241632473 | 1 |
| 17 | 6 | +1 | 1 | 3241632473 | 1 |

The exact coordinate lists, product hashes, root hashes, and vector hashes
for every basis vector are in `RECONSTRUCT_INTERACTION_OUTPUT.json`.

Union vector 0 selects 331 frozen-owned and 36 appended-owned coordinates.
Its exact product has 21,856 bits and is a positive square. Its positive root
has 10,928 bits. The bounded-encoding pins are:

```text
vector SHA-256  = 4bf4b99cc7cad3f6de1841369d57f14cce3c25971acb5c5c0b8d401faf340ed3
product SHA-256 = 6f7784a31401b7a43c03188668fd0c3bd4dedb201351e6e867595dfd51d68c07
root SHA-256    = a6acf32e3d6eb81f39592a76a7387b902695263764780f14f244acad34c8d490
```

## Cross-layer quotient

The complete dimensions are:

```text
dimension(K_F) = 7
dimension(K_A) = 0
dimension(K_U) = 18
dimension(K_F direct_sum K_A) = 7
dimension(K_U / (K_F direct_sum K_A)) = 11
```

The independent dimension identity is exact:

```text
18 - 7 - 0 = 11
11878 + 684 - 12551 = 11
```

Both one-layer normalized root maps are trivial. The root map therefore
descends to the quotient. Its quotient rank is one, with image classes
`{1, 1058780986}` modulo global sign.

| Quotient vector | Total columns | Frozen-owned | Appended-owned | Root class | Root mod N | Terminal gcds |
|---:|---:|---:|---:|---|---:|---|
| 0 | 367 | 331 | 36 | non-global | 1058780986 | 79043, 41011 |
| 1 | 8 | 7 | 1 | +1 | 1 | 3241632473, 1 |
| 2 | 6 | 4 | 2 | +1 | 1 | 3241632473, 1 |
| 3 | 8 | 5 | 3 | +1 | 1 | 3241632473, 1 |
| 4 | 6 | 5 | 1 | +1 | 1 | 3241632473, 1 |
| 5 | 6 | 5 | 1 | +1 | 1 | 3241632473, 1 |
| 6 | 6 | 4 | 2 | +1 | 1 | 3241632473, 1 |
| 7 | 8 | 6 | 2 | +1 | 1 | 3241632473, 1 |
| 8 | 8 | 4 | 4 | +1 | 1 | 3241632473, 1 |
| 9 | 10 | 8 | 2 | +1 | 1 | 3241632473, 1 |
| 10 | 6 | 4 | 2 | +1 | 1 | 3241632473, 1 |

Any union dependency supported only on frozen-owned coordinates belongs to
`K_F`. Any union dependency supported only on newly appended coordinates
belongs to `K_A`. Both subspaces have trivial normalized root images. Thus a
non-global union dependency must use coordinates owned by both layers.

This conclusion uses first-occurrence coordinate ownership. It does not claim
that a repeated exact value has only one record-level occurrence.

## Completeness and fixed-instance boundary

For a prime inside one final block, its parity row is either the block's
signature row or zero. Perfect-power extraction guarantees that an odd
internal exponent realizes every nonzero block row. Pairwise coprimality and
exact reconstruction therefore make the block rows complete without exposing
the primes. Restriction and remapping preserve each requested row space.

The normalized root map is a homomorphism. Testing a full kernel basis gives
the image of every dependency. Testing the quotient basis gives every image
not supplied by a pure-layer subspace.

This reconstruction concerns only `N = 3241632473`, `n = 32`, `B = 1024`,
the retained-record stop 15,383, the specified source order, and the stated
first-occurrence coordinate convention. It gives no stop selector,
other-input theorem, density law, success probability, or polynomial
bit-time factoring algorithm.

The first named reconstruction run passed in 53.322 seconds under a
7,200-second hard timeout. No computational attempt failed.
