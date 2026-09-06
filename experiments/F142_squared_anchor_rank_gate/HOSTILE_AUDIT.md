# F142 hostile audit — PASS AS CLAIMED

## Frozen inputs

I audited the frozen proof-only candidate with hashes

- `STATEMENT.md`:
  `0049f74a635b7da7f288460ddbaf8e6669eb329073e8164b0834e74d3e4c1a1e`;
- `PROOF.md`:
  `4f257c6425f81926459b6acba3d401af2024c5d9394889150bcb9fa148f7dc4e`.

No computation was needed.  I did not edit either frozen file.

## Result

**PASS AS CLAIMED.**

F142 is an exact conditional decoder boundary.  It does not prove that the
F141 source closes, that an endpoint cycle occurs, or that any resulting root
is non-global.  I found no counterexample to the rank formulas, bridge
replacement, root formulas, forest obstruction, or cycle formulas within
that scope.

## 1. Square-class and rank checks

For

\[
A_\ell=c_\ell w_\ell,
\qquad
B_\ell=q\ell^2w_\ell,
\]

the exact square classes are

\[
[A_\ell]=[c_\ell]+[w_\ell],
\qquad
[B_\ell]=[q]+[w_\ell].
\]

Thus $B=H+a\mathbf1^{\mathsf T}$.  The difference has rank at most one,
so the two ranks differ by at most one in both directions.  This proves the
absolute rank claim without assuming that $q$, $c_\ell$, or $w_\ell$
is a rational prime.

Since $q\ell^2w_\ell\equiv1\pmod N$, cancellation of the unit $q$
gives

\[
\ell^2w_\ell\equiv q^{-1}\pmod N.
\]

This is only a modular identity.  It gives no exact parity dependency.  The
statement keeps this distinction.

## 2. Bridge replacement and exact-value deletion

Exact multiplication gives

\[
A_\ell B_\ell
=q\ell^2c_\ell w_\ell^2
=D_\ell w_\ell^2,
\qquad
D_\ell=q\ell^2c_\ell.
\]

Hence the bridge column is exactly

\[
[D_\ell]=[A_\ell]+[B_\ell]=[q]+[c_\ell].
\]

Also $D_\ell\equiv c_\ell^2\pmod N$, so its supplied modular root is
$c_\ell$.  The exact root changes by $w_\ell$, while the supplied root
changes by $c_\ell$.  Since $w_\ell\equiv c_\ell^{-1}\pmod N$, the P66
normalized root is unchanged.  The bridge operation is therefore an
invertible binary column change when the matched canonical column is
present.

I checked the global first-exact-value rule against P100 and P106.  An equal
earlier canonical or lifted relation value is still congruent to one and has
supplied root one.  Restoring logical duplicate copies before the bridge
change adds only duplicate directions with global normalized root $+1$.
It does not change the normalized-root image.  Equivalently, one can apply
the theorem chronologically whenever a retained lift is added after its
matched canonical value.  F142 does **not** authorize deletion of duplicate
bridge values with different supplied roots.

The exceptional canonical value $A_\ell=1$ is a zero square-class column.
It can be adjoined formally with supplied root one without changing rank or
root image.  This does not invalidate the conditional bridge statement.

## 3. Relative-rank and owner-contraction checks

Relative to $C=\operatorname{colspan}(M_0)$, the sum of selected bridge
columns is

\[
\Gamma x+(\mathbf1^{\mathsf T}x)a.
\]

It extends to an old/new dependency exactly when this vector lies in $C$.
This proves (7) and its quotient form (8).  If $a\in C$, its quotient is
zero and the gate reduces to $\overline\Gamma x=0$.  The quotient bridge
matrix differs from the quotient residue matrix by one rank-one matrix, so
their ranks differ by at most one.

For (10), each declared pivot row is private among the old columns, is owned
by its stated owner column, and occurs in every bridge column under
consideration.  Its row equation forces the owner coefficient to equal

\[
t(x)=\mathbf1^{\mathsf T}x.
\]

Deleting those rows leaves

\[
\sum_\ell x_\ell\widehat D_\ell
+t(x)\sum_i\widehat v_i
\in\operatorname{colspan}(\widehat W),
\]

which is exactly (10).  If a residue class cancels one of the $q$-pivots,
this uniform-pivot derivation no longer applies.  F142 correctly returns to
the general gate (7) in that case.

The warning about gcds is also correct.  From
$\gcd(q,w_\ell)=1$ one cannot infer $\gcd(q,c_\ell)=1$.  The bridge must
use the actual vector $[q]+[c_\ell]$, including any exact cancellation.

