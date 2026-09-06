# F262-D01 preregistration — polynomial Frobenius lift symbolic search

## Purpose and prior boundary

F262-D01 is a finite C++17 discovery search for public polynomial-algebra
invariants obtained one `N`-adic digit beyond `X^N mod (f,N)`. It is
materially independent of F258–F261: it uses no Pell rows, centered integer
carries, beta-2 prefix data, or sampled common orders.

P11/P14/P18/P24 close several standard AKS coefficient, full-rank, canonical
PSC, row-matroid, and prefix selectors. P22/P56/P60 close fixed sparse scalar
principal digits and multiplicative linear-cocycle inconsistency. P132 closes
fresh uniform nonunit and generic Krylov probes and explains why a supplied
genuine glued Frobenius is factor-bearing. F262 changes all three operations:
the source is a correlated coefficient lift vector, the new quotients are
integer second carries after exact division by `N`, and the decoder searches
joint nonlinear minors/resultants/Smith indicators of typical nonzero values.
Finite results are discovery only.

## Frozen public polynomial source

Use degrees `d=2,3,4,5`. For each degree use these four monic recipes, with
missing coefficients zero:

```text
A: X^d + X + 1
B: X^d - X^(d-1) + 2X + 3
C: X^d + X^(d-1) - 2X + 5
D: X^d + c_(d,2) X^(d-1) + c_(d,1) X + c_(d,0)
```

For recipe D, each `c_(d,j)` is the centered residue in `[-8,8]` of a fixed
SplitMix64 hash of `N,d,j`; replace a zero constant coefficient by `1`.
This gives exactly 16 public base polynomials before screens.

For every surviving polynomial use the five public elements

```text
a_s = X+s,  s in {-2,-1,0,1,2}.
```

Compute every `a_s^N mod (f,N^2)` by binary polynomial exponentiation. Also
form the ten products `a_s a_t`, `s<t`, and authenticate their `N`th powers
both by direct exponentiation in self-test mode and by multiplicativity in
cohort mode. The cohort path uses the latter exact value to avoid redundant
work; the quotient formula remains the exact formula in `ALGEBRA.md`.

For every base polynomial also construct translations `f_t(X)=f(X-t)` for
`t=-2,+2` and the element `a_0=X`. Compute the conjugate source in the
self-test and public synthetic identity-mining inputs. Transport the full
residue modulo `N^2` back before digit splitting.
Any failure of exact equality aborts. Translated raw coordinates are controls,
not candidate atoms.

Gcd-screen `Res(f,f')` before any candidate use. A proper gcd is a cleanup
certificate. If the gcd equals `N`, skip that polynomial. Screen any nonunit
leading coefficient or defining resultant before a quotient or monicization.

## Frozen typed static grammar

The evaluator has scalar, vector, matrix, and polynomial types. It admits
only these nodes:

```text
scalar:  negate, add, subtract, multiply, exact_div_N,
         determinant, trace, characteristic coefficient, resultant
vector:  add, subtract, finite_difference, section_carry,
         second_section_carry, exponent_lift, Q_mult, Q_assoc
matrix:  column_window, multiplication_matrix, finite_difference
poly:    coefficient_vector, monic polynomial, derivative
```

`exact_div_N` aborts unless every exact integer coefficient is divisible.
The static family layer is exhaustive over the fixed polynomial/element,
pair, and triple scopes. Its 48 families are:

```text
 0 low_coeff_control             24 trace_C
 1 lift_coeff_C                  25 norm_C
 2 lift_delta1                   26 charpoly_C
 3 lift_delta2                   27 resultant_f_C
 4 lift_reflection_sum           28 resultant_C_pair
 5 lift_reflection_difference    29 discriminant_unit_monic_C
 6 low_lift_2minors              30 trace_delta1
 7 lift_2minors                  31 norm_delta1
 8 lift_3minors                  32 charpoly_delta1
 9 lift_window_determinants      33 trace_Qmult
10 lift_window_cofactors         34 norm_Qmult
11 section_K_control             35 charpoly_Qmult
12 section_k_digit               36 trace_Qassoc
13 section_H_second              37 norm_Qassoc
14 section_2minors               38 charpoly_Qassoc
15 assoc_exact_zero_decoy        39 mixed_trace_determinants
16 assoc_digit_residual_control  40 mixed_norm_differences
17 assoc_quotient_Q              41 mixed_resultants
18 mult_residual_control         42 coefficient_hankel_minors
19 mult_quotient_Q               43 multiplication_krylov_minors
20 mult_Q_2minors                44 smith_D1_controls
21 mult_Q_3minors                45 smith_D2_indicators
22 assoc_Q_2minors               46 translation_raw_decoy
23 assoc_Q_3minors               47 translation_canonical_control
```

Families 15, 16, 18, 46, and 47 are mandatory controls and do not enter candidate
ranking. Family 16 is retained as an `N`-multiple control; only its exact
primitive quotient in family 17 is ranked. Every scalar atom is normalized by
public `N`-primitive normalization before gcd scoring. Each normalized syntax
is fixed in `symbolic_search.cpp`.

## Frozen expression-DAG synthesis

Build one scalar summary per ranked static family by hashing all its scoped
atoms into two commutative residue-mod-`N` accumulators: a sum and a product
of `1+atom`. These are public residue candidates, not exact integer values.
For every represented full public expression `W`,
`gcd(<W>_N,N)=gcd(W,N)`, so residue evaluation preserves every factor ticket.
The exhaustive synthesis layer contains:

