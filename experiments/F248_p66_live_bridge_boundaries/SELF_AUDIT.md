# Self-audit for F248

## Audit scope

This audit checks every asymptotic and algebraic claim in `STATEMENT.md`
against `PROOF.md`.  It uses no computation.  It does not replace a fresh
hostile audit.

## Scalar-lift checks

1. **Power-map kernel.**  The proof uses \(\gcd(E,N)=1\).  Without it, the
   kernel modulo \(p^2\) or \(q^2\) can contain the prime-power part, and
   \(K=g_pg_q\) is incomplete.  The assumption is stated.

2. **Square count below \(N^2\).**  A positive exact square below \(N^2\)
   has one positive root below \(N\).  Restricting to unit outputs leaves
   exactly \(\varphi(N)\) possible integer squares.  This gives an upper
   bound because some squares can be absent from the power-map image.

3. **Conditional half law.**  The half law is conditional on a fixed square
   output and on at least one active local kernel-root image.  It is not a
   lower bound on the probability of reaching a square.  The packet does not
   apply it to \(E=N^2-1\) on P209, where both local images are trivial.

4. **Principal-fibre count.**  The affine slope is a unit only because both
   \(a\) and \(E\) are units modulo \(N\).  The four roots modulo a distinct
   odd semiprime give four distinct positive squares below \(N^2\), and the
   affine digit permutation reaches each exactly once.

5. **Canonical section.**  Uniformity over all \(t\bmod N\) gives no law for
   the fixed section \(t=0\).  The packet leaves that bias open.

6. **Duplicate event.**  Equality modulo \(N^2\) implies membership in the
   \(E\)-kernel modulo \(N\), but the converse need not hold.  The result is
   correctly stated as an upper bound.

7. **Reciprocal-output scope.**  The divisor proof uses
   \(v=[u^{-1}]_{N^2}\).  It does not apply to the source value obtained from
   the canonical inverse base modulo \(N\).  This exclusion appears in the
   theorem, proof, and provenance.

8. **Reciprocal root count.**  If \(uv=R^2\), then \(0<R<N^2\) and
   \(R^2=1\bmod N^2\).  There are exactly four canonical choices for \(R\).
   For each, every admissible \(u\) divides \(R^2\).  The divisor bound is an
   upper bound; it does not assume that every divisor is a valid output.

## A repaired proof and a rejected overclaim

An intermediate justification for the fixed-past \(2/N\) law was invalid.
A mixed normalized root fixes the final integer square root only modulo
\(N\), not as an integer.  Several lifts

\[
S=s_0+\ell N
\]

can have the same residue, so this observation alone does not fix the fresh
digit.

The theorem itself is repaired by the squarefree kernel.  Writing
\(P=du^2\), exact squareness of \(PB_t\) forces \(B_t=dv^2\).  The strict
bound \(B_t<N^2\) gives \(v<N\).  The four CRT classes for \(v\) therefore
have at most one integer representative each, and their normalized-root
images are injective.  At most two are mixed.  This is the proof used in
`PROOF.md`.

The theorem assumes \(P\) is fixed before the fresh lift coordinate is
sampled and \(P\) is a unit modulo \(N\).  It cannot be union-bounded over
all exponentially many subsets of a retained bank.  If \(P\) is not a unit,
a factor-first gcd screen has already exited.

An associated “carry-zero pair” formulation conflated an arbitrary lift row
with the square of a complementary residue.  It is excluded.  The valid
singleton statement is already contained in the principal-fibre theorem.

## Torus checks

1. **Integer representative of \(D\).**  Exact-square and Pell statements use
   the positive canonical integer \(D_0=[D]_N\), not a signed formal
   representative.  The congruence root uses only \(D_0=D\bmod N\).

2. **Clean-set size.**  A local norm-one torus has order
   \(r-(D/r)\).  The number of local points with \(x=0\) is zero or two and
   equals \(1+(-D/r)\).  Conditioning on \(x\) being a unit gives the stated
   product size.

3. **Raw \(y\)-fibres.**  Every admitted local \(y\) has two distinct roots
   \(\pm x\).  Hence every global admitted \(y\) has four points.  This makes
   the raw duplicate probabilities exact, not only upper bounds.

4. **Pell count.**  If \(D_0\) is a square, factorization of
   \(R^2-D_0y^2=1\) leaves only \(y=0\).  If it is nonsquare, the fundamental
   positive unit is larger than \(2\sqrt{D_0}\), and \(y<N\) gives the stated
   logarithmic count.  The count includes \(y=0\).

5. **Powered \(y\)-fibres.**  The second local point with the same \(y\) is
   \(-U^{-1}\).  It lies in the image subgroup exactly when \(-1\) does,
   equivalently when the subgroup order is even.  Removing \(x=0\) removes
   the only fixed cases.  Coprime local image orders permit at most one even
   side, so the global fibre has size at most two.

6. **Marker scope.**  The P209 exponential lower bound for \(H'\) is asserted
   only for the P208/P209 square exponent \(N^2-1\) and for the signed-power
   grammar covered by P209.  An arbitrary exponent can absorb a marker and
   make the image small; F248 makes no claim in that case.

7. **Inverse-point identity.**  Direct expansion gives exactly
   \(A_yA_{N-y}-C^2=D_0N^2\).  If the product is square, both factors
   \(R-C\) and \(R+C\) are positive because \(R>|C|\).  Divisor pairs give at
   most \(\tau(D_0N^2)\) values of \(C\), and each quadratic equation for
   \(y\) gives at most two integer roots.

8. **Divisor asymptotic.**  Since \(D_0N^2<N^3\), it has \(O(n)\) bits.
   The standard divisor bound gives \(2^{o(n)}\), which is sufficient against
   an image size \(2^{\Omega(n)}\).  The proof does not claim that this
   divisor enumeration is quasipolynomial-time.

## Decoder-boundary check

The probability bounds address only:

- one row;
- an exact duplicate;
- one specified reciprocal pair;
- one specified torus inverse pair.

They do not constrain an unrelated nonduplicate pair or the parity kernel of
several distinct rows.  In particular, source-group order markers do not
determine the ordinary integer
prime factors of \(1+D_0y^2\) or \([a^E]_{N^2}\).  No route-wide negative
claim follows.

## Complexity check

Every source value and exponent named in the packet has \(O(n)\) or
polynomially many bits.  The conclusions about quasipolynomial banks use
only union bounds of a \(2^{o(n)}\) bank against a \(2^{-\Omega(n)}\) event.
No hidden enumeration of all \(N\) lift digits or all Pell/divisor solutions
is presented as an algorithm.

## Novelty and evidence limits

- No numerical evidence was generated.
- No cross-family audit was run.
- No external literature review was run.
- The packet is a collection of exact source boundaries and one exact
  second-root equivalence.  It makes no publication-level novelty claim.
- A fresh hostile proof audit is still required before promotion.
