# Fresh hostile re-audit of F38 — horizontal fused matchgate strips

**Audited artifact:**
`experiments/F38_horizontal_matchgate_strip_kill/RESULT.md`.

**Prior material used:** the F20 registry row, P46/X40, and the historical
first F38 audit.  The historical audit was used only as a checklist of the
promised amendment and optional clarifications; its verdict was not assumed.

**Verdict:** **PASS AS WRITTEN.**

The amended artifact proves its exact tensor identity, multiplicity-one
claim, planar contiguous cut, rank formula, and characteristic-zero
matchgate-orbit obstruction for every integer \(L\geq1\).  The mandatory
pure-spinor correction is present and correct.  Both optional clarifications
from the first audit are also present, and neither introduces a new
inconsistency.  I found no further mathematical amendment.

No computation was used.

## 1. Amendment audit

The historical mandatory correction concerned the decomposition

\[
\omega=\omega_I+\omega_O+\omega_{IO}.
\]

The amended Section 5 now says exactly that the two local terms
\(\omega_I\) and \(\omega_O\) act by invertible row and column maps,
respectively, while the cross term \(\omega_{IO}\) controls the remaining
rank.  This is the correct division of roles.  The artifact no longer treats
the cross term as a one-sided operation.

The two prior optional clarifications are also incorporated:

1. Section 2 explicitly evaluates each Boolean relation over the integers
   before embedding its truth value as \(0\) or \(1\) in the coefficient
   field.
2. Section 3 supplies a clockwise port order, fixes the physical order of the
   two horizontal lanes, discusses their lens faces, and checks both endpoint
   cells and \(L=1\).

These additions agree with the tensor definition and with the cut used in the
rank proof.

## 2. Tensor definition, field semantics, and multiplicity

Before fusion the \(L\) cells have \(8L\) leg incidences.  Each of the
\(L-1\) shared \(y\)-edges and \(L-1\) shared carry edges consumes two
incidences, leaving

\[
8L-4(L-1)=4L+4
\]

external Boolean legs.  The displayed sets \(I_L\) and \(O_L\) each contain
\(2L+2\) legs, so the definition neither omits nor silently contracts an
external leg.

The field-independent semantics are precise.  In each local cell the
statements

\[
x_i^-=x_i^+,qquad y_i=y_{i+1},qquad
a_i+c_i+x_i^-y_i=s_i+2c_{i+1}
\]

are integer statements on Boolean values.  Their truth values are then
embedded in an arbitrary field \(K\).  In particular the last equality is
not reduced modulo \(\operatorname{char}K\).  This avoids the characteristic
two ambiguity that would arise from interpreting the indicator as a field
polynomial equation.

For a nonzero summand, equality propagation forces

\[
x_i^-=x_i^+=x_i,qquad y_0=\cdots=y_L=y.
\]

Multiplying the local full-adder equations by \(2^i\) and summing cancels
each internal \(2^ic_i\) once from each side and leaves exactly

\[
A+yX+c_0=S+2^Lc_L.
\]

This proves the forward direction of the closed relation.

Conversely, fix external values satisfying the closed relation.  The
internal \(y\)-word is forced.  Starting from the exposed \(c_0\), the
ordinary binary full-adder recurrence uniquely determines each pair
\((\widehat s_i,\widehat c_{i+1})\), because its input sum lies in
\(\{0,1,2,3\}\).  It yields

\[
A+yX+c_0
=\sum_{i=0}^{L-1}2^i\widehat s_i+2^L\widehat c_L.
\]

The represented integer lies between \(0\) and \(2^{L+1}-1\).  The exposed
word \((s_0,\ldots,s_{L-1},c_L)\) is another \((L+1)\)-bit representation
of the same integer, so uniqueness of binary expansion makes it identical
to the recursively generated word.  Hence there is exactly one internal
carry assignment and exactly one internal \(y\)-assignment.  When \(L=1\),
both contracted-index sets are empty and have the unique empty assignment.

Thus every fused-tensor entry is genuinely \(0\) or \(1\), rather than a
positive multiplicity that could vanish in some field.  The claimed tensor
identity over every field follows.

## 3. Planar rotation and cyclic contiguity

The amended clockwise order on cell \(i\), starting along the top, is

\[
x_i^-,a_i,\ y_{i+1},c_{i+1},\ x_i^+,s_i,\ c_i,y_i.
\]

Consequently the right-side ports occur physically from top to bottom as
\(y_{i+1},c_{i+1}\), while the left-side ports occur physically from top to
bottom as \(y_i,c_i\) (clockwise traversal goes upward on the left side and
therefore lists them as \(c_i,y_i\)).  Like labels on adjacent disks can be
joined in two parallel horizontal lanes with the \(y\)-lane above the carry
lane.  The endpoint orders agree, so the two curves do not cross.

The two relevant ports are consecutive on both facing disk boundaries.  The
bounded lens between the parallel curves therefore contains no external
port.  Separate inter-cell corridors are disjoint, and every upper or lower
external leg exits away from these corridors.  This supplies an actual
planar embedding rather than merely a planar-looking incidence graph.

A regular outer boundary encounters four groups cyclically:

1. top ports \((x_i^-,a_i)\), all in \(I_L\);
2. right endpoint ports \((y_L,c_L)\), both in \(O_L\);
3. bottom ports \((x_i^+,s_i)\), all in \(O_L\); and
4. left endpoint ports \((y_0,c_0)\), both in \(I_L\).

