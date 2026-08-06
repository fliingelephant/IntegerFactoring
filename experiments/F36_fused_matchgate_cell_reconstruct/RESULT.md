# Reconstruction of the fused scalar-Boolean cell obstruction

Let the ground field be \(K\) of characteristic zero, and let every leg of \(C\) be Boolean. I use \(x_i\) for the bit propagated through logical column \(i\), \(y_j\) for the bit propagated through logical row \(j\), and \(X=\sum_{i=0}^{n-1}2^i x_i\), \(Y=\sum_{j=0}^{n-1}2^j y_j\). All ranks below are ordinary tensor-flattening ranks over \(K\).

## 1. Arithmetic represented by the tiling

Connect

\[
x_R(j,i)=x_L(j+1,i),\qquad
y_D(j,i)=y_U(j,i+1),
\]

whenever the indicated neighboring cell exists. The equality factors in \(C\) then make the first quantity equal to \(x_i\) throughout logical column \(i\), and the second equal to \(y_j\) throughout logical row \(j\). Also connect

\[
d_{j,i}=c_{j,i+1}\quad(0\leq i<n-1),
\]

and, for \(j<n-1\),

\[
s_{j,i}=a_{j+1,i-1}\quad(1\leq i<n),
\qquad
d_{j,n-1}=a_{j+1,n-1}.
\]

The boundary conditions are \(a_{0,i}=0\) and \(c_{j,0}=0\). Thus every cell equation is

\[
a_{j,i}+c_{j,i}+x_i y_j=s_{j,i}+2d_{j,i}. \tag{1}
\]

Define the value entering row \(j\) by

\[
A_j=\sum_{i=0}^{n-1}2^i a_{j,i}.
\]

Multiplying (1) by \(2^i\) and summing over a row cancels all carries except the last one:

\[
A_j+Xy_j=\sum_{i=0}^{n-1}2^i s_{j,i}+2^n d_{j,n-1}. \tag{2}
\]

Indeed, the incoming-carry sum is

\[
\sum_i2^i c_{j,i}=\sum_{i=0}^{n-2}2^{i+1}d_{j,i},
\]

which cancels the corresponding part of the outgoing-carry sum. For \(j<n-1\), the diagonal sum connections and the special last-carry connection give

\[
A_{j+1}=\sum_{i=1}^{n-1}2^{i-1}s_{j,i}+2^{n-1}d_{j,n-1}.
\]

Consequently (2) is exactly

\[
A_j+Xy_j=s_{j,0}+2A_{j+1}. \tag{3}
\]

This displays why the last carry must feed \(a_{j+1,n-1}\): without that edge, the term \(2^n d_{j,n-1}\) in (2) would be lost.

Multiply (3) by \(2^j\), sum it for \(0\leq j<n-1\), use \(A_0=0\), and cancel the intermediate \(A_j\)'s. This gives

\[
X\sum_{j=0}^{n-2}2^j y_j
=\sum_{j=0}^{n-2}2^j s_{j,0}+2^{n-1}A_{n-1}. \tag{4}
\]

For the final row, multiply (2) by \(2^{n-1}\) and combine with (4). The result is

\[
XY=
\sum_{j=0}^{n-2}2^j s_{j,0}
+\sum_{i=0}^{n-1}2^{n-1+i}s_{n-1,i}
+2^{2n-1}d_{n-1,n-1}. \tag{5}
\]

Thus the output bits, in increasing weight, are

\[
s_{0,0},\ldots,s_{n-2,0},
s_{n-1,0},\ldots,s_{n-1,n-1},
d_{n-1,n-1},
\]

at weights \(0,\ldots,2n-1\). Formula (5) also covers \(n=1\), when the first list is empty.

There is no hidden multiplicity. Given the boundary factor bits, process cells in increasing \(j\), and within a row in increasing \(i\). At each cell, \(a,c,x,y\) are already known, and the integer \(a+c+xy\in\{0,1,2,3\}\) has a unique binary decomposition \(s+2d\) with \(s,d\in\{0,1\}\). Hence all internal legs are uniquely determined. Conversely, any satisfying assignment obeys (5), so target pins spelling \(N\) imply \(XY=N\). The two factor buses distinguish \(X\) from \(Y\), so these are ordered pairs. Optional factor-prefix unaries merely restrict this bijection to pairs obeying those prefixes; with only the product fixed to \(N\), it is exactly the asserted bijection with all ordered \(n\)-bit factor pairs of \(N\).

