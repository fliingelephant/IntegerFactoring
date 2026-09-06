# F259-D02 preregistration — full Pell-lift symbolic grammar search V2

## Purpose

This is an immutable C++17 repair packet for the finite F259 search. V1
(`F259-D01`) and its hostile audit remain byte-for-byte unchanged. V1 failed
pre-run review and must never be launched. V2 retains the public source,
cohorts, sparse scopes, 22 family names, and 255 word shapes. It repairs the
zero-carry semantics, cocycle basis, certificates, reporting, firewalls, and
runner gates before any cohort is opened.

The search investigates public integer invariants in the live
Pell/resultant/carry core. It extends F255 in three material ways:

1. it uses both full lift quotients `ell=(S-x)/N` and `k=(T-y)/N`;
2. it searches tangent defects and exact multiplication carries;
3. it searches low-degree determinant, resultant, and second-carry atoms,
   followed by every degree-at-most-two product of frozen atom families.

The hidden prime labels are used only to label proper gcd outcomes and to score P205
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
recorded on every input. `cleanup_free` means that no source-screen factor was
found. `strict` is reserved for P205 rows with neither a source-screen factor
nor a grammar-atom factor. A direct-family hit is called screen-free when its
input is `cleanup_free`; it cannot also be a strict P205 row by definition.

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
first_carry_control     D*c*(2*z+c*N), h in {3,5}; zero stays zero
second_carry_full       E_(r|h,j), r,h in {3,5}
second_carry_core       3*z+c*N for r=3; B_(5|h,j) for r=5;
                        and the sum and difference of the two orderings
                        for the target multiplier 15; all remain defined
                        and are inserted when c=0
