# F36 — the minimal propagated multiplier cell has a rank-12 matchgate obstruction

**Family:** F20.

**Status:** promoted as P46 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Classification:** evidence against the exact auxiliary mechanism consisting
of the natural scalar-Boolean propagated schoolbook cell, transformed one cell
at a time into planar matchgate signatures.  It is not a tensor-contraction
lower bound and does not close larger fused blocks, block encodings, global
Pfaffian formulas, or non-matchgate contraction.

**Computation:** none.  The cell rank and every other claim below are proved
symbolically.

## 1. Outcome

The smallest nearest-neighbor Boolean cell that simultaneously

1. propagates both factor bits to their next occurrences,
2. forms their partial product internally, and
3. performs one exact sum/carry update

is the eight-leg signature

\[
\begin{aligned}
 C(x_L,x_R,y_U,y_D,a,c,s,d)
  ={}&\mathbf 1[x_L=x_R]\,\mathbf 1[y_U=y_D]\\
    &\cdot\mathbf 1[a+c+x_Ly_U=s+2d].
\end{aligned}
\tag{1.1}
\]

It tiles an explicit planar shifted-add multiplier with one satisfying
internal assignment per ordered factor witness, and prefix pins are boundary
unaries.  Thus this genuinely avoids P36's separated
\(\operatorname{COPY}_3\)--\(\operatorname{AND}_3\) hypothesis.

Nevertheless, split the legs as

\[
 I=(x_L,y_U,a,c),
 \qquad
 O=(x_R,y_D,s,d).
\tag{1.2}
\]

Embed the cell with the four incoming legs \(I\) on one boundary arc and the
four outgoing legs \(O\) on the complementary arc, as in Section 4.2.  The
\(I\mid O\) coefficient flattening of \(C\) has rank \(12\).  Every nonzero
matchgate signature, including every degenerate pure-spinor chart, has
power-of-two rank across a contiguous split of its cyclically ordered
external legs.  Independent invertible \(2\times2\) transformations on the
eight legs preserve flattening rank.
Consequently

\[
 (T_1\otimes\cdots\otimes T_8)C
 \quad\text{is not a matchgate for every }T_i\in\operatorname{GL}_2.
\tag{1.3}
\]

This grants strictly more local freedom than a contraction-compatible global
edge-gauge assignment.  Hence the natural fused cell does not land in the
planar Pfaffian/matchgate family even before shared-edge gauge compatibility,
boundary pins, or coefficient growth become relevant.

## 2. Closest prior results and material difference

### 2.1 P36/X30

P36 closes an explicit *separated* realization.  A ternary fanout COPY is
directly adjacent to a ternary AND, the COPY is first made parity-pure, and
the required transpose-dual action then makes the AND parity equations
inconsistent.  That theorem permits common bases for the two factor roles,
but explicitly leaves fused cells and edge-dependent gauges open.

Cell (1.1) has no external partial-product wire, no standalone AND, and no
branching COPY.  A factor bit travels through a chain of binary occurrences,
and its equality, partial product, addition, and carry are all inside one
indivisible signature.  The present obstruction also permits a different
\(\operatorname{GL}_2\) action on every one of the eight legs.  Its invariant
is bipartite matrix rank, not ternary parity.  Thus it is not an instance of
P36's hypothesis.

### 2.2 P38 and P42

P38 concerns positive perfect-matching *boundary-deletion* signatures.  Its
direct six-bit fused relation

\[
 a+c+xy=s+2d
\]

does not propagate repeated occurrences of \(x,y\), and its obstruction is
fixed parity/matching exchange (or a one-hot subcube theorem), not a signed
Pfaffian orbit invariant.

P42 shows that closed internal-edge occupancies can realize AND and COPY with
multiplicity one, while a universal clean four-port occupancy equality wire
is impossible.  Cell (1.1) neither assumes such a connector nor decodes
closed matching occupancies.  It is an ordinary Boolean tensor tested under
arbitrary invertible holographic gauges.  P42 therefore neither proves nor
implies the rank-12 theorem below.

## 3. Why eight legs are the minimal natural fused interface

