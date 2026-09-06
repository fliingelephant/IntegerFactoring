# F152 statement-only blind reconstruction

## Protocol and verdict

I read only `STATEMENT.md` in the F152 directory before writing this file. I
did not read a proof, audit, manifest, ledger, or another F152 artifact.

The SHA-256 of the statement is

```text
db35d6381867052c876b69111c7b5409030e117501cccec2be12c45c8642a4e4
```

**Verdict: refuted as written, but repairable.** The decorated-group law, the
split-or-section equivalence, the online decoder, the abstract splitting, the
cross-layer disagreement map, formula (8), and the numerical certificate all
reconstruct. The material defect is that pairwise coprimality of the `q_j`
does not make their rational square classes independent. Consequently,
`ker A` need not be the complete integer-square dependency kernel. A one-row
transcript can factor `N` even when event 1 does not occur. The required repair
is to assume that

\[
v\longmapsto [Q(v)]\quad\text{from }\mathbf F_2^m
\text{ to }\mathbf Q^\times/(\mathbf Q^\times)^2
\]

is injective. Under the stated pairwise-coprimality condition, it is enough to
require every `q_j` to be a nonsquare. Alternatively, define the decoder
kernel as the kernel of this square-class map composed with `A`.

The statement also needs an explicit supplied-root deduplication rule. It is
not safe to discard a repeated value before comparing its supplied roots.

## 1. Decorated group

For bit vectors `v,w`, ordinary integer exponents give

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2. \tag{9}
\]

Thus, if `z^2=Q(v)` and `t^2=Q(w)` modulo `N`, then

\[
(ztC(v,w)^{-1})^2=Q(v+w),
\]

so the product is closed. For each coordinate, the bit identity

\[
vw+(v\mathbin\oplus w)u
=wu+v(w\mathbin\oplus u)
\]

proves

\[
C(v,w)C(v+w,u)=C(w,u)C(v,w+u).
\]

This is associativity. Symmetry of `C` gives commutativity. The identity is
`(0,1)`. Also,

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Because `N` is odd, `(0,-1)` is distinct from the identity. Hence the group
has exponent two.

The projection image is exactly `V_Q(N)`. Identity (9) shows that this image
is closed under addition, so it is an `F_2`-subspace. The projection kernel is

\[
\{(0,r):r^2=1\}=R_N,
\]

which proves exactness of (2). The inclusion of `R_N` is `r -> (0,r)`.
The two elements `(0,1)` and `(0,-1)` form `Delta`.

If `r^2=1 mod N`, every odd prime-power divisor of `N` divides exactly one of
`r-1` and `r+1`. Thus

\[
\gcd(r-1,N)\gcd(r+1,N)=N.
\]

When `r` is neither `1` nor `-1` modulo `N`, both gcds are strictly between
`1` and `N`. Claim (3) is correct.

## 2. Relation lift and normalized-root identity

Equation (4) gives

\[
(\alpha_i s_i^{-1})^2=Q(v_i)\pmod N,
\]

so every `g_i` is in `E_Q(N)`.

For `c in F_2^t`, put

\[
k_j(c)=\sum_i c_i v_{ij}
\]

as an ordinary integer, and let `epsilon_j` be its parity. Repeated use of the
group law gives

\[
G(c)=\left(A(c),
\frac{\prod_i\alpha_i^{c_i}}
{\prod_i s_i^{c_i}
 \prod_jq_j^{(k_j(c)-\epsilon_j)/2}}
\right). \tag{10}
\]

If `c in ker A`, define

\[
S(c)=\prod_i s_i^{c_i}\prod_jq_j^{k_j(c)/2},
\qquad
B(c)=\prod_i\alpha_i^{c_i}.
\]

Then, exactly over the integers,

\[
\prod_iT_i^{c_i}=S(c)^2,
\]

and the second coordinate in (10) is `B(c)S(c)^{-1}`. This is the standard
normalized root of the congruence `B(c)^2 = S(c)^2 mod N`. Reversing its
orientation has no effect: an element whose square is one is its own inverse.
This reconstructs the stated P66 root identity without relying on P66.

Therefore `G(ker A)` is exactly the image of the decoder restricted to the
formal parity dependencies `ker A`. It is not necessarily the image of the
complete integer-square decoder under the hypotheses in the statement.

Let

