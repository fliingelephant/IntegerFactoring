# F54 hostile whole-artifact audit

## Verdict

**PASS AS WRITTEN.** I found no mathematical, scope, or retained-run
provenance defect in the pinned candidate. The result is a narrow obstruction
for one polynomial and its affine conjugates. It is not a lower bound for all
polynomial dynamics and not a factoring algorithm.

## Pinned artifacts

- Candidate:
  `experiments/F54_polynomial_root_basin_kill/RESULT.md`

  SHA-256:
  `a0ca496ec0aba9cf0ad9c52683aefc0e05507558d3d0120eb6a50454dd96db19`
- Run manifest:
  `experiments/F54_polynomial_root_basin_kill/RUN_MANIFEST.md`

  SHA-256:
  `bee0d78de357e606232f7166ec4e880811b394630f03efe18c18d0fff161f6dc`

I read both pinned artifacts in full. I also checked the complete promoted
statements P45 and P52 and the current registry entry for F54-D01.

## 1. Exact basin proof

For \(H(x)=x(x-1)\), the inverse image of \(0\) is exactly
\(\{0,1\}\). The equation \(H(x)=1\) is

\[
x^2-x-1=0,
\]

with discriminant \(5\). If \(5\) is a quadratic nonresidue modulo the odd
prime \(p\), this equation has no root. Therefore

\[
H^{-1}(\{0,1\})=\{0,1\}.
\]

Backward induction then proves the claimed all-time statement: an orbit
enters the target set if and only if it starts in that set. This argument is
valid for every iteration count, not only a fixed or polynomial count.

The excluded cases are correct. The prime \(5\) cannot satisfy the stated
nonresidue hypothesis, and the theorem explicitly assumes odd primes.

## 2. Exact CRT probabilities

For a raw uniform start modulo \(N=pq\), each local start has two target
values. Failure occurs in exactly these disjoint cases:

- both local starts avoid \(\{0,1\}\): \((p-2)(q-2)\) classes;
- both starts are \(0\): one class;
- both starts are \(1\): one class.

The two mixed target starts succeed at time zero because the separate
\(x_i\) and \(x_i-1\) tickets expose opposite factors. Thus the success count
is exactly

\[
pq-(p-2)(q-2)-2=2p+2q-6.
\]

For a uniform unit start, only the local target \(1\) remains. Exactly one
local component equals \(1\) in

\[
(q-2)+(p-2)=p+q-4
\]

unit CRT classes. This proves the stated denominator
\((p-1)(q-1)\). The formulas also remain valid when one prime is \(3\).

The global-root claim is correct. A root of \(a(a-1)=0\pmod N\) has four
CRT patterns. Either it is the public root \(0\) or \(1\), or it is mixed.
In a mixed pattern, \(\gcd(a,N)\) is already a proper factor.

## 3. Random affine relabeling

For a unit \(c\), substituting \(x=cy\) gives

\[
H_c(cy)=cH(y).
\]

This is an exact conjugacy over \(\mathbb Z/N\mathbb Z\) and over both
hidden fields. It carries \(\{0,1\}\) to \(\{0,c\}\). Multiplication by a
unit preserves a uniform raw start, a uniform unit start, and the two
root-difference gcd tickets. Therefore the success probabilities hold for
each unit \(c\), not only after averaging.

The raw-\(c\) count is also exact. There are \(q-1\) nonzero multiples of
\(p\) and \(p-1\) nonzero multiples of \(q\), for total probability

\[
\frac{p+q-2}{pq}.
\]

After rejecting zero and accepting only gcd-one values, the accepted value
is uniform over the units. A mixed root of \(H_c\) exposes a factor through
\(\gcd(a,N)\) or \(\gcd(a-c,N)\), as claimed.

For a general affine relabeling, “affine” must retain its standard meaning:
the slope \(c\) is a unit. Under that reading, the conjugacy and target-set
claim are exact. The candidate already separates these relabeled targets
from the root-preserving scaling subfamily.

## 4. Infinite balanced family and runtime claim

