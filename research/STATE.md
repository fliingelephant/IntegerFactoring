# Research State

Updated 2026-09-07 during the fifth authorized Astra research cycle. The
goal is active. The root read notes/Zhihu.md and notes/Inspirations.md in full
at launch; their claims remain motivation, not assumptions.

## Target

STATEMENT.md fixes the all-input classical Las Vegas quasipolynomial
bit-complexity target. No algorithm meeting that target is established.
P232--P237 are scoped supporting results. P237 is the current all-input
conditional interface; C259--C262 retain adjacent author-derived claims and
finite evidence.

## Current results

| Packet / record | Result and scope | Remaining question |
| --- | --- | --- |
| F288--F292, P235--P236 | A succinct 1.01-relative dyadic support optimizer would factor odd composites, and one rational-root quadratic-Gauss/exponential-Cauchy kernel has an output-sensitive polynomial-bit algorithm conditional on Hiary 2011, Theorem 1.1. | Neither result supplies an all-input support or rectangle oracle. P236 covers no whole outer family or ordinary-coordinate mixed resolvent. |
| F298, C259, route:F31 | The global quadratic two-window family has an exact four-child parity recurrence with cheap boundary corrections. | Bound the number of distinct signed child states; closure of the family alone gives no QP cost. |
| F299, C260, route:F31 | The common-conductor all-frequency identity is exact, but every faithful halfbox class collapses to one affine half-window and the full class family is exactly P235's existing cover. | No new asymptotic class aggregation or public short-window interface results; Barvinok is unnecessary. |
| F300, C261, route:F31 | A complete Gauss-weighted Salié sum is polynomial-bit evaluable. Adding one or two exponential Cauchy denominators leaves a Fourier-weighted quadratic digit, with only a partial parity descent. | Evaluate the retained odd-frequency triangular digit and still assemble the original chart/window geometry. |
| F301, P237, C262, route:F31 | A succinct modular rectangle-emptiness oracle of cost \(T(n)\) would completely factor every integer with \(O(n^2)\) calls and cost \(O(n^2T(n)+\operatorname{poly}(n))\). Bounded rational windows reduce each public rectangle to polynomially many calls to one global mixed ordinary-Cauchy kernel. | Construct a uniform QP evaluator for that kernel; the numerical Empty oracle and rational filters do not supply one. |

P237 passed a fresh statement-only Sol reconstruction and root scope check.
The statement SHA-256 is
e6a68b51f1dc7f0820741b290c916f4318a126d4932ae3a12da3cab28777623d,
and the reconstruction SHA-256 is
76aea453f4c0e5cbdb759982afe78939d0c6dfcc7c7fcc7cec0999e700975fa7.
It covers primes, prime powers, repeated factors, even inputs, and unbalanced
composites. It promotes no efficient Empty implementation or rational
filter theorem.

## Actual bottleneck

For the current rectangle route, the missing operation is a uniform
quasipolynomial-bit evaluator for

\[
 Z_{N,M}(z,w)=
 \sum_{\substack{1\leq u<M\\u\ {\rm odd}}}
 \frac{1}{(u-z)((Nu^{-1}\bmod M)-w)},
\]

where \(M\) is the largest power of two at most \(N/8\). F301's interval
filters have degree \(O(n^2)\), half-integer real pole coordinates, explicit
polynomial-size conditioning, and rigorous count error at most \(1/8\).
Their pole expansion needs \(O(n^4)\) mixed calls per rectangle, hence
\(O(n^6)\) calls over P237's complete factorization, up to fixed polynomial
factors. No fast evaluator for \(Z_{N,M}\) is known in this work.

This is a sum over the whole original inverse graph with ordinary coordinate
denominators. P236 instead treats a quadratic exponential phase and a
root-of-unity denominator; applying it here requires a new proved
transformation.

The older chart route retains two separate scope gaps. F294, F298, and F300
work inside one odd \(u_0\)-chart for original modulus \(m^3\), with
\(q=m^2\) internal and full cyclic half-windows. Summing internal frequencies
still leaves \(m/2\) chart classes and the change to the factor-isolating
short windows. F299 reorganizes the faithful classes but proves that they
are exactly P235's existing affine cover. F301 reaches the actual
\(M=\Theta(N)\) public rectangles directly; only their global mixed kernel
remains unimplemented.

## Verification and resources

All F298--F301 numerical jobs are complete and retain sources, outputs, logs,
timeouts, and resource measurements. F301's reference implementation matched trial
division on 4,095 consecutive and 120 seeded inputs. Its rational filters
passed 131,064 exact integer checks and 67 certified original rectangles;
the pole pilot isolated 93 positive roots and passed 24 partial-fraction
checks. These are finite evidence, not asymptotic algorithms.

The retained F289 scaling JSON reports 16 exact and 8 budget-exhausted
queries. An earlier 15/9 run has no surviving full JSON and was not
reconstructed. P232--P237 have independent statement-only reconstructions
and root scope checks. No graph relation follows from a textual mention.

Use the Rust reader for older heads and bodies. Creative route work belongs
to Astra; blind reconstruction uses fresh Sol contexts. Follow PROMPT.md.

## Next operation

Construct and verify one uniform recurrence or evaluator for \(Z_{N,M}(z,w)\)
at F301's pole locations and required precision. It must group all odd
\(u<M\) without enumerating graph points or a numerical family of local
charts.
