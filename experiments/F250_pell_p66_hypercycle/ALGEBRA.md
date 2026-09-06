# F250 exact algebra before the scan

## Pell powers and canonical wrapping

Fix a positive nonsquare integer (D) and a positive norm-one Pell unit

\[
\varepsilon=S_1+T_1\sqrt D.
\]

Write

\[
\varepsilon^j=S_j+T_j\sqrt D,
\qquad S_j^2-DT_j^2=1.
\]

For an odd semiprime (N), set

\[
y_j=[T_j]_N,
\qquad x_j=[S_j]_N,
\qquad A_j=1+Dy_j^2.
\]

Then (A_j\equiv x_j^2\pmod N).  If (0\le T_j<N), canonical reduction has
not wrapped and

\[
A_j=1+DT_j^2=S_j^2
\]

is an exact integer square.  Thus every pre-wrap row is a singleton-square
case.  Its positive exact root is (S_j), and comparing it with the supplied
root (x_j) either factors (N) or proves a global normalized sign.

The same statement applies to every post-wrap row that happens to be an
exact square.  Indeed, an exact square (A_j=R^2) gives another nonnegative
Pell solution (R+y_j\sqrt D).  Every nonnegative solution is a power of the
fundamental Pell unit.  Hence (y_j=T_k) for an earlier Pell index (k)
whenever (y_j<T_j).  Every post-wrap singleton square is therefore a
collision of the wrapped coefficient with an earlier exact Pell coefficient.
The supplied-root comparison again either factors (N) or proves a global
sign.

Because (D>0) and the canonical coordinates are nonnegative,

\[
A_j=A_k\iff y_j=y_k.
\]

If two supplied roots for one repeated row are not globally equal up to sign,
their ratio is a mixed square root of one and the two sign gcds factor (N).
Otherwise the duplicate contributes only the same global root class and can
be removed without changing the useful normalized-root image.

## Tangent-law triples are inert

The norm-one group law gives the rational tangent coefficient

\[
t={y+z\over1-Dyz}.
\]

Let (y,z\ge1), and assume the denominator is nonzero and (t) is an
integer.  Put (d=Dyz-1>0).  Then (d\mid y+z), so

\[
Dyz-1\le y+z. \tag{1}
\]

Suppose first that (D\ge2), and take (y\le z).  If (y\ge2), then

\[
Dyz-1-y-z
\ge 2yz-1-y-z
=(y-1)(z-1)+yz-2>0,
\]

contradicting (1).  Thus (y=1).  Inequality (1) becomes

\[
(D-1)z\le2.
\]

The only cases, up to swapping (y,z), are

\[
(D;y,z)=(2;1,1),(2;1,2),(3;1,1).
\]

Their absolute tangent coordinates are respectively (2,1,1).  Each is an
input coordinate, so none is a distinct positive-coordinate triple.  The
case (yz=0) uses the trivial row (A_0=1).

For completeness, (D=1) gives

\[
(y-1)(z-1)\le2.
\]

The divisibility condition leaves only

\[
(y,z)=(1,2),(1,3),(2,3)
\]

and swaps, apart from the undefined denominator at ((1,1)).  Each again
has absolute tangent coordinate equal to an input coordinate.  Also (D=1)
has no nonzero positive solution of (S^2-T^2=1).

Therefore the rational tangent identity produces no genuine triple with
three distinct positive integer coordinates for any positive nonsquare
(D).  Any live Pell/P66 event must be an ordinary-prime square-class
hypercycle outside this tangent identity.

