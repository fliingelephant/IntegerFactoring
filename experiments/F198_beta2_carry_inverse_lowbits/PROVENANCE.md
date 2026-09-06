# F198 provenance

## Local antecedents

F198 sharpens the promoted P173 interface. The frozen source package is
`experiments/F196_beta2_carry_factoring_equivalence`, with:

- statement SHA-256
  `07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c`;
- proof SHA-256
  `9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b`;
- source-level hostile-audit SHA-256
  `e9eeddfb8dc5cc9a36119bf6df74da24655e800395afae0848ea297a05c5e263`;
- strict blind-reconstruction SHA-256
  `f39f54088dbec5ed84cda7938521f2c378119e3b7069daf633f447f8061d2b00`.

P173 supplies the audited polynomial-time computation of
\(\binom{N-1}{B}\bmod2^n\) and the signed-carry notation. F198 reproves the
balanced-prime congruence and every new low-bit reduction.

The modern arithmetic-progression terminal was audited in the promoted P172
package `experiments/F195_latest_common_order_beta2_bridge`, with:

- V2 statement SHA-256
  `49df39f6311c00c9fa1fc2f54b7da715783f17da10eec302373fe0fe479e2c3a`;
- V2 proof SHA-256
  `bdbcbcff93de0fb1cee7ecc2783d9edf1fb066f87f9c943bec4ce1d990205bb5`;
- primary-source hostile re-audit SHA-256
  `d0aa16f2872303213af6141fbbdbb2ff8eac60c5f22915045d1ec942ef0e573f`;
- strict blind-reconstruction SHA-256
  `5e08a972df2395228b715ec0439aa7f2f5cf36adc7e62e93a10f75eb40496a64`.

## Primary source for the public offset

Mugurel Ionut Andreica, “A Fast Algorithm for Computing Binomial
Coefficients Modulo Powers of Two,” *The Scientific World Journal*, 2013,
Article ID 751358, DOI
[`10.1155/2013/751358`](https://doi.org/10.1155/2013/751358), PMCID
[`PMC3856163`](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856163/).

Exact interface inherited from the P173 audit:

- precision-\(T\) uniform preprocessing costs
  \(O(T^3\mathsf M(T)+T^4)\) bit operations;
- one main-range query \(\binom P Q\bmod2^T\), with
  \(0\le Q\le P\le2^T-1\), costs
  \(O(T^2\log T\,\mathsf M(T))\) bit operations.

The source has four typographical defects that the P173 source-level audit
resolved from the surrounding definitions:

1. equation (25) combines odd-factorial blocks by multiplication, not
   addition;
2. equation (29) multiplies the odd part by the recursively halved
   factorial, rather than adding it, and uses an integer floor;
3. the Section 3 valuation recurrence uses the preceding index \(Q-1\),
   not the current index on both sides;
4. equation (17), Legendre's formula, requires floors.

Those forced corrections preserve the published complexity. F198 uses the
main range only, with \(T=n,P=N-1,Q=B\), and does not use the Section 9
large-index extension.

## Primary source for the direct arithmetic-progression terminal

Yiming Gao, Yansong Feng, Honggang Hu, and Yanbin Pan, “On Factoring and
Power Divisor Problems via Rank-3 Lattices and the Second Vector,”
Cryptology ePrint Archive, Report 2025/1004, current revision dated
2025-11-11,
[`eprint.iacr.org/2025/1004`](https://eprint.iacr.org/2025/1004), primary PDF
[`eprint.iacr.org/2025/1004.pdf`](https://eprint.iacr.org/2025/1004.pdf).

Exact premise used: Theorem 3.1 takes natural numbers \(N,s\), a modulus
\(m\in(\mathbb Z/N\mathbb Z)^*\), \(s,m<N\), and finds prime divisors
\(p\) satisfying

\[
p\equiv s\pmod m,
\qquad p^r\mid N,
\]

in

\[
O\!\left(
\left\lceil\frac{N^{1/(4r)}}m\right\rceil
\frac{\log^{7+3\epsilon}N}{r^{2+\epsilon}}
\right)
\]

deterministic Turing-machine bit operations, for fixed \(\epsilon>0\).
F198 uses \(r=1\), \(m=2^t\), and \(s=p\bmod2^t\). It uses Theorem 3.1
directly. It does not use Corollary 3.2's stronger premise that every
rational prime divisor of \(N\) lies in the same residue class.

## Primary source for the independent low-bit terminal

Don Coppersmith, “Small Solutions to Polynomial Equations, and Low Exponent
RSA Vulnerabilities,” *Journal of Cryptology* **10** (1997), 233--260,
DOI
[`10.1007/s001459900030`](https://doi.org/10.1007/s001459900030).
The primary PDF is available at
[`link.springer.com/content/pdf/10.1007/s001459900030.pdf`](https://link.springer.com/content/pdf/10.1007/s001459900030.pdf).

Exact premise used: Theorem 5 on pages 253--254 states a deterministic
polynomial-time factorization algorithm for \(N=PQ\) when the low-order

\[
\left\lfloor\frac14\log_2N\right\rfloor
\]

bits of \(P\) are known. Its proof writes
\(P=2^kx+P_0\), \(Q=2^ky+Q_0\), iterates over the possible bit length of
\(P\), and applies the bivariate integer small-root construction to

\[
\bigl((2^kx+P_0)(2^ky+Q_0)-N\bigr)/2^k.
\]

F198 uses this exact low-order-bit theorem, not the preceding high-order-bit
Theorem 4 and not a secondary formulation of a modular Coppersmith bound.
The balanced smaller factor \(p\) is the theorem's \(P\).

## Derivation boundary

All other claims are symbolic consequences of the displayed definitions,
Lucas' theorem, modular inversion modulo powers of two, exhaustive
extension of a bit prefix, and exact candidate verification. No empirical
timing, randomized assumption, unproved heuristic small-root claim, or
experimental mathematical computation is used.
