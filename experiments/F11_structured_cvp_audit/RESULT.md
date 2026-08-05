# Hostile audit of F11 structured CVP

## Verdict

The central positive statement survives, after making the CVP convention and
the linear-algebra step explicit:

> There is a deterministic polynomial-bit Turing reduction from complete
> integer factoring to **search exact Euclidean CVP** on the integer kernels of
> the stated one-hot schoolbook-multiplication systems, with their translated
> half-integral targets.

This is a valid conditional reduction, not a factoring algorithm.  It supplies
no polynomial-time algorithm for those CVP instances.

The three concrete negative certificates also survive in their proper scope:

- this particular constraint-incidence presentation has treewidth at least
  `min(a,b)`;
- this particular affine kernel has codimension at least `ab`;
- the rank-one-free lifted-matrix relaxation has a spurious binary optimum for
  `N=25`.

Two broader conclusions do **not** follow:

1. No proof shows that every polynomial-size exact linearization of Boolean
   rank one, or every basis/presentation of the same lattice, must have high
   width.  The `K_(a,b)` proof applies to the displayed one-hot presentation.
2. The `N=25` matrix refutes direct rank-one decoding, but it does not prove
   that no postprocessing of a relaxed optimum can recover a factor.  Indeed,
   this particular witness retains the true convolution polynomial.

Accordingly, F11 is a sound reduction plus two obstructions to specific
proposed algorithms.  It is not a general “structural kill” of all ways to
exploit these lattices.

## 1. Bit-length enumeration: correct

Let `n` be the bit length of an odd composite `N`.  If factors `x,y` have exact
bit lengths `a,b`, then

\[
2^{a+b-2}\le xy=N<2^{a+b}.
\]

Hence `n` is either `a+b-1` or `a+b`, equivalently

\[
a+b\in\{n,n+1\}.
\]

Choose a nontrivial divisor `x <= sqrt(N)` and put `y=N/x`; then `a<=b`.
After even inputs are split off, `x` is odd and at least 3, so `a>=2`.  There
are `O(n)` candidate pairs.  Exact leading-bit constraints enforce the claimed
lengths.  This covers unbalanced factors, prime powers, repeated factors, and
general composites.  Bits `N_k` above the leading bit must simply be defined
as zero; this convention was implicit in the original statement.

## 2. One-hot and carry equations: correct and complete

Assume every coordinate is binary.  For a fixed `(i,j)`, the equation

\[
\sum_{u,v\in\{0,1\}}\lambda_{ij}^{uv}=1
\]

selects exactly one tuple.  The two marginal equations force its selected
values to equal `x_i` and `y_j`.  Therefore

\[
\lambda_{ij}^{11}=x_i y_j.
\]

Let `s_k=sum_(i+j=k) lambda_(i,j)^11`.  Multiplying the carry equations by
`2^k` and summing over `0 <= k <= a+b-1` gives

\[
\sum_k2^ks_k+c_0-2^{a+b}c_{a+b}
  =\sum_k2^kN_k=N.
\]

The boundary carries vanish, while the left convolution is `xy`; hence every
binary solution gives `xy=N`.  The low- and high-bit constraints make both
factors odd, nontrivial, and of the enumerated lengths.

Conversely, an actual factor pair selects its `(x_i,y_j)` tuple at every pair
and uses the ordinary schoolbook carries, satisfying every equation.  Thus the
binary solutions are exactly the intended multiplication witnesses.

No nonlinear equation was silently used here.  Nonbinary integral solutions
are allowed in the affine lattice and are excluded only by the distance
objective.

## 3. Carry-digit bound: correct

Since `a<=b`, every column contains at most `a` partial products, so
`0<=s_k<=a`.  Starting with `c_0=0`, suppose `0<=c_k<=a-1`.  The recurrence is

\[
c_{k+1}=\frac{s_k+c_k-N_k}{2}.
\]

Its numerator is at least `-1`; when it is integral it cannot be a negative
integer.  It is at most `2a-1`, so integrality also gives `c_(k+1)<=a-1`.
Thus `ceil(log_2 a)` binary digits suffice, including when `a` is a power of
two.  The actual product has the stated zero terminal carry.

## 4. Size and integral linear algebra: correct with a proof repair

The coordinate count

\[
M=4ab+a+b+(a+b+1)\lceil\log_2a\rceil=O(n^2)
\]

is correct.  There are `O(n^2)` equations.  The largest coefficients are carry
weights below `2a`, so their bit length is `O(log n)`; even a dense encoding is
polynomial size.

