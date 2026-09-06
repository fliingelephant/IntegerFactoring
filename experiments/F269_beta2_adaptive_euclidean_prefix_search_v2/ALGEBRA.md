# F269-D02 algebra — adaptive Euclidean beta-two prefix states

## Status

**Status:** frozen D02 algebra contract. Its mathematical claims are the D01
algebra contract without a semantic change; only version/status wording moved.
Five earlier draft states each received `KILL/REVISE`; all five failed
verdicts remain attached to their exact bytes. This file authorizes source
implementation, self-tests, and the registered stress preflight. It does not
authorize a production cohort.

F269 grants a correct reciprocal prefix. It does not compute that prefix. It
searches for a public Archimedean statistic that selects the next ordinary
factor bit, then converts it to the next reciprocal bit by an exact public
formula.

Assume

\[
 N=pq,\qquad p<q<2p,
\]

where `p` and `q` are distinct odd primes. Let

\[
 m=2^t,\qquad t\ge1,\qquad 2m<p,
\]

and grant

\[
 u\equiv p^{-1}\pmod m.
\]

Use the canonical odd residues

\[
 r\equiv u^{-1}\equiv p\pmod m,
 \qquad c\equiv Nu\equiv q\pmod m,
 \qquad 1\le r,c<m.
\]

Put

\[
 K={N-rc\over m},\qquad \delta=K\bmod2,
 \qquad \kappa={ur-1\over m}\bmod2.
\]

The quotient `(ur-1)/m` is integral because `ur=1 mod m`. Take its canonical
residue modulo two. All quantities in this setup are public after the prefix
grant.

The branch label below is the next ordinary factor bit

\[
 p=r+am\pmod {2m}.
\tag{0a}
\]

The actual next reciprocal bit `e` is defined by

\[
 p^{-1}=u+em\pmod {2m}.
\tag{0b}
\]

Expanding the product in (0a)--(0b) gives

\[
 (u+em)(r+am)
 \equiv1+(\kappa+a+e)m\pmod {2m}.
\]

Hence the exact public conversion is

\[
 \boxed{e=a\mathbin{\mathsf{xor}}\kappa,
 \qquad a=e\mathbin{\mathsf{xor}}\kappa.}
\tag{0c}
\]

F269 expressions compare the two factor-lift branches `a=0,1`. Every
reported reciprocal prediction is obtained only after applying (0c).
The identity has both behaviors. For `m=4,u=r=1`, one has `kappa=0`.
For `m=8,u=r=3`, one has `ur=9` and `kappa=1`. These are mandatory exact
self-test fixtures; the second prevents silently equating `a` with `e`.

## 1. The four quotient corners form one translated rectangle

For `x,y` in `{0,1}`, define

\[
 R_x=r+xm,\qquad C_y=c+ym,
\]

and the scaled quotient corner

\[
 Z_{xy}={N-R_xC_y\over m}.
\tag{1}
\]

Direct expansion gives

\[
 \boxed{Z_{xy}=K-xc-yr-xym.}
\tag{2}
\]

Thus

\[
 \boxed{
 \{Z_{00},Z_{10},Z_{01},Z_{11}\}
 =\{K,K-c,K-r,K-r-c-m\}.}
\tag{3}
\]

Let

\[
 b_a=a\mathbin{\mathsf{xor}}\delta.
\]

The two product-compatible corners are `Z_(a,b_a)`. The two crossed corners
are `Z_(a,1-b_a)`. Therefore `delta` changes only which two corners are
called compatible. It does not change the rectangle.

In the F210 notation for the compatible quotient `K_a`, define the crossed
scaled corner `J_a` by

\[
 2K_a=Z_{a,b_a},\qquad J_a=Z_{a,1-b_a}.
\tag{4}
\]

This is an exact normalization of all four F210 quotient children. The new
letter `J` avoids conflict with P185's separate notation `H_a=2mK_a`.

Each corner is positive. Indeed, `R_x,C_y<2m<p`, so `R_xC_y<p^2<N`.
Each corner is also a unit modulo `N`:

\[
 mZ_{xy}\equiv-R_xC_y\pmod N,
\]

and `m,R_x,C_y` are units modulo `N`. Hence

