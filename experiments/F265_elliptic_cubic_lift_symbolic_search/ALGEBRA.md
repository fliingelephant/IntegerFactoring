# F265 algebra: canonical elliptic cubic-lift rows

## Status

This file fixes the exact algebra before any search result exists. It is a
candidate packet. It is not a factoring theorem.

The closest prior route is X14/P20. That route clears and pools pairwise
elliptic `x`-coordinate collisions through an index near `sqrt(N)`. F265 does
not use that product. It keeps a quasipolynomial-size bank of canonical
affine coordinates and sends their cubic integer lifts to the complete P66
square-class decoder. Nonduplicate multirow relations are the target.

## 1. Public curve and orbit

Let `N >= 3` be odd. Choose public residues

\[
  A,x_0,y_0\in\{0,\ldots,N-1\}
\]

without using a factor of `N`, and set

\[
  B=[y_0^2-x_0^3-Ax_0]_N.
\]

The public modular curve and seed are

\[
 E_N:y^2=x^3+Ax+B\pmod N,
 \qquad P=(x_0,y_0).
\]

Put

\[
  \delta_E=4A^3+27B^2.
\]

The first screen is `gcd(delta_E,N)`. A proper gcd is a certified factor.
If the gcd is `N`, the curve is rejected. If it is one, the curve has good
short-Weierstrass reduction at every prime divisor of `N`.

The construction normally has a nonzero integer seed defect

\[
 x_0^3+Ax_0+B-y_0^2=c_0N.
\]

Thus it does not assume that `P` is an integral rational point on one fixed
curve over the integers. The zero-defect case is retained as a separate
singleton-square control.

## 2. Factor-first affine arithmetic

F265 never assumes that a nonzero residue is invertible.

For doubling an affine point `(x,y)`, the proposed denominator is `2y`.
For adding distinct affine points, it is `x_2-x_1`. Before inversion, compute
its gcd with `N`.

- A proper gcd is a certified denominator factor.
- A unit denominator is inverted by extended Euclid.
- A denominator with gcd `N` is handled as a global exceptional case.

For equal global `x`-coordinates, compare `y_2-y_1` and `y_2+y_1` modulo
`N`. Equality gives doubling or the point at infinity. If neither is zero,
good reduction implies different signs on different CRT components. One of
the two signed gcds is then proper. The orbit stops at every proper factor;
it is never continued with factor-assisted arithmetic.

This is an explicit-factor-first affine implementation. A future projective
implementation must preserve the same exit classification.

## 3. Exact public row and root law

Let a clean affine orbit point be

\[
  P_k=(u_k,v_k),\qquad 0\le u_k,v_k<N.
\]

Define the positive integer

\[
  a_k=u_k^3+Au_k+B.
\]

The curve equation gives the exact public congruence

\[
  \boxed{a_k\equiv v_k^2\pmod N.}
\]

Before admitting this row, compute `gcd(v_k,N)`, equivalently
`gcd(a_k,N)` at the level of prime support. A proper gcd is a certified row
factor. A nonunit with gcd `N` is not a P66 row and is skipped.

The row-size bound is uniform:

\[
  0<a_k<N^3+N^2+N<2N^3,
\]

so its bit length is at most `3n+1`, where
`n=ceil(log2(N+1))`. In the frozen corpus, factors have at most 60 bits,
so `N` has at most 120 bits and every row has at most 361 bits. The source
code checks the actual bound and rejects a bank on violation.

The signed lift carry

\[
  c_k={a_k-v_k^2\over N}\in\mathbb Z
\]

is also public and exact. It is a feature for discovery, not a proof that a
relation exists.

## 4. Direct square controls

### 4.1 Singleton square

If `a_k=s^2` over the integers, then

\[
 z=s v_k^{-1}\pmod N,
 \qquad z^2=1\pmod N.
\]

The two signed gcds classify the event. A proper gcd is a certified factor.
The values `z=1` and `z=-1` are global-root decoys. Singleton rows are
reported separately from multirow relations.

### 4.2 Equal integer rows and equal `x`-coordinates

Within one fixed curve, `X^3+AX+B` is strictly increasing on nonnegative
integers when `A>=0`, so

\[
 a_i=a_j\iff u_i=u_j.
\]

Across different curves, equal integer rows are tested directly and no
coordinate implication is assumed.

For an equal row, `v_i/v_j` is a square root of one modulo `N`. A mixed
ratio gives a proper signed gcd. A global ratio is a duplicate decoy.

The inverse points `Q` and `-Q` have the same `x`-coordinate and opposite
`y`-coordinates. Their ratio is the global root `-1`; this is the named
inverse decoy.

F265 also tests every public pairwise gcd

\[
 \gcd(u_i-u_j,N),\quad
 \gcd(v_i-v_j,N),\quad
 \gcd(v_i+v_j,N)
\]

