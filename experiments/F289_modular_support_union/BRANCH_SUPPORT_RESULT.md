# F289: affine-node branch-and-bound support

Status: exact finite query-count experiment. This is not a fast support
implementation claim or a factoring complexity claim.

## Implementation

For odd \(N\), \(M=2^k\), and a positive integer normal \((a,b)\), the search
uses nodes \((r,u_0)\) with

\[
s=2^r,\qquad m=2^{\min(k,2r+1)}.
\]

The node lattice is represented by

\[
x=u_0+sj,\qquad
y\equiv v_0+\delta j\pmod m,
\]

where

\[
v_0\equiv Nu_0^{-1}\pmod m,\qquad
\delta\equiv N((u_0+s)^{-1}-u_0^{-1})\pmod m.
\]

The root is \((1,1)\), and the last depth is
\(h=\max(1,\lceil(k-1)/2\rceil)\). Each child recomputes its own
\(m,v_0,\delta\).

The initial incumbent is public. The source tests 64 odd \(x\)-values around
\(\lfloor\sqrt{bN/a}\rfloor\), rounds \(y\) to the target modulus, and also
tests \((1,N)\) and \((N,1)\). Factor labels do not enter this step.

For incumbent objective \(U\), a node scans only its \(x\)-values in

\[
\left[
\left\lceil\frac{U-\lfloor\sqrt{U^2-4abN}\rfloor}{2a}\right\rceil,
\left\lfloor\frac{U+\lfloor\sqrt{U^2-4abN}\rfloor}{2a}\right\rfloor
\right].
\]

The two endpoints are audited against the exact quadratic inequality. For
each eligible \(x\), the source selects the least feasible \(y\) in the node
lattice. The node oracle minimizes the complete tuple

\[
(aX+bY,XY,X,Y).
\]

This preserves product and coordinate tie ordering. A target-feasible node
minimum closes the subtree. Otherwise the node splits. A best-first heap holds
the exact tuple bounds.

The branch search runs before its baseline. The baseline streams the existing
full-support capture: all eligible \(x\leq K\), their least target-feasible
\(y\), and the coordinate-swapped points. It retains one exact optimum for
each fixed normal without materializing a hull.

## Test matrix and exact agreement

The five labelled semiprimes use
\(B=2^8,2^{10},2^{12},2^{14},2^{16}\). At each scale, every power-of-two
modulus from 16 through the largest one not exceeding
\(16\lfloor\sqrt N\rfloor\) is tested. The seven fixed public normals are

\[
(1,1),(9,8),(5,4),(4,3),(3,2),(7,4),(2,1).
\]

All 455 branch results matched the full-enumeration baseline in the complete
tuple order. Four additional capped node queries matched the geometry route's
independent exact affine-patch support implementation. These checks validate
the finite implementation only.

## Aggregate counts

Across 65 \((N,M)\) batches:

- queried nodes: 12,107;
- expanded nodes: 5,826;
- pruned nodes: 6,028;
- accepted nodes: 253;
- full-leaf count over the same queries: 20,692;
- peak live heap: 158 nodes;
- public incumbent already optimal: 202 of 455 queries;
- root accepted, expanded, and pruned: 9, 399, and 47 queries;
- proper-factor and nonfactor results: 105 and 350; and
- trivial-factor results: 0.

The exact queried-node to full-leaf ratio is \(12107/20692\).

| Depth | Queried | Expanded | Pruned | Accepted | Scanned \(x\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 455 | 399 | 47 | 9 | 869,327 |
| 2 | 798 | 600 | 169 | 29 | 866,459 |
| 3 | 1,200 | 889 | 268 | 43 | 842,575 |
| 4 | 1,778 | 1,097 | 632 | 49 | 822,288 |
| 5 | 2,194 | 1,191 | 944 | 59 | 765,000 |
| 6 | 2,382 | 1,046 | 1,307 | 29 | 652,475 |
| 7 | 2,092 | 511 | 1,556 | 25 | 426,282 |
| 8 | 1,022 | 84 | 928 | 10 | 178,954 |
| 9 | 168 | 9 | 159 | 0 | 23,450 |
| 10 | 18 | 0 | 18 | 0 | 2,344 |

## Enumeration cost

The branch nodes scanned 5,449,154 \(x\)-values. Running the streaming
baseline separately for every normal would scan 13,890,506 \(x\)-values.
Their exact ratio is

\[
\frac{2724577}{6945253}.
\]

The retained baseline shares each stream across all seven normals, so its
actual scan count was 1,984,358. The two counts answer different questions:
the logical count compares independent support queries, while the shared
count measures this batched pilot.

| Scale | Queries | Branch nodes / full leaves | Branch scans / logical baseline scans | Peak heap |
|---|---:|---:|---:|---:|
| \(2^8\) | 63 | 273 / 644 | 5,800 / 25,417 | 5 |
| \(2^{10}\) | 77 | 877 / 1,316 | 40,698 / 133,728 | 18 |
| \(2^{12}\) | 91 | 1,943 / 2,660 | 197,973 / 487,424 | 26 |
| \(2^{14}\) | 105 | 3,181 / 5,348 | 733,017 / 2,246,846 | 60 |
| \(2^{16}\) | 119 | 5,833 / 10,724 | 4,471,666 / 10,997,091 | 158 |

Measured branch-query time summed to 1.177 seconds. The shared baseline
streams took 3.699 seconds. These are implementation timings for this matrix,
not asymptotic evidence.

## Compact certificates

### Root acceptance with an objective tie

For

\[
N=2152963,\quad M=16,\quad (a,b)=(1,1),
\]

the public incumbent was \((1405,1535)\), with objective 2940 and product
2,156,675. The root node returned the target-feasible point
\((1381,1559)\), also with objective 2940 but product 2,152,979. The complete
tie order selected the lower product. One node was queried and accepted.

### One-node certificate against 64 leaves

For the same \(N\), with \(M=16384\) and \((a,b)=(3,2)\), the public
incumbent \((1181,1823)\) was already exact. Its objective was 7189 and its
product was \(N\). The root bound pruned the hierarchy after one node scan,
compared with 64 leaf patches. The branch scanned 18 \(x\)-values; the
full-union baseline scanned 7,520.

### A case where hierarchy overhead is visible

For

\[
N=8464705853,\quad M=131072,\quad (a,b)=(1,1),
\]

the exact result was the nonfactor point \((90969,93317)\), with objective
184286 and product 8,488,954,173. The search queried 171 nodes although the
tree had 128 leaves. It scanned 115,789 \(x\)-values, while the baseline
scanned 56,445. This exact case prevents interpreting node pruning as a
uniform enumeration reduction.

### Largest tested modulus

For the same \(N\), with \(M=1048576\) and \((a,b)=(3,2)\), the exact result
was \((73771,114743)\), with product \(N\). The search queried 65 nodes
against 512 leaves, reached a peak heap of 33, and scanned 230,096
\(x\)-values versus 515,197 for the baseline.

## Resources and artifacts

The single-process run completed in 4.881 seconds with peak RSS 23,658,496
bytes. The source has a 30-second alarm. No scale gate was hit, so the run
extended through \(B=2^{16}\).

The retained files are:

- branch_support.py: source;
- branch_output.json: all query summaries, exact results, depth counts, and
  compact certificates;
- branch_run.log: timings and aggregate counters; and
- BRANCH_RESOURCE_ESTIMATE.md: pre-run resource estimate and scale gates.

Factors appear only in case construction and post-hoc outcome auditing. The
branch decisions use only \(N,M,a,b\), node arithmetic, and public feasible
points.
