# F276 V2 statement — corrected determinant-one endpoint laws and affine transfer boundary

## Status and scope

This is an additive corrected proof-only candidate. It contains no
computation, search result, or factoring algorithm. The frozen V1 packet is
preserved unchanged. V1 correctly reduced the easy affine branch to constant
powering and geometric sums, but one search-disposition sentence then called
that branch a `SIGNAL` failure. No such universal signal failure was proved.
V2 replaces it with the exact statement that this packet supplies no signal
law for that branch; a separately justified constant-power candidate remains
open.

The packet studies five named mechanisms for an ordered matrix interval
product:

1. a rational formula in the two interval endpoints;
2. a rational endpoint gauge with a separate finite-dimensional length law;
3. a polynomial unimodular direct-summand line carrying a scalar multiplier;
4. a factor signal shared by every coordinate of a unimodular state; and
5. an affine polynomial transition in `SL_2`.

The first four mechanisms have exact boundaries. The fifth has an exact
normal form. Its generic branch remains a variable-coefficient continuant and
has no numerical-quasipolynomial endpoint evaluator in this packet.

The results do not give a lower bound for arbitrary determinant-one systems,
higher-degree or higher-dimensional transitions, nonlinear or
characteristic-dependent states, digit recurrences, implicit large states, or
general arithmetic circuits.

## 1. Ordered interval products

Let `K` be a characteristic-zero field. For

\[
 A(X)\in \operatorname{GL}_d(K(X)),
\]

define the ordered product

\[
 \Pi_A(a,m)
 =A(a+m-1)\cdots A(a+1)A(a),
 \qquad \Pi_A(a,0)=I.
\tag{1}
\]

The rightmost factor acts first. If `x=a` and `y=a+m`, write the same product
as `P(x,y)`. Adjacent intervals obey

\[
 P(y,z)P(x,y)=P(x,z).
\tag{2}
\]

An identity over `K(X)` is not automatically a modular algorithm. Every
denominator used at a numerical endpoint must be a unit modulo the composite
modulus.

## Theorem A — a rational endpoint cocycle is a gauge

Suppose

\[
 P(X,Y)\in\operatorname{GL}_d(K(X,Y))
\]

satisfies the rational identities

\[
 P(Y,Z)P(X,Y)=P(X,Z),
 \qquad P(X,X)=I.
\tag{3}
\]

Then there is a rational matrix

\[
 G(T)\in\operatorname{GL}_d(K(T))
\]

such that

\[
 \boxed{P(X,Y)=G(Y)G(X)^{-1}.}
\tag{4}
\]

Conversely, every expression in (4) satisfies (3).

Thus a matrix product that is rational in only its two endpoints is an
endpoint telescope. Noncommutativity does not create another rational
two-endpoint addition law.

This theorem does not say that constructing or evaluating `G` is cheap. It
also does not cover formulas with a nonrational length state, floors, binary
digits, Frobenius maps, or other semilinear data.

## Theorem B — a separable length law is a constant-matrix alias

Suppose an interval law has the form

\[
 P(x,y)=G(y)H_{y-x}G(x)^{-1},
\tag{5}
\]

where `G` is rational, `H_0=I`, and the length states satisfy

\[
 H_{r+s}=H_sH_r
 \qquad(r,s\geq0).
\tag{6}
\]

Then, with `C=H_1`,

\[
 \boxed{H_m=C^m}
\tag{7}
\]

and the one-step transition is

\[
 \boxed{A(X)=G(X+1)CG(X)^{-1}.}
\tag{8}
\]

Consequently,

\[
 \boxed{\Pi_A(a,m)=G(a+m)C^mG(a)^{-1}.}
\tag{9}
\]

If `A(X)` has determinant one, then necessarily

\[
 \boxed{\det C=1,\qquad \det G(X)\in K^*.}
\tag{10}
\]

Equation (9) is a rational gauge followed by ordinary constant-matrix
powering. A signal in `C^m` is a constant-power problem, not a compressed
evaluation of the varying interval leaves.

