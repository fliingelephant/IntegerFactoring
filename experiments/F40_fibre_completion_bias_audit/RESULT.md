# Hostile audit of F40: fibre-dependent completion bias

**Artifact audited:** `experiments/F40_fibre_completion_bias_kill/RESULT.md`

**Method:** proof-only.  No computation was run.

## Verdict

**Amendment required; the main rational-map boundary and the degree-one
counterexample survive.**

The following parts are correct after small representation clarifications:

1. the affine conic has \(r-\left(\frac{-1}{r}\right)\) points;
2. a nonconstant rational row- or image-line map of projective degree at most
   \(D+1\) has fibres of size at most \(2(D+1)\);
3. an arbitrary selector among \(B\) such maps has atom at most the sum of
   those fibre bounds;
4. unequal reduced degrees of an explicitly supplied binary-form map over
   \(\mathbb Z/N\mathbb Z\) expose a proper zero divisor by coefficient or
   subresultant gcds;
5. the public quadratic parametrization is an exact same-fibre sampler; and
6. the degree-one constantizer is valid, factor-free once one base completion
   is known, and can make a row or image line constant at both CRT primes
   without a coefficient-asymmetric degeneration.

Two claims are not valid as currently phrased.

* A curve described globally over \(\mathbb Z/N\mathbb Z\) cannot simply be
  called irreducible and then treated as one irreducible curve at both local
  primes.  Its reductions can split.  Nonconstancy on the total reduction
  does not exclude a source-dominating constant component that an arbitrary
  multivalued selector always chooses.  The algebraic-graph atom theorem must
  be stated component-by-component after local reduction, with total degree
  charged across all selectable components.
* Maximum-atom bounds control fresh independent calls, fixed targets, and
  stabilizer exceptional sets.  They do not control equality of two line maps
  of the same source point.  Two nonconstant marginals may be perfectly
  coupled.  This occurs inside the quaternion setting itself: for a fixed
  completion \(C\), P31 gives
  \(\operatorname{im}\beta=J_C\operatorname{row}\beta\) identically while
  both marginal maps are nonconstant.  Equation (13) therefore cannot be
  advertised as covering all P28--P31 line-equality tickets.

The binary-form visibility theorem is proved.  Its one-sentence extension to
multivalued algebraic graphs via unspecified "equivalent eliminant/Chow
forms" is not yet a proof and should be removed or separately formalized.

These defects do not refute the central negative lesson: bounded degree only
makes nonconstant single-line outputs diffuse, while simultaneous constant
degeneration is real and need not yield the named coefficient or unit-menu
extractors.

## 1. Local conic and rank-one charts

For nonzero \(R\in\mathbb F_r\), the standard character sum gives

\[
\#\{(x,y):x^2+y^2=-R\}=r-\chi_r,
\qquad \chi_r=\left(\frac{-1}{r}\right).
\]

The projective closure has \(r+1\) points and has \(1+\chi_r\) points at
infinity, giving the same affine count.  Thus the denominator in the atom
bounds is correct.

The proof-local choice \(s^2+t^2=-1\) always exists: the same count with
\(R=1\) is positive for every odd \(r\).  It need not be computable over
\(\mathbb Z/N\mathbb Z\) without additional work.  F40 uses it only for the
local proof and later explicitly makes global access to composed line forms
an extra hypothesis, so no hidden splitting algorithm is being assumed.

The matrix

\[
\begin{pmatrix}
x+A_c&y+B_c\\
-y+B_c&x-A_c
\end{pmatrix}
\]

has determinant zero and is nonzero because \(z^2+w^2=R\ne0\).  It therefore
has rank one.  The first-row and first-column formulas in (5) and (8) are
correct.

### Base points, poles, and infinity

Suppose first that the completion numerator and denominator have been put in
a common homogeneous degree.  Then \(P_b,Q_b\) are sections of
\(\mathcal O_{\overline C^-}(D+1)\), whose degree is \(2(D+1)\).  For any
target line ([u:v]), a nonconstant map makes
\(vP_b-uQ_b\) a nonzero section, so its zero divisor has degree
\(2(D+1)\).  Every affine preimage of the target is among those zeros.

