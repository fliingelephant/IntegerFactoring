# F263-D01 preregistration — hypergeometric block evaluator search

## Purpose

F263-D01 is a freeze-first C++17 symbolic and numerical search for a new
evaluator or singular-block locator for the balanced beta-two central-binomial
gate.  It does not run a characteristic-size coefficient or factorial scan.

The primary question is precise:

> Does a dyadic hypergeometric block admit a public, low-description
> composition state whose construction and merge dependency cone are
> numerical-quasipolynomial, and whose public gcd, minor, resultant, Smith
> divisor, or randomized projection localizes the unique hidden nonunit?

The full product tree is retained only as an oracle control.  Logarithmic
tree depth is not counted as a speedup when the tree still has `Theta(B)`
leaves.

This is finite discovery.  A positive pattern must be proved symbolically
before it can support an algorithm.  A null is not a circuit lower bound.

## Prior boundary and material difference

P171/P173/P174/P175 and P215 isolate the remote coefficient, quotient carry,
factorial, quarter-bit terminal, and shifted threshold.  P21 and P34 show
that literal product trees, fixed binomial lists, and meet-in-the-middle
products remain exponential.  P11/P14/P18/P24/P133 close several raw
coefficient, rank, canonical-minor, prefix, and generic local-exchange claims
in the AKS family.  F260 includes short hypergeometric ratios in a broad
integer-source grammar.

F263 does not repeat a short ratio bank.  It studies block transfer
composition itself.  It searches truncated product jets, upper-triangular
binary-splitting matrices, exact block cancellations, finite differences in
the block start, nonlinear minors/resultants, public randomized sketches,
and low-order recurrences.  Every survivor is charged for its complete
dependency cone.  This operation and cost audit are the material change.

## Frozen parity and singularity screens

The code implements both central parities exactly.

```text
B=2H:    binom(B,H)=a_H.
B=2H+1: binom(B,H)=B/(H+1)*a_H.
```

It first computes `gcd(B,N)` and `gcd(H+1,N)`.  A proper gcd is a cleanup
factor.  A gcd equal to `N` aborts the promised row.  On the unresolved odd
branch, it also screens the public multiplier `B` before treating it as a
unit.  The exact range proof and the unique central numerator and shifted
denominator locations are in `ALGEBRA.md` and are checked by `--self-test`.

## Frozen symbolic identity grammar

Before any labelled semiprime is generated, build 192 public generic affine
block instances.  Their parameters, starts, and lengths are deterministic
SplitMix64 functions of the literal source seed.  The instances contain no
hidden factors.  Use 128 instances for discovery and 64 disjoint instances
for exact authentication.

For a parent block and its two equal children, construct:

```text
U_0,U_1,U_2 and V_0,V_1,V_2;
forward and reverse upper-triangular transfers for weights 1, k+1, hash(k);
the exact reduced numerator/denominator pair on small instances;
endpoint and length monomials of total degree at most two;
all typed child products needed by degree-at-most-two merge identities.
```

Over each of the public primes `1000000007` and `1000000009`, compute the
feature-matrix rank and modular nullspace.  Search every normalized
`{-1,0,1}` relation of support at most four by a meet-in-the-middle signed
column-sum table.  Also try to rescale each nullspace basis vector to a
primitive integer vector with coefficients of absolute value at most 4096.

Every candidate is then evaluated as an exact integer identity on all 64
disjoint authentication instances.  A modular-only survivor is rejected.
The source must recover the six jet-convolution controls and all six frozen
transfer controls.  Exact zeros and identities whose dependency cone is a
full recursive merge are canonicalized as controls, not candidates.

A relation is called a possible evaluator shortcut only if one parent target
appears with coefficient `+/-1`, every other term is descriptor or an already
operational state, and recursive expansion leaves at most
`2^O((log n)^c)` source nodes.  The frozen grammar is expected to find zero
such shortcuts.  A nonzero count is an anomaly to inspect, not a proved
algorithm.

## Frozen recurrence search

The recurrence miner has two parts.

1. For consecutive block starts, search order `0..3` and polynomial
   coefficient degree `0..3`.  It must rediscover the generic affine law
   `(alpha*l+beta)P(l+1,m)=(alpha*(l+m)+beta)P(l,m)` for the central
   numerator, central denominator, shifted numerator, and shifted
   denominator.  These are controls and are tagged `short_scan` or
   `full_scan` according to the initial block.
2. For the dyadic-length sequence `P(l,2^j)`, search the same order and
   degree limits with coefficient height at most 4096.  Discovery uses one
   public prime and public starts.  Every recurrence must pass different
   starts, both affine families, a second public prime, and exact small-
   integer tests.  No recurrence may be inferred from a fitted curve alone.

The miner reports each accepted recurrence, its order, degree, coefficient
height, and dependency class.

## Frozen public numerical query bank

For an odd public `N`, put `n=bitlength(N)`,
`B=floor(sqrt(N))`, and `H=floor(B/2)`.  The two block families are:

```text
central: k in [0,H),       u_k=4k+2,       v_k=k+1;
shifted: c in [1,H),       u_c=N+c,        v_c=N+c-B.
```

