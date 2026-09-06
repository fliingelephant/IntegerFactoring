# F151 V3 hostile audit — PASS

## Verdict

**PASS.** V3 repairs the three interfaces that were missing from the V2
statement-only reconstruction. The canonical inverse is now unambiguous,
the exact-value decoder is complete, and the two imported theorems are
stated as external premises with the parameters used by F151.

I found no false claim in the all-component order upgrade, the six named
short-window screens, the factor-free square decoder, the two finite
capability witnesses, the Pilatte catalogue count, or the fixed-coordinate
Jacobi-torus obstruction. The complete short power-bank computation also
has quasipolynomial cost.

This remains a boundary result. It is not an all-input factoring algorithm
and it does not show that the high-order source is factor-correlated.

## Frozen inputs and review history

I read the complete V3 statement and proof, the preserved V1 failure, the
V2 hostile re-audit, the V2 statement-only reconstruction, and the current
manifest. The requested V3 hashes match:

- `V3_STATEMENT.md`:
  `73c8e7a8c58fd3fd40f56f3128ded748313a98cd9b76ec663bee9ec55ba50b98`;
- `V3_PROOF.md`:
  `a4ffebd5cd981ea949850bc2cb71ff34a07ec41969904cf7c46cd05941ca3f57`.

The relevant preserved review hashes also match the manifest:

- V1 failed audit:
  `249eda66360cf80f16257821c58cb1dcffe1495fb028ae9b1a70be29af8448c7`;
- V2 hostile re-audit:
  `64a74cd43084ad3578db218fd1ed8a43e836b33cf6131ba152fe3097fa185fe2`;
- V2 statement-only reconstruction:
  `3158e2011a416827b7be07b4e6105fda61a6a351ea7c31d29118f0e403a0a989`.

I did not edit a frozen candidate file, a prior review, the manifest, or a
durable ledger.

## 1. The external premises match their primary sources

I checked the cited current versions of both papers.

Harvey--Hittmeir, arXiv:2601.11131v2, Theorem 1.1, takes integers

\[
N\geq 3,\qquad 1\leq B<N-1,
\]

and returns either a nontrivial divisor of \(N\), or a unit \(\alpha\) with
\(\operatorname{ord}_N(\alpha)>B\). Its stated bit cost is exactly

\[
O\!\left(
\frac{B^{1/2}\log B}{(\log\log B)^{1/2}}\log N
\right),
\]

subject to the paper's stated small-parameter convention. This is the HH
premise in V3.

Pilatte, arXiv:2404.16450v2, Corollary 1.5, takes

\[
d=\lceil\sqrt{\log N}\rceil,
\qquad
X=d^{1000d},
\]

and \(d\) i.i.d. uniform primes at most \(X\) that do not divide \(N\).
With high probability, their full modular relation lattice has a basis of
Euclidean norm \(\exp(O(d))\). Theorem 3.18 gives the more explicit bound
\(\ll\exp(42d)\) when its extra-generator parameter is zero. V3 imports
only this consequence and correctly does not import a classical basis
finder.

The phrase "the stated generators" in V3 could be made more literal by
copying the words "i.i.d. uniform primes at most \(X\) not dividing \(N\)"
and the displayed definition of the relation lattice. This is an editorial
self-containment improvement, not a mathematical ambiguity in the cited
premise or in Theorem 3's deduction.

## 2. The canonical inverse and exact-value deduplication are sound

For a unit represented in \(\{1,\ldots,N-1\}\), the residue

\[
\iota_N(c)=[c^{-1}]_N
\]

is again in \(\{1,\ldots,N-1\}\). Thus every endpoint product used later is
a positive exact integer congruent to one modulo \(N\).

The first-occurrence rule loses no useful root. If the same exact value
\(A\equiv1\pmod N\) occurs twice in a selected product, deleting the pair
divides the exact product by \(A^2\) and its positive root by \(A\). The
root is unchanged modulo \(N\). Every multiplicity can therefore be reduced
modulo two. A dependency created only by two duplicate columns has root
\(A\equiv1\pmod N\), so it is necessarily trivial.

Discarding \(P_i=1\) is the same special case. Because this V3 decoder uses
endpoint presentations only to construct \(P_i\), it does not have the
root-aware duplicate issue that applies to a decoder supplied with
independent roots.

## 3. The factor-free parity matrix is exact

Repeated gcd splitting produces a gcd-free basis for a finite list of
integers. Extracting an exact perfect power from one block preserves
coprimality with all other blocks and only multiplies that block's exponent
coordinates. Repeating the extraction leaves pairwise-coprime blocks that
are not perfect powers. None is therefore a square.

For a selected column set, write its exact product as

\[
Q=\prod_j g_j^{u_j}.
\]

If all \(u_j\) are even, \(Q\) is a square. If some \(u_j\) is odd, the
nonsquare integer \(g_j\) has a rational prime of odd valuation. No other
block contains that prime because the blocks are pairwise coprime. Its
valuation in \(Q\) is odd, so \(Q\) is not a square. This proves the claimed
equivalence between the binary kernel and exact integer-square closures.

