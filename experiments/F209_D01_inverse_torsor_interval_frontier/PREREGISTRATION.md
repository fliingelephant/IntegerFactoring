# F209-D01 preregistration — exact inverse-torsor interval frontier

## Status

Prelaunch candidate.  No experiment has run.  Launch requires root-agent
approval after the source, runner, preregistration, hashes, remote paths, and
resource limits below are frozen.  F209-D01 is finite discovery evidence.  It
cannot prove a quasipolynomial bound.

## Closest prior routes and material difference

F205-D01 tested a fixed bank of scalar features and decision stumps derived
from the complete factorizations of

\[
K=(N-1)/2,
\qquad
E=N-\lfloor\sqrt N\rfloor^2.
\]

Its holdout result was null for that declared feature family.  F207 then
proved that those two factorizations give

\[
M=\operatorname{lcm}(K,E),
\qquad R^2\equiv N\pmod M,
\]

and the exact inverse-unit torsor

\[
(x,y)=(Ru,Ru^{-1}),
\qquad u\in(\mathbb Z/M\mathbb Z)^\times.
\]

F207 deliberately left Archimedean orientation open.

F209-D01 differs materially from F205-D01.  It uses no trained feature,
stump, or transition bank.  It reveals the prime-power CRT components of
the exact F207 torsor one at a time.  At every prefix it constructs the
complete live branch set under a fixed Archimedean interval relaxation of
the factor equation.  It measures the actual frontier width and the exact
number of children removed by each interval test.  The experiment asks
whether CRT branch geometry collapses before its exact construction pays a
square-root-size current-node cost.

## Input promise and public data

Every dataset pair consists of distinct odd primes satisfying

\[
p<q<2p,
\qquad N=pq\equiv3\pmod4.
\]

The factors construct the promised dataset and later label the true torsor
branch.  They are never passed to the public frontier constructor.

For each public \(N\), the constructor computes

\[
B=\lfloor\sqrt N\rfloor,
\quad K=(N-1)/2,
\quad E=N-B^2,
\]

and complete factorizations of \(K\) and \(E\).  These calls simulate the
two recursively completed children in F207.  If \(\gcd(E,N)>1\), the row is
recorded as F207's public easy exit and no torsor frontier is constructed.
The primary cohort consists of the remaining rows.

For a primary row, form \(M=\operatorname{lcm}(K,E)\).  For each
\(\ell^a\parallel M\), use F207's fixed local root

\[
r_\ell\equiv
\begin{cases}
1\pmod {\ell^a},&v_\ell(K)\geq v_\ell(E),\\
B\pmod {\ell^a},&v_\ell(E)>v_\ell(K).
\end{cases}
\]

The pairwise-coprime prime powers are revealed in the fixed public order

\[
(\ell^a,\ell)\quad\hbox{in increasing lexicographic order}.
\]

Incremental CRT gives a compatible root \(R_j\) modulo the accumulated
modulus \(m_j\).  The final values are exactly F207's \(M,R\).

## Exact branch representation

The balanced promise gives the public integer intervals

\[
P=[\lfloor\sqrt{\lfloor N/2\rfloor}\rfloor+1,B],
\qquad
Q=[B+1,\lfloor\sqrt{2N-1}\rfloor].
\]

They contain the hidden \(p\) and \(q\), respectively.

At stage \(j\), every unit branch \(u\bmod m_j\) has

\[
x_u=R_ju\bmod m_j,
\qquad
y_u=R_ju^{-1}\bmod m_j.
\]

For either residue \(z\), modulus \(m_j\), and interval \([L,U]\), the
source constructs the exact odd-representative set

\[
\mathcal A(z,m_j;L,U)
=\{Z\in[L,U]\cap(2\mathbb Z+1):Z\equiv z\pmod {m_j}\}.
\]

It is empty or one arithmetic progression.  The stored tuple is exactly its
first member, last member, step \(\operatorname{lcm}(2,m_j)\), and
cardinality.  Thus a branch has an exact coefficient-box representation

\[
\mathcal P_u=\mathcal A(x_u,m_j;P),
\qquad
\mathcal Q_u=\mathcal A(y_u,m_j;Q),
\]

together with the exact unresolved equation

\[
XY=N,
\qquad (X,Y)\in\mathcal P_u\times\mathcal Q_u.
\]

