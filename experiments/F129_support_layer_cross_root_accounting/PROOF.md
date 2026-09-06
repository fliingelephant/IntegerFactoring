# Proof of the F129 support-layer accounting candidate

## 1. Intrinsic layer definition

The declared menu is fixed before exact-value deletion. Two declared words
can give the same residue. Two different endpoint pairs can also give the
same exact integer value. In addition, replacing a residue by its canonical
inverse leaves its exact value unchanged.

For this reason, assigning a layer to the first retained record would depend
on enumeration order. The definition

\[
\sigma(P)=
\min\{|\operatorname{supp}(e)|:c(e)\in\mathcal O(P)\}
\]

instead takes the minimum over every declared presentation of every endpoint
residue attached to \(P\) before exact-value deletion. It is therefore a
function of the declared finite menu and the exact value only. The sets
\(\mathcal L_s\) are disjoint and their union is the retained exact-value
set.

All later matrices are formed only after this partition is fixed.

## 2. Proof of Theorem 1

Fix \(s\geq2\). A vector in \(\widehat K_s\) has a unique coordinate split
\((x,y)\), where \(x\) uses the columns of \(U_{s-1}\) and \(y\) uses the
columns of \(A_s\). It satisfies

\[
U_{s-1}x+A_sy=0.
\]

Over \(\mathbb F_2\), this is equivalent to

\[
U_{s-1}x=A_sy.
\]

Define

\[
\Phi_s:\widehat K_s
\longrightarrow
\operatorname{im}U_{s-1}\cap\operatorname{im}A_s,
\qquad
\Phi_s(x,y)=U_{s-1}x=A_sy.
\]

The map is surjective. If \(z\) lies in the image intersection, choose
\(x,y\) with \(U_{s-1}x=z=A_sy\). Then \((x,y)\in\widehat K_s\) and maps
to \(z\).

Its kernel consists exactly of pairs with

\[
U_{s-1}x=0
\quad\text{and}\quad
A_sy=0.
\]

Therefore

\[
\ker\Phi_s=\widehat K_{s-1}\oplus K_s.
\]

The first isomorphism theorem gives

\[
C_s
=
\widehat K_s/(\widehat K_{s-1}\oplus K_s)
\simeq
\operatorname{im}U_{s-1}\cap\operatorname{im}A_s.
\]

Taking dimensions gives the recurrence

\[
\dim\widehat K_s
=
\dim\widehat K_{s-1}
+\dim K_s
+\dim C_s.
\]

Since \(\widehat K_1=K_1\), induction on \(s\) gives

\[
\dim\widehat K_d
=
\sum_{s=1}^{d}\dim K_s
+
\sum_{s=2}^{d}\dim C_s.
\]

The proof requires one aligned row space. If each layer used an unrelated
gcd-free basis, the displayed image intersection would not be defined.
Using rational-prime parity rows gives a canonical common space. P106 shows
that the factor-free public refinement computes the same distinct nonzero
parity rows for the fixed finite batch.

## 3. Proof of Theorem 2

For a kernel vector \(z\), the selected exact values have a square integer
product. Let \(R(z)\) be its positive integer square root. Each selected
value is \(1\bmod N\), so

\[
R(z)^2\equiv1\pmod N.
\]

If two kernel vectors \(x,y\) are added, their positive integer roots satisfy
the exact identity

\[
R(x+y)=
{R(x)R(y)\over\prod_{j:x_j=y_j=1}P_j}.
\]

Every denominator factor is part of the exact integer product and is
\(1\bmod N\). Hence

\[
R(x+y)\equiv R(x)R(y)\pmod N.
\]

The positive square root has no sign ambiguity. The quotient by the two
global roots discards globally useless outputs. Consequently,

\[
\rho(z)=R(z)\bmod N\pmod{\{+1,-1\}}
\]

is the P66 homomorphism from the binary kernel to \(T_N\).

The coordinate embeddings by zeros preserve the selected exact product.
Thus the restrictions of \(\rho_{\leq s}\) to the old and pure-new kernel
subspaces are exactly \(\rho_{\leq s-1}\) and \(\rho_s\). In particular,

\[
H_{\leq s-1}+H_s\subseteq H_{\leq s}.
\]

For a class represented by \(z\in\widehat K_s\), define

\[
\bar\rho_s([z])
=
\rho_{\leq s}(z)
+(H_{\leq s-1}+H_s).
\]

