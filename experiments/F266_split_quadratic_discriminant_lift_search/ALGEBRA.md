# F266-D01 algebra — canonical split-quadratic discriminant lifts

## Status and scope

This file fixes the exact algebra before any semiprime corpus is opened.
F266 is a finite symbolic search. It is not a factoring theorem.

The closest prior decoder is P66. P66 completely decodes any explicit list
of positive integers with supplied modular square roots, but it does not
construct a useful list. F266 constructs such rows from canonical lifts of
split binary quadratic forms.

The closest lift searches are F262 and F264. F262 applies the exponent `N`
inside a polynomial algebra. F264 keeps ordered noncommutative matrix-word
coordinates. F266 does neither. Its matrices only change variables in one
commutative binary quadratic form. The exact invariant is the discriminant.
The searched data are the integer carries created when canonical coefficient
representatives destroy that exact invariant over the integers.

## 1. Public split source and supplied root

Let `N>=3` be odd. Let `h` be 1 or 2 and put

\[
  m=N^h.
\]

Choose public residues `a,r,s` modulo `m`. Their reductions modulo `N` are
selected and screened without a hidden factor. Require

\[
  \gcd(a,N)=\gcd(r,N)=\gcd(s,N)=\gcd(r-s,N)=1.
\]

Every gcd is computed before a row is used. A proper gcd is already a
certified factor. A full gcd rejects the attempted source value.

Define canonical coefficients

\[
  A_0=[a]_m,
  \qquad B_0=[-a(r+s)]_m,
  \qquad C_0=[ars]_m,
\]

and the binary quadratic form

\[
  Q_0(X,Y)=A_0X^2+B_0XY+C_0Y^2.
\]

Modulo `m`, it is the public split form

\[
  Q_0(X,Y)=a(X-rY)(X-sY).
\]

Its exact integer discriminant is

\[
  \Delta_0=B_0^2-4A_0C_0.
\]

Put

\[
  x=[a(r-s)]_N.
\]

Then

\[
  \boxed{\Delta_0\equiv x^2\pmod N}.
\]

The source screens `gcd(x,N)` and `gcd(Delta_0,N)`. The first screen also
proves that every admitted discriminant row is a unit modulo `N`.

Swapping `r` and `s` changes `x` to `-x` and changes no coefficient. F266
sorts the two base roots and replaces `x` by `min(x,N-x)`. Thus the swapped
source is one canonical source, not two observations.

## 2. Exact `SL_2(Z)` change of variables

Let

\[
 M=\begin{pmatrix}u&v\\w&z\end{pmatrix},
 \qquad uz-vw=1.
\]

Define

\[
 Q_M(X,Y)=Q_0(uX+vY,wX+zY)
          =A^*X^2+B^*XY+C^*Y^2,
\]

where

\[
\begin{aligned}
 A^*&=A_0u^2+B_0uw+C_0w^2,\\
 B^*&=2A_0uv+B_0(uz+vw)+2C_0wz,\\
 C^*&=A_0v^2+B_0vz+C_0z^2.
\end{aligned}
\]

Direct expansion gives the exact integer identity

\[
  \boxed{(B^*)^2-4A^*C^*=\Delta_0}.                 \tag{1}
\]

Equation (1) is a mandatory global decoy. It never enters a word or a P66
list.

For an original affine root `t`, the transformed projective root is

\[
  P_M(t)=(zt-v:u-wt).
\]

The two root determinants satisfy the exact congruence

\[
 \det(P_M(r),P_M(s))=r-s\pmod N.                    \tag{2}
\]

F266 uses projective pairs. It does not invert a denominator silently. It
screens each numerator, denominator, and every same-bank cross determinant.
A proper gcd is a direct root certificate. A component equal to zero modulo
all of `N` is a public zero or infinity and is retained only when the other
projective coordinate is a unit.

## 3. Canonical coefficient lift and positive P66 row

Reduce the three transformed coefficients independently:

\[
  A=[A^*]_m,\qquad B=[B^*]_m,\qquad C=[C^*]_m.
\]

Write

\[
 A=A^*-m\alpha,\quad B=B^*-m\beta,\quad C=C^*-m\gamma.
\]

The canonical discriminant is

\[
  D_M=B^2-4AC.
\]

Substitution into (1) gives the exact carry identity

\[
\boxed{
 D_M=\Delta_0
 +m[-2B^*\beta+4(A^*\gamma+C^*\alpha)]
 +m^2(\beta^2-4\alpha\gamma).}                      \tag{3}
\]

In particular, `m | D_M-Delta_0` and

\[
  D_M\equiv x^2\pmod N.
\]

The discriminant can be negative. Define the positive row

\[
 R_M=
 \begin{cases}
 D_M,&D_M>0,\\
 D_M+4m^2,&D_M\le0.
 \end{cases}                                        \tag{4}
\]

The added term is the exact square `(2m)^2`, so (4) preserves the supplied
modular root `x`. Since `0<=A,B,C<m`,

\[
 -4(m-1)^2\le D_M\le(m-1)^2.
\]

Therefore

\[
  \boxed{0<R_M\le4m^2}.                              \tag{5}
\]

If `n=ceil(log2(N+1))`, every level-`N` row has at most `2n+2` bits and
every level-`N^2` row has at most `4n+2` bits. These are checked by the
executable. No sign assumption is used.

The exact invariant carry is

\[
  \kappa_M={R_M-\Delta_0\over m}\in\mathbb Z.       \tag{6}
\]