```

All determinants use the ordinary alternating determinant. The exact
resultant and curvature formulas are frozen in `ALGEBRA.md`. Every atom has
bit length polynomial in `bitlength(N)` because the discriminant, multiplier,
and index windows are fixed or linear.

The implementation uses 22 hard-coded exact family constructors. It records
one normalized schema string per family and aborts if family names or schema
strings collide. This is a static typed table, not a general expression DAG.
Edge and triple scope sets are deduplicated before evaluation. Distinct scopes
remain distinct atoms even when they have the same integer value. Every
explicit `N` or `N^2` quotient aborts unless exact divisibility holds. Exact
zeros, resulting units, and the count of stripped public `N` powers are
reported per family and are not inserted as word factors. No other content is
removed.

## Frozen symbolic identity-mining layer

Before any semiprime score, build 96 public synthetic Pell instances. Use
the public odd moduli `1000003+2*t`, the eight frozen discriminants, and the
index triples encoded in `symbolic_search.cpp`. These moduli need not be
prime or semiprime. They contain no hidden labels.

For every triple use exactly the twelve additive scalar terms that appear in
the two coordinates of

```text
c_(i+j,k) + c_(i,j)*r_k - c_(i,j+k) - r_i*c_(j,k),
```

where `r=x+y*sqrt(D)` and `c=(r_i*r_j-r_(i+j))/N`. The ordered real terms are

```text
a_(i+j,k), a_ij*x_k, D*b_ij*y_k,
-a_(i,j+k), -x_i*a_jk, -D*y_i*b_jk.
```

The ordered imaginary terms are

```text
b_(i+j,k), a_ij*y_k, b_ij*x_k,
-b_(i,j+k), -x_i*b_jk, -y_i*a_jk.
```

No product of two carry coordinates is admitted. Form the 96-by-12
evaluation matrix modulo the fixed public prime `1000000007`. Compute its
rank. Exhaustively enumerate all `3^12` coefficient vectors in
`{-1,0,1}^12`, discard zero, and normalize sign by making the first nonzero
coefficient positive. Authenticate every modular null vector by exact zero
evaluation on 64 disjoint public synthetic instances. Holdout modulus `t` is
exactly `2000003+2*t` for `0<=t<64`; its index schedule uses source indices
`96+t`.

The known control is the associativity cocycle identity

```text
c_(i+j,k)+c_(i,j)*r_k=c_(i,j+k)+r_i*c_(j,k).
```

The source must recover rank 10 and nullity two or abort. The normalized
ternary null list must be exactly the real identity, the imaginary identity,
their sum, and their difference. The two disjoint-support coordinate
identities are the primitive basis; the other two are aliases in their span.
All four are authenticated global-zero decoys and none becomes a word factor.
Thus this frozen 12-term basis has no other ternary identity. This bounded
layer is exhaustive only for that coefficient alphabet and basis.

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
at one size are rejected. Every prime, safe-prime, and cohort retry loop has a
frozen one-million-attempt failure bound. Exhaustion aborts the packet rather
than changing a seed or cohort. Total planned inputs: `7,040`.

The safe-safe cohorts are the hostile cohorts for the P205 interpretation.
No grammar or threshold may change after any discovery score is inspected.

## Frozen outputs and interpretation

Preserve one gzip TSV row for every input. Use cohort labels `random`,
`consecutive`, and `safe-safe`. Preserve atom, zero, unit, stripped-`N`-power,
and direct-gcd counts; `cleanup_free`; `strict`; the first exact certificate;
and all 255 exact residual gcd pairs. Every positive `cleanup_events` count
must have a nonempty first certificate containing its proper divisor and
public scope. A cleanup certificate takes priority over an earlier grammar
certificate on the same input. Thus every cleanup-free direct hit retains a
grammar certificate, while every non-cleanup-free input retains its first
cleanup certificate. Aggregate family counts and direct-hit inputs by split, factor
size, and cohort. For every word report count, arithmetic mean `H`,
median/90th/99th percentile of `-log2(H)`, strict improvement over baseline,
and residual saturation. Discovery description length is the byte length of
the frozen normalized word syntax assembled from `FAMILY_SCHEMAS`; it is not
the display-name length. Ranking is reporting only.

Interpretation:

- Any proper direct gcd on a cleanup-free held-out input is an exact anomaly.
- A direct family is a strong finite lead only if it has at least 16
  cleanup-free held-out input hits across at least three held-out sizes,
  including safe-safe.
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

F259-D02 is incompatible with every F258, F260, F261, F263, and F264
mathematical or validation process. The runner inspects `/proc/PID/cmdline`,
`/proc/PID/cwd`, and `/proc/PID/exe`, refuses before compilation and every executable mode,
checks again afterward, and monitors throughout compilation and every mode,
including report and compression validation. Any detected overlap terminates
the active mode and invalidates the run. In
particular, no cohort may open while F258 is active.

After all incompatible processes complete, compile with
`/usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread`. Every execution of the
binary, including describe, self-test, and benchmark modes, uses `nice -n 15`,
a 4 GiB virtual-memory limit, a mode timeout, and the live overlap monitor.
The runner is one-shot: it refuses a nonempty output or log directory before
installing its manifest trap. A failed attempt cannot be resumed or silently
combined with another attempt. Before the trap is installed, it also requires
a nonempty fresh `HOSTILE_PRERUN_AUDIT.md` whose first substantive line is an
unambiguous PASS verdict. The final manifest records that audit's hash.
Production uses exactly eight threads and one shared four-hour deadline for
cohort evaluation, report validation, and compression. Before compilation,
benchmark, and production the runner requires at least eight allowed CPUs,
8 GiB available RAM, 4 GiB free disk, and one-minute load no larger than three
times the allowed CPU count. Expected peak RSS is below 512 MiB. Based
on the frozen `7,040` inputs, eight discriminants, at most `4n` rows per
discriminant, the frozen scope caps, and 255 modular words, the conservative
runtime estimate is 1.2–3 hours on eight allowed low-priority CPUs. The exact
projected work is 7,040 input evaluations, at most 3,840 materialized rows,
2,048 retained pair scopes, 512 retained triple scopes, and about 176,384
static atom insertions per largest input. This gives an upper projection of
about 1.25 billion atom insertions and exactly 1,795,200 word-input scores,
plus the fixed `96+64` synthetic identity cases.

The invalid V1 packet measured its maximum-size public synthetic input at
4.936830, 4.267517, and 4.953039 seconds. Those timings are planning evidence,
not V2 validation. V2 runs three frozen full-pipeline 120-bit benchmark
repetitions after its self-test. Production is refused unless

```text
1.75 * max_benchmark_seconds * 7040 / 8 <= 14400.
```

The static predicted uncompressed output is
`7040*65536+33554432 = 494,927,872` bytes. The runner refuses a prediction
above 1 GiB, monitors aggregate output and log bytes during every mode, checks
them again before and after compression, and includes JSON and logs in the
limit. The live gate reserves 1 MiB inside that cap for the final manifest.
A successful production must have exactly 7,040 data rows, 634 TSV
columns, the exact split/cohort counts, parseable JSON, 255 ranking rows, 462
family summaries, and 5,355 word summaries. Failed report validation
invalidates the run.

This packet is frozen before target execution. A fresh hostile pre-run audit
must pass before `remote_run.sh` may proceed; the runner enforces the audit
file and verdict gate. Abort rather than change the
host, source, cohort, grammar, limits, or interpretation.
