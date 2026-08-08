# Frozen-layer proof-blind reconstruction

## Verdict

**PASS.** The complete normalized frozen-layer dependency space has no
non-global square root modulo `N = 3241632473`. All seven vectors in a full
binary kernel basis have root residue `1`. Their terminal gcds are
`gcd(R - 1, N) = 3241632473` and `gcd(R + 1, N) = 1`.

This verdict concerns only the fixed public frozen batch. It is not an
all-input theorem or a factoring algorithm.

## Frozen source

- Trial gcds: `gcd(t, N) = 1` for all `2 <= t <= 1024`.
- Seed records: 31 retained from 31 attempts.
- Seed gcd basis: 23 blocks. The blocks are pairwise coprime,
  perfect-power-free, and reconstruct all 62 seed endpoints exactly.
- Ordered frozen pairs: 31.
- Frozen attempts: 63,550.
- Frozen duplicate residues: 49,230.
- Raw retained frozen relations: 14,320.
- Total retained records through the frozen layer, including seeds: 14,351.

The replay evaluated 28,702 direct sign screens through the frozen layer.
There was no proper factor. One screen was nonunit but improper. It was the
retained frozen record with `c = w = 1`, where
`gcd(c - w, N) = gcd(0, N) = N`.

## Exact-value normalization and matrix

- Raw frozen relation values: 14,320.
- Removed unit values: 1.
- Removed repeated exact-value occurrences: 2,438.
- Distinct repeated-value classes: 2,083.
- Distinct normalized columns: 11,881.
- Final exact-value gcd-basis blocks: 13,284.
- Zero block rows: 0.
- Repeated nonzero block rows: 0.
- Distinct nonzero public rows: 13,284.
- Binary rank: 11,874.
- Kernel dimension: 7.

The exact-value basis is pairwise coprime and perfect-power-free. Its 69,894
signature entries reconstruct all 11,881 exact values with no mismatch.

## Complete kernel roots

| Basis vector | Selected normalized columns | Root mod N | gcd(R - 1, N) | gcd(R + 1, N) |
|---:|---|---:|---:|---:|
| 0 | 533, 3968, 3973, 10653, 10657, 10660 | 1 | 3241632473 | 1 |
| 1 | 870, 2567, 2569, 2571, 4312, 4317 | 1 | 3241632473 | 1 |
| 2 | 1187, 1189, 1191, 1193, 2895, 2899 | 1 | 3241632473 | 1 |
| 3 | 1367, 1369, 1371, 4850, 4852, 4854 | 1 | 3241632473 | 1 |
| 4 | 1443, 1444, 1448, 3149, 3154, 3156 | 1 | 3241632473 | 1 |
| 5 | 1450, 1452, 1456, 1458, 3158, 3166 | 1 | 3241632473 | 1 |
| 6 | 1632, 1633, 1634, 5135, 5137, 5139 | 1 | 3241632473 | 1 |

Every selected product was multiplied as an exact positive integer. Every
product was an exact square. The root bit lengths range from 178 to 183.
Every root squares to one modulo `N`.

## Why the decode is complete

The deterministic gcd basis gives pairwise-coprime blocks with exact integer
signatures. For a rational prime inside one block, its parity row is either
the block signature row or zero. Perfect-power extraction guarantees that
each block has at least one odd internal exponent, so every nonzero block row
is also a rational-prime row. Thus the deduplicated block rows have the same
kernel as the unavailable prime-valuation matrix.

The seven reported vectors are independent, satisfy every public row, and
have count `11881 - 11874 = 7`. They are therefore a full kernel basis. The
normalized-root map is a homomorphism. All seven basis images are `+1`, so
every normalized dependency has root `+1`.

Normalization does not hide a non-global root. A removed unit column has
root `1`. Two columns with the same exact value `P` add a dependency with
product `P^2` and positive root `P`. Every retained relation has
`P = cw congruent to 1 (mod N)`. Duplicate columns therefore add only
global `+1` roots.

## Factor-free and advice boundaries

The decoder used integer gcd, modular inverse, modular exponentiation, exact
integer nth-root extraction, exact integer square root, and binary Gaussian
elimination. It used no factorization routine, primality test, endpoint prime
factorization, or known factor of `N`.

The public stop count and advice indices were not used. They belong to the
cross-layer fixed certificate. This task exhausts only the complete frozen
batch before the appended trajectories. It does not supply a selector,
probability law, or all-input result.

## Failed attempt

Version 1 completed and validated the same 13,284-block exact gcd basis, then
failed its own kernel orthogonality assertion. Its echelon insertion could
retain lower pivot columns. The named timeout runner preserved the complete
log as `RECONSTRUCT_LAYER_FAILED_20260808T034025Z_EXIT_1.log`. Version 2
reduced all pivot columns before constructing the nullspace. Randomized
dimension, orthogonality, and independence checks passed before the complete
version-2 replay.