For two closures \(z,z'\), coordinates selected by both contribute one
factor \(A_i\) to the product of their positive roots. Since every
\(A_i\equiv1\pmod N\),

\[
R_{z+z'}\equiv R_zR_{z'}\pmod N.
\]

The root map is a homomorphism. If every vector of one complete kernel basis
mapped into \(\{\pm1\}\), every kernel vector would. Hence any non-global
root forces at least one tested basis vector to have a non-global root.
For such a root, neither gcd with \(R-1\) or \(R+1\) can be one or all of
\(N\); otherwise the root would be globally \(-1\) or \(+1\). Both tests
therefore return proper divisors. This reasoning is valid for general
composite \(N\), not only squarefree semiprimes.

## 4. The all-component order upgrade is exact

Suppose the HH call returns \(\alpha\) with global order greater than \(B\).
If a rational prime \(r\mid N\) had

\[
e=\operatorname{ord}_r(\alpha)\leq B,
\]

then \(r\) would divide \(\gcd(\alpha^e-1,N)\). That gcd cannot equal
\(N\), because this would give global order at most \(e\). It must be a
proper divisor. Thus survival of the full scan proves order greater than
\(B\) in every residue field. The argument also works when \(N\) has
repeated prime factors; V3 correctly makes no prime-power order claim.

## 5. Every displayed short-window screen is null

Put \(L=\lfloor B/4\rfloor\). Modulo any prime \(r\mid N\), a zero in the
four pair screens forces an order relation with positive exponent bounded
respectively by

\[
L-1,\qquad 2(L-1),\qquad 2L,\qquad 4L.
\]

All are at most \(B\). A zero in \(c_e-w_e\) forces
\(\alpha^{2e}=1\), and a zero in \(c_e+w_e\) forces
\(\alpha^{4e}=1\); these exponents are also at most \(B\). Every case
contradicts the strict local-order lower bound. Therefore each gcd in
(14)--(15) is exactly one.

This proof does not extend beyond the named screens. V3 preserves the V1
counterexample channel: larger exponents, a different decoder, and exact
integer effects remain open.

## 6. Quasipolynomial cost survives the complete decoder

The HH cost is quasipolynomial for the permitted \(B\), and the added scan
uses \(B\) modular multiplications and gcds.

The short bank contains at most \(B/4\) exact values. Each is less than
\(N^2\), so the complete input has \(O(Bn)\) bits. Gcd-free refinement,
exact perfect-power testing, binary linear algebra, exact products and
square roots, and the gcd screens all take a polynomial number of bit
operations in this explicit input size. Even forming a separate exact root
for every one of at most \(B/4\) kernel-basis vectors remains
\(B^{O(1)}\operatorname{poly}(n)\). This is quasipolynomial in \(n\).

V3 does not claim that this computation succeeds on every input. It only
defines and bounds the computation whose residual behavior remains open.

## 7. Both capability witnesses are exact

For \(N=143\), \(B=8\), and \(\alpha=2\), the component orders are ten
and twelve. The pairs

\[
(2,72),\qquad(4,36)
\]

are canonical inverse pairs and both have exact product \(144\). This is a
real duplicate despite the certified modular screens.

For \(N=391\), \(B=12\), and \(\alpha=37\), the component orders are
sixteen and twenty-two. The exact values factor over the valid gcd-free
basis \((2,7,37)\) as

\[
2738=2\cdot37^2,
\qquad
392=2^3\cdot7^2.
\]

Their parity columns agree, their product is \(1036^2\), and

\[
\gcd(1035,391)=23,
\qquad
\gcd(1037,391)=17.
\]

Adding the third position in the certified bank cannot remove this kernel
vector. A complete kernel basis therefore detects some useful vector by the
homomorphism argument. The example proves capability only, as stated.

## 8. The Pilatte catalogue boundary is correctly limited

Here \(d=\Theta(\sqrt n)\). For any fixed positive constant \(C\), the
integer ball of radius \(R=\exp(Cd)\) is contained in a cube with
\(\exp(O(d^2))\) points and contains a cube of coordinate radius
\(\lfloor R/\sqrt d\rfloor\), with \(\exp(\Theta(d^2))\) points. Hence
the full ball has

\[
\exp(\Theta(d^2))=\exp(\Theta(n))
\]

points. This is exponential rather than quasipolynomial in the input bit
length. The norm theorem gives no support bound. V3 also says explicitly
that this count is not a lower bound against a structured sampler.

## 9. The fixed-coordinate torus obstruction is exact

For each hidden odd prime \(r\), the local order condition excludes
\(\alpha=\pm1\). Therefore

\[
x^2-1=left(\frac{\alpha-\alpha^{-1}}2\right)^2
\]

is a nonzero local square. Since a Legendre symbol is unchanged by
inversion,

\[
\left(\frac{\Delta^{-1}(x^2-1)}r\right)
=
\left(\frac\Delta r\right).
\]

Jacobi symbol minus one makes the two local signs opposite. Thus the fixed
equation \(x^2-\Delta y^2=1\) has a coefficient \(y\) in exactly one
component and no coefficient modulo \(N\). In the split component a square
root \(s^2=\Delta\) gives

\[
y=\frac{\alpha-\alpha^{-1}}{2s},
\qquad
x+ys=\alpha,
\qquad
x-ys=\alpha^{-1}.
\]

The Chebyshev recurrence reconstructs

\[
T_m(x)=\frac{\alpha^m+\alpha^{-m}}2
\]

for every \(m\geq0\). The formula has no \(\Delta\), so this direct
fixed-coordinate projection loses the explicit split/nonsplit label. V3
correctly limits the obstruction to this splice. It does not close other
torus coordinates or multi-relation decoders.

## Scope conclusion

F151 V3 establishes a useful clean-source boundary:

1. a deterministic QP procedure can certify large order in every hidden
   residue field;
2. that certificate removes the six displayed short-window collision
   screens;
3. the surviving exact-value decoder is well-defined, QP, and genuinely
   capable of exposing a factor on some certified windows;
4. Pilatte's norm theorem alone does not give a QP full-ball search; and
5. the direct high-order-to-fixed-Jacobi-Kummer splice loses its explicit
   orientation.

It does not prove an all-input closure law, a useful-root density, a
classical sampler for Pilatte's lattice basis, or a factoring algorithm.
A fresh statement-only reconstruction is still required before promotion.
