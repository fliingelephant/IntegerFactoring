# F260-D02 V2 preregistration — repaired Las Vegas integer symbolic search

## Decision boundary

This packet replaces no D01 byte. D01 remains failed. D02 is a new frozen
experiment and needs an independent hostile pre-run PASS before launch.

Finite results are guidance only. A lead is not an inverse-QP theorem. A null
is not a factoring lower bound.

## Public input and exact leaves

For odd `N`, put

```text
n  = bitlength(N)
B2 = 2^floor(n/2)
B  = floor(sqrt(N))
H  = floor(B/2)
```

The common gcd screen includes these public scalars before candidate scoring:

1. constants `1,...,n` and rational primes at most `n^2`;
2. `N-1`, `N+1`, `B`, `H`, `N-B^2`, and `2B+1`;
3. dyadic quotient, remainder, centered remainder, and bit carry
   `floor(N/2^j)-2 floor(N/2^(j+1))` for admitted `j`;
4. half-size quotients, remainders, centered remainders, and adjacent
   remainder differences for odd `u<=31`;
5. all square-root quotient/remainder/centered records for `u<=16` and
   shifts `-8<=c<=8`;
6. all seven Pell coordinates for the eight frozen `D` values and all frozen
   row indices; and
7. every reduced hypergeometric numerator, denominator, and admitted adjacent
   determinant.

The admitted dyadic indices are `j<=16` and

```text
floor(n/4), floor(n/3), floor(n/2),
2floor(n/3), 3floor(n/4), n-2.
```

The Pell values use

```text
D in {2,3,5,6,7,10,11,13}
j in {1,...,min(32,2n)}.
```

All gcd operations use public integers. Hidden factors only label whether the
returned public gcd is proper.

## Sequence sources and canonical thinning

D02 has 22 named base sequences:

```text
dyadic_q, dyadic_r, dyadic_center, dyadic_carry,
half_q, half_r, half_center, half_adjacent_r,
sqrt_q, sqrt_r, sqrt_center,
pell_x, pell_y, pell_k, pell_ell, pell_gminus, pell_gplus, pell_norm,
hyper_p, hyper_q, hyper_det_horizontal, hyper_det_vertical.
```

For each raw base source, combine equal exact integer values while preserving
the first public provenance. If more than 24 values remain, retain the 24
indices

```text
floor(i*(m-1)/23), i=0,...,23.
```

Apply the same exact-value canonicalization and thinning after each transform.
The sequence remains ordered.

## Frozen D02 grammar

Non-hypergeometric sequences admit these six transforms:

```text
identity, adjacent absolute difference, all-pair absolute difference,
adjacent absolute sum, adjacent absolute quotient, adjacent remainder.
```

The quotient and remainder use absolute adjacent inputs and emit zero for a
zero divisor. Hypergeometric sequences admit identity only. This restriction
is part of operational status.

Every word is

```text
(N-1)^n times the nth power of the product of all nonzero absolute
values from zero, one, or two admitted sequence programs.
```

The zero-sequence word is the baseline. A two-sequence word is admitted if
the sources share a base, both transforms are identity, or the fixed public
syntax hash in `search.cpp` is zero modulo five. Product children are sorted
by normalized syntax.

The three unconditional factored programs are exactly

```text
lcm(1,...,n), lcm(1,...,n^2), lcm(1,...,n^3).
```

The six recursive-oracle diagnostics factor the first canonical value of

```text
dyadic_r, half_q, half_r, sqrt_r, pell_y, hyper_p
```

only when its absolute value is in `(1,2^(ceil(n/2)+2))` and fits in 63 bits.
They are nonoperational. They receive a separate diagnostic ranking. They
cannot enter the operational selection or a lead.

The full central binomial coefficient is a named nonoperational control. It
is never materialized.

## Canonicalization

Each syntax is a normalized typed syntax. Commutative children sort.
Associative product nodes flatten. Exact zero, one, and `N` use canonical
names. Hard-coded D02 syntax depth is at most two.

Every candidate type is sorted by

```text
(depth, normalized syntax length, normalized syntax).
```

It then receives a 192-bit semantic fingerprint from 24 fixed public odd
composite inputs and three fixed public 61-bit moduli. This includes factored
programs. No factored fingerprint is a hard-coded identifier. The
lexicographically first normalized syntax represents a duplicate fingerprint.