\[
 \boxed{\gcd(Z_{xy},N)=1.}
\tag{5}
\]

Likewise,

\[
 \boxed{
 \gcd(Z_{xy},R_x)=\gcd(Z_{xy},C_y)=1.}
\tag{6}
\]

For example, multiply (1) by the inverse of `m` modulo `R_x`, then use
`gcd(N,R_x)=1`. Equation (6) kills any claim that the full Euclidean chain
against one of its own lifted coordinates ends in a nontrivial support
factor. Its intermediate quotients and remainders can still be asymmetric.

## 2. Exact difference table and the affine-shell kill gate

Put

\[
 S=r+c+m.
\]

The six unsigned corner differences are exactly

\[
\begin{array}{c|c}
\text{corner pair}&\text{difference}\\ \hline
00,10&c\\
00,01&r\\
00,11&S\\
10,01&|r-c|\\
10,11&r+m\\
01,11&c+m.
\end{array}
\tag{7}
\]

Every difference is public and is less than `3m`. Any integer affine
combination of the four corners reduces to

\[
 \lambda K+A r+B c+C m
\]

for public integer coefficients. F269 therefore removes duplicate affine
expressions before program synthesis. It does not score a raw difference as
a new selector.

Use the registered nonterminal stages

\[
 1\le t<t_{\rm terminal},\qquad
 t_{\rm terminal}=\left\lfloor{n-1\over4}\right\rfloor,
 \qquad n=\operatorname{bitlength}(N).
\tag{8}
\]

If this range is nonempty, `n>=9`. Its largest `t` satisfies

\[
 4t\le n-5.
\]

Since `N>=2^(n-1)`, this implies both `m^4<N` and

\[
 \boxed{N>8m^2.}
\tag{9}
\]

For two distinct corners, write the larger as `A`, the smaller as `B`, and
their difference as `d`. Equations (7) and (9) give

\[
 B\ge Z_{11}={N-(r+m)(c+m)\over m}
 >{N\over m}-4m>4m>S\ge d.
\]

Therefore their first Euclidean division is always

\[
 \boxed{A=1\cdot B+d.}
\tag{10}
\]

This corrects the tempting but false statement that the whole Euclidean
chain has at most two divisions. After (10), the live tail is the exact
Euclidean chain of `(B,d)`. It can have several nonconstant quotients. F269
starts each pair feature after the forced quotient one.

## 3. Branch-local linear carries also collapse

For either candidate `a`, direct use of (2) gives

\[
 \boxed{
 \bigl\{|J_a-2K_a|,\ |J_{1-a}-2K_a|\bigr\}
 =\{R_a,C_{b_a}\}.}
\tag{11}
\]

Thus the most natural `J-2K` carries return the already public lifted
coordinates. F269 registers them as positive controls and forbids their use
as finite leads.

Equations (3), (7), and (11) are the exact boundary for the affine F210
quotient grammar. The surviving grammar must contain a floor, quotient,
remainder, continued fraction, or another nonlinear integer operation.

## 4. The two same-coordinate resultants are symbolic controls

Let `h=2m`, and define the two compatible quotient charts

\[
 F_a(P,Q)=hPQ+C_{b_a}P+R_aQ-K_a.
\tag{12}
\]

Fix the ordered resultant convention before eliminating anything. If

\[
 f=A_0Q+B_0,\qquad g=A_1Q+B_1,
\]

then

\[
 \operatorname {Res}_Q(f,g)=A_0B_1-A_1B_0.
\tag{12a}
\]

In particular, `F_0` is always the first polynomial and `F_1` is always the
second. Eliminate `Q` between them and use the physical coordinate

\[
 X=hP+r.
\]

The exact ordered resultant

\[
 R_Q(P)=\operatorname {Res}_Q(F_0,F_1)
\]

satisfies

\[
 \boxed{
 2R_Q(P)=
 \begin{cases}
 X^2+mX+N,&\delta=0,\\
 N-X^2-mX,&\delta=1.
 \end{cases}}
\tag{13}
\]

The first polynomial has no real zero. An integer zero of the second gives

\[
 N=X(X+m).
\tag{14}
\]

It therefore factors `N` directly and forces `q-p=m` after ordering.

