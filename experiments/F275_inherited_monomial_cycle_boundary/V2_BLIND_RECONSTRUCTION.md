# F275 V2 blind reconstruction

## Blind input and verdict

Input: `V2_STATEMENT.md` at SHA-256
`a9bd86b4e4515f133c3c2d7711c530d334749675e0aa75eb8bc7547f3ad0f0da`.
Its manifest `V2_FROZEN.sha256` had SHA-256
`fb8e508c100bc81cf1105ba7be09162df7d73eb7a5ef704b3a687b3567b1a372`.
Both hashes matched before this reconstruction began.

This reconstruction was derived from that statement alone. Before this file
was sealed, I did not read a proof, audit, provenance file, ledger, prior F275
claim, or prior F275 reconstruction.

**Verdict.** The monomial, graph, even-cycle, and canonical-size assertions
listed in V2 follow from exact integer multiplication and unit arithmetic
modulo `N`. The result is an obstruction for one precise mechanism. It is not
a factoring algorithm, and it says nothing about F270.

## Conventions

Let `N>1`. A *unit* is an integer coprime to `N`. For a unit residue `x`, write
`[x]_N` for its unique representative in `[1,N)`. If `a` is a unit, then

\[
 \gcd(ab,N)=\gcd(b,N).
 \tag{1}
\]

Also, replacing an integer by a congruent integer does not change its gcd
with `N`. These two facts justify every gcd cancellation below. They also show
why each inverse and unit hypothesis is necessary.

## Theorem A: monomial pullback and the direct root screen

Let `d_j` be positive units indexed by a finite set `J`. Let the positive rows
be the exact monomials

\[
 A_i=\prod_{j\in J}d_j^{M_{ji}},\qquad M_{ji}\in\mathbf Z_{\ge0},
 \tag{2}
\]

and let the supplied unit labels satisfy `y_i^2 = A_i (mod N)`. Choose
nonnegative row multiplicities `m_i`. Suppose every entry of `Mm` is even.
Set

\[
 q_j=\frac12\sum_i M_{ji}m_i,
 \qquad
 X=\prod_j d_j^{q_j},
 \qquad
 Y=\prod_i y_i^{m_i}.
 \tag{3}
\]

Then the following are exact or modular identities, as marked:

\[
 \prod_i A_i^{m_i}=X^2 \quad\text{exactly},
 \qquad
 Y^2\equiv X^2\pmod N.
 \tag{4}
\]

The normalized supplied root is

\[
 h=[YX^{-1}]_N
   =\left[\prod_i y_i^{m_i}
           \prod_j d_j^{-q_j}\right]_N,
 \qquad h^2\equiv1\pmod N.
 \tag{5}
\]

The standard exact-square gcds therefore pull back to the normalized root:

\[
 \gcd(X-Y,N)=\gcd(1-h,N),
 \qquad
 \gcd(X+Y,N)=\gcd(1+h,N).
 \tag{6}
\]

This is a formula, not a promise of a factor. If `h=1 (mod N)`, the minus
gcd is `N`. If `h=-1 (mod N)`, the plus gcd is `N`. Only a square root of one
that is neither sign gives nontrivial gcds. No assertion here supplies such a
root.

There is also a direct screen for an arbitrary root. If `R` is any unit with
`R^2 = X^2 (mod N)`, define

\[
 r=[RX^{-1}]_N,
 \qquad s=[RY^{-1}]_N.
 \tag{7}
\]

Both `r` and `s` square to one. One can compare `R` directly with either the
integer square root or the supplied root:

\[
\begin{aligned}
 \gcd(X-R,N)&=\gcd(1-r,N),&
 \gcd(X+R,N)&=\gcd(1+r,N),\\
 \gcd(R-Y,N)&=\gcd(s-1,N),&
 \gcd(R+Y,N)&=\gcd(s+1,N).
\end{aligned}
 \tag{8}
\]

Thus an alleged alternative root needs no indirect cycle test. The two gcds
against the supplied root are the complete direct screen for this mechanism.

### Structural graph corollary

