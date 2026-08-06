# F36 hostile audit — fused propagated matchgate cell

**Verdict: PASS AS WRITTEN.**

**Audit type:** fresh hostile proof audit.  I tried to refute the candidate at
each of the requested geometry, arithmetic, matchgate, rank, gauge, and scope
interfaces.  I found no mathematical error and no missing premise needed for
the stated scoped theorem.

**Computation:** none.  This audit is proof-only.

**Material checked:** `PROMPT.md`, `AGENTS.md`, the F20 row of `REGISTRY.md`,
P36 and P38 and P42 in `PROVED.md`, X30 in `FAILED.md`, and the complete F36
candidate in `experiments/F36_fused_matchgate_cell_kill/RESULT.md`.

The result is an auxiliary obstruction, not a factoring algorithm.  Passing
this audit supports only the exact negative theorem about the displayed
eight-leg cell in its displayed planar port order.

## 1. Exact shifted-add network

Write

\[
x=\sum_{i=0}^{n-1}x_i2^i,
\qquad
y=\sum_{j=0}^{n-1}y_j2^j.
\]

For fixed factor bits, the equality parts of \(C_{j,i}\) force one constant
\(x_i\) down column \(i\) and one constant \(y_j\) across row \(j\).  There is
no fanout choice and no multiplicity in either propagation chain.

Define

\[
A^j=x\sum_{r<j}y_r2^r.
\]

Because \(x<2^n\) and \(\sum_{r<j}y_r2^r<2^j\), one has
\(0\le A^j<2^{n+j}\).  After the already finalized weights
\(0,\ldots,j-1\) are removed, exactly the \(n\) possible active positions
\(j,\ldots,j+n-1\) remain.  Thus it is consistent to let \(a_{j,i}\) be the
bit of \(A^j\) at weight \(j+i\).

Within row \(j\), \(c_{j,0}=0\) and

\[
a_{j,i}+c_{j,i}+x_i y_j=s_{j,i}+2d_{j,i}
\]

are exactly the usual ripple recurrence.  For each input triple the right
side is uniquely

\[
s_{j,i}\equiv a_{j,i}+c_{j,i}+x_i y_j\pmod 2,
\qquad
d_{j,i}=\left\lfloor
  \frac{a_{j,i}+c_{j,i}+x_i y_j}{2}
\right\rfloor.
\]

The row-transition wiring is exact:

- \(s_{j,0}\) is the finalized bit of weight \(j\);
- \(s_{j,i}\), for \(i\ge1\), has weight \(j+i\) and is connected to
  \(a_{j+1,i-1}\), which has the same weight;
- \(d_{j,n-1}\) has weight \(j+n\) and is connected to
  \(a_{j+1,n-1}\), again of the same weight.

Consequently the next active word is precisely

\[
A^{j+1}=A^j+y_jx2^j.
\]

Induction from the all-zero \(a_{0,i}\) row yields \(A^n=xy\).

### 1.1 Product-bit boundary weights

The output list has exactly \(2n\) bits:

\[
\begin{array}{c|c}
\text{leg}&\text{weight}\\ \hline
s_{j,0},\ 0\le j<n-1&j\\
s_{n-1,i},\ 0\le i<n&n-1+i\\
d_{n-1,n-1}&2n-1.
\end{array}
\]

These are the consecutive weights \(0,\ldots,2n-1\), with no duplication or
gap.  Pinning them to the \(2n\)-bit zero extension of \(N\) therefore imposes
exactly \(xy=N\).  There is no discarded overflow: two \(n\)-bit factors have
product below \(2^{2n}\).

### 1.2 Prefix pins and multiplicity one

The only unconstrained factor choices are the initial \(x_i\) and \(y_j\)
legs.  Their terminal chain legs carry neutral unaries.  Replacing any chosen
initial \(x_i\) unary by a zero- or one-pin therefore imposes the corresponding
fixed-length prefix bit without creating another state.

For fixed \(x,y\), process rows in increasing \(j\) and cells within a row in
increasing \(i\).  The base accumulator and carry are pinned, every
propagation bit is fixed, and the displayed recurrence uniquely determines
every \(s_{j,i},d_{j,i}\).  Hence there is at most one internal extension.
It exists exactly when the product pins agree with \(xy\).  Since \(N>0\), a
zero factor never survives, and since \(N<2^n\), every positive divisor has
the required \(n\)-bit encoding.  The contraction is therefore exactly the
number of ordered divisor pairs extending the requested \(x\)-prefix, with
multiplicity one.  This is precisely the count interface imported from P36.