Retain at most 4,096 canonical programs per type after complete enumeration.
The cap is label-free. Preserve program counts, syntax, depth, operational
status, oracle status, and fingerprint.

## Exact scoring

Use every formula in `ALGEBRA.md`.

For a factored program, retain:

```text
direct factor probability;
stripping factor probability;
strict-growth probability at M=1 and M=2;
factor-or-growth probability at M=1 and M=2;
expected log-lcm gain at M=1 and M=2;
the same strict-growth, factor-or-growth, and expected-gain values at hidden
diagnostic M=gcd(p-1,q-1);
three exact dyadic Delta-Phi distributions and expectations;
the maximum operational primary score.
```

The expected-gain implementation must be linear in the support of `A`.

For a word, retain exact P205 probability, `H(W)`, both residual log sizes,
and baseline improvement. For a sequence, retain exact distinct-pair Miller
probability, primary collision contributions, captured log mass and fraction
on both hard residuals, and exact joint P241 scores.

The row score is the maximum within one candidate channel only. Probabilities
from different candidate programs are never added. A common proper-gcd screen
sets every candidate's row score to one. A candidate-specific proper gcd sets
that candidate and each dependent word to one.

## Frozen cohorts

Use bounded deterministic SplitMix64 streams. Generate balanced distinct
semiprimes in three cohorts:

```text
random:       independently generated exact-bit primes;
safe-safe:    p=2r+1 and q=2s+1, with all four values prime;
consecutive:  q is the next prime after p at the same exact bit length.
```

Every accepted row obeys `p<q<2p`. Moduli are unique across discovery and
held-out splits. Discovery publishes only public `N` in a byte-authenticated
corpus manifest. Held-out verifies that manifest before generation and rejects
any repeated `N`.

```text
discovery factor bits: 16,24,32
held-out factor bits:   40,48,56,60
```

Counts per discovery size are `2048 random + 512 safe-safe + 512
consecutive`, except that 16-bit safe-safe has 256 rows. Counts per held-out
size are `4096 random + 1024 safe-safe + 1024 consecutive`.

```text
discovery total:  8,960
held-out total:  24,576
combined total:  33,536
```

Every prime search, safe-prime search, next-prime scan, factorization restart,
and cohort retry has a source-level finite cap. Exhaustion aborts the run.

## Discovery ranking and exact selection

Run all candidates on discovery rows. Pool bit sizes only for the four frozen
ranking orders. Pooling is row-weighted within each cohort. For order four,
the row statistic is the arithmetic mean of the three separately retained
`Delta-Phi` expectations. Keep per-size aggregates for output.

Rank operational programs separately by:

1. minimum cohort mean primary score;
2. minimum cohort upper median minimum-side captured-log fraction;
3. minimum cohort mean exact Miller probability; and
4. minimum cohort mean expected dyadic potential decrease.

Ties use normalized syntax. Compute the literal first eight IDs under each
complete order. Form their ordered union. Only after this union, fill to 32
with the first not-yet-selected programs under complete order 1. No later
order may scan past its eighth entry to add a novel program.

Write the 32-row selection, close it, compute SHA-256 from its exact bytes,
and write a digest sidecar. The runner independently verifies that sidecar.
Held-out receives the verified expected digest, reads the selection bytes
once, verifies the digest, and parses those same bytes. It
requires exact header and field counts, 32 unique known IDs, matching kind,
syntax, fingerprint, and `operational=1,oracle=0`.

The held-out process reads no discovery score or aggregate file. It requires
that the output directory first contain the exact ten-file discovery set. It
then verifies only the selection bytes and the public discovery-corpus bytes.
It generates held-out rows only after both byte verifications pass.

## Frozen aggregate output

Every aggregate row is keyed by

```text
program, split, factor bit size, cohort.
```

Discovery writes exactly:

```text
F260-D02.grammar.tsv
F260-D02.discovery.corpus.tsv
F260-D02.discovery.corpus.sha256
F260-D02.discovery.aggregates.tsv
F260-D02.discovery.certificates.tsv
F260-D02.discovery.collisions.tsv
F260-D02.discovery.oracle.tsv
F260-D02.selection.tsv
F260-D02.selection.sha256
F260-D02.discovery.manifest.tsv
```