The word "minimal" here is deliberately scoped to scalar Boolean,
nearest-neighbor schoolbook tiles.

The partial product needs two independently variable factor bits.  If one
cell is not the final occurrence of either bit, exact chain propagation needs
an incoming and outgoing occurrence for each, hence four factor legs

\[
 x_L,x_R,y_U,y_D.
\]

A one-column shifted-add update needs an incoming and outgoing accumulator
bit and an incoming and outgoing ripple-carry bit, hence four more legs

\[
 a,s,c,d.
\]

None of these pairs can be identified: there are valid local rows with
\(a\ne s\) and with \(c\ne d\), while both state bits vary independently of
either factor bit in valid surrounding computations.  Relation (1.1) attains
the resulting eight-leg lower bound within this declared interface.

This is not a lower bound for asymmetric tile sets, several bits packed into
one edge, auxiliary/projected boundary states, higher-radix arithmetic, or a
larger block treated as one signature.

## 4. Exact planar tiling and prefix semantics

Let

\[
 x=\sum_{i=0}^{n-1}x_i2^i,
 \qquad
 y=\sum_{j=0}^{n-1}y_j2^j.
\]

Use one copy \(C_{j,i}\) of (1.1) for every
\(0\le j,i<n\).  Row \(j\) ripple-adds the shifted row
\(y_jx2^j\) into the accumulator.  In cell \((j,i)\), write the four
arithmetic legs as \(a_{j,i},c_{j,i},s_{j,i},d_{j,i}\), so

\[
 a_{j,i}+c_{j,i}+x_i y_j
   =s_{j,i}+2d_{j,i}.
\tag{4.1}
\]

Make the following contractions.

* Propagate \(x_i\) from \(C_{j,i}\) to \(C_{j+1,i}\).
* Propagate \(y_j\) from \(C_{j,i}\) to \(C_{j,i+1}\).
* For \(i<n-1\), connect \(d_{j,i}\) to \(c_{j,i+1}\).
* For \(j<n-1\) and \(i\ge1\), connect \(s_{j,i}\) to
  \(a_{j+1,i-1}\).
* For \(j<n-1\), connect the last carry \(d_{j,n-1}\) to
  \(a_{j+1,n-1}\).

Pin

\[
 a_{0,i}=0,
 \qquad
 c_{j,0}=0.
\tag{4.2}
\]

The finalized product outputs are

\[
 s_{j,0}\quad(0\le j<n-1),
 \qquad
 s_{n-1,i}\quad(0\le i<n),
 \qquad
 d_{n-1,n-1}.
\tag{4.3}
\]

They have binary weights \(0,\ldots,2n-1\), respectively, and are pinned
to the corresponding bits of \(N\) (the high bits are zero).  The initial
\(x_i,y_j\) legs receive free unaries, except that any requested prefix of
the fixed-length \(x\)-encoding replaces the appropriate free unaries by
\(0\)- or \(1\)-pins.  Determined factor-line outputs receive neutral
unaries.

### 4.1 Arithmetic proof

Before row \(j\), let

\[
 A^j=x\sum_{r<j}y_r2^r.
\tag{4.4}
\]

Its still-active bit of weight \(j+i\) is \(a_{j,i}\).  Equation (4.1),
the zero incoming carry, and the horizontal carry contractions are exactly
a ripple addition of \(y_jx2^j\).  The \(i=0\) sum becomes the finalized bit
of weight \(j\); the other sums shift to the next row's active inputs; and
the last carry becomes its highest active input.  Therefore

\[
 A^{j+1}=A^j+y_jx2^j
          =x\sum_{r\le j}y_r2^r.
\tag{4.5}
\]

Induction from \(A^0=0\) gives \(A^n=xy\), so the pins (4.3) impose exactly
\(xy=N\).

For fixed \(x,y\), every factor propagation value is forced.  Starting from
\(c_{j,0}=0\), each equation (4.1) uniquely gives

\[
 s_{j,i}\equiv a_{j,i}+c_{j,i}+x_i y_j\pmod 2,
 \qquad
 d_{j,i}=\left\lfloor
 \frac{a_{j,i}+c_{j,i}+x_i y_j}{2}
 \right\rfloor.
\tag{4.6}
\]

