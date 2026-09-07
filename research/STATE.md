# Research State

Updated 2026-09-07 after the ninth authorized Astra research cycle. All
current mathematical jobs are terminal. The goal remains active, and no
complete factoring algorithm is established.

## Goal interfaces and current tools

| Record | Exact role | Missing operation |
| --- | --- | --- |
| P237 | Reduces every integer factorization input to \(O(n^2)\) public dyadic inverse-graph rectangle-emptiness calls, with polynomial additional work. | A uniform efficient implementation of those rectangle calls. |
| P239 | Recovers one exact rectangle count from four shifted binomial-carry values \(B(c,d)\bmod M\), with full-input and division precision retained. | A uniform efficient evaluator for shifted \(B(c,d)\bmod M\). |
| P240 | Computes bounded numerical-degree mixed and linear-carry moments for one canonical Möbius map in polynomial bit cost. | It does not aggregate the shifted map or window family. |
| P238 | Computes the global unshifted inverse-graph low-digit bank and odd-unit product in polynomial bit cost. | It does not evaluate shifted binomial carries or a sharp selector trace. |
| P241 | Replaces sign-antisymmetric values by their residues modulo \(2^{p-2}\) inside \(Q_\epsilon\bmod2^p\). | It does not evaluate the residual overlap or reduce the graph modulus or output precision. |

P237 and P239 remain the goal interfaces. P240, P238, and P241 are reusable
tools with the displayed limits.

## Ninth-cycle findings

F311 studies the complete half-period ring-inverse phase over
\(\mathbb F_q\). The input \(N=527\), \(q=16\) has an exact genus-two
Artin--Schreier model in sign/log coordinates and signed total 12, although
the first genus-one model is excluded by Hasse. A fixed-pole order-31 family
has a retained dual nonmembership certificate at \(q=256\). Four \(q=16\)
phases become quadratic after tested nonlinear coordinate pullbacks and then
have exact polynomial-time quadratic totals; no tested larger case does.

The moving-two-finite-pole family, with a possible simple pole at infinity
and two freely filled pole bits, was searched completely at \(q=32,64,128\)
over original residues up to complement in both coordinates. It fits 18 of
64 targets at \(q=32\), but none of the 128 and 256 targets at \(q=64,128\).
At \(q=256\), only 16 seeded residues in both coordinates, 32 targets in
total, were tested, and none fit. These are exact bounded constructions and exclusions. A scalar
complete-phase model does not implement P239's arbitrary interval cuts.

P241 is the independently reconstructed positive result from F312. For
sign-antisymmetric integer functions \(r,g\), pointwise congruence modulo
\(2^{p-2}\) implies
\[
 Q_\epsilon(r)=Q_\epsilon(g)\pmod {2^p}
\]
for every \(p\geq3\) and every odd \(\epsilon\). The proof includes
inversion-fixed pairs, sign-inversion pairs, four-point orbits, negative
values, and the \(p=3\) boundary. Applied to centered floors, it reduces the
remaining value alphabet to \(\{-1,0,1\}\) at modulus eight. It does not
reduce the inverse graph, summand count, or requested output precision.

F312 also gives the exact unsigned modulo-eight form. Its ordinary floor
terms and at most four exceptional roots are computable, but the binary
overlap \(\sum_w a(w)a(\epsilon w^{-1})\bmod8\) remains unknown. Exact
half-translation keeps both the top-bit and canonical-wrap cuts. Generic
eight-point orbits contribute 4 and 6 modulo eight in retained examples.
The two-lift quotient halves the graph modulus only by introducing an exact
carry-signed product with both source and image masks still present.

The current Harvey--Hittmeir paper arXiv:2601.11131 is cached under the
generated key `harvey_2026_deterministic`. Its Theorem 1.1 and Algorithm 3.1
use the same interface as the v2 PDF already used in F195/F280; the
current version supplies no new order interface.

## Evidence and scope controls

P241 retains the unchanged statement and reconstruction hashes. C271 records
the F311 models, scoped Hasse/Walsh bounds, dual certificate, nonlinear
pullbacks, and full-versus-seeded moving-pole coverage. C272 records the
exceptional-root correction, faithful half-lift, generic counterexamples,
and remaining binary operations. F311's searches enumerate finite truth
tables; F312's finite controls verify identities but supply no global trace.

The catalog has 603 records, 34 routes, and 527 experiment packets. There
are 221 supported packet-to-route assignments and 306 explicit unknowns.
Missing mappings remain unknown.

## Restart point

F308 remains the main constructive advance: three polynomial-bit marginal
calls evaluate its complete ordinary remainder \(R_d(A,B)\). The concrete
missing operation is the inverse-floor term \(K_d(A,B)\) together with its
affine input-cut pullback, or a direct uniform evaluator for shifted
\(B(c,d)\bmod M\). F311's scalar field models do not carry arbitrary cuts,
and P241's two-bit value compression leaves the same graph and output
precision. A successful next construction must aggregate the remaining
binary or carry-signed correlation without enumerating graph points,
patches, windows, or orbit classes.
