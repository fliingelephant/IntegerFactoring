# Closed Routes

Record every closed route with what was tried, the exact obstruction, the evidence, and the condition that would make a retry materially new. A theorem-strength missing lemma is a blocked route, not near-completion.

## X01 — generic exact linear compression of arbitrary square classes

**Status:** promoted for the exact linear-rank obstruction and the resulting narrow method failure. The separate \(\mathbb F_7\) one-moment certificate remains candidate because its blind reconstruction has not run.

**Family:** F01.

**Classification:** method failure for the generic compression mechanism; this does not close special structured generators.

**What was tried.** Encode arbitrary positive-integer square classes \(v_i=[a_i]\in\mathbb Q^\times/(\mathbb Q^\times)^2\) by vectors \(e_i\in\mathbb F_2^d\), requiring every dependence in the sketch to be a sound square-product relation.

**Exact obstruction.** Let \(E,V\) be the linear maps from coefficient vectors in \(\mathbb F_2^m\) to the sketch space and the true square-class space. Soundness is \(\ker E\subseteq\ker V\), hence rank-nullity gives \(\operatorname{rank}E\ge\operatorname{rank}V\). For \(m\) distinct rational primes, \(\operatorname{rank}V=m\), so \(d\ge m\) and the sketch forces no nonzero dependence. A generic lower-dimensional exact linear sketch therefore cannot manufacture square relations.

A warning against a one-moment nonlinear slogan occurs in \(\mathbb F_7\): multisets \(\{1,2\}\) and \(\{4,6\}\) have the same first power sum \(3\), but products \(2\) and \(3\), respectively, have opposite quadratic character. (The entries are all distinct; no claim of minimal field size is made.)

**Evidence.** The rank-nullity argument survived a focused hostile audit and a proof-blind end-to-end reconstruction; it is P01 in `PROVED.md`. The explicit \(\mathbb F_7\) calculation passed hostile audit but has not independently been reconstructed.

**What would make a retry materially new.** An efficiently generatable special sample family whose true integer square-class span is proved polynomially bounded for structural reasons, together with a way to compute a nontrivial second modular square root that does not already perform factoring; or a nonlinear reconstruction theorem using enough explicitly bounded moments and surviving adversarial collisions.

## X02 — a fixed synchronized duplication-Lattès instance

**Status:** promoted as the exact fixed-instance obstruction P03. No broader family-level closure is claimed.

**Family:** F02.

**Classification:** evidence against the auxiliary principle that succinctness plus an addition law automatically gives local separation. It is only a fixed-instance obstruction for affine curve-point seeds, not a method failure for the duplication-Lattès family.

**What was tried.** Use the \(x\)-coordinate Lattès map induced by doubling on an elliptic curve, hoping that a succinct orbit-collision discriminant vanishes modulo one unknown prime before the other.

**Exact obstruction and certificate.** Set \(N=15\) and

\[
E:y^2=x^3+2x+1,
\qquad
F(X)=\frac{X^4-4X^2-8X+4}{4(X^3+2X+1)}.
\]