\[
\sigma:\mathbf F_2^m\longrightarrow
\mathbf Q^\times/(\mathbf Q^\times)^2,
\qquad \sigma(v)=[Q(v)].
\]

The complete integer-square dependency space is

\[
\ker(\sigma\circ A), \tag{11}
\]

not `ker A` unless `sigma` is injective.

### Counterexample under the stated hypotheses

Take

\[
N=15,\quad m=1,\quad q_1=4,
\]

and one relation

\[
v_1=1,\quad s_1=1,\quad T_1=4,\quad\alpha_1=7.
\]

All specified quantities are units modulo `15`, and `7^2 = 4 mod 15`.
The map `A` is the identity, so `ker A={0}` and `G(ker A)` contains only the
identity. Nevertheless, `T_1=2^2` is already an integer square. Its normalized
root is

\[
7\cdot2^{-1}=11\pmod {15},
\]

and

\[
11^2=1\pmod {15},\qquad
\gcd(11-1,15)=5,\qquad
\gcd(11+1,15)=3.
\]

Thus the complete decoder factors `15`, while event 1 of the stated theorem
does not occur. This refutes the word "complete" and the corresponding
no-factor interpretation as written.

Pairwise-coprime `q_j` have disjoint prime supports. Hence `sigma` is
injective exactly when no `q_j` is a perfect square. This gives a small repair
that preserves all later formulas.

## 3. Exact split-or-section equivalence

Define the homomorphism

\[
L:\mathbf F_2^t\longrightarrow \overline E_Q(N),
\qquad L(c)=G(c)\Delta.
\]

It satisfies `overline pi o L=A`. Event 1 fails exactly when

\[
G(c)\in\Delta\quad\text{for all }c\in\ker A,
\]

or equivalently `ker A` is contained in `ker L`. In that case `L` factors
uniquely through

\[
\mathbf F_2^t/\ker A\simeq W.
\]

The resulting map is

\[
h(A(c))=L(c). \tag{12}
\]

It is a homomorphism, sends each `v_i` to `g_i Delta`, and its composite with
the projection is the identity on `W`. Conversely, any `h` with those values
forces `L(c)=1` for every `c in ker A`, so event 1 cannot occur. The generators
`v_i` make `h` unique. This proves that the two formal events are exclusive
and exhaustive.

This equivalence itself does not require square-class independence. That
hypothesis is required only to identify its first event with every available
integer-square decoding dependency.

## 4. Online form and abstract sections

Maintain a row-echelon basis of observed parity vectors and one representative
in `E_Q(N)` for each basis lift. For a new `(v,z)`:

1. If `v` is independent, append it and its lift.
2. If `v` is dependent, solve for its basis coefficients and multiply the
   corresponding stored lifts to obtain an old lift `e`.
3. The product `(v,z) star e` is `(0,r)` with `r^2=1`. If `r` is not `+1` or
   `-1`, the two gcds factor `N`. Otherwise the two lifts agree in the
   quotient by `Delta`.

Gaussian elimination over `F_2` and modular multiplication, inversion, and
gcd computation are polynomial in the total encoded transcript size. The
runtime claim is correct in that encoding model.

Every group in (2) is an `F_2`-vector space. Choose a basis of `V_Q(N)`, choose
one lift of each basis vector, and extend by products. This gives an abstract
full section. The section is noncanonical, but it always exists. Therefore a
section cannot itself contradict the parity data. That conclusion is correct.

## 5. Cross-layer disagreement map

Let the two relation maps be `(A_F,G_F)` and `(A_A,G_A)`. The pure no-factor
assumptions give sections `h_F` and `h_A`. A dependency in the union is a pair
`(c_F,c_A)` such that

\[
A_F(c_F)+A_A(c_A)=0.
\]

In characteristic two this means that both sides equal some

\[
u\in W_F\cap W_A.
\]

Modulo `Delta`, its normalized root is

\[
G_F(c_F)G_A(c_A)\Delta=h_F(u)h_A(u). \tag{13}
\]

The right side lies in the kernel `R_N/{+/-1}` and is independent of the
chosen preimages because pure dependencies vanish in the quotient. Conversely,
every `u` in the intersection has preimages in both layers. Hence the image
of all union dependencies modulo global sign is exactly the image of

\[
\delta(u)=h_F(u)h_A(u).
\]

The union contains a non-global normalized root exactly when `delta` is
nonzero, which is exactly when the two sections disagree somewhere on their
intersection. This reconstructs (7) and the stated P108 interpretation
without using P108.

