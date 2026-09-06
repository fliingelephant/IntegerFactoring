# F152 V2 statement-only blind reconstruction

## Scope and input integrity

This reconstruction uses only `V2_STATEMENT.md`. I did not use another F152
artifact, a proof, a V1 artifact, an audit, a manifest, or a ledger.

The SHA-256 digest of the statement used here is

```text
3f5b232d6bdeb9ca6a70cecd2bdfc0e1307406de3f84a23c953c59323fcfc78e
```

## Verdict

**PASS, with one scope/wording qualification.** All algebraic claims in
Sections 1--6 reconstruct from the definitions. The exact kernel identity,
the split-or-section dichotomy, its online algorithm, the layer-disagreement
criterion, the cross-ratio identity, and the numerical certificate are
correct.

The qualification concerns only the prose form of the source boundary. What
is mathematically necessary is failure of the observed decorated lifts to
factor through parity modulo global sign. Two named source families are one
way to force that failure, but they are not the only logical presentation: a
single family can already contain a useful parity circuit. The final
"equivalently" formulation in Section 7, which requires lift nonlinearity, is
the precise general statement. This does not affect the theorem.

The names P66, P108, P101, and P134 are treated only as labels in this blind
reconstruction. The identities attributed to them are verified below. Their
historical equivalence to artifacts not in scope is not independently
checked.

## 1. Rational square-class independence

Write the prime factorization of each positive integer `q_j` as

\[
q_j=\prod_p p^{e_{j,p}}.
\]

If `q_j` is not an integer square, it has a prime `p_j` for which
`e_{j,p_j}` is odd. Pairwise coprimality makes the prime supports of distinct
`q_j` disjoint. Thus, for every nonzero `v`, choose an index `j` with
`v_j=1` and an odd-valuation prime `p_j` of `q_j`. Then

\[
\nu_{p_j}(Q(v))=e_{j,p_j}
\]

is odd. No other selected `q_k` changes this valuation. Hence `Q(v)` is not a
rational square. Therefore `sigma(v)` is trivial only for `v=0`, and `sigma`
is injective.

Conversely, injectivity makes every singleton image `sigma(e_j)=[q_j]`
nontrivial, so every `q_j` is a nonsquare. This proves the stated equivalence
under pairwise coprimality.

There is also a useful exact identity:

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2. \tag{R1}
\]

Here and below vector addition is in `F_2^m`. Identity (R1) proves directly
that `sigma` is a homomorphism.

## 2. The decorated group and exact sequence

### Closure

Let `(v,z)` and `(w,t)` lie in `E_Q(N)`. Since all `q_j` are units modulo
`N`, `C(v,w)` is invertible. By (R1),

\[
\left(ztC(v,w)^{-1}\right)^2
\equiv Q(v)Q(w)C(v,w)^{-2}
\equiv Q(v+w)\pmod N.
\]

Thus the product in the statement remains in `E_Q(N)`.

### Associativity and commutativity

The required cocycle identity is

\[
C(v,w)C(v+w,u)=C(w,u)C(v,w+u). \tag{R2}
\]

For one coordinate with bits `a,b,c`, the exponent on both sides is

\[
ab+ac+bc-2abc.
\]

So (R2) holds coordinate by coordinate. It proves associativity. Symmetry of
`C(v,w)` proves commutativity.

The identity is `(0,1)`. Also,

\[
(v,z)\star(v,z)
=\left(0,z^2C(v,v)^{-1}\right)
=\left(0,Q(v)Q(v)^{-1}\right)
=(0,1),
\]

because `C(v,v)=Q(v)`. Hence every element is its own inverse and `E_Q(N)`
is an abelian group of exponent two.

### Projection and kernel

Closure shows that the set of first coordinates is closed under addition.
It contains zero. Thus `V_Q(N)` is an `F_2`-subspace. The projection is a
surjective homomorphism onto this subspace. Its kernel consists exactly of

\[
(0,r),\qquad r^2\equiv1\pmod N.
\]

After the natural identification `r -> (0,r)`, this kernel is `R_N`. This
proves exactness of (6).

