# F157-D01 V2 corrected result

## Version scope

V2 is a narrow claim-boundary correction. It changes no source, input,
registration, run, output, certificate, count, or finite outcome. The V1
arithmetic evidence remains frozen byte-identically.

The V1 hostile audit passed the registered computation and failed two prose
claims about the availability of a public locator. V2 corrects only those
claims.

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

The registered support-two discovery index used the disclosed prime factors.
This is factor-assisted indexing. It partitions pairs by their least common
light block or their exact heavy-block intersection. Its joint local-value
lookup removes cases that have the same sign modulo both factors. Those cases
can give only the improper gcd `N`.

Every retained candidate was rebuilt from the public factor-free basis.
Every hit was verified by a direct public gcd. The index retained exactly 65
candidates. All 65 gave a proper public gcd. It retained no false candidate.
For each input, the reported null count is the full unordered-pair count minus
the publicly verified hit count.

The factors accelerate this registered finite run. They are not required by
the declared F156 public algorithm.

## Public quasipolynomial locator

The pinned F156 source sets

\[
L=\lceil\log_2(n+1)\rceil,
\qquad
D=L^2,
\]

and publicly enumerates every nonempty relation-basis subset of support at
most `D`. Here `n` is 32 or 58, so `L=6` and `D=36`. Support two is inside
the declared public menu.

A factor-free public locator therefore does the following:

1. rebuild the public base ledger, parity basis, and actual basis lifts;
2. enumerate all unordered basis pairs in the fixed order;
3. construct each public star-product and run both gcd screens;
4. stop at the first proper gcd.

F156 bounds the base rank by `2^{O(L^4)}` and the total source cost by
`2^{O(L^6)}`. Squaring the quasipolynomial basis size remains
quasipolynomial. Thus exhaustive support-two enumeration is already a public
quasipolynomial locator. On `N = 3241632473`, it reaches the reported proper
pair without using `p` or `q`.

The registered factor-assisted index is an implementation acceleration. It
made the complete five-input classification fit the 900-second experimental
limit. V2 makes no claim that exhaustive public enumeration fits that limit.

## Exact claim boundary

This is exact finite evidence. It proves that the F156 support-two operation
has real capability on the fixed 32-bit frozen-null witness. It also gives a
complete support-at-most-two null result on four fixed 58-bit frozen-null
inputs.

It gives a public quasipolynomial locator on the fixed positive input. It does
not prove that a support layer succeeds on a new input. It does not give a
success frequency, useful-pair density, all-input progress law,
polynomial-time factoring algorithm, or public selector asymptotically
smaller than exhaustive F156 enumeration.

The remaining theoretical problem is an all-input success or progress law.
A separate practical problem is a public selector that is substantially
faster than exhaustive enumeration. Neither problem is the existence of a
public quasipolynomial locator on this fixed input.
