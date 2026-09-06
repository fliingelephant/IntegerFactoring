# F260-D01 preregistration — Las Vegas integer symbolic search

## Purpose and evidence boundary

This is an independent large-scale C++17 heuristic search for public
integer sources that make certified Las Vegas progress in the beta-two
framework.  It searches for either a proper gcd, a certified common-primary
lcm gain, an improved unfactored Miller word, or high distinct-integer
collision energy on a hidden hard residual.

Finite evidence is guidance only.  A holdout signal is not an inverse-QP
theorem.  A null is not a factoring lower bound.

## Material difference from prior routes

P197 fixes the exact aggregate-order drift target.  P198 tests one uniform
half-size child bank.  P200--P204 test zero-defect quotient words and their
Miller amplification.  P206/P241 identifies collision energy but does not
enumerate a broad typed source grammar.  F239 tests seven fixed binary-spine
products.  F255 searches Pell-resultant words but does not score certified
primary growth, dyadic potential, or integer-source collision energy.

F260 combines all four exact operational scores in `ALGEBRA.md` and searches
a typed, public grammar.  It includes factorable-annihilator programs,
unfactored words, collision sources, and short exactly evaluable
hypergeometric ratios.  It ranks only by history-safe Las Vegas progress.

## Frozen public leaves

For an odd input `N`, put

```text
n = bitlength(N)
B2 = 2^floor(n/2)
B = floor(sqrt(N))
H = floor(B/2)
```

The public scalar leaves are:

1. constants `1,2,...,n` and primes at most `n^2`;
2. `N-1`, `N+1`, `B`, `H`, `N-B^2`, and `2B+1`;
3. dyadic quotients, positive remainders, centered remainders, and quotient
   carries for `j` in
   `{1,...,n-1}` thinned to `j<=16` or
   `j in {floor(n/4),floor(n/3),floor(n/2),2floor(n/3),3floor(n/4),n-2}`;
4. for odd `u in {1,3,5,...,31}`, the half-size children
   `uN mod B2`, quotients `floor(uN/B2)`, centered residues modulo `B2`,
   and all adjacent differences in increasing `u`;
5. square-root quotient/remainder records for
   `u in {1,2,...,16}` and shifts `c in {-8,...,8}`:
   `floor(uN/(B+c))`, `uN mod (B+c)`, and centered residues;
6. Pell row coordinates `x,y,k,ell,g_minus,g_plus,norm_digit` for
   `D in {2,3,5,6,7,10,11,13}` and indices
   `j in {1,...,min(32,2n)}`;
7. reduced hypergeometric endpoints `(P_rc,Q_rc)` for
   `r,c in {-8,...,8}` with valid binomial indices, plus adjacent ratio
   determinants and cross-multiplied finite differences.

Every leaf is computable from `N` without its factors.  Duplicate integer
values remain distinct only until public provenance is combined; exact
value and normalized syntax then canonicalize them.

## Frozen typed program grammar

There are four types.

```text
Scalar:       one public integer
Sequence:     ordered public multiset of 1..24 integers
Factored:     complete prime-power factorization of a positive integer
Word:         positive integer represented by residues and public provenance
```

Depth-zero programs are the named leaf families.  The typed vocabulary
contains these operations:

```text
Scalar x Scalar:
  abs difference, sum, product, gcd, lcm,
  quotient and remainder when the divisor is nonzero,
  exact division when divisibility holds,
  cross determinant P_i*Q_j-P_j*Q_i.

Sequence:
  adjacent differences, all-pair differences (first 24 values),
  adjacent sums, quotients, remainders, centered remainders,
  prefix products reduced modulo scoring moduli.

Scalar/Sequence -> Word:
  product of nonzero absolute values, saturated nth power,
  product of adjacent differences, product of all-pair differences,
  product with (N-1)^n, and product with the public smooth word.

Scalar/Sequence -> Factored:
  unconditionally only for products/lcms of already factored small leaves;
  conditionally for values below 2^(ceil(n/2)+2), tagged
  recursive-oracle.  Finite factorization of the latter is a diagnostic
  stand-in for the declared recursive half-size dispatcher and is excluded
  from unconditional operational ranking.
```

For the hypergeometric family, only the operations allowed by
`ALGEBRA.md` enter operational programs.  The full central-binomial oracle
control is never ranked.