1. both summaries of every ranked family;
2. for every unordered summary pair: sum, absolute difference, product, and
   the alternating determinant across the sum/product channels;
3. all ordered second finite differences of three adjacent family summaries;
4. 8,192 degree-three expressions selected by the smallest fixed public hash
   of normalized syntax from the complete distinct-family triple universe;
5. 4,096 degree-four expressions selected the same way from the complete
   distinct-family quadruple universe.

Commutative children are syntax-sorted. Duplicate syntax is rejected. A second
canonicalization uses evaluations on 32 public synthetic odd moduli and two
fixed public primes. Equal fingerprints are retained as one representative
with an alias count. No factor label is available in either step. The static
layer is always reported separately, so a synthesis cap cannot hide a static
grammar null.

The candidate list is built and frozen before any discovery semiprime is
opened. Discovery scores rank candidates for reporting only. They do not
change which candidates are evaluated on held-out inputs.

## Frozen modular-nullspace identity miner

Before candidate construction, use 96 public synthetic odd moduli
`1000003+2t` and fixed degree-2 through degree-5 polynomials/elements encoded
in the source. Build the degree-at-most-two monomial matrix over the public
prime `1000000007` for:

- all `d` coordinates of the full section associator (A);
- all `d` coordinates of the principal-digit associator (B);
- all `d` coordinates of the exponent multiplicativity residual before (D);
- all `d` translation/conjugacy coordinates before and after transport.

Compute RREF and a modular nullspace basis. Reconstruct only coefficient
vectors in `{-1,0,1}` with support at most 12. Authenticate each reconstructed
identity by exact evaluation on 64 disjoint public synthetic moduli
`2000003+2t`.

The miner must rediscover and canonicalize the full associator zero, the
`N`-divisibility of the digit associator and multiplicativity residual, and
the transported translation equality. Those are decoys. Any other universal
zero or exact primitive quotient is recorded as a synthesized family only if
it passes all exact held-back synthetic tests. This mining step uses no
semiprime or hidden factor labels.

## Frozen scoring

For every exact static scalar atom `w`, compute `gcd(w,N)`. For every
synthesized residue candidate, compute the gcd of its least residue and `N`.
Either gcd strictly between `1` and `N` is an exact factor ticket. Record the
first certificate, all family counts, and candidate hit counts.

For each surviving `f`, reconstruct the hidden factor-degree partitions only
in the labelled verifier. Record whether they agree. For every candidate,
report hits and tested scopes separately on cycle-match and cycle-mismatch
polynomials. Labels never select or modify a candidate.

Discovery ranking is lexicographic:

1. proper-gcd inputs, with safe-safe inputs first;
2. cycle-mismatch conditional hit rate;
3. number of distinct factor sizes and polynomial degrees hit;
4. shorter normalized syntax;
5. syntax string.

Held-out results are reported in frozen candidate order and in the discovery
ranking, without reranking.

## Frozen cohorts

Factor bit sizes and split:

```text
discovery: 16,24,32
held-out:  40,48,56,60
```

At each size generate disjoint deterministic balanced cohorts:

```text
random prime pairs:      384
consecutive prime pairs: 192
safe-safe prime pairs:   192 (96 at 16 bits)
```

Every factor has the declared bit length and `p<q<2p`. Safe-safe means
`p=2r+1`, `q=2s+1` with all four primes. Seeds are fixed in
`symbolic_search.cpp`. Duplicate moduli across cohorts at one size are
rejected. Planned total: 5,280 inputs.

The first three sizes are discovery. The last four are unopened held-out.
The safe-safe cohorts are hostile. No grammar, cap, threshold, or
interpretation changes after a discovery score is inspected.

## Frozen outputs and interpretation

Write one compact TSV row per input. It contains cohort metadata, cleanup
counts, polynomial/cycle counts, family atom/hit counts, total candidate hits,
and the first exact certificate. Do not write a dense candidate-by-input
matrix. Write one JSON summary row per candidate with discovery and held-out
aggregates, plus exact aggregate hashes and all alias counts.

A family is a strong finite lead only if it has at least 16 held-out proper
gcd inputs across at least three held-out sizes, including safe-safe and two
polynomial degrees. A synthesized candidate must meet the same condition and
beat every constituent static family. A mismatch-only anomaly is reported but
is not a factor ticket. Linear null tails or isolated small-size hits are a
finite null for this grammar only. No finite rate proves or refutes an
inverse-quasipolynomial theorem.

## Frozen resource envelope and incompatibility

Implementation: C++17 with Boost.Multiprecision. Threads: `1..8`; production
uses 8. Hard limits: `nice 15`, `timeout 14400s`, virtual memory 4 GiB, and
uncompressed output 1 GiB. The runner predicts output from the fixed row and
candidate counts and refuses if the bound exceeds 1 GiB.

F262-D01 is incompatible with any active F258-D01, F259-D01, F260-D01, or
F261-D01 process. `remote_run.sh` checks all four before compilation and again
immediately before cohort execution. Self-test and `--benchmark` do not open
the cohorts. The mathematical cohort run is not part of this freeze.

The target benchmark, measured resource inspection, projected candidate count,
runtime, memory, and output appear in `BENCHMARK.md`. If the conservative
projection exceeds 4 hours, 4 GiB, or 1 GiB, freeze must stop and the scope
must be reduced deterministically before any cohort is opened.

## Workflow status

This packet freezes design, algebra, source, self-test, benchmark, runner, and
hashes. It does not run discovery or held-out cohorts. It edits no durable
ledger (`REGISTRY.md`, `FAILED.md`, `PROVED.md`, or `notes/Progress.md`).