I found no off-by-one weight, missing carry, extra high-bit state, or hidden
assignment multiplicity.

## 2. Planarity and the local cyclic cut

At the proposed position

\[
(u,v)=(i+j,j),
\]

the internal edge displacement vectors, oriented from the earlier cell to
the later cell, are

\[
\begin{array}{c|c}
\text{wire}&\Delta(u,v)\\ \hline
y\text{ propagation}&(1,0)\\
\text{ordinary carry}&(1,0)\\
s\text{ to next-row }a&(0,1)\\
x\text{ propagation}&(1,1)\\
\text{last carry}&(1,1).
\end{array}
\]

Thus the simple underlying graph is a finite triangular-lattice patch using
one diagonal orientation.  The two horizontal edges between neighboring
cells, and the two boundary-diagonal edges where a last carry parallels an
\(x\)-wire, are planar parallel edges; they can be given disjoint lanes in an
arbitrarily thin strip.  They do not introduce a crossing.

The exposed legs also lie on the actual exterior of this patch:

- \(a_{0,i}\) and the initial \(x_i\) legs lie on the \(j=0\) side;
- \(c_{j,0}\), the initial \(y_j\) legs, and the early finalized
  \(s_{j,0}\) legs lie on the \(i=0\) side;
- the last-row sums and terminal \(x\)-legs lie on the \(j=n-1\) side;
- terminal \(y\)-legs and the final carry lie on the \(i=n-1\) side.

Constants, target pins, free unaries, neutral unaries, and prefix pins can
therefore all be attached in the outer face.  The counts \(n^2\) cells and
\(O(n)\) boundary unaries are correct.

More importantly, the rank cut is compatible with the rotation system, not
merely with the abstract incidence graph.  At an ordinary interior cell,
using the displayed coordinates, the incoming directions are south
\((a)\), southwest \((x_L)\), and west \((y_U,c)\); the outgoing directions
are east \((y_D,d)\), northeast \((x_R)\), and north \((s)\).  Each class is
one contiguous angular sector.  Reversing the vertical drawing direction
gives exactly the north/northwest/west versus south/southeast/east wording
in the candidate.  At the last column, \(a\) shares the incoming diagonal
strip with \(x_L\), while \(d\) shares the outgoing diagonal strip with
\(x_R\); contiguity is unchanged.  The order of parallel ports can be chosen
inside the corresponding sector.

Hence, at every tile, the four \(I=(x_L,y_U,a,c)\) legs form one boundary
arc and the four \(O=(x_R,y_D,s,d)\) legs the complementary arc.  Permuting
ports inside either arc only permutes flattening rows or columns.  The
candidate does not rely on a nonplanar rotation or on a noncontiguous rank
cut.

## 3. Rank of the Boolean cell

Across \(I\mid O\), the propagation equalities force
\((x_L,y_U)=(x_R,y_D)=(x,y)\).  The flattening is therefore the direct sum of
four disjoint \(4\times4\) blocks.  For \(q=xy\), each row \((a,c)\) contains
one \(1\), in the output column determined by \(a+c+q=s+2d\).

For \(q=0\), the row images are

\[
00\mapsto00,
\quad01\mapsto10,
\quad10\mapsto10,
\quad11\mapsto01.
\]

There are exactly three distinct standard rows, so the block rank is \(3\).
For \(q=1\), the images are

\[
00\mapsto10,
\quad01\mapsto01,
\quad10\mapsto01,
\quad11\mapsto11,
\]

again giving rank \(3\).  Three of the four factor blocks use \(q=0\) and
one uses \(q=1\), but all four ranks are \(3\), so direct-sum additivity gives

\[
\operatorname{rank}\operatorname{Flat}_{I\mid O}(C)=4\cdot3=12.
\]

This computation is field-independent; in particular there is no
characteristic-zero cancellation hidden in it.

## 4. Lemma 5.1, including all degenerate charts

The candidate's power-of-two theorem is correct.  The following checks the
steps at which an even-vacuum-only proof could otherwise fail.

### 4.1 Cyclic order and Koszul signs

Because \(I\) and \(O\) are complementary contiguous arcs, the cyclic order
can be cut so that all \(I\)-modes precede all \(O\)-modes.  Permutations
inside \(I\) and inside \(O\) give row and column permutations together with
row- or column-dependent exterior signs.

