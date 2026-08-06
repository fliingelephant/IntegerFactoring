# F26 — holographic factor-witness contraction: a copy--AND parity obstruction

**Family:** F20.

**Status:** verifier-backed after a corrected hostile re-audit and independent
proof-blind reconstruction; no cross-family audit has run.

**Classification:** method failure for the natural separated Boolean
\(\operatorname{COPY}_3\)-plus-\(\operatorname{AND}_3\) factor graph in an
explicit bipartite ternary-fanout realization under a common holographic basis
for each copied input role.  The proof even permits independent common bases
for the two roles and an arbitrary invertible dual basis on the AND-output
wire.  This does not close combined multiplier cells, high-arity equality,
edge-dependent gauges, other gate sets, non-matchgate Pfaffian formulas, or
other exactly contractible factor-witness networks.

**Computation:** none.  Every statement is symbolic.

## Outcome

An exact polynomial contraction of pinned multiplication-witness networks
would be enough for complete classical factoring, and the factor decoder
would need no terminal factor-extracting gcd.  Exact witness counts can be
self-reduced bit by bit after subtracting the two known trivial witnesses
\(x=1,N\), yielding a verified
nontrivial divisor; deterministic primality testing and recursion finish.

The most direct Valiant-style construction nevertheless fails locally before
planarity or contraction cost is reached.  A ternary matchgate tensor over
\(\mathbb C\) must have one parity: all odd-weight entries vanish or all
even-weight entries vanish.  Every invertible basis that makes
\(\operatorname{COPY}_3\) parity-pure has a Hadamard-type normal form.  Under
the corresponding transpose-dual actions, the two output-wire slices of the
transformed AND tensor are coordinates of

\[
  W_{s,t}
  =
  u(1+xs+yt)+vxy\,st,
  \qquad s,t\in\{\pm1\},
  \qquad xy\ne0,
\]

where \(u,v\) are the two independent transformed output columns.  The four
parity equations force both \(x=y\) and \(x=-y\), while a zero coordinate of
\(u\) immediately forces \(xy=0\).  Thus the transformed AND tensor has mixed
parity and is not a matchgate.

This is a precise obstruction to one natural non-gcd route, not a complexity
lower bound for factoring or tensor contraction.

## 1. Closest prior routes and material difference

P10/F06 encodes multiplication by a scalar-carry automaton and refutes one
polynomial-state quotient.  P19/F11 gives an exact search-CVP reduction for a
one-hot multiplication witness but does not land in a known tractable lattice
class.  P29/F15 observes that an exact factor-trace or divisor-sum evaluator
would expose the factors, but does not construct one.

The present route is different in both representation and terminal operation.
It treats the full multiplication witness as a tensor-network partition
function and asks for exact Pfaffian/free-fermion contraction.  If that
contraction existed, witness-count self-reduction would output the divisor
directly; no residue-ring separator or final gcd is required.