Since `N` is odd, `1` and `-1` are distinct. They give the subgroup `Delta`.

### Why a non-global root factors `N`

If `r^2=1 mod N`, then `N` divides `(r-1)(r+1)`. Also

\[
\gcd(r-1,r+1)\mid2.
\]

No odd prime can therefore divide both factors. Each full prime power in
`N` divides exactly one of them. If `gcd(r-1,N)=1`, all prime powers in `N`
divide `r+1`, so `r=-1 mod N`. Similarly, `gcd(r+1,N)=1` implies
`r=1 mod N`. A root that is neither global sign therefore makes both gcds
strictly between `1` and `N`. Both are proper nontrivial factors. This proves
(9), including the nonsquarefree case.

## 3. Supplied-root-aware deduplication

Suppose two records have

\[
T=s^2Q(v)=t^2Q(w)
\]

with positive `s,t`. In rational square classes,

\[
1=[T/T]=[Q(v)/Q(w)]=\sigma(v+w).
\]

Injectivity of `sigma` gives `v=w`. Exact equality then gives `s^2=t^2`, and
positivity gives `s=t`.

Let the supplied roots be `alpha` and `beta`. The product, equivalently the
quotient because the group has exponent two, of their decorated lifts is

\[
\begin{aligned}
(v,\alpha s^{-1})\star(v,\beta s^{-1})
&=\left(0,\frac{\alpha\beta}{s^2Q(v)}\right)\\
&=\left(0,\frac{\alpha\beta}{T}\right)
=\left(0,\alpha\beta^{-1}\right),
\end{aligned} \tag{R3}
\]

where `beta^2=T mod N` was used in the last step. Thus the proposed check
`r=alpha beta^{-1}` is exactly the decorated-lift comparison.

If `r` is non-global, Section 2 gives a factor. If `r` is a global sign, the
two columns are equal in `E_Q(N)/Delta`. Removing one column then removes
only a redundant copy in the quotient. A coefficient vector that used both
copies contributes zero parity and a global sign, so it cannot carry a
useful normalized root. Any coefficient vector that used one copy can use
the retained copy, with at most a global-sign change.

Consequently, this deduplication preserves the normalized-root image modulo
global sign. Assigning the retained record the union of the layer
memberships preserves each named parity span. Keeping all occurrence
identities preserves provenance. These conclusions would be false for
parity-only deduplication: two records with the same `v` need not have the
same coset in `E_Q(N)/Delta`.

## 4. Complete parity kernel and normalized-root image

For `c in F_2^t`, define the ordinary integer counts

\[
n_j(c)=\sum_i c_i(v_i)_j
\]

and let `a_j=n_j mod 2`, so `a=A(c)`. Put

\[
D(c)=
\prod_i s_i^{c_i}
\prod_j q_j^{(n_j-a_j)/2}. \tag{R4}
\]

The exact product of relation values is

\[
\prod_iT_i^{c_i}=D(c)^2Q(A(c)). \tag{R5}
\]

This follows by separating every exponent `n_j` into its parity bit `a_j`
and its even part.

If `A(c)=0`, (R5) is the integer square `D(c)^2`. Conversely, if the left
side is an integer square, then its rational square class is trivial. Its
class is `sigma(A(c))`, so injectivity gives `A(c)=0`. This reconstructs the
equivalence (14) in both directions.

Repeated use of the star law gives the companion decorated identity

\[
G(c)=
\left(A(c),\frac{\prod_i\alpha_i^{c_i}}{D(c)}\right). \tag{R6}
\]

The correction exponent introduced by the star product in coordinate `j`
is `(n_j-a_j)/2`, exactly the exponent in (R4). This proves (R6) either by
induction on the number of selected rows or directly from the cocycle.

For `c in ker A`, `D(c)` is the positive integer square root in (R5), and

\[
r(c)=\frac{\prod_i\alpha_i^{c_i}}{D(c)}\pmod N,
\qquad r(c)^2=1\pmod N. \tag{R7}
\]

