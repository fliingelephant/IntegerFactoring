# F275 proof — inherited monomial pullback and cycle holonomy

## 1. Pullback of an exact square relation

Use the notation of Theorem A. Fix `c in F_2^t` whose transformed row
product is an exact square. Define

\[
 Q=\prod_j s_j^{c_j},
 \qquad
 \epsilon=\prod_j\varepsilon_j^{c_j},
\]

and, for each old row,

\[
 z_i=\sum_jc_jM_{ji},
 \qquad
 d_i=z_i\bmod2,
 \qquad
 h_i={z_i-d_i\over2}.
\]

All `h_i` are nonnegative integers. Expanding the transformed product gives

\[
 \begin{aligned}
 \prod_j A_j^{c_j}
 &=Q^2\prod_i a_i^{z_i}\\
 &=\left(Q\prod_i a_i^{h_i}\right)^2
   \prod_i a_i^{d_i}.                               \tag{1}
 \end{aligned}
\]

The left side is a square by hypothesis. Divide it by the displayed positive
integer square. The remaining positive rational number

\[
 \prod_i a_i^{d_i}
\]

is an integer and a rational square. An integer that is a rational square is
an integer square: in lowest terms, the denominator of its rational square
root must divide one. Therefore there is a positive integer `r_d` with

\[
 \prod_i a_i^{d_i}=r_d^2.                            \tag{2}
\]

This proves that `d=M^Tc mod 2` belongs to the old exact square-class kernel.

Taking the positive square root of (1) and using (2) gives

\[
 R_c=Q\left(\prod_i a_i^{h_i}\right)r_d.             \tag{3}
\]

On the modular side, the product of the supplied transformed roots is

\[
 \begin{aligned}
 \prod_jX_j^{c_j}
 &\equiv
 \epsilon Q\prod_i x_i^{z_i}\\
 &=\epsilon Q
   \left(\prod_i x_i^{2h_i}\right)
   \left(\prod_i x_i^{d_i}\right)\\
 &\equiv
 \epsilon Q
   \left(\prod_i a_i^{h_i}\right)
   \left(\prod_i x_i^{d_i}\right)
 \pmod N.                                           \tag{4}
 \end{aligned}
\]

All displayed factors are units modulo `N`. Divide (3) by (4). Since
`epsilon^{-1}=epsilon`, one obtains

\[
 R_c\left(\prod_jX_j^{c_j}\right)^{-1}
 \equiv
 \epsilon r_d\left(\prod_i x_i^{d_i}\right)^{-1}
 =\epsilon\rho_a(d)
 \pmod N.                                           \tag{5}
\]

This is the claimed exact pullback formula.

If `d=0`, then the empty old product has positive root one and supplied root
one. Equation (5) is `epsilon in {+1,-1}`. Every structural-incidence
relation is therefore global.

If `d` is nonzero, (5) is equally important: the transformation may retain
a useful old root, but it does not manufacture a new root class. This is why
Theorem A is a pullback theorem rather than a claim that every monomial
relation is global.

## 2. Why arbitrary root choices require a direct screen

For one transformed row define its inherited root

\[
 Z_j=s_j\prod_i x_i^{M_{ji}}\pmod N.
\]

Both `Z_j` and an arbitrary supplied root `X_j` square to `A_j mod N`.
Hence

\[
 \eta_j=X_jZ_j^{-1}
\]

satisfies `eta_j^2=1 mod N`.

The identities

\[
 \gcd(X_j-Z_j,N)=\gcd(\eta_j-1,N),
\]

\[
 \gcd(X_j+Z_j,N)=\gcd(\eta_j+1,N)
\]

hold because `Z_j` is a unit modulo `N`. If `eta_j` is not a global sign,
the standard signed-root comparison gives a proper divisor of `N`. On the
branch where this comparison gives no factor, `eta_j=+1` or `-1`, so (2) in
the statement holds for a suitable `epsilon_j`.

Thus independently generated roots do not evade the theorem silently. They
either factor immediately or reduce to inherited roots up to global signs.

## 3. Exact square attached to an Eulerian edge set

For the graph source, take an edge set `C subseteq E` in which every selected
vertex degree is even. Then

\[
 \prod_{e=\{u,v\}\in C}A_e
 =\prod_vd_v^{\deg_C(v)}
 =\left(\prod_vd_v^{\deg_C(v)/2}\right)^2.           \tag{6}
\]

This proves that an Eulerian edge set is an exact square relation without
factoring any carrier.

