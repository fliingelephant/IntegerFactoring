# Research State

Updated 2026-09-07 after the seventh authorized Astra research cycle. The
goal remains active. No complete factoring algorithm is established.

## Current proved interfaces

| Record | Exact scope | Missing operation |
| --- | --- | --- |
| P237 | Reduces every integer factorization input to \(O(n^2)\) public dyadic inverse-graph rectangle-emptiness calls, with polynomial additional work. It covers primes, prime powers, repeated factors, even inputs, and unbalanced composites. | A uniform efficient implementation of those rectangle calls. |
| P239 | Recovers an exact canonical rectangle count from four shifted binomial-carry values \(B(c,d)\bmod M\), including full input, endpoints, negative carries, and the required \(2M\) carry precision. | A uniform efficient evaluator for shifted \(B(c,d)\bmod M\). |
| P240 | Computes every bounded numerical-degree mixed moment modulo \(L^2\) and linear carry moment modulo \(L\) for one canonical Möbius map, in polynomial bit cost without enumerating its \(L\) points. | A faithful aggregation over the shifted windows or the growing family of maps. |
| P238 | Computes the global unshifted inverse-graph low-digit bank \(S_{ab}\bmod M^2\), \(Q_j\bmod M\), and the odd-unit product in polynomial bit cost. | It does not evaluate shifted binomial carries or trace an interval circuit. |

P237 is the all-input conditional factoring reduction. P239 identifies a
smaller exact sufficient statistic for each rectangle call. P240 and P238
are modular moment constructors. Neither supplies P239's shifted statistic.

## Seventh-cycle findings

F306 proves P239's four-corner identity. For each point in both selected
windows, the mixed shifted-carry contribution is \(N-M/2\bmod M\); it is
zero outside. The multiplier is odd, and the count is smaller than \(M\),
so the recovered residue is the exact count. This reduction does not
construct the \(B\) evaluator.

F304 proves P240 for a general map

\[
 T(x)=\frac{n-Ax}{B+Cx},\qquad 0\leq x<2^s,
\]

with odd \(A,B\), positive even \(C\), and the full integer \(n\) retained
in the carry. Ordinary power sums, uniformly truncated 2-adic binomial
series, guarded Newton identities, and a unit-triangular symmetric-function
recurrence give the bank. The \(d=0\) interface is included.

F304 also gives succinct guarded digit selectors and a triangular Newton
error bank. Repeated exact quotients create two Möbius branches per level.
The literal map family has exponentially many distinct members at the
tested depth, and finite degree-two carry banks exhibit the same growth on
the retained cases. This is not a lower bound against another aggregation.

F305 transports all canonical inputs to one fixed \(N=1\) carry measure.
It gives polynomial-bit evaluators for the reciprocal-floor marginals
\(R_1^*\) and \(R_2\bmod2M\), and FULL_INPUT.md gives the exact correction
for every positive odd full input. The remaining term is a sharp floor
weighted by the fixed carry measure. Its mixed cut difference is the
rectangle count. A dyadic reflection leaves an additional carry-bit
weighted floor term, with no proved closed total-state recursion.

## Evidence and scope controls

All current mathematical jobs are complete. P239 was reconstructed from a
statement-only input and checked by the root. P240 passed an independent
statement-only reconstruction. Its input SHA-256 is
19599f6d20c1fac30bfeda265dd395dcdda6d81d1786c1dacb8dd8b1f4b3165c,
and its reconstruction SHA-256 is
bc9ef597891d4b61df699975fdd1abbc3769b4a203c928397e8ada490dd762d0.

The repaired P240 implementation passed 32 exact edge checks for
\(s=1,\ldots,4\) and \(d=0,1\). A correctly coupled original-input pilot at
\(M=2^{65}\), \(L=2^{64}\), and \(N=9M+1\) completed in 0.529 seconds at
18,087,936 bytes peak RSS and matched all degree-three universal marginals.
Its large mixed values were computed but not independently verified. The
earlier \(s=33,65\) runs remain valid generic one-map pilots; their retained
scope note states that they were not original \(M=2^s\) first-quotient
patches.

F305 retained 11,352 pointwise transports, 150 shifted binomial identities,
450 marginal checks, 25 reflection checks, and non-enumerative marginal
runs through \(M=2^{32}\). F306 retained 1,200 general rectangles, 175
public factor rectangles, and 21 complete enumerated reference inputs.
Finite checks support the stated identities and implementations only.

The catalog has 521 experiment packets, 215 supported packet-to-route
assignments, and 306 explicit unknowns. Missing mappings remain unknown.

## Restart point

The concrete missing operation is a uniform efficient evaluator for the
shifted statistic \(B(c,d)\bmod M\), or an equivalent faithful aggregation
that preserves both public cuts, the full-input carry, and the required
division precision. Solving the entire ordinary Cauchy resolvent is not
necessary. A proposed construction must aggregate the correlated map or
carry/window family without enumerating graph points, residue patches, or
window boxes. Unshifted low digits and one-map moment banks must not be
counted as a solved shifted evaluator.
