# Proof of the F242 V2 quadratic-torus unfactored-word theorem

## 1. The public exponent contains the exact common shifted part

Fix the two hidden signs `epsilon_p,epsilon_q` and put

\[
 m_p=p-\epsilon_p,\qquad m_q=q-\epsilon_q,
 \qquad J=\epsilon_p\epsilon_q.
\]

Reduction modulo `m_p` gives `p=epsilon_p` and hence

\[
 N-J=pq-\epsilon_p\epsilon_q
 \equiv\epsilon_p(q-\epsilon_q)\pmod {m_p}.
\]

Multiplication by `epsilon_p` does not change a gcd.  Therefore

\[
 \gcd(N-J,m_p)=\gcd(m_p,m_q)=d.                       \tag{P1}
\]

The same calculation with `p` and `q` interchanged proves

\[
 \gcd(N-J,m_q)=d.                                    \tag{P2}
\]

These identities cover all four sign orientations.  In particular,
`d|(N-J)`.  Write `N-J=dA`.  Since `m_p=ds_p`, (P1) gives

\[
 \gcd(A,s_p)=1.
\]

Thus, for `E=(N-J)W`,

\[
 \gcd(E,m_p)
 =\gcd(dAW,ds_p)
 =d\gcd(W,s_p),                                      \tag{P3}
\]

and similarly

\[
 \gcd(E,m_q)=d\gcd(W,s_q).                           \tag{P4}
\]

The two local tori are cyclic.  In the split case they are isomorphic to
the cyclic group `F_r^*`; in the nonsplit case they are subgroups of the
cyclic group `F_{r^2}^*`.  For a uniform element of a cyclic group of order
`m`, the kernel of the `E`-power map has `gcd(E,m)` elements.  Dividing
(P3)--(P4) by `m_p=ds_p` and `m_q=ds_q` proves (5), once the exact uniform
sampler has been established.

## 2. Units and the division-free public representation

For any commutative ring `R`, put

\[
 A_D(R)=R[w]/(w^2-D),
 \qquad \overline{x_0+x_1w}=x_0-x_1w.
\]

The norm is

\[
 \operatorname{Nm}(x_0+x_1w)=x_0^2-Dx_1^2.
\]

An algebra element `z` is a unit exactly when its norm is a unit.  If the
norm is a unit, then

\[
 z^{-1}=\overline z\,\operatorname{Nm}(z)^{-1}.
\]

Conversely, a unit `z` has unit conjugate, so their product
`Nm(z)=z bar(z)` is a unit.

Take `R=Z/NZ`.  The norm gcd in the sampler therefore certifies the only
inverse used in (2).  If `z=A+Bw`, then

\[
 {z\over\overline z}
 =z\,\overline z^{-1}
 ={z^2\over\operatorname{Nm}(z)}
 ={A^2+DB^2\over\nu}+{2AB\over\nu}w.
\]

Its norm is one.  After this single certified normalization, multiplication
is exactly (3), with no division or hidden square root.  The identity points
are `+1=(1,0)` and `-1=(-1,0)`.

For a hidden prime `r`, `z=0` in the local algebra exactly when both
coefficients vanish modulo `r`; the coefficient gcd detects precisely these
prime supports.  In the nonsplit case the algebra is a field, so zero is its
only nonunit.  In the split case there are additional nonzero zero divisors;
their norm is zero and the norm gcd detects them.  Thus the coefficient and
norm screens cover zero elements, split zero divisors, and every attempted
denominator failure.  No inverse is attempted on a nonunit.

If `D` is not a unit modulo `N`, its preliminary gcd either factors `N` or
is `N`; in the latter case that `D` is rejected.  The rest of the proof uses
only unit `D`.  A square `D` modulo one hidden prime causes no singularity:
it is exactly the split algebra treated below.

## 3. Exact local Hilbert--90 fibre counts

Fix an odd prime `r` not dividing `D`, let `k=F_r`, and define

\[
 \phi:A_D(k)^*\longrightarrow T_D(k),
 \qquad \phi(z)=z/\overline z.
\]

### 3.1 Split algebra

If `epsilon=(D/r)=+1`, choose `delta` with `delta^2=D`.  The isomorphism

\[
 x_0+x_1w\longmapsto
 (x_0+x_1\delta,x_0-x_1\delta)
\]

identifies the algebra with `k x k`, conjugation with coordinate exchange,
and the norm with coordinate product.  Hence

\[
 A_D(k)^*=(k^*)^2,
\]

and

\[
 \phi(x,y)=(x/y,y/x).
\]

