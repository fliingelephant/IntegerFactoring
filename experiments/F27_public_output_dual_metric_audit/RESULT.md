# Hostile audit of F27: public output, scaled dual, and the residual cyclic quotient

**Status:** focused hostile audit.

**Artifact audited:** experiments/F27_public_output_dual_metric_kill/RESULT.md.

**Verdict:** **PASS WITH REQUIRED CORRECTIONS.**

The algebraic core is correct.  I found no counterexample to the CRT
intersection identities, Smith forms, fixed-batch output decomposition,
singular cyclic normal forms, duality formulas, exact SVP/CVP statements, or
the stated scope boundary.  The current version is not an unqualified PASS
for two formal reasons in the uniform-line SVP subsection:

1.  That subsection must assume that \(p,q\) are odd.  The report initially
    assumes only distinct primes, while
    \(\left(\frac{-1}{r}\right)\) and the stated formula for
    \(\mathcal S_r\) use the Legendre symbol.  As written, the displayed
    theorem is undefined when \(p=2\).  The intended P30 application already
    has distinct odd primes, so this is a scope correction, not a change to
    the proof.
2.  The projective-line step in (6.7) must explicitly justify that, after
    writing \(v=py\), the reduction \(y\bmod q\) is nonzero.  It is true:
    if \(q\mid y_1,y_2\), then \(N\mid v_1,v_2\), contradicting
    \(\gcd(N,v_1,v_2)=p\).  This also handles all small-prime and zero-reduction
    cases.  The text should state it before asserting equality of projective
    lines.  It should define \(B_\kappa\), for example, as the number of
    primitive integer directions admitting a nonzero representative of
    squared norm at most \(\gamma_2\kappa\).  This makes the finite union
    bound explicit.

Once those two points are inserted, the audited claims pass.  No computation
was used in this audit.

## 1. General output and scaled-dual identities

Let

\[
\Lambda_{\rm out}(A,r)=A\mathbb Z^d+r\mathbb Z^t.
\]

The claimed identity

\[
\Lambda_{\rm out}(A,N)
=\Lambda_{\rm out}(A,p)\cap\Lambda_{\rm out}(A,q)
\]

is exact.  If \(y\) belongs to both local lattices, choose local coefficient
vectors \(x_p,x_q\).  Coordinatewise CRT produces \(x\) with the two
prescribed reductions, and then \(y-Ax\) is divisible by \(pq=N\).
The converse inclusion is immediate.

Consequently, for any \(v\in\Lambda_{\rm out}(A,N)\),

\[
t-v\in\Lambda_{\rm out}(A,r)
\quad\Longleftrightarrow\quad
t\in\Lambda_{\rm out}(A,r).
\]

This does not depend on how \(v\) was selected and therefore applies to
exact or approximate CVP outputs.  It controls local output-module
membership only, not ordinary coordinate gcds of the error.

If \(s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r)\), the local image has
cardinality \(r^{s_r}\).  A target uniform modulo \(N\) therefore has local
membership probabilities

\[
a=p^{-(t-s_p)},\qquad b=q^{-(t-s_q)}.
\]

Its CRT components are independent, so the exclusive-or probability is
exactly

\[
a(1-b)+b(1-a)
=p^{-(t-s_p)}+q^{-(t-s_q)}
-2p^{-(t-s_p)}q^{-(t-s_q)}.
\]

The zero-codimension and rank-mismatch cases are correctly delimited.

Since

\[
\Lambda_{\rm dual}(A,N)
=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t
=\Lambda_{\rm out}(A^{\mathsf T},N),
\]

all intersection, coset-invariance, and uniform-target statements transfer
with ambient dimension \(d\) and the same local ranks.  The dimensions and
transposes in (2.3)--(2.5) are correct.

Both Euclidean duality identities in (2.6) are also exact:

\[
N\Lambda_{\rm out}(A,N)^*=K_N(A^{\mathsf T}),
\qquad
NK_N(A)^*=\Lambda_{\rm out}(A^{\mathsf T},N).
\]

For the first, write a dual vector as \(u/N\).  Pairing with
\(N\mathbb Z^t\) forces \(u\in\mathbb Z^t\), and pairing with
\(A\mathbb Z^d\) is equivalent to
\(A^{\mathsf T}u\equiv0\pmod N\).  For the second, the annihilator of
\(\ker(A\bmod N)\) under the perfect dot-product pairing on
\((\mathbb Z/N\mathbb Z)^d\) is \(\operatorname{im}(A^{\mathsf T}\bmod N)\).
Integer Smith form gives the same statement without invoking finite-ring
duality abstractly.

## 2. Smith form and the no-factor branch

Take \(UAV=S\) in integer Smith form.  Unimodularity gives

\[
U\Lambda_{\rm out}(A,N)
=S\mathbb Z^d+N\mathbb Z^t.
\]