For odd \(p\equiv2\pmod5\), quadratic reciprocity gives

\[
\left(\frac5p\right)=\left(\frac p5\right)=-1.
\]

The prime number theorem in arithmetic progressions implies that, for all
sufficiently large \(X\), the interval \([X,2X]\) contains at least two such
primes. Choosing two distinct primes from each of an unbounded sequence of
these intervals gives the claimed balanced semiprimes.

On this family, \(p,q=\Theta(\sqrt N)\). Both exact restart probabilities
are \(\Theta(N^{-1/2})\), and the raw scaling ticket is of the same order.
The orbit length cannot increase the probability because the basin is
already closed. A polynomial number of independent restarts therefore has
negligible success by the union bound, and independent repeat-until-success
has expected restart count \(\Omega(\sqrt N)\). This is exponential in
\(\log N\).

## 5. General necessary basin condition

For a fixed public map and a uniform CRT start, a target-ticket factor event
requires at least one local start to lie in its depth-\(t\) backward basin.
The union bound gives exactly

\[
\Pr(\text{factor by time }t)
\le |B_{p,t}|/p+|B_{q,t}|/q.
\]

Averaging preserves the inequality when the public map randomness is
independent of the uniform start. This independence is required, and it is
already enforced by the candidate's uniform-start model and its explicit
exclusion of correlated starts. The bound does not assert sufficiency. Even
large local basins can have synchronized hit signatures, as the candidate
states.

The coefficient and target screens are also scoped correctly. If map
construction itself emits a zero divisor, factoring has already succeeded;
the basin theorem concerns the remaining factor-free branch.

## 6. Boundary comparison

- P45 does not imply this result. P45 concerns explicit low-degree
  bijections of the zero-product point set. The map \(x(x-1)\) is
  noninvertible.
- P52 does not imply this result. P52 treats the rational known-square
  Newton map, whose root basins are singletons by global conjugacy to
  squaring. F54 treats a polynomial with branching preimages and proves that
  one infinite prime family removes the first new branch, leaving a
  two-point basin.
- The current approach table has no standalone F29 mechanism row. The
  computation ledger does contain F54-D01 and identifies F29 as “iterated
  polynomial root-basin.” This is an administrative integration item for
  promotion, not a defect in the pinned theorem or run. The candidate itself
  supplies the exact scope: fixed \(x(x-1)\), affine conjugates, uniform
  uncorrelated starts, and target-root tickets only.

The exclusions are material and correct. The result does not cover unrelated
quadratics, \(N\)-dependent maps, nonuniform or correlated starts, extra
state, lifts, arbitrary public targets, or full-orbit decoders.

## 7. Retained finite run and provenance

The manifest's hashes match the retained files:

- source SHA-256:
  `943ea2fd1cc28bc53998499f468f06a9ea43176e6819929fa1ff0853a80fca60`;
- runner SHA-256:
  `2fa47db442b6b7c5a5d45c43af073d4f67f24ac68b36d81db13a92f6ad416f00`;
- log SHA-256:
  `3ce069be420d1a929996c1e88f2e7694a29818a4d42f54fe7fe4eaec05f68048`;
- output SHA-256:
  `1c6c32f0b4e7dfbeffe2b171fb36ba02921b62a648fff7347f10c9fdd189b6f3`.

The runner names the source, applies the declared 60-second timeout, records
Python 3.14.5, and ends with exit status 0. The source exactly implements the
declared finite questions. Its counts are internally consistent: 49 primes,
10,954 nonzero scaling parameters, and \(\binom{11}{2}=55\) semiprime pairs.
It found no counterexample. The registry and candidate correctly classify
this run as a finite cross-check only.

I did not run a new finite computation. The symbolic proof settles every
unbounded claim, and the retained source, log, output, hashes, and arithmetic
counts were sufficient for this provenance audit.

## Final audit disposition

The pinned candidate can proceed to strict proof-blind reconstruction. A
promotion must keep the result narrow and must add a standalone F29 approach
row or otherwise integrate the new family name into the approach registry.
