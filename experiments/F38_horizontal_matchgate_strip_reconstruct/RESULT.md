# Independent reconstruction: horizontal matchgate strips

This report proves the stated claim from the bare definition. All Boolean labels below lie in \(\{0,1\}\). Every equality inside an indicator is an equality of ordinary integers; only the resulting value \(0\) or \(1\) is embedded in the field. This distinction is essential in positive characteristic.

## 1. Exact horizontal fusion

For cell \(i\), rename its two \(y\)-legs as \(y_i,y_{i+1}\) and its carry legs as \(c_i,c_{i+1}\). Thus
\[
C_i=
\mathbf 1[x_i^-=x_i^+]\,
\mathbf 1[y_i=y_{i+1}]\,
\mathbf 1[a_i+c_i+x_i^-y_i=s_i+2c_{i+1}].
\]
The fused tensor is exactly
\[
T_L=
\sum_{\substack{y_1,\ldots,y_{L-1}\\c_1,\ldots,c_{L-1}}}
\prod_{i=0}^{L-1} C_i,                                      \tag{1}
\]
where every summed label is Boolean. Put
\[
X=\sum_{i=0}^{L-1}2^i x_i^-,\qquad
A=\sum_{i=0}^{L-1}2^i a_i,\qquad
S=\sum_{i=0}^{L-1}2^i s_i.
\]

### Necessity and multiplicity at most one

A nonzero summand in (1) forces
\[
x_i^-=x_i^+\quad(0\leq i<L),\qquad
y_0=y_1=\cdots=y_L=:y,
\]
and the local recurrences
\[
a_i+c_i+yx_i^-=s_i+2c_{i+1}.                                \tag{2}
\]
Multiplying (2) by \(2^i\) and summing makes the internal carry terms telescope:
\[
A+yX+c_0=S+2^L c_L.                                         \tag{3}
\]
Moreover, \(y_1,\ldots,y_{L-1}\) are already forced by \(y_0\), and (2), starting from the exposed \(c_0\), determines each next carry uniquely. Hence there is at most one nonzero summand in (1).

### Converse, including Booleanity of every internal carry

Assume the propagation equalities and (3), and set
\[
b_i=a_i+yx_i^- -s_i.
\]
Then (3) is the integer identity
\[
c_0+\sum_{i=0}^{L-1}2^i b_i=2^L c_L.                        \tag{4}
\]
We construct the carries from low to high. Suppose \(c_i\in\{0,1\}\) has been obtained and the lower-bit equations imply
\[
c_0+\sum_{j=0}^{i-1}2^j b_j=2^i c_i.                        \tag{5}
\]
For \(i=0\), (5) is just \(c_0=c_0\). Subtracting (5) from (4) and dividing as an integer by \(2^i\) shows that
\[
t_i:=b_i+c_i=a_i+yx_i^-+c_i-s_i
\]
is even. Since its four terms are Boolean in the displayed signed combination,
\[
-1\leq t_i\leq 3.
\]
The only even values in this range are \(0\) and \(2\). Therefore
\[
c_{i+1}:=t_i/2\in\{0,1\},
\]
and this is precisely (2). It also advances (5) from \(i\) to \(i+1\). At \(i=L-1\), (4) gives \(t_{L-1}=2c_L\), so the constructed last carry equals the prescribed exposed \(c_L\). Thus all local indicators are one. The construction is forced at every step, so the summand is unique.

Consequently, over every field,
\[
\boxed{
T_L=
\left(\prod_{i=0}^{L-1}\mathbf 1[x_i^-=x_i^+]\right)
\mathbf 1[y_0=y_L]
\mathbf 1[A+y_0X+c_0=S+2^L c_L]
}.                                                           \tag{6}
\]
There is no characteristic-dependent multiplicity: an allowed entry receives exactly one contribution equal to \(1\), and a forbidden entry receives none.

### Range and the case \(L=1\)