Expansion stops at normalized syntax depth two.  Product commutativity is
sorted.  Associative gcd/lcm/product nodes are flattened.  Public exact
values `0,1,N` are normalized.  Programs are canonicalized by normalized
syntax and by a 192-bit fingerprint on 24 public synthetic odd composite
inputs.  No hidden prime label enters canonicalization.

The implementation keeps at most 4,096 canonical programs per type.  If a
type exceeds the cap, retain the lexicographically first programs by
`(depth, syntax length, syntax)`.  This cap is fixed and label-free.

The D01 admitted expansion is more specific than the vocabulary.  It uses
all 21 named sequence families, each under `id`, adjacent difference,
all-pair difference, adjacent sum, adjacent quotient, and adjacent
remainder.  It then forms `(N-1)^n` times the saturated product of one or
two sequence programs.  Two-sequence products are admitted when they share
a base source, both are identity transforms, or pass the fixed public hash
filter encoded in `search.cpp`.  The three unconditional factored programs
are exactly

```text
lcm(1,...,n), lcm(1,...,n^2), lcm(1,...,n^3).
```

The six conditional recursive-oracle programs factor the first value of
`dyadic_r`, `half_q`, `half_r`, `sqrt_r`, `pell_y`, and `hyper_p` when it is
below the declared half-size bound.  They are reported in a separate
diagnostic ranking.  They cannot enter the 32-program operational
selection.  Standalone scalar nodes outside these admitted families are
vocabulary for a future registration, not D01 candidates.

## Frozen scoring

For each semiprime row, first gcd-screen every scalar and every exact
numerator/denominator.  A proper gcd is an exact factor certificate.

For each `Factored` program, use the full primary-pair distribution in
equations (1)--(3).  Record exact direct-factor probability, exact
factor-or-strict-growth probability, expected `log2(M'/M)`, and dyadic
potential decrease for each frozen `t`.  Operational ranking uses public
`M=1` and the program's own previously certified smooth block.  The hidden
state `M=gcd(p-1,q-1)` is reported only as a hostile/oracle diagnostic.

For each `Word`, record exact P205 Miller probability, `H(W)`, both
residuals, and improvement over `(N-1)^n`.

For each `Sequence`, record exact distinct-sample collision energy (5),
captured log mass (6), and exact average P205 score of pair-difference words
when the sequence has at most 24 values.

The primary row score is the maximum of the following separate experiment
channels.  Probabilities from different channels are not added:

```text
factor probability + nonfactor strict-growth probability,
factor probability + E[dyadic potential decrease]/max(1,Phi),
exact Miller factor probability,
exact average pair-difference Miller probability.
```

Direct proper gcd has score one.  A program must remain public and
operational to rank.

## Frozen cohorts

Use deterministic SplitMix64 streams encoded in the source.  Generate
distinct balanced semiprimes `N=pq`, `p<q<2p`, in three cohorts:

```text
random:       independent primes of the declared factor bit length
safe-safe:    p=2r+1 and q=2s+1, all four values prime
consecutive:  q is the next prime after p, subject to the same bit length
```

The split is:

```text
discovery factor bits: 16,24,32
held-out factor bits:   40,48,56,60
```

Per discovery bit size use `2048 random + 512 safe-safe + 512 consecutive`
rows.  Per held-out bit size use
`4096 random + 1024 safe-safe + 1024 consecutive` rows.  At 16 bits the
safe-safe count is exactly 256.  Planned total is 33,536 rows.

Safe-safe is the primary hostile common-capacity cohort.  Consecutive primes
are the bounded-gap hostile cohort.  A result must report both separately.

## Frozen train/held-out firewall

All programs run on discovery rows.  Rank separately by:

1. minimum mean primary score over the three discovery cohorts;
2. minimum median captured-log fraction over the three cohorts;
3. minimum mean exact Miller probability;
4. minimum mean expected dyadic potential decrease.

Take the top eight operational programs under each order, deduplicate by
syntax, and fill to exactly 32 with the first programs under order 1.  The
discovery process writes `F260-D01.selection.tsv` containing the 32 syntax
strings, fingerprints, discovery aggregates, and its SHA-256.  It closes
that file, reopens it, verifies its hash, discards discovery rows, and only
then calls the held-out generator.  The held-out generator aborts unless
the verified selection manifest exists.  It evaluates only those 32
programs.  No grammar or selection rule changes after held-out generation.