Eliminating `P` uses the same ordered convention: write
`F_a=A_aP+B_a` and set `R_P(Q)=A_0B_1-A_1B_0`. With `Y=hQ+c`, the exact
sign is

\[
 \boxed{
 2R_P(Q)=
 \begin{cases}
 Y^2+mY+N,&\delta=0,\\
 Y^2+mY-N,&\delta=1.
 \end{cases}}
\tag{15}
\]

There is no division or sign normalization in the checked identities: the
left sides are literally `2*R_Q` and `2*R_P` under (12a). Equivalently, in
ascending coefficient order in the chart variables `P,Q`,

\[
\begin{array}{c|c|c}
 &\delta=0&\delta=1\\ \hline
2R_Q(P)&
(r^2+mr+N,\ h(2r+m),\ h^2)&
(N-r^2-mr,\ -h(2r+m),\ -h^2)\\
2R_P(Q)&
(c^2+mc+N,\ h(2c+m),\ h^2)&
(c^2+mc-N,\ h(2c+m),\ h^2).
\end{array}
\tag{15a}
\]

The coefficient tuples in (15a), and evaluations at the literal chart
points

\[
 \boxed{-2,-1,0,1,2,3}
\tag{15b}
\]

are verification-only symbolic controls. They are not integer row controls
and their evaluated values are never compared with a scoreable row value.
For discriminant reporting only, multiply the `delta=1` polynomial in (13)
by `-1` to make it monic. The four reported discriminants are therefore
`m^2-4N` for both `delta=0` polynomials and `m^2+4N` for both `delta=1`
polynomials. This sign normalization changes neither ordered resultant.

Under (8), the bound `m^4<N` implies that `q-p=m` is a first-Fermat-trial
modulus. Indeed, with `A=(p+q)/2`,

\[
 A^2-N=(m/2)^2
\]

and `(A-1)^2<N`. Thus `A=ceil(sqrt(N))`. F269 screens the first Fermat
trial before scoring. It excludes (13)--(15), their discriminants, and
algebraically identical formulas from the search grammar.

## 5. The surviving public Archimedean seam

For each formally registered corner pair, first compute its actual unsigned
gap. If that gap is zero, the tail constructor returns the nonnumeric state
`ZERO_GAP`. It performs no Euclidean division and supplies no scalar root.
Otherwise remove the forced first quotient in (10).
The residual state is

\[
 (B,d),
\]

where `B` is the smaller corner and `d` is one of the six public gaps in
(7). The raw pair `(B,d)` is constructor-only. It is not a scoreable scalar.
F269 derives bounded strict-prefix statistics after at least one further
Euclidean division:

- single quotients, remainders, and centered remainders;
- strict-prefix continuants of lengths 2, 4, and 8, never a completed
  continued fraction or its terminal gcd scale;
- cross-chain determinants between branch-equivariant tails; and
- a fixed bounded list of typed adaptive compositions.

The orientation and continuant convention are fixed as follows. Every tail
starts with an ordered positive state

\[
 x_0>x_1>0.
\]

For a valid pair tail this is `(x_0,x_1)=(B,d)`, after deleting the forced
corner quotient one. For a coordinate tail it is
`(corner,own-coordinate)`. For
`j>=1`, while `x_j>0`, perform the unique Euclidean division

\[
 x_{j-1}=q_jx_j+x_{j+1},\qquad
 q_j=\left\lfloor{x_{j-1}\over x_j}\right\rfloor,qquad
 0\le x_{j+1}<x_j.
\tag{16}
\]

A prefix of depth `d` is the ordered quotient word
`(q_1,...,q_d)` in this direction. Its numerator and denominator continuants
are

\[
 P_0=1,\quad Q_0=0,\qquad P_1=q_1,\quad Q_1=1,
\tag{17}
\]

and, for `2<=j<=d`,

\[
 P_j=q_jP_{j-1}+P_{j-2},\qquad
 Q_j=q_jQ_{j-1}+Q_{j-2}.
\tag{18}
\]

Thus `P_d/Q_d=[q_1;q_2,...,q_d]`, and the sign convention is checked by