The relevant integer ranges are
\[
0\leq X,A,S\leq 2^L-1,
\qquad
0\leq A+y_0X+c_0\leq 2^{L+1}-1.
\]
Also, \((S,c_L)\mapsto S+2^Lc_L\) is a bijection from its Boolean labels onto every integer in \([0,2^{L+1}-1]\). Thus (6) neither suppresses a needed overflow value nor permits a carry beyond the exposed Boolean \(c_L\).

For \(L=1\), there are no contracted labels and (6) reads
\[
C_0=
\mathbf 1[x_0^-=x_0^+]\mathbf 1[y_0=y_1]
\mathbf 1[a_0+y_0x_0^-+c_0=s_0+2c_1],
\]
which is the defining cell itself. So the endpoint and converse arguments include the one-cell strip without an empty-strip assumption.

## 2. An explicit planar rotation and its boundary arcs

Represent cell \(i\) by a small disk and place its ports clockwise in the order
\[
x_i^-,\ a_i,\ y_{i+1},\ c_{i+1},\ x_i^+,\ s_i,\ c_i,\ y_i. \tag{7}
\]
Put the disks from left to right. On each disk, place \(y_i\) upper-left and \(c_i\) lower-left, and place \(y_{i+1}\) upper-right and \(c_{i+1}\) lower-right. The two ports \(x_i^-,a_i\) then leave through the upper sector from left to right, while \(x_i^+,s_i\) leave through the lower sector from right to left.

For every adjacent pair of disks, connect the shared \(y_{i+1}\) ports through the upper corridor and the shared \(c_{i+1}\) ports through a disjoint lower corridor. This is a planar embedding, not merely an abstract rotation-system assertion:

* at the left endpoint of a gap, its two corridor half-edges occur consecutively as \(y_{i+1},c_{i+1}\) in (7);
* at the right endpoint, the same two half-edges occur consecutively in the reverse facial order as \(c_{i+1},y_{i+1}\);
* hence those two parallel edges bound an empty digon, or lens face, and no external port lies inside it.

The gap rectangles are disjoint, so all \(L-1\) lens faces coexist without crossings. At the left end, \(c_0,y_0\) are consecutive across the cyclic end of (7), and they exit lower-left and upper-left. At the right end, \(y_L,c_L\) are consecutive and exit upper-right and lower-right. Thus neither endpoint closes a corridor around an external leg.

Reading the outer face clockwise, beginning at \(c_0\), gives
\[
\begin{split}
c_0,\ y_0,&\ x_0^-,a_0,\ x_1^-,a_1,\ldots,
x_{L-1}^-,a_{L-1},\\
&y_L,c_L,\ x_{L-1}^+,s_{L-1},\ldots,x_0^+,s_0.
\end{split}                                                   \tag{8}
\]
The return from the last entry to \(c_0\) closes the cycle. Therefore
\[
I_L=\{x_i^-:0\leq i<L\}\cup\{a_i:0\leq i<L\}\cup\{y_0,c_0\}
\]
is the single arc in (8) from \(c_0\) through \(a_{L-1}\), and
\[
O_L=\{x_i^+:0\leq i<L\}\cup\{s_i:0\leq i<L\}\cup\{y_L,c_L\}
\]
is its complementary arc. In a linear boundary list begun on the top, the incoming set appears as the top segment together with the two left legs at the other end of the list; its contiguity uses the cyclic wrap. It is not being inferred merely from the abstract planarity of the chain.

When \(L=1\), there is no lens, and (8) reduces to
\[
c_0,y_0,x_0^-,a_0,y_1,c_1,x_0^+,s_0,
\]
so the same two complementary arcs remain valid.

## 3. Exact rank across \(I_L\mid O_L\)

Flatten (6) with rows indexed by the incoming labels and columns by the outgoing labels. The propagation indicators say that a row with \((x_0^-,\ldots,x_{L-1}^-,y_0)=(x,y)\) can meet only columns with
\[
(x_0^+,\ldots,x_{L-1}^+,y_L)=(x,y).
\]
After row and column permutations, the matrix is therefore a direct sum of exactly
\[
2^L\cdot 2=2^{L+1}
\]
arithmetic blocks, one for every pair \((x,y)\). These blocks have disjoint row and column sets even when two pairs give the same numerical value below.

