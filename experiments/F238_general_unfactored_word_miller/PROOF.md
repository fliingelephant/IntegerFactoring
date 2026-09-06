# Proof of the F238 general unfactored-word Miller theorem

## 1. The part of each local order already present in `N-1`

Reduction modulo `p-1` gives

\[
 N-1=pq-1\equiv q-1\pmod {p-1}.
\]

Therefore

\[
 \gcd(N-1,p-1)=\gcd(q-1,p-1)=d.                        \tag{P1}
\]

Write `N-1=dA`.  Since `p-1=ds_p`, (P1) also gives

\[
 \gcd(A,s_p)=1.
\]

It follows that

\[
 \begin{aligned}
 \gcd(E,p-1)
 &=\gcd(dAW,ds_p)\\
 &=d\gcd(W,s_p).
 \end{aligned}                                         \tag{P2}
\]

The same proof gives

\[
 \gcd(E,q-1)=d\gcd(W,s_q).                             \tag{P3}
\]

For a uniform element of a cyclic group of order `m`, the kernel of the
map `z -> z^E` has `gcd(E,m)` elements.  Hence (P2)--(P3), divided by the
two local group orders, prove the local probabilities in (2).  CRT makes
the two events independent.

Exactly one local return makes `gcd(x^E-1,N)` a proper factor.  These two
exclusive atoms have total probability

\[
 \alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).             \tag{P4}
\]

Both local returns occur with probability `alpha_p alpha_q`, and for a
squarefree semiprime this event is exactly `g=N`.

## 2. The conditional two-primary kernels

Let `G_p` and `G_q` be the two cyclic local unit groups.  Their two-primary
parts are `C_{2^{e_p}}` and `C_{2^{e_q}}`.  If `v=v_2(E)`, the kernel of
the `E`-th power map on `C_{2^{e_i}}` is its unique subgroup of order

\[
 2^{h_i},\qquad h_i=\min(e_i,v).                        \tag{P5}
\]

The odd and two-primary coordinates of each cyclic local group are
independent.  Conditional on a local return, its two-primary coordinate is
therefore uniform on this kernel.  CRT independence survives conditioning
on the intersection of the two local return events.  Conditional on
`g=N`, the two relevant coordinates are thus independent uniform elements
of `C_{2^{h_p}}` and `C_{2^{h_q}}`.

Both kernel exponents are positive because `N-1` is even and both local
orders are even.

For completeness, let `e_p<e_q`.  Expanding the two odd primes at one gives

\[
 p=1+2^{e_p}a_p,\qquad q=1+2^{e_q}a_q
\]

with `a_p,a_q` odd, and hence

\[
 v_2(N-1)=e_p.                                         \tag{P6}
\]

Thus (7) follows.  If `e_p=e_q=e`, then the two terms of valuation `e`
in the expansion of `N-1` add, so

\[
 v_2(N-1)\ge e+1,                                      \tag{P7}
\]

which proves the equal-exponent specialization.

## 3. Exact Miller probability

For a uniform element of `C_{2^h}`, let `J` be the exponent of its order:
the order is `2^J`.  The exact distribution is

\[
 P_h(0)=2^{-h},\qquad
 P_h(j)=2^{j-1-h}\quad(1\le j\le h).                  \tag{P8}
\]

Indeed, one element has order one and `2^{j-1}` elements have exact order
`2^j`.

Write `E=2^v u` with `u` odd.  On the global-return atom, every local odd
component has order dividing `u`, so `x^u` kills it.  Raising a two-primary
element to the odd power `u` preserves its exact order.  The square chain
therefore starts with independent order exponents having laws
`P_{h_p}` and `P_{h_q}`.

The chain exposes a proper CRT square root of one if and only if these two
order exponents differ.  If they agree, both local values reach the unique
element of order two, namely `-1`, at the same step and then reach `1` at
the same step.  If they differ, one local value reaches `1` before the
other, and one of the tested plus/minus gcds is proper.

Assume `a=min(h_p,h_q)` and `b=max(h_p,h_q)`.  The probability that the
two order exponents agree is

\[
 \begin{aligned}
 \sum_{j=0}^aP_a(j)P_b(j)
 &=2^{-a-b}
   +2^{-a-b}\sum_{j=1}^a4^{j-1}\\
 &=2^{-a-b}\left(1+{4^a-1\over3}\right)\\
 &={4^a+2\over3\,2^{a+b}}.
 \end{aligned}                                         \tag{P9}
\]