## 2. Planarity and boundary placement

Place cell \((j,i)\) at

\[
(u,v)=(i+j,j).
\]

The centers occupy the lattice parallelogram \(0\leq v<n\), \(0\leq u-v<n\). The connections above use only three kinds of lattice segment:

* row propagation and ordinary carry use \((u,v)\)--\((u+1,v)\);
* diagonal sum propagation uses \((u,v)\)--\((u,v+1)\);
* column propagation uses \((u,v)\)--\((u+1,v+1)\).

On the rightmost logical column, the special last-carry edge uses the third kind of segment in parallel with the \(x\)-propagation edge. Row propagation and ordinary carry are likewise parallel on the first kind. Replace every center by a small disk and every lattice segment by a sufficiently thin corridor. Horizontal, vertical, and only one orientation of diagonal occur, so distinct corridors meet only at endpoint disks. Parallel wires can be drawn as disjoint curves inside their common corridor. This is a planar multigraph embedding.

At a generic disk the incoming wires approach from west \((y_U,c)\), northwest \((x_L)\), and north \((a)\); the outgoing wires leave east \((y_D,d)\), southeast \((x_R)\), and south \((s)\). Hence all four legs

\[
I=\{x_L,y_U,a,c\}
\]

occupy one uninterrupted boundary arc of the disk, and all four legs

\[
O=\{x_R,y_D,s,d\}
\]

occupy the complementary arc. On the right boundary, \(a\) joins the northwest parallel bundle and \(d\) joins the southeast parallel bundle, so the same assertion remains true. The order chosen among parallel ports inside either arc is immaterial to the \(I\mid O\) rank, since it only permutes rows or columns.

All remaining attachments really are on the outer face. The \(a_{0,i}\) pins and initial \(x_i\)'s are on the top side; the \(c_{j,0}\) pins and initial \(y_j\)'s are on the left slanted side. For \(j<n-1\), \(s_{j,0}\) leaves that slanted side; all \(s_{n-1,i}\) leave the bottom; and \(d_{n-1,n-1}\) leaves the final corner. Unused terminal copies of \(x\) and \(y\) can be terminated by the neutral unary \((1,1)\) on the bottom and right sides. Target-bit unaries attach to the displayed product legs, and factor-prefix unaries attach to the initial factor legs. Since each is attached in a thin outer collar next to its boundary leg, none introduces a crossing.

## 3. Rank of the cell flattening

Flatten \(C\) with rows indexed by \((x_L,y_U,a,c)\) and columns by \((x_R,y_D,s,d)\). The two propagation equalities make this matrix a direct sum of four blocks, one for every fixed pair \((x,y)=(x_L,y_U)=(x_R,y_D)\). Within a block, rows are indexed by \((a,c)\), columns by \((s,d)\), and the entry is

\[
1[a+c+xy=s+2d].
\]

If \(xy=0\), the possible totals are \(0,1,2\): rows \(00\), \(01/10\), and \(11\) respectively select three distinct standard-basis columns. If \(xy=1\), the possible totals are \(1,2,3\), with the same three-row pattern. Each block therefore has rank \(3\). The four blocks have disjoint row and column supports, so

\[
\operatorname{rank}\operatorname{Flat}_{I\mid O}(C)=4\cdot3=12. \tag{6}
\]

## 4. Contiguous-cut rank lemma for every pure-spinor chart

I now prove the needed statement without assuming a nonzero vacuum coefficient.

Let \(E=\langle e_1,\ldots,e_m\rangle_K\), with spinor module \(\Lambda E\), and write

\[
|z\rangle=e_1^{z_1}\wedge\cdots\wedge e_m^{z_m}
\qquad(z\in\{0,1\}^m)
\]

in increasing mode order. A nonzero matchgate signature is a pure spinor of a definite parity in this coefficient convention.

### Reaching the vacuum chart

Let \(\iota_i\) denote contraction by \(e_i^*\), and set