## 4. Root checks

For a standalone lifted dependency, the parity equation makes

\[
Q=P_0(y)q^{|S|}\prod_{\ell\in S}w_\ell
\]

an exact square.  All old and lifted relation values are congruent to one.
Therefore

\[
Q\equiv
q^{|S|}\prod_{\ell\in S}q^{-1}\ell^{-2}
=\left(\prod_{\ell\in S}\ell\right)^{-2}
\pmod N.
\]

Multiplying the positive square root of $Q$ by
$\prod_{\ell\in S}\ell$ gives the exact root of the original selected
product and a square root of one modulo $N$.  This verifies (13).  It does
not show that the root is non-global.

For bridge columns, P66 uses supplied root $c_\ell$.  Thus

\[
\sqrt{P_0(y)\prod_{\ell\in S}D_\ell}
\left(\prod_{\ell\in S}c_\ell\right)^{-1}
\pmod N
\]

is exactly the normalized root.  The bridge calculation above proves that
this is the same root label as for the corresponding canonical-plus-lifted
selection.

## 5. Forest and cycle checks

When every endpoint class is one atomic row, a bridge column is the binary
incidence vector $e_u+e_v$.  A selected set sums to zero exactly when every
vertex has even selected degree.  This is the graph cycle space.  A forest
has a leaf in every nonempty edge subgraph, so its columns are independent.

The pre-contraction columns

\[
A_i=\gamma_i+h_i,
\qquad
B_i=a+h_i
\]

are the incidence columns of a subdivided star when the displayed rows are
independent.  Inspecting the private $\gamma_i$-row first forces the
$A_i$ coefficient to zero.  The private $h_i$-row then forces the
$B_i$ coefficient to zero.  The matrix has full column rank.  This is an
abstract parity obstruction.  F142 does not claim an all-input arithmetic
realization of it.

For an exact endpoint cycle

\[
c_i=[q_i\ell_i^2]_N=q_{i+1},
\qquad q_{k+1}=q_1,
\]

the bridge product is

\[
\prod_iq_i\ell_i^2q_{i+1}
=\left(\prod_iq_i\ell_i\right)^2.
\]

Its supplied root is $\prod_i c_i=\prod_iq_i$.  The normalized root is
therefore $\prod_i\ell_i\pmod N$.  Multiplication of the endpoint
congruences and cancellation of the unit $\prod_iq_i$ proves that this is
a square root of one.  It yields a proper gcd exactly when it is not global
$+1$ or $-1$.

For square-class matching, the representations

\[
c_i=d_ir_i^2,
\qquad q_{i+1}=d_is_i^2
\]

give exact root

\[
\left(\prod_i\ell_i\right)\prod_i d_ir_is_i
\]

and supplied root $\prod_i d_ir_i^2$.  Their quotient is exactly

\[
\prod_i\ell_i s_ir_i^{-1}\pmod N.
\]

Every $r_i$ is a unit because $c_i$ is a unit.  Formula (21) is valid.

## 6. Scope against the closest records

- P66 supplies the factor-free exact-square decoder and normalized-root
  map.  F142 changes no decoder rule.
- P100 says a new presentation helps only through multiplicity or column
  closure.  F142 identifies the exact new bridge columns and their closure
  condition; it does not bypass P100.
- P106 says complete refinement preserves the hidden prime-parity kernel.
  The bridge vectors are exact rational square classes, so later gcd-free
  refinement does not change the gate.
- P119 resolves most weight-two root labels only after closure.  F142 does
  not claim closure and does not claim that a cycle root is automatically
  useful.
- P127 shows that many shared old rows can coexist with full rank.  The
  subdivided-star forest is the exact squared-anchor specialization of this
  boundary.
- X73--X78 reject row count, row width, pivot cancellation, and packed
  multiplicity as rank certificates.  F142 respects those failures.  Its
  positive cycle statement assumes the missing cycle instead of claiming
  that F141 forces one.

## Exact surviving conclusion

F141's squared-anchor lifts remove inverse-cofactor rows only after they are
compared with their matched canonical columns.  The remaining incremental
column is exactly

\[
[q]+[c_\ell].
\]

This can still be a full-rank forest.  A cycle gives an exact dependency, and
its normalized root is given by (19), or by (21) for square-class matching.
The unsolved source theorem is to force such a cycle or hypercycle in the
quasipolynomial transcript and then force its root to be non-global.