\[
 \boxed{P_dQ_{d-1}-P_{d-1}Q_d=(-1)^d.}
\tag{19}
\]

For an ordered registered tail pair `(T,T')`, the signed cross-continuant is

\[
 \boxed{D_d(T,T')=P_d(T)Q_d(T')-Q_d(T)P_d(T').}
\tag{20}
\]

The listed role order is part of the syntax. F269 does not take an absolute
value and does not sort the two tails; reversing them negates `D_d`.
The strict-prefix predicate for every step-`d` quotient, remainder, centered
remainder, aggregate, or continuant is `x_(d+2)>0`. Its one extra division is
only a lookahead. It does not append `q_(d+1)` to (17)--(20). Failure of this
predicate is the nonnumeric state `DEPTH_MISSING`; a numeric sentinel is
forbidden. A cross-continuant at depth `d` exists only when both input tails
have valid strict prefixes at depth `d`. It otherwise propagates
`ZERO_GAP` if either tail has that state, and `DEPTH_MISSING` otherwise.

It also runs the Euclidean chain of each corner against its own two lifted
coordinates. Equation (6) makes the final gcd a global unit. The intermediate
integer quotients remain admissible.

Formal tail roles need not be distinct as actual public states. The exact
non-Fermat witness

\[
 N=10541=83\cdot127,\quad t=2,\quad m=4,\quad u=r=c=3,
 \quad K=2633,\quad\delta=1
\]

has `PC:R=OC:C` in both candidate branches. For `a=0`, both states are
`(2630,3)` and begin with quotient 876 and remainders 2,1. For `a=1`, both
are `(2630,7)` and begin with quotient 375 and remainders 5,2. Thus distinct
syntax or provenance labels cannot prevent an expression such as
`floor_div(x,x)=1`. The operational grammar must canonicalize actual public
tail and value aliases on every row, and reject equal operands and
control-valued results before scoring. This check is factor-free because all
states are functions of `(N,t,u)`.

The same witness fixes both zero-gap edge cases used by the later self-test.
At `t=1`, one has `m=2,u=r=c=1,K=5270,delta=0`, so `Z_10=Z_01` and the
formal pair tail `PX:OX` is `ZERO_GAP` in both candidate branches. At `t=2`,
one has the values displayed above and `delta=1`, so `PC:OC` is `ZERO_GAP`
in both branches. More generally `t=1` always has `r=c=1` and
`Z_10=Z_01`; according to `delta`, exactly the registered diagonal role pair
`PX:OX` (`delta=0`) or `PC:OC` (`delta=1`) has zero gap. The constructor must
invalidate it before any quotient or remainder is requested. Provenance
labels cannot turn a zero actual gap into a valid tail.

These exact floors are not among the odd-local invariants that P185 proves
equal: a half-translation can change an ordinary integer quotient or
remainder. They are not congruence jets. They use exact Archimedean division
on public `O(n)`-bit integers and take polynomial bit time per expression.
This distinction makes the seam materially new; it does not prove that the
seam contains a selector.

No theorem says that one of them selects the factor-lift bit `a`. F269 is a
finite symbolic discovery search for such a theorem candidate. Equation
(0c) then converts any candidate `a` prediction to the reciprocal bit `e`.

## 6. Operational and recursion boundary

F269-D02 has one operational lane only. It uses `N,m,u,r,c,K` and public
integer arithmetic. It does not factor any quotient child. It makes no
recursive call.

Complete factorizations of late-stage corners would be fixed-ratio side calls
only inside an independently correct all-input factoring dispatcher covered
by the P183 recurrence. No such dispatcher is supplied here. Therefore
child-factor fingerprints are absent from D02. They cannot affect expression
generation, canonicalization, discovery ranking, held-out selection, or lead
status.

If a later immutable version adds them without first supplying that
dispatcher, it must label every such field `ORACLE_DIAGNOSTIC`, cap it
separately, and forbid it from every operational verdict.

## 7. Evidence boundary

All identities above are elementary exact identities. They do not factor an
input or evaluate the missing factor-lift bit `a` or reciprocal bit `e`. A
finite exact selector would remain a conjecture until a proof covers every
promised modulus and every registered stage. A finite null would close only
the frozen expression grammar and cohorts.