This remains true at a point where the first row vanishes.  Such a point is a
base point of the displayed pair and is consequently a zero of
\(vP_b-uQ_b\) for every target.  Charging it in the zero divisor only weakens
the bound; the actual extended row is correctly read from the nonzero second
row.  If the first row vanishes identically, the second row gives the same
argument.  Both rows cannot vanish generically because the matrix is
nonzero.  The column argument is identical.

Poles not selected do not contribute an output.  Points handled by another
branch are charged to that branch.  Projective points at infinity are already
included in the divisor degree, so restricting back to the affine fibre
cannot increase the count.

There is one necessary wording correction.  F40 allows \(Z_b,W_b,H_b\) to be
homogeneous forms "all of degree at most \(D\)."  A ratio on a projective
curve and the sums in (5) require common degree.  The theorem should either
require common homogeneous degree from the outset or say that affine forms
of degree at most \(D\) are homogenized to one common degree by powers of
\(T\).  With that correction the stated \(2(D+1)\) bound is valid.

## 2. Arbitrary branch selectors

For a fixed line \(L\), a point-dependent selector among branches can output
\(L\) only at a source point lying in the union of the individual algebraic
preimages of \(L\).  No independence between the selector and the source is
needed.  Therefore

\[
\#\{x:f(x)=L\}\le \sum_b\#f_b^{-1}(L),
\]

which proves (10) for rational branches after the common-degree correction.
The bound is unconditional with respect to the original uniform source.

If evaluation can instead terminate with a factor because a denominator is a
proper zero divisor, the clean probability statement is

\[
\Pr(\text{a no-factor output has line }L)
 \le \frac{2B(D+1)}{r-\chi_r}.
\]

It should not silently be renormalized conditional on the no-factor event;
that conditioning can bias the surviving source points.  Either require that
one unit-denominator branch is selected on every source point of a failure
transcript, or retain the above subprobability formulation.  A large
denominator-factor event is already success for factoring and is not an
obstruction theorem.

### Algebraic graph: the local intersection calculation is sound

On a local irreducible component \(\Gamma\) of the graph, use projective
coordinates \([X:Y:T]\) and \([Z:W:S]\).  The row coordinates are really

\[
XS+T(sZ+tW),\qquad YS+T(tZ-sW),
\]

and similarly for a column.  They are sections of
\(\mathcal O(1,1)|_\Gamma\).  On the normalization of \(\Gamma\), a
nonconstant line map therefore has a target fibre of degree at most

\[
\deg\mathcal O(1,1)|_\Gamma=a_\Gamma+c_\Gamma.
\]

Base points and singular points are included in the divisor degree.
Projecting this finite intersection to the source cannot increase the number
of distinct source points.  This also proves that choosing arbitrarily among
several points of the graph over one source point does not evade the bound.

### Algebraic graph: the global statement needs componentwise hypotheses

The candidate starts over \(A=\mathbb Z/N\mathbb Z\cong\mathbb F_p\times
\mathbb F_q\) and calls \(\Gamma_b\) an "irreducible curve."  Irreducibility
over a product ring is not the local geometric property used in the proof.
Moreover, even an integral model over the integers can have reducible or
nonreduced special fibres.

This matters for an arbitrary multivalued selector.  A local reduction may
have a source-dominating component on which the line map is constant and a
second component on which it is nonconstant.  The map on the total reducible
graph is not constant, yet the selector can choose the constant component at
every source point, producing an atom of one.  This directly defeats (11) if
"nonconstant branch" refers only to the total graph.

A correct statement is:

* normalize every irreducible component of every local reduction that the
  selector may use;
* classify a component that dominates the source and has constant line map as
  a degeneration, not as a nonconstant branch; and
* when all selectable components are nonconstant, sum their
  \(\mathcal O(1,1)\)-degrees in the numerator.

