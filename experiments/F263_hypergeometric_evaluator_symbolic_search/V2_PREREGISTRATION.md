# F263-D02 V2 preregistration — authenticated hypergeometric block search

## Status and purpose

F263-D02 is an immutable repair of F263-D01.  It is a freeze-first C++17
symbolic and numerical search for a public evaluator or singular-block
locator for the balanced beta-two central-binomial gate.  It does not alter
or supersede any F263-D01 file.  The hostile F263-D01 pre-run audit remains
the reason that D01 must not run.

The question is:

> Does a public short-block state, an authenticated identity, or an
> authenticated dyadic recurrence locate the unique hidden nonunit with a
> complete numerical-quasipolynomial dependency DAG?

This is finite discovery.  A finite hit is not an inverse-QP theorem.  A
finite null is not a circuit lower bound.  No cohort can run until this V2
packet is frozen and an independent hostile pre-run audit passes.

## Promised algebra and cleanup

Rows satisfy

```text
N=pq, p<q<2p, p and q distinct odd primes.
B=floor(sqrt(N)), H=floor(B/2).
```

The central factors are `u_k=4k+2`, `v_k=k+1` on `0<=k<H`.  Their unique
hidden numerator nonunit is at `k=(p-1)/2`.  The shifted factors are
`u_c=N+c`, `v_c=N+c-B` on `1<=c<H`.  Their unique hidden denominator
nonunit is at `c=B-p`.  `V2_ALGEBRA.md` proves the endpoints and both
parities.

The public screens are `gcd(B,N)` and `gcd(H+1,N)`.  A proper gcd ends the
row as cleanup.  A saturated gcd is not a factor.  On the unresolved odd
branch, the public multiplier `B/(H+1)` is a unit.  The self-test checks an
even row, an odd row, and the `B=p` cleanup edge.

## Symbolic feature matrix

Before any labelled row exists, construct 128 discovery and 64 disjoint
held-back generic affine instances.  SplitMix64 and the literal source seed
determine all affine coefficients, starts, lengths, and hash weights.  Each
instance has a parent of length `2m` and two adjacent children of length
`m`.

The 70 columns are:

```text
28 public descriptor monomials of total degree at most two;
18 parent/typed-child quadratic-jet terms;
18 parent/typed-child forward and reverse transfer terms;
four exact reduced-pair controls;
two parent jet determinants.
```

Build the complete 128-by-70 matrix independently modulo the public primes
`1000000007` and `1000000009`.  Compute both ranks and both nullspaces.
Every basis vector from each nullspace is separately rescaled to a primitive
integer vector of height at most 4096 when possible.  It is retained only if
it vanishes exactly on all 128 discovery and all 64 held-back integer rows.

The sparse search is exhaustive for normalized coefficients in
`{-1,0,1}` and support at most four.  Enumerate the empty half, every signed
singleton, and every signed unordered pair.  There are exactly

```text
1 + 2*70 + 4*binom(70,2) = 9801
```

halves.  Key each half by its full 256-entry residue vector: both public
primes on every discovery row.  Store every member of each equal-vector
class.  Compare every pair in a class.  Normalize and retain only supports
two through four with coefficients `+/-1` that vanish exactly on all 192
integer rows.  No digest and no first-member shortcut is part of this
search.

The required controls are the six jet convolutions and six transfer merge
identities.  The self-test requires all 12.

## Typed dependency audit

Each symbolic column contains executable metadata:

```text
dependency class: descriptor, short_scan, recursive_merge,
                  oracle_block, or full_scan;
parent-target flag;
exact source-node count on the synthetic instance;
named dependency-DAG nodes.
```

An identity is an evaluator shortcut only if exactly one parent target has
coefficient `+1` or `-1`, every other term is `descriptor` or `short_scan`,
every term has a dependency DAG, and the expanded source-node count does not
overflow.  The grammar has constant size and each `short_scan` node costs at
most `n^2`, so this criterion gives a polynomial, hence numerical-QP, DAG.
`recursive_merge`, `oracle_block`, and `full_scan` are never silently
reclassified.  Every accepted identity is output with the target, decision,
expanded node count, and rejection reason.

## Recurrence authentication

Search order `0..3`, coefficient degree `0..3`, and primitive coefficient
height at most 4096.

For adjacent starts, run four independent controls:

```text
(alpha,beta,length) = (4,2,5), (1,1,7), (1,1009,8), (1,989,8).
```

For each search box, compute candidates from both public-prime nullspaces.
Every survivor must vanish on both modular discovery matrices and at exact
held-back starts `50..69`.  The first survivor in increasing order and
degree is retained.  It must rediscover the order-one, degree-one affine
shift law.  Its dependency is `full_scan`, because its initial block still
costs its full length.

For dyadic lengths `2^j`, one shared discovery matrix contains both affine
families `(4,2)` and `(1,1)`, public starts `1,3,7,11`, and both public
primes.  Candidates from both nullspaces must vanish in both matrices and
on exact held-back starts `2,5,13` for both families.  Report every accepted
recurrence with order, degree, height, coefficients, authentication counts,
unit-target flag, and dependency class.  It is operational only when the
highest-shift coefficient is the literal constant `+1` or `-1`; otherwise
it stays `oracle_block`.

## Public numerical query bank

For every row compute `n=bitlength(N)` from the public modulus.  Cohort
factor-bit metadata never enters the bank.  For each public domain, take
every distinct length among powers of two from eight through
`min(n^2,domain)`, plus `min(n,domain)` and `min(n^2,domain)` when at least
eight.  For each length use starts

