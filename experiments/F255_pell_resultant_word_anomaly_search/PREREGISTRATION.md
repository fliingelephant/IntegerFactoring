# F255-D01 preregistration — Pell/resultant/carry word anomaly search

## Purpose

This is a discovery computation.  It tests whether a fixed public Pell bank
produces an anomalously strong unfactored word for the P205 Miller splitter.
It is not proof evidence for an all-input probability bound.

For a labelled semiprime `N=pq`, put

\[
d=\gcd(p-1,q-1),\qquad s_p=(p-1)/d,\qquad s_q=(q-1)/d.
\]

The hidden factors are used only to score the public words.  They are not
used by the row, edge, carry, or word generators.

For every public base product `V`, the tested word is

\[
W=V^n,\qquad n=\operatorname{bitlength}(N),
\]

and its exact P205 quality is

\[
H_N(W)=\max\left\{
 {\gcd(s_p,W)\over s_p},
 {\gcd(s_q,W)\over s_q}
\right\}
={1\over\min(r_p(W),r_q(W))}.
\]

The corresponding proved one-trial factor probability is at least
`H_N(W)/2`.  The computation evaluates each public product modulo `s_p`
and `s_q`; this is exactly equivalent to materializing `W` for the gcd, but
does not make factor-dependent choices.

## Frozen public Pell bank

Use exactly

```text
D = 2,3,5,6,7,10,11,13
1 <= j <= 4*n
```

For each `D`, let

\[
(S_1+T_1\sqrt D)^j=S_j+T_j\sqrt D,
\]

where `(S_1,T_1)` is the least positive norm-one Pell solution.  Define

\[
k_j=\lfloor T_j/N\rfloor,\quad y_j=T_j-k_jN,
\quad a_j=1+Dy_j^2.
\]

Only post-wrap rows `k_j>0` are admitted.

For two rows `i,j`, use the exact public resultant

\[
R_{ij}=
[D_iD_j\Delta^2+D_jk_j^2+D_ik_i^2]^2
-4D_iD_jk_i^2k_j^2,
\qquad
\Delta=T_i k_j-T_j k_i.
\]

The following public edge menus are frozen.

1. Same-`D` index offsets `1,2,3,5,8,13`.
2. Same-`D` odd multiples `(j,3j)` and `(j,5j)` when both rows exist.
3. Cross-`D` pairs at the same index, for every pair in the frozen `D`
   menu.
4. Four deterministic hash partners per retained row.  The hash uses only
   `N`, the public row number, and the partner number.

For same-`D` edges, also retain the two exact factors

\[
M^-_{ij}=D\Delta^2+(k_i-k_j)^2,qquad
M^+_{ij}=D\Delta^2+(k_i+k_j)^2.
\]

For odd multiples, define the canonical-wrap carries

\[
F_{3,D}(y)=y(3+4Dy^2),
\]

\[
F_{5,D}(y)=y(5+20Dy^2+16D^2y^4),
\]

\[
c_{h,j}={F_{h,D}(y_j)-y_{hj}\over N}\ge0,qquad h\in\{3,5\}.
\]

When `c>0`, the carry factor is

\[
C_{h,j}=D c_{h,j}(2y_{hj}+c_{h,j}N).
\]

When `c=0`, insert the neutral factor `1`, not zero.

## Frozen candidate words

Every base product below includes `N-1`.

```text
baseline       N-1
rows           (N-1) * product a_i
same_res       (N-1) * product R_ij over same-D offset and odd edges
cross_res      (N-1) * product R_ij over cross-D same-index edges
hash_res       (N-1) * product R_ij over deterministic hash edges
norm_minus     (N-1) * product M^-_ij over same-D edges
norm_plus      (N-1) * product M^+_ij over same-D edges
carry3         (N-1) * product C_3,j
carry5         (N-1) * product C_5,j
combined       product of every preceding non-baseline public factor,
               with one leading factor N-1
```

Repeated public factors are allowed.  They can only increase valuations.
The fixed discriminant menu, `O(n)` rows, and `O(n)` frozen edges, each with
`O(n)`-bit coordinates, give every materialized candidate word
`O(n^3)` bits after the final power `n`.  The implementation must not use
factorization of a word.

## Frozen cohorts

Factor bit sizes:

```text
12,16,20,24,28,32,40,48,56,60
```

For every factor bit size, generate the following disjoint deterministic
cohorts.

```text
random balanced semiprimes: 4096
safe-safe balanced semiprimes: 128 at 12 bits, 1024 at every other size
```

Random balanced means distinct odd primes `p<q<2p` with the declared factor
bit length.  Safe-safe means `p=2r+1`, `q=2s+1`, where all four numbers are
prime, again with `p<q<2p`.  Cohort generation uses fixed SHA-independent
64-bit seeds encoded in the source.  Duplicate `N` values within a cohort
are rejected.  The source generator is identical for every candidate word.

The reduced 12-bit safe cohort is necessary because that interval contains
only 23 safe primes and 253 distinct balanced safe-safe pairs.  All generated
`N` values are unique within their cohort.

Total planned rows: `50,304` labelled semiprimes.

## Frozen outputs and interpretation

For every bit size, cohort, and word report:

- count;
- arithmetic mean of `H_N`;
- median, 90th, and 99th percentiles of `-log2(H_N)`;
- worst `H_N` and its exact `(p,q,N,gcd_p,gcd_q)` witness;
- count with strict improvement over `baseline`;
- count with one residual fully saturated.

Also report global totals and elapsed time.  Preserve a TSV containing one
row per input and all ten exact gcd pairs so that alternative summaries do
not require rerunning the search.

Interpretation is frozen as follows.

- A candidate is a useful finite lead only if its worst-cohort
  `-log2(H_N)` grows visibly slower than the factor bit size on both random
  and safe-safe cohorts, and the gain survives larger held sizes.
- Linear growth on safe-safe inputs is a finite null for this fixed word
  grammar.
- A single strict improvement is an anomaly to explain, not evidence of an
  inverse-QP theorem.
- No empirical result proves or refutes an all-input asymptotic claim.

## Workflow and resource envelope

Remote host alias: `seetacloud`.

Observed before freeze:

```text
32 visible CPUs
503 GiB RAM, 367 GiB available
22 GiB free disk
load average about 56.5
visible container processes essentially idle
available arithmetic compiler: /usr/bin/g++
no Python or Sage executable in PATH
```

Use one low-priority process with at most 16 worker threads, peak memory
below 4 GiB, and a four-hour outer timeout.  The exact command will compile
the frozen C++17 source, then execute it once.  A compile/invariant smoke
with the source's `--self-test` mode is permitted before the mathematical
run; it emits no cohort score.  Do not change the cohort, word menu, or
interpretation after inspecting output.
