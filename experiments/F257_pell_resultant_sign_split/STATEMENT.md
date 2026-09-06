# F257 statement — signed Pell-resultant refinement

## Status and scope

This is a proof-only refinement of P217 for two rows with the same positive
discriminant. It has three conclusions.

1. Every odd rational prime power shared by the two specialized row values
   has a public and unique coordinate sign.
2. The two signs feed the two explicit same-discriminant resultant factors.
3. A Jacobi-minus-one discriminant and a short nonzero carry combination
   make either resultant factor a one-sided Las Vegas gcd ticket.

The sign label does not determine the normalized-root sign of a P66 square
relation. The packet gives no inverse-quasipolynomial lower bound for the
ticket event and is not a factoring algorithm.

## Setup

Let \(N\ge3\) be odd and let \(D>0\). For two canonical Pell rows write

\[
 S_h^2-DT_h^2=1,\qquad T_h=y_h+k_hN,\qquad 0\le y_h<N
\]

for \(h=i,j\), and put

\[
 A_h=1+Dy_h^2,\qquad x_h=S_h\bmod N.
\]

Assume \(y_i\ne y_j\), as after the usual duplicate-coordinate cleanup.
Since the coordinates are nonnegative, both
\(y_i-y_j\) and \(y_i+y_j\) are then nonzero.

The square-root comparison is made only after the public screens

\[
 \gcd(D,N)=\gcd(x_i x_j,N)=1.
\]

For the resultant statements assume \(k_i,k_j>0\), and define

\[
 f_h(X)=1+D(T_h-k_hX)^2,\qquad
 \Delta=T_i k_j-T_j k_i.
\]

The carry determinant has the three exact forms

\[
 \boxed{
 \Delta=y_i k_j-y_j k_i
 ={T_jy_i-T_iy_j\over N}.}
\]

## A. Exact shared-gcd sign split

Set

\[
 u=y_i-y_j,\qquad v=y_i+y_j,\qquad
 d=\gcd(A_i,A_j),
\]

\[
 d_-=\gcd(A_i,u),\qquad d_+=\gcd(A_i,v).
\]

Then

\[
 \boxed{d=\gcd(A_i,uv),\qquad d_-\mid d,\qquad d_+\mid d.}
\]

Write \(z_{\rm odd}=z/2^{v_2(z)}\). The odd part splits exactly:

\[
 \boxed{
 d_{\rm odd}=(d_-)_{\rm odd}(d_+)_{\rm odd},\qquad
 \gcd((d_-)_{\rm odd},(d_+)_{\rm odd})=1.}
\]

Equivalently, every odd prime power in \(d\) occurs to its full exponent in
exactly one of \(d_-\) and \(d_+\). The minus label means
\(y_i\equiv y_j\); the plus label means \(y_i\equiv-y_j\).

There are two separate factor-of-two effects. Exactly,

\[
 \gcd(d_-,d_+)=\gcd(A_i,u,v)\in\{1,2\},
\]

and

\[
 \boxed{d=\operatorname{lcm}(d_-,d_+)2^\eta,\qquad \eta\in\{0,1\}.}
\]

If \(a=v_2(A_i)\), \(b=v_2(u)\), and \(c=v_2(v)\), then

\[
 \eta=\min(a,b+c)-
 \max\{\min(a,b),\min(a,c)\}.
\]

The value \(\eta=1\) occurs exactly when \(D,y_i,y_j\) are odd and

\[
 v_2(A_i)\ge v_2(uv).
\]

Thus an unqualified full-integer identity
\(d=\operatorname{lcm}(d_-,d_+)\) is false. For example,
\(D=7,y_i=1,y_j=3\) gives

\[
 d=8,\qquad d_-=2,\qquad d_+=4.
\]

The correction is public and is irrelevant to gcd extraction against the
odd modulus \(N\). It must still be retained in an exact integer
square-class decoder.

## B. Signed resultant factors and orbit formulas

Define

\[
 Q_-=D\Delta^2+(k_i-k_j)^2,\qquad
 Q_+=D\Delta^2+(k_i+k_j)^2.
\]

P217's same-discriminant resultant factors as

\[
 \boxed{\operatorname{Res}_X(f_i,f_j)=D^2Q_-Q_+.}
\]

The sign split feeds these factors with full integer divisibility:

\[
 \boxed{d_-\mid Q_-,\qquad d_+\mid Q_+.}
\]

Consequently every odd shared prime power is placed in one explicit
resultant factor without factoring \(A_i\), \(A_j\), or the resultant.
The converse is false: \(Q_-\) or \(Q_+\) can have prime divisors that are
not shared by the two row values.

If the two rows are powers in one Pell orbit and \(i<j\), then

\[
 \boxed{
 Q_-=(k_iS_j-k_jS_i)^2+2k_ik_j(S_{j-i}-1),}
\]