The public frontier applies only these monotone necessary conditions:

1. \(\mathcal P_u\neq\varnothing\);
2. \(\mathcal Q_u\neq\varnothing\); and
3. if \(P_u^- ,P_u^+,Q_u^-,Q_u^+\) are the progression endpoints, then

   \[
   P_u^-Q_u^-\leq N\leq P_u^+Q_u^+.
   \]

The third condition is the exact intersection test between \(N\) and the
ordinary product interval of the positive rectangle.  It is not asserted to
solve the discrete product equation.  No primality test, gcd with a candidate
representative, divisibility test by a representative, hidden factor, or
target bit participates in pruning.

These tests are monotone under CRT refinement: a child progression is a
subset of its parent progression.  Therefore a pruned branch has no live
descendant under this declared relaxation.

## Exact frontier construction without enumerating the full torsor

Let the next component be \(r=\ell^a\), and let \(F_{j-1}\) be the current
frontier.  It has exactly

\[
|F_{j-1}|\varphi(r)
\]

algebraic children.  The implementation constructs exactly the children
whose \(x\)-class meets \(P\), choosing the cheaper of two exact methods:

1. **CRT expansion:** enumerate all \(\varphi(r)\) local units for every
   parent when \(|F_{j-1}|\varphi(r)\) is no larger than the number of odd
   integers in \(P\).
2. **Small-interval scan:** otherwise scan every odd \(X\in P\), discard
   \(\gcd(X,m_j)>1\), set
   \(u=X R_j^{-1}\bmod m_j\), retain it only when its reduction is in
   \(F_{j-1}\), and deduplicate it.

The second method is exact: multiplication by \(R_j^{-1}\) bijects unit
\(x\)-classes and unit \(u\)-classes, and every class meeting \(P\) is
witnessed by a scanned representative.  Modular inverses of all retained
\(x\)-classes are computed by one batch inversion.  The \(Q\)-interval and
product-interval tests are then applied to every retained branch.

For each stage the output records:

- accumulated modulus and root;
- full torsor size \(\varphi(m_j)\);
- previous frontier width and exact algebraic-child count;
- generator mode and actual generator iterations;
- widths after the \(P\), \(Q\), and product-interval tests;
- exact counts pruned by each test;
- a SHA-256 digest of every sorted live branch and its two exact progression
  tuples; and
- fixed first-eight and last-eight branch samples.

The source aborts rather than samples or truncates if the declared maximum
number of odd \(P\)-representatives is exceeded.

## Hidden labels and public decoder audit

Only after the complete public frontier is fixed, the separate label
function computes

\[
u_{p,j}=pR_j^{-1}\pmod {m_j},
\qquad
u_{q,j}=qR_j^{-1}=u_{p,j}^{-1}\pmod {m_j}.
\]

It checks that \(u_{p,j}\) survives.  It records:

- the first stage where \(u_{p,j}\neq u_{q,j}\) and the swapped orientation
  is pruned;
- the first stage whose whole public frontier has width one;
- the first stage where that unique branch has singleton \(P,Q\)
  progressions whose product is exactly \(N\); and
- whether the resulting public exact-division certificate equals the hidden
  factors.

The label function never changes a frontier or the order of a branch.  The
public singleton-product check is an audit of when the declared geometry has
already produced a verifiable factor; it is not used to prune later stages.

## Fixed datasets

The random cohorts are exact prefixes of the F205-D01 deterministic
generators, permitting paired comparison with that scalar-feature run.

- `paired_train`: 256 accepted pairs; smaller-factor bit lengths cycle from
  12 through 17; seed `20501`.
- `paired_holdout`: 64 accepted pairs; smaller-factor bit lengths cycle from
  18 through 23; seed `20502`.
- `small_exhaustive`: every accepted pair with \(p\leq1000\), using the same
  loop and acceptance predicate as F205-D01.
- `frozen_witnesses`: \((5,7),(17,31),(37,71),(53,67)\), corresponding to
  \(N=35,527,2627,3551\).

Acceptance uses only the declared promise and \(N\equiv3\pmod4\).  It does
not resample by a frontier outcome, target bit, F205 feature, or F207 easy
exit.  Easy exits remain in the output but are excluded from primary torsor
statistics.

## Fixed summaries and correlations

For every primary row, report:

