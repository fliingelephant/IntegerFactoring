# F259-D01 preregistration — full Pell-lift symbolic grammar search

## Purpose

This is an independent finite C++17 discovery search for public integer invariants
in the live Pell/resultant/carry core. It extends F255 in three material ways:

1. it uses both full lift quotients `ell=(S-x)/N` and `k=(T-y)/N`;
2. it searches tangent defects and exact multiplication carries;
3. it searches low-degree determinant, resultant, and second-carry atoms,
   followed by every degree-at-most-two product of frozen atom families.

The hidden prime labels are used only to verify proper gcds and to score P205
residual capture. They are never inputs to the Pell source, grammar, cleanup,
candidate choice, or word construction. Finite output is guidance only.

## Frozen public source

Use exactly

```text
D = 2,3,5,6,7,10,11,13
1 <= j <= 4*bitlength(N)
```

For each `D`, generate powers of its least positive norm-one Pell unit. For
every row materialize

```text
S_j = x_j + N*ell_j,   0 <= x_j < N
T_j = y_j + N*k_j,     0 <= y_j < N.
```

Apply, in increasing index and separately for each `D`, the usual public
screens for `gcd(D,N)`, nonunit supplied roots, exact-square row values, and
repeated `y` coordinates. Retain distinct nonsquare rows with `k>0`.

The same-`D` edge candidate universe is the deduplicated union of

```text
(j,j+o), o in 1,2,3,5,8,13
(j,3j), (j,5j)
```

when both endpoints are retained and `i+j` stays in the frozen window. Give
each candidate a SplitMix64 priority derived only from `N,D,i,j` and the
fixed source constant. Retain the 256 smallest-priority edges per `D`, or
all candidates when fewer exist. The
cross-`D` edge set contains every pair of retained rows at the same index.
The triple candidate patterns are

```text
(j,j+1,j+2), (j,j+2,j+5), (j,2j,3j)
```

when all three same-`D` rows are retained and `i+j+k` stays in the window.
Give them a separate public SplitMix64 priority and retain the 64 smallest
per `D`, or all candidates when fewer exist. These caps make the broad
grammar resource-safe without using hidden labels. Odd carry compositions use
`h,r in {3,5}` with `r*h*j` inside the same window.

## Direct screens before P205 scoring

Every generated atom is first replaced by the public `N`-primitive value
from `ALGEBRA.md`. Zero and units are counted and skipped. Compute its gcd
with `N`. A proper gcd is an exact factor certificate. The frozen row
features `ell,k,g_minus,g_plus,norm_digit` are also tested on every frozen
same-`D` edge through both differences and sums.

Thus direct gcd and collision laws are exhausted for this grammar before a
word is interpreted as a screen-free P205 lead. P205 scores are still
recorded on every input, but the strict summaries use only inputs with no
cleanup or grammar gcd factor.

## Frozen static atom grammar

The 22 base families are:

```text
row_ell                 ell
row_k_control           k
row_tangent_minus       g_minus
row_tangent_plus        g_plus
row_norm_defects        norm_digit and ell^2-D*k^2
original_q_minus        D*Delta(y,k)^2+(k_i-k_j)^2
original_q_plus         D*Delta(y,k)^2+(k_i+k_j)^2
multiplication_carry    a_ij and b_ij
carry_norm_minus        a_ij^2-D*b_ij^2
carry_norm_plus         a_ij^2+D*b_ij^2
lift_determinants       det((ell_i,k_i),(ell_j,k_j))
vector_determinants     all pair determinants among
                        (ell_i,k_i),(ell_j,k_j),(a,b),
                        (g_i_minus,g_i_plus),(g_j_minus,g_j_plus)
lift_resultant_minus    D*det(lift_i,lift_j)^2+(k_i-k_j)^2
lift_resultant_plus     D*det(lift_i,lift_j)^2+(k_i+k_j)^2
carry_resultants        both signed same-D resultant factors between
                        (a,b) and each endpoint lift/tangent vector
cross_lift_resultants   full quadratic resultants for same-index,
                        cross-D lift and tangent vectors
collision_minus         differences of ell,k,g_minus,g_plus,norm_digit
collision_plus          sums of the same five row features
triple_determinants     the four 3x3 feature determinants from columns
                        ell,k,g_minus,g_plus; four affine two-feature
                        determinants; and the affine determinant of the
                        three pair-carry vectors
first_carry_control     D*c*(2*z+c*N), h in {3,5}
second_carry_full       E_(r|h,j), r,h in {3,5}
second_carry_core       3*z+c*N for r=3; B_(5|h,j) for r=5;
                        and the sum and difference of the two orderings
                        for the target multiplier 15
```

