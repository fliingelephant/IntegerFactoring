# Hostile audit of F38 — horizontal fused matchgate strips

**Audited artifact:**
`experiments/F38_horizontal_matchgate_strip_kill/RESULT.md`.

**Verdict:** **PASS WITH AMENDMENTS.**

The exact fused relation, multiplicity-one statement, planar contiguous cut,
rank formula, and characteristic-zero matchgate-orbit obstruction are correct.
I found no counterexample at (L=1), at either strip endpoint, in positive
characteristic for the rank computation, or in the topology of the two
parallel inter-cell corridors.  One sentence in the self-contained recap of
the pure-spinor lemma names the wrong summands as local row/column operations.
That sentence is false literally and must be corrected as specified below.
It does not alter the imported promoted lemma or the candidate's conclusion.

No computation was used.

## 1. Exact mandatory amendment

In Section 5, after

\[
\omega=\omega_I+\omega_O+\omega_{IO},
\]

the candidate says that "the first and last terms act by invertible row and
column maps."  This is wrong: the cross term \(\omega_{IO}\) is precisely the
term whose rank determines the Schmidt/flattening rank and is not a one-side
row or column operation.

Replace that clause by:

> The two local terms \(\omega_I\) and \(\omega_O\) act by invertible row and
> column maps, respectively.  The cross term \(\omega_{IO}\) controls the
> remaining rank.

Equivalently, "the first two terms" is correct for the ordering displayed in
the formula.  The paragraphs immediately following already analyze
\(\omega_{IO}\) as the cross form, so this is a localized incorrect sentence,
not a change to the proof's mechanism.

No other mathematical amendment is required.  Two optional precision edits
are recorded in Section 7, but the existing text already contains the needed
claims.

## 2. Fused tensor and multiplicity one

The leg count and contraction pattern are consistent.  There are (8L) leg
incidences before fusion.  The (L-1) shared (y)-edges and (L-1) shared
carry edges each consume two incidences, leaving

\[
8L-4(L-1)=4L+4
\]

external legs, exactly (2L+2) in each of (I_L) and (O_L).  No
(x_i^-\!\)--\(x_i^+\), (a_i\!\)--\(s_i\), or endpoint contraction is
implicit in (2.1).

For a nonzero summand, the propagation indicators force

\[
x_i^-=x_i^+,
\qquad
y_0=y_1=\cdots=y_L.
\]

The local arithmetic constraints are

\[
a_i+c_i+x_i y=s_i+2c_{i+1}.
\]

Multiplication by (2^i) and summation is exact integer arithmetic.  For
each (1\leq k<L), the term (2^k c_k) on the left at (i=k) cancels the
term (2^k c_k) on the right at (i=k-1).  The uncancelled endpoints are
(c_0) and (2^L c_L), giving

\[
A+yX+c_0=S+2^L c_L.
\]

The converse is also valid.  Given (c_0), the full-adder recurrence
uniquely determines a Boolean pair

\[
(\widehat s_i,\widehat c_{i+1})

\]

from (a_i+x_i y+\widehat c_i\in\{0,1,2,3\}).  It produces the integer
binary expansion

\[
A+yX+c_0
=\sum_{i=0}^{L-1}2^i\widehat s_i+2^L\widehat c_L.
\]

The left side lies in (0,\ldots,2^{L+1}-1).  The given external
((s_0,\ldots,s_{L-1},c_L)) is another ((L+1))-bit expansion of the same
integer, so uniqueness of binary expansion makes it identical to the
recursively produced word.  Thus there is exactly one internal carry word.
The internal (y)-word is likewise forced; for (L=1), both internal index
sets are empty and have exactly one empty assignment.  Consequently every
tensor entry is genuinely (0) or (1), rather than a positive assignment
count that could vanish modulo a field characteristic.

This proves the displayed closed form as a (0/1)-valued tensor over every
field, provided—as is standard in the candidate's indicator notation—the
integer Boolean relation is evaluated before its truth value is embedded in
the coefficient field.  It is not the polynomial equation
(a+c+xy=s+2d) interpreted inside a characteristic-two field.

