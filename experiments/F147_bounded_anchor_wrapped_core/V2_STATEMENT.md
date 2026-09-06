# F147 V2 candidate statement — bounded-anchor wrapped cycles have a quasipolynomial large-core decoder

## Status and scope

This is a proof-only candidate for the P128/P129/P131 positive-containment
route.  It is not a cycle-existence theorem and it is not a factoring
algorithm.

P131 proves that a positive directed cycle with a wrapped edge needs anchor
product above `sqrt(N)`.  It leaves open whether one must search an
exponentially branching path to reach that scale.  F147 gives a different
answer for every explicit frozen P128 source whose raw anchors are bounded
by `H` with `H^4 <= N`:

1. every wrapped cycle lies entirely in one publicly enumerable large-block
   core;
2. every edge in that core has carry and residual below `H^2`;
3. each word position has at most one possible large target block; and
4. all bridge dependencies and normalized roots in the core can be decoded
   in time polynomial in the explicit source and `H`.

Thus a single-path selector is not the computational gate inside one frozen
bounded-anchor source.  The remaining gate is arithmetic: prove that the
large core contains a surviving dependency whose normalized root is not
global.

## 1. Frozen source and directed edges

Let `N >= 3` be odd.  Let

\[
\mathcal B=(q_1,\ldots,q_m)
\]

be one frozen P128 named basis.  Its members are positive units modulo `N`,
are strictly between one and `N`, are pairwise coprime, and have undergone
the source's maximal perfect-power extraction.  Let `\mathcal P` be an
explicit finite list of legal squared-anchor positions

\[
(q,a),\qquad q\in\mathcal B,\qquad 1<a\le H,
\]

where every anchor is a unit modulo `N`.  Assume

\[
\boxed{H^4\le N.}
\tag{1}
\]

For a position put

\[
U=qa^2,
\qquad
c=[U]_N,
\qquad
w=\iota_N(c),
\qquad
U=c+tN,
\tag{2}
\]

with `0 <= t < a^2`.  The position is wrapped when `t >= 1`.

For distinct `q,r in \mathcal B`, exact division

\[
c=rT,
\qquad T\in\mathbb Z_{>0},
\tag{3}
\]

gives a directed containment edge `q -> r`, with residual `T`.  The actual
P128 values at the position are

\[
C=cw,
\qquad
L=Uw.
\tag{4}
\]

All quantities in (2)--(4) are public.  Before using an edge, run the usual
endpoint screens `gcd(c-w,N)` and `gcd(c+w,N)`.  A proper gcd is immediate
success and leaves the branch considered below.

## 2. Large-core theorem

Let a directed containment cycle contain at least one wrapped edge.  Then
every edge of the cycle is wrapped.  Moreover, for every edge `e:q -> r`
of that cycle,

\[
\boxed{
q>\frac{N}{H^2},
\qquad
r>\frac{N}{H^2},
\qquad
1\le t_e<H^2,
\qquad
1\le T_e<H^2.
}
\tag{5}
\]

For every fixed legal position `(q,a)`, its residue `c` is divisible by at
most one named block larger than `N/H^2`.

Consequently, define the **wrapped large core** `G_H` as follows.  Its
vertices are the named blocks greater than `N/H^2`.  Scan every position in
`\mathcal P` whose source is such a vertex.  Keep its unique large target,
if one exists, only when the position wraps.  Every wrapped directed cycle
in the full positive-containment graph occurs in `G_H`, and no word position
branches into two large targets.

This is a structural statement.  A vertex can still have several outgoing
edges from different anchors.

## 3. Exact bridge decoder for the large core

For an edge `e:q -> r`, its conceptual P128 bridge is

\[
D_e=U_ec_e=qra_e^2T_e,
\qquad
D_e\equiv c_e^2\pmod N.
\tag{6}
\]

Jointly run complete multiplicity-aware gcd-free refinement and maximal
perfect-power extraction on all center blocks and all residuals in `G_H`.
This gives the exact binary square-class column of every `D_e`.  Let `M_H`
be the resulting matrix.

Equivalently, the residuals can be factored directly in time polynomial in
`H`: because `T_e < H^2`, trial division through `H` removes every possible
composite part, with at most one prime cofactor left.