All determinants use the ordinary alternating determinant. The exact
resultant and curvature formulas are frozen in `ALGEBRA.md`. Every atom has
bit length polynomial in `bitlength(N)` because the discriminant, multiplier,
and index windows are fixed or linear.

The implementation records these atoms as a typed expression-template DAG. Scalar
leaves carry their row, pair, triple, or composition scope. Pair-valued
leaves carry one of the types `residue`, `lift`, `tangent`, or
`multiplication_carry`. Admitted nodes use negation, sum, difference,
product, determinant, the signed norm `u^2 +/- D*v^2`, the quadratic
resultant template, finite difference, and the two exact quotient nodes
`exact_div_N` and `exact_div_N2`. A quotient node aborts unless its exact
divisibility assertion holds. The 22 named families are the exhaustive
static layer induced by the frozen sparse row, edge, triple, and composition
scopes. Each family has one normalized syntax string. The source aborts if
two family templates have the same normalized syntax. Edge and triple scope
sets are deduplicated before evaluation. Distinct scopes remain distinct
atoms even when they happen to take the same integer value. Exact zero
identities and public `N` powers are reported as decoys and are not inserted
as word factors. The modular-nullspace layer below supplies independent
public-evaluation canonicalization for synthesized identities.

## Frozen symbolic identity-mining layer

Before any semiprime score, build 96 public synthetic Pell instances. Use
the public odd moduli `1000003+2*t`, the eight frozen discriminants, and the
index triples encoded in `symbolic_search.cpp`. These moduli need not be
prime or semiprime. They contain no hidden labels.

For every triple use the 16 scalar monomials of degree at most two that
appear in the two coordinates of

```text
c_(i+j,k) + c_(i,j)*r_k - c_(i,j+k) - r_i*c_(j,k),
```

where `r=x+y*sqrt(D)` and `c=(r_i*r_j-r_(i+j))/N`. Form their evaluation
matrix modulo the fixed public prime `1000000007`. Compute RREF and a basis
of its modular nullspace. Reconstruct only coefficient vectors in
`{-1,0,1}`. Authenticate each candidate by exact zero evaluation on 64
disjoint public synthetic instances with moduli `2000003+2*t`.

The known control is the associativity cocycle identity

```text
c_(i+j,k)+c_(i,j)*r_k=c_(i,j+k)+r_i*c_(j,k).
```

The source must recover rank 14 and rediscover both scalar coordinates or
abort. Those two controls then span the full modular nullspace. The two
authenticated global-zero identities are canonicalized as decoys and do not
become word factors. Thus this frozen 16-monomial basis has no other identity
or primitive quotient survivor. This bounded layer is exhaustive for that
basis; it is not a claim about unrestricted symbolic search.

This layer is deliberately public and pre-score. It is not a beam trained
on hidden factors. The discovery semiprimes rank the surviving 255 public
words by description length, direct-gcd count, and P205 residual score for
reporting only. No ranking changes the survivor set opened on held-out
inputs. Thus a ranking miss is distinguishable from a static-grammar null.

## Frozen word grammar and P205 score

For labelled `N=pq`, put

```text
d=gcd(p-1,q-1), s_p=(p-1)/d, s_q=(q-1)/d.
```

Within each base family multiply all nonneutral `N`-primitive atoms. The
frozen public base products are:

1. `N-1` alone;
2. `(N-1)` times each one of the 22 family products;
3. `(N-1)` times every unordered product of two distinct family products;
4. `(N-1)` times the product of all 22 families.

There are exactly `1+22+C(22,2)+1 = 255` words. For each base `V`, use
`W=V^n`, where `n=bitlength(N)`, and score