Hence the \(i\)-th nonzero Smith coordinate is
\(\gcd(\sigma_i,N)\mathbb Z\), while every zero row contributes
\(N\mathbb Z\).  Equation (2.1) follows.

If some \(\delta_i=\gcd(\sigma_i,N)\) lies strictly between \(1\) and \(N\),
it is already a public proper divisor.  Otherwise every \(\delta_i\) is
\(1\) or \(N\).  Since \(\sigma_i\mid\sigma_{i+1}\), the \(\delta_i\) form
a divisibility chain, so all \(1\)'s precede all \(N\)'s.  This proves
(2.2).

Transposing \(UAV=S\) gives

\[
V^{\mathsf T}A^{\mathsf T}=S^{\mathsf T}U^{-\mathsf T}.
\]

Therefore \(V^{\mathsf T}\Lambda_{\rm dual}(A,N)\) has precisely the
diagonal form stated in (2.4).  There is no transpose or ambient-dimension
error.

The report correctly refuses to transfer this arithmetic diagonalization
to Euclidean SVP or CVP in the original coordinates.  The matrices \(U\)
and \(V^{\mathsf T}\) are unimodular, not generally orthogonal.  They
preserve the abstract quotient and the ideal generated by all coordinates,
but they can distort lengths and change which vector a metric optimizer
selects.

## 3. Fixed-residual batch

For the \(3\times m\) matrix \(T\), surjectivity

\[
T:(\mathbb Z/N\mathbb Z)^m\longrightarrow
(\mathbb Z/N\mathbb Z)^3
\]

is equivalent to the ideal of maximal minors being the unit ideal modulo
\(N\).  Equivalently,

\[
\gcd(N,\Delta_3(T))=1.
\]

This remains true when different maximal minors witness full rank modulo
\(p\) and modulo \(q\).  If desired, the convention
\(\Delta_3(T)=0\) when all maximal minors vanish can be stated explicitly.
A proper gcd is indeed an immediate factor; gcd \(N\) is the non-surjective,
non-factoring branch.

For

\[
\psi(u,v,s)=(u,v,sz,sw),
\]

the condition \(\gcd(N,z,w)=1\) gives integers \(a,b,c\) with
\(az+bw+cN=1\).  Thus \(sz=sw=0\pmod N\) implies \(s=0\), proving
injectivity.  Surjectivity of \(T\) then gives exactly

\[
\operatorname{im}(A\bmod N)
=Re_1\oplus Re_2\oplus R(0,0,z,w)^{\mathsf T}.
\]

Taking the full integer preimage yields

\[
\Lambda_{\rm out}(A,N)
=\mathbb Z^2\oplus\bigl((z,w)\mathbb Z+N\mathbb Z^2\bigr).
\]

The first two directions are genuinely saturated: a congruence preimage of
each displayed generator can be corrected by a vector in \(N\mathbb Z^4\).

The report also correctly treats these as additional fixed-batch
hypotheses.  P30 supplies \(\gcd(N,z,w)=1\) from the unit
\(z^2+w^2\bmod N\), but supplies neither shared completion data nor
surjectivity of \(T\).

The two-dimensional object is on the output side.  It is not the original
coefficient-side lattice

\[
N\mathbb Z^m+A^{\mathsf T}\mathbb Z^4.
\]

The distinction in dimensions and metric claims is maintained throughout.

## 4. Cyclic normal forms, including singular branches

For \(C\ne0\), write \(C=gC_0\), where \(g=\gcd(z,w)>0\) and \(C_0\) is
primitive, and choose \(D\) with \(\det(C_0,D)=1\).  Put
\(h=\gcd(g,N)\), \(N_0=N/h\).  Since \(g/h\) and \(N/h\) are coprime,

\[
N\mid g\det(C_0,v)
\quad\Longleftrightarrow\quad
N_0\mid\det(C_0,v).
\]

Writing \(v=aC_0+bD\) gives the exact formula

\[
L_C=\mathbb ZC_0+N_0\mathbb ZD,
\qquad \det L_C=N_0.
\]

All three branches are correct:

- \(h=1\): \(L_C=\mathbb ZC_0+N\mathbb ZD\);
- \(1<h<N\): \(h\) is a public proper divisor;
- \(h=N\): the determinant congruence is vacuous and \(L_C=\mathbb Z^2\).

The actual output lattice satisfies

\[
O_C=g\mathbb ZC_0+N\mathbb Z^2
=h\mathbb ZC_0+N\mathbb ZD,
\qquad \det O_C=hN.
\]

Thus \(O_C=L_C\) exactly when \(h=1\).  Under the fixed-batch
unimodularity hypothesis, \(h=1\), so the report's identification of the
output quotient with \(L_C\) is valid.  The discussion of \(h>1\) is a
correct generalization beyond that hypothesis; the outcome paragraph could
make this quantifier transition more explicit.