Vertical components cover only finitely many source points and can be charged
by the same total intersection/degree accounting.  Nonreduced multiplicities
should be included in the advertised degree.  Under these corrections the
multivalued atom bound survives.

## 3. Probability quantifiers and inherited Hurwitz tests

Condition on the past before drawing a fresh source point.  If the current
displayed branches are then fixed and every selectable local map is
nonconstant, the current line distribution has maximum atom at most
\(\mu_r\).  For any earlier line \(L_0\), even if the current branch list was
chosen using \(L_0\),

\[
\Pr(L_{\rm new}=L_0\mid\text{past})\le\mu_r.
\]

Thus an adaptive transcript of fresh independent source draws is allowed;
the correct term is "predictable from the past," not necessarily
"transcript-independent."  A union bound controls all polynomially many
cross-call pairs.  A fixed projective transform preserves the atom bound.  If
one chooses adaptively among a displayed menu of \(T\) transforms after
seeing the current point, the safe bound acquires a factor \(T\).

Likewise, membership in the at most fourteen exceptional stabilizer lines has
probability at most \(14\mu_r\).  Unioning the two CRT primes does not require
their events to be independent.  With polynomial branch, degree, call, pair,
and menu counts, this yields the displayed

\[
O\!\left(\operatorname{poly}(n)(1/p+1/q)\right)
\]

bound on an infinite balanced family.

The Hurwitz inheritance invoked from P28--P31 is correctly conditional on the
retained squarefree-modulus, primitivity, norm-\(N\), and handed-normalization
hypotheses.  Left normalization preserves a right-gcd's row space; right
normalization preserves a left-gcd's image space.

### Same-source pairs are not controlled

The collision inequality uses a fresh independent source.  It is false for
two outputs formed from the same source point merely because both marginals
have small atoms.  Abstractly, \(f=g\) can be a nonconstant degree-one map;
then every atom is \(O(1/r)\) but
\(\Pr(f(x)=g(x))=1\).

This is not an artificial example outside the family.  For a residual-only
fixed completion \(C\), P31 proves

\[
\operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta
\]

at every source point, while each marginal is uniform on the supported line
set.  A matching same-source relation is therefore deterministic despite
small marginal atoms.  Whether a *particular public unit menu* contains a
useful asymmetric relation is a separate algebraic question.

Accordingly, (13) covers independent-call line collisions, fixed target
events, and exceptional-line stabilizer tests.  It does not cover same-source
row--image comparisons, two different fibre maps evaluated on one point, or
joint nonlinear transcript decoders.  The verdict and theorem should not say
that the atom bound alone closes every P28--P31 line-equality ticket.

## 4. Coefficient visibility

### Explicit binary-form maps: passed

Let \(P,Q\in A[U,V]\) be homogeneous of common degree \(e\).  Over a local
field, after removing their homogeneous gcd, the resulting morphism has
degree

\[
\delta_r=e-\deg\gcd(P_r,Q_r).
\]

A common factor \(V\) accounts for a cancellation at the dehomogenized point
at infinity, so the homogeneous formulation does not hide a leading-degree
exception.  Equivalently one may use both affine charts.

The full subresultant sequence characterizes the local gcd degree.  If the
two local gcd degrees differ, one subresultant polynomial is zero in one
component and nonzero in the other; at least one of its coefficients is
therefore a proper zero divisor in \(A\).  Taking the integer gcd of that
coefficient with \(N\) factors \(N\).  If \(P,Q\) are both zero in exactly one
component, an input coefficient already separates the components.  Cases in
which one form is zero and the other is not are also covered by the ordinary
gcd convention.

Enumerating all coefficients of all subresultant polynomials, rather than
assuming one preselected principal coefficient is nonzero, handles defective
subresultant patterns.  Sylvester minors have dimension \(O(e)\), their number
and coefficient-list length are polynomial, and they can be evaluated
fraction-free modulo \(N\).  The stated polynomial bit bound follows from
the explicit polynomial bounds on \(e\), coefficient lengths, and input
sizes.