Thus every admitted ordered factor pair has exactly one internal extension,
and every nonzero summand is such a pair.  As \(N>0\), zero factors are not
admitted; every positive divisor is below \(2^n\).  Prefix pinning therefore
gives exactly the counts used in P36's factor self-reduction, with
multiplicity one.

### 4.2 Planarity

Place \(C_{j,i}\) at the lattice point

\[
 (u,v)=(i+j,j).
\]

The \(y\)- and ordinary carry-contractions are parallel horizontal edges;
the sum-to-next-accumulator contractions are vertical edges; and the
\(x\)-propagation contractions are the same-oriented diagonals of the
resulting triangular lattice.  The last-carry contractions run as parallel
boundary diagonals.  Parallel edges can be separated in a thin strip, and
only one diagonal orientation is used, so no edges cross.  All free legs,
constants, target bits, and prefix pins lie on the outer boundary.  The graph
has \(n^2\) constant-arity cells and \(O(n)\) unaries.

At each cell, the incoming \(a,x_L,y_U,c\) edges approach through the
north/northwest/west arc, while the outgoing \(s,x_R,y_D,d\) edges leave
through the south/southeast/east arc.  Thus the split (1.2), up to row and
column permutations internal to its two sides, is a contiguous split in the
cyclic boundary order required of a planar matchgate signature.

This establishes original-network planarity.  It does not by itself make the
cell a matchgate or establish a Pfaffian evaluation.

## 5. A rank theorem for every matchgate chart

We work over a characteristic-zero field (in particular over
\(\mathbb Q\), \(\mathbb R\), \(\mathbb C\), or an algebraic extension).
The usual boundary-order signs multiply rows and columns of a flattening by
nonzero signs and never affect its rank.

### Lemma 5.1 (power-of-two rank for a contiguous boundary split)

Let \(F\ne0\) be an \(m\)-leg matchgate signature whose external legs have
their planar cyclic order.  If \(I\) and \(O\) are the two contiguous arcs
of that order, then the coefficient flattening
\(\operatorname{Flat}_{I\mid O}(F)\) has rank \(2^r\) for some integer
\(r\ge0\).

#### Proof

Start the cyclic order at the cut between the two arcs, so every \(I\)-mode
precedes every \(O\)-mode.  Identify the matchgate signature, with the
conventional boundary signs in this order, with a pure spinor in the exterior
algebra \(\Lambda V\).  We first remove a possible degenerate chart.
Choose a nonzero coefficient \(F_S\).  For every \(i\in S\), apply the
particle-hole Clifford operator

\[
 \gamma_i=e_i\wedge+\iota_{e_i}.
\]