Direct enumeration gives \(\#E(\mathbb F_3)=\#E(\mathbb F_5)=7\). Hence every affine local point is a nonidentity point of order 7. Modulo sign, \(1,2,4\) are distinct in \(\mathbb Z/7\mathbb Z\), while \(2^3=1\), so \(x(P),x(2P),x(4P)\) are distinct and \(x(8P)=x(P)\) in both local components. No local point has \(y=0\), so every duplication denominator \(4y^2\) is a unit. CRT therefore gives, for every affine \(P\in E(\mathbb Z/15\mathbb Z)\),

\[
\gcd(D_m(P),15)=1\quad(m\le3),\qquad
\gcd(D_m(P),15)=15\quad(m\ge4).
\]

Thus even a maximally succinct large-\(m\) collision product has zero separator probability for every distribution supported on the 36 affine points of this fixed CRT curve. Here iterates and differences are defined using stepwise inversion of unit denominators; the orbit repeats with period 3 in \(x\), so \(D_m\) is literally zero for \(m\ge4\). Clearing accumulated denominators changes the product only by a unit.

**Hostile-audit scope correction.** This fixed map can separate CRT components on residue seeds that are not curve points: \(x=2\) has orbit \(2\to9\to7\pmod {15}\), and \(D_3=70\) has gcd 5 with 15. The witness therefore cannot justify a family-level closure. Also, 15 is called smallest only within products of two distinct odd primes; no global minimality over all composite inputs or curves is claimed.

**What would make a retry materially new.** A distributional theorem over randomized curves/seeds proving inverse-polynomial local-threshold separation, together with a genuinely polylogarithmic product circuit; or a synchronized-family obstruction covering that distribution rather than one curve.

## X03 — naive global-\(N\) DDF substitution and uniform linear probes

**Status:** promoted as the exact narrow failures/certificates P06–P08. F03 remains open.

**Family:** F03.

**Classification:** method failure for substituting the global exponent \(N\) into local DDF powers, and evidence against uniform random linear probes. This does not close Berlekamp, resolvent, or Galois-certificate families.

**What was tried.** Generate a low-degree polynomial whose Frobenius cycle types differ modulo two unknown prime factors, then turn that difference into unequal polynomial-gcd degrees over \(\mathbb Z/N\mathbb Z\).

**Exact obstruction.** For \(N=15\) and \(f=X^2+1\), the reduction is irreducible modulo 3 and split modulo 5, and \(\operatorname{Res}(f,f')=4\) is a unit. Nevertheless, using the available exponent \(N\) in the usual DDF powers gives

\[
X^{15^i}-X\equiv -2X\pmod f\quad(i\text{ odd}),
\qquad
X^{15^i}-X\equiv0\pmod f\quad(i\text{ even}),
\]

in both CRT components, so every local gcd-degree profile matches and no zero divisor appears. The correct local tests require \(X^{3^i}-X\) and \(X^{5^i}-X\). At \(i=1\), their CRT-combined difference is \(10X\), whose coefficient has gcd 5 with 15. Thus the currently specified componentwise construction is circular: once that coefficientwise object is constructed, it performs the split. This is not a proof that no alternative global construction exists.

A smaller even witness is \(N=10\), \(f=X^2+9X+5\). It is irreducible modulo 2 and split modulo 5, has unit resultant, yet \(X^{10^i}-X\equiv0\pmod f\) in both components for every \(i\ge1\). Therefore 15 is minimal only after restricting to products of two distinct odd primes; degree 2 is minimal for a squarefree cycle mismatch.

**Cycle-sign limitation.** For a random squarefree quadratic over \(N=pq\) with distinct odd primes, local split/irreducible types disagree with probability \(1/2\), and the immediately available aggregate is a unit discriminant of Jacobi symbol \(-1\). The promise of such a unit is Las Vegas randomized-polynomial-time equivalent to factoring this restricted semiprime class: rejection sampling takes exactly two unit samples in expectation and at most \(15/4\) raw samples, while factoring solves the promise. This is not an information-theoretic assertion that every richer coefficient expression is a unit.

For a split quadratic modulo \(p\), an irreducible quadratic modulo \(q\), and uniform \(B=aX+b\), the exact probability of unequal local gcd degrees is

\[
\frac{2p-1}{p^2}+\frac{p-2}{pq^2}<\frac2p+\frac1{q^2}.
\]

This is exponentially small in the bit length for balanced factors. Conditional on unit \(a\) and monic normalization, the probability is exactly \(2/p\).

**What would make a retry materially new.** A polynomial-size invariant computable with the global input \(N\), not merely the substitution \(r=N\) or unknown component exponents, whose local ranks provably differ with inverse-polynomial probability and whose differing rank is division-free extractable; or a certificate using more than the product/Jacobi image of local cycle types.

## X04 — blind characteristic substitution in a Hasse–Witt formula

**Status:** candidate (initial kill test only; hostile audit and blind reconstruction pending).

**Family:** F05.

**Classification:** method failure for the blind substitution of \(N\) for the local characteristic in the genus-1 Hasse–Witt coefficient; genuinely global geometric invariants remain open.

**Exact certificate.** Let \(N=15\) and \(E:y^2=f(x)=x^3+x+1\). Its discriminant is \(-496\), a unit modulo 15. For an odd prime \(r\), the Hasse–Witt entry is

\[
H_r=[x^{r-1}]f(x)^{(r-1)/2}.
\]

The true entries are \(H_3=[x^2]f=0\) and \(H_5=[x^4]f^2=2\), so their ranks differ. The blind substitution gives

\[
H_{15}^{\rm blind}=[x^{14}]f^7
=\frac{7!}{4!2!1!}=105\equiv0\pmod {15},
\]

so both reductions have blind rank zero. The CRT combination of the true entries is \(12\pmod {15}\), whose gcd with 15 is 3; once this characteristic-dependent combined entry is available, the factor is already exposed.

**What would make a retry materially new.** A geometric operator defined directly and uniformly over \(\mathbb Z/N\mathbb Z\), not by substituting \(N\) into local characteristic formulas or by first selecting each CRT characteristic, together with an inverse-polynomial rank-separation probability and polynomial bit-cost construction.