Thus `G(c)=(0,r(c))`. Formula (R7) is exactly the normalized modular root of
the selected integer-square product. If the normalization convention uses
its reciprocal, nothing changes because `r(c)^{-1}=r(c)`.

Every square-producing subset is in `ker A` by (14), and every vector in
`ker A` produces the root (R7). Therefore `G(ker A)` is exactly, not merely a
subgroup of, the normalized-root image of the complete factor-free decoder.

## 5. Exact split-or-section law

Let `bar G` be `G` followed by quotienting by `Delta`. The quotient projection
obeys

\[
\bar\pi\circ\bar G=A. \tag{R8}
\]

A map `h` with the prescribed generator values must satisfy

\[
h(A(c))=\bar G(c). \tag{R9}
\]

Such a map is well-defined exactly when

\[
c\in\ker A\quad\Longrightarrow\quad \bar G(c)=1,
\]

or equivalently

\[
G(\ker A)\subseteq\Delta. \tag{R10}
\]

If (R10) fails, some kernel vector gives a root outside `Delta`, and the gcd
calculation factors `N`. This is event 1.

If (R10) holds, define

\[
h(A(c))=\bar G(c). \tag{R11}
\]

If `A(c)=A(d)`, then `c+d` is in `ker A`; (R10) gives
`bar G(c)=bar G(d)`. So (R11) is well-defined. It is a homomorphism. By (R8),
`bar pi(h(u))=u`. It also sends every `v_i` to `bar g_i`. Since the `v_i`
span `W`, these prescribed values make `h` unique.

Conversely, the existence of such an `h` forces (R10) by applying (R9) to
`c in ker A`. Therefore the two events are exhaustive and mutually
exclusive.

### Online algorithm

Maintain independent parity vectors `b_1,...,b_k` and decorated lifts
`e_1,...,e_k` with `pi(e_l)=b_l`.

For a new `(v,z)`, row reduction gives either a proof that `v` is independent
or coefficients `lambda_l` with

\[
v=\sum_l\lambda_lb_l.
\]

In the independent case, append `v` and its lift. In the dependent case,
form

\[
e(v)=\mathop{\star}_l e_l^{\lambda_l}.
\]

Then `(v,z) star e(v)` has first coordinate zero. Read its second coordinate
`r`. If `r` is neither `1` nor `-1 mod N`, the two gcds factor `N`. Otherwise
the new lift agrees with the maintained quotient section and can be
discarded algebraically after its metadata is merged when appropriate.

Gaussian elimination over `F_2`, modular multiplication and inversion, sign
comparison, and gcd computation are all polynomial in the bit length of the
explicit transcript. No enumeration of `ker A` is required. Therefore an
explicit quasipolynomial-size transcript is processed in quasipolynomial
work, subject to the usual condition that the bit lengths of all explicit
integers are included in the transcript size.

## 6. Abstract splitting and its exact consequence

Every element of `E_Q(N)` and `R_N` has order at most two. With the displayed
operations, (6) is therefore a short exact sequence of `F_2`-vector spaces.
Choose a basis `b_1,...,b_d` of `V_Q(N)` and choose any lift `e_l` of each
`b_l`. Then

\[
s\left(\sum_l\lambda_lb_l\right)
=\mathop{\star}_l e_l^{\lambda_l}
\]

is a well-defined linear section of `pi` on all of `V_Q(N)`. Thus the full
extension always splits abstractly.

This gives a direct countermodel to any projection-only factoring claim:
for any parity geometry, the observed lifts can lie on an abstract section,
in which case every parity circuit has only the identity normalized root
(and independent global-sign changes still give only global roots). Large or
small doubling, many circuits, or row reuse in the projection cannot exclude
this model.

What must be forced is therefore

\[
\bar G(c)\ne1\quad\text{for some }c\in\ker A, \tag{R12}
\]

equivalently, failure of the lifted relation map to factor through `A`.
Comparing two canonical source layers is a useful way to expose (R12). A
direct within-family circuit can expose the same condition. This is the
scope qualification stated in the verdict.

## 7. Two layers and the cross-ratio decoder

