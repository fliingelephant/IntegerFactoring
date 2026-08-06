# Fresh hostile re-audit of amended F40

**Artifact audited:** `experiments/F40_fibre_completion_bias_kill/RESULT.md`

**Prior audit retained:** `experiments/F40_fibre_completion_bias_audit/RESULT.md`

**Method:** proof-only. No computation was run.

## Verdict

**Clean pass.** The amended artifact repairs every substantive objection in
the first hostile audit, and I found no new gap that changes its theorem or
scope. It is ready for a fresh context-free proof-blind reconstruction.

In particular, the repaired result now proves only the following narrow
boundary.

* A nonconstant bounded-degree rational row/image map has small individual
  line atoms. With denominator gcds, this is an unconditional probability of
  a no-factor output, not a law renormalized after failures are discarded.
* The analogous graph claim is local, componentwise, and charged by the sum
  of the selectable components' actual \(\mathcal O(1,1)\)-degrees.
* Fresh-call collisions, fixed targets, fixed displayed transform menus, and
  exceptional-stabilizer events inherit those atom bounds. Two maps of the
  same source point do not.
* Unequal local map degrees are coefficient-visible only when the composed
  map is explicitly supplied as a global homogeneous binary-form pair. No
  eliminant or Chow-form extension is asserted for multivalued graphs.
* Simultaneous degree-zero degeneration is genuinely possible. The displayed
  degree-one constantizer realizes it without forcing any of the named direct
  detectors to split \(N\).

The last statement is explicitly detector-relative. The artifact does not
claim information-theoretic neutrality, a lower bound for arbitrary
algorithms, or closure of metric and nonlinear many-sample decoders.

## 1. Local conic, split matrix, and common homogenization

For each odd \(r\mid N\) and nonzero \(R\),

\[
 \#\{(x,y)\in\mathbb F_r^2:x^2+y^2=-R\}
 =r-\left(\frac{-1}{r}\right).
\]

The same count with right side \(-1\) supplies proof-local \(s,t\) with
\(s^2+t^2=-1\). This choice is not claimed to be publicly computable over
\(\mathbb Z/N\mathbb Z\).

With

\[
 A_c=sz+tw,\qquad B_c=tz-sw,
\]

one has \(A_c^2+B_c^2=-(z^2+w^2)=-R\). Therefore the determinant of

\[
 \begin{pmatrix}
 x+A_c&y+B_c\\
 -y+B_c&x-A_c
 \end{pmatrix}
\]

is \(x^2+y^2-A_c^2-B_c^2=0\). The matrix cannot be zero: all four entries
zero would imply \(x=y=0\) in odd characteristic, contrary to
\(x^2+y^2=-R\ne0\). It consequently has rank one at every affine source
point.

The amended rational input model requires \(Z_b,W_b,H_b\) to have one common
homogeneous degree \(d_b\le D\). Equivalently, an affine input is homogenized
to a common degree with powers of \(T\). Hence

\[
 P_b=XH_b+T(sZ_b+tW_b),\qquad
 Q_b=YH_b+T(tZ_b-sW_b)
\]

are honest sections of
\(\mathcal O_{\overline C^-}(d_b+1)\). This closes the former mismatch
between differently graded numerator and denominator forms.

## 2. Rational Bezout bound

Fix a target line \(L=[u:v]\). If the intrinsic row map of a branch is
nonconstant, then

\[
 vP_b-uQ_b
\]

is not identically zero on the smooth projective conic. Its zero divisor has
degree \(2(d_b+1)\le2(D+1)\). Every affine point in the branch domain whose
row is \(L\) is among these zeros.

The base-point discussion is sound. At an isolated point where the first row
vanishes, both \(P_b\) and \(Q_b\) vanish, so the point is charged to the zero
divisor for every target. The rank-one minors show that the extension of the
first-row ratio agrees with the actual second-row line wherever the latter is
needed. If the first row vanishes identically, the second row supplies the
same degree bound; both rows cannot vanish identically because the matrix is
nonzero. Points at infinity and unused poles can only enlarge the divisor
count relative to the selected affine domain.

The first-column/image formula has the same degree and the identical
argument. Thus each nonconstant rational branch has at most \(2(D+1)\)
preimages of one row or image line.

For a point-dependent selector among \(B\) displayed branches, the source
points outputting \(L\) lie in the union of these \(B\) algebraic fibres.
No independence between selector and source is needed. This proves the
factor \(B\) in (10).

## 3. Denominators and probability accounting

The repaired statement no longer conditions on survival of denominator
tests. If a selected denominator is a proper zero divisor, the execution has
already factored \(N\). Otherwise, for every fixed target \(L\),

\[
 \Pr(\text{no-factor output whose local line is }L)
 \le {2B(D+1)\over r-\chi_r}.
\]

This follows directly from the union of algebraic preimages and remains true
even if branch selection depends on the full current CRT point. It is not
renormalized by dividing by the probability of no factor. The stronger
maximum-atom formulation is invoked only in the explicitly stated case in
which a unit-defined branch is selected for every possible fresh source
point after the past transcript is fixed. Input-dependent rejection is
excluded by the model.

