# F262 algebra — polynomial Frobenius lift carries modulo `N^2`

## 1. Canonical polynomial model

Fix a public monic polynomial

\[
 f(X)=X^d+f_{d-1}X^{d-1}+\cdots+f_0,\qquad 2\le d\le5.
\]

All polynomial remainders below are the unique degree-below-`d` remainders
under monic division in `Z[X]`. For a modulus `m`, brackets mean
coefficientwise least residues in `[0,m)`.

For a public element `a(X)` define

\[
 P_f(a)=\langle a^N\bmod f\rangle_{N^2}=r_f(a)+N C_f(a),
 \qquad 0\le r_i,C_i<N.
\]

Both vectors are public. Binary exponentiation needs `O(d^2 log N)` modular
coefficient operations. Monicity makes the representation canonical without
an inverse or a hidden factor.

Before using a polynomial, F262 computes

\[
 \Delta_f=(-1)^{d(d-1)/2}\operatorname{Res}(f,f').
\]

It gcd-screens `Delta_f` with `N`. A proper gcd is an exact cleanup factor. If
the gcd is `N`, the polynomial is skipped. Thus every scored polynomial is
squarefree in both hidden prime components.

## 2. The exact integer section carry

For canonical vectors `u,v in [0,N)^d`, put

\[
 w=\operatorname{rem}_f(uv),\quad z=\langle w\rangle_N,
 \quad K_f(u,v)={w-z\over N}.
\]

The quotient is coefficientwise integral by definition. Split it once more:

\[
 k_f(u,v)=\langle K_f(u,v)\rangle_N,
 \qquad H_f(u,v)={K_f(u,v)-k_f(u,v)\over N}.
\]

This second quotient is also an exact integer vector. It is not inferred from
a modular zero.

For a third canonical vector `s`, write
`z_uv=<rem_f(uv)>_N` and `z_vs=<rem_f(vs)>_N`. Associativity in
`Z[X]/(f)` gives the exact full-carry identity

\[
 K(z_{uv},s)+\operatorname{rem}_f(K(u,v)s)
 -K(u,z_{vs})-\operatorname{rem}_f(uK(v,s))=0.                \tag{A}
\]

Replacing each full `K` by its principal digit `k` gives the public residual

\[
 E_f(u,v,s)=k(z_{uv},s)+\operatorname{rem}_f(k(u,v)s)
 -k(u,z_{vs})-\operatorname{rem}_f(uk(v,s)).                  \tag{B}
\]

Substitution of `K=k+NH` into (A) proves coefficientwise exact divisibility
`N | E_f`. F262 inserts only the authenticated integer quotient

\[
 Q^{assoc}_f(u,v,s)=E_f(u,v,s)/N.                              \tag{C}
\]

The exact zero in (A) is a mandatory decoy. The quotient in (C) is the next
integer carry left open by the linear-cocycle boundary P56.

## 3. Exponent-lift multiplicativity quotient

The map `a -> a^N` is multiplicative in the commutative algebra modulo
`(f,N^2)`. For public elements `a,b`, abbreviate

\[
 P_f(a)=r_a+NC_a,\quad P_f(b)=r_b+NC_b,\quad
 P_f(ab)=r_{ab}+NC_{ab}.
\]

Let `K=K_f(r_a,r_b)`. Exact multiplication modulo `N^2` implies

\[
 C_{ab}-K-\operatorname{rem}_f(r_aC_b+C_ar_b)\equiv0\pmod N.
\]

F262 forms the displayed integer vector and verifies every coefficient is
exactly divisible by `N` before inserting

\[
 Q^{mult}_f(a,b)=
 {C_{ab}-K-\operatorname{rem}_f(r_aC_b+C_ar_b)\over N}.       \tag{D}
\]

The unquotiented residual is a globally zero modulo-`N` control. No quotient
node is admitted from a tested congruence alone.

## 4. Translation and basis-change control

For an integer `t`, let `f_t(X)=f(X-t)`. The substitution `Y=X-t` gives a
public unimodular triangular change of basis between
`Z[Y]/(f)` and `Z[X]/(f_t)`. F262 compares

\[
 a(Y)^N\bmod f(Y)
 \quad\hbox{with}\quad
 a(X-t)^N\bmod f_t(X).
\]

It transports the full canonical residue modulo `N^2` back through the exact
inverse substitution and only then splits it into low and high digits. The
two canonical pairs must agree exactly. Raw high-digit coordinate vectors do
not transform linearly because canonical low-digit reduction creates a public
carry. They are retained only as a basis-artifact control and are excluded
from factor-candidate ranking. A public evaluation fingerprint maps every
translated copy to the same canonical source identifier.

## 5. Basis-invariant polynomial summaries

A vector `v` represents an element of `Z[X]/(f)`. Let `M_f(v)` be its
`d by d` multiplication matrix in the power basis. F262 uses:

- `trace(M_f(v))` and `det(M_f(v))`;
- all characteristic coefficients from `det(TI-M_f(v))`;
- determinants of coefficient-window matrices;
- all `2 by 2` and selected `3 by 3` minors of lift/carry columns;
- `Res(f,v)`, pairwise `Res(v,w)`, and discriminants of monicized public
  coefficient polynomials when the leading coefficient is `+1` or `-1`;
- determinantal divisors, represented by the gcd of `N` and the enumerated
  integer minors, as public Smith/rank indicators.

Trace, norm, characteristic polynomial, and resultants are invariant under
the translation control. Coordinate minors are grouped by their transported
canonical basis fingerprint. Any nonunit leading coefficient or defining
resultant is gcd-screened before division or interpretation.

## 6. Local cycle label used only for scoring

For a hidden verification prime `r | N`, squarefreeness gives a factor-degree
partition of `f mod r`. It is reconstructed from

\[
 D_k=\deg\gcd(f,X^{r^k}-X),\qquad
 D_k=\sum_{e\mid k}e m_e,\quad 1\le k\le d.
\]

The counts `m_e` are labels only. They never enter the source, grammar,
canonicalization, candidate selection, or gcd computation. F262 reports
candidate hits separately when the two hidden partitions agree and differ.
This is not construction of a glued local Frobenius and does not contradict
P132.

## 7. Public `N`-primitive normalization

For a nonzero exact scalar atom `w`, define

\[
 \operatorname{prim}_N(w)=|w|/N^{v_N(w)},
\]

where repeated division is by the known composite integer `N`. Exact zeros
and resulting units are neutral. This removes public global `N` factors. It
does not divide by a hidden prime.
