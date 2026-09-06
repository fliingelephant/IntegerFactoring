# F209-D01 result — interval geometry orients, but its exact constructor still scans a square-root interval

## Preregistered verdict

`strong_finite_geometry_lead`, with zero integrity failures.

All 5,858 primary F207 torsor rows ended in one verified branch.  Every one
also stayed below both preregistered finite thresholds

\[
\max_j|F_j|\leq n^4,
\qquad
\max_j W_j\leq n^4,
\]

where \(W_j\) is the registered generator-iteration count.  The other 36 of
the 5,894 total rows took F207's public \(\gcd(E,N)\) exit.

This is finite discovery evidence only.  It is not a QP bound or a factoring
theorem.

## Main measurements

| Cohort | Primary / total | Maximum frontier | Maximum generator iterations | Rows within both `n^4` bounds |
|---|---:|---:|---:|---:|
| paired train | 256 / 256 | 7,164 | 25,059 | 256 |
| paired holdout | 64 / 64 | 209,664 | 1,642,142 | 64 |
| exhaustive small | 5,535 / 5,570 | 121 | 206 | 5,535 |
| frozen witnesses | 3 / 4 | 5 | 9 | 3 |
| all | 5,858 / 5,894 | 209,664 | 1,642,142 | 5,858 |

The paired-holdout medians were 3,796 for maximum frontier width and 178,713
for maximum generator iterations.  The worst ratios to the registered
\(n^4\) bound were approximately `0.0430` for frontier width and `0.3365`
for generator iterations.

The largest frontier occurred at

\[
N=122815828493671
=8290591\cdot14813881.
\]

Its maximum live width was 209,664.  The maximum same-stage construction
count occurred at

\[
N=125736926187071
=8323643\cdot15105997,
\]

where the constructor examined 1,642,142 candidates against
\(47^4=4,879,681\).

## The Archimedean geometry is genuinely informative

The interval tests orient the actual inversion orbit before the final CRT
component on 5,715 of 5,858 primary rows.  They produce a verified public
singleton-product factor before the final component on 5,658 rows.

On the disjoint paired holdout, all 64 rows orient and decode before the
final component.  The first decode leaves one component unrevealed on 29
rows, two on 30 rows, three on four rows, and four on one row.

This materially differs from F205-D01's scalar-feature null.  The exact F207
torsor plus ordinary factor-size intervals contains useful orientation
information that the frozen scalar bank did not express.

The stored `first_global_unique_depth` is not itself an orientation measure:
frontier width can be one at a small component and grow again when that
branch acquires children.  The true-orbit orientation and verified decode
depths are the meaningful monotone outcomes.

## The same-node cost remains the core obstruction

The positive finite classification does not make the declared constructor
QP.  On 5,840 of 5,858 primary rows, including all 64 holdout rows, the
largest construction step is exactly a full scan of the odd integers in

\[
\left(\sqrt{N/2},\sqrt N\right].
\]

That scan has \(\Theta(\sqrt N)\) representatives.  The experiment's exact
switch between CRT expansion and interval scanning therefore still pays an
exponential current-node cost in the input bit length on these rows.  The
strong finite label occurs because \(n^4\) remains larger than this scan on
the registered 47-bit range; it cannot justify extrapolation.

The predeclared correlation analysis reinforces this accounting.  The
Spearman correlation between \(\log_2M\) and the logarithm of maximum
generator iterations is `0.9131` on train and `0.9037` on holdout.  The
largest-component log fraction also correlates with normalized orientation
depth (`0.5851` train, `0.5806` holdout).  These are follow-up leads under the
preregistered rules, not laws or proofs.

## Exact scope and next gate

F209-D01 establishes only this finite distinction:

- the raw \(\varphi(M)\)-sized inverse torsor is far larger than the live
  Archimedean frontier;
- fixed-order CRT refinement often orients and exactly decodes before all
  components are revealed; but
- the registered exact frontier constructor usually discovers that collapse
  by scanning the full small-factor interval.

It proves no lower bound against a compressed algorithm.  The precise
remaining positive target is a QP method for counting, isolating, or finding
the modular-inverse points

\[
x\in P,
\qquad Nx^{-1}\bmod m\in Q,
\]

with the product-interval condition, without enumerating \(P\), the unit
group, or an equally large set.  A different public component ordering or an
adaptive compressed representation also remains open.

Artifacts and provenance are recorded in `RUN_MANIFEST.md`.  The summary
and complete rows have SHA-256 values
`a75121324d320756847945bbbd97f93b914ec8476c99255464837b13d2563a5c`
and
`4684356503f785d878a79ace81af1bbf621bb2a0fa55c0b1ea51de25e0fb78b0`.
