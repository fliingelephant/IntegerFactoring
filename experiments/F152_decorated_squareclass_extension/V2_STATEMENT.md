# F152 V2 — decorated square classes give an exact split-or-section law

**Status:** repaired proof-only candidate. This is a structural theorem for
the many-relation decoder. It is not a source theorem and not a factoring
algorithm. V1 passed hostile audit but failed statement-only reconstruction
because it did not require square-class independence and did not state a
supplied-root-aware deduplication rule.

## Closest prior results and the material difference

P66 computes the complete square-class kernel and its normalized-root image.
P108 identifies cross-layer dependencies. P129 packages squared-anchor
relations as bridge cycles. P134 gives the same-squareclass two-cycle
cross-ratio decoder.

The result below does not add another scalar identity. It puts every parity
class together with its supplied modular square root in one public abelian
group. In that group, a failed decoder has an exact positive meaning: the
observed lifts form a homomorphic section over their generated parity span.
A later relation must extend this section, agree with it, or disagree with it
and factor `N`. This makes the proposed Babai/PFR-style
"split or enter structure" branch precise. It also proves that parity
structure alone cannot finish the route, because the underlying vector-space
extension always has abstract sections.

## 1. The decorated squareclass group

Let `N >= 3` be odd. Let `q_1,...,q_m` be pairwise-coprime positive
integers, all units modulo `N`, and require every `q_j` to be a nonsquare.
Equivalently, under pairwise coprimality, require the exact square-class map

\[
\sigma:\mathbf F_2^m\longrightarrow
\mathbf Q^\times/(\mathbf Q^\times)^2,
\qquad
\sigma(v)=[Q(v)]
\tag{1}
\]

to be injective. For `v in F_2^m`, put

\[
Q(v)=\prod_{j=1}^m q_j^{v_j},
\qquad
C(v,w)=\prod_{j=1}^m q_j^{v_jw_j}.
\tag{2}
\]

Let

\[
E_Q(N)=
\left\{(v,z):v\in\mathbf F_2^m,
z\in(\mathbf Z/N\mathbf Z)^\times,
z^2\equiv Q(v)\pmod N\right\}.
\tag{3}
\]

Define

\[
(v,z)\star(w,t)
=
\left(v+w,zt\,C(v,w)^{-1}\right).
\tag{4}
\]

Then `E_Q(N)` is an abelian group of exponent two. Its projection image

\[
V_Q(N)=\{v:Q(v)\text{ is a square modulo }N\}
\tag{5}
\]

is an `F_2`-subspace, and there is an exact sequence

\[
0\longrightarrow R_N\longrightarrow E_Q(N)
\overset{\pi}{\longrightarrow}V_Q(N)\longrightarrow0,
\tag{6}
\]

where

\[
R_N=\{r\in(\mathbf Z/N\mathbf Z)^\times:r^2=1\}.
\tag{7}
\]

The two global roots form

\[
\Delta=\{(0,1),(0,-1)\}\le E_Q(N).
\tag{8}
\]

A kernel element outside `Delta` gives proper factors through

\[
\gcd(r-1,N),\qquad \gcd(r+1,N).
\tag{9}
\]

## 2. Supplied-root-aware deduplication

A relation record includes its exact positive unit value `T`, its supplied
unit root `alpha mod N`, its factor-free coordinates, its occurrence identity,
and all named source-layer memberships. The unit conditions also follow from
the factorizations in Section 3.

For two records with the same exact value, square-class independence forces
their `v` and positive `s` coordinates to agree. Therefore their decorated
lift quotient is the quotient of their supplied roots. Before discarding
either record, put

\[
r=\alpha\beta^{-1}\pmod N.
\tag{10}
\]

Then `r^2=1 mod N`.

* If `r` is not `+1` or `-1`, (9) factors `N` immediately.
* If `r=+1` or `r=-1`, the records have the same decorated lift modulo
  `Delta`. One algebraic copy can be discarded, but the retained record must
  keep the union of all occurrence identities and source-layer memberships.

Do not deduplicate records only by parity vector. Equal-parity records can
have different decorated lifts, and that disagreement is the signal studied
below. This root-aware rule preserves the useful normalized-root image modulo
global sign. It also preserves the named layer spans and their provenance.

## 3. Exact relation values embed in the group

Suppose the retained explicit relation list has exact factorizations

\[
T_i=s_i^2Q(v_i),
\qquad
\alpha_i^2\equiv T_i\pmod N,
\tag{11}
\]

where every `s_i` and `alpha_i` is a unit modulo `N`. Define its decorated
lift

