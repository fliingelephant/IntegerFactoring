# Proof of the F237 finite obstruction certificate

## 1. Two elementary certificate lemmas

Suppose the complete prime factorization of `m-1` is known.  If an integer
`a` satisfies

\[
a^{m-1}\equiv1\pmod m
\]

and

\[
a^{(m-1)/\ell}\not\equiv1\pmod m
\]

for every prime `ell | m-1`, then `a` has exact order `m-1` in the unit
group modulo `m`.  Therefore

\[
\varphi(m)\ge m-1.
\]

Since always `phi(m) <= m-1`, with equality only for a prime, `m` is prime.
Starting from `2`, this gives a recursive Lucas primality certificate.

Similarly, let the complete prime factorization of `t` be known.  If

\[
z^t\equiv1\pmod m
\]

but

\[
z^{t/\ell}\not\equiv1\pmod m
\]

for every prime `ell | t`, then `z` has exact order `t` modulo `m`.

The verifier applies these two lemmas directly.  Its certificate table is
topologically ordered: every prime factor of `m-1` has already received a
certificate before `m` is checked.

## 2. Domain and zero defect

Direct integer multiplication gives the displayed value of `N=pq`.  The
recursive Lucas table proves that `p` and `q` are prime.  Direct comparison
gives `p<q<2p`.

The inequalities

\[
2^{128}<N+1<2^{129}
\]

give `n=129`.  Exact division gives

\[
N-1=2^{64}\cdot21874638913457614155.
\]

Both `p-1` and `q-1` have exact two-adic valuation one.  Their odd parts
are

\[
P=7593622735504604171,
\]

\[
Q=13284695585898979283
 =37\cdot359045826645918359.
\]

The certificate table proves that the three displayed factors are prime,
and Euclid's algorithm gives `gcd(P,Q)=1`.  Thus `D=1`, `s_p=P`, and
`s_q=Q` exactly as claimed.

## 3. Exact orders

For `s_p`, the candidate order factors as

\[
3796811367752302085
 =5\cdot759362273550460417.
\]

For the large factor of `s_q`, the candidate order factors as

\[
179522913322959179
 =6014663\cdot29847543133.
\]

The recursive table proves every factor in these two factorizations prime.
The verifier checks a return at the candidate order and a nonreturn after
division by each distinct prime factor.  The order lemma therefore proves
both exact orders.  It applies in the same way to the order `36` modulo
`37`.

Because the two prime factors of `s_q` are coprime, the Chinese remainder
theorem gives

\[
\operatorname{ord}_{s_q}(N)
 =\operatorname{lcm}
   \left(36,179522913322959179\right)
 =6462824879626530444.
\]

The direct integer comparisons with `2^61` prove the whole-residual order
bounds.

## 4. The full range of power words

A prime `ell` divides one factor `N^k-1` exactly when

\[
\operatorname{ord}_{\ell}(N)\mid k.
\]

Now

\[
2^{57}<179522913322959179
 <3796811367752302085.
\]

Therefore, for every `1 <= k <= K <= 2^57`, neither `s_p` nor the large
prime factor `359045826645918359` of `s_q` divides `N^k-1`.  It follows
that

\[
\gcd(s_p,W_K)=1
\]

and that the large prime factor remains in `r_q`.  Hence

\[
r_p=s_p,
\qquad
r_q\ge359045826645918359>2^{58}.
\]

Since `s_p` is still larger, the claimed lower bound on
`min(r_p,r_q)` follows.

## 5. Exact boundary

This proof establishes one finite obstruction.  It does not give infinitely
many such prime pairs.  An asymptotic obstruction would require an infinite
family of balanced prime pairs on the modular hyperbola

\[
pq\equiv1\pmod{2^{\lfloor n/2\rfloor}}
\]

with simultaneous lower bounds for the two cross-orders.  No such prime
distribution theorem is asserted here.