- maximum live frontier width;
- maximum generator iterations paid at one stage;
- total generator iterations;
- first true-orbit orientation depth and accumulated-modulus bit length;
- first global-width-one depth;
- first verified singleton-product decode depth;
- final frontier width;
- the ratios between live width, algebraic children, and
  \(\varphi(m_j)\); and
- the smallest exact row exceeding each operational work threshold below.

The predeclared public factorization covariates are

\[
\omega(K),\ \omega(E),\ \omega(M),\
\log_2M,\ \log_2\gcd(K,E),
\]

the largest prime-power component's log fraction of \(M\), its reveal
position, the number of `K`-dominant, `E`-dominant, and tied components, and
the largest exponent in \(M\).  The predeclared outcomes are

\[
\log_2(1+\max|F_j|),
\quad
\log_2(1+\max\text{ generator iterations}),
\]

the normalized first-orientation depth, and the normalized log modulus at
first orientation.  The source reports average-tie Spearman correlations for
every declared pair on `paired_train`, `paired_holdout`, their union, and
`small_exhaustive`.  No feature is selected and no prediction rule is fit.

## Frozen interpretation criteria

Let \(n=\lceil\log_2(N+1)\rceil\), and define the deliberately strict finite
work proxy

\[
W_0(n)=n^4.
\]

The classifications are fixed before seeing output.

1. **Integrity failure:** any true branch is absent; a branch digest is
   inconsistent with its stored sample; the final CRT root fails
   \(R^2=N\bmod M\); or a public singleton-product certificate disagrees
   with exact division.  Any integrity failure invalidates the run.
2. **Strong finite geometry lead:** every primary row completes exactly,
   ends with one verified branch, and has both maximum live width and maximum
   generator iterations at most \(W_0(n)\).  This remains finite evidence,
   not a QP proof.
3. **Partial geometry lead:** the integrity checks pass and at least 95% of
   primary `paired_holdout` rows meet both \(W_0\) bounds, but the strong
   criterion fails.
4. **Declared-proxy null:** more than 5% of primary `paired_holdout` rows
   exceed either \(W_0\) bound.  The smallest exact exceedance is preserved.
   This rejects only this strict proxy and the declared reveal order; it is
   not evidence against numerical QP in general.
5. **Structural correlation lead:** a predeclared correlation has
   \(|\rho|\geq0.50\) with the same sign on both paired random cohorts.
   This is a follow-up lead only.  It does not alter criteria 2--4.

Final uniqueness by itself is a sanity check, not a positive discovery: at
the full modulus \(M\geq K\), representative intervals are shorter than the
modulus, so the product-interval test becomes exact.  The central outcomes
are the maximum same-node frontier and construction work before that point.

## Run budget, remote paths, and abort policy

- Family and run ID: `F209-D01`.
- Remote alias: `seetacloud` from the local SSH configuration.
- Remote working directory:
  `/root/IntegerFactoring_F209/F209-D01`.
- Remote source:
  `/root/IntegerFactoring_F209/F209-D01/scripts/F209_D01_inverse_torsor_frontier.py`.
- Remote runner:
  `/root/IntegerFactoring_F209/F209-D01/scripts/run_F209_D01_remote.sh`.
- Remote log:
  `/root/IntegerFactoring_F209/F209-D01/logs/F209-D01.log`.
- Remote summary:
  `/root/IntegerFactoring_F209/F209-D01/output/F209-D01.json`.
- Remote rows:
  `/root/IntegerFactoring_F209/F209-D01/output/F209-D01.rows.jsonl.gz`.
- Runtime: `/root/miniconda3/bin/python`, using the existing SymPy package.
- Timeout: 1,800 seconds.
- Concurrency: one Python process and no workers.
- Address-space limit: 8 GiB through `ulimit -v 8388608`.
- Maximum odd representatives in \(P\): 2,000,000.  Exceeding it aborts the
  run; it does not truncate a row.
- Estimated peak memory: below 3 GiB.
- Estimated output disk: below 250 MiB.

Immediately before launch, the runner records CPU count, load, memory,
processes, and free disk.  It aborts before the experiment if available
memory is below 16 GiB, free disk is below 5 GiB, or the one-minute load
average exceeds twice the CPU count.  A preflight abort is an environment
event, not an experimental result.  No alternate dataset, threshold,
ordering, or timeout may silently replace this preregistration.