For an integer matrix `A`, Smith normal form gives unimodular `P,Q` with
`PAQ=D`.  Integral feasibility of `Az=d` is exactly the usual divisibility and
zero-row test on `Pd`.  If feasible, setting the free transformed coordinates
to zero gives a particular solution `z_0`; the columns of `Q` belonging to zero
diagonal positions give a basis `B` of

\[
L=\ker_{\mathbf Z}(A).
\]

Polynomial-bit HNF/SNF algorithms compute these objects in time polynomial in
the matrix dimensions and coefficient bit lengths.  Therefore `z_0` and `B`
have polynomial output bit length for this input family.

The original sentence “Hadamard bounds the minors and hence the retained basis
data” is not, by itself, a proof: arbitrary unimodular transformations can be
made unnecessarily enormous.  The required conclusion follows from the
standard polynomial-bit HNF/SNF algorithm, not from Hadamard alone.  This is a
repairable exposition gap, not a counterexample to the reduction.

## 5. The affine coset is an exact CVP instance

The feasible integer set is `z_0+L`.  With

\[
h=\tfrac12\mathbf 1,
\]

minimizing `||z-h||` over this coset is exactly minimizing

\[
\|\ell-(h-z_0)\|\quad\text{over }\ell\in L.
\]

Thus a kernel basis and target `h-z_0` form an ordinary embedded-lattice CVP
instance.  Fractions can be removed without changing minimizers: query the
integer lattice generated by `2B` at the integer target

\[
t=\mathbf1-2z_0.
\]

All dimensions and bit lengths remain polynomial.  Standard CVP allows a
rank-`r` lattice embedded in `R^M`.  If one insists on a full-rank-in-ambient-
space convention, the conversion is still polynomial: append a sufficiently
large multiple of independent rows of `A`.  Those rows span the orthogonal
complement of `ker_R(A)`.  Taking an integer multiplier `K>||t||` makes every
vector using a nonzero appended component farther than the candidate with all
appended coefficients zero.  `K` has polynomial bit length, so this padding
preserves the desired closest kernel vector.

The reduction must be stated for **search** CVP, or separately include the
standard search-from-decision step.  The original decoding discussion already
uses a returned closest vector, so search CVP is the clean exact scope.

## 6. Baseline optimum and gap: correct, with one wording correction

For an integer `m`,

\[
(m-\tfrac12)^2\ge\tfrac14,
\]

with equality exactly for `m` in `{0,1}`.  The next possible value is `9/4`, an
increase of 2.  Therefore every integral vector has squared distance at least
`M/4`, with equality exactly when every coordinate is binary.

If a factor witness exists, the optimum is exactly `M/4` and every minimizer
is a valid binary witness.  If none exists, the optimum is **at least**
`M/4+2`.  It need not equal `M/4+2`; “exact additive gap” is safe only if it
means an exact certified separation, not equality for every no-instance.

The relative threshold

\[
\sqrt{(M/4+2)/(M/4)}=\sqrt{1+8/M}
\]

is also correct.  A fixed constant-factor approximation does not distinguish
these two bounds.

## 7. Decoding, verification, and recursion: valid conditionally

For every length pair with an integral affine solution, ask exact search CVP
for a closest vector, translate it back to `z`, and accept only if:

1. all coordinates are 0 or 1;
2. the decoded bit strings have the required endpoints; and
3. direct multiplication verifies `1<x<N` and `xy=N`.

This verification is polynomial and makes every returned split correct.  At
the correct length pair, the baseline argument guarantees that every closest
vector passes.  Infeasible or wrong length pairs can be skipped.

For complete factorization, first remove factors of 2 and use deterministic
polynomial-time primality testing at every node.  Recursively apply the split
procedure only to composite children.  A factorization tree has at most `n`
prime-factor leaves counted with multiplicity and fewer than `n` internal
nodes.  Each node tries `O(n)` length pairs, so there are `O(n^2)` CVP calls in
total; all query dimensions and bit lengths are polynomial in the original
`n`.  Consequently a uniform polynomial-time exact-CVP algorithm for this
family would yield a uniform polynomial-time complete factoring algorithm.

This proves the reduction.  It does not provide the required CVP algorithm.

## 8. Incidence treewidth: correct only for the displayed presentation

In the bipartite variable/equation incidence graph, for each `(i,j)` the edges

\[
x_i-E^x_{ij}-\lambda^{11}_{ij}-E^y_{ij}-y_j
\]

form a path.  Its three internal vertices are distinct for different pairs.
Deleting all unneeded incident edges leaves a subdivision of `K_(a,b)`.
Contracting the paths gives the minor, hence