\[
\gamma_i=e_i\wedge+\iota_i.
\]

Then

\[
\gamma_i|z\rangle=(-1)^{z_1+\cdots+z_{i-1}}|z\oplus e_i\rangle.
\]

Thus, as an ordinary Boolean tensor operator,

\[
\gamma_i=Z_1\otimes\cdots\otimes Z_{i-1}\otimes X_i\otimes I_{i+1}\otimes\cdots\otimes I_m,
\]

where \(X=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) and \(Z=\operatorname{diag}(1,-1)\). It is therefore a tensor product of invertible one-leg maps. Any product of the \(\gamma_i\)'s has the same property and preserves every ordinary flattening rank.

Moreover \(\gamma_i^2=1\), and \(\gamma_i\) is an invertible Clifford vector. Clifford conjugation carries a maximal isotropic annihilator to a maximal isotropic annihilator, so it preserves pure-spinor status (while one \(\gamma_i\) switches parity).

Choose any nonzero coefficient \(\psi_S\) of the given nonzero pure spinor \(\psi\), and apply the product of \(\gamma_i\) over \(i\in S\), in any fixed order. This toggles support by symmetric difference with \(S\), so the new vacuum coefficient is \(\pm\psi_S\ne0\). Since every nonzero coefficient of \(\psi\) has the parity of \(\psi\), the transformed spinor is even. This handles odd spinors and every degenerate Pfaffian chart.

For completeness, a pure spinor \(\phi\) with scalar coefficient \(\lambda\ne0\) necessarily has the form

\[
\phi=\lambda\exp(\omega),\qquad \omega\in\Lambda^2E. \tag{7}
\]

Indeed, projection of its maximal isotropic annihilator to the contraction space \(E^*\) is injective: a pure creation operator \(v\wedge\) annihilating \(\phi\) would have degree-one term \(\lambda v\), hence \(v=0\). By dimension, the projection is an isomorphism. Isotropy says that this annihilator is the graph

\[
\{\,\iota_\alpha-(\iota_\alpha\omega)\wedge:\alpha\in E^*\,\}

\]

for a unique two-form \(\omega\). These operators annihilate \(\exp(\omega)\), because

\[
\iota_\alpha\exp(\omega)=(\iota_\alpha\omega)\wedge\exp(\omega).
\]

Equivalently, wedging \(\phi\) by \(\exp(-\omega)\) produces a form killed by every contraction, hence just its scalar \(\lambda\). This proves (7). Characteristic zero ensures the finite exponential has its usual factorial coefficients.

### The contiguous split

There is one sign issue in making a cyclic order linear. Moving an ordered prefix \(P\) past its suffix \(Q\) changes a wedge monomial by

\[
(-1)^{|S\cap P|\,|S\cap Q|}.
\]

On a parity-\(p\) spinor, put \(a=|S\cap P|\), \(b=|S\cap Q|\). Since \(a+b\equiv p\pmod2\), the exponent satisfies

\[
ab\equiv (p+1)a\pmod2.
\]

Hence a cyclic rotation changes the ordinary coefficient tensor only by the axis permutation and a product of one-leg \(Z\)'s on \(P\) (for even parity), or by the axis permutation alone (for odd parity). In particular it preserves flattening rank. This accounts for the cyclic/Koszul sign rather than silently discarding it.

Now suppose \(I\) is one cyclic boundary arc and \(O\) its complementary arc. Contiguity is used precisely here: a cyclic rotation, with no interleaving shuffle, puts every \(I\)-mode before every \(O\)-mode. Write \(E=E_I\oplus E_O\), in that order. After the rank-preserving vacuum-chart operation above, decompose

\[
\omega=\omega_I+\beta+\omega_O,
\]

where \(\omega_I\in\Lambda^2E_I\), \(\omega_O\in\Lambda^2E_O\), and \(\beta\in E_I\wedge E_O\). Under the canonical ordered identification

\[
\Lambda(E_I\oplus E_O)\cong\Lambda E_I\otimes\Lambda E_O,
\qquad \alpha\otimes\eta\longmapsto\alpha\wedge\eta,
\]

ordinary tensor entries have no additional regrouping sign. Since two-forms commute under wedge,