Thus the claim "constant modulo \(p\), nonconstant modulo \(q\) is visible"
is correct for an explicitly supplied binary-form pair.  Equal local reduced
degrees, including two different local constants, need not expose a
coefficient; the qualification in F40 is essential.

### Multivalued algebraic graphs: not proved by the displayed argument

A multivalued graph does not in general descend to one pair
\([P(U,V):Q(U,V)]\) on the source.  An eliminant can encode several possible
line values, components, and multiplicities.  Saying that "equivalent
eliminant/Chow forms" are explicitly computable does not by itself prove that
a one-sided constant component or unequal component degrees force a
coefficient whose gcd with \(N\) is proper.  Bad reduction can also change
the component structure while preserving coarse total eliminant degree.

The rational/binary-form theorem should be retained exactly.  The graph
extension needs a separate precise input format, a definition of the local
degree predicate being compared, a fraction-free construction of its
determinantal conditions, and a proof that the conditions commute with both
CRT reductions.  Until then the graph visibility sentence is unsupported,
though the local graph atom bound remains valid after the componentwise
correction above.

## 5. Public parametrization and exact sampling

The identities (17)--(18) are correct.  Writing
\(A_0=U^2-V^2\) and \(B_0=2UV\), the linear change

\[
(X,Y)=(aA_0-bB_0,\ bA_0+aB_0)
\]

has determinant \(a^2+b^2=-R\in A^\times\), and
\(A_0^2+B_0^2=(U^2+V^2)^2\).  Hence
\(X^2+Y^2=-RT^2\).

Over each local field this is the standard quadratic embedding
\(\mathbb P^1\to\overline C^-\), followed by an invertible linear change.  It
is an isomorphism onto the smooth projective conic, not a two-to-one map.
The three forms have no common projective zero.  No square root or local
quaternion split is used.

Conditional on \((U,V)\) being unimodular in both CRT components, every
global projective parameter has exactly

\[
(p-1)(q-1)=\varphi(N)
\]

representatives.  Thus the parameter is uniform on
\(\mathbb P^1(\mathbb F_p)\times\mathbb P^1(\mathbb F_q)\).  The condition
\(T\ne0\) in each component removes precisely the points at infinity.  The
remaining sets have sizes \(r-\chi_r\), so the output is exactly uniform on
the product of the two affine source conics.

The acceptance claim only needs a minor accounting clarification.  The
ratio \((r-\chi_r)/(r+1)\ge2/3\) is the affine fraction *after* reaching a
projective parameter.  Starting from uniform vectors also contributes
\(1-1/r^2\) per local field.  The direct no-factor affine-output probability
is

\[
\prod_{r\in\{p,q\}}
\frac{(r-1)(r-\chi_r)}{r^2},
\]

which is still bounded below by an absolute constant for distinct odd
primes.  Proper vector or \(T\)-gcds already factor \(N\); simultaneous-zero
cases are rejected.  Standard exact rejection from a power-of-two range
gives polynomial expected random-bit and bit complexity.

The construction assumes one public affine point \((a,b)\) on the residual
fibre.  That is supplied by the existing accepted source point in the F14
setting; it is not a factor-local datum.

## 6. Degree-one constantizer

Let \(u_0\bar u_0=-R\), \(c_0\bar c_0=R\), and
\(h=u_0^{-1}c_0\).  Since \(R\) is a unit, all operations are public and

\[
h\bar h=(u_0\bar u_0)^{-1}(c_0\bar c_0)=-1.
\]

For every fresh \(u\bar u=-R\), setting \(c=uh\) gives
\(c\bar c=R\) and

\[
\beta(u)=u+(uh)j=u(1+hj).
\]

At each local prime \(u\) is invertible.  Left multiplication by its matrix
only takes invertible linear combinations of rows, so

\[
\operatorname{row}\beta(u)=\operatorname{row}(1+hj)
\]

