# Proof of F163

## 1. The generated decorated subgroup

P138 proves that `E_Q(N)` is an elementary abelian group and that its
projection kernel is `R_N`. Quotienting by the two global signs gives (1),
with kernel `K=R_N/Delta`.

Let `H=<A>`. Binary elimination on the public parity coordinates of `A`
keeps the matching decorated products. A parity dependency produces an
element of `H intersect K`. If that class is nonzero, any representative is
a square root of one that is not globally `+1` or `-1`. The two standard
gcds factor `N`.

Assume this does not occur. Then

\[
\ker(\pi|_H)=H\cap K=0.
\]

The map `pi|_H` is injective by this equality and surjective onto
`W=pi(H)` by definition. Hence it is an isomorphism. During the same
elimination, retain one decorated product for every parity-basis vector.
For a public coordinate expression of `v in W`, multiply those retained
lifts. This computes the inverse `h` in (3). Therefore the isomorphism and
the section are public, not only abstract.

The root-aware deduplication condition is essential. Two equal exact values
with non-global root quotient already give a nonzero element of `K`. If their
quotient is global, identifying them in `overline E` is valid and preserves
the argument. Parity-only deduplication could delete the kernel witness.

## 2. Exact preservation of additive structure

For every `k >= 1`, homomorphism gives

\[
\pi(kA)=k\pi(A).
\]

Both sets lie in `H` and `W`, respectively. Since `pi|_H` is injective, its
restriction from `kA` to `k pi(A)` is a bijection. This proves (4).

The same argument applies to every equality between two additive words. An
equality upstairs projects to one downstairs. An equality downstairs has a
difference in `ker(pi|_H)=0`, so it lifts to an equality upstairs. Additive
energy counts such equalities, so it is preserved. An affine subspace or a
coset cover inside `W` lifts through the linear isomorphism `h`; every such
object inside `H` projects through `pi`. If an ambient cover is used, its
intersection with `H` is the only part that controls `A`. Thus any intrinsic
PFR conclusion expressed by additive relations, subspaces, affine subspaces,
or their cosets contains no information beyond the parity projection on this
branch.

## 3. Both doubling regimes inside one graph

For `B_1={h(0),h(e_1),...,h(e_d)}`, a sum is either zero, one basis vector,
or a sum of two distinct basis vectors. These vectors are all distinct, so
(5) follows. The basis elements already span `W`, hence `B_1` already
generates `h(W)`.

Every vector of weight at most `s+t` can partition its support into two
sets of sizes at most `s` and `t`. Conversely, the sum of vectors of weights
at most `s` and `t` has weight at most `s+t`. This proves (6), with the
obvious cap at `d`. All these sets remain subsets of `h(W)`, whose projection
kernel is zero.

For a subspace `U`, linearity gives

\[
h(U)+h(U)=h(U).
\]

For `u notin U`,

\[
h(u+U)+h(u+U)=h(U)
\]

because `2u=0`. Both equalities preserve cardinality. This proves the
doubling-one statements.

The generated subgroup is unchanged through every Hamming-ball doubling.
Therefore cardinality growth is not subgroup growth. Full enumeration can
be too large, while a compact basis is precisely the public section already
known. This proves the non-potential claim.

## 4. Exact canonical-inverse section-completion realization

Choose `p,q,a_p,a_q` as in the statement. Each CRT class `c_j` is coprime to
`N`. Dirichlet's theorem on primes in arithmetic progressions supplies a
prime in that class, and finitely many choices can be made distinct. Hence
the `ell_j` are distinct primes. In particular, they are pairwise coprime
nonsquares and units modulo `N`.

The CRT definition (9) and the congruences (8) give

\[
z_j^2\equiv\ell_j\pmod p,
\qquad
z_j^2\equiv\ell_j\pmod q,
\]

and therefore modulo `N`. Thus `(e_j,z_j)` is a legal decorated lift. Since
the parity vectors `e_j` are independent, their generated subgroup projects
injectively onto `F_2^d`; it is a section graph.

For `v`, multiplication in `E_Q(N)` gives a root `z_v` of

\[
Q(v)=\prod_j\ell_j^{v_j}.
\]

Since `s_v z_v = 1 mod N`, equation (10) satisfies

\[
T_v=s_v^2Q(v)\equiv s_v^2z_v^2\equiv1\pmod N.
\]

The supplied root `alpha_v=1` is legal. Its decorated second coordinate is

\[
\alpha_vs_v^{-1}\equiv z_v\pmod N,
\]

so the record realizes `h(v)` exactly. A dependency in a section graph has
decorated product equal to the identity modulo `Delta`, hence its normalized
root is global.

For nonzero `v`, let `k=k(v)`. Modulo `p`,

\[
Q(v)\equiv a_p^{2k}.
\]

The inequalities

\[
0<2k\le2(2^d-1)<\frac{p-1}{2}
\]

show that this residue is neither `1=a_p^0` nor
`-1=a_p^((p-1)/2)`. The same proof applies modulo `q`. Hence neither
`Q(v)-1` nor `Q(v)+1` is divisible by `p` or `q`.

Finally,

\[
z_v-s_v\equiv s_v(z_v^2-1)\pmod N,
\qquad
z_v+s_v\equiv s_v(z_v^2+1)\pmod N,
\]

and `s_v` is a unit. This proves both gcd identities and the null value in
(11).

The values are P142 completion records built from canonical inverse
endpoints. They are not asserted to be raw products `z_v iota_N(z_v)`. The
construction also depends on chosen hidden factors and primitive roots. It is
therefore a realizability countermodel to a structural implication, not a
uniform source from bare `N`.

## 5. Boundary

The proof uses only the additive group `overline E`, its parity projection,
and the supplied decorated lifts. It makes no claim about data outside that
group. Integer gcd refinement can distinguish two presentations that map to
the same decorated element. Carries and sizes are not homomorphism invariants
of (1). Provenance can select another source rule. A second rule can choose a
different section on an overlapping parity span. These are exactly the
places where a PFR-guided retry could be materially new.

Absent one such extra arithmetic hypothesis, the proposed Babai-style
alternative

\[
\text{large doubling gives progress}
\quad\text{or}\quad
\text{small doubling gives useful structure}
\]

has two root-global branches. Neither branch forces a factor.