For every `x in ker(M_H)`, the exact integer

\[
\prod_{e:x_e=1}D_e
\]

is a square.  If its positive square root is `Y_x`, its normalized root is

\[
\boxed{
\rho_x
\equiv
Y_x\left(\prod_{e:x_e=1}c_e\right)^{-1}
\pmod N.
}
\tag{7}

The corresponding actual P128 selection uses both values `C_e,L_e` for
every selected edge.  Indeed,

\[
C_eL_e=D_ew_e^2,
\tag{8}
\]

so it has the same normalized root (7).

Map every selected `C_e,L_e` to its global exact-value equality class before
binary decoding.  Equal actual values cancel in pairs.  This gives a linear
map from `ker(M_H)` to the globally deduplicated P128 ledger.  Compute a
basis of its image and test (7) for basis preimages.  If every basis root is
in `{+1,-1}`, every combination is global.  If one basis root is non-global,
`gcd(rho_x-1,N)` gives a proper factor.  A non-global dependency cannot
vanish under exact-value deletion.

This decoder is complete for the bridge dependencies supported on `G_H`.
It does not claim that `ker(M_H)` is nonzero or that its normalized-root
image is non-global.

There is one explicit edge-surplus criterion.  Let `E_H` be the number of
edges in `G_H`, and let `R_H` be the number of distinct rational primes that
divide its residuals.  If the frozen named basis has `m` blocks, then

\[
\boxed{
\dim\ker(M_H)\ge E_H-m-R_H
\ge E_H-m-\pi(H^2).
}
\tag{9}
\]

Thus `E_H>m+R_H` forces a conceptual bridge dependency.  Survival under
global exact-value deletion and a non-global normalized root remain separate
checkable gates.

## 4. Quasipolynomial cost

Let `Q` bound the number of named blocks, the complete retained ledger, and
the number of explicit positions.  The large core can be constructed by at
most `Q^2` exact
division tests on `O(n+log H)`-bit integers.  The direct screens, actual
value construction, global exact-value sorting, complete refinement, binary
linear algebra, and normalized-root tests are polynomial in

\[
Q,
\quad H,
\quad n+\log H.
\tag{10}
\]

Therefore the procedure is quasipolynomial when

\[
Q=2^{(\log n)^{O(1)}},
\qquad
H=2^{(\log n)^{O(1)}}.
\tag{11}
\]

Condition (1) then holds for all sufficiently large `n`.  Small inputs can
be handled separately by the permitted finite preprocessing.

The construction retains the original P128 word provenance.  It does not
promote a residue, cofactor, or gcd aggregate to a new named generator.  A
partial gcd with an old named block is processed by the standard complete
refinement; the frozen integer presentation remains valid.

## 5. Consequence for a single-path sampler

If a wrapped directed cycle has length `L` and all its anchors are bounded
by `H`, P131 gives

\[
\sqrt N<\prod_{e=1}^{L}a_e\le H^L.
\]

Consequently,

\[
\boxed{
L>\frac{\log N}{2\log H}
}
\qquad\text{or equivalently}\qquad
L\ge
\left\lfloor\frac{\log N}{2\log H}\right\rfloor+1.
\tag{12}
\]

This is only a necessary length condition.  Its numerical threshold is
polynomial in `n` when `H=n^{O(1)}`, but it gives no upper bound on the
required cycle length and does not show that suitable legal anchors can be
selected.  It does not force a return edge, a square residual product, or a
non-global root.

Inside one frozen source, exhaustive path branching is unnecessary: scan
`G_H` once and run the exact linear decoder above.  Outside a frozen source,
a rule that follows one newly manufactured aggregate is a different source
grammar.  F147 gives no all-input law for that grammar.

The exact positive theorem still needed is

> For every surviving input, some frozen bounded-anchor large core has a
> bridge-kernel vector that survives global exact-value deletion and has a
> non-global normalized root.

An inverse-quasipolynomial density theorem for such vectors would also be
enough for a Las Vegas quasipolynomial algorithm.  Mere existence of one
long anchor sequence gives no such sampling bound.