for every source point.  The dual identity
\(\beta(u)=(1+hj)u\) for \(c=h\bar u\) similarly fixes the image line.  These
are genuine degree-one completions.  No local \(s,t\), square root, factor, or
conditioning is hidden in them.

### The \(N=21\) certificate

The displayed values satisfy

\[
u_0\bar u_0=20=-1,\qquad c_0\bar c_0=1,
\qquad h=2+4i,\qquad h\bar h=20=-1\pmod {21}.
\]

Multiplication gives exactly

\[
z=2x-4y,\qquad w=4x+2y,
\]

and \(\alpha=1+hj=1+2j+4k\) has integral norm \(21\).  The displayed nonzero
coefficients are units modulo \(21\).

One can also make the constant row completely explicit without a hidden
split: choose the public split parameters \(s=2,t=4\), which satisfy
\(s^2+t^2=20=-1\pmod {21}\).  Then

\[
A_c=2z+4w=-x,\qquad B_c=4z-2w=y,
\]

and the matrix is

\[
\begin{pmatrix}0&2y\\0&2x\end{pmatrix}.
\]

Its row line is \([0:1]\) everywhere, using the second row when the first
vanishes.  The only nonzero scalar coefficient is the unit \(2\).  This
confirms directly that the local degree drops are synchronized and that the
binary-form coefficient/subresultant detector need not expose \(3\) or \(7\).

The counterexample therefore refutes both unqualified claims identified in
F40: bounded-degree point dependence need not be diffuse, and simultaneous
constancy need not be coefficient-asymmetric.

## 7. What "factor-neutral" can safely mean

A projective line over
\(A\cong\mathbb F_p\times\mathbb F_q\) is exactly an arbitrary pair of local
lines.  Two synchronized degree-zero maps may have different local constant
values without any contradiction or forced zero divisor.  This part of
Section 6 is correct.

For the complete Hurwitz unit menu, success is governed by mismatch of the
two local \(A_4\)-stabilizers.  If both local lines have trivial stabilizer,
the menu fails deterministically.  Since there are only \(O(1)\) exceptional
lines and the P30 supported set has \(r-\chi_r\) elements, such pairs exist
for all sufficiently large local primes.  If the base line comes from P30's
uniform residual-only fibre, the chance of an exceptional stabilizer remains
\(O(1/p+1/q)\).  Cloning the draw cannot amplify that event.

This establishes neutrality only for the named equality, stabilizer, and
unequal-degree coefficient detectors.  It is not an information-theoretic
statement about the public seed.  For example, exact integer lifts also make
\((1+h\bar h)/N\) and other metric statistics available; F40 neither proves
them useful nor proves them useless.  The candidate mostly acknowledges this
by asking for a new selector or nonlinear decoder.  The theorem and verdict
should preserve that narrow wording and avoid saying that simultaneous
constancy is factor-neutral against arbitrary algorithms.

## Required amendments before promotion

1. Require common homogeneous degree for rational numerator/denominator
   forms, or specify a common homogenization from affine forms.
2. State atom bounds as unconditional no-factor-output subprobabilities, or
   require a unit-defined branch on every source point of a failure
   transcript.
3. Replace the global "irreducible graph over \(A\)" premise by local
   componentwise normalization, nonconstancy, and total-degree accounting.
4. Restrict (13) explicitly to fresh independent-call comparisons, fixed
   targets/menus, and exceptional stabilizer events.  Exclude same-source
   paired line maps.
5. Retain coefficient visibility as a theorem for explicitly supplied
   binary forms.  Remove the algebraic-graph eliminant extension until its
   representation and determinantal criterion are proved.
6. Include the missing nonzero-vector factor in the sampler's acceptance
   accounting, while retaining the exact-uniformity conclusion.
7. Qualify "factor-neutral" as relative to the tested direct detectors, not
   all public metric or nonlinear statistics.

With these amendments, the corrected F40 boundary is suitable for a fresh
hostile re-audit.  It is not ready for proof-blind reconstruction in its
current wording.
