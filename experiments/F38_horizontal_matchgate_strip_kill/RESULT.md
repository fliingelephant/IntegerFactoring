# F38 — every horizontal fused strip retains a non-power-of-two matchgate obstruction

**Family:** F20.

**Status:** promoted as P48 after the first hostile audit required one
mathematical wording correction, the amended whole artifact passed a fresh
hostile re-audit, and a context-free proof-blind reconstruction succeeded.

**Classification:** evidence against the exact auxiliary mechanism which
horizontally fuses finitely many copies of the natural F36 propagated
schoolbook cell, leaves the vertical Boolean interfaces scalar, and tries to
put the resulting strip in a planar matchgate orbit by independent invertible
changes of basis on its exposed legs.

**Computation:** none.  All tensor entries and ranks below are derived
symbolically.

## 1. Exact outcome

For \(L\geq1\), horizontally fuse \(L\) consecutive copies of the F36 cell

\[
 C(x^-,x^+,y^-,y^+,a,c,s,d)
 =\mathbf 1[x^-=x^+]\mathbf 1[y^-=y^+]
  \mathbf 1[a+c+x^-y^-=s+2d].
\tag{1.1}
\]

Only the common \(y\)-propagation legs and the ripple-carry legs between
adjacent cells are contracted.  Both \(x\)-propagation legs and both
accumulator/sum legs of every cell remain external.  The initial and final
\(y\) and carry legs also remain external.

The resulting tensor has a planar embedding in which

\[
 I_L=\{x^-_0,\ldots,x^-_{L-1},y_0,
       a_0,\ldots,a_{L-1},c_0\}
\tag{1.2}
\]

is one contiguous boundary arc and

\[
 O_L=\{x^+_0,\ldots,x^+_{L-1},y_L,
       s_0,\ldots,s_{L-1},c_L\}
\tag{1.3}
\]

is the complementary arc.  Across this split its flattening rank is exactly

\[
 \boxed{\quad 2^{L+1}(2^L+1).\quad}
\tag{1.4}
\]

The odd factor \(2^L+1>1\) makes (1.4) a non-power of two for every
\(L\geq1\).  The promoted all-chart lemma from F36 says that a nonzero
characteristic-zero matchgate/pure-spinor signature has power-of-two rank
across a contiguous cyclic cut.  Independent invertible transformations on
the external Boolean legs preserve this rank.  Hence no such transformations
put any finite strip in the matchgate orbit with the inherited planar port
order.

For \(L=1\), formula (1.4) is \(4\cdot3=12\), exactly recovering F36.  The
argument is uniform in \(L\); it does not merely check a fixed collection of
strip lengths.

## 2. Exact fused tensor

Use local column indices \(i=0,\ldots,L-1\).  The strip may begin at any
global schoolbook column; dividing all arithmetic weights by the weight of
that first column gives the local indexing below.

For cell \(i\), denote its two factor-propagation legs by
\(x_i^-,x_i^+\), its accumulator and sum legs by \(a_i,s_i\), and its two
\(y\)-legs by \(y_i,y_{i+1}\).  Denote the carry entering cell \(i\) by
\(c_i\) and the carry leaving it by \(c_{i+1}\).  Thus
\(y_1,\ldots,y_{L-1}\) and \(c_1,\ldots,c_{L-1}\) are contracted indices,
while all other displayed
indices are external.

Over any field \(K\), define the fused Boolean tensor by the ordinary tensor
contraction

\[
 \begin{aligned}
 \mathcal S_L={}&
 \sum_{y_1,\ldots,y_{L-1}\in\{0,1\}}
 \sum_{c_1,\ldots,c_{L-1}\in\{0,1\}}
 \prod_{i=0}^{L-1}
 C(x_i^-,x_i^+,y_i,y_{i+1},a_i,c_i,s_i,c_{i+1}).
 \end{aligned}
\tag{2.1}
\]

The sums are empty when \(L=1\).  This definition specifies exactly which
legs are fused; in particular, no \(x_i^-\)--\(x_i^+\),
\(a_i\)--\(s_i\), or external endpoint contraction is being hidden.
Every bracket in (1.1) is first evaluated as the truth value of the displayed
integer Boolean relation and then embedded as \(0\) or \(1\) in \(K\); the
integer equation is not reduced inside a field of positive characteristic.

