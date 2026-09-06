# F263-D02 V2 hostile pre-run audit

## Decision

**PASS.**  The frozen F263-D02 V2 packet repairs every blocking defect in the
F263-D01 hostile audit.  The frozen V2 discovery and held-out phases may run
only after the runner's overlap and resource gates pass.  This decision does
not authorize F263-D01, does not promote a mathematical claim, and does not
turn a finite hit into an inverse-QP theorem.

## Frozen input authentication

Authentication preceded semantic review.

```text
V2_PREREGISTRATION.md  6dd1c052cb4eebba07e40b75b527254c6daa6e771bd12082fe161fb1ae11946a
V2_ALGEBRA.md           fdf72364070e5b0ded549be171afcf005dc063afe4d7179968aa58ffdbb318d6
V2_symbolic_search.cpp  05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827
V2_remote_run.sh        006e12b87552457c931eea7200a5eb6b5ba8417624a6d3b0b4d7969700b42d18
V2_preflight_remote.sh  18339cadf29d9f9fd3e9bf9dd7605b44aa9c2e4421d29481266f431df8eeaaf6
V2_PROVENANCE.md        fa8d69c29a92eead321fe069c337f40f2095074cb7e9dd3922c86392c42762bd
V2_PRELAUNCH_MANIFEST   34e04237fe055e972c26ee2db4a124768760eb63470a58a97e62e5406fce6780
V2_FROZEN.sha256        2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271
```

`shasum -a 256 -c V2_FROZEN.sha256` authenticated all 17 V2 entries.
The preserved D01 boundary also authenticated in full:

```text
FROZEN.sha256            95eb34870050009cd281b2d27413cf5a52688d3345a21e62d19fba0aa6bd3e5f
HOSTILE_PRERUN_AUDIT.md  2e5801933e3eb26b6aa1c3f8cb3e23d5d199297051ae451484cf26d791446099
```

`shasum -a 256 -c FROZEN.sha256` authenticated all 17 preserved D01
entries.  A fresh read-only target check authenticated the frozen V2 source,
compiled binary, and every retained validation stream.  In particular, the
target binary remained

```text
d8ce872f62c3c488bf22b29899423caad2f287279db144a6488227771766420a
```

and its source remained the exact local frozen source above.

## Reconstruction of the five D01 blockers

### 1. Public query scale: repaired

Production computes `modulus_bits=bitlength(N)` and passes that value to both
query banks.  Factor-bit metadata is used only in labels and output.  The bank
contains the registered powers of two, `min(n,domain)`, and
`min(n^2,domain)`, with deduplicated left, right, middle, quarter, and four
public hash starts.  Adjacent states are constructed only inside the domain,
and cross-block comparisons use the lexicographically first state at a fixed
length.

An independent reconstruction of the frozen 120-bit synthetic input gives
exactly 390 constructed states and 926,880 leaf touches.  These values match
the retained benchmark.  Thus the benchmark measures the corrected `n=120`
bank, not the D01 factor-bit bank with `n=60`.

### 2. Symbolic and recurrence authentication: repaired

The source builds 128 discovery and 64 disjoint held-back exact affine rows,
with 70 columns in the registered `28+18+18+4+2` split.  It constructs and
reduces complete matrices independently modulo both public primes.

The sparse miner enumerates exactly

```text
1 + 2*70 + 4*binom(70,2) = 9801
```

signed halves.  Its key is the full 256-coordinate residue vector.  It stores
all members of each equal-vector class, compares every pair, normalizes the
result, and authenticates every retained support-two-through-four relation
exactly on all 192 rows.  There is no digest or first-member shortcut.

Basis vectors from both prime nullspaces are independently rescaled under the
height-4096 rule and then checked exactly on all 192 rows.  The retained
self-test reports ranks `58,58`, nullities `12,12`, 14 sparse relations, and
12 authenticated small basis relations from each prime.  All six jet and six
transfer controls are present.

Each adjacent recurrence retains its order, degree, primitive coefficients,
height, dependency class, unit-target status, and authentication counts.  All
four registered affine controls are checked modulo both primes and on exact
starts 50 through 69.  The dyadic search uses both `(4,2)` and `(1,1)` in one
two-prime discovery system, checks both held-back affine families, retains all
survivors, and applies the literal constant-unit highest-shift test.  The
current frozen symbolic result contains four adjacent controls and no dyadic
survivor; this is an authenticated finite null, not a lower bound.