The local fact used below is standard: an arity-one, arity-two, or arity-three
tensor is a matchgate tensor exactly when it is parity-pure.  It follows
directly from the matchgate identities and is stated explicitly in Sergey
Bravyi, [*Contraction of matchgate tensor networks on non-planar
graphs*](https://arxiv.org/abs/0801.2989), equation (1) and the discussion
immediately following it.  The proof below uses only the necessary parity
condition.

## 2. Conditional non-gcd reduction from exact contraction to factoring

Let \(N>1\) have \(n\) bits.  A polynomial-size Boolean constraint network can
express

\[
  xy=N,
  \qquad 0\le x,y<2^n,
\]

using partial-product AND constraints, copy constraints, and full-adder/carry
constraints.  Every satisfying assignment to its internal deterministic wires
corresponds to one ordered positive divisor pair \((x,N/x)\), and conversely.
Leading zeroes do not create multiple integer encodings.

Assume, conditionally, a uniform exact algorithm that contracts this network
and every version obtained by pinning any prefix of the \(x\)-bits, with bit
complexity polynomial in \(n\).  Let \(Z(P)\) be the exact number of witnesses
whose \(x\)-encoding extends a prefix \(P\).  Define

\[
  Z_*(P)
  =
  Z(P)
  -\mathbf1_{\{1\text{ extends }P\}}
  -\mathbf1_{\{N\text{ extends }P\}}.
\]

If \(N\) is composite, \(Z_*(\varnothing)=\tau(N)-2>0\).  At each next bit,

\[
  Z_*(P)=Z_*(P0)+Z_*(P1),
\]

so at least one child has positive adjusted count.  Choose such a child.
After \(n\) steps the resulting integer \(x\) satisfies

\[
  1<x<N,
  \qquad x\mid N.
\]

Exact division verifies the output.  A deterministic primality test handles
prime recursion leaves, and repeating the procedure on \(x\) and \(N/x\)
produces the complete factorization.  There are at most \(O(n)\) recursive
internal nodes and \(O(n)\) pinned contractions per node.  Every count has at
most \(2n+1\) bits because the network has at most \(2^{2n}\) external
assignments.  The conditional reduction is therefore polynomial in bit
complexity.

This decoder uses comparisons, subtraction of two known counts, exact
division, and recursion.  It uses no factor-extracting gcd; exact division may
of course be implemented by standard integer arithmetic whose internal library
routines are immaterial to the reduction.  The hypothesis deliberately
includes pinned instances; an unpinned scalar partition function alone need
not support self-reduction.

## 3. The two local signatures

Use the computational basis \(e_0,e_1\).  The ternary copy tensor is

\[
  E=e_0^{\otimes3}+e_1^{\otimes3}.
\]

The ternary AND relation, with third bit \(z=xy\), is

\[
  A
  =
  e_0\otimes e_0\otimes e_0
  +e_0\otimes e_1\otimes e_0
  +e_1\otimes e_0\otimes e_0
  +e_1\otimes e_1\otimes e_1.
  \tag{3.1}
\]

Use the ordinary contraction pairing \(x^{\mathsf T}y\).  If a basis \(T\)
acts covariantly on one endpoint of an edge, preservation of that pairing
requires the dual action

\[
  S=(T^{-1})^{\mathsf T}
\]

on the adjacent endpoint.  Allow independent common bases \(T_1,T_2\) for the
two factor-bit roles on the copy side; their fanout trees contain ternary copy
nodes.  Permit an entirely arbitrary invertible copy-side basis \(T_3\) on the
partial-product output wire and write \(S_j=(T_j^{-1})^{\mathsf T}\).  AND is
transformed by

\[
  A'
  =
  (S_1\otimes S_2\otimes S_3)A.
  \tag{3.2}
\]

Equivalently, one may place the primal bases on the constraint side and the
dual bases on the copy side.  The transpose in the dual action cannot in
general be dropped.

## 4. Classification of a basis that makes ternary copy parity-pure

First take one invertible matrix

\[
  T=
  \begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

whose columns are \(u=(a,c)^{\mathsf T}\) and
\(v=(b,d)^{\mathsf T}\).  Then

\[
  T^{\otimes3}E=u^{\otimes3}+v^{\otimes3}.
\]

If this tensor has even parity, its weight-one and weight-three entries give

\[
  a^2c+b^2d=0,
  \qquad
  c^3+d^3=0.
  \tag{4.1}
\]

Invertibility forces \(a,c\ne0\).  Put \(\rho=d/c\) and \(t=b/a\).
Then

\[
  \rho^3=-1,
  \qquad
  t^2=-\rho^{-1}=\rho^2.
\]

The solution \(t=\rho\) makes the columns proportional, so
\(t=-\rho\).  Hence

\[
  T=
  \operatorname{diag}(a,c)
  \begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix},
  \qquad \rho^3=-1.
  \tag{4.2}
\]

If the transformed copy tensor has odd parity, its weight-zero and weight-two
entries instead give

\[
  a^3+b^3=0,
  \qquad
  ac^2+bd^2=0,
\]

and the same argument yields

\[
  T=
  \operatorname{diag}(a,c)
  \begin{pmatrix}1&\rho\\1&-\rho\end{pmatrix},
  \qquad \rho^3=-1.
  \tag{4.3}
\]

There are no missing zero-coordinate cases: either equation pair would force
an entire row or column to vanish if \(a=0\) or \(c=0\).

Taking the transpose-dual of (4.2)--(4.3) shows that, for each
copied input role \(j\in\{1,2\}\), there are nonzero
\(\lambda_{j,0},\lambda_{j,1}\) and \(r_j\ne0\) such that

\[
  S_je_0
  =
  \begin{pmatrix}\lambda_{j,0}\\\lambda_{j,1}\end{pmatrix},
  \qquad
  S_je_1
  =
  r_j
  \begin{pmatrix}\lambda_{j,0}\\-\lambda_{j,1}\end{pmatrix},
  \qquad S_j=(T_j^{-1})^{\mathsf T}.
  \tag{4.4}
\]

More explicitly, the even form (4.2) has
\(r_j=-\rho_j^{-1}\), whereas the odd form (4.3) has
\(r_j=\rho_j^{-1}\).  Thus the transformed-coordinate ratio between the
original \(e_1\) and \(e_0\) columns is always \(r_j(-1)^b\) at output
coordinate \(b\); all row scalings cancel from that ratio.

## 5. AND cannot acquire either parity

For a transformed-coordinate bit \(b_j\in\{0,1\}\) on copied input role
\(j=1,2\), the ratio of the original-\(e_1\) column component to the
original-\(e_0\) column component in (4.4) is

\[
  r_j(-1)^{b_j}.
\]

Write the two columns of the arbitrary invertible dual output action \(S_3\) as

\[
  u=S_3e_0=
  \begin{pmatrix}u_0\\u_1\end{pmatrix},
  \qquad
  v=S_3e_1=
  \begin{pmatrix}v_0\\v_1\end{pmatrix}.
\]

They are linearly independent.  Put \(x=r_1\), \(y=r_2\), and for signs
\(s,t\in\{\pm1\}\) define the output-wire slice

\[
  W_{s,t}
  =
  u(1+xs+yt)+vxy\,st.
  \tag{5.1}
\]

Apart from nonzero input-coordinate factors, (5.1) is exactly the pair of
\(A'\)-components obtained by fixing \((-1)^{b_1}=s\) and
\((-1)^{b_2}=t\) and varying \(b_3\).

If \(A'\) had even parity, the odd-total-weight entries give

\[
  u_0(1-x+y)-v_0xy=0,
  \qquad
  u_0(1+x-y)-v_0xy=0,
  \tag{5.2}
\]

from the output-zero slice, and

\[
  u_1(1+x+y)+v_1xy=0,
  \qquad
  u_1(1-x-y)+v_1xy=0
  \tag{5.3}
\]

from the output-one slice.  If \(u_0=0\), invertibility gives \(v_0\ne0\)
and (5.2) forces \(xy=0\), impossible.  Likewise \(u_1=0\) contradicts
(5.3).  Thus \(u_0u_1\ne0\).  Subtracting within (5.2) gives \(x=y\), while
subtracting within (5.3) gives \(x=-y\).  Hence \(x=0\), again impossible.

If \(A'\) had odd parity, the even-total-weight entries instead give

\[
  u_0(1+x+y)+v_0xy=0,
  \qquad
  u_0(1-x-y)+v_0xy=0,
  \tag{5.4}
\]

and

\[
  u_1(1-x+y)-v_1xy=0,
  \qquad
  u_1(1+x-y)-v_1xy=0.
  \tag{5.5}
\]

The same zero-coordinate check applies.  Subtraction gives \(x=-y\) from
(5.4) and \(x=y\) from (5.5), a contradiction.

Thus \(A'\) is neither even nor odd and is not a ternary matchgate.  The
contradiction permits independent common bases for the two copied inputs,
independent cube roots \(\rho_1,\rho_2\), arbitrary nonzero scalings and copy
parities, and an arbitrary invertible dual action \(S_3\) on the AND output.
It therefore includes the usual single common basis as a special case.

## 6. Network and topology scope

A schoolbook or array multiplication network uses each factor bit in many
partial products.  The following explicit realization makes the local
bipartition used above literal.  For each factor bit, build a complete binary
fanout tree whose vertices are ternary copy tensors.  Contract the spare root
leg and any unused leaf leg with the neutral unary tensor \((1,1)\).  Every
used leaf leg is connected directly to an AND input.  All leaf copy vertices
then occur at one depth; adding one complete dummy level when necessary makes
the leaf vertices for both factor-input roles lie on the same side of the
bipartition.  Consequently every adjacent AND lies on the opposite side.
Any remaining edge of the multiplier network whose endpoints have the same
chosen color can be subdivided by a binary equality tensor, so the entire
network is bipartite without changing its witness count.

Under a common role basis on each side, a leaf copy tensor therefore receives
\(T_j\) on all three legs, while the adjacent AND input receives precisely
\(S_j=(T_j^{-1})^{\mathsf T}\).  If every local tensor in this realization
were a matchgate, this directly adjacent leaf-copy/AND pair would satisfy the
hypotheses of Sections 4--5, which is impossible.  Internal copy tensors,
neutral unaries, binary equalities, and full-adder signatures need not be
classified: the obstruction is already present in that local pair.

This local failure is independent of whether the resulting incidence graph is
planar.  It does not prove that a chosen multiplier layout is nonplanar, nor
does it analyze ordinary crossing signatures.  If a proposed construction
uses crossings, it must separately show a planar matchgate crossover or pay
the relevant nonplanar/genus cost.

The following remain open:

1. fusing copy, partial product, and addition into a larger multiplier-cell
   tensor before transforming;
2. high-arity equality used directly instead of the displayed ternary fanout
   realization;
3. edge-dependent gauges rather than one common basis per role and side;
4. an alternative Boolean gate set or a higher-domain encoding;
5. a Pfaffian/sub-Pfaffian identity not obtained by making the displayed
   local tensors matchgates;
6. cancellations or projections specialized to the fixed public bits of
   \(N\);
7. a bounded-genus or otherwise exactly contractible nonplanar network; and
8. a non-Pfaffian polynomial tensor contraction exploiting multiplication
   structure.

No complexity-theoretic hardness assumption is used to close any of these
possibilities.

## 7. Bit complexity and exact verdict

The conditional witness network has polynomially many Boolean variables and
constant-arity tensors with entries in \(\{0,1\}\).  Its exact partition
function has polynomial bit length.  A planar matchgate realization with
polynomially many vertices and polynomial-bit algebraic weights would be
contractible by a Pfaffian in polynomial arithmetic operations, provided its
field representation and exact bit growth were also polynomial.  The present
candidate supplies no such realization.

The narrow obstruction itself is constant-size algebra.  Its basis
classification and parity contradiction have fixed symbolic cost and introduce
no algorithm for factoring.

> **Exact verdict.** The natural separated
> \(\operatorname{COPY}_3,\operatorname{AND}_3\) signature set in the explicit
> bipartite ternary-fanout realization cannot be made into ternary matchgates
> by any invertible common role basis with its required transpose-dual action.
> More strongly, the two copied factor-input roles may use independent common
> bases while the AND-output wire uses an arbitrary invertible dual action.
> Consequently that natural multiplication-witness factor graph does not
> acquire an FKT/Pfaffian contraction through this transformation.  A
> hypothetical polynomial exact contraction for all pinned witness networks
> would nevertheless imply complete classical factoring by a self-reduction
> with no terminal factor-extracting gcd.

## 8. Materially new reopen condition

A retry must provide at least one exact ingredient outside the theorem:

1. a fused multiplier-cell signature and bases satisfying all matchgate
   identities, with a planar polynomial-size layout and pinned-count
   contraction;
2. a globally compatible edge-dependent gauge solution;
3. another Pfaffian/sub-Pfaffian realization with explicit signs, crossings,
   weights, and polynomial bit complexity;
4. a non-matchgate tractable tensor family containing the complete pinned
   multiplication network; or
5. a different exact count/metric observable whose polynomial evaluator and
   all-input factor decoder are both proved.

Merely observing that the multiplier circuit is polynomial size, or that each
individual rank-three tensor is separately SLOCC-equivalent to some matchgate,
does not meet the reopen condition.  Adjacent edge transformations must be
globally compatible, and the pinned partition functions must remain exactly
contractible.
