# F252 statement — Pell polynomial independence and the resultant-supported numerical core

## Status and scope

This is a deterministic structural theorem for an explicit finite bank of
canonical Pell rows. It proves two facts.

1. After constant-square rows and exact polynomial duplicates are removed,
   the generic square-class kernel is zero.
2. After private square parts are discarded, every cross-row prime
   interaction created only by specialization at \(N\) is supported on
   explicit pairwise resultants.

The theorem does not prove that the specialized numerical kernel is zero. It
does not bound the probability that a resultant-supported dependency occurs,
and it is not a factoring algorithm.

## Setup

Let \(N\ge 3\) be odd. For \(1\le i\le m\), let

\[
D_i,S_i,T_i,k_i\in\mathbb Z,
\qquad D_i>0,\quad S_i>0,\quad T_i\ge0,\quad k_i\ge0,
\]

and assume

\[
S_i^2-D_iT_i^2=1.
\]

For a canonical Pell row one has

\[
y_i=T_i-k_iN,
\qquad 0\le y_i<N,
\]

but only the displayed affine identity is needed below. Define

\[
f_i(X)=1+D_i(T_i-k_iX)^2\in\mathbb Z[X],
\qquad
a_i=f_i(N)=1+D_i y_i^2.
\]

Then

\[
a_i\equiv S_i^2\pmod N.
\]

On the clean branch assume \(\gcd(S_i,N)=1\), equivalently
\(\gcd(a_i,N)=1\), and use \(x_i=S_i\bmod N\) as the supplied unit square
root. A nonunit row is outside the normalized-root conclusion and is first
subject to its public gcd screen.

Let

\[
K_{\rm gen}
=
\left\{c\in\mathbb F_2^m:
\prod_i f_i(X)^{c_i}\text{ is a square in }\mathbb Q(X)
\right\},
\]

and let

\[
K_N
=
\left\{c\in\mathbb F_2^m:
\prod_i a_i^{c_i}\text{ is an integer square}
\right\}.
\]

The first kernel records identities before specialization. The second is the
exact numerical kernel computed by the P66 decoder.

## A. Content, primitive part, and irreducibility

If \(k_i=0\), then

\[
f_i(X)=1+D_iT_i^2=S_i^2
\]

is a constant integer square.

Suppose \(k_i\ne0\). The exact positive content of \(f_i\) is

\[
\boxed{
\operatorname{cont}(f_i)
=\gcd(S_i^2,k_i^2,2k_i).
}
\]

After division by this content, the primitive quadratic has discriminant

\[
\boxed{
-\frac{4D_i k_i^2}{\operatorname{cont}(f_i)^2}<0.
}
\]

It is therefore irreducible over \(\mathbb Q\). In particular, a post-wrap
polynomial is neither a square nor a product of linear polynomials over
\(\mathbb Q\). No squarefree assumption on \(D_i\) is required.

## B. Pairwise resultant and exact duplicate classification

Take two post-wrap rows

\[
f(X)=1+D(T-kX)^2,
\qquad
g(X)=1+E(U-\ell X)^2,
\]

where \(k\ell\ne0\), and put

\[
\Delta=T\ell-Uk.
\]

Their exact resultant is

\[
\boxed{
\operatorname{Res}_X(f,g)
=
[DE\Delta^2+E\ell^2+Dk^2]^2
-4DEk^2\ell^2.
}
\]

When \(D=E\), this factors as

\[
\boxed{
D^2[D\Delta^2+(k-\ell)^2]
   [D\Delta^2+(k+\ell)^2].
}
\]

For positive \(D,E\), the following are equivalent:

\[
\operatorname{Res}_X(f,g)=0,
\]

\[
\Delta=0\quad\text{and}\quad Dk^2=E\ell^2,
\]

and

\[
f=g\quad\text{in }\mathbb Z[X].
\]

Thus two post-wrap Pell polynomials are associates over \(\mathbb Q\) exactly
when they are equal as integer polynomials. If \(D,E\) are squarefree and
\(k,\ell>0\), equality further reduces to

\[
D=E,\qquad k=\ell,\qquad T=U.
\]

Without squarefree normalization, scaled duplicates can occur, and the exact
criterion remains \(\Delta=0\) and \(Dk^2=E\ell^2\).

## C. Complete generic kernel and its root image

Let \(I_0=\{i:k_i=0\}\). Partition the post-wrap indices into exact
polynomial-equality classes \(C\). Then

\[
\boxed{
c\in K_{\rm gen}
\iff
\sum_{i\in C}c_i=0\pmod2
\quad\text{for every post-wrap class }C.
}
\]