A cyclic block rotation can additionally contribute
\((-1)^{|S_I||S_O|}\) to an exterior basis coefficient.  Matchgate
signatures are parity-pure.  On even support, the two subset parities agree,
so this sign is \((-1)^{|S_I|}\), a row scaling (equivalently a column
scaling).  On odd support, the parities differ and the sign is \(1\).
Thus the ordinary coefficient flattening and the exterior-algebra
flattening have the same rank for a contiguous cut.  This is exactly where
contiguity is used; no arbitrary-bipartition sign claim is needed.

### 4.2 Particle-hole reduction reaches the even vacuum chart

Let \(F_S\ne0\).  On an occupation word, the Clifford operator

\[
\gamma_i=e_i\wedge+\iota_{e_i}
\]

toggles bit \(i\) with sign determined by the earlier occupied modes.  In
ordinary tensor coordinates its matrix is

\[
Z_1\otimes\cdots\otimes Z_{i-1}\otimes X_i\otimes
I_{i+1}\otimes\cdots\otimes I_m.
\]

It is consequently a tensor product of invertible one-leg maps.  It
preserves the rank of every flattening, including when its \(Z\)-string
crosses the \(I\mid O\) cut.  Products of these operators remain tensor
products of invertible one-leg Pauli maps, up to an irrelevant scalar sign.

Each \(\gamma_i\) is Clifford multiplication by a nonisotropic vector and
therefore maps pure spinors to pure spinors.  The product over \(i\in S\) is
a signed permutation of the occupation basis, so exactly the coefficient
\(F_S\), with no possible cancellation from another coefficient, becomes
the vacuum coefficient.

This also handles odd signatures.  A matchgate signature is supported in
one parity, so \(|S|\) has the parity of \(F\).  Applying \(|S|\)
particle-hole operators changes the parity by \(|S|\), making the resulting
nonzero-vacuum spinor \(G\) even.  Thus the subsequent even Pfaffian chart is
valid for an originally even or odd signature and for an arbitrary
degenerate starting chart.

### 4.3 Rank in the vacuum Pfaffian chart

For \(G_\varnothing\ne0\), the matchgate identities give

\[
G=G_\varnothing\exp(\omega).
\]

With \(V=V_I\oplus V_O\), write

\[
\omega=\omega_I+\omega_O+\omega_{IO}.
\]

The even forms commute.  Multiplication by
\(\exp(\omega_I)\) and \(\exp(\omega_O)\) acts invertibly on the row and
column exterior spaces, respectively, so neither changes rank.  If \(B\) is
the matrix of the cross-form and \(r=\operatorname{rank}B\), independent
one-particle changes of basis on the two sides put it into

\[
\omega_{IO}=\sum_{k=1}^r\lambda_k u_k\wedge v_k,
\qquad \lambda_k\ne0.
\]

Then

\[
\exp(\omega_{IO})=
\prod_{k=1}^r(1+\lambda_k u_k\wedge v_k).
\]

In the coefficient flattening, rows and columns indexed by the same subset
of the \(r\) paired modes have nonzero diagonal coefficients; all other
paired-mode entries vanish.  Reordering the exterior factors may insert
subset-dependent nonzero signs, but only rescales these nonzero diagonal
entries.  Hence this paired part has rank \(2^r\).  Unused modes contribute
rank-one vacuum factors.  Undoing the invertible row and column operations,
and then the particle-hole operations, proves Lemma 5.1 for every nonzero
even or odd matchgate chart.

No assumption that the original vacuum coefficient is nonzero survives in
the argument.

## 5. The noncontiguous rank-three example

For

\[
\omega=e_1\wedge e_2+e_3\wedge e_4
       +e_1\wedge e_4+e_2\wedge e_3,
\]

the Pfaffian four-body coefficient is

\[
A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}=1+1=2.
\]

Using rows
\(\varnothing,\{1\},\{3\},\{1,3\}\) and columns
\(\varnothing,\{2\},\{4\},\{2,4\}\), its **ordinary**
\(\{1,3\}\mid\{2,4\}\) flattening is

\[
\begin{pmatrix}
1&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&2
\end{pmatrix}.
\]

Over characteristic zero this has rank \(3\).  The split alternates around
the cyclic order and is noncontiguous.  The example is therefore correct and
does exactly what the candidate claims: it rules out an illicit extension
of Lemma 5.1 to arbitrary ordinary tensor bipartitions, without weakening the
contiguous obstruction used for \(C\).