Set

\[
 X=\sum_{i=0}^{L-1}2^i x_i^-,\qquad
 A=\sum_{i=0}^{L-1}2^i a_i,\qquad
 S=\sum_{i=0}^{L-1}2^i s_i.
\tag{2.2}
\]

Then the complete closed form of (2.1) is

\[
 \begin{aligned}
 \mathcal S_L={}&
 \left(\prod_{i=0}^{L-1}\mathbf1[x_i^-=x_i^+]\right)
 \mathbf1[y_0=y_L]\\
 &\quad\cdot
 \mathbf1\!\left[A+y_0X+c_0=S+2^Lc_L\right].
 \end{aligned}
\tag{2.3}
\]

In particular every entry is \(0\) or \(1\), not an assignment multiplicity
which might collapse in some field.

### 2.1 Forward implication and carry cancellation

A nonzero summand in (2.1) first forces

\[
 x_i^-=x_i^+=:x_i,
 \qquad
 y_0=y_1=\cdots=y_L=:y.
\tag{2.4}
\]

Its local arithmetic equations are

\[
 a_i+c_i+x_i y=s_i+2c_{i+1}.
\tag{2.5}
\]

Multiply (2.5) by \(2^i\) and sum over \(i\).  The terms
\(2^ic_i\) for \(1\leq i<L\) cancel between the two sides, leaving

\[
 A+yX+c_0=S+2^Lc_L.
\tag{2.6}
\]

Thus every nonzero summand satisfies the three factors in (2.3).

### 2.2 Converse and multiplicity one

Suppose the external assignment satisfies (2.3).  Equality propagation
forces one possible choice \(y_1=\cdots=y_{L-1}=y_0\).  Starting from
\(\widehat c_0=c_0\), recursively define

\[
 \widehat s_i\equiv a_i+x_i y_0+\widehat c_i\pmod2,
 \qquad
 \widehat c_{i+1}=
 \left\lfloor\frac{a_i+x_i y_0+\widehat c_i}{2}\right\rfloor.
\tag{2.7}
\]

Every quantity in the numerator lies in \(\{0,1,2,3\}\), so
\(\widehat s_i,\widehat c_{i+1}\) are Boolean and (2.5) holds.  This is the
only possible internal carry sequence.

The recurrence encodes the integer

\[
 A+y_0X+c_0
 =\sum_{i=0}^{L-1}2^i\widehat s_i+2^L\widehat c_L.
\tag{2.8}
\]

Its range is

\[
 0\leq A+y_0X+c_0
 \leq(2^L-1)+(2^L-1)+1=2^{L+1}-1.
\tag{2.9}
\]

Hence (2.8) is its unique \((L+1)\)-bit binary representation.  Equation
(2.3) says that the given external word
\((s_0,\ldots,s_{L-1},c_L)\) represents the same integer.  Therefore
\(s_i=\widehat s_i\) for every \(i\) and \(c_L=\widehat c_L\).  The one
forced \(y\)-assignment and one
forced carry sequence give exactly one nonzero summand.  This proves (2.3)
as an equality of tensors over every field.

## 3. Planarity and the contiguous cut

Use the verified local rotation system of F36.  Draw the \(L\) cell disks
from left to right.  On each disk put the incoming \(y\) and carry ports on
its left side, with the \(y\)-lane physically above the carry lane, and put
the outgoing \(y\) and carry ports on its right side in the same physical
order.  Put \(x_i^-,a_i\) on the upper arc and \(x_i^+,s_i\) on the lower
arc.  One clockwise order, starting on the top, is

\[
x_i^-,a_i,\ y_{i+1},c_{i+1},\ x_i^+,s_i,\ c_i,y_i.
\tag{3.1}
\]

Thus the incoming ports form one cyclic interval across the chosen starting
point and the outgoing ports its complement, exactly as in the F36
triangular-lattice embedding.

Between neighboring disks, connect the outgoing \(y\)-port to the next
incoming \(y\)-port and the outgoing carry port to the next incoming carry
port using those two parallel horizontal lanes.  Their endpoint orders agree,
so the lanes do not cross.  The short disk-boundary interval between the two
ports contains no other port, so the lens between the parallel curves traps
no external leg.  Different inter-cell corridors are disjoint.  No other
strip leg is contracted.  This is an explicit planar embedding of the
multigraph, including the two parallel edges between each adjacent pair.