before calling a later P66 hit strict. These are unpooled elliptic-collision
controls. A P66 factor that occurs after any direct factor in the same bank
does not count as a strict gain.

### 4.3 Exact square-multiple pairs

If `a_j=a_i s^2` for an integer `s`, then `a_i a_j=(a_i s)^2`.
The source verifies this equality and classifies its normalized root. A
global root is a named square-multiple decoy. A mixed root is useful, but it
is reported as a two-row template rather than as an unexplained multirow
pattern.

## 5. Tangent and chord factor channels

Put

\[
 F(X)=X^3+AX+B.
\]

For two integer coordinates `u` and `w`, define

\[
 H(u,w)=u^2+uw+w^2+A.
\]

There is an exact integer identity

\[
 \boxed{F(u)-F(w)=(u-w)H(u,w).}
\]

Therefore

\[
 \gcd(F(u),F(w))
 =\gcd(F(u),(u-w)H(u,w)).
\]

The two public refinements are

\[
 d_{\rm tan}=\gcd(F(u),u-w),\qquad
 d_{\rm chord}=\gcd(F(u),H(u,w)).
\]

Let `ell` be a rational prime that divides both channels. Then
`w=u (mod ell)` and

\[
 H(u,w)=3u^2+A=F'(u)\pmod\ell.
\]

Together with `F(u)=0`, this implies

\[
 \ell\mid 4A^3+27B^2.
\]

Thus away from the public cubic discriminant, a shared rational prime has a
unique tangent or chord label. In the chord channel, `u` and `w` are
distinct roots of `F` modulo `ell`; the third root is

\[
  -u-w\pmod\ell.
\]

The implementation refines shared opaque blocks by the discriminant,
tangent, and chord gcds. It does not assume that a block is prime. It also
tests `gcd(H(u,w),N)` as a direct public control. These rational-prime
channels do not determine the normalized-root sign modulo the hidden factors
of `N`.

## 6. Exact factor-free square-class decoder

For every admitted list `(a_i,v_i)`, use a gcd-free basis. A block is split
until all final positive blocks are pairwise coprime. Exact exponent vectors
are retained, and every row is reconstructed from the blocks.

No block is called prime. No unresolved cofactor is called a private prime.
A pairwise-coprime opaque block is used only as follows.

- If the block is an exact square, it contributes no parity equation.
- If it is not an exact square, the parity of its total exponent is one exact
  square-class equation. This is valid without knowing its prime factors.

The resulting binary matrix is the complete P66 parity matrix. For every
reported kernel-basis vector `c`, the implementation independently forms

\[
  A(c)=\prod_i a_i^{c_i},
\]

computes its exact integer square root, and aborts the bank unless the square
identity verifies. It also computes

\[
  V(c)=\prod_i v_i^{c_i}\pmod N,qquad
  z(c)=\sqrt{A(c)}V(c)^{-1}\pmod N,
\]

and classifies both signed gcds. Every claimed useful relation therefore has
an exact product-square certificate and a proper gcd certificate.

The decoder reports the prime factorization status of every opaque block as
`UNKNOWN_NOT_NEEDED`. This label is never converted into an independence or
primality assertion.

## 7. Global-root identities and residual classes

The following controls are disjoint in the report:

1. denominator/discriminant/row-root direct factors;
2. local `x`-collision and signed-`y` direct factors;
3. singleton exact squares;
4. equal-row and inverse decoys;
5. exact square-multiple pairs;
6. other verified relations with normalized root `+1` or `-1`;
7. verified non-global relations that occur with no earlier direct factor.

Category 6 is the generic/global-root control. The packet does not claim a
complete theorem classifying every formal elliptic identity. It freezes a
bounded template grammar before discovery. A new post-hoc template cannot
be tested on the frozen held-out set without a new version.

## 8. P20 synchronization control

The self-test independently reconstructs the public input

\[
 N=10403,\qquad E:y^2=x^3+x+5,\qquad P=(5461,5889).
\]

It checks the curve equation, the discriminant gcd, all affine multiples
through 101, the two local collision gcds at the declared pairs, and the
simultaneous pooled zero. These values are recomputed from the displayed
data. No historical theorem or stored output is used as an assumption.

This control distinguishes F265 from the pooled P20 observable. It is not a
held-out success row and does not affect family selection.

## 9. Exact scope

The search can discover finite exact relations and counterexamples. It can
reject weak source families. It cannot prove an unbounded success law.

Even a positive held-out signal leaves these gaps:

- an all-input inverse-quasipolynomial probability law;
- a proof that a useful relation appears before every direct failure state;
- uniform bit-complexity for an unbounded bank; and
- the complete reduction for arbitrary composites.

Finite frequency, fitted scaling, and symbolic patterns are guidance only.
