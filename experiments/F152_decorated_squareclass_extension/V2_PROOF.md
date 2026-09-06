# Proof of the F152 V2 decorated-squareclass theorem

## 1. Exact square-class independence

Because the positive integers `q_j` are pairwise coprime, their rational-prime
supports are disjoint. Each `q_j` is a nonsquare, so some prime occurs in it
to an odd exponent. That prime occurs in no other `q_k`. Therefore every
nonempty product

\[
\prod_jq_j^{v_j}
\]

has a prime with an odd exponent and is not an integer or rational square.
Thus the square-class map `sigma` in (1) is injective. The converse is also
immediate: if some `q_j` is a square, its basis vector is in the kernel of
`sigma`. This proves the stated equivalence under pairwise coprimality.

## 2. The group law

For bit vectors `v,w`, exact integer multiplication gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\tag{25}
\]

All `q_j` are units modulo `N`, so (4) is defined. If
`z^2=Q(v)` and `t^2=Q(w)`, then (25) shows that the second coordinate of
their product squares to `Q(v+w)`. Thus the set is closed.

For bits `a,b,c`, with addition in `F_2`,

\[
ab+(a\mathbin{\mathsf{xor}}b)c
=bc+a(b\mathbin{\mathsf{xor}}c).
\]

Coordinatewise, this gives the cocycle identity

\[
C(u,v)C(u+v,w)=C(v,w)C(u,v+w).
\]

Hence (4) is associative. Symmetry of `C` gives commutativity. The identity
is `(0,1)`. Since `C(v,v)=Q(v)`,

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Every element is its own inverse. Closure also shows that `V_Q(N)` is a
subspace. The kernel of the projection consists exactly of the pairs `(0,r)`
with `r^2=1`, which proves (6).

If `r^2=1 mod N` but `r` is not `+1` or `-1 mod N`, every odd prime-power
divisor of `N` divides exactly one of `r-1` and `r+1`. Both sign sets are
nonempty. Hence both gcds in (9) are strictly between `1` and `N`.

## 3. Root-aware exact-value deduplication

Suppose two records have the same exact positive value and coordinates

\[
T=s^2Q(v)=t^2Q(w).
\]

Using (25), the exact equality implies

\[
Q(v+w)=\left(\frac{tQ(w)}{sC(v,w)}\right)^2.
\]

Thus `Q(v+w)` is a rational square. Injectivity of `sigma` gives `v=w`.
Positivity then gives `s=t`.

Let their supplied roots be `alpha,beta`. Their ratio

\[
r=\alpha\beta^{-1}\pmod N
\]

satisfies `r^2=1`. If it is non-global, Section 2 factors `N`. If it is
global, the two decorated lifts `(v,alpha/s)` and `(v,beta/s)` have the same
class modulo `Delta`.

Keeping both such root-equivalent records adds only the binary dependency
formed by their pair, and its normalized root is global. Any dependency that
uses both can delete the pair without changing its useful normalized-root
class. Any dependency that uses one is represented by the retained copy.
Therefore removing one algebraic copy preserves the normalized-root image
modulo global sign.

The occurrence and layer labels are not algebraic factors and must not be
removed. Attach their union to the retained record. A conceptual layer may
continue to use the record whenever one of its original occurrences belonged
to that layer. If the two named layers both use it, their two conceptual
copies differ only by the global kernel direction just described. Identifying
those copies does not change the useful cross-layer root image. Thus
root-aware deduplication preserves both factor detection and source
provenance.

Equal parity alone does not imply equal decorated class. Such records must
remain available for the comparison in (20).

## 4. Relation lifts and the complete normalized-root image

Equation (11) gives

\[
(\alpha_i s_i^{-1})^2\equiv Q(v_i)\pmod N,
\]

so (12) lies in `E_Q(N)`.

For an arbitrary selector `c`, put

\[
d_j=\sum_i c_i(v_i)_j
\]

as an ordinary nonnegative integer. The rational square class of the exact
selected product is

\[
\left[\prod_iT_i^{c_i}\right]
=\left[Q(A(c))\right]
=\sigma(A(c)).
\]