## 3. Hostile topology check

The suspected "top plus left" error does not occur.  It is useful to make a
single compatible rotation system completely explicit.

Reflect the verified F36 drawing vertically if necessary.  On every cell
disk place (x_i^-,a_i) on the top, (y_i,c_i) on the left,
(y_{i+1},c_{i+1}) on the right, and (x_i^+,s_i) on the bottom.  Put the
(y)-lane physically above the carry lane in every horizontal corridor.
One possible clockwise boundary order, starting on the top, is

\[
x_i^-,a_i,
y_{i+1},c_{i+1},
x_i^+,s_i,
c_i,y_i.
\tag{3.1}
\]

Thus the four incoming ports

\[
c_i,y_i,x_i^-,a_i
\]

form one cyclic interval across the chosen starting point, and the four
outgoing ports

\[
y_{i+1},c_{i+1},x_i^+,s_i
\]

form its complement.  This differs from the set order used to index the
flattening only by row and column permutations.

At an interface, the (y)-port is above the carry port on both facing disk
sides.  Connecting like labels therefore gives two noncrossing parallel
curves.  The short disk-boundary interval between those two ports contains no
other port at either endpoint.  Hence the two curves bound a lens face, but
no (x), accumulator, or sum leg is trapped in that face.  Repeating this in
disjoint corridors gives a planar chain for every (L).

A regular neighbourhood of the chain has, in clockwise order, four boundary
port groups:

1. top ports, all in (I_L);
2. the right endpoint ports, all in (O_L);
3. bottom ports, all in (O_L); and
4. the left endpoint ports, all in (I_L).

Groups 4 and 1 meet across the cyclic starting point, so their union is one
cyclic interval.  Groups 2 and 3 meet at the opposite corner and form the
complementary interval.  Therefore (I_L) and (O_L) really are
complementary contiguous arcs.  They are not two disconnected linear
intervals mistakenly called contiguous: cyclic contiguity is the relevant
notion, and the wraparound joins the left and top portions.

For (L=1), (3.1) is exactly a valid F36 input/output rotation.  There is no
parallel inter-cell lens, and the same two cyclic intervals remain.  At the
two endpoints for (L>1), the unpaired (y,c) stubs go directly into the
outer face.  The argument also permits any permutation within either arc,
which changes only the indexing of rows or columns.

Thus the topology claim is sound.  It relies on the inherited F36 sector
placement and on keeping the two horizontal ports consecutive; it would not
follow from the abstract incidence graph alone.  The candidate supplies
those ingredients, and (3.1) is an explicit audit certificate for them.

## 4. Direct-sum decomposition and rank

Across (I_L\mid O_L), the propagation equalities force identical labels

\[
(x_0,\ldots,x_{L-1},y)
\]

on the two sides.  Distinct labels occupy disjoint row sets and disjoint
column sets, so the matrix is a direct sum of exactly (2^{L+1}) blocks.
This remains a direct sum even when different labels have the same numerical
quantity (Q=yX).

Fix a label and (Q=yX).  Encoding the row by ((A,c_0)) and the output
column by

\[
W=S+2^L c_L,
\]

the block has one (1) in every row, at

\[
W=Q+A+c_0.
\]

The quantity (A+c_0) takes every value (0,\ldots,2^L).  The endpoints
have one preimage, and each interior value has exactly the two preimages

\[
(A,c_0)=(t,0),\ (t-1,1),
\qquad 1\leq t\leq2^L-1.
\]

Hence the used columns are exactly

\[
Q,Q+1,\ldots,Q+2^L.
\]

They are legal because (0\leq Q\leq2^L-1), so the greatest possible
column is (2^{L+1}-1).  The distinct nonzero row vectors are distinct
standard basis vectors.  They are independent over every field, including
characteristic two, and therefore

\[
\operatorname{rank} B_Q=2^L+1.
\]

Adding ranks of the disjoint blocks gives

\[
\operatorname{rank}M_L=2^{L+1}(2^L+1).
\]

