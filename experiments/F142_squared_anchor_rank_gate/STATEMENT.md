# F142 candidate statement — exact rank and root gate for squared-anchor lifts

## Status and scope

This is a proof-only decoder boundary.  It assumes the frozen F141 lifted
source.  It does not change that source and does not prove an all-input
factoring algorithm.

P120 gives the one-pivot residual-span test.  P122 proves that a common row
does not close unrelated fresh rows.  P127 gives the multi-owner shifted
residual test.  F142 identifies the exact specialization for the F141
squared-anchor columns.  It also gives the exact cycle root.

## 1. Three equivalent columns

Fix a named unit block \(q\).  For an eligible prime anchor \(\ell\), put

\[
U_\ell=q\ell^2,\qquad
c_\ell=[U_\ell]_N,\qquad
w_\ell=\iota_N(c_\ell).
\]

The canonical and lifted relations are

\[
A_\ell=c_\ell w_\ell,\qquad
B_\ell=q\ell^2w_\ell.
\tag{1}
\]

Write \([z]\) for the exact rational square class of a positive integer
\(z\).  Put

\[
a=[q],\qquad \gamma_\ell=[c_\ell],\qquad h_\ell=[w_\ell].
\]

Then

\[
[A_\ell]=\gamma_\ell+h_\ell,\qquad
[B_\ell]=a+h_\ell.
\tag{2}
\]

The square multiplier \(\ell^2\) contributes no parity row.  The standalone
lifted layer is therefore a rank-one perturbation of the inverse-cofactor
matrix:

\[
B=H+a\mathbf 1^{\mathsf T}.
\tag{3}
\]

In particular,

\[
\boxed{|\operatorname{rank}B-\operatorname{rank}H|\le1.}
\tag{4}
\]

The congruence

\[
\ell^2w_\ell\equiv q^{-1}\pmod N
\tag{5}
\]

supplies a modular square root after an exact parity dependency exists.  It
does not make such a dependency exist.

If the canonical column \(A_\ell\) is already retained, adding \(B_\ell\) is
equivalent to adding the bridge

\[
D_\ell=U_\ell c_\ell=q\ell^2c_\ell,
\qquad
[D_\ell]=a+\gamma_\ell,
\qquad
c_\ell^2\equiv D_\ell\pmod N.
\tag{6}
\]

The inverse-cofactor class \(h_\ell\) cancels between the canonical and
lifted columns.  Thus the rank added by F141 over its matched canonical
ledger is controlled by the exact residue classes \(\gamma_\ell\), not by
the common \(q\)-row and not by the fresh \(w_\ell\)-rows.

F141's good-anchor condition \(\gcd(q,w_\ell)=1\) does not imply
\(\gcd(q,c_\ell)=1\).  Therefore a \(q\)-row that is present in
\(B_\ell\) can cancel in the bridge \(D_\ell\).  Relative rank must use
(7), not the absolute row multiplicity of the lifted columns.

## 2. Exact relative-rank gate

Let \(M_0\) be any retained old parity matrix that includes the matched
canonical columns, and put

\[
C=\operatorname{colspan}(M_0).
\]

For a fixed \(q\), let \(\Gamma\) have columns \(\gamma_\ell\).  A nonzero
new coefficient vector \(x\) participates in an old/new dependency exactly
when

\[
\boxed{
\Gamma x+t(x)a\in C,
\qquad
t(x)=\mathbf1^{\mathsf T}x.
}
\tag{7}
\]

Equivalently, in the quotient square-class space \(V/C\),

\[
\overline\Gamma x=t(x)\overline a.
\tag{8}
\]

If \(a\in C\), the common reused class disappears completely and the gate is
only

\[
\overline\Gamma x=0.
\tag{9}
\]

More generally, adding \(a\mathbf1^{\mathsf T}\) changes the quotient rank
of the residue columns by at most one.  Polynomial multiplicity of the
common \(q\)-rows cannot by itself give polynomial nullity.

Suppose private pivot rows of \(a\) are owned by old independent columns
\(v_1,\ldots,v_s\), and restrict to bridge columns that contain every one of
those pivots.  Delete the pivot rows and let \(W\) contain the other old
columns.  With hats denoting the residual columns, (7) becomes the P127
owner contraction:

\[
\boxed{
\sum_\ell x_\ell
\left(\widehat D_\ell+\sum_{i=1}^s\widehat v_i\right)
\in\operatorname{colspan}(\widehat W).
}
\tag{10}
\]

