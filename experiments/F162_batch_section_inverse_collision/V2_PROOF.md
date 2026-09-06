# Proof of the F162 batch signed-inverse detector V2

## 1. Deduplication and equal-value positions

All input values are units. If a supplied value is not known to be a unit,
the algorithm first computes its gcd with `N`; a nontrivial result is already
a valid output.

Replace the position list by its distinct canonical residue set `A`, while
retaining multiplicities. Suppose two distinct source positions have the
same residue `a`. Their signed pair test is

\[
\gcd(a^2-\epsilon,N).
\]

The algorithm tests this value for every distinct `a`, so no useful
equal-value pair is lost. Running the test when `a` occurs only once is an
additional public factor test and cannot make an output incorrect.

The explicit `r`-position input must first be read. Deterministic sorting,
canonicalization, and deduplication cost `\widetilde O(rn)` bit operations.
If exact multiplicities are retained, their counters use
`O(m log(r+1))` bits. The detector itself needs only one duplicate flag per
value because it runs every self screen even for a singleton.

It remains to detect useful pairs with distinct residues `a,b in A`.

## 2. The product-polynomial identity

Fix `a in A` and `epsilon in {+1,-1}`. Put

\[
x=\epsilon a^{-1}\pmod N.
\]

For every `b in A`,

\[
x-b=a^{-1}(\epsilon-ab)\pmod N.
\tag{16}
\]

Since `a` is a unit, the two sides have the same gcd with `N`, up to the
other product factors.

If `x notin A`, direct evaluation gives

\[
P(x)=a^{-m}\prod_{b\in A}(\epsilon-ab)\pmod N.
\tag{17}
\]

If `x in A`, then the factor with `b=x` is exactly zero modulo all of `N`.
It corresponds to the publicly visible global relation `ab=epsilon mod N`,
whose gcd is the improper value `N`. Formal differentiation at the exact
root gives

\[
P'(x)
=\prod_{\substack{b\in A\\b\ne x}}(x-b)
=a^{-(m-1)}
\prod_{\substack{b\in A\\b\ne x}}(\epsilon-ab)
\pmod N.
\tag{18}
\]

The derivative removes exactly the one distinct global partner. It uses no
division by `x-b` and remains valid over the composite ring.

Now assume a useful distinct-position pair `(a,b)` exists. If `a=b`, the
equal-value test has already returned a factor. If `a!=b` and
`ab!=epsilon mod N`, then `b` occurs in the product (17) or (18), and its
factor has a nontrivial gcd with `N`. Hence

\[
\gcd(H_{a,\epsilon},N)>1.
\tag{19}
\]

The only omitted value in (18) satisfies the equality modulo all of `N`, so
it cannot be a proper pair hit. This proves detection completeness.

## 3. Localization when the aggregate gcd is `N`

If the gcd in (19) is proper, return it directly. Suppose it equals `N`.
Build a balanced scalar product tree whose leaves are

\[
x-b\pmod N,
\qquad b\in A,\ b\ne x.
\tag{20}

The root product is `H` up to a public unit. At a node with gcd `N`, inspect
its two children. A child with proper gcd is already an answer. A child with
gcd `N` is descended recursively. Children with gcd one are ignored.

This process cannot end at a leaf with gcd `N`. The canonical residues `x`
and `b` are distinct integers in `[0,N-1]`, so

\[
0<|x-b|<N.
\]

Thus `N` does not divide the leaf difference. Since the root gcd is `N`, at
least one child remains nonunit at every split. The descent therefore reaches
a node, and at worst a leaf, whose gcd is a proper factor of `N`.

This argument does not assume that `N` is squarefree or semiprime.

## 4. Exact composite-ring evaluation and cost

Build `P` with a monic product tree. Build a monic point tree for the
`2m` points `x_(a,epsilon)`. A remainder tree evaluates `P` and its formal
derivative `P'` at all points.

Polynomial division by a monic divisor works over every commutative ring.
Fast reversed division inverts only a power-series constant term equal to
one. Thus the evaluator never divides by a point difference, a leading
coefficient, or another data-dependent residue. This is the same
composite-ring multipoint interface already verified for P34.

Carry-safe Kronecker multiplication gives soft-linear polynomial arithmetic
in the total coefficient encoding. The product tree, two remainder trees,
`2m` modular inverses, gcd tests, and at most one localization have bit cost

\[
\widetilde O\!\left(rn+(m(n+\log m))^{1+o(1)}
+m\,\mathsf M(n)\log n\right).
\]

All stored coefficients are residues modulo `N`, and all tree degrees sum to
`O(m log m)`. The post-normalization polynomial working storage is
soft-linear in `mn`. Exact multiplicity counters add `O(m log(r+1))` bits;
one duplicate flag per distinct value is enough for this detector. If the
resident explicit input is counted, it occupies `O(rn)` bits. This proves the
general batch theorem and its factor-free cost.

## 5. Shared-block batches

For a frozen section basis, every `q_i=z_i^2 mod N` is a unit. If
`T subseteq v_i`, then its public block product `C_T` is also a unit, so
`a_(i,T)=q_i/C_T` is public.

When `v_i intersection v_j=T`, the decorated star law cancels every common
block twice. Therefore

\[
Q(v_i\mathbin\triangle v_j)
=q_iq_jC_T^{-2}
=a_{i,T}a_{j,T}\pmod N.
\]

A proper F156 sign screen on this pair is exactly a proper signed-product
screen inside the `T` owner list. The general theorem finds a factor.

If the actual intersection is larger than `T`, the normalized product is not
the literal F156 star value. It is still a public unit scalar. A proper gcd
from it is still a correct factor. Hence the owner superset introduces no
false output.

Each record `i` occurs in exactly

\[
\sum_{k=0}^{\min(t,|v_i|)}\binom{|v_i|}{k}
\]

owner lists through intersection cap `t`. Thus `S_t` counts positions before
per-owner-list deduplication. Summing the `rn` normalization terms and the
post-normalization batch costs over all groups gives the stated soft-linear
dependence on `S_t`, up to coefficient and gcd costs. For `t=polylog(n)` and
an explicit quasipolynomial transcript, the binomial enumeration and every
batch remain quasipolynomial.

## 6. Frozen F157 consequence and boundary

The frozen F157 output lists 28 successful pairs with `C=1`. For such a pair,
the F156 star value is the uncorrected product `q_iq_j`. Therefore the empty
subset owner batch contains a useful signed product and must return a factor.

For basis pair `(656,10097)`, the frozen public certificate gives

\[
q_iq_j\equiv2{,}922{,}074{,}762\pmod N
\]

and

\[
\gcd(2{,}922{,}074{,}761,
3{,}241{,}632{,}473)=41{,}011.
\]

This proves the fixed-input locator corollary without a new experimental
run. The certificate came from the frozen registered output. The grouping
of its 65 serialized hit records is read-only analysis of that artifact.

The argument proves no collision-existence theorem. It also does not turn
the direct hits into a P108/P117 cross-layer normalized-root event. Equal
public `z` values have the same canonical inverse and the same exact product,
so their multiplicity disappears under global exact-value deduplication.