For \(C=(0,0)\), the separately stated \(L_C=\mathbb Z^2\) is correct, and
the corresponding actual output lattice is \(O_C=N\mathbb Z^2\).

The rotation formulas are exact:

\[
NO_C^*=R(L_C),\qquad NL_C^*=R(O_C).
\]

Indeed \(R(v)\cdot C=-\det(C,v)\), so each identity follows from the
defining congruence and then equality of determinants.  The determinant
checks are

\[
\det(NO_C^*)=N/h=\det L_C,\qquad
\det(NL_C^*)=Nh=\det O_C.
\]

For a prime \(r\mid N\), if \(r\mid g\), the determinant condition is zero
and \(L_{C,r}=\mathbb Z^2\).  Otherwise \(g\) is invertible modulo \(r\)
and

\[
L_{C,r}=\mathbb ZC_0+r\mathbb ZD.
\]

Thus every local rank mismatch is exposed by \(\gcd(g,N)\).  The cheaper
coordinate-gcd branches are also correct for squarefree \(N=pq\): after
proper coordinate gcds have been removed, each coordinate is either a unit
or zero modulo \(N\), and the two cannot both vanish on the residual-unit
branch.

## 5. The two scalar coordinates

On \(h=1\), every ambient vector is uniquely \(aC_0+bD\), and

\[
v\in L_{C,r}\quad\Longleftrightarrow\quad r\mid b,
\qquad b=\det(C_0,v).
\]

For \(v\in L_C\), write \(v=aC_0+NbD\).  A unimodular coordinate change
preserves the ideal generated by the coordinates, hence

\[
\gcd(N,v_1,v_2)=\gcd(N,a,Nb)=\gcd(N,a),
\qquad a=\det(v,D).
\]

The distinction is exact: \(b\) tests local output-module membership, while
\(a\) tests coordinatewise divisibility of a vector already in both local
output modules.

The identities

\[
L_C\cap p\mathbb Z^2=pL_{C,q},\qquad
L_C\cap q\mathbb Z^2=qL_{C,p}
\]

follow by cancelling the other prime in the determinant congruence.  The
minimum length in the \(p\)-divisible slice is therefore
\(p\lambda_1(L_{C,q})\), and symmetrically for \(q\).

## 6. Exact cyclic SVP and quotient geometry

Let \(\ell=\lVert C_0\rVert_2\).  Since
\(\det(C_0,D)=1\), the perpendicular component of \(D\) has length
\(1/\ell\).  Every \(aC_0+NbD\) with \(b\ne0\) consequently has norm at
least \(N|b|/\ell\).  If \(\ell^2<N\), this exceeds \(\ell\), while the
nonzero \(b=0\) vectors are integer multiples of \(C_0\).  Hence the only
shortest vectors are \(\pm C_0\), and their public scalar \(a\) is
\(\pm1\).

Orthogonal projection off \(\mathbb RC_0\) maps a vector to its determinant
coordinate divided by \(\ell\).  Primitivity of \(C_0\) makes that
determinant coordinate range over all of \(\mathbb Z\).  Therefore

\[
\pi(\mathbb Z^2)=\ell^{-1}\mathbb Z,\quad
\pi(L_{C,r})=r\ell^{-1}\mathbb Z,\quad
\pi(L_C)=N\ell^{-1}\mathbb Z.
\]

The faithful quotient is one-dimensional.

On \(h=1\),

\[
L_C=C_0\mathbb Z+N\mathbb Z^2.
\]

Thus

\[
NL_C^*
=\{u\in\mathbb Z^2:C_0\cdot u\equiv0\pmod N\}
=RC_0\mathbb Z+N\mathbb Z^2
=R(L_C).
\]

The primitivity of \(C_0\) ensures that its dot-product kernel modulo \(N\)
is cyclic with this lift.  The resulting rotation theorem concerns only
this rank-two quotient, not the growing-dimensional coefficient-side
scaled dual.

### Uniform-line sparse-SVP theorem

After adding the required odd-prime scope and the explicit nonzero-reduction
sentence identified in the verdict, the theorem is correct.

Hermite's two-dimensional bound gives

\[
\lambda_1(L_C)^2\le\gamma_2N,\qquad \gamma_2=2/\sqrt3.
\]

If a shortest \(v\) has coordinate gcd \(p\), write \(v=py\).  Then

\[
0<\lVert y\rVert^2
\le\gamma_2q/p
\le\gamma_2\kappa.
\]

Moreover \(y\bmod q\ne0\), because otherwise \(N\) would divide both
coordinates of \(v\).  Reducing the determinant condition modulo \(q\)
forces

\[
[C\bmod q]=[y\bmod q].
\]