The selected product is an integer square if and only if its rational square
class is trivial. Injectivity of `sigma` makes this equivalent to `A(c)=0`.
This proves (14), including its converse.

Now fix `c in ker A`. Every `d_j` is even. The exact positive root of the
selected integer product is

\[
R(c)=\left(\prod_i s_i^{c_i}\right)
      \left(\prod_jq_j^{d_j/2}\right).
\tag{26}
\]

Repeated use of (4) divides the product of second coordinates by exactly
`prod_j q_j^(d_j/2)`. Therefore the second coordinate of `G(c)` is

\[
\frac{\prod_i\alpha_i^{c_i}}{R(c)}.
\tag{27}
\]

Its square is one. A square root of one is its own inverse, so (27) is also
`R(c)/(prod_i alpha_i^c_i)`, the P66 normalized root. Equation (14) shows
that no integer-square dependency lies outside `ker A`. This proves the
complete decoder identification in (15).

## 5. Split or section

Assume first that every element of `G(ker A)` lies in `Delta`. Define

\[
h(Ac)=\overline{G(c)}.
\]

If `Ac=Ac'`, then `c+c'` is in `ker A`, so
`G(c)G(c')` is in `Delta`. Hence the two quotient classes agree and `h` is
well-defined. It is a homomorphism because `G` is one. Its projection is
`Ac`, and it sends every `v_i` to `bar g_i`. Since the `v_i` span `W`, these
values make `h` unique.

Conversely, if such an `h` exists, then for every `c in ker A`,
`bar G(c)=h(0)` is the identity. Thus `G(c)` is in `Delta`. Therefore failure
of (17) is exactly the existence of a non-global normalized root, and (9)
factors `N`.

The online algorithm is Gaussian elimination on the `v_i`. When a new vector
is dependent, the stored basis expression gives a comparison lift. Their
group quotient has parity coordinate zero. Equality up to global sign is a
direct modular comparison. Otherwise Section 2 applies. All group
operations, comparisons, gcds, and elimination steps are polynomial in the
explicit input length.

Finally, (6) is a short exact sequence of finite-dimensional vector spaces
over a field. Choose a basis of `V_Q(N)`, choose any lift of each basis
vector, and extend linearly. This proves that an abstract full section always
exists. It need not be computable from bare `N` without supplied lifts, but
its existence blocks a contradiction based only on parity-space structure.

## 6. Two named layers

For a pure layer whose normalized-root image is global, Section 5 gives a
section on its parity span. Let `u in W_F intersect W_A`, and choose
coefficient vectors `c_F,c_A` that represent `u` in the two named layers.
Their union is a parity dependency. Its decorated product modulo `Delta` is

\[
h_F(u)h_A(u).
\]

Changing either representation multiplies the corresponding lift by a pure
kernel element, which is global and disappears in the quotient. Thus (18) is
well-defined. It is a homomorphism. Every cross dependency gives one such
intersection vector, and every intersection vector gives a cross dependency.
Therefore its image is exactly the induced cross normalized-root image from
P108. Root-equivalent shared records contribute only the zero element of this
image, as proved in Section 3; their retained membership labels keep both
named spans correct.

When two objects have the same parity vector, their product has parity zero.
For (19), formula (4) divides their two lift coordinates by
`C(v_i,v_i)=Q(v_i)=d`, giving

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}.
\]

Using `alpha_i^2=d*s_i^2 mod N` and
`alpha_j^2=d*s_j^2 mod N` converts this to either cross-ratio form in (20).
This is exactly P134.

## 7. Two-row illustration

The displayed integer factorizations are direct. Their product is

\[
T_1T_2=(3\cdot43\cdot842)^2.
\]

Also `108618=471 mod 2773`, and

\[
471^2-1=47\cdot59\cdot80.
\]

Thus the two gcds are `47` and `59`, as stated.

## 8. Scope

This proof constructs no relation source. It does not show that a canonical
inverse, feedback, torus, or high-order family violates a common section. It
does not turn algorithmic PFR into a factoring algorithm. It isolates the
additional datum that any such source theorem must control: the decorated
lift, not only its parity projection.
