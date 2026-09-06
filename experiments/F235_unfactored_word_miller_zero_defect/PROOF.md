# Proof of the F235 unfactored-word Miller theorem

## 1. Zero-defect arithmetic

The P200 identities give

\[
 \gcd(H,P)=\gcd(H,Q)=D.                                  \tag{P1}
\]

We prove the extra two-adic equality.  Since `B | N-1`,

\[
 v_2(N-1)\ge \lfloor n/2\rfloor.                         \tag{P2}
\]

For odd `p,q`, if `e!=f`, then

\[
 v_2(pq-1)=\min(e,f).                                    \tag{P3}
\]

Assume, without loss, `e<f`.  Balance gives `q<2p`.  Since
`p>=2^e+1` and `q>=2^f+1`, the inequality `f>=e+1` alone does not contradict
balance.  Instead combine (P2) and (P3): `e>=floor(n/2)`.  But
`p-1>=2^e>=2^{floor(n/2)}` and `q-1>=2^{e+1}`.  Hence

\[
 N=pq>(2^{\lfloor n/2\rfloor})(2^{\lfloor n/2\rfloor+1})
 \ge 2^n,
\]

for both parities of `n`, contradicting `N<2^n`.  Thus `e=f`.

The common value is positive because both primes are odd.

## 2. Exact local return law

Because `N-1=BH` and `B` is a power of two, (P1) gives

\[
 \gcd(E,p-1)
 =2^eD\gcd(W,s_p).
\]

The corresponding identity modulo `q` is

\[
 \gcd(E,q-1)
 =2^eD\gcd(W,s_q).                                      \tag{P4}
\]

For a uniform element of a cyclic group of order `m`, the equation
`z^E=1` has exactly `gcd(E,m)` solutions.  The CRT coordinates of a uniform
unit modulo `N` are independent and uniform.  Dividing (P4) by the local
group orders proves (2).

Exactly one local return makes `gcd(x^E-1,N)` proper.  The probabilities of
the two exclusive events sum to

\[
 \alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).              \tag{P5}
\]

The global-return probability is `alpha_p alpha_q`.

## 3. The conditional Miller law

Let `G_r` be the cyclic group modulo `r` for `r=p,q`, and write

\[
 G_r=C_{2^e}\times C_{m_r},\qquad m_r\text{ odd}.
\]

The condition `x^E=1 mod r` restricts only the odd coordinate through
`gcd(W,s_r)`.  The exponent `E` contains the full factor `2^e`, so every
two-primary coordinate returns.  Therefore, conditional on a local return,
the two-primary coordinate remains uniform in `C_{2^e}`.  Conditional on a
global return, the two local two-primary coordinates remain independent and
uniform.

For a uniform element of `C_{2^e}`, let `J` be the two-adic exponent of its
order, so `J in {0,...,e}`.  Its exact law is

\[
 \Pr(J=0)=2^{-e},\qquad
 \Pr(J=j)=2^{j-1-e}\quad(1\le j\le e).                  \tag{P6}
\]

The Miller square chain exposes a nontrivial CRT square root of one exactly
when the two local values of `J` differ.  Hence its conditional success
probability is

\[
 \begin{aligned}
 \mu_e
 &=1-\sum_{j=0}^e\Pr(J=j)^2\\
 &=1-4^{-e}-\sum_{j=1}^e4^{j-1-e}\\
 &=1-4^{-e}-{1-4^{-e}\over3}\\
 &={2\over3}(1-4^{-e}).
 \end{aligned}                                           \tag{P7}
\]

This proves (3) and (5).  Adding `mu_e alpha_p alpha_q` to (P5) proves
(4).

The implementation does not need to trust that `E` is a multiple of both
local group orders.  It invokes the chain only after the verified global
return `x^E=1 mod N`.  Every output is a gcd checked to lie strictly between
`1` and `N`.  A false universal-annihilator premise can only make the trial
null.

## 4. Saturation consequences

If `s_p|W`, then `alpha_p=1`.  Formula (4) becomes

\[
 1-(1-\mu_e)\alpha_q\ge\mu_e\ge1/2.                     \tag{P8}
\]

The same argument applies with `p,q` interchanged.  Independent fresh trials
therefore have geometric expectation at most two and terminate almost
surely.

If `t_p=ord_{s_p}(N)<=K`, then `s_p | N^{t_p}-1`, which is a factor of
`W_K`.  This proves (8).  Moreover,

\[
 \log_2 W_K
 <\sum_{k=1}^K kn
 ={nK(K+1)\over2},
\]

which proves (9).

Every prime power dividing `s_p` or `s_q` is smaller than `N<2^n`, so its
exponent is less than `n`.  Thus if a rational prime divides one child
`A_j`, its `n`-th power in (10) contains the complete corresponding primary
part of both residuals.  This proves the shifted-child claim without
factoring any child.

## 5. Bit complexity

The algorithm can construct `W` as a binary integer by a product tree, or
construct `E mod` the moduli used by modular exponentiation while retaining
its binary exponent.  In either form, its running time is polynomial in
`n+log W` under standard fast integer arithmetic.  The two-adic valuation
of `E` is obtained by counting trailing zero bits; here it also equals
`v_2(N-1)+v_2(W)`.  One modular power and at most `v_2(E)=O(log E)` squarings
and gcds cost a polynomial in `n+log W`.

For `K=QP(n)`, (9) is numerical QP.  For (10),

\[
 \log W=n\sum_j\log A_j,
\]

so a numerical-QP count and aggregate child encoding length also give a
numerical-QP trial.  No hidden order, unknown factor, factorization of the
word, or recursive factoring call occurs.

Finally, since `p=1 mod s_p` and `q=1 mod s_q`, reduction of `N=pq` gives
(11).  These congruences prove correlation, not a small-order theorem.  That
is the exact remaining gap.