Every torus point `(t,t^{-1})` occurs.  Its fibre consists of
`(ty,y)` with `y in k^*`, so every fibre has exactly `r-1` elements.  The
kernel is the diagonal scalar subgroup and the torus has order `r-1`.

### 3.2 Nonsplit algebra

If `epsilon=-1`, then `A_D(k)=F_{r^2}` and conjugation is Frobenius:
`bar(z)=z^r`.  Thus

\[
 \phi(z)=z^{1-r}.
\]

The kernel is `F_r^*`, of order `r-1`.  Since `F_{r^2}^*` is cyclic, the
image has order

\[
 {r^2-1\over r-1}=r+1.
\]

Every image has norm one.  The norm-one kernel itself also has order
`r+1`, so the image is the full torus.  Again every fibre has exactly
`r-1` elements.

These calculations prove exact surjectivity and constant fibre size in
both local algebra types.  In particular, a uniform local algebra unit maps
to a uniform point of the full local torus.  Unlike the affine Cayley
parameter, this map includes `-1`, the point represented by infinity in the
Cayley parameter line.  It also includes `+1`; its fibre is the scalar
subgroup.

## 4. Global independence and sampler cost

CRT identifies a uniformly sampled coefficient pair modulo `N` with two
independent uniform local algebra elements.  The event that both are units
is the product of two local events.  Conditioning on this product event
therefore leaves independent uniform local algebra units.  Applying the two
maps from Section 3 preserves independence and produces independent uniform
`U_p` and `U_q` in the full local tori.

The optional coefficient screen removes only nonunits.  Therefore it does
not change the accepted distribution.  A proper screen value is already a
factor; a global zero is rejected.

The number of local algebra units is

\[
 |A_D(F_r)^*|=(r-1)(r-\epsilon_r).
\]

Indeed, this is `(r-1)^2` in the split product algebra and `r^2-1` in the
nonsplit field.  Hence one local unit probability is

\[
 \left(1-{1\over r}\right)
 \left(1-{\epsilon_r\over r}\right)\ge {4\over9}.
\]

The two-prime acceptance probability is at least `16/81`.  Repeating the
coefficient sample for the fixed `D` therefore takes at most `81/16`
attempts in expectation.  This proves the sampler claim and its constant
expected cost.

Sampling `D` itself also needs no factorization.  Sample a residue, take its
gcd with `N`, return a proper gcd, reject zero modulo `N`, and otherwise
compute the Jacobi symbol.  The unit density is

\[
 (1-1/p)(1-1/q)\ge8/15,
\]

so this step also has constant expected cost.

## 5. Exact local return and conditional two-primary laws

CRT independence and Section 1 prove the independent return probabilities
`alpha_p,alpha_q`.  Exactly one local return makes `G_+(U^E)` a proper
factor.  These two disjoint atoms have total probability

\[
 \alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).           \tag{P5}
\]

On the intersection of the two return events, `G_+(U^E)=N`.

The two-primary part of the cyclic local torus is `C_{2^{e_i}}`.  If
`v=v_2(E)`, the kernel of the `E`-power map on this part is its unique
subgroup of order

\[
 2^{h_i},\qquad h_i=\min(e_i,v).                      \tag{P6}
\]

Conditional on a local return, the whole local point is uniform in the
power-map kernel.  Its two-primary coordinate is therefore uniform in the
subgroup from (P6).  The two local conditional coordinates remain
independent.

There is no order-zero edge case.  Every `m_i=p_i-epsilon_i` is even, and
`N-J` is even because `N` is odd and `J` is a sign.  Since `W>=1`, both
`e_i` and `v` are at least one, so both `h_i>=1`.  The identity point is
still present: it is the order-exponent value zero in the distribution
below.

## 6. The torus square chain and its exact success probability

Write `E=2^v u` with `u` odd.  On the global-return event, the odd-order
part of each local point has order dividing `u`, so raising to `u` kills
it.  Raising the two-primary coordinate to the odd power `u` preserves its
exact order.

For a uniform element of `C_{2^h}`, let `K` be the exponent of its exact
order, so that its order is `2^K`.  Then

\[
 P_h(0)=2^{-h},\qquad
 P_h(j)=2^{j-1-h}\quad(1\le j\le h).                 \tag{P7}
\]

The first value accounts for the identity.  The second follows because a
cyclic `2`-group has `2^{j-1}` elements of exact order `2^j`.

