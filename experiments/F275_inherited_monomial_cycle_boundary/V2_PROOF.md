# F275 V2 proof — size repair and unchanged core

## Imported proof

V2 incorporates the complete frozen V1 proof at SHA-256

`d5d1990b1e3fa4cf5e4d4e6efa1cfc02690576e761aa136e8f59afb6df836447`.

Sections 1, 2, 4, and 5 are unchanged. Section 3's unit and root-congruence
argument is unchanged. The following calculation supplies the only repaired
claim.

## Canonical construction (8)

Assume the input to construction (8) satisfies

\[
 1\le d<N,
 \qquad \gcd(d,N)=1,
\]

and let `y` be a unit modulo `N`. By definition,

\[
 T_y(d)=[y^2d^{-1}]_N
\]

is the canonical representative of a unit, so

\[
 1\le T_y(d)<N.
\]

Therefore the exact positive edge row obeys

\[
 1\le dT_y(d)\le(N-1)^2<N^2.                       \tag{V2.1}
\]

Its supplied-root congruence remains

\[
 dT_y(d)
 \equiv d(y^2d^{-1})
 \equiv y^2
 \pmod N.                                           \tag{V2.2}
\]

This proves the corrected construction claim.

## Why the general theorems do not change

The general graph calculation uses only

\[
 A_e=d_ud_v>0,
 \qquad \gcd(d_ud_v,N)=1,
 \qquad y_e^2\equiv d_ud_v\pmod N.
\]

It does not use `d_v<N` or `A_e<N^2`. Thus the Eulerian-square identity,
the two perfect-matching identities on an even cycle, the alternating-label
root formula, and both exact gcd equalities remain exactly as proved in V1.

Theorem A does not use construction (8). Its exponent-parity pullback and
normalized-root formula likewise remain unchanged.

