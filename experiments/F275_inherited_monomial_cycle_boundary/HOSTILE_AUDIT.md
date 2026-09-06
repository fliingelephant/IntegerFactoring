# F275 fresh hostile proof audit

## Verdict: FAIL

The central pullback theorem, the even-cycle identities, and the stated
F270 grammar boundary pass. The packet still contains one false unconditional
claim. Frozen bytes must not be promoted as written.

## Authentication and method

I first computed the SHA-256 of `FROZEN.sha256`. It was exactly

```text
6c3cebe4f34bdb439dabb9cc50990bb68d0250ae552ea5087dd4e57dc057aa9d
```

I then verified every file named by that authenticated manifest. All five
listed hashes passed. I read `STATEMENT.md` and `PROOF.md` only after those
checks. I used no remote work and no numerical search. I did not modify a
frozen file or a ledger.

## Blocking counterexample

The statement says that the row made by

\[
T_y(d)=[y^2d^{-1}]_N,\qquad A=dT_y(d)
\]

is below `N^2`. The hypotheses require only `d>0` and `gcd(d,N)=1`. They do
not require `d<N`.

Take

\[
N=3,\qquad d=10,\qquad y=1.
\]

These values satisfy every stated condition. Since `d=1 mod 3`,

\[
T_y(d)=[1^2\,10^{-1}]_3=1.
\]

Thus

\[
A=dT_y(d)=10>9=N^2,
\]

while `A=1=y^2 mod 3`. The root claim is valid, but the size claim is false.
The size claim becomes valid if this construction also requires the input
carrier to be canonical: `1<=d<N`.

This defect does not invalidate Theorem B. The proof of Theorem B uses only
positivity, unit status, the exact endpoint product, and the root congruence.
It does invalidate the packet-wide claim audit requested here.

## Claims that pass

### Exact inherited monomials

For a transformed relation, writing `z_i=2h_i+d_i` gives

\[
\prod_j A_j^{c_j}
=\left(Q\prod_i a_i^{h_i}\right)^2\prod_i a_i^{d_i}.
\]

The final product is an integer and a rational square, so it is an integer
square. Taking the positive root and dividing by the inherited modular root
gives exactly `epsilon*rho_a(d)`. Unit cancellation is valid: the old rows
are units, and unit status of `A_j` forces every selected `s_j` to be a unit.

Only the structural incidence kernel `M^T c=0` is forced to have a global
root. A relation with nonzero pullback can retain a useful old normalized
root. The statement and proof both preserve this distinction. They do not
claim that all transformed dependencies are global.

Zero exponents, repeated old values, repeated transformed values, and empty
supports do not break the proof. They remain formal row coordinates. The
positive-root convention removes an integer sign ambiguity.

For an arbitrary supplied row root, its ratio with the inherited root squares
to one modulo odd `N`. A non-global ratio yields a proper signed gcd. If no
proper gcd occurs, the ratio is exactly `+1` or `-1`. Thus compatibility is
screened and is not assumed.

### Even-cycle identities

On a simple even cycle, the even edges and the odd edges are the two perfect
matchings. Each matching product is exactly `R`. Hence

\[
R=P_0^2=P_1^2\pmod N,
\]

and division by the unit `P_0P_1` proves both alternating forms of `rho`.
Multiplying `P_0-P_1` or `P_0+P_1` by the unit `P_0` proves the two exact gcd
identities. A change of start vertex, parity convention, or cycle orientation
only swaps the two matching products or changes a difference by a sign. The
gcds and normalized root class are unchanged.

No endpoint or edge label can be zero modulo `N`: every carrier is a unit and
`y_e^2` is a unit. Equal integer carrier values at different vertices do not
affect the matching argument. The theorem correctly excludes odd cycles and
does not identify the structural graph-incidence kernel with the full
arithmetic square-class kernel.

### Reduced complement boundary and F270

The unreduced product `P_E(a)` is an exact monomial in its two operand rows,
with the inherited product root. Theorem A applies to relations made by that
operation. The canonical reduction satisfies only

\[
P_E(a)=C_E(a)+\lambda N^2.
\]

For nonzero `lambda`, this identity does not preserve the operand prime
incidence. Theorem A gives no general conclusion from this construction.
This is a grammar boundary. It does not exclude an accidental numerical
relation involving a reduced row.

The inspected F270-D03 grammar rebuilds the block system over the union of
the original canonical scalar rows `U_E(b)`. It does not generate
`C_E(a)` by reduced complement multiplication. Cross-family sharing can
create a nonstructural arithmetic dependency even when each separate bank
has private pivots. Such a dependency has nonzero old-row pullback and is not
forced global by Theorem A. F275 therefore does not close F270.

## Exact scope qualification

The failure is limited to the unconditional `A<N^2` sentence for the
inverse-square edge constructor. Subject to adding `1<=d<N` there, the audited
proof supports Theorem A, Theorem B, and the operation-level reduced-product
boundary. It supports no claim that every dependency is structural or global,
no classification of arithmetic carrier coincidences, and no success or
failure law for F270 or for reduced complement rows.
