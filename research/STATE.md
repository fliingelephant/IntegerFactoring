# Research State

Updated 2026-09-07 after the tenth authorized Astra research cycle. All
mathematical jobs are terminal. The goal remains active, and no complete
factoring algorithm is established.

## Current counting route and constructors

| Record | Exact role | Remaining limit |
| --- | --- | --- |
| P237 | Reduces every integer factorization input to \(O(n^2)\) public short dyadic inverse-graph rectangle-emptiness calls. | Needs a uniform efficient implementation of arbitrary public rectangles. |
| P239 | Recovers one exact rectangle count from four shifted binomial-carry values \(B(c,d)\bmod M\). | Needs a uniform evaluator for shifted \(B(c,d)\) with both cuts. |
| P243 | Computes the fixed half/half inverse-graph count modulo eight for every positive odd full input. | Fixed endpoints and three residue bits do not decide arbitrary emptiness. |
| P242 | Computes canonical unshifted \(K(A,B)\) and \(T(N)\) modulo four, with stated raw corrections. | Supplies no shifted or higher-precision sum. |
| P240 | Computes bounded-degree moments for one canonical Möbius map. | Does not aggregate shifted maps or windows. |
| P238 | Computes global unshifted low-digit and odd-product banks. | Does not insert a sharp selector. |

P237 and P239 are sufficient interfaces for the current counting route,
not requirements on other routes. P237 itself allows Las Vegas oracles.
P242 and P243 are polynomial-bit constructors with the displayed limits.

## Tenth-cycle findings

P242 uses canonical coordinates \(A=(-1)^\sigma5^a\bmod M\). A fixed number
of lifted section bits and four characteristic-two square coefficients give
every canonical \(K(A,B)\bmod4\). Two ordinary Euclidean floor sums give
canonical \(T(N)\bmod4\). Raw \(K\) has an explicit bilinear correction;
raw \(T\) uses P238's even \(Q_0\bmod4\). The independently reconstructed
cost is \(O(k^3)\) with schoolbook arithmetic. The focused source comparison
in F313 found no theorem dependency or new known interface; it makes no
novelty claim.

P243 turns that transport bit into actual inverse-graph count precision.
For \(R=2^k\), \(\phi=R/2\), and positive odd \(N\), put
\[
 C(N,2R)=\#\{u\text{ odd}<R:N/u\bmod2R<R\}.
\]
An all-integer binomial parity identity reduces this count modulo eight to
\(H_N\bmod8\), \(B_N\bmod4\), and one cubic fixed-point bit. P238 computes
\(H_N\) from the odd product modulo \(8R\); P242 and ordinary degree-two
floor moments compute \(B_N\). All divisions have explicit guard bits and
the full quotient \(N=\nu+R\ell\) is retained. The constructor is polynomial
in \(k\) and \(\log N\) and does not enumerate graph points.

This is a real three-bit count gain, but it is one fixed half-box. A zero
residue modulo eight does not imply emptiness. The modular half-box may also
contain wrapped products, while P237's short rectangles require the exact
unwrapped condition.

F314 gives an integral symmetric-power lift whose arbitrary cut trace equals
the rectangle count modulo four. A degree-\(O(p)\) integer idempotent raises
the entry precision to \(2^p\), but summation still needs cut-restricted
Hadamard moments. Pascal tensor cuts are compact; their normalized Cauchy
block has no constructed fast aggregate.

F317 computes each normalized Cauchy entry in polynomial bit cost and gives
an exact local affine chart. Its intercept is the moving quotient \(q_0\);
its slope and both inherited endpoints also vary with the base residue.
Even the first half-box block asks for the parity histogram of \(q_0\).
The per-entry locality therefore does not evaluate the cut trace.

F316 gives a guarded half-modulus recurrence for the next canonical section
precision. It leaves one mixed high/low-section correlation and one
truncated convolution endpoint. Neither repeated state closure nor an
arbitrary-cut version is proved.

F315's exact spectra are a useful control: the first bit has dense,
high-degree algebraic normal forms in the tested orders even though P242
computes its scalar total in polynomial bit cost. The density of the next
two finite tables is therefore no evidence of hardness.

## Evidence and counts

P242 and P243 retain fresh statement-only reconstructions and exact hashes.
C273–C276 retain the integral-lattice, bulk-spectrum, guarded-section, and
Cauchy scopes with all failures and resource logs. P243 passed 1,173 direct
counts through \(R=4096\); proof-based nonenumerative cases reached
\(R=2^{256}\). F318's ENDPOINTS.md proves the exact polarization
\[
 2\,\#([a,b)\times[c,d))
 =D(a,d)+D(b,c)-D(a,c)-D(b,d),
\]
requiring one extra precision bit, but supplies no variable-\(D\) evaluator.

The catalog has 609 records, 34 routes, and 533 experiment packets. There
are 227 supported packet-to-route assignments and 306 explicit unknowns.
Missing mappings remain unknown.

## Restart point

The recent work overemphasized deterministic exact counting. Next investigate
randomized discovery of a verified divisor without requiring a count or an
emptiness certificate. For independent identical attempts at a fixed composite
\(N\), with finite expected cost \(a(N)\) and success probability \(p(N)>0\),
the expected cost to obtain a verified divisor is \(a(N)/p(N)\). Prove a
uniform quasipolynomial bound on that ratio for every composite input, then
account for complete factorization. Quasipolynomial state banks and rare
expensive branches are allowed within the total expected bound.

For continued work on the counting route, concrete targets are a variable
diagonal interval count \(D(x,y)\) with its guard bit, P239's shifted
\(B(c,d)\), F317's moving \(q_0\) histogram, or F316's mixed recurrence.
A route using P237 must retain its short public endpoints; the fixed P243
half-box cannot replace them. Other routes need not implement these oracles.