\[
H_N(W)=\max\left\{{\gcd(s_p,W)\over s_p},
{\gcd(s_q,W)\over s_q}\right\}.
\]

Products are evaluated modulo `s_p,s_q`; this is exactly equivalent for the
gcd and does not affect the public grammar.

## Frozen cohorts

Factor bit sizes and split:

```text
discovery: 16,24,32
held-out:  40,48,56,60
```

At each size generate disjoint deterministic balanced cohorts:

```text
random prime pairs:      512
consecutive prime pairs: 256
safe-safe prime pairs:   256 (128 at 16 bits)
```

All factors have the declared bit length and satisfy `p<q<2p`. Safe-safe
means `p=2r+1,q=2s+1` with all four numbers prime. Generation uses the fixed
SplitMix64 seeds derived from the fixed constant encoded in
`symbolic_search.cpp`; duplicate moduli across all cohorts
at one size are rejected. Total planned inputs: `7,040`.

The safe-safe cohorts are the hostile cohorts for the P205 interpretation.
No grammar or threshold may change after any discovery score is inspected.

## Frozen outputs and interpretation

Preserve one gzip TSV row for every input. Preserve atom counts, direct gcd
counts, first certificates, and all 255 exact residual gcd pairs. Aggregate
by split, factor size, and cohort. For every word report count, arithmetic
mean `H`, median/90th/99th percentile of `-log2(H)`, strict improvement over
baseline, and residual saturation.

Interpretation:

- Any proper direct gcd on a screen-free held-out input is an exact anomaly.
- A direct family is a strong finite lead only if it has at least 16 strict
  held-out hits across at least three held-out sizes, including safe-safe.
- A word is a strong finite lead only if its safe-safe median
  `-log2(H)` grows visibly slower than factor size at all four held-out sizes
  and the improvement is also present on random inputs.
- Linear safe-safe growth is a finite null for this fixed grammar.
- One improvement is an anomaly to explain, not an inverse-QP theorem.
- No finite rate proves or refutes an all-input asymptotic claim.

## Frozen resource envelope and incompatibility

Remote alias: `seetacloud`. Read-only inspection at
`2026-08-13T13:28:30Z` and `2026-08-13T13:42:33Z` observed:

```text
128 configured logical CPUs; 32 allowed CPUs (96-127)
load average 65.28,60.96,59.39
503 GiB RAM; 367 GiB available; no swap
22 GiB free disk
F258-D01 active under nice 15
```

F259 is declared incompatible with F258 and must not overlap it. The runner
must refuse to start if the F258 mathematical process is present.

After F258 completes, compile with `/usr/bin/g++ -std=c++17 -O3 -DNDEBUG
-pthread`; use at most eight threads, `nice -n 15`, a 4 GiB virtual-memory
limit, and a four-hour hard timeout. Expected peak RSS is below 512 MiB. Based
on the frozen `7,040` inputs, eight discriminants, at most `4n` rows per
discriminant, the frozen scope caps, and 255 modular words, the conservative
runtime estimate is 1.2–3 hours on eight allowed low-priority CPUs. The exact
projected work is 7,040 input evaluations, at most 3,840 materialized rows,
2,048 retained pair scopes, 512 retained triple scopes, and about 176,384
static atom insertions per largest input. This gives an upper projection of
about 1.25 billion atom insertions and exactly 1,795,200 word-input scores,
plus the fixed `96+64` synthetic identity cases.

The pre-freeze maximum-size public synthetic benchmark materialized a
120-bit modulus and 123,481 nonneutral atoms. Three target-host timings were
4.936830, 4.267517, and 4.953039 seconds at `nice -n 15`; the last measured
peak RSS as 16,136 KiB. Linear extrapolation gives 72.6 minutes at perfect
eight-thread scaling. The declared 1.2–3 hour envelope allows for imperfect
scaling and shared-host load. Eight worker states plus the dense result remain
well below 512 MiB. The dense in-memory result is
about 40 MiB. The uncompressed TSV upper estimate is 80 MiB and the expected
gzip output is below 20 MiB; in all cases the experiment must abort if its
own output exceeds 1 GiB. This is well below the 22 GiB observed free disk.
Abort rather than change
the host, source, cohort, grammar, limits, or interpretation.