\[
g_i=(v_i,\alpha_i s_i^{-1})\in E_Q(N).
\tag{12}
\]

Let

\[
A:\mathbf F_2^t\to\mathbf F_2^m,
\qquad
A(c)=\sum_i c_iv_i,
\tag{13}
\]

and let `G(c)` be the `star`-product of the selected `g_i`.
Square-class independence gives the exact equivalence

\[
A(c)=0
\quad\Longleftrightarrow\quad
\prod_iT_i^{c_i}\text{ is an integer square}.
\tag{14}
\]

For every `c in ker A`, the second coordinate of `G(c)` is exactly the P66
normalized root of the integer square in (14), up to the irrelevant
inversion of a square root of one. Therefore

\[
G(\ker A)\subseteq R_N
\tag{15}
\]

is exactly the normalized-root image of the complete factor-free decoder.

## 4. Exact split-or-section theorem

Put

\[
\overline E_Q(N)=E_Q(N)/\Delta.
\tag{16}
\]

For any explicit list (11), exactly one of these events occurs:

1. `G(ker A)` contains a non-global root, and (9) factors `N`.
2. There is a unique homomorphism on the generated parity span
   `W=im A`,

   \[
   h:W\longrightarrow\overline E_Q(N),
   \qquad
   \overline\pi\circ h=\operatorname{id}_W,
   \qquad
   h(v_i)=\overline g_i.
   \tag{17}
   \]

Thus every no-factor transcript supplies a public homomorphic section over
its observed parity span.

There is an online form. Keep a parity basis and one decorated lift for each
basis vector. For a new `g=(v,z)`:

* if `v` is not in `W`, extend the basis and the section;
* if `v` is in `W`, reconstruct the old lift of `v`;
* if the two lifts differ outside global sign, their quotient is a
  non-global root and factors `N`;
* otherwise the new lift agrees with the existing section.

The work is polynomial in the explicit transcript length. It is therefore
quasipolynomial for an explicit quasipolynomial source.

The sequence (6) is a sequence of `F_2`-vector spaces. It always admits an
abstract full section. Consequently, the existence of a section is not
itself a contradiction. A source theorem must force two public source
mechanisms to choose incompatible lifts of the same parity span.

## 5. Cross layers are section disagreements

Let two named relation layers share the common root-aware retained source.
Use the preserved membership metadata to form their parity spans `W_F,W_A`.
Assume each pure layer has only global normalized roots. Let `h_F,h_A` be
their sections from (17). Then the induced cross-layer normalized-root map is

\[
u\longmapsto h_F(u)h_A(u)
\quad
(u\in W_F\cap W_A),
\tag{18}
\]

viewed in `R_N/{+1,-1}`. The union has a useful cross dependency exactly
when `h_F` and `h_A` disagree on their intersection. This is the section
form of P108.

For two relations in the same parity class, (18) is their lift quotient.
P134 is the feedback-cycle specialization: if

\[
T_i=d s_i^2,\qquad T_j=d s_j^2,
\qquad d=Q(v_i)=Q(v_j),
\tag{19}
\]

the disagreement root is

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}
=
\frac{\alpha_i s_j}{\alpha_j s_i}
\pmod N.
\tag{20}
\]

## 6. Exact two-row illustration

At

\[
N=2773=47\cdot59,
\tag{21}
\]

take

\[
T_1=5547=3\cdot43^2=1+2N,
\qquad
T_2=2{,}126{,}892=3\cdot842^2=1+767N,
\tag{22}
\]

with supplied roots `alpha_1=alpha_2=1`. Both values project to the same
one-dimensional rational square class `[3]`. Their decorated lifts disagree:

\[
R=3\cdot43\cdot842=108{,}618\equiv471\pmod N,
\qquad
R^2\equiv1\pmod N,
\tag{23}
\]

and

\[
\gcd(R-1,N)=47,
\qquad
\gcd(R+1,N)=59.
\tag{24}
\]

This is the earlier P101 certificate, now interpreted as a two-row section
disagreement. It is an illustration, not new empirical evidence.

## 7. Precise remaining quasipolynomial problem

The parity/PFR branch can compress the projection set `{v_i}`, but it cannot
by itself force a factor. The missing source theorem is:

> In quasipolynomial work, generate two canonical relation families whose
> decorated sections must disagree on a shared parity vector, or prove that a
> common section forces a separate public restriction that cannot persist.

Equivalently, a useful source must force nonlinearity of the lifted relation
map modulo global sign. Large doubling, small doubling, many parity circuits,
and high row reuse are not enough without this lift inconsistency.