There are only a constant \(B_\kappa\) of primitive integer directions
admitting such a bounded representative.  Directions reducing to an
isotropic line contribute nothing because \(C\)'s line lies in
\(\mathcal S_q\); collisions among reductions only decrease the union
bound.  Marginal uniformity at \(q\) therefore gives at most
\(B_\kappa/|\mathcal S_q|=O(1/q)\).  This argument is valid for every odd
\(q\), including the finitely many small primes; the implicit constant can
absorb them.  The symmetric event is \(O(1/p)\).

The event quantified is the existence of any factor-revealing shortest
vector, so arbitrary ties are already covered.  No independence between the
two local lines is used.

The report correctly says that P30 does not supply the uniform-completion-line
premise.  P30 conditions on completion data and proves uniformity of the
quaternion row and image lines, not of \([(z,w)]\).

## 7. CVP and bit complexity

In the unimodular coordinates \(t=AC_0+BD\), every
\(v=aC_0+NbD\in L_C\) has error

\[
t-v=(A-a)C_0+(B-Nb)D.
\]

Thus

\[
t-v\in L_{C,r}
\quad\Longleftrightarrow\quad
r\mid B
\quad\Longleftrightarrow\quad
t\in L_{C,r}.
\]

Uniformity of \(t\bmod N\) makes \(B\bmod N\) uniform, so the exact
one-local probability is

\[
\frac1p+\frac1q-\frac2N.
\]

Rotation transfers this result to \(NL_C^*\), but not to the original
rank-\(m\) scaled dual.  Biased target laws remain outside the theorem.

The bit-complexity claims are proportionate to the results.  Integer
Smith/Hermite form and extended Euclid have deterministic polynomial bit
complexity; a Bezout complement \(D\) has polynomial bit length; the basis
\((C_0,ND)\) has polynomial bit length; exact two-dimensional Gauss
reduction and exact fixed-dimensional CVP are polynomial in that bit length.
The report does not claim exact polynomial-time SVP/CVP in growing
dimension.

## 8. Scope audit

The report does not claim a factoring algorithm or a general lattice lower
bound.  In particular, it explicitly leaves open:

- SVP, CVP, and coordinate-gcd extraction in the original
  \(N\mathbb Z^m+A^{\mathsf T}\mathbb Z^4\);
- Euclidean full-lattice behavior after nonorthogonal Smith changes;
- biased completion and target distributions;
- batches without a common completion or without the maximal-minor
  surjectivity condition;
- nonlinear sample combinations and constructions whose informative rank
  grows.

The general intersection and Smith results close determinant,
finite-quotient, and uniform local-membership signals only.  The two-dimensional
metric claims are not silently transferred to arbitrary dimension.

## 9. Valid strengthening not stated in F27

There is a useful exact strengthening of Section 2.

On the no-factor Smith branch, write

\[
U\Lambda_{\rm out}(A,N)
=\mathbb Z^u\oplus N\mathbb Z^{t-u}
\]

and define the public primitive exact-direction lattice

\[
E=U^{-1}(\mathbb Z^u\oplus0).
\]

Then, more strongly,

\[
\Lambda_{\rm out}(A,N)=E+N\mathbb Z^t.
\]

If \(\pi\) is orthogonal projection off \(\mathbb RE\), then

\[
\pi(\Lambda_{\rm out}(A,N))=N\,\pi(\mathbb Z^t).
\]

Indeed every Smith-coordinate vector \((a,Nb)\) differs by an element of
\(\mathbb Z^u\oplus0\) from \((0,Nb)\), and
\(\pi(\mathbb Z^t)=\pi(U^{-1}(0\oplus\mathbb Z^{t-u}))\).  The same exact
direction works locally:

\[
\pi(\Lambda_{\rm out}(A,r))=r\,\pi(\mathbb Z^t)
\qquad(r=p,q).
\]

For the scaled dual, define

\[
E_{\rm dual}
=V^{-\mathsf T}(\mathbb Z^u\oplus0).
\]

Projection off its real span gives

\[
\pi_{\rm dual}(\Lambda_{\rm dual}(A,N))
=N\,\pi_{\rm dual}(\mathbb Z^d),
\]

with the analogous local \(r\)-scalings.

Thus the faithful Euclidean quotient of either general lattice is a uniform
public \(N\)-scaling after the elementary Smith-gcd branches are removed.
This is stronger than the candidate's finite-quotient statement and extends
the one-dimensional collapse in Section 6.

It still does not settle full-lattice SVP/CVP or coordinate-gcd extraction.
The exact-direction lattice can be nonorthogonally coupled to the quotient,
and a metric optimizer in the full lattice may select a vector in or near
that direction whose public coordinates have a factor-correlated gcd.
Accordingly, this strengthening narrows the surviving metric question but
does not contradict any disclaimer in F27.