This distinction is sufficient for all later uses: on executions where a
denominator factor has not already ended the algorithm, the probability of
a named no-factor ticket is bounded unconditionally by the same numerator.

## 4. Componentwise algebraic-graph bound

The amended graph theorem no longer speaks of an irreducible object over the
product ring. It reduces locally first and normalizes every selectable
irreducible component \(\Gamma\). On such a component the cleared row (or
column) coordinates are bihomogeneous of bidegree \((1,1)\), hence sections
of

\[
 \mathcal L=\pi_-^*\mathcal O(1)\otimes
             \pi_+^*\mathcal O(1).
\]

Writing

\[
 a_\Gamma=\deg\pi_-^*\mathcal O(1),\qquad
 c_\Gamma=\deg\pi_+^*\mathcal O(1),
\]

gives \(\deg\mathcal L=a_\Gamma+c_\Gamma\). If the intrinsic line map on a
source-dominating component is nonconstant, a target fibre is the zero
divisor of a nonzero section of \(\mathcal L\), so its degree is at most
\(a_\Gamma+c_\Gamma\). Projecting to the source cannot increase the number
of distinct source points.

The exceptional component cases are also correctly accounted for.

* A constant source-dominating component is explicitly called a degeneration
  and excluded from the nonconstant theorem.
* A vertical curve has one source image and positive completion degree, so
  charging it to the advertised total degree is safe.
* Multiple graph values above one source point cannot evade the bound,
  because every value selected for the target belongs to one of the summed
  component intersections.
* Singularities, component intersections, and nonreduced multiplicities only
  increase the scheme-theoretic degree budget.

Summing over every selectable component of every branch proves (11). The
artifact explicitly disclaims global computability of the local
decomposition, so no hidden factor-dependent algorithmic step is being used.

## 5. Fresh-call adaptive quantifiers, and the same-source exclusion

Condition on the whole past immediately before a new draw. The displayed
branch list may depend arbitrarily on that past, but is then fixed; the next
source point is fresh and uniform. Therefore, for every past-measurable
target line, the new line has probability at most the applicable atom bound.

This proves sequential adaptive collision bounds: after the first line is
known, it is merely a fixed target for the independent fresh call. Unioning
over polynomially many ordered cross-call pairs, fixed targets, and
past-predictable menus is valid. A selector among \(T\) displayed projective
bijections after seeing the current point contributes the stated factor
\(T\). The at-most-fourteen exceptional stabilizer lines contribute the
same finite-union factor. No independence between the two CRT-prime events
is assumed.

The repaired text now expressly excludes the invalid inference for two maps
of one source point. Small marginal atoms do not bound a coupled equality;
indeed the inherited identity

\[
 \operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta
\]

is deterministic while both marginals can be diffuse. Equation (13), the
theorem, the verdict, and the retry conditions all preserve this exclusion.

## 6. Binary-form degree visibility

The accessibility hypothesis is now exact. The composed map must be supplied
as a labelled pair

\[
 [P(U,V):Q(U,V)]
\]

of common-degree homogeneous binary forms over \(A\). For a local field,
removing the homogeneous gcd gives a morphism of degree

\[
 \delta_r=e-\deg\gcd(P_r,Q_r).
\]

Homogeneous subresultants determine this gcd degree and commute with
reduction to both CRT fields. If \(\delta_p\ne\delta_q\), choose an index at
which the appropriate subresultant polynomial is zero in one component and
nonzero in the other. At least one displayed coefficient is then a proper
zero divisor modulo \(N\). Cases in which a whole form pair vanishes in only
one component are caught directly by input coefficients. Treating both
projective charts, or equivalently using the homogeneous construction,
includes common factors at infinity and leading/content degeneration.

Enumerating all coefficients, rather than one principal subresultant
coefficient, covers defective patterns. The number and size of the relevant
Sylvester determinants are polynomial in the explicitly bounded degree and
coefficient lengths, and no modular division is required.

Crucially, the artifact stops there. It makes no analogous claim for a
multivalued graph and specifically explains why an eliminant can mix
components and multiplicities. This fully repairs the former unsupported
Chow-form sentence.

For the synchronized constant example, the phrase “variation
minor/subresultant” is correctly read as the predicates that would witness a
positive or unequal reduced degree: those vanish in both CRT components.
The terminal nonzero member of a full subresultant sequence need not vanish,
but it is supported in both components and hence yields gcd \(1\), not a
proper factor. This does not affect the stated coefficient-clean
certificate.

## 7. Public parametrization and exact sampler

Set \(A_0=U^2-V^2\), \(B_0=2UV\). The linear map

\[
 (A_0,B_0)\longmapsto
 (X,Y)=(aA_0-bB_0,bA_0+aB_0)
\]

has determinant \(a^2+b^2=-R\), a unit in both CRT components, and
\(A_0^2+B_0^2=(U^2+V^2)^2\). Thus (17)--(18) give the standard
base-point-free quadratic isomorphism from \(\mathbb P^1\) to the smooth
projective conic, without a square root or local split.

