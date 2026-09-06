# F127 V2 proof

For (m<N), the integer (K_m) is the canonical carry. Indeed,

\[
w_m={1+K_mN\over m}
\]

is integral, positive, below (N), and satisfies (mw_m\equiv1\pmod N).

If (r\mid s\), both (K_s) and (K_r) solve

\[
NK\equiv-1\pmod r.
\]

Thus (K_s\equiv K_r\pmod r). The range bounds give unique (A,B,T) with

\[
K_{ua}=K_u+uA,
\quad
K_{ub}=K_u+uB,
\quad
K_{uab}=K_u+uT.
\]

Reduction of the last equality against the first two gives

\[
T\equiv A\pmod a,
\qquad
T\equiv B\pmod b.
\]

Hence (A\equiv B\pmod{\gcd(a,b)}), even when (a,b) are not coprime.

Substitute

\[
K_{uab}-K_u=uT,
\qquad
K_{ua}-K_{ub}=u(A-B)
\]

into the P114 residual. This proves the displayed formula.

Put (M=\max(a,b)). Since (T\le ab-1) and
(|A-B|\le M-1),

\[
\begin{aligned}
|\Omega_{\square}|
&\le u(ab-1)(|b-a|+|A-B|)\\
&\le u(ab-1)(|b-a|+M-1)\\
&<2uabM.
\end{aligned}
\]

If this bound is below (h), a nonzero residual has gcd one with (N),
while a zero residual has gcd (N). For (a,b>1), (a\ne b), the actual
eligibility factors

\[
u,a,b,a-1,b-1,b-a
\]

are also nonzero units under the same least-prime bound. The coefficient
(ab-1) is not an eligibility factor.

Now suppose (R\ge2), (u,a,b\le R), and (h>R^6+1). The four corners
are at most (R^3<N), and (R^6+1>2R^4), so the residual result applies.
For a corner (c) with canonical inverse (w), a prime (r\mid N) dividing
(c-w) must divide (c^2-1), and a prime dividing (c+w) must divide
(c^2+1). But

\[
c^2+1\le R^6+1<h\le r.
\]

This is impossible. The case (c=1) gives only the global minus gcd (N).
This proves the complete-channel statement.

For the tail count, every successful ordered triple must use at least one of
the (T_R) large entries. Therefore the number of possibly successful
triples is

\[
Q^3-(Q-T_R)^3\le3T_RQ^2,
\]

which gives density at most (3T_R/Q). Use the (2R^4) hypothesis for the
residual/prefactor channel and the (R^6+1) hypothesis for the full channel.

On balanced (n)-bit semiprimes, (h=2^{\Theta(n)}). Every numerical bound

\[
R=2^{O((\log n)^k)}
\]

satisfies both least-prime inequalities for all sufficiently large (n).
Thus every quasipolynomial-magnitude unreduced rectangle is eventually dead.

## Infinite fixed traps

For (u=1,a=2,b=3) and (N\equiv5\pmod6), the carries are

\[
(K_1,K_2,K_3,K_6)=(0,1,1,1),
\]

so \(\Omega_{\square}=1\). Balanced trial-hard semiprimes occur infinitely
often with (p\equiv1\pmod6\), (q\equiv5\pmod6\).

For (u=1,a=3,b=7) and the odd class (N\equiv23\pmod{42}), the carries
are

\[
(K_1,K_3,K_7,K_{21})=(0,1,3,10),
\]

so \(\Omega_{\square}=0\). Balanced trial-hard semiprimes occur infinitely
often with (p\equiv1\pmod{42}), (q\equiv23\pmod{42}). The mod-42
conditions make every eligibility factor a unit. In both families, all fixed
endpoint screens fail once the factors exceed the fixed corner squares plus
one.

For every fixed finite bank of unreduced rectangles, take one constant larger
than all residual bounds, all eligibility factors, and all corner squares
plus one. Every balanced semiprime whose least factor exceeds this constant
defeats the full bank. Infinitely many such trial-hard semiprimes exist.

## Scope

The theorem forces a successful local rectangle channel into the
exponentially large or wrapped sector. It does not bound the large-value tail,
does not refute F26-Q, and does not address P66.
