# F242 candidate — an unfactored word gives an exact Miller law in every quadratic-torus orientation

## Status and scope

This is a proof-only reduction for distinct odd semiprimes.  It is not an
all-input factoring algorithm.  It does not construct the required
quasipolynomial-size integer word.

Let

\[
 N=pq
\]

with distinct odd primes `p` and `q`.  Let `D` be a public integer.  A
proper value of `gcd(D,N)` is already a factor.  On the unit branch, put

\[
 \epsilon_p=\left({D\over p}\right),\qquad
 \epsilon_q=\left({D\over q}\right),\qquad
 J=\epsilon_p\epsilon_q=\left({D\over N}\right).
\]

The Jacobi symbol `J` is public.  The two local quadratic norm-one tori are
cyclic of orders

\[
 m_p=p-\epsilon_p,\qquad m_q=q-\epsilon_q.
\]

Define

\[
 d=\gcd(m_p,m_q),\qquad s_p={m_p\over d},\qquad
 s_q={m_q\over d}.
\]

Thus `gcd(s_p,s_q)=1`.  Let `W>=1` be any public integer.  Its
factorization is not supplied or required.  Put

\[
 E=(N-J)W,
\]

\[
 r_p={s_p\over\gcd(s_p,W)},\qquad
 r_q={s_q\over\gcd(s_q,W)},
 \qquad
 \alpha_p={1\over r_p},\quad \alpha_q={1\over r_q}.
\]

Write

\[
 e_i=v_2(m_i),\qquad v=v_2(E),\qquad
 h_i=\min(e_i,v)\quad(i=p,q),
\]

and let `a=min(h_p,h_q)` and `b=max(h_p,h_q)`.  Every `m_i` and `N-J`
is even, so `h_p,h_q>=1`.  Define

\[
 \mu_{a,b}=1-{4^a+2\over3\,2^{a+b}}.                 \tag{1}
\]

## Exact factor-free sampler

Work in

\[
 A_D=(\mathbb Z/N\mathbb Z)[w]/(w^2-D),
 \qquad \overline{x_0+x_1w}=x_0-x_1w.
\]

For fixed unit `D`, repeatedly sample `A,B` independently and uniformly
modulo `N`.  The optional coefficient screen

\[
 c=\gcd(N,A,B)
\]

returns `c` when it is proper and rejects when `c=N`.  Compute

\[
 \nu=A^2-DB^2\pmod N,
 \qquad g_\nu=\gcd(\nu,N).
\]

Return a proper `g_nu`; reject when `g_nu=N`; and, when `g_nu=1`, set

\[
 U={A+Bw\over A-Bw}
   ={A^2+DB^2\over\nu}+{2AB\over\nu}w.               \tag{2}
\]

The inverse in (2) is taken only after the norm gcd has certified it.
After this normalization, multiplication, squaring, and powering use the
division-free coefficient rule

\[
 (x_0,x_1)(y_0,y_1)
 =\bigl(x_0y_0+Dx_1y_1,\ x_0y_1+x_1y_0\bigr)\pmod N. \tag{3}
\]

Conditional on acceptance, the reductions `U_p` and `U_q` are independent
uniform elements of their full local tori.  This includes `+1` and `-1`.
No Cayley-chart point is omitted.  The acceptance probability of one
coefficient pair is at least `16/81`, so the expected number of pairs is at
most `81/16`.  A proper coefficient or norm gcd only ends the procedure
earlier with a verified factor.

## One exact powered trial

For a pair `Y=(y_0,y_1)`, define the joint-coordinate identity screens

\[
 G_+(Y)=\gcd(N,y_0-1,y_1),\qquad
 G_-(Y)=\gcd(N,y_0+1,y_1).                            \tag{4}
\]

Compute `V=U^E` using (3).  Return `G_+(V)` when it is proper.  If
`G_+(V)=1`, declare the powered trial null.  If `G_+(V)=N`, write
`E=2^v u` with `u` odd.  Starting at `Y_0=U^u`, square successively and
test both values in (4) at every step.  Return only a verified proper gcd.
If no proper gcd appears, declare the powered trial null.

For the accepted uniform point, the two local return events are independent
and have exact probabilities

\[
 \Pr(U_p^E=1)=\alpha_p,
 \qquad
 \Pr(U_q^E=1)=\alpha_q.                              \tag{5}
\]

Conditional on the global return `U^E=1` in both local tori, the square
chain returns a factor with exact probability `mu_{a,b}`.  Consequently the
clean powered phase returns a factor with exact probability

\[
 \boxed{
 S=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
 }                                                     \tag{6}
\]

Moreover,

\[
 \mu_{a,b}\ge {1\over2},
 \qquad
 \boxed{S\ge{1\over2\min(r_p,r_q)}.}                 \tag{7}
\]

Sampler gcd exits can only increase the complete procedure's success
probability.  Thus, if `min(r_p,r_q)<=R`, fresh trials split `N` almost
surely in at most `2R` expected clean powered trials.  If `log W` and `R`
are numerical quasipolynomial in `log N`, all sampling, algebra arithmetic,
powering, square-chain tests, and gcd verification have expected numerical-
quasipolynomial cost.

## Four orientations and the exact remaining source

For a fixed word `W`, varying a unit discriminant changes the probability
law only through

\[
 (\epsilon_p,\epsilon_q)\in
 \{(+,+),(+,-),(-,+),(-,-)\}.                         \tag{8}
\]

If `D` is sampled uniformly from the units modulo `N`, these four hidden
orientations are independent and equiprobable.  To preserve this law, keep
the chosen `D` and resample only `(A,B)` until (2) is clean.  Rejecting the
whole pair `(D,A,B)` would bias the orientations because the split and
nonsplit algebras have different unit densities.

For each orientation `epsilon`, let `R_epsilon` be its value of
`min(r_p,r_q)`.  A fresh uniform `D` and a clean torus point therefore give

\[
 \Pr(\text{powered factor})
 ={1\over4}\sum_\epsilon S_\epsilon
 \ge {1\over8\min_\epsilon R_\epsilon}.              \tag{9}
\]

The `(+,+)` residual pair is the ordinary P205 pair.  The other three are
the shifted pairs made from `p+1` and/or `q+1`.  Thus the torus construction
adds three exact residual interfaces, with only a constant orientation
loss.  It does not prove that one of the four residuals is small.

On the infinite P158/F172 family, all four common shifted gcds are at most
six.  With `W=1`, every `R_epsilon` is `2^{Theta(log N)}`, and every clean
powered success probability is exponentially small.  The incidental
random zero-divisor screens also have only `O(1/p)` probability per
constant-cost sampling stage.  Hence a quasipolynomial number of bare
orientation trials does not solve that family.

This use of P158 is narrow.  It does not obstruct a word that absorbs a
large part of a shifted residual.  If `W` is allowed to depend materially
on the full value of `D`, that dependence is a new integer-source proposal,
not a consequence of the four-orientation torus law, and requires its own
all-input progress proof.