Enclose the fused drawing by one outer disk.  Its uncontracted legs occur as
follows:

* all \(x_i^-,a_i\) legs occur along the top boundary;
* \(y_0,c_0\) occur along the left boundary;
* \(y_L,c_L\) occur along the right boundary; and
* all \(x_i^+,s_i\) legs occur along the bottom boundary.

In cyclic order, the top and left portions meet and contain exactly \(I_L\),
while the right and bottom portions meet and contain exactly \(O_L\).  Thus
each is one contiguous boundary arc; neither set alternates with the other.
Permuting ports within either arc only permutes rows or columns of the
selected flattening and does not alter its rank.

The same description covers both endpoint cells and \(L=1\).  No external
leg is trapped in one of the bounded faces between a pair of parallel
internal wires: all upper and lower legs leave away from those horizontal
corridors, and both endpoint pairs leave directly into the outer face.

## 4. Exact flattening rank

Let \(M_L=\operatorname{Flat}_{I_L\mid O_L}(\mathcal S_L)\).  Rows are
indexed by

\[
 (x^-_0,\ldots,x^-_{L-1},y_0,a_0,\ldots,a_{L-1},c_0)
\]

and columns by the analogous outgoing tuple with \(x_i^+,y_L,s_i,c_L\).
The first two factors of (2.3) make \(M_L\) block diagonal in

\[
 (x_0,\ldots,x_{L-1},y)\in\{0,1\}^{L+1}.
\tag{4.1}
\]

There are exactly \(2^{L+1}\) disjoint row-and-column blocks.  Fix one such
label and write

\[
 Q=yX\in\{0,\ldots,2^L-1\}.
\tag{4.2}
\]

The corresponding arithmetic block \(B_Q\) has rows indexed by
\((A,c_0)\) and columns indexed by the output word

\[
 W=S+2^Lc_L\in\{0,\ldots,2^{L+1}-1\}.
\tag{4.3}
\]

By (2.3), each row of \(B_Q\) is the standard basis row supported at

\[
 W=Q+A+c_0.
\tag{4.4}
\]

As \(A\) ranges over \(0,\ldots,2^L-1\) and \(c_0\) over \(0,1\), the sum
\(A+c_0\) ranges over every integer from \(0\) through \(2^L\).  Therefore
the used output columns are exactly

\[
 Q,Q+1,\ldots,Q+2^L.
\tag{4.5}
\]

They are all legal columns because
\(Q+2^L\leq2^{L+1}-1\).  Thus the row space of \(B_Q\) is spanned by exactly
\(2^L+1\) distinct standard basis rows.  Those rows are linearly independent
over every field, so

\[
 \operatorname{rank}_K B_Q=2^L+1.
\tag{4.6}
\]

This count also makes the only row collisions explicit: for
\(1\leq t\leq2^L-1\), the two rows \((A,c_0)=(t,0)\) and
\((A,c_0)=(t-1,1)\) both map to \(W=Q+t\); the two endpoint output words
each have one preimage.
There are no other collisions.

Since the factor/y labels occupy disjoint row and column sets, ranks add
across the direct sum.  Combining (4.1) and (4.6) gives

\[
 \operatorname{rank}_K M_L
 =2^{L+1}(2^L+1).
\tag{4.7}
\]

The rank calculation itself is characteristic-independent.  It uses no
division, cancellation of tensor contributions, or interpretation of an
integer coefficient modulo the field characteristic.

## 5. Matchgate-orbit consequence

For completeness, the exact imported all-chart statement is:

> If \(F\neq0\) is a matchgate/pure-spinor signature over a
> characteristic-zero field and \(I,O\) are complementary contiguous arcs
> of its planar cyclic boundary order, then
> \(\operatorname{rank}\operatorname{Flat}_{I\mid O}(F)=2^r\) for some
> \(r\geq0\).