Subtracting (P9) from one proves (1).  For fixed `a`, the equality
probability in (P9) is largest when `b=a`.  In that case it is

\[
 {1+2\cdot4^{-a}\over3}\le {1\over2}
\]

for every `a>=1`, with equality only at `a=1`.  This proves (4).

Adding `mu_{a,b} alpha_p alpha_q` to (P4) proves the exact success formula
(3).

## 4. The residual lower bound

Assume without loss that `alpha_p>=alpha_q`, and abbreviate
`mu=mu_{a,b}`.  From (3),

\[
 S-\mu\alpha_p
 =(1-\mu)\alpha_p
  +\alpha_q\bigl(1-(2-\mu)\alpha_p\bigr),              \tag{P10}
\]

where `S` is the one-trial success probability.  If the parenthesized
coefficient is nonnegative, (P10) is nonnegative.  If it is negative, use
`alpha_q<=alpha_p`; multiplying this inequality by the negative
coefficient reverses it and gives

\[
 \begin{aligned}
 S-\mu\alpha_p
 &\ge (1-\mu)\alpha_p
      +\alpha_p\bigl(1-(2-\mu)\alpha_p\bigr)\\
 &=(2-\mu)\alpha_p(1-\alpha_p)\ge0.
 \end{aligned}                                         \tag{P11}
\]

Thus `S>=mu max(alpha_p,alpha_q)`.  Combining this with `mu>=1/2` and

\[
 \max(\alpha_p,\alpha_q)={1\over\min(r_p,r_q)}
\]

proves (5).  Independent fresh trials then have geometric expectation at
most `2 min(r_p,r_q)` and terminate almost surely.

## 5. Cost and implementation

Every output is checked to be a strict divisor of `N`; therefore the
procedure is Las Vegas.  Uniform unit sampling does not require knowing the
factorization: sample a residue and first compute its gcd with `N`.  A
proper gcd is already success, while rejection of the remaining nonunits
produces a uniform unit.  For distinct odd primes the expected number of
samples is constant.

The bit length of `E` is at most

\[
 \lceil\log_2 N\rceil+\lceil\log_2 W\rceil.
\]

One modular exponentiation, at most `v_2(E)+1` modular squarings, and the
same order of gcds take time polynomial in this bit length and in
`log N`.  Repeating an expected `2R` times preserves numerical
quasipolynomial cost when `log W` and `R` are numerical quasipolynomial.

The values `d,s_p,s_q,r_p,r_q` are used only to analyze the probability.
The algorithm does not know them.

## 6. More than two prime supports

Let `N=prod_i p_i^{c_i}` have at least two distinct odd prime supports.
Reduction modulo `p_i-1` and the definition

\[
 d_i=\gcd(N-1,p_i-1),\qquad s_i=(p_i-1)/d_i
\]

give, exactly as in (P2),

\[
 \Pr(x^E=1\bmod p_i)=
 {\gcd(E,p_i-1)\over p_i-1}
 ={1\over r_i}=\alpha_i.                               \tag{P12}
\]

These prime-support events are independent.  Any nonempty proper pattern
of returns makes the initial gcd proper.  The probability of such a
pattern is

\[
 1-\prod_i(1-\alpha_i)-\prod_i\alpha_i.                \tag{P13}
\]

On the all-return pattern, the initial gcd can already be proper when a
prime power is repeated.  If instead `g=N`, the same conditional-kernel
argument gives independent order exponents with laws `P_{h_i}`.  The
Miller chain fails exactly when all these exponents agree, so its exact
conditional success probability is (8).  The all-agree event is contained
in the event that the first two exponents agree.  Formula (P9) bounds the
latter probability by `1/2`; hence `mu_boldsymbol_h>=1/2`.

Adding the guaranteed contribution `mu_boldsymbol_h prod_i alpha_i` to
(P13) proves the first inequality in (9).  If `alpha_m=max_i alpha_i`, then

\[
 \prod_i(1-\alpha_i)\le1-\alpha_m,
 \qquad
 \prod_i\alpha_i\le\alpha_m.
\]

These inequalities prove the second bound in (9).  If `N` is squarefree,
the all-return event is exactly `g=N`, so no extra partial-power success is
present and equality holds in the first part of (9).