Held-out adds exactly:

```text
F260-D02.heldout.corpus.tsv
F260-D02.heldout.aggregates.tsv
F260-D02.heldout.certificates.tsv
F260-D02.heldout.collisions.tsv
F260-D02.heldout.lead_gate.tsv
F260-D02.heldout.manifest.tsv
```

Certificate output preserves split, bit size, cohort, row index, source
syntax, and exact proper factor. Collision output preserves the largest exact
primary contribution for each sequence aggregate cell, including side,
residual prime and exponent, collision probability, captured bits, and public
row identity. Held-out contains only the 32 selected programs and their
dependencies. A sequence used only as a word dependency evaluates its values,
gcd screens, modular product, and two-adic support. It does not evaluate the
unselected pair-collision channel. Held-out has no dense all-program-by-input
matrix.

Every source writer checks an aggregate one-GiB budget before each write,
checks close status, and refuses overwrite. Phase manifests contain file byte
counts, line counts, and SHA-256.

For `lcm(1,...,n^3)`, the candidate-specific gcd pre-screen multiplies the
squarefree support with primes above `n^2` modulo `N` and screens that public
residue when needed. Primes at most `n^2` were already screened as common
public leaves. On a registered balanced row, `q<2p` implies
`p>sqrt(N/2)`. Therefore `2(n^3)^2<N` publicly certifies that the remaining
support cannot contain either factor and skips the product without changing
the gcd result. This preserves the full factored support and avoids a
per-prime gcd loop. Recursive-oracle factor maps receive the common leaf
screen and screen each diagnostically revealed primary before diagnostic
scoring. Those recursive screens remain nonoperational.

## Frozen finite lead gates

V2 changes D01's unrealized “event” wording to an exact expected-certificate
mass. No randomized annihilator outcome is fabricated.

For each selected operational program, define strong finite lead as all of:

1. positive mean primary score on safe-safe and consecutive cohorts at each
   held-out size;
2. for each hostile cohort, upper-median loss growth from 40 to 60 factor bits
   is less than 15 bits;
3. expected exact factor-or-certified-growth mass is at least 16 in each
   hostile cell at 56 and 60 factor bits; and
4. the program is operational and not an oracle/control.

The exact loss is `-log2(primary score)`. A zero median score has infinite
loss and fails. The threshold 15 freezes “visibly slower” as slope below
`3/4` over the 20-bit interval.

A collision anomaly requires the upper median minimum-side captured-log
fraction to be at least `1/64` in every held-out bit-size/cohort cell. The
lead-gate TSV records every component and both final booleans. A null lead is
a valid experiment result and does not make the runner fail.

## Runner and resource gates

The runner must:

1. authenticate every frozen packet byte;
2. authenticate an independent hostile-audit artifact with exact PASS text;
3. refuse existing output or log directories;
4. refuse active F258-D01, F259-D01, F260-D01, F261-D01, F262-D01,
   F263-D01, or F264-D01 production before validation, discovery, and held-out;
5. require at least eight visible CPUs, 8 GiB available memory, 2 GiB free
   disk, and one-minute load no larger than four times visible CPUs;
6. compile C++17 under `nice 15`, a 4 GiB virtual-memory cap, and timeout;
7. run self-test and the full-row public validation benchmark before corpus
   generation;
8. reject benchmark projections above four hours, 4 GiB, or 1 GiB output;
9. use at most eight workers, `nice 15`, one shared four-hour deadline, a
   4 GiB virtual-memory limit, and a one-GiB file limit;
10. recheck conflicts at both split boundaries;
11. verify exact output sets and row counts; and
12. check combined uncompressed output and log bytes before final manifest.

The benchmark evaluates one fixed maximum discovery row with the full grammar
and one fixed maximum held-out row with a conservative 32-program dependency
envelope. It is validation only. It supplies no cohort evidence.

## Validation status

At static freeze, F258-D01 is active and D02 has not been compiled, executed,
self-tested, benchmarked, or transferred. `VALIDATION_PENDING.md` is part of
the frozen packet. No discovery or held-out corpus may start until target
validation passes and a fresh independent hostile audit gives an unqualified
PASS.