\[
 \boxed{
 Q_+=(k_iS_j+k_jS_i)^2-2k_ik_j(S_{i+j}-1).}
\]

These are exact formulas in the orbit indices and the canonical-wrap
carries. They do not imply that either \(Q_-\) or \(Q_+\) has a useful
hidden-prime divisor.

## C. One-sided Jacobi-minus-one gcd tickets

Now let

\[
 N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes, and assume

\[
 \left({-D\over N}\right)=-1.
\]

Thus \(-D\) is a square at exactly one hidden prime, denoted \(r_{\rm sp}\),
and a nonsquare at the other, denoted \(r_{\rm ns}\).

For \(\sigma\in\{-,+\}\), put

\[
 a_-=k_i-k_j,\qquad a_+=k_i+k_j.
\]

If

\[
 \boxed{0<|a_\sigma|<\sqrt{N/2},}
\]

then

\[
 \boxed{
 \gcd(Q_\sigma,N)\in\{1,r_{\rm sp}\}.}
\]

It equals \(r_{\rm sp}\) exactly when \(r_{\rm sp}\mid Q_\sigma\). In
particular, it can never equal \(N\). If \(w^2\equiv-D\pmod {r_{\rm sp}}\),
the success event is the union of the two linear congruences

\[
 a_\sigma\equiv w\Delta\pmod {r_{\rm sp}},\qquad
 a_\sigma\equiv-w\Delta\pmod {r_{\rm sp}}.
\]

This gives an exact conditional Las Vegas interface. If a public source of
admissible pairs makes this event occur with probability at least
\(1/Q(n)\), independent repetition has expected \(Q(n)\) trials, and every
accepted output is certified by a proper gcd. No such inverse-QP source law
is proved here. Uniform or source-independent heuristics cannot be applied
because \(D,\Delta\), and the carries are arithmetically coupled.

## D. Factor-free signed refinement and root-sign boundary

For an explicit bank with one fixed \(D\), all \(d_{ij,-}\) and
\(d_{ij,+}\), their odd parts, all \(Q_{ij,-},Q_{ij,+}\), and their gcds
with \(N\) are computable in polynomial time in the materialized input
length. P66 gcd refinement can be refined further by the signed gcds. Every
resulting odd fragment then has a public row-incidence mask and a consistent
pairwise coordinate-sign label. Binary parity still computes the complete
integer square-class kernel.

The extra sign label does not compute the normalized-root homomorphism. For
a two-row square relation \(A_iA_j=R^2\), the value that matters is

\[
 \rho=R(x_ix_j)^{-1}\pmod N,
\]

whereas \(d_-\) and \(d_+\) record congruences modulo rational primes that
divide the exact integers \(A_i,A_j\). These are different residue systems.

Clean odd-multiple identities make the limitation exact. For odd \(h\),

\[
 1+DF_{h,D}(Y)^2=(1+DY^2)G_{h,D}(Y)^2.
\]

At every odd prime \(\ell\mid1+Dy^2\),

\[
 \boxed{F_{h,D}(y)\equiv(-1)^{(h-1)/2}y\pmod\ell.}
\]

Thus an uncarried retained odd-multiple dependency lies in the minus channel
when \(h\equiv1\pmod4\) and in the plus channel when
\(h\equiv3\pmod4\). P218 proves that its normalized root is nevertheless
\(+1\). Hence neither coordinate sign certifies a useful P66 root.

There is also a same-channel contrast. In the \(D=2,N=13859\) Pell orbit,

\[
 (S_6,T_6)=(19601,13860),\qquad y_6=1,
\]

and the uncarried fifth multiple has \(y_{30}=109\). Therefore

\[
 A_6=3,\qquad A_{30}=23763=3\cdot89^2,\qquad d_-=3,
\]

and the exact root \(267\) equals the supplied product modulo \(N\). This is
a global minus-channel relation. By contrast, the preserved F253 arithmetic
certificate

\[
 N=143,\quad D=2,\quad (y_i,x_i,A_i)=(1,17,3),
\]

\[
 (y_j,x_j,A_j)=(109,5,23763)
\]

has the same minus-channel shared factor \(3\), but

\[
 \gcd(267-85,143)=13,\qquad
 \gcd(267+85,143)=11.
\]

Its normalized root is non-global. That certificate has earlier cleanup
factors, so it is not a screen-free algorithmic hit. Together the two exact
examples show that the minus coordinate label alone does not determine the
supplied-root sign.

## Exact remaining gap

The live requirement is an all-input or inverse-QP law that forces at least
one of the following in a numerical-QP bank:

1. a split-side zero of a short-carry \(Q_-\) or \(Q_+\), giving the direct
   one-sided gcd ticket; or
2. a signed resultant-supported square dependency whose normalized root is
   non-global.

This packet proves neither event. It does not cover cross-discriminant pairs,
for which the \(y_i\pm y_j\) sign split is unavailable.