Let a finite undirected multigraph have a positive unit carrier `d_v` at each
vertex. For an edge occurrence `e={u,v}`, set

\[
 A_e=d_ud_v,
 \qquad y_e^2\equiv d_ud_v\pmod N.
 \tag{9}
\]

An endpoint is counted with multiplicity. In particular, a loop contributes
two incidences at its vertex. For edge multiplicities `m_e`, define the
weighted degree

\[
 \delta_v=\sum_{e\ni v}m_e.
 \tag{10}
\]

If all `delta_v` are even, the edge multiset is Eulerian and (3)--(6) become

\[
 \prod_e A_e^{m_e}
   =\left(\prod_v d_v^{\delta_v/2}\right)^2,
 \quad
 h=\left[
       \prod_e y_e^{m_e}
       \prod_v d_v^{-\delta_v/2}
     \right]_N.
 \tag{11}
\]

This is the unsigned incidence calculation. It is a sufficient numerical
square condition. It is necessary only as a *structural monomial* condition,
where the carriers are treated as independent formal generators. Numerical
carriers can have accidental equalities or square factors. Equation (11)
does not classify those accidents or the full graph-carrier kernel.

## Theorem B: cycles and even-cycle holonomy

Consider a cycle with vertex occurrences `v_1,...,v_ell` and edges
`e_i={v_i,v_{i+1}}`, where `v_{ell+1}=v_1`. Repeated vertices and parallel
edges cause no change when occurrences are counted. Define

\[
 X_C=\prod_{i=1}^{\ell}d_{v_i},
 \qquad
 Y_C=\prod_{i=1}^{\ell}y_{e_i}.
 \tag{12}
\]

Every vertex occurrence appears in two edge rows. Hence

\[
 \prod_{i=1}^{\ell}A_{e_i}=X_C^2 \quad\text{exactly},
 \qquad
 Y_C^2\equiv X_C^2\pmod N.
 \tag{13}
\]

The exact square in (13) holds for cycles of either parity. The label-only
formula below needs an even cycle.

Let `ell=2k`. Put

\[
 P_{\rm odd}=\prod_{i\ \mathrm{odd}}y_{e_i},
 \qquad
 P_{\rm even}=\prod_{i\ \mathrm{even}}y_{e_i}.
 \tag{14}
\]

Each alternating edge set meets every vertex occurrence once. Therefore

\[
 P_{\rm odd}^2\equiv X_C\equiv P_{\rm even}^2\pmod N.
 \tag{15}
\]

The even-cycle holonomy is the label-only unit

\[
 z_C=[P_{\rm odd}P_{\rm even}^{-1}]_N.
 \tag{16}
\]

It satisfies

\[
 z_C^2\equiv1\pmod N,
 \qquad
 z_C\equiv Y_CX_C^{-1}\pmod N.
 \tag{17}
\]

Indeed, the first identity follows from (15), and the second follows from
`Y_C=P_odd P_even` and `X_C=P_even^2 (mod N)`. The cycle gcds are exactly

\[
\begin{aligned}
 \gcd(X_C-Y_C,N)
   &=\gcd(P_{\rm even}-P_{\rm odd},N)
    =\gcd(1-z_C,N),\\
 \gcd(X_C+Y_C,N)
   &=\gcd(P_{\rm even}+P_{\rm odd},N)
    =\gcd(1+z_C,N).
\end{aligned}
 \tag{18}
\]

Changing the starting parity replaces `z_C` by its inverse. Reversing the
cycle has the same effect, up to the same parity choice. Since `z_C^2=1`,
its inverse is itself. Thus (18) has no hidden orientation or starting-edge
sign.

There is no corresponding alternating label-only identity for an odd cycle.
For example, take `N=35`, carriers `(4,9,16)`, and edge labels `(6,12,8)` in
cyclic order. Their squares match the three edge products modulo `35`.
Here `X_C=Y_C=576`, so the normalized cycle root is `1`. In contrast,
`y_1 y_3 y_2^{-1}=4 (mod 35)`, which does not even square to `1`. This also
shows why an odd-cycle extension cannot be obtained by choosing a starting
edge.

