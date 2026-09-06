# F151 V2 hostile re-audit — PASS

## Verdict

**PASS.** V2 fully repairs the scope failure from V1. The four displayed
theorems are correct under their stated hypotheses. I found no false order
upgrade, short-window screen, quasipolynomial cost claim, lattice-catalogue
count, torus-character identity, or remaining-source claim.

This result is a boundary theorem. It does not give a factoring algorithm or
a factor-correlated sampler. It leaves larger exponents, other decoders,
canonical integer effects, structured lattice sampling, and other torus
coordinates open.

## Frozen inputs

I read the complete V2 statement, V2 proof, preserved V1 statement, preserved
V1 proof, failed V1 audit, and current manifest. The two requested hashes
match exactly:

- `V2_STATEMENT.md`:
  `325c1f8facf40e114586a5e7c1759129d7a422479102f9798da6a5fa42f7dec6`;
- `V2_PROOF.md`:
  `79f6ba29e886e61c98e913ade8933e5c4157822047bfae6332e6bc017c2855be`.

The preserved V1 files also have the hashes recorded in the manifest:

- `STATEMENT.md`:
  `eaa960c2e3e9ee594ec714d58d2a69af0ea2e1c818c89524cbd154aef2935acb`;
- `PROOF.md`:
  `0cc9660bc00f668c5f14f34ac684fa916e0acd4e05c59108b8a9864c761dcefd`;
- `HOSTILE_AUDIT_FAILED.md`:
  `249eda66360cf80f16257821c58cb1dcffe1495fb028ae9b1a70be29af8448c7`.

I did not modify either frozen V2 input or a durable ledger.

## V1 failure is fully repaired

V1 said that integer carries were the only possible progress source for the
short power bank. The failed audit gave

\[
N=77,\qquad B=4,\qquad \alpha=3.
\]

Here all component orders exceed `B`, and the complete scan through exponent
four is null. Nevertheless,

\[
\gcd(3^5-1,77)=11.
\]

V2 now says only that the listed screens are null. It explicitly leaves open
larger exponents, component-order mismatches beyond `B`, and other
value-dependent decoders. It limits its carry statement to possible progress
inside the current canonical exact-value decoder. The old counterexample now
illustrates an explicitly open channel. It no longer contradicts any V2
claim.

The title and conclusion were repaired in the same way. They no longer say
that the source has no factor signal. The Chebyshev index was also restricted
from every integer to every nonnegative integer.

## 1. Harvey--Hittmeir input and the component upgrade

I checked Harvey--Hittmeir, arXiv:2601.11131v2, Theorem 1.1. For
`N >= 3` and `1 <= B < N-1`, it returns a nontrivial divisor or a unit
`alpha` with `ord_N(alpha) > B`. Its stated bit cost is

\[
O\!\left(
\frac{B^{1/2}\log B}{(\log\log B)^{1/2}}\log N
\right).
\]

This is quasipolynomial when
`B=2^((log n)^O(1))`. Iteratively computing the first `B` powers and their
gcds adds `B*poly(n)` work, which is also quasipolynomial.

Let `r` be a rational prime divisor of `N`. If
`ord_r(alpha)=e <= B`, then `r` divides
`gcd(alpha^e-1,N)`. This gcd cannot equal `N`, because that would give
`ord_N(alpha) <= e <= B`. Thus the scan returns a proper divisor. If the
scan survives, every residue-field order is larger than `B`. This proof also
covers repeated prime factors. It correctly makes no prime-power order
claim.

## 2. Every listed short-bank screen is null

For distinct `e,f <= floor(B/4)`, a hidden prime divisor of one of the four
integers in (5) would force one of

\[
\alpha^{|e-f|}=1,\qquad
\alpha^{2|e-f|}=1,\qquad
\alpha^{e+f}=1,\qquad
\alpha^{2(e+f)}=1
\pmod r.
\]

Each exponent is positive and at most `B`. This contradicts the upgraded
local order bound.

For the canonical inverse `w_e`, multiplication by the unit `c_e` gives