Changing the branch in (4) adds `4m` to (6), which is a multiple of `N`.
It does not change `gcd(kappa_M,N)`.

For two matrices in the same base and lift level,

\[
  {R_M-R_L\over m}=\kappa_M-\kappa_L               \tag{7}
\]

is exact. For rows at different lift levels but with the same base residues,
`N | R_{M,N^2}-R_{L,N}`. F266 also tests that cross-level quotient. Equations
(6) and (7) are public integer tickets. A proper quotient gcd is a certified
factor. A zero or a full gcd is a global carry decoy.

## 4. Word size and intermediate bounds

F266 uses the five generators

\[
 U(1),U(-1),L(1),L(-1),S,
\]

where

\[
 U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
 L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\quad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The maximum word length is seven. The maximum row-sum norm of one generator
is two, so every matrix entry has absolute value at most `2^7`. The source
checks this bound. A deliberately looser frozen bound of `4^7` is used in the
raw-coefficient estimate.

The raw transformed coefficients have absolute value below

\[
  6m(4^7)^2.
\]

They therefore have `O(n)` bits. Canonical reduction makes the final row
bound (5) independent of the word entries.

## 5. Direct screens before P66

Every direct screen is public and runs before a later relation can be called
strict. The complete list is:

1. `gcd` of each source root, root difference, leading coefficient, and
   supplied discriminant root with `N`;
2. `gcd` of every base and transformed coefficient and discriminant with
   `N`;
3. `gcd` of every projective root coordinate and every projective root
   determinant with `N`;
4. the exact Sylvester resultant of every retained pair of affine quadratic
   coefficient triples, followed by `gcd(resultant,N)`;
5. every single invariant carry (6), same-level quotient (7), and admitted
   cross-level quotient;
6. every exact singleton-square normalized-root comparison; and
7. every equal-row or exact square-multiple normalized-root comparison.

The resultant is the determinant of the displayed `4 by 4` Sylvester matrix.
The implementation computes it over the integers and checks it against a
second fraction-free determinant path in self-test mode.

No proper gcd from this list is relabelled as a P66 gain.

## 6. Canonical decoys

F266 removes these structures before the residual decoder:

- `M` and `-M`, which give the same quadratic form;
- exact duplicate matrices;
- stabilizer words with the same canonical coefficient triple;
- swapped base roots;
- equal positive rows;
- exact square rows;
- exact square-multiple row pairs after their supplied-root comparison;
- the raw invariant identity (1);
- zero or full-gcd carries from (6) and (7); and
- relations generated by a row already removed in one of the preceding
  classes.

For a square multiple `R_j=R_i t^2`, the exact product root is `R_i t`.
F266 verifies `(R_i t)^2=R_iR_j`, multiplies the two supplied roots modulo
`N`, and tests both signed gcds. A useful result is reported as the named
two-row template. A global result is a decoy. Only then is one rational
square-class representative retained.

The executable never treats a larger kernel dimension as progress by itself.

## 7. Complete factor-free square decoder

Each retained positive row `R_i` has a supplied unit `x_i` with

\[
  x_i^2\equiv R_i\pmod N.
\]

F266 applies the P66 gcd-free decoder. It repeatedly splits explicit integer
blocks by gcd and exact division until the final blocks are pairwise coprime.
It preserves the complete exponent vector of every row. It never assumes an
opaque block is prime and records every nonsquare block as
`UNKNOWN_OPAQUE_NOT_NEEDED`.

The following caps are part of correctness:

- at most 96 retained rows in one bank;
- at most 25,000 gcd-free split or merge steps;
- at most 4,096 final opaque blocks; and
- at most 65,536 total input-row bits.

Crossing a cap rejects the bank as a resource event. It is not a null result.

For every binary kernel-basis vector `c`, the executable forms

\[
 P(c)=\prod_i R_i^{c_i}
\]

as an exact integer, computes its exact positive square root, and verifies
the square identity. It also computes

\[
 X(c)=\prod_i x_i^{c_i}\pmod N
\]

and both signed gcds. A useful certificate contains the complete selected
row list, exact root, supplied root, normalized root, and proper gcd. A
multirow gain has support at least two and survives every decoy and direct
screen above.

## 8. Singleton baseline and interpretation

A clean exact-square row can already have a mixed supplied root. This is a
real factor certificate, but it is not evidence for orbit amortization.
F266 separates:

1. `BASE_SINGLETON`: the identity word at either lift level;
2. `ORBIT_SINGLETON`: a nonidentity canonical word;
3. `CARRY_TICKET`: an invariant-carry or quotient gcd;
4. `SQUARE_MULTIPLE_TEMPLATE`: a verified two-row template; and
5. `MULTIROW_P66`: a residual P66 relation.

For every eligible bank with `k` distinct tested rows, the report includes
the exact comparison mass

\[
  {2k\over N}.
\]

This is the P213 useful-square mass for `k` independent uniform principal
digits. It is a comparison only. F266 rows are deterministic functions of
`N` and are not claimed independent or uniform.

## 9. Exact finite scope

A positive finite certificate factors its displayed modulus. It does not
prove an inverse-quasipolynomial event law. A null result is only a null for
the frozen source, word cap, cohorts, and decoder.

Even a repeated held-out signal leaves the all-input probability theorem,
uniform bit-complexity at unbounded scale, arbitrary-composite dispatch, and
complete Las Vegas analysis open.