The conclusion is exact only for the separable law (5)-(6). A semilinear
state whose composition depends on scale, digits, or characteristic is
outside it.

## 2. Two smallest apparent positive controls

### Rational factorial lift

The dimension-two rational transition

\[
 A(X)=
 \begin{pmatrix}X&0\\0&X^{-1}\end{pmatrix}
 \in\operatorname{SL}_2(\mathbb Q(X))
\tag{11}
\]

has

\[
 \Pi_A(1,B)=
 \begin{pmatrix}B!&0\\0&(B!)^{-1}\end{pmatrix}.
\tag{12}
\]

On a balanced semiprime `N=pq` with

\[
 p<q<2p,
 \qquad B=\lfloor\sqrt N\rfloor,
\tag{13}
\]

the first diagonal entry has gcd `p` with `N`. But the step `X=p` requires
the inverse of `p`, and the endpoint formula requires the inverse of `B!`.
The denominator audit therefore returns the factor before the matrix product
is defined, or declares the proposed modular evaluation invalid.

Dimension one has no such determinant-one example because
`SL_1` is trivial. Thus (11) is the smallest rational algebraic signal, but
it is only the factorial gate paired with its forbidden reciprocal.

### Constant Jordan/binomial alias

Let

\[
 H=\left\lfloor B/2\right\rfloor
\]

and let `J` be the nilpotent Jordan shift of dimension `H+1`. For

\[
 C=I+J
\]

one has

\[
 C^B=\sum_{j=0}^{H}\binom BjJ^j,
\qquad
 (C^B)_{1,H+1}=\binom BH.
\tag{14}
\]

Writing `B=p+s`, the balanced inequalities give `0<=s<H<p<q`. Lucas's
theorem and `B<q` give

\[
 \boxed{\gcd\!\left(\binom BH,N\right)=p.}
\tag{15}
\]

This is a genuine constant-matrix entry signal, but its explicit state has
dimension `H+1=2^{Theta(log N)}`. An implicit request for only the displayed
entry is exactly the central-binomial evaluator gate. Constant powering has
not made that scalar evaluator numerical quasipolynomial.

## Theorem C — a unimodular direct-summand line has only a unit multiplier

Let `R=K[X]` or `R=Z[X]`. Suppose

\[
 A(X)\in\operatorname{SL}_d(R),
 \qquad U(X)\in\operatorname{GL}_d(R),
\]

and the first vector of the unimodular moving frame satisfies

\[
 A(X)U(X)e_1
 =\lambda(X)U(X+1)e_1.
\tag{16}
\]

Then

\[
 \boxed{\lambda(X)\in R^*.}
\tag{17}
\]

In particular, over `Z[X]`, `lambda=+1` or `-1`.

Therefore a polynomial determinant-one system cannot carry `X+c`, or any
other nonunit product multiplier, on a polynomial unimodular direct-summand
line. Such a multiplier requires a nonunimodular frame, a rational
complement, or another mechanism outside (16). The frame determinant or
rational complement must then be included in the denominator and
construction-cost audit.

This theorem does not rule out a factor in one coordinate of a moving state
that is not a unimodular invariant line.

## Theorem D — coordinate ideals are preserved by unimodular transport

For a commutative ring `R`, a vector `v in R^d`, and
`M in GL_d(R)`, let `I(v)` be the ideal generated by the coordinates of
`v`. Then

\[
 \boxed{I(Mv)=I(v).}
\tag{18}
\]

Hence every product of integer determinant-one matrices preserves the gcd of
all coordinates of an integer state. Every row and every column of an
integer unimodular matrix is primitive.

This kills a whole-state or whole-column common-factor claim. It does not
kill a factor in one selected entry: another coordinate can retain the
missing local unit, as determinant one requires.

The identities

\[
 \det \Pi_A=1,
 \qquad
 \Pi_A\operatorname{adj}(\Pi_A)=I,
\tag{19}
\]

and the Cayley-Hamilton identity are likewise global identities. A residue
that is identically zero for every determinant-one matrix gives gcd `N`, not
a factor.

## Theorem E — exact affine `SL_2` normal form

Let