The statement includes degenerate even and odd charts.  Its short
first-principles proof is to choose any nonzero coefficient and apply
particle-hole Clifford toggles until the vacuum coefficient is nonzero.
Each toggle is a tensor product of one-leg Pauli maps, so it preserves the
selected flattening rank.  In the vacuum chart the pure spinor is
\(\lambda\exp(\omega)\).  Splitting
\(\omega=\omega_I+\omega_O+\omega_{IO}\), the two local terms
\(\omega_I\) and \(\omega_O\) act by invertible row and column maps,
respectively; the cross term \(\omega_{IO}\) controls the remaining rank.
If the cross-form has matrix rank \(r\),
independent one-particle changes of basis reduce it to
\(\sum_{k=1}^r u_k\wedge v_k\).  The coefficient flattening of

\[
 \prod_{k=1}^r(1+u_k\wedge v_k)
\]

has one nonzero diagonal entry for every subset of the \(r\) paired modes
and hence rank \(2^r\).  Contiguity is what lets all \(I\)-modes precede all
\(O\)-modes after a cyclic rotation; the resulting exterior signs are only
invertible row/column sign changes.  This is the fully audited F36 lemma,
not the false version for arbitrary interleaving bipartitions.

Now let an arbitrary \(T_e\in\operatorname{GL}_2(K)\) act independently on
every exposed strip leg.  Across \(I_L\mid O_L\), the flattening changes by

\[
 M_L\longmapsto
 \left(\bigotimes_{e\in I_L}T_e\right)M_L
 \left(\bigotimes_{e\in O_L}T_e\right)^{\mathsf T},
\tag{5.1}
\]

up to the harmless covariant-leg convention.  Both multipliers are
invertible, so (4.7) is invariant.

For \(L\geq1\), \(2^L+1\) is odd and greater than one.  Consequently

\[
 2^{L+1}(2^L+1)
\]

has a nontrivial odd factor and cannot equal \(2^r\).  The tensor is nonzero,
for example on the all-zero assignment.  The contiguous-cut lemma therefore
rules out membership in the matchgate orbit after arbitrary independent
external-leg gauges.  Contraction-compatible gauges inherited from a larger
network are a restriction of these arbitrary gauges, so they cannot rescue
this particular fused strip and port order.

The matchgate inference is stated only in characteristic zero, exactly where
the audited pure-spinor lemma applies.  Although (4.7) remains true in every
characteristic, no unsupported extension of the all-chart lemma to modular
matchgate formalisms is used here.

## 6. Exact scope and verdict

The negative theorem covers every \(L\geq1\) for the following precise
construction:

1. \(L\) consecutive F36 scalar-Boolean cells in one schoolbook row;
2. contraction only of their shared \(y\)-propagation and ripple-carry legs;
3. all individual \(x\)-propagation and accumulator/sum legs exposed;
4. the inherited planar rotation in which those incoming and outgoing legs
   occupy complementary boundary arcs; and
5. arbitrary independent invertible \(2\times2\) transformations on every
   exposed leg over a characteristic-zero field.

It does **not** close any of the following materially different routes:

* a genuinely two-dimensional fused block which also contracts some
  \(x\)-propagation or accumulator/sum legs;
* another planar rotation or a noncontiguous regrouping of the same ports;
* higher-domain or packed edge encodings, auxiliary boundary states,
  noninvertible projections, or asymmetric cells;
* a global Pfaffian/sub-Pfaffian identity which does not make each horizontal
  strip an ordinary matchgate signature;
* a finite-characteristic construction with an independently proved exact
  reconstruction and bit-complexity argument; or
* any non-matchgate polynomial-time contraction algorithm.

It is also not a contraction-complexity lower bound and supplies no factoring
algorithm.  It only shows that ordinary horizontal fusion, at every finite
length, leaves exactly the same type of local matchgate-orbit obstruction as
the single F36 cell.

> **Candidate verdict.**  The horizontally fused length-\(L\) tensor is
> exactly the multiplicity-one relation
>
> \[
> x_i^-=x_i^+\ (0\leq i<L),\qquad y_0=y_L,\qquad
> A+y_0X+c_0=S+2^Lc_L.
> \]
>
> Its natural planar incoming/outgoing split is contiguous and has rank
> \(2^{L+1}(2^L+1)\).  This is never a power of two for \(L\geq1\), so no
> independent invertible Boolean leg gauges transform the strip into a
> characteristic-zero matchgate in that inherited cyclic order.

This verdict is **promoted as P48** after the amended artifact survived a
fresh hostile re-audit and a context-free proof-blind reconstruction.