Fix one pair and put \(Q=yX\). Inside its block, rows are indexed by \((A,c_0)\), columns by \((S,c_L)\), and a row is nonzero precisely at the column whose integer label is
\[
W:=S+2^Lc_L=Q+A+c_0.                                         \tag{9}
\]
The output encoding \((S,c_L)\mapsto W\) is bijective on \([0,2^{L+1}-1]\), so every row is a standard basis row. As \(A\) and \(c_0\) vary,
\[
\{A+c_0\}=\{0,1,\ldots,2^L\};
\]
hence the used output columns are exactly
\[
Q,Q+1,\ldots,Q+2^L.                                         \tag{10}
\]
They are all legal because \(0\leq Q\leq 2^L-1\), so
\[
0\leq Q\leq Q+2^L\leq 2^{L+1}-1.
\]
Distinct standard basis rows are linearly independent over every field, while duplicate rows add no rank. Thus every arithmetic block has rank exactly
\[
2^L+1.
\]
Ranks add over a direct sum, yielding
\[
\boxed{\operatorname{rank}_{I_L\mid O_L}(T_L)
=2^{L+1}(2^L+1)}                                             \tag{11}
\]
over every field. For \(L=1\), this is four propagation blocks of rank three, hence total rank \(12\), agreeing with the direct one-cell description.

For \(L\geq1\), the factor \(2^L+1\) is odd and greater than one. Therefore (11) is never a power of two.

## 4. The all-chart pure-spinor rank lemma

Here the field has characteristic zero. The required statement is:

> Every nonzero matchgate, equivalently parity-homogeneous pure-spinor, signature has flattening rank \(2^r\) across any two complementary contiguous cyclic boundary arcs, for some integer \(r\geq0\).

The following argument includes charts with zero vacuum coordinate, odd signatures, and the exterior-algebra signs.

Cut the cyclic order at a junction of the two arcs and write the mode space as
\[
E=U\oplus V,
\]
where \(U\) contains the incoming-arc modes and \(V\) the outgoing-arc modes. Use the Fock basis of \(\Lambda E\). If a different cyclic cut moves the whole \(U\)-block past the \(V\)-block, a coefficient of bidegree \((p,q)\) acquires the Koszul sign \((-1)^{pq}\). A matchgate signature has fixed total parity. On its even support, \(p\equiv q\pmod2\), so this sign is the row sign \((-1)^p\); on its odd support, \(p\not\equiv q\pmod2\), so the sign is one. Thus recutting changes the flattening only by invertible diagonal/permutation operations and does not change rank.

### Reaching a vacuum chart

For mode \(j\), let
\[
\tau_j=\varepsilon(e_j)+\iota(e_j^*)
\]
be the particle-hole Clifford operator. On a basis vector it toggles occupation of \(j\) with the exact Jordan-Wigner sign
\[
\tau_j|R\rangle=(-1)^{|R\cap\{1,\ldots,j-1\}|}
|R\mathbin\triangle\{j\}\rangle.                            \tag{12}
\]
Equivalently, in tensor coordinates it is
\[
Z_1\otimes\cdots\otimes Z_{j-1}\otimes X_j\otimes I\otimes\cdots,
\]
up to the fixed basis convention. Hence it is an invertible product of one-leg operations and preserves every bipartite flattening rank. It is also a Pin/Clifford operation: \(\tau_j^2=1\), and conjugation by it carries a maximal isotropic annihilator to another maximal isotropic annihilator. It therefore maps pure spinors to pure spinors.

Choose any nonzero coefficient \(\psi_T\) of a nonzero pure spinor \(\psi\), and apply the product of \(\tau_j\) over \(j\in T\). This product is a signed permutation of the Fock basis, and its vacuum coefficient is exactly \(\pm\psi_T\neq0\). It preserves flattening rank and purity. If \(\psi\) was odd, then \(|T|\) is odd, so the toggled spinor is even; if \(\psi\) was even, \(|T|\) is even. Thus in all cases the transformed spinor is in the even, nonzero-vacuum chart. This handles both odd signatures and every degenerate chart in which the original vacuum coordinate vanished.

