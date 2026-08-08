# Proof-blind F116 reconstruction

## Verdict

**PASS.** The public source replay reached the exact retained-record stop.
All direct screens passed. The 6,486 advised relation values multiply to an
exact positive square. Its positive root is a non-global square root of one
modulo `N`, and both terminal gcds are proper.

```text
N = 12800004879996637
R mod N = 5266287723884331
gcd(R - 1, N) = 159999943
gcd(R + 1, N) = 80000059
159999943 * 80000059 = 12800004879996637 = N
```

## Isolation

Before reconstruction, I read only:

1. `RECONSTRUCT_STATEMENT.md`
2. `RECONSTRUCT_INPUT.json`

I did not read another F116 file. I did not read an F104, F110, F111, or F115
file. I did not use a factorization routine, primality routine, or known
factor of `N`. After the replay, I inspected only the new
`RECONSTRUCT_*` artifacts.

## Public instance and advice

- `N`: 12,800,004,879,996,637.
- `n`: 54, verified against `N.bit_length()`.
- `B = n^2`: 2,916.
- Trial gcds: `gcd(t, N) = 1` for every `2 <= t <= 2916`.
- Retained-record stop: 771,082.
- Advice indices: 6,486.
- First advice index: 655.
- Last advice index: 771,081, the final retained record.
- The indices are distinct, strictly increasing, and in range.
- Advice-index SHA-256:
  `5f049b7552d76c1b99c202994565965a0ef11f76230cfdce297937a76a31c0ef`.

## Seed basis and frozen layer

The 53 seeds were all retained. Their 106 endpoints produced a deterministic
39-block gcd basis.

- Basis gcd scans: 18,035.
- Basis pops: 795.
- Perfect-power reductions: 27.
- Proper gcd splits: 124.
- Equal merges: 193.
- Final blocks: 39.
- Exact signature entries: 214.
- Endpoint reconstruction mismatches: 0.

The final blocks are pairwise coprime and perfect-power-free. They reconstruct
every endpoint exactly. They define 53 ordered frozen pairs.

- Frozen trajectory attempts: 309,202.
- Frozen trajectory duplicates: 233,418.
- Frozen trajectory retained records: 75,784.
- Frozen-layer records including seeds: 75,837.

## Complete small-pair menu prefix

The full public menu has 1,378 unordered pairs.

- Menu pairs started before the stop: 177.
- Menu pairs completed: 176.
- Final partial menu pair: index 176, `(5, 29)`.
- Started pairs with at least one retained record: 166.
- Menu attempts: 1,026,963.
- Menu duplicates: 331,718.
- Menu retained records: 695,245.

## Complete source counts

```text
total attempts   = 1336218
total duplicates = 565136
total retained   = 771082
attempts - duplicates = retained
```

Retained provenance:

| Provenance | Records |
|---|---:|
| Seed | 53 |
| Frozen seed-basis pair | 75,784 |
| Nonadaptive menu pair | 695,245 |

The full retained-record transcript SHA-256 is
`d14d9139e6e5d276c1be9a51d7cc7bb32cd0da466fb52a08674437f6ae094199`.

## Every direct screen

All 771,082 retained residues are units. The replay evaluated 1,542,164 sign
screens.

| Screen result | Count |
|---|---:|
| Unit | 1,542,163 |
| Improper nonunit | 1 |
| Proper factor | 0 |

The one improper result is retained record 70,008 from frozen pair 45. It has
`c = w = 1`, so `gcd(c - w, N) = gcd(0, N) = N`.

The complete screen-transcript SHA-256 is
`00a8712dd0e068fad69c4568c528cfbeaffe48a34a2afffdcb130fd0c2fd801b`.

## Advised exact-square certificate

Selected provenance:

| Provenance | Selected records |
|---|---:|
| Seed | 0 |
| Frozen seed-basis pair | 1,844 |
| Nonadaptive menu pair | 4,642 |
| Total | 6,486 |

The support uses 12 distinct frozen pairs and 137 distinct appended menu
pairs. The full appended-pair list is in `RECONSTRUCT_OUTPUT.json`.

- Selected-value SHA-256:
  `4da154587186547ffa06bab9eb37090db0819647588e2be8f330a18bd70ca1a1`.
- Selected-record transcript SHA-256:
  `8d00cca0af833d0b9c188093df9ba89d3db6fab5c43f79139c8d55eb55de13e6`.
- Exact product bit length: 672,808.
- Exact product SHA-256:
  `a10c30c2be30d7665f02ab721e7b1e548dd8986c0a4ce6b2050f1e505bfef696`.
- Positive root bit length: 336,404.
- Positive root SHA-256:
  `1c70b587135415eb699cd7032630ee8990162e3d9a459cd5511df34cbaa3ab71`.

The product is an exact positive square. The root residue squares to one
modulo `N`. It is neither `1` nor `N - 1`. Both terminal gcds are
proper and their product is exactly `N`.

## Factor-free, advice, and monotonic boundaries

The replay used integer gcd, modular inverse, modular multiplication, exact
perfect-power extraction, and exact integer square root. It did not factor an
endpoint, exact relation value, basis block, or `N`.

The 6,486-index support is external advice. This replay verifies it. It does
not discover it and does not prove that another input succeeds.

Appending more ordered records preserves every record in this valid support.
Thus exact-value dependency existence is monotone for this source prefix. A
separate complete factor-free decoder can process the full public pair menu
without using this stop or support. This monotonic consequence is not an
all-input factoring theorem.

The first named reconstruction run passed in 4.603 seconds under a
7,200-second hard timeout. No attempt failed.
