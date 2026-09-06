# F157-D01 result

## Verdict

**CAPABILITY on one fixed input; finite null on four fixed inputs.**

The authoritative run passed in 167.39 seconds. It stayed inside the named
900-second hard timeout.

The public factor-free decoder reconstructed every exact base relation. Its
rank matched the pinned F111 or F118 rank on all five inputs. Every old
dependency had a global root. Every old direct endpoint screen was null.

Support one tested all 356,241 selected basis records. It found no proper
factor.

Support two covered exactly 15,366,751,493 unordered basis pairs. It found 65
proper-hit pairs for `N = 3241632473`. It found none for the four 58-bit
inputs.

| `N` | Basis rank | Public blocks | Support-one hits | Support-two pairs | Support-two hits |
|---:|---:|---:|---:|---:|---:|
| 3,241,632,473 | 11,874 | 13,284 | 0 | 70,490,001 | 65 |
| 204,800,061,759,986,701 | 106,937 | 134,359 | 0 | 5,717,707,516 | 0 |
| 204,800,066,879,973,329 | 80,446 | 100,507 | 0 | 3,235,739,235 | 0 |
| 204,800,093,759,919,353 | 65,005 | 82,445 | 0 | 2,112,792,510 | 0 |
| 204,800,123,199,900,673 | 91,979 | 115,799 | 0 | 4,230,022,231 | 0 |

## Public certificate

The first proper pair has basis indices `(253, 9723)` and source columns
`(253, 9729)`. The public common-block product is `C = 534`. The public star
construction gives

```text
z = 3183314832
w = z^(-1) mod N = 205056
gcd(z - w, N) = 41011
gcd(z + w, N) = 1
N / 41011 = 79043
```

Thus this support-two decorated product exposes the proper factor `41011`.
The old frozen layer did not expose a factor through its direct screens or
its normalized-root image. The other 64 certificates are in `OUTPUT.json`.
Of the 65 pairs, 63 expose `41011` and two expose `79043`. The sorted
candidate-pair hash is
`ef54beec77babbcd82ea9e9833c24216bf4e6ac4603811c6a8abb160e15eca3d`.

## Completeness and disclosure

The support-two discovery index used the disclosed prime factors. This is
factor-assisted indexing, not a factoring algorithm. It partitions pairs by
their least common light block or their exact heavy-block intersection. Its
joint local-value lookup removes cases that have the same sign modulo both
factors. Those cases can give only the improper gcd `N`.

Every retained candidate was then rebuilt from the public factor-free basis.
Every hit was verified by a direct public gcd. The index retained exactly 65
candidates. All 65 gave a proper public gcd. It retained no false candidate.
For each input, the reported null count is the full unordered-pair count
minus the publicly verified hit count.

## Claim boundary

This is exact finite evidence. It proves that the F156 support-two operation
has real capability on the fixed 32-bit frozen-null witness. It also gives a
complete support-at-most-two null result on four fixed 58-bit frozen-null
inputs.

It does not give a public method to locate the successful pair. It does not
prove a density bound, an all-input theorem, or a quasipolynomial factoring
algorithm. The remaining source-side problem is to replace the disclosed
factor-assisted index with a public quasipolynomial selector, or to prove
that a larger sparse support layer has enough useful pairs.