Use every distinct block length in

```text
8,16,32,... <= min(n^2,domain_length), n, n^2,
```

clipped to the public domain.  For each length query the left, right, middle,
and quarter blocks, plus four deterministic public hash blocks.  Duplicate
blocks are removed.  An adjacent-start state is constructed only when it is
inside the domain.  At each length, pair the lexicographically first state
with every other queried state for cross-block invariants.

Every state scans at most `n^2` factors.  The number of states is
`O(n log n)`, so the complete query bank is polynomial in `n`.  The program
records the exact number of block queries and leaf touches.  It never scans
the full `H`-term gate on a cohort row.

## Frozen candidate grammar

For each family and every public queried block, test:

```text
six order-2 jet entries;
three jet 2x2 minors and the quadratic Sylvester resultant;
six forward/reverse transfer off-diagonal entries;
three transfer cross determinants;
16 public linear projections;
eight public multiplicative block hashes;
six adjacent-start finite differences;
six adjacent-state jet minors;
two adjacent-state resultants;
the first two Smith-style determinantal divisors.
```

For each frozen cross-block pair, test eight projection differences, three
jet determinants, three transfer determinants, and one combined quadratic
resultant.  All syntax, seeds, signs, and tie orders are literal constants in
`symbolic_search.cpp`.  Every expression is evaluated over `Z/NZ` before a
gcd with `N`.  No local field or hidden factor participates in evaluation.

The non-operational controls are:

```text
full central root product;
full shifted denominator product;
full product-tree preprocessing;
binary singular-child search with oracle block values;
recomputation of each queried oracle block.
```

The code reports their exact symbolic costs and label-assisted coverage.  It
does not materialize them on large rows and never ranks them with candidates.

## Frozen labelled cohorts

All factors have the declared exact bit length and satisfy `p<q<2p`.
Generation is deterministic with the SplitMix64 seeds in the source.
Duplicate `N` values within a run are rejected.  Labels are passed only to
the verifier after the public query bank has been fixed and evaluated.

```text
discovery factor bits: 16,24,32
held-out factor bits:  40,48,56,60

per size:
random balanced pairs:                  128
consecutive-prime balanced pairs:        64
safe-safe pairs:                         32 (16 at 16 bits)
bounded common capacity gcd(p-1,q-1)<=16:64
```

Safe-safe means that `p`, `q`, `(p-1)/2`, and `(q-1)/2` are all prime, so
the common capacity is exactly two.  Safe-safe and bounded-capacity rows are
the hostile cohorts.  The generator has a frozen per-row attempt cap and
aborts instead of replacing a cohort.

## Frozen scoring and holdout gate

For every row preserve:

```text
public cleanup result and parity;
query and leaf-touch counts;
whether the public bank covers the true central or shifted singular index;
candidate proper-gcd and saturated-gcd bitsets;
the first exact candidate certificate;
the hidden common capacity, used only as a verifier label.
```

Discovery ranks the fixed candidates by:

1. more proper-gcd rows in safe-safe and bounded-capacity cohorts;
2. more proper-gcd rows overall;
3. more factor sizes with a hit;
4. normalized syntax.

The first 64 candidates are written to a hashed selection file.  Held-out
mode accepts only that exact file and does not rerank.  The executable still
evaluates the complete frozen bank so that a ranking miss is distinct from a
grammar null.

A finite useful lead must satisfy all of these conditions:

1. at least 16 held-out proper-gcd rows;
2. hits at three held-out sizes, including 56 or 60 and a hostile cohort;
3. a success mechanism not equal to direct inclusion of the labelled
   singular index in a queried short block;
4. an authenticated symbolic identity or recurrence that reduces the full
   dependency cone to numerical-QP size.

No finite rate is an inverse-QP theorem.

## Frozen output

Discovery writes:

```text
output/F263-D01.discovery.rows.tsv
output/F263-D01.discovery.summary.json
output/F263-D01.selection.tsv
```

Held-out writes analogous `heldout` files.  Rows contain compact hexadecimal
candidate bitsets, not dense per-block traces.  Total uncompressed output
must remain below 1 GiB.

## Frozen resource and workflow envelope

Implementation: C++17 with Boost.Multiprecision.  Production uses at most
eight threads.  The runner applies `nice 15`, a four-hour timeout, a 4 GiB
virtual-memory cap, and a 1 GiB output cap.

F263-D01 is incompatible with every F258-D01 through F262-D01 production
run.  `remote_run.sh` checks for them before compilation and immediately
before each cohort phase.  `--self-test` and `--benchmark` do not generate or
open the frozen cohorts.

Before freeze, the exact target source must compile, pass `--self-test`, and
complete the public synthetic benchmark on `seetacloud`.  Resource state,
runtime, peak RSS, projected cohort cost, source hashes, and every failed
pre-freeze attempt are retained.  If the projection exceeds the declared
limits, the packet must be revised and benchmarked again before any cohort is
opened.

This packet freezes design, algebra, source, runner, self-test, benchmark,
and hashes.  It does not launch discovery or held-out cohorts and does not
edit `REGISTRY.md`, `FAILED.md`, `PROVED.md`, or `notes/Progress.md`.