\[
\gcd(c_e-w_e,N)=\gcd(c_e^2-1,N),
\]

\[
\gcd(c_e+w_e,N)=\gcd(c_e^2+1,N).
\]

A local zero would force the component order to divide `2e` or `4e`, again
at most `B`. Thus both gcds are one. The proof claims no control over the
integer factorization of `c_e w_e`, and V2 preserves this distinction.

## 3. Pilatte scale and support boundary

I checked Pilatte, arXiv:2404.16450v2, Corollary 1.5 and Theorem 3.18. The
parameters are

\[
d=\lceil\sqrt{\log N}\rceil,
\qquad X=d^{10^3d}.
\]

The `d` generators are independent random primes from the eligible set. With
high probability, the full relation lattice has a basis with Euclidean norm
`exp(O(d))`; the general theorem gives the explicit bound
`<< exp(42(d+r))`.

This norm theorem gives no polylogarithmic support theorem. A basis vector can
use as many as all `d=Theta(sqrt(n))` coordinates. For a fixed radius
`R=exp(Cd)` large enough to cover the theorem's bound, the integer Euclidean
ball is inside `[-R,R]^d` and contains the coordinate box of radius
`floor(R/sqrt(d))`. Its size is therefore

\[
\exp(\Theta(d^2))=\exp(\Theta(n)).
\]

Complete brute-force enumeration is exponential, not quasipolynomial. V2
correctly says that this is only a catalogue boundary. It is not a lower
bound against a structured classical sampler.

## 4. The fixed-Kummer-coordinate torus obstruction

For each hidden odd prime `r`, the local order bound with `B >= 4` excludes
`alpha=+1` and `alpha=-1`. Therefore

\[
x^2-1=
\left(\frac{\alpha-\alpha^{-1}}2\right)^2
\]

is a nonzero local square. With
`b=Delta^(-1)(x^2-1)`, inversion does not change a quadratic character, so

\[
\left(\frac b r\right)=\left(\frac{\Delta}r\right).
\]

The Jacobi-minus-one condition makes the two local characters opposite.
Thus `y^2=b`, equivalently `x^2-Delta*y^2=1`, is soluble in exactly the split
component and has no solution modulo `N`. The usual scalar embedding needs a
local square root of `Delta`; it cannot produce one global point with this
fixed `x`.

For every nonnegative integer `m`, the standard Chebyshev identity gives

\[
T_m(x)=\frac{\alpha^m+\alpha^{-m}}2.
\]

The right side contains no `Delta`. Therefore this x-only orbit loses the
specific split/nonsplit orientation introduced by `Delta`. V2 correctly
limits the obstruction to this direct splice. It does not cover P55's actual
Cayley points or other coordinate-aware decoders.

## Independent finite counterexample search

The audit checker is
`V2_HOSTILE_REAUDIT_CHECK.py`, with SHA-256
`109dcac3a3785f59cfd9e866fb471009a69e679078281221945a1b1c279365c8`.
It found no counterexample in these exact ranges:

- all `6 <= N <= 350`;
- all `4 <= B <= min(18,N-2)`;
- all units with global order larger than `B`;
- 440,878 component-upgrade cases;
- 160,692 surviving short-bank cases;
- all pairs of distinct odd primes through 43 that can support local order
  larger than four;
- both Jacobi-minus-one local orientations for each pair;
- 40,920 torus cases; and
- Chebyshev exponents from zero through 20.

The script also rechecks the `N=77` V1 counterexample. Its final output is
`status: PASS`. This finite search is only an audit check. The proofs above
establish the general statements.

## Scope conclusion

F151 V2 gives three clean facts:

1. a global large-order certificate can be upgraded to every hidden residue
   field in quasipolynomial time;
2. that upgrade removes the listed short collision and inverse-sign screens;
   and
3. the most direct scalar-to-Jacobi-torus Kummer splice loses the required
   local orientation.

The candidate does not make carry effects exclusive. It does not show how to
find Pilatte's relations classically. It does not prove that any surviving
channel factors all inputs. A fresh statement-only blind reconstruction is
still required before promotion.
