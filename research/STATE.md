# Research State

Updated 2026-09-07 after the thirteenth authorized Astra cycle. All jobs are terminal. No expected-quasipolynomial factoring algorithm is established.

## Current Las Vegas interface

The target is complete factorization of every integer with one uniform expected
quasipolynomial bit bound. Attempts may fail and restart; deterministic
completion, exact counting, and uniformly fast auxiliary parameters are optional.

P249 gives the broadest current sufficient contract. For each fixed odd
\(N\) with at least two distinct prime divisors, run one public \(A(N,a)\)
on uniform Jacobi-positive units.
If its valid-output probability and mean verified cost satisfy
\[
 \delta_J(N)>0,\qquad
 \tau_J(N)/\delta_J(N)\leq Q(\operatorname{bitlength}N)
\]
then two uncapped engines give an all-input Las Vegas algorithm. One accepts
direct factors on the full set; the other uses private squares and P02.
Bit-step dovetailing costs at most \(6(g+\tau_J)/\delta_J\), with no
\(Q\) evaluation, separate square-subset mean, or cost-success independence.

| Mechanism | Positive primitive | Missing result |
| --- | --- | --- |
| P249 | Average-\(J\) FacRoot outputs suffice by uncapped two-source dovetailing. | A public procedure meeting the uniform cost/success contract. |
| P248 | Exact count defects, rational blocks, and inverse-parity predicates for P246 paths. | A charged hitting law or another useful partial solver. |
| P247 | Exact lazy-uniform-matching survival and endpoint law. | Its semiprime work remains least-factor scale. |
| P245/F321 | Radical-shadow transfer for adaptive root basins. | Squarefree cumulative hazard after all evaluation cost. |
| P41/P244/F320 | Energy sampler, hull normals, and pair-bank decoders. | Their respective factor-free sampling or numerical-power cost gaps. |

No narrow failure below bounds other transformations, matchings, screens,
rational maps, or partial FacRoot procedures.

## Thirteenth-cycle findings

P248 promotes F330's exact arithmetic identities. A signed remainder
\(r=\operatorname{rep}(at)\) expresses \(2Q_a(t)-t\) using at most
\(2|r|-1\) inverse-image tests and gives
\(|2Q_a(t)-t|\leq|r|\). Reflection has explicit affine defects. For fixed
\(a=-1,N=1\bmod4\), reflection has two constant matrices and adjacent
matching has guarded positive rational blocks
\[
 P:(U,V)\mapsto(U+V,U),\qquad Q:(U,V)\mapsto(V,U+V).
\]
Consecutive \(Q,P\) blocks translate the public coordinate by two exactly
under an alternating inverse-parity condition. All intermediate gcd, root,
special, and range guards remain necessary; the inherited bound is only
\(O(N)\) blocks.

An unpromoted continued-fraction certificate gives
\[
 |2Q_a(t)-t|\leq10\sum_i b_i
\]
simultaneously for adaptive \(t\), where \([0;b_1,\ldots,b_m]=a/N\).
This packet proves no Jacobi-positive mass or useful-success bound under a
small continued-fraction cutoff.

F329 found no consistent finite advantage for uniform-center reflections
over P247's lazy benchmark. Static edge screens raised short hit counts but
charged six gcds per edge and often worsened gcds per factor. F331 compared
path-derived, independent-uniform, and last-coordinate square rescalings.
They returned 16, 23, and 15 factors in 256 attempts; eight uniform factors
came from its extra generation/screen gcds. Every policy had zero successes
on the retained 36- and 44-bit cells. These are finite scoped results, not
bias or impossibility theorems.

F332 verified the fixed \(a=-1\) kernels but retained long paths. Both
methods completed through the 36-bit input; at cap 262,144, reflection alone
also completed one 44-bit input, while the remaining large cases were
censored. The \(N=61\) lift refutes only a proposed \(2N\) norm bound:
\((8,11)\) has norm \(185>122\), before a later root of \(-1\).
Near-balanced finite matrix words supply no length law.

P249 combines two source modes. Mode secrecy equates the root-output laws;
private-root secrecy and independent coins give P02. A capped version has
factor probability at least \(\delta_J/4\) after truncation, but must charge
evaluation of its literal budget or use an efficiently evaluable
quasipolynomial majorant. The uncapped dovetail avoids that issue entirely.
Standard primality, even-part, perfect-power, verified-split, and recursive
accounting supply the conditional all-input conclusion.

## Evidence and counts

P248 preserves statement/reconstruction hashes a1b1b87a... and eb515433....
P249 preserves hashes 0cc27150... and 63d19572.... C287--C291 retain all
finite outputs, repairs, censors, cost decompositions, source checks, and
manifests for F329--F333.

The catalog has 630 records, 34 routes, and 548 experiments, with 242 supported experiment-route assignments and 306 explicit unknowns.

## Restart point

Implement F330's unrun count descent on every small Jacobi-positive unit:
gcd-screen \(t,Q_a(t),t-Q_a(t)\), then replace
\(t\leftarrow\min(Q_a(t),t-Q_a(t))\). Compare one retained multiplier with
a fresh public multiplier, the inverse-start control, and the direct public
dyadic-window menu containing every bounded-defect child; charge every
generation, floor sum, gcd, and failure. Its \(O(\log N)\) stage count proves
only work. Test whether it has enough verified factor probability for P249.