\[
\exp(\omega)=\exp(\omega_I)\wedge\exp(\beta)\wedge\exp(\omega_O).
\]

Exterior multiplication by \(\exp(\omega_I)\) is an invertible row map, with inverse exterior multiplication by \(\exp(-\omega_I)\); the analogous \(O\)-map is an invertible column map. Therefore the flattening rank equals that of \(\exp(\beta)\).

Identify (\beta) with its (I\)-by-(O) coefficient matrix and let its ordinary matrix rank be (r). Independent changes of basis in (E_I) and (E_O), whose exterior powers are invertible row and column maps, put it into the form

\[
\beta=\sum_{k=1}^r p_k\wedge q_k.
\]

The summands commute and square to zero, so

\[
\exp(\beta)=\prod_{k=1}^r(1+p_k\wedge q_k)
=\sum_{T\subseteq[r]}(-1)^{|T|(|T|-1)/2}p_T\wedge q_T. \tag{8}
\]

The sign in (8) is the cost of moving each selected (q_k) past the later selected (p)'s. Under the ordered tensor identification, (8) is a diagonal pairing between the (2^r) distinct row basis vectors (p_T) and the (2^r) distinct column basis vectors (q_T), with every diagonal coefficient equal to (\pm1). Hence

\[
\operatorname{rank}\operatorname{Flat}_{I\mid O}(\psi)=2^r. \tag{9}
\]

All transformations used to reach (9) were invertible row/column operations for this flattening. Thus (9) holds for every nonzero pure spinor, in either parity and in every chart, across a contiguous cyclic split.

## 5. Why contiguity cannot be omitted

Consider four modes in their ordinary order (1,2,3,4), and

\[
\Psi=\exp(e_1e_2+e_3e_4+e_1e_4+e_2e_3).
\]

It is a pure spinor by the vacuum-chart argument above. Writing wedges explicitly, the only two disjoint pairings in the square of the exponent are ((12)(34)) and ((14)(23)), both with positive orientation. Therefore

\[
\Psi=1+e_{12}+e_{34}+e_{14}+e_{23}+2e_{1234}. \tag{10}
\]

For the ordinary, noncontiguous split (\{1,3\}\mid\{2,4\}), order rows as

\[
\varnothing,\{1\},\{3\},\{1,3\}
\]

and columns as

\[
\varnothing,\{2\},\{4\},\{2,4\}.
\]

Directly from the coefficients in the original (1,2,3,4) order, the flattening is

\[
\begin{pmatrix}
1&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&2
\end{pmatrix}. \tag{11}
\]

Its first, second, and fourth rows are independent and its third row repeats the second, so its rank is exactly (3) in characteristic zero. To put the modes into (1,3\mid2,4) order one would need a genuinely interleaving permutation. Its Koszul sign depends bilinearly on selected row and column bits and is not, in general, a row factor times a column factor. Equation (11) is an explicit demonstration that dropping contiguity invalidates the power-of-two conclusion.

## 6. Matchgate-orbit consequence and scope

For independent (G_\ell\in\mathrm{GL}_2(K)) on the eight legs, the selected flattening transforms as

\[
M\longmapsto
\left(\bigotimes_{\ell\in I}G_\ell\right)
M
\left(\bigotimes_{\ell\in O}G_\ell\right)^{\!T},
\]

up to harmless choices of row/column convention. Both multipliers are invertible, so the rank remains (12). If this cell were in the independent-leg (\mathrm{GL}_2) orbit of a nonzero planar matchgate in the displayed cyclic port arrangement, its contiguous (I\mid O) flattening would have to have rank (2^r) by (9). No power of two is (12). Therefore this scalar-Boolean cell is not in that matchgate orbit. Since compatible gauges on two ends of every shared edge are a restriction on independent leg transformations, the obstruction arises before shared-edge compatibility is considered.

This conclusion is deliberately narrow. It excludes only the displayed natural scalar-Boolean cell with this input/output cyclic separation. It does not exclude larger fused blocks, other rotations or encodings, global Pfaffian identities not obtained from such a cellwise matchgate realization, modular constructions, or contractions by non-matchgate tensors.

RECONSTRUCTED