There is no condition on the constant-square indices \(I_0\). Consequently,
after deleting \(I_0\) and retaining one representative of every equality
class,

\[
\boxed{K_{\rm gen}=0.}
\]

The global-root conclusion has no coefficient-denominator exception. For
every \(c\in K_{\rm gen}\), there is an explicit integral polynomial
\(H_c(X)\in\mathbb Z[X]\) such that

\[
H_c(X)^2=\prod_i f_i(X)^{c_i},
\qquad
H_c(0)=\prod_i S_i^{c_i}.
\]

If \(R_c\) is the positive integer square root of
\(\prod_i a_i^{c_i}\), then \(R_c=|H_c(N)|\), and hence

\[
\boxed{
R_c\equiv\pm\prod_i x_i^{c_i}\pmod N.
}
\]

Every generic dependency therefore has a global normalized root. It cannot
split \(N\) through the two standard square-root gcds.

## D. The resultant-supported numerical core

Delete the constant-square rows and retain one representative of each exact
post-wrap polynomial. Denote the remaining index set by \(J\). Every
pairwise resultant on \(J\) is nonzero. For \(i\in J\), define

\[
\mathcal R_i
=
\prod_{\substack{j\in J\\j\ne i}}
\left|\operatorname{Res}_X(f_i,f_j)\right|,
\]

with empty product \(1\), and put

\[
e_i=\left\lceil\log_2(a_i+1)\right\rceil,
\qquad
g_i=\gcd(a_i,\mathcal R_i^{e_i}),
\qquad
b_i=\frac{a_i}{g_i}.
\]

Then

\[
\boxed{
\gcd(b_i,a_j)=1\qquad(i\ne j).
}
\]

Thus every prime divisor of \(b_i\) is private to row \(i\). The following
consequences are exact.

1. If \(b_i\) is not an integer square, then every vector \(c\in K_N\) has
   \(c_i=0\).
2. If \(b_i\) is an integer square, then \(a_i\) and \(g_i\) have the same
   rational-prime parity column, and every prime divisor of \(g_i\) divides
   the explicit integer \(\mathcal R_i\).
3. After all nonsquare-private rows are removed and each square \(b_i\) is
   discarded from its column, the complete remaining numerical parity
   problem is supported on the pairwise resultants.

This is a localization theorem, not a claim that the localized core is empty.
Specialization at \(X=N\) can still create a square dependency that has no
counterpart in \(\mathbb Q(X)\). A post-wrap singleton can also become an
integer square only after specialization; its parity column is zero, but its
supplied-root comparison must still be screened separately.

## E. Factor-free complexity

All steps use coefficient gcds, exact integer arithmetic, the closed
resultant formula, binary exponentiation, integer gcds, exact division,
integer square tests, and binary linear algebra. They do not factor any
integer.

Let \(L\) be the total bit length of the explicit list

\[
N;(D_i,S_i,T_i,k_i)_{i=1}^m.
\]

The coefficient sizes, all \(a_i\), all pairwise resultants, and every
\(\mathcal R_i\) have total bit length polynomial in \(L\). Also
\(e_i=O(L)\), so \(\mathcal R_i^{e_i}\) has polynomial bit length. The full
cleanup and saturation therefore have deterministic bit complexity
\(\operatorname{poly}(L)\).

In particular, an explicitly materialized bank of quasipolynomially many
rows whose coordinates have quasipolynomial bit length remains within
quasipolynomial work. This does not apply to an implicitly specified bank
whose explicit expansion is larger.

## F. Relation to P68 and exact remaining gap

P68 handles general polynomial sources with constant term \(1\). It removes
generic dependencies whose rational square roots have denominator coprime to
\(N\), but it does not normally make the generic kernel zero and does not
localize specialization-only relations.

Here the Pell identity gives square constant terms \(f_i(0)=S_i^2\). Direct
irreducible-factor classification gives the complete generic kernel and an
integral square root for every vector in it. Hence there is no denominator
gap. The new conclusions beyond applying P68 are:

1. zero generic kernel after constant-square and exact-duplicate cleanup;
2. the closed pairwise resultant formula and exact duplicate criterion; and
3. factor-free reduction of the entire numerical kernel to an explicit
   resultant-supported core plus private parity pivots.

The remaining source problem is to control that resultant-supported core.
This statement gives no all-input private-prime theorem, no inverse-QP event
bound, no non-global root law, and no complete factoring algorithm. F250's
finite null scan is consistent with the theorem but is not used in its proof.
