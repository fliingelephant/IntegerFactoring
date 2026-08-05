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

## X02 — duplication-Lattès collision products with synchronized local groups

**Status:** candidate (initial kill test only; hostile audit and blind reconstruction pending).

**Family:** F02.

**Classification:** method failure for the standard degree-4 duplication-Lattès map with affine point seeds; not a closure of arbitrary dynamics or arbitrary residue seeds.

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

Thus even a maximally succinct large-\(m\) collision product has zero separator probability for every distribution supported on these point seeds.

**What would make a retry materially new.** A different dynamical family or seed space with a proved inverse-polynomial probability that the local collision thresholds differ, plus a genuinely polylogarithmic product circuit; or a theorem preventing synchronized local dynamics for all admissible inputs.

## X03 — standard cycle-type extraction through squarefree/DDF/resolvent tests

**Status:** candidate (initial kill test only; hostile audit and blind reconstruction pending).

**Family:** F03.

**Classification:** method failure for the standard squarefree factorization, distinct-degree factorization, Berlekamp, and resolvent-root-test instantiations; not a no-go theorem for every Galois certificate.

**What was tried.** Generate a low-degree polynomial whose Frobenius cycle types differ modulo two unknown prime factors, then turn that difference into unequal polynomial-gcd degrees over \(\mathbb Z/N\mathbb Z\).

**Exact obstruction.** For \(N=15\) and \(f=X^2+1\), the reduction is irreducible modulo 3 and split modulo 5, and \(\operatorname{Res}(f,f')=4\) is a unit. Nevertheless, using the available exponent \(N\) in the usual DDF powers gives

\[
X^{15^i}-X\equiv -2X\pmod f\quad(i\text{ odd}),
\qquad
X^{15^i}-X\equiv0\pmod f\quad(i\text{ even}),
\]

in both CRT components, so every local gcd-degree profile matches and no zero divisor appears. The correct local tests require \(X^{3^i}-X\) and \(X^{5^i}-X\). Already at \(i=1\), their CRT-combined remainder is \(10X\), whose coefficient has gcd 5 with 15. Thus constructing the needed componentwise Frobenius action already performs the split.

Cycle-type disagreement itself is too weak: for a random squarefree quadratic it occurs with probability \(1/2\), but is exposed only as a Jacobi symbol \(-1\). The promise of a unit \(\Delta\) with \((\Delta/N)=-1\) is randomized-polynomial-time equivalent to semiprime factoring: rejection sampling generates the promise in expected two unit samples, while factoring solves it.

**What would make a retry materially new.** A polynomial-size invariant computable with the global input \(N\), not component-specific Frobenius exponents, whose local ranks provably differ with inverse-polynomial probability and whose differing rank is division-free extractable; or a certificate using more than the product/Jacobi image of local cycle types.