\[
\operatorname{tw}(G)\ge\operatorname{tw}(K_{a,b})=\min(a,b).
\]

This is `Theta(n)` for balanced length pairs.  It rules out a polynomial bound
from a dynamic program whose running time is exponential in the width of
**this incidence presentation**.

It says nothing by itself about the graph of an HNF/SNF basis.  A computed
basis may densify, but “typically dense” was not defined or proved, and one
dense basis does not rule out another sparse or algorithmically favorable
basis.  Conversely, sparsity of the constraints does not transfer
automatically to a kernel basis.  Any basis-level tractability or obstruction
needs a separate theorem.

## 9. Codimension: correct

Each one-hot row contains its own coordinate `lambda_(i,j)^(0,0)`, and that
coordinate occurs in no marginal, carry, endpoint, or other one-hot row.
Those `ab` rows are therefore linearly independent over `Q`, so

\[
\operatorname{rank}(A)\ge ab.
\]

For a feasible coset its real codimension is `rank(A)`, hence at least `ab`.
For balanced pairs this is `Omega(n^2)`, a constant fraction of the ambient
dimension.  The instance is not in a fixed- or low-codimension regime in this
presentation.

## 10. The `N=25` certificate: arithmetic correct, conclusion narrower

For `a=b=3`, the true bit vectors are `(1,0,1)`, and their outer product has
anti-diagonal sums

\[
(1,0,2,0,1).
\]

The proposed matrix

\[
Z'=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}
\]

has the same sums.  With the bits of 25 equal to `(1,0,0,1,1)`, the carry
sequence `(0,0,0,1,0,0)` satisfies every column equation.  `Z'` is binary and
therefore attains the same half-target baseline as the true lift, while
`det(Z')=1`; it is rank 3 and cannot be a Boolean outer product.

This proves that the rank-one-free Toeplitz/convolution relaxation has
spurious exact minimizers and invalidates a decoder that assumes every returned
matrix is `xy^T`.

It does **not** prove that no decoder can use such a minimizer.  In this exact
example the anti-diagonal polynomial is

\[
1+2T^2+T^4=(1+T^2)^2,
\]

so polynomial factorization recovers the bit polynomial `1+T^2` and hence the
factor 5.  This observation does not rescue the relaxation on general inputs;
it only refutes the literal phrase that “no factor can be decoded” from this
particular witness.  To rule out all postprocessing or tie-breaking would
require an additional argument, and none is present.

## 11. No universal width lower bound was proved

The set `Z=xy^T` is nonlinear over the integers.  The displayed one-hot gadget
enforces it exactly and creates the `K_(a,b)` subdivision.  Direct `2x2` minor
equations are quadratic, and the usual pairwise truth-table or McCormick-style
binary linearizations again create dense pair interactions.

That is the full proved scope.  No extension-complexity, communication, minor,
or treewidth lower bound was supplied for **all** polynomial-size auxiliary-
variable formulations.  Auxiliary copies, alternative coordinates, or a
different lattice basis could change the graph.  Therefore the claims that
restoring rank one “requires the full consistency gadgets” or necessarily
restores high width must be retracted or explicitly limited to the named
local linearizations.

Likewise, saying the Boolean rank-one set is “not an ideal” is undefined until
a ring and operations are specified.  Nonadditivity is enough to show it is
not itself an affine lattice; it does not establish a complexity lower bound.

## Corrected theorem and exact scope

The strongest theorem established by F11 is:

> **Corrected F11 theorem.** Complete integer factoring has a deterministic
> polynomial-bit Turing reduction to search exact Euclidean CVP on the
> (possibly embedded, or polynomially padded to full-rank) integer kernel
> lattices of the explicit one-hot multiplication systems, at the translated
> half targets.  Yes-instances have squared affine distance exactly `M/4`; a
> length pair without a binary multiplication witness has squared affine
> distance at least `M/4+2`.  The displayed constraint presentation has
> treewidth at least `min(a,b)` and codimension at least `ab`.  Dropping Boolean
> rank one from the lifted convolution system admits a spurious baseline
> minimizer at `N=25`.

What remains unproved is any polynomial-time exact-CVP algorithm for this
family, any low-width presentation or basis for it, or any universal lower
bound excluding such a presentation.  The `N=25` witness rules out only direct
outer-product decoding of the relaxed optimum, not every possible
postprocessing algorithm.  Thus F11 remains a valid reduction to a
theorem-strength missing lemma and does not resolve factoring.

## Audit method

This audit rederived each equation, bound, graph minor, and finite certificate
symbolically.  No computational experiment was used.