```text
left, right, middle, quarter, and four SplitMix64 public hash starts.
```

Remove duplicates.  Build an adjacent-start state only when the adjacent
block remains in the domain.  At each length, pair the lexicographically
first state with every other state.  Every state scans at most `n^2`
factors.  Record the exact query and leaf-touch counts.  No cohort row scans
the complete characteristic-size gate.

The public benchmark is fixed at

```text
p=2^60-93, q=2^60-33, bitlength(pq)=120.
```

It must report `modulus_bits=120`.  Its query bank and its resource
projection are the same V2 bank used by production.

## Fixed numerical grammar

There are 74 candidates per family and 148 total.  Per family they are:

```text
six jet entries;
three jet minors and one quadratic Sylvester resultant;
six forward/reverse transfer off-diagonal entries;
three transfer determinants;
16 public linear projections and eight product hashes;
six adjacent finite differences;
six adjacent jet determinants and two adjacent resultants;
two Smith-style determinantal divisors;
eight paired projection differences;
three paired jet determinants, three paired transfer determinants,
and one paired resultant.
```

All arithmetic is division-free in `Z/NZ` before gcd extraction.  A proper
gcd overrides an earlier saturated gcd.  Each proper hit stores the exact
public support blocks that produced it.  Only after evaluation does the
label verifier mark a hit as direct when at least one recorded support block
contains the true singular index.  This label does not change evaluation.

## Explicit non-operational controls

V2 represents and outputs these controls but never ranks them:

```text
full central root product              full_scan
full shifted denominator product       full_scan
full product-tree preprocessing         recursive_merge
binary singular-child search            oracle_block
recomputation of each oracle child       full_scan
```

Every row records exact factor evaluations, merges, state words, oracle
calls, recomputed factors, and label-assisted coverage.  The binary path
uses the literal floor/ceiling split containing the singular index.

## Deterministic labelled cohorts

Factors have the declared exact bit length and satisfy `p<q<2p`.

```text
discovery factor bits: 16,24,32
held-out factor bits:  40,48,56,60

per size:
random balanced pairs:                   128
consecutive-prime balanced pairs:         64
safe-safe pairs:                          32 (16 at 16 bits)
bounded common capacity <=16:             64
```

Discovery has exactly 848 rows.  Held-out has exactly 1,152 rows.  The full
bank has 2,000 rows.  Factor-bit ranges make discovery and held-out moduli
disjoint.  A single set enforces distinct `N` values across every cohort and
size inside each phase, including safe-safe.

Every primitive generator is bounded.  A row has at most 64 attempts.  A
prime search has at most 4,096 candidates, a safe-prime search 65,536
candidates, and a consecutive-prime walk 4,096 odd candidates.  Exhaustion,
equality, wrong bit length, imbalance, capacity failure, or a duplicate
causes a new bounded row attempt.  Final exhaustion aborts; it never replaces
or shrinks a cohort.  Safe-safe verifies both Sophie Germain halves and
common capacity exactly two.

## Discovery selection and held-out firewall

Discovery ranks all 148 fixed candidates by:

1. hostile proper-gcd rows, descending;
2. all proper-gcd rows, descending;
3. factor sizes hit, descending;
4. syntax, ascending.

It writes exactly 64 rows with canonical decimal rank and score fields.  The
runner computes the SHA-256 of the exact selection bytes and passes it to
held-out mode.  Before symbolic work or cohort construction, held-out mode
checks that digest, the exact header, the final newline, five fields per row,
ranks `1..64`, canonical score fields, score ranges, known unique names, and
the declared ordering.  It does not rerank.  It still evaluates all 148
candidates so that selection loss is distinct from a grammar null.

## Executable finite lead gate

For each selected candidate, held-out mode writes four booleans.  A finite
lead passes only if all are true:

1. at least 16 held-out proper-gcd rows;
2. hits at least three held-out sizes, includes size 56 or 60, and includes
   a hostile row;
3. at least one proper hit is non-direct under the recorded-support test;
4. the candidate maps to a parent target of an authenticated operational
   identity or unit-target dyadic recurrence.

The final `pass` column is the conjunction.  A pass remains heuristic and
requires a proof.

## Exact output and resource gates

Discovery writes exactly:

```text
F263-D02.discovery.rows.tsv
F263-D02.discovery.summary.json
F263-D02.selection.tsv
```

Held-out adds exactly:

```text
F263-D02.heldout.rows.tsv
F263-D02.heldout.summary.json
F263-D02.heldout.lead_gate.tsv
```

The executable refuses to overwrite a phase file.  Before each write it
computes current aggregate output bytes and refuses a write that would cross
1 GiB.  The runner also applies a file-size limit, verifies the exact file
sets and nonempty files after each phase, checks 64 lead rows, and checks the
aggregate cap.

Production uses at most eight threads, `nice 15`, one shared four-hour
deadline, a 4 GiB virtual-memory cap, and a 1 GiB output cap.  It refuses any
active F258-D01 through F263-D01 production process before compilation and
before both phases.

Compile, algebra-only self-test, and one public synthetic benchmark are
validation-only operations.  They do not generate, open, or hash a cohort.
They may run at `nice 15` on one core while F258-D01 uses one low-priority
core, after resource inspection.  No F263-D02 discovery or held-out process
may overlap F258-D01 through F263-D01 production.

The packet freezes V2 algebra, protocol, source, runner, validation
provenance, prelaunch manifest, and hashes.  It launches no cohort and edits
no durable ledger.
