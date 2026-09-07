# Research State

Updated 2026-09-07 after the eighth authorized Astra research cycle. All
current mathematical jobs are terminal. The goal remains active, and no
complete factoring algorithm is established.

## Goal interfaces and current tools

| Record | Exact role | Missing operation |
| --- | --- | --- |
| P237 | Reduces every integer factorization input to \(O(n^2)\) public dyadic inverse-graph rectangle-emptiness calls, with polynomial additional work. | A uniform efficient implementation of those rectangle calls. |
| P239 | Recovers one exact rectangle count from four shifted binomial-carry values \(B(c,d)\bmod M\), with full-input and division precision retained. | A uniform efficient evaluator for shifted \(B(c,d)\bmod M\). |
| P240 | Computes bounded numerical-degree mixed and linear-carry moments for one canonical Möbius map in polynomial bit cost. | It does not aggregate the shifted map or window family. |
| P238 | Computes the global unshifted inverse-graph low-digit bank and odd-unit product in polynomial bit cost. | It does not evaluate shifted binomial carries or a sharp selector trace. |

P237 and P239 remain the goal interfaces. P240 and P238 are reusable modular
tools. No eighth-cycle claim is promoted because no complete new claim
received a fresh statement-only reconstruction.

## Eighth-cycle findings

F307 computes the whole shifted norm
\[
 \prod_u(1+Mq_u/N)\pmod {M^3}
\]
without enumerating graph points or Möbius branches. Its second residual
satisfies
\[
 B(c,d)=(N-M/2)h(c,d)-E(c,d)\pmod M,
\]
where \(h\) is the next digit of the total linear carry. The norm cancels
explicit quadratic cross-branch terms, but the selected window remains in
\(h\). Exact carry composition retains a weighted cross term. Summed
\(h_c\)-doubling reduces to an existing P240 moment identity and supplies
no independent precision. The tested norm reduction still needs the third
digit of that moment.

F308 gives the main positive advance. For
\[
 V(A,d)=\sum_{w\ {\rm odd}<M}w^{-2}
 \left\lfloor\frac{Aw-d}{M}\right\rfloor^2\pmod {2M},
\]
three existing polynomial-bit marginal calls compute the complete ordinary
remainder:
\[
 2A R_d(A,B)=V(AB,d)-A^2V(B,0)-B^2V(A,d)\pmod {2M}.
\]
The even residue is divided by two with one guard bit, and only odd \(A\)
is inverted. After subtracting this ordinary term, the corrected cocycle
retains only the inverse-floor term \(K_d(A,B)\); an input cut also adds an
affine-window pullback. For square inputs, a separate orbit argument
computes unshifted \(T(N,0)\bmod4\), not modulo \(M\).

F309 computes the complete pair-difference product at every dyadic
separation scale. One progression product gives the first band and every
other band is its \(2^{r-1}\)-st power. The two-source/two-target mixed
contrast is identically one. This is a complete non-enumerative product
constructor, but its separable cut dependence loses the selected rectangle.

F310 tests one fixed low-bit/high-bit linear representation of the inverse
top-bit phase. The \(N=9M+1\) matrices have finite-field rank \(R-3\) for
\(R=8,\ldots,256\), with certified nonzero minors. Their rational nullity is
three through \(R=64\). These ranks constrain that fixed characteristic-zero
separable representation only. A full-rank Hadamard matrix has an elementary
total sum, so high matrix rank does not imply that this scalar phase sum is
hard. Nonlinear and algebraic totals remain open.

## Evidence and scope controls

C267–C270 retain the exact equations, scope, and evidence paths. F307 passed
its norm, regrouping, composition, and third-digit controls; dropping the
unknown digit failed every relevant norm control. F308 passed 84 full
\(R_d\) residues and 28 corrected cocycles. Its non-enumerative \(k=64\)
general case took 1.55 seconds. The balanced \(k=128\) general case reached
the retained 30-second timeout and produced no result; the distinct
square-input modulo-four evaluator did complete through \(k=128\).

F309 passed 324 band identities and retained a correctly coupled
\(M=2^{65}\), \(L=2^{64}\) non-enumerative run. F310 retained all rank
minors and primitive rational nullspace vectors. Finite checks support only
their stated implementations and identities.

The catalog has 600 records, 34 routes, and 525 experiment packets. There
are 219 supported packet-to-route assignments and 306 explicit unknowns.
Missing mappings remain unknown.

## Restart point

The concrete missing operation is now the inverse-floor term
\(K_d(A,B)\) together with its affine input-cut pullback, or a direct
uniform evaluator for shifted \(B(c,d)\bmod M\). F308 has completely removed
the ordinary remainder \(R_d\). A successful next construction must retain
both public cuts and the full-input carry while aggregating this remaining
correlation without graph, patch, or window enumeration. The complete pair
product and tested composition norms provide no extra digit. High rank in
one linear variable order must not be treated as a lower bound against a
nonlinear or direct scalar aggregation.
