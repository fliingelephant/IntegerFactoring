# F142 proof — bridge quotient, forest obstruction, and cycle root

## 1. Column identities

For one squared-anchor position,

\[
A_\ell=c_\ell w_\ell,\qquad
B_\ell=q\ell^2w_\ell.
\]

Taking exact square classes and using \([\ell^2]=0\) gives

\[
[A_\ell]=[c_\ell]+[w_\ell],
\qquad
[B_\ell]=[q]+[w_\ell].
\tag{1}
\]

This proves (2) and the matrix identity \(B=H+a\mathbf1^{\mathsf T}\).
The difference of these two matrices has rank at most one, so their ranks
differ by at most one.

Also

\[
q\ell^2w_\ell\equiv1\pmod N
\]

implies (5).  This is only a modular statement.  Exact squareness is
equivalent to a binary relation among the integer prime-parity columns and
does not follow from equal modular residues.

Multiplying the exact canonical and lifted values gives

\[
A_\ell B_\ell
=q\ell^2c_\ell w_\ell^2
=D_\ell w_\ell^2.
\tag{2}
\]

Thus replacing \(B_\ell\) by \(D_\ell=A_\ell+B_\ell\) in square-class
coordinates is an invertible binary column operation when \(A_\ell\) is
retained.  Since \(D_\ell=q\ell^2c_\ell\), its square class is
\([q]+[c_\ell]\), and \(D_\ell\equiv c_\ell^2\pmod N\).  Its supplied modular
root is \(c_\ell\).

If canonical exact-value deletion kept an equal earlier integer instead of
the displayed \(A_\ell\), that retained column has the same square class and
the same supplied root one.  The column operation remains valid.

## 2. Relative rank and old owners

Let \(C=\operatorname{colspan}(M_0)\).  For a new coefficient vector \(x\),
the bridge sum is

\[
\sum_\ell x_\ell(a+\gamma_\ell)
=\Gamma x+t(x)a.
\tag{3}
\]

It extends to an old/new dependency if and only if (3) belongs to \(C\).
This proves (7).  Passing to \(V/C\) proves (8).  If \(a\in C\), its quotient
is zero and (9) follows.

The quotient bridge matrix and the quotient residue matrix differ by the
rank-one matrix \(\overline a\mathbf1^{\mathsf T}\).  Their ranks therefore
differ by at most one.

For the owner form, assume the selected bridge subfamily contains every
declared private pivot of \(a\).  If \(t(x)=1\), the pivot equations force
every owner \(v_i\) to be selected; if \(t(x)=0\), none is selected.  After
deleting the pivot rows, the remaining equation is

\[
\sum_\ell x_\ell\widehat D_\ell
+t(x)\sum_i\widehat v_i
\in\operatorname{colspan}(\widehat W).
\]

Distributing the second term through
\(t(x)=\sum_\ell x_\ell\) gives (10).

This owner formula is conditional.  Although a good F141 lift has
\(\gcd(q,w_\ell)=1\), the canonical residue \(c_\ell\) can share a factor
with \(q\).  Then \(\gamma_\ell\) can cancel a pivot of \(a\) in
\(D_\ell=a+\gamma_\ell\).  Equation (7) remains exact for this nonuniform
pivot pattern.

## 3. Root formulas

Suppose (11) holds.  Exact parity cancellation says that

\[
Q=P_0(y)q^{|S|}\prod_{\ell\in S}w_\ell
\]

is a square, because the omitted factor
\(\prod_{\ell\in S}\ell^2\) is already a square.  Multiplying its positive
root by \(\prod_{\ell\in S}\ell\) gives (13).

Modulo \(N\),

\[
Q
\equiv
q^{|S|}\prod_{\ell\in S}q^{-1}\ell^{-2}
=\left(\prod_{\ell\in S}\ell\right)^{-2}.
\]

Therefore the root in (13) squares to one modulo \(N\).  This proves the
standalone root reduction.

For bridge inputs, each old relation has supplied root one and each
\(D_\ell\) has supplied root \(c_\ell\).  The P66 normalized-root definition
therefore gives (14).

Equation (2) proves preservation under the column change.  The exact root of
\(A_\ell B_\ell\) is \(w_\ell\) times the exact root of \(D_\ell\), while
\(w_\ell\equiv c_\ell^{-1}\pmod N\).  Thus the normalized roots agree for
each replacement and hence for every selected combination.

## 4. Forest and cycle

Over \(\mathbf F_2\), the column \(e_u+e_v\) is the incidence column of an
unoriented edge.  A selected edge set sums to zero exactly when every vertex
has even selected degree.  This is the graph cycle space.  A nonempty forest
has a leaf, so no nonempty selected forest has all degrees even.  Its columns
are independent.

For the subdivided star (16), any zero combination first inspects the private
\(\gamma_i\)-row and gets the coefficient of \(A_i\) equal to zero.  It then
inspects the private \(h_i\)-row and gets the coefficient of \(B_i\) equal to
zero.  Thus all \(2m\) columns are independent even though every \(B_i\)
contains \(a\).

Now assume the exact endpoint cycle (17).  Since \(c_i=q_{i+1}\),

\[
\prod_iD_i
=\prod_iq_i\ell_i^2q_{i+1}
=\left(\prod_iq_i\ell_i\right)^2.
\]

The supplied root product is

\[
\prod_ic_i=\prod_iq_{i+1}=\prod_iq_i.
\]

Dividing the positive exact root by the supplied root proves (19).
Multiplication of the congruences
\(q_i\ell_i^2\equiv q_{i+1}\pmod N\), followed by cancellation of the unit
\(\prod_iq_i\), proves \((\prod_i\ell_i)^2\equiv1\pmod N\).

For square-class matching, write
\(c_i=d_ir_i^2\) and \(q_{i+1}=d_is_i^2\).  Then

\[
\sqrt{\prod_iD_i}
=
\left(\prod_i\ell_i\right)
\prod_i d_ir_is_i,
\]

while the supplied root product is
\(\prod_ic_i=\prod_id_ir_i^2\).  Their quotient is (21).  The same P66
definition covers a composite parity vector or hyperedge without requiring
an atomic endpoint.

## 5. Boundary

The only F141 conclusion used here is the declared source of canonical and
lifted squared-anchor positions.  No finite computation is used.  The proof
does not assert that the abstract forest occurs for an infinite input family,
only that F141's proved row-reuse facts do not exclude it.  It also does not
assert that an adaptive endpoint cycle exists.  It gives the exact rank and
root tests if either structure occurs.