### 3. Dependency-cost classification: repaired

Every symbolic column now carries a typed dependency class, a parent-target
flag, an exact source-node count, and named DAG nodes.  The classifier accepts
only one unit-coefficient parent target whose other terms are `descriptor` or
`short_scan`, have dependency metadata, and have a nonoverflowing expanded
cost.  It explicitly rejects `recursive_merge`, `oracle_block`, and
`full_scan` terms.  Each identity is retained with its target, acceptance
decision, expanded node count, and reason.

The five non-operational controls are represented but never ranked.  Every
row records exact full-root, product-tree, oracle-edge, and selected-child
recomputation costs.  A direct self-test accepts a typed unit-target descriptor
identity and rejects the same shape after its dependency is changed to
`recursive_merge`.  The frozen bank currently has zero accepted shortcuts.

### 4. Cohort caps and invariants: repaired

Every primitive search is bounded: 4,096 prime candidates, 65,536 safe-prime
candidates, and 4,096 consecutive-prime candidates.  A complete row has 64
bounded attempts.  Equality, wrong bit length, imbalance, capacity failure,
safe-prime failure, and duplication all reject the attempt.  Exhaustion
aborts instead of changing the row or cohort.

Production calls the same acceptance predicate for every path.  Safe-safe
rows recheck both Sophie Germain halves and common capacity two.  Consecutive
rows require the bounded next prime to retain the declared bit length.  One
set enforces modulus uniqueness across all sizes and cohort types within a
phase.  The source derives and enforces exactly 848 discovery rows and 1,152
held-out rows; disjoint factor-bit ranges make the two phases disjoint.

### 5. Selection, lead, output, and resource gates: repaired

Discovery ranks all 148 fixed syntaxes by hostile proper hits, all proper
hits, hit sizes, and syntax, then writes exactly 64 canonical rows.  The
runner hashes the exact bytes.  Held-out mode validates that SHA-256 before
symbolic work or row construction, then checks the exact header, final
newline, field count, canonical decimal fields, ranks, ranges, known unique
names, row count, and registered order.  It evaluates all 148 candidates and
does not rerank.

Held-out mode implements all four finite lead conditions directly.  Proper
hits, hostile coverage, size coverage including 56 or 60, non-direct support,
and mapping to an authenticated operational target are computed from retained
row witnesses and symbolic metadata.  The lead file contains 64 rows plus its
header, and the final pass bit is the conjunction of the four gates.

The executable refuses phase-file overwrites and applies the aggregate 1 GiB
budget before each write.  The runner additionally applies a 1 GiB file-size
limit, a 4 GiB virtual-memory limit, at most eight low-priority threads, one
shared four-hour discovery/held-out deadline, exact output-set checks,
nonempty-file checks, the 64-row lead check, overlap checks before compilation
and each phase, and a final aggregate-size check.  Both shell scripts pass
`bash -n`.

## Target validation and resource audit

The authenticated target compile has empty stdout and stderr.  The exact
self-test completed with status zero in 1.972386473 seconds and 32,120 KiB
peak process-tree RSS.  The exact synthetic benchmark completed with status
zero in 5.031588949 seconds and 32,024 KiB peak RSS.  Its output is:

```text
BENCHMARK_PASS seconds=4.995265 modulus_bits=120 blocks=390 leaf_touches=926880 candidates=148 symbolic_columns=70 symbolic_relations=14 shortcuts=0 projected_rows=2000
```

Charging the maximum-size benchmark to all 2,000 rows and then applying the
registered factor eight gives 166.5 minutes.  The documented factor-four
memory margin remains below 1.6 GiB.  These conservative projections fit the
four-hour and 4 GiB production caps.

The benchmark is explicitly synthetic.  Its literal second nominal factor,
`2^60-33`, is composite.  This is not a blocker because the benchmark is used
only to authenticate the public 120-bit query bank and its resource cost; it
must not be cited as a promised-semiprime algebra test.  The exact parity,
cleanup, and singular-index algebra is instead exercised on distinct-prime
self-test fixtures and agrees with `V2_ALGEBRA.md`.

## Evidence boundary

This audit used hash checks, static source and runner reconstruction, small
exact arithmetic checks, and a read-only target hash check.  It did not run,
open, or hash a discovery or held-out cohort.  It did not edit a frozen input
or a durable ledger.  A production launch must still wait until no forbidden
F258-D01 through F263-D01 process is active and the live host resource check
passes.