If \(z'\) is another representative, then

\[
z-z'\in\widehat K_{s-1}\oplus K_s.
\]

The homomorphism property gives

\[
\rho_{\leq s}(z)-\rho_{\leq s}(z')
\in H_{\leq s-1}+H_s.
\]

The displayed definition is therefore independent of the representative and
gives a homomorphism

\[
\bar\rho_s:C_s\to T_N/(H_{\leq s-1}+H_s).
\]

Every element of \(H_{\leq s}\) is the image of some
\(z\in\widehat K_s\). Hence the image of the relative map is precisely

\[
H_{\leq s}/(H_{\leq s-1}+H_s).
\]

This also proves why a direct map \(C_s\to T_N\) is not canonical in
general. Replacing a representative by an old or pure-layer dependency can
change its root by any element of \(H_{\leq s-1}+H_s\). If both subgroups
are zero, the ambiguity disappears and the direct map to \(T_N\) is valid.

Now suppose \(H_{\leq d}\neq0\), and choose the least \(s\) with
\(H_{\leq s}\neq0\). If \(H_s\neq0\), layer \(s\) has a useful pure
normalized-root direction. If \(H_s=0\), minimality gives
\(H_{\leq s-1}=0\), and

\[
\operatorname{im}\bar\rho_s
=H_{\leq s}\neq0.
\]

Conversely, a nonzero pure image embeds into the cumulative image, and a
nonzero relative cross image is a nonzero quotient of the cumulative image.
This proves the stated localization equivalence.

It proves only a fact about the complete normalized-root decoder for the
declared relation list. It gives no source-success law and no full factoring
algorithm.

## 4. Proof of Theorem 3

Let \(R_{\rm old}\) be the rows that occur in \(U_{s-1}\), and let
\(R_{\rm new}\) be the rows that occur in \(A_s\). Put

\[
S_s=R_{\rm old}\cap R_{\rm new}.
\]

Every vector in \(\operatorname{im}U_{s-1}\) is zero outside
\(R_{\rm old}\). Every vector in \(\operatorname{im}A_s\) is zero outside
\(R_{\rm new}\). Therefore every vector in their intersection is supported
inside \(S_s\). Projection to the coordinates in \(S_s\) is injective on
that intersection, so

\[
\dim C_s
=
\dim(\operatorname{im}U_{s-1}\cap\operatorname{im}A_s)
\leq |S_s|.
\]

For the private-row statement, let \(r_j\) be a row that occurs in new
column \(j\) and in no old or other new column. Suppose

\(A_sy\in\operatorname{im}U_{s-1}\). The old image is zero in row
\(r_j\), while row \(r_j\) of \(A_sy\) equals \(y_j\). Thus \(y_j=0\)
for every new column. Hence \(y=0\), the image intersection is zero, and
\(C_s=0\).

Finally, let

\[
P=1+\kappa N,
\qquad
P'=1+\kappa'N,
\]

and suppose a rational prime \(r\) occurs as a shared parity row. Then
\(r\mid P\) and \(r\mid P'\). Since each value is \(1\bmod N\), one has
\(r\nmid N\). Reducing both equations modulo \(r\) gives

\[
\kappa\equiv-N^{-1}\pmod r,
\qquad
\kappa'\equiv-N^{-1}\pmod r.
\]

Thus \(\kappa\equiv\kappa'\pmod r\). A nonzero cross quotient has a
nonzero vector in the image intersection. Such a vector has at least one
shared row, so some old and new columns satisfy this carry collision.

The converse does not follow. The congruence must first correspond to actual
odd valuations in both columns. Even a shared parity row does not imply that
the two column images have a nonzero intersection. A nonzero intersection
still does not imply a nonzero relative normalized-root image.

## 5. Proof of Proposition 4

Dirichlet's theorem supplies arbitrarily many pairwise-distinct primes in the
reduced class \(1\bmod N\). Choose

\[
a_1,\ldots,a_m,b_1,\ldots,b_m
\]

from this class.

Use one rational-prime row for every \(a_i\) and \(b_i\). In layer one, the
columns of \(a_i\) and \(b_i\) are the corresponding standard basis vectors.
Thus \(K_1=0\). In layer two, the column of \(a_ib_i\) is

\[
e_{a_i}+e_{b_i}.
\]

These columns are independent for different \(i\), so \(K_2=0\). Their
span is contained in the layer-one image. Therefore

\[
\operatorname{im}A_1\cap\operatorname{im}A_2
=
\operatorname{im}A_2
\]

and has dimension \(m\). Theorem 1 gives \(\dim C_2=m\).

For each \(i\), selecting the three values gives

\[
a_i\,b_i\,(a_ib_i)=(a_ib_i)^2.
\]

These \(m\) triples form a basis of the cumulative kernel. The positive root
of every basis dependency is \(a_ib_i\), which is \(1\bmod N\). The root of
any kernel combination is a product of such roots and is also
\(1\bmod N\). Hence

\[
H_{\leq2}=0.
\]

This is a genuine exact-congruence and parity construction with an arbitrarily
large cross quotient. It is not a canonical-inverse construction. Since a
prime congruent to \(1\bmod N\) is at least \(N+1\), the support-one values
\(a_i,b_i\) are primes greater than \(N\). They cannot equal
\(c\iota_N(c)\) with two nontrivial endpoints below \(N\). Also,

\[
a_ib_i\geq(N+1)^2>N^2,
\]

while

\[
c\iota_N(c)\leq(N-1)^2<N^2.
\]

Both canonical constraints fail independently.

## 6. Exact P111 corollary and its boundary

P111 constructs selected canonical values indexed by declared words
\(c=a^2b\), with \(a\neq b\) drawn from a set of small rational primes.
There are \(\Theta(n/\log n)\) selected values. For every selected column,
P111 constructs a rational-prime row \(q_c\) of odd valuation in that column
and zero valuation in all other selected columns. The selected matrix
therefore contains an identity submatrix and has full column rank.

Any submatrix obtained by partitioning these selected columns also has full
column rank. If two parts had a nonzero image intersection, the corresponding
old/new column combination would give a nonzero kernel vector in their union,
contradicting the identity submatrix. Thus all cross quotients computed only
inside the selected subsource are zero.

This corollary uses only the selected columns. P111 explicitly permits an
omitted seed, frozen, or other word column to reuse \(q_c\). It also does not
exclude a different earlier residue with the same exact value and a different
direct-sign outcome. The words have declared support two, but P111 does not
prove that no different declared presentation gives the same exact value at
smaller intrinsic support. Therefore the corollary is not a statement about
the complete intrinsic F26-Q support layers.

## 7. Final boundary

Theorems 1 and 2 make permanent retention exact: a relation that is
nonclosing in one layer remains available for every later image intersection.
They also show that relation count, kernel dimension, and normalized-root
image are different invariants.

Theorem 3 and Proposition 4 give the two independent missing conditions.
Canonical carry arithmetic must first prevent enough stable private rows to
create a pure or cross dependency. It must then break global-root
synchronization. Neither quasipolynomial source size nor polylogarithmic word
support proves either condition by itself.