For uniform \((U,V)\bmod N\), the test
\(\gcd(U,V,N)=1\) is exactly the event that the vector is nonzero in each
local field. Conditional on that event, every global projective parameter
has \((p-1)(q-1)=\varphi(N)\) representatives. The additional unit test on
\(T=U^2+V^2\) removes exactly the projective points at infinity. Therefore
the accepted affine output is exactly uniform on
\(C^-_p\times C^-_q\).

Counting before any conditioning, the per-prime number of vectors that are
both nonzero and affine is

\[
 (r-1)(r-\chi_r).
\]

The direct no-factor affine-output probability is consequently

\[
 \prod_{r\in\{p,q\}}
 { (r-1)(r-\chi_r)\over r^2},
\]

exactly as amended. A vector zero in exactly one component, or a \(T\) zero
in exactly one component, returns a proper factor. Simultaneous-zero events
are rejected. The displayed product is bounded below by an absolute
constant for distinct odd primes, so repeated exact trials have polynomial
expected random-bit and bit complexity. This closes the missing
nonzero-vector factor from the first audit.

## 8. Degree-one constantizer

From

\[
 u_0\bar u_0=-R,\qquad c_0\bar c_0=R,
\]

the public element \(h=u_0^{-1}c_0\) satisfies

\[
 h\bar h=(-R)^{-1}R=-1.
\]

For every fresh \(u\bar u=-R\), the completion \(c=uh\) has
\(c\bar c=R\), and associativity gives

\[
 \beta(u)=u+(uh)j=u(1+hj).
\]

The local matrix of \(u\) is invertible because its norm is a unit. Left
multiplication therefore applies invertible row operations, proving that the
row line of \(\beta(u)\) is the fixed row line of \(1+hj\). Dually,
\(c=h\bar u\) and \(j u=\bar u j\) give

\[
 \beta(u)=(1+hj)u,
\]

so invertible right multiplication fixes the image line. Both completions
are degree-one global formulas, and computing \(u_0^{-1}\) uses only the
assumed unit \(R\).

This is a synchronized degree-zero line map at both CRT primes, not a
one-sided degree drop. It therefore lies outside the small-atom hypothesis
and does not trigger the unequal-degree theorem.

## 9. Independent check of the \(N=21\) certificate

With

\[
 u_0=2-4i,\quad c_0=-1,\quad h=2+4i,
\]

one has

\[
 u_0\bar u_0=20=-1,\qquad c_0\bar c_0=1,
 \qquad h\bar h=20=-1\pmod {21}.
\]

Multiplication by \(h\) gives

\[
 z=2x-4y,\qquad w=4x+2y.
\]

Also

\[
 \alpha=1+hj=1+2j+4k,
 \qquad \operatorname{nrd}(\alpha)=1+4+16=21.
\]

Every displayed nonzero scalar coefficient is coprime to \(21\). Taking
\(s=2,t=4\), whose squared norm is \(20=-1\pmod {21}\), gives

\[
 A_c=2z+4w=20x=-x,
 \qquad B_c=4z-2w=-20y=y.
\]

Thus

\[
 \beta=
 \begin{pmatrix}0&2y\\0&2x\end{pmatrix}.
\]

Since \(x^2+y^2=-1\) in both \(\mathbb F_3\) and \(\mathbb F_7\), the two
rows cannot vanish simultaneously. The row line is globally \([0:1]\), and
the surviving coefficient \(2\) is a unit at both primes. The certificate
therefore demonstrates simultaneous constancy with no coefficient or
degree-asymmetry factor. Nothing in this check uses a computation or a
hidden local choice.

## 10. Narrow meaning of detector-neutrality

A projective line over
\(A\simeq\mathbb F_p\times\mathbb F_q\) is an arbitrary pair of local lines.
Synchronized degree zero does not require the two local constants to have the
same coordinate description. Pairwise equality of cloned row lines holds at
both primes, and the full Hurwitz-unit test depends only on whether the two
local \(A_4\)-stabilizers differ.

There are only constantly many exceptional local lines. On sufficiently
large primes, one can choose supported lines with trivial stabilizer at both
primes and combine the corresponding data by CRT; the unit-menu mismatch is
then absent deterministically. If instead the base quaternion is drawn from
the P30 residual-only fibre, its line has the inherited uniform supported
law, so constantization merely clones that one draw and leaves the
exceptional-stabilizer probability \(O(1/p+1/q)\).

The artifact carefully limits “neutral” to direct line equality, the fixed
stabilizer menu, and unequal-degree coefficient/subresultant tests. It
expressly leaves canonical integer lifts, magnitude statistics, metric
functions of \(h\), adaptive conditioning, and nonlinear joint decoders
open. The counterexample therefore supports exactly the advertised negative
lesson and no stronger lower bound.

## Final authorization

All seven amendments required by the first hostile audit are present and
mathematically sufficient. The amended F40 artifact passes hostile
re-audit and may proceed to a fresh context-free proof-blind
reconstruction. This verdict alone does not promote F40 and is not a
cross-family audit.