\[
 A(X)=C+XD\in\operatorname{SL}_2(\mathbb Z[X]).
\tag{20}
\]

Put `B_0=C^{-1}D`. Then

\[
 \boxed{
 C\in\operatorname{SL}_2(\mathbb Z),
 \quad \operatorname{tr}B_0=0,
 \quad \det B_0=0,
 \quad B_0^2=0,
 \quad A(X)=C(I+XB_0).
 }
\tag{21}
\]

If `D` is nonzero, a constant rational change of basis puts `B_0=E_{12}`.
Write the conjugated constant matrix as

\[
 \widetilde C=
 \begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad ad-bc=1.
\tag{22}
\]

For every state

\[
 z_{k+1}=\widetilde C(I+kE_{12})z_k,
 \qquad z_k=(x_k,y_k)^T,
\tag{23}
\]

the second coordinate obeys

\[
 \boxed{
 y_{k+2}=(ck+a+c+d)y_{k+1}-y_k.
 }
\tag{24}
\]

If `c=0`, the nilpotent line is preserved by `C`; the recurrence has
constant coefficients and the product reduces to constant powers and
geometric-weighted polynomial sums. If `c!=0`, (24) is a genuine
affine-coefficient continuant. F276 supplies neither a universal hidden
`p/q` divisibility law nor a numerical-quasipolynomial evaluator for that
generic branch.

Equation (21) classifies only one affine matrix per step in dimension two.
It does not classify higher polynomial degree, products of multiple affine
shears inside one step, or higher dimension.

## 3. Holonomic certificate versus endpoint cost

For a fixed rational `d`-dimensional first-order system, each scalar
coordinate satisfies some rational-coefficient linear recurrence of order at
most `d`. This follows from linear dependence among `d+1` shifted row
covectors.

That holonomic certificate is not an endpoint evaluator. Literal recurrence
evaluation or a generic product tree still touches `m` transition leaves.
F276 proves no lower bound against a special fast algorithm, but it does not
count the words "fixed order", "holonomic", or "binary splitting" as a
numerical-quasipolynomial construction.

Every future candidate in this lane must separately pass all five labels:

| Label | Required evidence |
|---|---|
| `LOCAL` | Every transition coefficient is constructible in numerical QP time. |
| `STATE` | The explicit or implicit state representation has numerical QP size and operations. |
| `ENDPOINT` | The target entry at remote length has an independent numerical QP evaluator. |
| `UNIT` | Every modular denominator is proved a unit, or its gcd is handled as a factor certificate. |
| `SIGNAL` | An exact asymmetric local law holds for the intended `p<=B<q`, not only on samples. |

The two positive controls fail `UNIT` or `STATE/ENDPOINT`. This packet
supplies no `SIGNAL` theorem for the easy affine branch. The generic affine
branch has no `ENDPOINT` or `SIGNAL` theorem.

## 4. Search decision and exact exclusions

No C++ interval-product search is justified solely by a rational
two-endpoint law, a separable length law, a unimodular direct-summand
multiplier, a whole-state coordinate gcd, or the reduction of the affine
`c=0` branch. These classifications yield a gauge telescope, a
constant-power alias, a unit multiplier, a global decoy, or a fixed-order
sum. A constant-power candidate with its own exact all-input signal law is a
separate lane and is not ruled out here.

The generic affine recurrence (24) remains mathematically open, but a scan of
small coefficients and small primes would test only finite divisibility of a
sequential holonomic recurrence. Without an independently specified QP
endpoint operation, it does not yet meet the entry condition for a
resource-bearing search.

F276 proves no:

1. lower bound for arbitrary `SL_d` polynomial or rational cocycles;
2. lower bound for nonlinear, semilinear, digit, Frobenius, or adaptive
   algorithms;
3. impossibility theorem for an implicit large Jordan state;
4. impossibility theorem for the generic affine continuant (24);
5. classification of higher-degree, higher-dimensional, or multiple-shear
   transitions;
6. numerical-quasipolynomial interval-product evaluator;
7. all-input factoring algorithm; or
8. computational or empirical result.