The joint-coordinate screens in (4) are exact: a hidden prime `r` divides
`G_+(Y)` exactly when `Y_r=+1`, and it divides `G_-(Y)` exactly when
`Y_r=-1`.  The local torus is cyclic of even order and therefore has the
unique order-two point `-1`.

If the two starting order exponents differ, the component with smaller
exponent reaches `+1` strictly before the other.  One of the tested
`G_+` values is then a proper factor.  At the last unequal stage, the
corresponding `G_-` screen also exposes the nontrivial CRT square root when
the other component is `-1`.  Conversely, if the two exponents agree, both
components reach `-1` and then `+1` at the same stages.  Before those stages
neither component is a signed identity.  Every screen is then `1` or `N`,
so no factor appears.  Thus the chain succeeds exactly when the two order
exponents differ.

Let `a=min(h_p,h_q)` and `b=max(h_p,h_q)`.  From (P7), the equality
probability is

\[
 \begin{aligned}
 \sum_{j=0}^aP_a(j)P_b(j)
 &=2^{-a-b}\left(1+\sum_{j=1}^a4^{j-1}\right)\\
 &={4^a+2\over3\,2^{a+b}}.
 \end{aligned}                                       \tag{P8}
\]

This proves (1).  For fixed `a`, (P8) is largest at `b=a`; there it equals

\[
 {1+2\cdot4^{-a}\over3}\le {1\over2}.
\]

Hence `mu_{a,b}>=1/2`.

Adding `mu_{a,b} alpha_p alpha_q` from the global-return atom to (P5)
proves (6).  The same elementary inequality as in P205 gives

\[
 S\ge\mu_{a,b}\max(\alpha_p,\alpha_q).
\]

For completeness, assume `alpha_p>=alpha_q` and write `mu=mu_{a,b}`.  If
`1-(2-mu)alpha_p>=0`, then

\[
 S-\mu\alpha_p
 =(1-\mu)\alpha_p
  +\alpha_q(1-(2-\mu)\alpha_p)\ge0.
\]

If the coefficient is negative, replace `alpha_q` by the larger
`alpha_p`, reversing the inequality, and obtain

\[
 S-\mu\alpha_p
 \ge(2-\mu)\alpha_p(1-\alpha_p)\ge0.
\]

Since `max(alpha_p,alpha_q)=1/min(r_p,r_q)`, this proves (7).

## 7. Four orientations and ordinary P205

A uniform unit modulo one hidden prime has each quadratic character on
exactly half of its values.  CRT makes the two characters independent.
Therefore a uniform unit `D` has each sign pair in (8) with probability
`1/4`.  Conditional on a public Jacobi sign `J`, the two compatible
orientations have probability `1/2` each.

This statement remains exact only when the chosen `D` is retained while
coefficient pairs are resampled.  If the whole `(D,A,B)` triple were
rejected after a nonunit norm, orientations with split local algebras would
be accepted less often.  The choose-`D`-first procedure avoids that bias.

For a fixed word `W`, the local cyclic orders, residuals, and clean powered
law depend on `D` only through the sign pair.  Averaging (7) over the four
equiprobable signs proves (9).  The `(+,+)` orders are `p-1,q-1`, exactly
the ordinary P205 orders.  The remaining signs give the three other pairs
chosen from `p-1,p+1` and `q-1,q+1`.

For a fixed word, this exhausts the information supplied by changing the
discriminant: every clean powered law is determined by one of the four sign
pairs.  Repeating discriminants within one sign pair repeats the same local
orders, residuals, and probability law.  The averaging theorem gives a
constant-cost menu of four exact interfaces, but it proves no upper bound on

\[
 \min_{\epsilon}\min(r_{p,\epsilon},r_{q,\epsilon}).
\]

A rule that makes `W` depend materially on the full integer value of `D`
would not be covered by this four-law exhaustion.  Such a rule is a new
integer source and needs a separate proof that it reduces one shifted
residual on every input.

## 8. Bit complexity and Las Vegas verification

All coefficient pairs are reduced modulo `N`.  Jacobi symbols, gcds,
modular inverses after unit certification, and multiplication by (3) take
polynomial time in `log N`.  The exponent has bit length

\[
 O(\log N+\log W).
\]

Binary powering and at most `v_2(E)+1` square-chain stages therefore take
time polynomial in `log N+log W`.  Each candidate output is checked to lie
strictly between `1` and `N` and to divide `N`.  All random exits are thus
Las Vegas.  Combining the constant expected sampler cost with the expected
`2R` clean powered trials proves the numerical-quasipolynomial claim under
the stated bounds on `log W` and `R`.
