# F238 candidate — any unfactored word gives an exact Miller law for every odd squarefree semiprime

## Status and scope

This is a proof-only reduction.  It is not an all-input factoring algorithm.
It does not construct the required quasipolynomial-size word on every input.

Let

\[
 N=pq,
\]

where `p` and `q` are distinct odd primes.  No balance or zero-defect
condition is assumed.  Put

\[
 d=\gcd(p-1,q-1),\qquad
 s_p={p-1\over d},\qquad s_q={q-1\over d}.
\]

Thus `gcd(s_p,s_q)=1`.  Let `W>=1` be any public integer.  Its
factorization is not supplied or required.  Define

\[
 E=(N-1)W,
\]

\[
 r_p={s_p\over\gcd(s_p,W)},\qquad
 r_q={s_q\over\gcd(s_q,W)},
\]

and

\[
 \alpha_p={1\over r_p},\qquad \alpha_q={1\over r_q}.
\]

Write

\[
 e_p=v_2(p-1),\qquad e_q=v_2(q-1),\qquad v=v_2(E),
\]

and set

\[
 h_p=\min(e_p,v),\qquad h_q=\min(e_q,v).
\]

Both `h_p` and `h_q` are positive.  Let

\[
 a=\min(h_p,h_q),\qquad b=\max(h_p,h_q)
\]

and

\[
 \mu_{a,b}
 =1-{4^a+2\over 3\,2^{a+b}}.                         \tag{1}
\]

## One exact trial

Choose `x` uniformly from the units modulo `N`.  Compute

\[
 g=\gcd(x^E-1,N).
\]

Return `g` if it is proper.  If `g=1`, declare the trial null.  If `g=N`,
write `E=2^v u` with `u` odd.  Starting with `z_0=x^u mod N`, square
successively and test every `gcd(z_i-1,N)` and `gcd(z_i+1,N)`.  Return only
a verified proper gcd.  If none appears, declare the trial null.

The local return events are independent and have exact probabilities

\[
 \Pr(x^E=1\bmod p)=\alpha_p,
 \qquad
 \Pr(x^E=1\bmod q)=\alpha_q.                           \tag{2}
\]

Conditional on `g=N`, the Miller chain returns a proper factor with exact
probability `mu_{a,b}`.  Therefore one complete trial returns a factor with
exact probability

\[
 \boxed{
  \alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
 }                                                       \tag{3}
\]

The exact Miller probability satisfies

\[
 \mu_{a,b}\ge {1\over2}.                               \tag{4}
\]

Moreover,

\[
 \boxed{
 \Pr(\text{factor in one trial})
 \ge \mu_{a,b}\max(\alpha_p,\alpha_q)
 \ge {1\over 2\min(r_p,r_q)}.
 }                                                       \tag{5}
\]

Consequently, if `min(r_p,r_q)<=R`, fresh trials factor `N` almost surely
in at most `2R` expected trials.  If `W` has numerical-quasipolynomial bit
length and `R` is numerical quasipolynomial in the input length, this is a
Las Vegas numerical-quasipolynomial reduction.  In particular, if either
`s_p|W` or `s_q|W`, the expected number of trials is at most two.

No factor-first stripping is used.  The algorithm does not factor `W`,
`E`, `N-1`, or an auxiliary child integer.

## Exact two-adic specialization

If `e_p=e_q=e`, then `v_2(N-1)>=e+1`, so

\[
 h_p=h_q=e,
 \qquad
 \mu_{e,e}={2\over3}(1-4^{-e}).                        \tag{6}
\]

If, for example, `e_p<e_q` and `w=v_2(W)`, then

\[
 v=e_p+w,\qquad h_p=e_p,\qquad h_q=\min(e_q,e_p+w).     \tag{7}
\]

Thus extra powers of two in `W` can only increase the conditional Miller
success probability.

## Natural extension beyond squarefree semiprimes

Let

\[
 N=\prod_{i=1}^k p_i^{c_i},\qquad k\ge2,
\]

be odd, with distinct primes `p_i`.  Put

\[
 d_i=\gcd(N-1,p_i-1),\qquad
 s_i={p_i-1\over d_i},\qquad
 r_i={s_i\over\gcd(s_i,W)},\qquad
 \alpha_i={1\over r_i},
\]

and

\[
 h_i=\min(v_2(p_i-1),v_2(E)).
\]

For `h>=1`, define

\[
 P_h(0)=2^{-h},\qquad
 P_h(j)=2^{j-1-h}\quad(1\le j\le h),
\]

and set `P_h(j)=0` outside this range.  Conditional on `g=N`, the exact
Miller success probability is

\[
 \mu_{\boldsymbol h}
 =1-\sum_{j\ge0}\prod_{i=1}^k P_{h_i}(j)
 \ge {1\over2}.                                        \tag{8}
\]

The complete trial has the rigorous lower bound

\[
 \Pr(\text{factor})
 \ge
 1-\prod_i(1-\alpha_i)
   -(1-\mu_{\boldsymbol h})\prod_i\alpha_i
 \ge {1\over2}\max_i\alpha_i.                        \tag{9}
\]

When all `c_i=1`, the first inequality in (9) is equality.  With repeated
prime powers, the initial gcd can already expose a proper partial power,
so (9) is stated only as a lower bound.

## Remaining source question

For semiprimes, the exact unresolved task is now

\[
 \boxed{
 \text{construct a public QP-bit }W
 \text{ for which }\min(r_p,r_q)=\operatorname{QP}(\log N)
 \text{ on every input.}
 }
\]

The word need not contain either residual completely.  An inverse-QP
remaining residual is sufficient.  Randomness supplies the Miller
amplification after the integer word has made that deterministic progress;
it does not by itself supply a large hidden divisor of `W`.
