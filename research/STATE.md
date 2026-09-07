# Research State

Updated 2026-09-07 after the sixth authorized Astra research cycle. The
goal remains active. This snapshot distinguishes proved modular residue
constructors from the ordinary-coordinate accuracy still needed for
factoring.

## Target and promoted interfaces

STATEMENT.md fixes the all-input classical Las Vegas quasipolynomial
factorization target. No algorithm meeting that target is established.

| Record | Exact scope | Missing operation |
| --- | --- | --- |
| P237 | A succinct modular rectangle-emptiness oracle would completely factor every integer with \(O(n^2)\) calls and polynomial additional work. It covers primes, prime powers, repeated factors, even inputs, and unbalanced composites. | No uniform efficient implementation of the rectangle oracle. |
| P238 | For \(M=2^k\), \(k\geq3\), positive odd \(N\), and a degree bank \(D\), all \(Q_j\bmod M\) and \(S_{ab}\bmod M^2\) are deterministically computable in bit complexity polynomial in \(k,D,\operatorname{bitlength}(N)\). The unit product \(\Pi_M\bmod2^P\) is also non-enumeratively computable. | No higher carry-precision bank and no Archimedean evaluation of the ordinary Cauchy kernel. |

P237 remains the actual all-input conditional factoring interface. P238 is
a global modular primitive. It does not implement P237's oracle.

P238 passed a fresh statement-only Sol reconstruction and root scope check.
Its input SHA-256 is
568441f2eebe3f519c356a4d0fe3cf43ac7243ede4a0e229f18683862f1f5b95,
and its reconstruction SHA-256 is
604a19e1cda14356b13e6e7bdc704e7a85fc3fc448fcb842c2ed6ed08a555450.
The full integer \(N\) is retained in the carry
\(q_u=(u(Nu^{-1}\bmod M)-N)/M\). Reducing \(N\bmod M\) leaves
\(S_{ab}\) unchanged but changes \(Q_j\).

## Sixth-cycle findings

F301 and C262 reduce each public rectangle to polynomially many evaluations
of

\[
 Z_{N,M}(z,w)=
 \sum_{\substack{1\leq u<M\\u\ {\rm odd}}}
 \frac{1}{(u-z)((Nu^{-1}\bmod M)-w)}
\]

at ordinary half-integer pole coordinates and specified absolute precision.

F302 and C263 give an exact half-modulus lift of this resolvent. Far poles
admit a certified \(O(\log M)\)-degree Taylor bank. The public near poles
require local boxes, whose zeroth joint moments are already the selected
inverse-graph half-counts. The lift reorganizes this operation but does not
compute it.

F303 and P238 compute every bounded-degree global mixed moment through two
base-\(M\) digits. C264 retains direct off-diagonal and diagonal formulas,
plus the exact next correction \(Q_{j,2}/2\bmod M\). When available, that
correction determines \(S_{11}\bmod M^3\), and the range of \(S_{11}\)
then makes this one moment exact. One exact \(S_{11}\) is not the whole
mixed Cauchy kernel or its required absolute-accuracy evaluation.

The tested high-input block average loses its apparent extra precision
after correction and division. The tested order-63 input-Mahler cutoff
fails modulo 4 at \(M=4096\). The exponent derivative obeys
\(L'(0)=(\log_{\rm adic}(N)/2)L(0)\) and adds no independent quadratic
carry equation. These are scoped results for those operations, not general
lower bounds.

Andreica, *The Scientific World Journal* (2013), Article 751358, already
gives a non-enumerative power-sum/Newton algorithm for the odd unit product
in its stated precision range. No novelty claim is made for the unit-product
primitive or the F303 mixed-moment identities.

## Evidence and restart point

All sixth-cycle jobs are complete. F302 retained 12 exact lift checks and
eight certified far-pole bounds. F303 retained 3,248 modulo-\(M^2\) mixed
checks, 3,248 corrected modulo-\(M^3\) checks, 2,320 weighted-carry checks,
large non-enumerative evaluations at \(k=32,64,128\), 12 sparse closed-form
controls, and 16 guarded exponent-derivative checks. Finite checks support
the implementations; they do not prove an ordinary resolvent algorithm.

The next operation is to construct a higher-precision, window-compatible
global aggregation for \(Z_{N,M}(z,w)\), or an equivalent evaluator at the
F301 poles and error budget. It must retain the selected window and enough
carry precision without enumerating graph points, local boxes, or a
numerical family of charts. Existing congruences and global low-digit
moments must not be counted as a solved \(Z\).