## Frozen outputs and interpretation

Preserve:

* grammar counts and canonical syntax hashes;
* the 32-program selection manifest;
* aggregate TSV rows by program, split, bit size, and cohort;
* aggregate held-out rows for selected programs, without a dense
  program-by-input matrix;
* exact direct gcd certificates;
* top residual-primary collision explanations;
* self-test and resource logs.

A strong finite lead must satisfy all of these:

1. nonzero held-out progress on safe-safe and consecutive cohorts at all
   four bit sizes;
2. median `-log2(primary score)` grows visibly slower than factor bit size;
3. at least 16 exact proper-gcd or certified-growth events in each hostile
   cohort at 56 and 60 bits;
4. the program is operational, not a central-binomial oracle control.

Linear hostile growth is a finite null for the frozen grammar.  A collision
source is a useful anomaly if its minimum-side captured-log fraction stays
bounded away from zero on all held-out sizes, even if it does not meet the
strong lead threshold.  Neither criterion is a theorem.

## Resource envelope and incompatibility

Read-only remote inspection at `2026-08-13T14:18:33Z` observed:

```text
32 allowed CPUs
load average 57.80,58.21,57.99
503 GiB RAM, 367 GiB available, no swap
22 GiB free disk
F258-D01 active under nice 15 (PID 6230 and wrappers)
```

F260 production corpus generation and scoring are incompatible with F258,
F259, and F261.  The runner must refuse to start production if any
mathematical process or runner with one of those experiment IDs is active.
Before the final source freeze, the root explicitly authorized target-host
compilation and the algebra-only self-test to overlap F258 under a fresh
resource check, using one process/core, `nice -n 15`, and a 120-second hard
timeout.  Because `/usr/bin/time` is absent, the approved exact replacement
adds `getrusage(RUSAGE_SELF)` and steady-clock metrics to the binary.  One
public synthetic benchmark constructs all 24-input fingerprints and the
widest public sources at one 120-bit odd composite.  It uses no hidden
factors, cohort generation, or semiprime score.  These exceptions generate
no mathematical evidence.  The
production run uses at most eight workers under `nice -n 15`, a 4 GiB
virtual-memory cap, and a four-hour timeout.

The frozen cap is 4,096 programs per type, 9,216 maximum discovery rows,
24,576 held-out rows, 32 held-out programs, and at most 786,432 held-out
program-row scores.  The expected runtime is 30--180 minutes on eight
allowed CPUs.  Estimated peak RSS is below 2 GiB.  Sparse output is
estimated below 200 MiB and must abort before 1 GiB.  This stays below the
user caps and the observed remote disk margin.

The target-host checks used source hash
`905001a2bc2a06a653bfad68bb22d09f9dee36a78472a288ba305632c5f7f01b`.
Compilation succeeded with empty stdout/stderr.  The algebra self-test
reported `126` sequence programs, `1,957` word programs, `9` factored
programs, and `2,092` total programs in `0.197080` seconds with peak RSS
`4,896 KiB`.  The public-only benchmark reported the same grammar and
checksum `17142857847814433080` in `0.121076` seconds with peak RSS
`4,828 KiB`.  These timings cover grammar construction and public source
evaluation, not cohort generation, hidden-label factorization, or full
scoring.  Therefore the 30--180 minute production estimate remains a
conservative forecast, not a benchmarked guarantee.  The first compile
failed only on two Boost expression-template ternaries; its exact log and
hash are preserved.  The first benchmark wrapper did not start because
`/usr/bin/time` is absent; the approved in-process metrics replaced it.
After these checks, static review found that a high-overlap top-eight union
could contain fewer than 32 programs.  The final source makes the fill pass
unbounded up to the already frozen total of 32.  This is a mechanical
selection-firewall repair; it changes no grammar, score, cohort, or selected
order.  The final source hash is recorded in `PRELAUNCH_MANIFEST.md`.  A
last target transfer timed out while F258 was active, so this final hash has
not been target-compiled.  Production must repeat compilation and the
self-test before any corpus generation, as `remote_run.sh` requires.

No F260 mathematical run may start until the incompatible processes have
finished.  If Boost.Multiprecision, C++17, exact integer arithmetic, or the
frozen workflow is unavailable, stop.  Do not substitute another language,
arithmetic, corpus, grammar, or selection protocol.