On the occupation basis, \(\gamma_i\) toggles bit \(i\) and contributes only
the sign \((-1)^{\#\{j<i:j\text{ is occupied}\}}\).  Its matrix is therefore
a tensor product of a Pauli \(X\) on leg \(i\), Pauli \(Z\)'s on earlier
legs, and identities elsewhere.  It is invertible, preserves pure spinors,
and preserves every bipartite flattening rank.  The product over \(i\in S\)
moves \(F_S\), up to sign, to the vacuum coefficient.  The resulting pure
spinor \(G\) has \(G_\varnothing\ne0\).

The nonzero-vacuum chart of the matchgate identities is the Pfaffian chart:
for a skew matrix \(A\),

\[
 G=G_\varnothing\exp(\omega),
 \qquad
 \omega=\sum_{i<j}A_{ij}e_i\wedge e_j,
\tag{5.1}
\]

equivalently \(G_T/G_\varnothing=\operatorname{Pf}(A_T)\) for even \(T\)
and the odd coefficients vanish.  Explicitly, set
\(A_{ij}=G_{\{i,j\}}/G_\varnothing\); the matchgate identity with the vacuum
and an even set \(T\), expanded at the least element of \(T\), is exactly the
Pfaffian cofactor recurrence, so induction on \(|T|\) gives (5.1).

Now write \(V=V_I\oplus V_O\) and decompose

\[
 \omega=\omega_I+\omega_O+\omega_{IO},
 \qquad
 \omega_{IO}=\sum_{i\in I,j\in O}B_{ij}e_i\wedge e_j.
\tag{5.2}
\]

Multiplication by \(\exp(\omega_I)\) on \(\Lambda V_I\) and by
\(\exp(\omega_O)\) on \(\Lambda V_O\) are invertible, with inverses obtained
by negating the two-forms.  They are invertible row and column operations on
the flattening.  Hence only \(\exp(\omega_{IO})\) affects its rank.

Let \(r=\operatorname{rank}B\).  Invertible one-particle changes of basis
inside \(V_I\) and \(V_O\), whose exterior powers are again invertible row
and column operations, put the cross-form into

\[
 \omega_{IO}=\sum_{k=1}^{r}\lambda_k u_k\wedge v_k,
 \qquad \lambda_k\ne0.
\tag{5.3}
\]

Therefore

\[
 \exp(\omega_{IO})
   =\prod_{k=1}^{r}(1+\lambda_k u_k\wedge v_k).
\tag{5.4}
\]

Each factor in (5.4) has a \(2\times2\) coefficient flattening of rank two;
unused modes contribute rank-one vacuum factors.  The total flattening is a
Kronecker product and has rank \(2^r\).  Undoing every invertible operation
proves the claim for the original, possibly degenerate, even or odd
signature.  \(\square\)

Contiguity is essential and is not being smuggled into a stronger theorem.
For example, the four-mode pure spinor

\[
 \exp(e_1\wedge e_2+e_3\wedge e_4
      +e_1\wedge e_4+e_2\wedge e_3)
\]

has vacuum coefficient \(1\), the four displayed two-body coefficients
equal to \(1\), and coefficient \(2\) on \(e_1\wedge e_2\wedge e_3\wedge
e_4\).  Its ordinary \(\{1,3\}\mid\{2,4\}\) flattening has three independent
rows, hence rank \(3\).  That is a noncontiguous split in the cyclic order.
The F36 obstruction uses the genuinely contiguous input/output arcs proved
in Section 4.2, so it does not rely on the false arbitrary-bipartition
generalization.

## 6. The fused cell has rank 12

Flatten (1.1) according to (1.2).  The two propagation equalities make the
matrix block diagonal in \((x,y)\in\{0,1\}^2\).  Within a fixed block, rows
are indexed by \((a,c)\), columns by \((s,d)\), and

\[
 H_q[(a,c),(s,d)]
   =\mathbf1[a+c+q=s+2d],
 \qquad q=xy.
\tag{6.1}
\]

For \(q=0\), the four input rows map to output columns

\[
 00\mapsto00,
 \quad 01\mapsto10,
 \quad 10\mapsto10,
 \quad 11\mapsto01.
\tag{6.2}
\]

They span exactly the three distinct standard basis rows belonging to
columns \(00,10,01\).  Thus \(\operatorname{rank}H_0=3\).  For \(q=1\),

\[
 00\mapsto10,
 \quad 01\mapsto01,
 \quad 10\mapsto01,
 \quad 11\mapsto11,
\tag{6.3}
\]

so \(\operatorname{rank}H_1=3\) as well.  The four \((x,y)\) blocks occupy
disjoint row and column sets.  Consequently

\[
 \operatorname{rank}\operatorname{Flat}_{I\mid O}(C)
 =3+3+3+3=12.
\tag{6.4}
\]

For arbitrary independent leg transformations, this flattening becomes

\[
 \left(T_{x_L}\otimes T_{y_U}\otimes T_a\otimes T_c\right)
 \operatorname{Flat}_{I\mid O}(C)
 \left(T_{x_R}\otimes T_{y_D}\otimes T_s\otimes T_d\right)^{\mathsf T},
\tag{6.5}
\]

up to the harmless convention for covariant legs.  Both multipliers are
invertible, so the rank remains \(12\).  Since \(12\) is not a power of two,
Lemma 5.1 proves (1.3).

## 7. Independent logical gates in the landing test

The negative conclusion occurs at exactly the first item below.  The other
items must not be conflated with it.

1. **Local signature orbit membership — failed.**  Even eight completely
   independent \(\operatorname{GL}_2\) leg actions cannot put one copy of
   \(C\), with the stated contiguous input/output boundary order, in the
   matchgate/pure-spinor variety.

2. **Compatibility of gauges on shared edges — not reached.**  For an edge
   joining cells \(u,v\), ordinary contraction would require
   \(T_{v,e}=(T_{u,e}^{-1})^{\mathsf T}\).  The local theorem grants arbitrary
   actions before imposing this equation, so global compatibility cannot
   repair the failed local orbit test.  It is not a proof that some different
   locally surviving tile set lacks compatible gauges.

3. **Planarity/topology — satisfied by the original tiling only.**  Section
   4.2 gives a planar incidence graph.  A larger block fusion or another
   wiring must establish its own planar embedding; local matchgate membership
   alone would not do so.

4. **Prefix pins — exact in the Boolean network, not tested after a
   hypothetical transform.**  Every prefix changes only boundary unaries and
   preserves planarity and multiplicity.  A surviving holographic proposal
   would still need one compatible treatment of free, zero-pin, and one-pin
   boundary signatures for every prefix.  The unpinned network already
   contains the rank-12 cell, so pinning cannot rescue this cell-by-cell
   proposal.

5. **Exact witness multiplicity — one.**  Section 4.1 proves a bijection
   between nonzero tensor summands and ordered factor witnesses.  No
   assignment-dependent multiplicity is hidden in the tiling.

6. **Bit growth — benign before transformation, not reached after it.**  The
   original network has \(n^2\) fixed \(0/1\) signatures, an
   \(O(n^2\log n)\)-bit explicit wiring description, and contraction at most
   \(2^n\), hence an \(O(n)\)-bit exact answer.  The orbit obstruction holds
   even over \(\mathbb C\), without a coefficient-height restriction.  If a
   different Pfaffian construction survives algebraically, it must separately
   provide a uniform exact field representation and polynomial intermediate
   bit lengths.

7. **Global factoring conclusion — absent.**  A local matchgate construction
   would only be one ingredient.  It would still need compatible gauges,
   planar composition, all prefix pins, a uniform Pfaffian evaluator, exact
   integer recovery, and polynomial bit complexity before P36's verified
   count-to-factor reduction could be invoked.

## 8. Exact verdict and reopen condition

> **Candidate theorem.**  The eight-leg propagated shifted-add cell (1.1)
> tiles a planar, prefix-pinnable Boolean network whose satisfying assignments
> are in multiplicity-one correspondence with ordered pairs \((x,y)\) such
> that \(xy=N\).  Yet its \((x_L,y_U,a,c)\mid(x_R,y_D,s,d)\) flattening has
> rank \(12\), whereas every nonzero matchgate signature has power-of-two
> flattening rank across every contiguous cyclic bipartition.  Therefore no
> independent invertible basis or gauge action on its external Boolean legs
> makes it a
> matchgate.  In particular, no contraction-compatible assignment of such
> gauges makes this exact cell-by-cell planar multiplier an FKT network.

This closes only the natural minimal scalar tile.  A retry is materially new
if it supplies at least one of the following:

1. a larger fused block whose every flattening passes the power-of-two test
   and which is explicitly proved to satisfy all matchgate identities;
2. a block or higher-domain edge encoding, projected auxiliary boundary
   states, or an asymmetric tile set not equivalent to (1.1) under invertible
   local changes;
3. a different planar rotation/order of the same logical legs whose global
   wiring remains planar and whose full matchgate identities are proved;
4. a global Pfaffian/sub-Pfaffian identity which does not require each copy of
   (1.1) to be a matchgate, with signs and prefix pins proved;
5. a modular or other field construction outside the characteristic-zero
   pure-spinor argument, together with exact integer reconstruction and
   polynomial bit growth; or
6. a non-matchgate polynomial contraction of the complete pinned witness
   network.

Merely changing common role bases to edge-dependent gauges, or observing
that the original incidence graph is planar, is covered by the rank-12
obstruction and does not reopen the route.