## Canonical inverse-square construction and its size endpoint

Let `y` and `d` be units and define the canonical inverse-square partner

\[
 T_y(d)=[y^2d^{-1}]_N.
 \tag{19}
\]

If the input carrier is canonical, `1<=d<N`, then `T_y(d)` is a canonical
unit too. The positive row

\[
 A=dT_y(d)
 \tag{20}
\]

has the supplied root `y`, because `A=y^2 (mod N)`, and it has the exact size
bound

\[
 1\le A\le(N-1)^2<N^2.
 \tag{21}
\]

This is the complete size argument. It uses both canonical inequalities. It
does not apply when the input `d` is an arbitrary positive representative.
For example, representatives congruent to `1` can be made arbitrarily large
while `T_y(d)` stays in `[1,N)`. Thus (21) cannot be imported into the
general graph theorem.

For reference, canonicality also makes `T_y` an involution:

\[
 T_y(T_y(d))=d.
 \tag{22}
\]

This follows first modulo `N`, then exactly from uniqueness in `[1,N)`.

## Reduction and complement boundary

Two distinct operations must not be confused with the exact monomial row.
For canonical `d`, let `t=T_y(d)`. Carrier complementation gives

\[
 T_y(N-d)=N-t,
 \tag{23}
\]

because inversion changes sign modulo `N` and both sides are canonical.
Consequently

\[
 (N-d)(N-t)=dt+N(N-d-t)\equiv dt\equiv y^2\pmod N.
 \tag{24}
\]

The two rows have the same canonical reduction, but they are generally
different integers. In fact

\[
 [dt]_N=[(N-d)(N-t)]_N=[y^2]_N.
 \tag{25}
\]

More generally, reduce each graph edge row to `a_e=[A_e]_N`. On a cycle,

\[
 \prod_e a_e\equiv X_C^2\pmod N,
 \tag{26}
\]

but the left side need not be an exact integer square. If instead one uses
the canonical complements `c_e=N-a_e`, then

\[
 \prod_e c_e\equiv(-1)^{\ell}X_C^2\pmod N.
 \tag{27}
\]

For an even cycle, (27) is congruent to the same square, but it still need not
be an exact square. Thus neither reduction nor reduced complementation
preserves the exact incidence identity (13).

A small counterexample tests both claims. Let `N=7` and take an even cycle
with carriers `(1,2,4,1)`. The unreduced edge rows are `(2,8,4,1)`, whose
product is the exact square `64`. They have supplied roots `(3,1,2,1)`
modulo `7`. The canonical reduced rows are `(2,1,4,1)`, whose product is `8`,
not a square. Their complements are `(5,6,3,6)`, whose product is `540`, also
not a square, although both products are congruent to `64` modulo `7`.

The inherited-monomial obstruction applies only when the exact integer
square comes from the unreduced carrier monomials. It does not apply merely
because a reduced or complement product is congruent to a square. Therefore
no conclusion about F270 follows from these theorems. In particular, this
reconstruction proves no F270 obstruction, success claim, event law, runtime
law, canonical-section lower bound, graph-carrier kernel classification, or
factoring algorithm.

## Edge-case audit

- Empty products give `X=Y=h=1`. The identities hold and yield no factor.
- A loop counts twice at its vertex. Counting it once would make (11) false.
- A two-edge cycle with parallel edges is valid. Each alternating set has one
  edge, so (15)--(18) still hold.
- Zero residues are excluded by the unit hypotheses. Without units, the
  inverses and gcd cancellations can fail.
- The gcd identities do not require `N` to be squarefree or semiprime. For
  even `N`, the plus and minus gcds can overlap, so they must not be described
  as complementary factors without an extra hypothesis.
- The Eulerian test captures structural exponents. Accidental numerical
  squares do not establish a converse or a kernel classification.
- Carrier size is irrelevant to (9)--(18). The bound `A<N^2` belongs only to
  (19)--(21), where `1<=d<N` is explicit.
- Odd cycles retain (13), but they do not inherit the label-only holonomy
  formula (16).