## 6. Independent leg actions and gauge inference

For arbitrary \(T_\ell\in\operatorname{GL}_2\), the selected flattening is
left- and right-multiplied by the corresponding Kronecker products:

\[
\Bigl(\bigotimes_{\ell\in I}T_\ell\Bigr)
\operatorname{Flat}_{I\mid O}(C)
\Bigl(\bigotimes_{\ell\in O}T_\ell\Bigr)^{\mathsf T},
\]

up to the covariant/contravariant convention.  Both factors are invertible,
so the rank remains \(12\).  An invertible action also cannot turn \(C\ne0\)
into the zero signature.  Lemma 5.1 would force any matchgate in the stated
cyclic order to have rank a power of two across this cut.  Since \(12\) is
not a power of two, no independent local leg actions put \(C\) in that
matchgate orbit.

A contraction-compatible edge gauge is a strict specialization: the two
endpoint actions must be transpose-dual.  Since even unconstrained
independent actions fail at one cell, shared-edge compatibility cannot repair
this cell/order.  This inference does not assume that a basis making one
cell a matchgate could be extended globally; it proves the stronger fact
that there is no such local basis to extend.

## 7. Minimality and scope

The candidate's use of “minimal” is properly restricted to its declared
interface.  An interior scalar-Boolean nearest-neighbor schoolbook tile that
passes each of two independently varying factor bits to its next occurrence
has two incidences for each factor bit.  A one-column full shifted-add update
has distinct incoming and outgoing accumulator incidences and distinct
incoming and outgoing ripple-carry incidences.  The local truth table does
not identify these roles: factor bits vary independently, and the arithmetic
table contains unequal values for every proposed input/output state
identification.  Within that interface the count \(4+4=8\) is attained.

This is only an interface-count statement.  The candidate expressly does
not turn it into a lower bound for asymmetric tiles, packed or higher-domain
wires, projected auxiliary states, different arithmetic schedules, or
larger fused blocks.

The separation from the promoted prior results is also correct:

- P36/X30 obstructs a separated ternary COPY--AND realization under common
  role bases and transpose-dual actions; \(C\) has neither external partial
  product nor standalone ternary COPY/AND and the present test allows eight
  independent leg actions.
- P38 is a support theorem for positive boundary-deletion matching
  signatures, not a signed matchgate-orbit theorem for ordinary Boolean
  tensors.
- P42 concerns closed edge-occupancy gadgets and a universal clean
  four-port connector.  Neither its positive AND/COPY examples nor its
  connector obstruction decides this tensor orbit.

The candidate closes no more than the stated cell-by-cell landing in the
displayed rotation system.  It correctly leaves open different cyclic port
orders, larger blocks, block encodings, noninvertible projections, global
Pfaffian identities not decomposed into matchgate copies of \(C\), modular
constructions outside the stated characteristic-zero theorem, and
non-matchgate contraction algorithms.  It also correctly does not claim
that original-network planarity alone yields an FKT evaluation, that
transformed pins have been solved, or that factoring follows from this
negative result.

The original \(0/1\) network has polynomial description size and its pinned
count is at most the number \(2^n\) of \(x\)-words, so the stated \(O(n)\)
answer-bit bound is valid.  Coefficient representation and Pfaffian bit
growth are explicitly left as obligations only for a different surviving
construction.

## 8. Final audit conclusion

All requested attack points survived:

1. the shifted-add wiring has correct state shifts, carries, output weights,
   boundary pins, and multiplicity-one semantics;
2. the proposed triangular-lattice embedding is planar and places the
   incoming and outgoing four-leg sets on complementary contiguous arcs at
   every tile, including the last column;
3. the cell flattening rank is exactly \(12\);
4. the particle-hole argument covers degenerate even and odd pure-spinor
   charts and preserves flattening rank, while contiguous-cut signs are only
   rank-preserving row/column changes;
5. the explicit noncontiguous pure-spinor example really has ordinary rank
   \(3\);
6. arbitrary independent invertible leg actions preserve the obstructing
   rank, so compatible edge gauges cannot evade it; and
7. the minimality and negative conclusion remain within the explicitly
   declared scalar-cell/order scope.

I therefore find no exact mathematical repair to demand.

> **PASS AS WRITTEN.**