The fourth and first groups meet across the cyclic starting point.  Their
union is therefore one cyclic boundary interval, and the second and third
groups form its complementary interval.  The fact that the displayed row
index lists all \(x\)'s before all \(a\)'s is harmless: it is only a
permutation within the input arc, just as the displayed output indexing is a
permutation within the output arc.

For \(L=1\) there is one disk and no lens.  The same clockwise order gives
the P46 input arc across the starting point and the complementary output arc.
For \(L>1\), the unpaired \((y,c)\) ports at both endpoints go directly into
the outer face.  Thus neither the base case nor an endpoint invalidates the
contiguous-cut certificate.

## 4. Exact rank calculation

Across \(I_L\mid O_L\), the propagation indicators force the incoming and
outgoing labels

\[
(x_0,\ldots,x_{L-1},y)
\]

to agree.  Distinct labels occupy disjoint row sets and disjoint column sets,
so the flattening is a direct sum of exactly \(2^{L+1}\) blocks.  This remains
true when two different labels happen to have the same numerical value
\(Q=yX\).

For a fixed label, rows are indexed by \((A,c_0)\) and columns by

\[
W=S+2^Lc_L\in\{0,\ldots,2^{L+1}-1\}.
\]

Every row is the standard basis row supported at

\[
W=Q+A+c_0.
\]

Since \(A\in\{0,\ldots,2^L-1\}\) and \(c_0\in\{0,1\}\), the value
\(A+c_0\) runs through exactly \(0,\ldots,2^L\).  The endpoint values have
one preimage and every strict interior value has the two displayed
preimages.  The used columns are therefore exactly

\[
Q,Q+1,\ldots,Q+2^L.
\]

They are all legal: \(0\le Q\le2^L-1\) implies
\(Q+2^L\le2^{L+1}-1\).  The distinct used standard basis rows are linearly
independent over every field, giving

\[
\operatorname{rank}B_Q=2^L+1.
\]

Ranks add over the direct sum, hence

\[
\operatorname{rank}M_L=2^{L+1}(2^L+1).
\]

For \(L=1\), this is four propagation-label blocks of rank three, totaling
\(12\), exactly as in P46.  The calculation uses neither division nor
cancellation of tensor contributions and is characteristic-independent.

## 5. Pure-spinor obstruction

The imported P46 statement has the exact hypotheses needed here: a nonzero
matchgate/pure-spinor signature over a characteristic-zero field has
power-of-two ordinary flattening rank across complementary contiguous cyclic
arcs.  The all-zero assignment proves that the F38 tensor is nonzero, and
Section 3 supplies the required cut.

The amended proof recap is internally consistent:

* particle-hole Clifford toggles are signed coefficient-basis permutations
  and tensor-product Pauli strings in Jordan--Wigner form, so they preserve
  purity and the selected ordinary flattening rank;
* a nonzero coefficient can therefore be moved to the vacuum coefficient,
  covering odd and degenerate charts as well as the generic even chart;
* in the vacuum chart, wedge multiplication by
  \(\exp(\omega_I)\) and \(\exp(\omega_O)\) gives invertible operations on
  the two one-side exterior spaces; and
* if the rectangular matrix of \(\omega_{IO}\) has rank \(r\), separate
  basis changes put it into \(r\) paired terms
  \(\sum_{k=1}^r u_k\wedge v_k\), whose subset expansion has flattening rank
  \(2^r\).

Here \(r\) is the rank of the rectangular cross matrix; there is no missing
factor of two from the rank of the associated full skew-symmetric matrix.
Contiguity is essential because it permits the two mode sets to be ordered as
blocks.  Cyclic-rotation and exterior-ordering signs on a fixed-parity spinor
are absorbable as invertible row or column signs, exactly within the promoted
P46 lemma.  The amended artifact does not invoke the false arbitrary
interleaving version.

For every \(L\ge1\), the factor \(2^L+1\) is odd and greater than one.
Therefore

\[
2^{L+1}(2^L+1)
\]

is not a power of two, contradicting the necessary rank form for a matchgate
on this contiguous cut.

## 6. Gauges and exact exclusions

An independent \(\mathrm{GL}_2\) transformation on every exposed input leg
left-multiplies the flattening by an invertible Kronecker product; the
corresponding transformations on exposed output legs right-multiply it by
another invertible Kronecker product (up to transpose convention).  The rank
is unchanged.  Thus the rank contradiction rules out the full advertised
external-leg orbit, not only a common basis change.

On already contracted shared edges, the usual contraction-compatible
inverse/dual gauges cancel.  Their only surviving effect is through exposed
leg gauges, already covered above.  Noncompatible internal transformations,
a changed edge bilinear form, or a projection would define a different
mechanism and are not silently ruled out.

The conclusion is restricted to characteristic zero even though the tensor
identity and rank formula hold over every field.  It covers only horizontal
fusion of the displayed scalar-Boolean cells, with shared \(y\) and carry
legs contracted and all \(x\), accumulator, and sum legs exposed in the
specified inherited port order.  The artifact explicitly leaves open
two-dimensional fusion, other rotations or regroupings, packed or auxiliary
states, noninvertible projections, asymmetric cells, genuinely global
Pfaffian identities, separately justified finite-characteristic methods, and
non-matchgate contraction algorithms.  It claims neither a general
contraction lower bound nor a factoring algorithm.

No new inconsistency is caused by the amendment.  The complete amended
artifact therefore merits **PASS AS WRITTEN**.