For the endpoint case (L=1), there are four ((x,y))-blocks, each of rank
three, so the formula gives (12) and agrees with P46.  No part of this
calculation uses division, cancellation of multiple tensor assignments, or a
field interpretation of the integer labels.

## 5. Pure-spinor lemma and gauge inference

The conclusion uses the promoted P46 lemma only over a
characteristic-zero field and only for a complementary contiguous cyclic
cut.  F38 satisfies both hypotheses: the tensor is nonzero on the all-zero
assignment, and Section 3 verifies the cut.

The all-chart proof mechanism remains valid after the mandatory wording fix:

* a product of particle-hole Clifford toggles is a signed coefficient-basis
  permutation and, in Jordan--Wigner form, a tensor product of one-leg Pauli
  maps, so it both preserves purity and preserves the selected flattening
  rank;
* a nonzero coefficient can therefore be moved to the vacuum coefficient,
  including for odd and degenerate charts;
* in the vacuum chart,
  \(\lambda\exp(\omega_I+\omega_O+\omega_{IO})\) has its two local
  exponentials absorbed into invertible operations on the two flattening
  spaces; and
* if the cross matrix has rank (r), separate changes of one-particle basis
  reduce it to (r) paired modes, whose subset expansion has rank (2^r).

Contiguity is used to linearize the cyclic order without an interleaving
shuffle.  The remaining Koszul effects are separable row/column signs, as in
P46.  Nothing in F38 invokes the known-false arbitrary-bipartition version.

For every (L\geq1), (2^L+1) is an odd integer greater than one.  Thus

\[
2^{L+1}(2^L+1)
\]

is not a power of two.  Independent invertible maps on exposed legs act on
the flattening by invertible Kronecker products on the left and right, so
they preserve its rank.  If any such transformed tensor were a
characteristic-zero matchgate signature, the contiguous-cut lemma would
force a power-of-two rank, a contradiction.

The statement about shared-edge gauges is also correctly scoped.  On an
already fused tensor, gauges on exposed legs are a constrained subset of the
arbitrary independent gauges just ruled out.  Compatible inverse/dual gauges
inserted on a contracted internal edge cancel in the contraction and do not
create a new fused tensor.  Noncompatible internal transformations, a changed
contraction bilinear form, or a projection are different mechanisms and are
not covered.

The rank formula is characteristic-independent, but the matchgate
consequence is asserted only in characteristic zero.  This is the precise
safe scope of the imported lemma.

## 6. Scope and overclaim audit

The final exclusions are honest.  The theorem closes only a one-row strip of
the displayed scalar-Boolean cell, contracting the shared (y) and carry
legs and exposing every (x), accumulator, and sum leg.  It does not rule
out:

* two-dimensional fusion, which changes both the boundary tensor and its
  available cuts;
* another rotation or a noncontiguous grouping;
* packed domains, auxiliary states, noninvertible projections, or asymmetric
  cells;
* a global Pfaffian identity which does not require this strip to be a
  matchgate;
* a separately proved modular construction; or
* a non-matchgate contraction algorithm.

The proof is an obstruction to one auxiliary holographic mechanism, not a
contraction lower bound and not a factoring algorithm.  It also does not
show that attaching endpoint unaries or projecting some exposed legs
preserves the obstruction; those operations are already outside the exact
construction.  I found no sentence that claims otherwise.

## 7. Optional clarity amendments

These are not needed to make the theorem true, but they would make the final
version harder to misread.

1. After (2.1), state explicitly that every bracket in the Boolean cell is
   the truth value of an integer relation embedded as (0) or (1) in
   (K).  This prevents a reader from incorrectly reducing the equation
   (a+c+xy=s+2d) inside (K) in characteristic two.
2. In Section 3, include an explicit clockwise order such as (3.1), or at
   least say that the physical top-to-bottom order is (y) then carry on
   both sides of every corridor.  The current assertions that the endpoint
   orders agree and that no external leg lies in a lens are sufficient, but
   the explicit order makes the cyclic-wrap argument immediate.

Subject to the one mandatory correction in Section 1, F38's exact negative
theorem survives the hostile audit.