Thus old owner columns can cancel common bridge pivots.  They do not cancel
the residue-endpoint residuals automatically.  If some
\(\gamma_\ell\) cancels a \(q\)-pivot inside \(D_\ell\), the general
condition (7), with the actual pivot-incidence pattern, applies instead.

## 3. Exact root reduction

For the standalone lifted layer, allow an old relation selection \(y\).  A
pair \((y,x)\) is a parity dependency exactly when

\[
M_0y+t(x)a+Hx=0.
\tag{11}
\]

Let \(P_0(y)\) be the selected old exact product and let
\(S=\{\ell:x_\ell=1\}\).  Then

\[
Q=P_0(y)q^{|S|}\prod_{\ell\in S}w_\ell
\tag{12}
\]

is an exact square.  The positive root of the original selected lifted
product is

\[
\boxed{
R=\left(\prod_{\ell\in S}\ell\right)\sqrt Q.
}
\tag{13}
\]

Equation (5) proves \(R^2\equiv1\pmod N\).  It gives no reason for \(R\) to
be non-global.

For the bridge formulation, if an old selection \(y\) and bridge selection
\(x\) give an exact square, its normalized root is

\[
\boxed{
\rho(y,x)=
\sqrt{P_0(y)\prod_{\ell\in S}D_\ell}
\left(\prod_{\ell\in S}c_\ell\right)^{-1}
\pmod N.
}
\tag{14}
\]

This is also the normalized root of the corresponding canonical-plus-lifted
dependency under the invertible replacement \(D_\ell=A_\ell+B_\ell\).

## 4. Forest obstruction and cycle criterion

If each bridge endpoint contributes one atomic square-class row, the bridge
columns are the binary incidence columns

\[
e_{q_i}+e_{c_i}.
\tag{15}
\]

Their kernel is exactly the cycle space of the resulting graph.  A forest
has full column rank.  A fixed-\(q\) star whose residue endpoints each have a
fresh private row is therefore full rank, regardless of how many arms reuse
the \(q\)-row.

The same obstruction is visible before bridge contraction.  With independent
rows \(a,\gamma_i,h_i\), the canonical and lifted columns

\[
A_i=\gamma_i+h_i,\qquad B_i=a+h_i
\tag{16}
\]

form the incidence matrix of a subdivided star.  It is a tree and has full
column rank.  This is an exact abstract parity obstruction compatible with
all row-multiplicity conclusions of F141.  F141 supplies no theorem that
excludes fresh private residue rows.

Conversely, suppose an adaptive all-block transcript makes an exact simple
cycle

\[
c_i=[q_i\ell_i^2]_N=q_{i+1},
\qquad
q_{k+1}=q_1.
\tag{17}
\]

The bridge product is the exact square

\[
\prod_{i=1}^kD_i
=
\left(\prod_{i=1}^kq_i\ell_i\right)^2.
\tag{18}
\]

Its supplied modular root is \(\prod_i c_i=\prod_iq_i\).  Therefore its
normalized root is

\[
\boxed{\rho=\prod_{i=1}^k\ell_i\pmod N.}
\tag{19}
\]

Multiplying (17) shows \(\rho^2\equiv1\pmod N\).  The cycle factors \(N\)
exactly when this anchor product is not globally \(+1\) or \(-1\).

If only square classes match, write

\[
c_i=d_ir_i^2,\qquad q_{i+1}=d_is_i^2.
\tag{20}
\]

The cycle is still an exact parity dependency, but its root is

\[
\boxed{
\rho=
\prod_{i=1}^k\ell_i\,s_i r_i^{-1}
\pmod N.
}
\tag{21}
\]

For composite endpoint vectors, the graph becomes a binary hypergraph.  The
general gate is still (7): a selected set must have even incidence at every
row after old-span cancellation, and (14) is its exact root.

## Exact consequence

F141 advances source-side row reuse.  It does not yet advance the final rank
gate by the same amount.  After the canonical columns are included, its
incremental content is exactly the bridge incidence family

\[
[q]+[c_\ell].
\]

A successful continuation must force a cycle or hypercycle in this quotient
incidence system and must prove that the corresponding normalized root in
(14) is non-global.  A short exact endpoint cycle would reduce this root gate
to the public anchor product in (19).  No theorem currently forces such a
cycle.