### Rank in the vacuum chart

The standard big-cell description of a pure spinor with nonzero vacuum coefficient is
\[
\psi=\alpha\exp(\omega),\qquad \alpha\neq0,\quad
\omega\in\Lambda^2E.                                        \tag{13}
\]
Decompose
\[
\omega=\omega_U+\omega_V+\omega_{UV}
\]
according to
\(\Lambda^2E=\Lambda^2U\oplus(U\wedge V)\oplus\Lambda^2V\).
All three summands have even exterior degree and commute, so
\[
\exp(\omega)=
\exp(\omega_U)\exp(\omega_{UV})\exp(\omega_V).              \tag{14}
\]
Exterior multiplication by \(\exp(\omega_U)\) is an invertible operation on the \(U\)-row space, with inverse multiplication by \(\exp(-\omega_U)\). The \(V\) term gives the analogous invertible column operation. Thus only the cross term can affect rank.

Write the cross term as the matrix-valued bilinear form
\[
\omega_{UV}=\sum_{i,j}B_{ij}u_i\wedge v_j
\]
and let \(r=\operatorname{rank}B\). Invertible changes of basis in \(U\) and \(V\), whose induced exterior-power maps are invertible row and column operations, reduce it to
\[
\omega_{UV}=u_1\wedge v_1+\cdots+u_r\wedge v_r.             \tag{15}
\]
Because the displayed degree-two terms commute and square to zero,
\[
\exp(\omega_{UV})
=\prod_{j=1}^r(1+u_j\wedge v_j)
=\sum_{J\subseteq[r]}(-1)^{\binom{|J|}{2}}u_J\otimes v_J.  \tag{16}
\]
The sign in (16) is the sign from moving each selected \(v_j\) past all later selected \(u\)'s; it is never zero in characteristic zero. In the exterior bases \(\{u_J\}\) and \(\{v_J\}\), (16) is a diagonal matrix on the \(2^r\) paired subsets, with diagonal entries \(\pm1\), and zero elsewhere. Its rank is exactly \(2^r\). The case \(r=0\) gives rank one. Combining (12)--(16) proves the all-chart lemma without assuming a nonzero original vacuum coordinate or even parity.

Applying the lemma to (11), the horizontal-strip tensor cannot be a nonzero matchgate/pure-spinor signature in this planar cyclic port order over characteristic zero, because its exhibited contiguous-arc rank is not a power of two.

## 5. Leg gauges

Let an arbitrary \(G_\ell\in\mathrm{GL}_2\) act independently on every exposed leg. Across \(I_L\mid O_L\), the new flattening has the form
\[
M'=
\left(\bigotimes_{\ell\in I_L}G_\ell\right)
M
\left(\bigotimes_{\ell\in O_L}G_\ell\right)^{\!\mathsf T}, \tag{17}
\]
up to harmless basis-order permutations and transpose conventions. Both outer factors are invertible, so (11) is unchanged. In particular, even gauges that do not themselves preserve the matchgate variety cannot turn this tensor into a matchgate: if the gauged tensor were one, the all-chart lemma would force the unchanged rank to be a power of two.

On a contracted shared leg, a basis gauge is contraction-compatible only when the matrices at its two ends are dual: if one end receives \(G\), the other receives \(G^{-\mathsf T}\) (equivalently the inverse under the chosen covariant convention). Then the two factors cancel inside the contraction. Applying such gauges to all internal \(y\) and carry edges leaves only independent gauges on the exposed legs, already covered by (17). Therefore contraction-compatible shared-edge gauges cannot remove the rank obstruction. Non-dual insertions change the contracted tensor rather than change its gauge and are outside this assertion.

## 6. Scope

The conclusion concerns only the horizontally fused strips above, with the inherited per-cell cyclic order (7) and the explicitly constructed complementary arcs (8). It makes no claim about two-dimensional blocks, alternate rotations or encodings, projections of legs, global Pfaffian identities, modular methods without a separate proof, contractions through non-matchgate resources, or integer factoring.

RECONSTRUCTED