Let the coefficient spaces of the two layers be `C_F` and `C_A`, with parity
maps `A_F,A_A` and decorated-product maps `G_F,G_A`. The assumption that
each pure layer has only global normalized roots gives

\[
G_F(\ker A_F)\subseteq\Delta,
\qquad
G_A(\ker A_A)\subseteq\Delta.
\]

Section 5 therefore constructs unique quotient sections `h_F` and `h_A`.

For `u in W_F intersect W_A`, choose `c_F,c_A` with

\[
A_F(c_F)=u=A_A(c_A).
\]

The combined coefficient vector has zero parity because the field has
characteristic two. Its normalized-root class is

\[
\overline{G_F(c_F)G_A(c_A)}=h_F(u)h_A(u). \tag{R13}
\]

Different choices of `c_F` or `c_A` change the unquotiented product only by a
global sign, so (R13) is well-defined in `R_N/{+1,-1}`. Every mixed parity
dependency yields some common `u` in this way. Since pure dependencies are
global by assumption, the union has a useful dependency if and only if

\[
h_F(u)\ne h_A(u)
\]

for some `u` in the intersection. This proves the complete if-and-only-if
claim in (18), not only its forward direction. Root-aware membership merging
is sufficient because duplicate lifts agree in the quotient.

### Same-parity specialization

For two rows with the same parity `v`, let `d=Q(v)` and

\[
T_i=ds_i^2,\qquad T_j=ds_j^2.
\]

Their decorated quotient is their star product:

\[
(v,\alpha_i/s_i)\star(v,\alpha_j/s_j)
=\left(0,\frac{\alpha_i\alpha_j}{d s_i s_j}\right). \tag{R14}
\]

Using `alpha_j^2=d s_j^2 mod N`,

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}
=\frac{\alpha_i s_j}{\alpha_j s_i}\pmod N. \tag{R15}
\]

This reconstructs both forms of (20). It is exactly the two-row
same-squareclass cross ratio claimed in the statement.

## 8. Independent check of the `N=2773` illustration

The integer identities are

\[
47\cdot59=2773,
\]

\[
3\cdot43^2=5547=1+2\cdot2773,
\]

and

\[
3\cdot842^2=2{,}126{,}892=1+767\cdot2773.
\]

Thus both supplied values `alpha_1=alpha_2=1` are valid modular roots. The
cross-ratio root in (R14) is the inverse of

\[
R=3\cdot43\cdot842=108{,}618.
\]

But this inverse equals `R mod N`, because

\[
R\equiv471\pmod{2773},
\qquad
471^2=221{,}841=1+80\cdot2773.
\]

The second form in (R15) also gives

\[
842\cdot43^{-1}\equiv471\pmod{2773}.
\]

Finally,

\[
\gcd(108{,}618-1,2773)=47,
\qquad
\gcd(108{,}618+1,2773)=59.
\]

All arithmetic in (21)--(24) is correct.

## 9. Claim-by-claim disposition

| Claim | Disposition |
|---|---|
| Pairwise-coprime nonsquares give independent rational square classes | Proved |
| `E_Q(N)` is an abelian exponent-two group | Proved |
| Projection image, kernel, exact sequence, and gcd factor extraction | Proved |
| Supplied-root-aware exact-value deduplication | Proved modulo the explicitly stated global-sign quotient |
| Equality of `ker A` with all exact square-producing subsets | Proved |
| Equality with the complete normalized-root image | Proved by (R6)--(R7) |
| Exactly one of factor or unique quotient section | Proved in both directions |
| Online basis algorithm and polynomial overhead | Proved |
| Existence of an abstract full section | Proved constructively from a basis |
| Two-layer useful dependency iff section disagreement | Proved in both directions |
| Same-squareclass cross-ratio identity | Proved |
| `N=2773` certificate | Verified exactly |
| Projection structure alone cannot force a factor | Proved by the abstract-section countermodel |
| Literally two named source mechanisms are necessary | Not logically necessary; lift nonlinearity is the exact requirement |

No algebraic counterexample was found. Subject to the last wording
qualification, the statement is self-contained and reconstructible.