For one inverse-square edge, `T_y(d)` is a canonical unit because both `d`
and `y` are units. Its row satisfies

\[
 dT_y(d)\equiv d(y^2d^{-1})\equiv y^2\pmod N,        \tag{7}
\]

so `y` is a valid supplied root.

## 4. Alternating products on an even cycle

Now let the selected edges be the simple cycle in Theorem B. Every cycle
vertex has degree two, so (6) becomes

\[
 \prod_{i=0}^{2k-1}A_{e_i}
 =\left(\prod_{i=0}^{2k-1}d_{v_i}\right)^2.
\]

Its positive exact root is

\[
 R=\prod_i d_{v_i}.                                  \tag{8}
\]

The even-indexed cycle edges form a perfect matching of the cycle vertices.
Therefore

\[
 \prod_{i\text{ even}}A_{e_i}=\prod_id_{v_i}=R.      \tag{9}
\]

The odd-indexed edges form the other perfect matching, so also

\[
 \prod_{i\text{ odd}}A_{e_i}=R.                     \tag{10}
\]

Use each edge congruence `A_e congruent y_e^2 mod N`. Equations (9) and
(10) give

\[
 R\equiv P_0^2\equiv P_1^2\pmod N.                 \tag{11}
\]

The supplied root of the complete cycle product is

\[
 X=P_0P_1\pmod N.                                   \tag{12}
\]

Every label is a unit. Dividing (11) by (12) yields

\[
 RX^{-1}\equiv P_0P_1^{-1}\pmod N.                 \tag{13}
\]

Interchanging `P_0` and `P_1` gives the inverse of the right side. But its
square is one by (11), so it equals its inverse. This proves both forms in
(11) of the statement.

For the signed gcds, reduce `R-X` modulo `N` using `R congruent P_0^2`:

\[
 R-X\equiv P_0^2-P_0P_1
       =P_0(P_0-P_1)\pmod N.                         \tag{14}
\]

Because `P_0` is a unit modulo `N`, multiplication by `P_0` does not change
the gcd with `N`. Hence

\[
 \gcd(R-X,N)=\gcd(P_0-P_1,N).                       \tag{15}
\]

The same calculation with a plus sign gives

\[
 \gcd(R+X,N)=\gcd(P_0+P_1,N).                       \tag{16}
\]

No integer factorization, gcd-free refinement, or parity elimination is
needed to test these two alternating products.

This argument uses the two perfect matchings of an even cycle. It does not
state the same label-only formula for an odd cycle. Nor does it claim that
the graph-incidence cycle space is the full square-class kernel: additional
dependencies can arise from arithmetic relations among the carriers.

## 5. Exact reduced-complement calculation

For `1<=a<N` with `gcd(a,N)=1`, write

\[
 a^2=qN+r,
 \qquad 1\le r<N.
\]

The remainder is nonzero because `a` is a unit. Put

\[
 c=N-r,
 \qquad t=a-q-1.
\]

Then

\[
 \begin{aligned}
 a(N-a)
 &=aN-a^2\\
 &=(a-q)N-r\\
 &=(a-q-1)N+(N-r)\\
 &=c+tN.                                             \tag{17}
 \end{aligned}
\]

Also `c=[-a^2]_N`. Since `a^2/N<a`, one has `q<=a-1`, and thus `t>=0`.
The lift coordinate is an explicit deterministic function of `a`; it is not
a fresh uniform coordinate.

For even `E`, reduction modulo `N` gives

\[
 (a(N-a))^E\equiv(-a^2)^E=a^{2E}\pmod N,            \tag{18}
\]

so `a^E mod N` is a supplied square root.

Let

\[
 P_E=U_E(a)U_E(N-a).
\]

Each `U_E` is congruent modulo `N^2` to the corresponding exact power.
Therefore

\[
 P_E\equiv(a(N-a))^E\pmod{N^2},
\]

and taking the canonical positive residue gives

\[
 [P_E]_{N^2}=[(a(N-a))^E]_{N^2}=C_E(a).             \tag{19}
\]

Before (19), `P_E` is an exact monomial and Theorem A applies. After (19),
one has an additive identity

\[
 P_E=C_E(a)+\lambda N^2
\]

for some nonnegative integer `lambda`. This additive reduction can remove
all rational-prime factors of the operands. The hypotheses of Theorem A are
therefore absent unless `lambda=0`. No claim about the square-class rank or
private factors of `C_E(a)` follows.

This establishes the stated narrow scope boundary and no more.
