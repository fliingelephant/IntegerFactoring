# Self-audit for F248 V2

## Verdict and repair scope

The V2 statement and proof are internally consistent under their explicit
hypotheses. V2 removes every family-specific specialization from V1. It does
not rely on an undefined marker construction, orientation, or signed-power
grammar.

This audit does not replace a fresh hostile audit or a fresh statement-only
reconstruction.

## Response to the V1 blind findings

The strict V1 reconstruction accepted the general algebraic and counting
arguments but failed on missing family data. V2 repairs that failure by
removal, not by importing a larger construction.

1. V2 makes no family-specific claim that \(K=4\) or \(K=24\). It defines
   \(K=\gcd(E,p-1)\gcd(E,q-1)\) and proves every scalar bound in terms of
   this parameter.
2. V2 makes no family-specific active or trivial root-image claim. It proves
   the exact local criterion
   \(v_2(E)\le v_2(r-1)\) from the cyclic kernel.
3. V2 makes no unconditional claim that \(H\) or \(H'\) is exponential.
   Their exact definitions appear in the statement. Exponential size is an
   explicit premise only in the conditional bank corollary.
4. V2 defines the powering exponent \(W\), the exact local image orders
   \(\rho_r=m_r/\gcd(m_r,W)\), and the clean powered size \(H'\). It assumes
   coprimality directly where the fibre proof needs it.
5. V2 contains no named signed-power grammar and no residual-order marker.
6. Every quasipolynomial-bank conclusion is derived from the explicit
   conditions \(K=2^{o(n)}\), \(H=2^{\Omega(n)}\), or
   \(H'=2^{\Omega(n)}\). The packet does not construct inputs satisfying
   those conditions.

Thus a statement-only verifier does not need any prior project proposition
to reconstruct A--G or the conditional corollary.

## Scalar checks

1. **Kernel size.** The local unit group modulo \(r^2\) has order
   \(r(r-1)\). The assumption \(\gcd(E,N)=1\) removes the \(r\)-part from the
   kernel. Hence its order is exactly \(\gcd(E,r-1)\), and the global order
   is \(K\).
2. **Full-lift square count.** Exact positive squares below \(N^2\) have
   unique positive roots below \(N\). Exactly \(\varphi(N)\) such roots are
   units. Intersecting with the power image gives an upper bound, not an
   equality claim.
3. **Conditional root law.** Reduction modulo \(r\) is injective on the
   \(E\)-kernel modulo \(r^2\), because their orders are respectively
   \(r\) and a divisor of \(r-1\). The local \(E/2\)-power image has size two
   exactly under the displayed two-adic criterion. The one-half conclusion
   is conditional on a reached square and at least one active side.
4. **Principal fibre.** The affine slope is a unit because both \(a\) and
   \(E\) are units. The four canonical roots of \(x^2\bmod N\) give all and
   only the four exact squares below \(N^2\) in the fibre. Exactly two have
   mixed normalized roots.
5. **Second-root equivalence.** A useful digit gives its integer square root
   and a mixed congruence root. A factorization gives both mixed roots by
   CRT, after which the affine digit equation gives both coordinates.
6. **Fixed-past bound.** The proof uses the squarefree kernel
   \(P=du^2\). Exact squareness forces \(B_t=dv^2\), and \(B_t<N^2\) forces
   \(v<N\). Therefore each of the four CRT classes has at most one integer
   representative. At most two have mixed normalized roots. The theorem
   requires \(P\) to be fixed before the fresh coordinate.
7. **Duplicate bound.** A full \(E\)-power fibre modulo \(N^2\) has size
   \(K\). Intersecting it with canonical bases cannot increase it.
8. **Reciprocal-output bound.** If \(uv=R^2\), then \(R\) is one of the four
   roots of one below \(N^2\), and every possible \(u\) divides \(R^2\).
   The theorem does not transfer to the canonical inverse base modulo \(N\).

## Torus checks

1. **Clean raw size.** The local torus order is
   \(m_r=r-(D/r)\). Exactly zero or two local points have \(x=0\). CRT gives
   the product formula for \(H\).
2. **Raw fibres.** Every admitted local \(y\) has the two distinct nonzero
   roots \(\pm x\). Thus every clean global \(y\)-fibre has exactly four
   points. This makes the duplicate probabilities exact.
3. **Pell bound.** An exact row solves
   \(R^2-D_0y^2=1\). Integer-square \(D_0\) leaves only \(y=0\). Otherwise,
   exponential growth of powers of the least Pell unit gives the stated
   logarithmic count. The bound includes \(y=0\).
4. **Powered distribution.** A power homomorphism maps a uniform cyclic
   input uniformly onto its image. Conditioning on the clean set preserves
   uniformity there.
5. **Powered fibres.** The other point with the same local \(y\) is
   \(-U^{-1}\). It belongs to the image exactly when \(-1\) does, hence
   exactly when the image order is even. Coprime local image orders allow at
   most one even side, so global fibres have size at most two.
6. **Powered duplicate law.** If both image orders are odd, a fibre is a
   singleton. If exactly one is even, every clean fibre has two points whose
   roots differ on exactly one hidden side. Ordered-pair counting gives
   \(1/H'\).
7. **Inverse identity.** Expansion gives
   \(A_yA_{N-y}=C^2+D_0N^2\). A square product gives a positive divisor pair
   of \(D_0N^2\), hence at most \(\tau(D_0N^2)\) values of \(C\) and at most
   twice as many \(y\)-values.
8. **Zero coordinate.** The inverse theorem counts only \(y\ne0\). The
   \(y=0\) row is one, and its inverse pair is a global decoy. Therefore it
   is not silently included in the nonzero probability bounds.

## Asymptotic and bank checks

The only asymptotic inputs are proved or stated as hypotheses:

\[
N,\varphi(N)=2^{n+O(1)},
\quad
B_D(N)=O(n),
\quad
S_M=2^{o(n)},
\quad
\tau(D_0N^2)=2^{o(n)}.
\]

A numerical-quasipolynomial bank has

\[
T=2^{(\log n)^{O(1)}}=2^{o(n)}.
\]

The scalar conclusions also assume \(K=2^{o(n)}\). The torus conclusions
also assume the applicable denominator is \(2^{\Omega(n)}\). Products of
the displayed subexponential numerators remain subexponential, including
the \(T^2\) duplicate counts. Division by an exponential denominator gives
\(2^{-\Omega(n)}\).

For the adaptive principal-lift bank, the proof conditions on the full past
at each stage. The \(2/N\) bound therefore survives adaptive choices of one
past product, provided that product is fixed before the new coordinate. It
does not cover post-hoc selection among many products.

## Exact nonclaims

V2 does not claim any of the following:

- an unconditional hard family;
- an unconditional lower bound for \(H\) or \(H'\);
- a bound for an arbitrary powered torus when the local image orders are not
  coprime;
- a bound for a nonduplicate relation between unrelated rows;
- a bound for a mixed scalar-torus product;
- a bound for a post-hoc subset of a retained bank;
- a law for the canonical scalar section \(t=0\);
- a result for the canonical inverse base modulo \(N\);
- an all-input factoring algorithm;
- an unconditional quasipolynomial success or failure theorem.

## Evidence limits

No computation or external literature search was used. The packet makes no
publication-level novelty claim. Fresh hostile and strict statement-only
audits remain required before promotion.