## 6. Same-parity specialization

For two rows with the same parity vector `v`, let `d=Q(v)` and

\[
T_i=d s_i^2,\qquad T_j=d s_j^2.
\]

Because `C(v,v)=Q(v)=d`, their product in the decorated group has root

\[
r=\frac{\alpha_i\alpha_j}{d s_i s_j}. \tag{14}
\]

Using `alpha_j^2=d s_j^2 mod N`,

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}
=\frac{\alpha_i s_j}{\alpha_j s_i}\pmod N. \tag{15}
\]

Also `r^2=1`. Thus (8) is correct and is the two-row specialization of the
section-disagreement map. The historical P134 label was not needed for this
derivation.

## 7. The `N=2773` certificate

The arithmetic checks directly:

\[
47\cdot59=2773,
\]

\[
3\cdot43^2=5547=1+2\cdot2773,
\]

and

\[
3\cdot842^2=2,126,892=1+767\cdot2773.
\]

Thus `alpha_1=alpha_2=1` are supplied modular roots. All denominators in the
decorated lifts are units. Formula (14) initially gives the inverse of
`3*43*842`; the inverse is the same residue because that residue squares to
one. Indeed,

\[
3\cdot43\cdot842=108,618=39\cdot2773+471,
\]

\[
471^2=80\cdot2773+1.
\]

Moreover,

\[
471=1\pmod {47},\qquad 471=-1\pmod {59},
\]

so

\[
\gcd(471-1,2773)=47,
\qquad
\gcd(471+1,2773)=59.
\]

The numerical certificate is valid. It has minimum support size for a
nontrivial same-nonzero-parity disagreement: one needs two rows. If the word
"smallest" instead asserts numerical minimality, that assertion is not
supported by the statement. The P101 provenance is historical metadata and
cannot be checked in a statement-only reconstruction.

## 8. Supplied roots and deduplication

The supplied modular root is part of a relation. It cannot be reconstructed
from `T` without choosing among CRT roots, and different choices can be the
entire factoring signal.

Suppose two records have the same exact value `T` and supplied roots `alpha`
and `beta`. Then

\[
r=\alpha\beta^{-1},\qquad r^2=1\pmod N.
\]

There are only two safe outcomes before one record is discarded:

* If `r=+1` or `r=-1`, the roots agree modulo global sign. Their decorated
  information is redundant, subject also to retaining the intended layer
  membership metadata.
* If `r` is not global, the repeated value already factors `N` through the
  two gcds. Discarding either root first loses the certificate.

More generally, records with the same parity vector must not be deduplicated
by parity. Their decorated-lift quotient is precisely (14), the disagreement
that the theorem is designed to find. A safe algebraic deduplication key is
the decorated coset `g_i Delta`, not `v_i` and not bare `T_i`. For bare-value
deduplication, compare the supplied roots first and emit a factor on
non-global disagreement.

Global deduplication across named layers also needs a membership rule. If one
physical record belongs to both source mechanisms, collapsing it to one row
is algebraically harmless only after the root comparison, but its membership
must remain attached to both mechanisms if `W_F`, `W_A`, and their sections
are meant to describe those mechanisms. Otherwise global deduplication can
change the stated layer spans and makes (7) a statement about a different
pair of layers. The cross-layer theorem itself does not require deduplication.

## 9. Quasipolynomial scope

The online decoder is polynomial in an already explicit transcript. Hence it
is quasipolynomial in the input length if the row count, parity dimension,
integer bit lengths, exact factorizations, and supplied roots are all produced
within quasipolynomial resources. This is a conditional decoder bound. It
does not generate those relations or guarantee a disagreement, so it is not
an end-to-end factoring algorithm.

The limitation on projection-only arguments is valid. Given any parity set
inside `V_Q(N)`, an abstract section can assign mutually compatible decorated
lifts to all its vectors. Thus doubling, circuit, or row-reuse facts about the
projection alone cannot logically force a non-global root. A source theorem
must add information that prevents the observed lift map from factoring
through parity modulo global sign, or it must derive a separate contradiction
from the existence of a common section.

The proposed quasipolynomial source theorem is therefore a precise remaining
research target, not a consequence of the structural result. With the
square-class independence repair and the supplied-root deduplication rule,
the claimed structural scope is correct.
