# F259 algebra — full Pell lifts and bounded symbolic atoms

Fix an odd public modulus `N`, a positive nonsquare discriminant `D`, and
one exact norm-one Pell row

\[
S^2-DT^2=1.
\]

Use least nonnegative residues and full public quotients

\[
S=x+N\ell,\qquad T=y+Nk,\qquad 0\le x,y<N.
\]

Everything below is computable from `N`, `D`, and a materialized Pell
index. Hidden factors are not inputs.

## Row identities

The norm digit

\[
q={x^2-Dy^2-1\over N}
\]

is integral and satisfies

\[
\boxed{q=-2(x\ell-Dyk)-N(\ell^2-Dk^2).}
\]

The two tangent principal-digit defects are

\[
g_-=k(x-1)-y\ell={T(x-1)-y(S-1)\over N},
\]

\[
g_+=k(x+1)-y\ell={T(x+1)-y(S+1)\over N}.
\]

They obey only the tautological linear relations

\[
g_+-g_-=2k,\qquad g_++g_-=2(kx-y\ell).
\]

The search therefore does not treat the sum and difference as independent
row atoms. It retains `g_-` and `g_+` themselves.

## Exact multiplication carries

For two rows in one Pell orbit, write `t=i+j` and define

\[
a_{ij}={x_ix_j+Dy_iy_j-x_t\over N},
\qquad
b_{ij}={x_iy_j+y_ix_j-y_t\over N}.
\]

Both are integers. Expansion of Pell multiplication gives

\[
\boxed{
\ell_t=a_{ij}+x_i\ell_j+x_j\ell_i
+D(y_ik_j+y_jk_i)+N(\ell_i\ell_j+Dk_ik_j),}
\]

\[
\boxed{
k_t=b_{ij}+x_ik_j+x_jk_i+y_i\ell_j+y_j\ell_i
+N(\ell_ik_j+k_i\ell_j).}
\]

These equations are exact self-tests. They also show why `a,b` must be
searched jointly with both quotient coordinates, rather than only with the
old `T` quotient `k`.

## Quadratic-resultant template

For public integer pairs `(u,v)` and `(U,V)`, let

\[
f(X)=1+D(u-vX)^2,\qquad h(X)=1+E(U-VX)^2.
\]

With `delta=uV-Uv`, their exact resultant is

\[
\boxed{
\operatorname{Res}(f,h)=
[DE\,\delta^2+Ev^2+DV^2]^2-4DEv^2V^2.}
\]

When `D=E`, it factors as

\[
D^2\,[D\delta^2+(v-V)^2]\,[D\delta^2+(v+V)^2].
\]

F259 applies this template to full lift vectors `(ell,k)`, tangent vectors
`(g_-,g_+)`, and multiplication-carry vectors `(a,b)`. The old `(y,k)`
factors remain as controls.

## Second carry curvature

For odd `h`, let `F_(h,D)` be the Pell multiplication polynomial defined by

\[
(1+DY^2)G_{h,D}(Y)^2=1+D F_{h,D}(Y)^2.
\]

For an index `i`, put

\[
F_{h,D}(y_i)=y_{hi}+c_{h,i}N.
\]

For an outer multiplier `r` in `{3,5}`, set `z=y_(hi)` and define the exact
second carry

\[
E_{r\mid h,i}=
{F_{r,D}(z+c_{h,i}N)-F_{r,D}(z)-c_{h,i}N F'_{r,D}(z)\over N^2}.
\]

Polynomial Taylor expansion proves integrality. For `r=3`,

\[
\boxed{E_{3\mid h,i}=4D c_{h,i}^2(3z+c_{h,i}N).}
\]

For `r=5`,

\[
\boxed{
E_{5\mid h,i}=4D c_{h,i}^2 B_{5\mid h,i},}
\]

where

\[
B_{5\mid h,i}=5(3z+cN)
+4D(10z^3+10z^2cN+5zc^2N^2+c^3N^3).
\]

The frozen grammar records the full `E` and the primitive displayed bracket.
This is a second-order carry family. F255 used only first carries.

## Public `N`-primitive normalization

For each nonzero symbolic atom `w`, F259 divides out every exact public
power of `N` before a gcd or word insertion:

\[
\operatorname{prim}_N(w)=|w|/N^{v_N(w)}.
\]

Here `v_N(w)` means repeated exact division by the composite integer `N`,
not a prime-adic valuation. Exact zero and resulting unit atoms are neutral.
This removes global `N`-multiple identities without factoring `N`. No other
content is removed.
