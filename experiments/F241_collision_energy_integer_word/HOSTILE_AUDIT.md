# F241 hostile audit — collision energy and integer words

## Verdict

**PASS.** All five supplied SHA-256 values matched before I read the frozen
content. The deterministic residual, collision-energy identity, P205
expectation step, divisor-source Parseval formula, subgroup lower bound,
simultaneous-capture bank, prime-power obstruction, and fixed-`u` quotient
interpretation are correct at their stated scopes.

I found two harmless endpoint wording slips in `PROOF.md` lines 162--163.
A sampled divisor can equal `A=N-1`, so not every divisor is *below* `A`.
Also, `log_2(Delta_t^n)<n^2` implies at most `n^2` bits, not necessarily
fewer than `n^2` bits. The needed facts are

\[
1\le Z\le A<N,
\qquad
1\le\Delta_t<A<N<2^n,
\]

and they prove the stated `O((R+1)n^2)` word-length bound unchanged. No
theorem or probability claim depends on either strict wording.

I did not edit a frozen input or a durable ledger. I ran no numerical
experiment. I wrote only this audit.

## 1. Frozen-input integrity

I listed the packet filenames and recomputed the supplied hashes before
opening any frozen file. Every value matched.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `11cbe1a262a546ad05c3462f8189f3704a98e73b1725d334a487ad36f0d5c48b` | match |
| `PROOF.md` | `5150d7416741d8bfa45f832f6d41e621e12068cced8d1267e241616b399c9edb` | match |
| `SELF_AUDIT.md` | `515c96550d965ec36e72a4b4143ffd76fc79d89a0aef6971da51754f20e5f027` | match |
| `PROVENANCE.md` | `16b1fd933ae9cc7ef80fec6c3a5022f7618109e3cc1080e5ae45565e32439c17` | match |
| `MANIFEST.md` | `1fab4af92448b91eeebfa220b5ca19d097851660dd484747fe01493c388ceb74` | match |

## 2. Exact deterministic residual

Put `A=N-1`. Reduction modulo `p-1` gives

\[
pq-1\equiv q-1\pmod {p-1},
\]

so

\[
\gcd(A,p-1)=\gcd(p-1,q-1)=d.
\]

The same argument interchanges `p` and `q`. Write

\[
A=dA_0,
\qquad p-1=ds_p.
\]

Then

\[
d\gcd(A_0,s_p)=\gcd(A,p-1)=d,
\]

hence `gcd(A_0,s_p)=1`; likewise `gcd(A_0,s_q)=1`. Thus a
prime occurring in `s_i` meets `A` exactly when it meets the already
extracted factor `d` of `A`.

If `ell^e || s_i`, then

\[
2^e\le \ell^e\le s_i<N<2^n,
\]

so `e<n`. If `ell | A`, then

\[
v_\ell(A^n)=n v_\ell(A)\ge n>e;
\]

if `ell` does not divide `A`, its valuation in `A^n` is zero. Therefore

\[
\frac{s_i}{\gcd(s_i,A^n)}
=\prod_{\substack{\ell^e\parallel s_i\\\ell\nmid A}}\ell^e
=s_i^\perp.
\]

This also covers `s_i=1`, when both products are empty and equal one. The
strict endpoint `e=n` cannot occur: it would force
`ell^e>=2^n>N>s_i`.

Finally,

\[
\log_2(A^n)=n\log_2 A<n^2,
\]

so `W_0=A^n` has at most `n^2` bits. Substitution into P205 gives expected
numerical-QP time whenever either exact surviving residual is numerical QP.

## 3. Exact collision-energy expansion

Fix `s<N` and write `s=product_(ell in P) ell^{e_ell}`. The same size
argument gives `e_ell<n`. For the packet's convention

\[
\Delta=|Z-Z'|\quad(Z\ne Z'),
\qquad
\Delta=1\quad(Z=Z'),
\]

one has, for every prime divisor of `s`,

\[
\gcd(\ell^{e_\ell},\Delta^n)
=
\begin{cases}
\ell^{e_\ell},&\ell\mid\Delta,\\
1,&\ell\nmid\Delta.
\end{cases}
\]

Hence the pointwise identity is

\[
\gcd(s,\Delta^n)
=\prod_{\ell\in\mathcal P}
\left(1+(\ell^{e_\ell}-1){\bf1}_{\ell\mid\Delta}\right).
\tag{A1}
\]

For a nonempty subset `S` of `P`, put
`m_S=product_(ell in S) ell`. This modulus is squarefree. The indicator
product in the corresponding expansion term obeys

\[
\prod_{\ell\in S}{\bf1}_{\ell\mid\Delta}
={\bf1}_{m_S\mid\Delta}.
\]

Because equal integer samples were replaced by `Delta=1`, and because
`m_S>1`,

\[
\Pr(m_S\mid\Delta)
=\Pr(Z\ne Z',\ Z\equiv Z'\pmod {m_S})
=\kappa_{m_S}.
\]

Taking expectations in (A1) and dividing by `s` gives exactly `(CE)`. The
prime powers enter through the full weights `ell^{e_ell}-1`; no collision
modulo `ell^{e_ell}` is needed because the outer exponent `n` saturates the
whole primary part after one hit modulo `ell`.

The endpoint attacks agree with the formula.

- If `s=1`, the prime set and nonempty sum are empty, and both sides equal
  one.
- If `s=ell^e`, the identity reduces to
  \[
  \mathbb E\frac{\gcd(\ell^e,\Delta^n)}{\ell^e}
  =\frac{1+(\ell^e-1)\kappa_\ell}{\ell^e},
  \]
  which is the direct hit/no-hit average.
- With two or more primes, the terms `kappa_(product S)` retain all
  correlations. No independence between different prime-hit events is
  assumed.
- For a point-mass integer law, `Z=Z'` always. Then `Delta=1`, every useful
  `kappa_m` is zero, and both sides are `1/s`. Thus ordinary sample equality
  cannot be inserted into the useful energy.
- Unequal consecutive integers also give `Delta=1`; they correctly create
  no collision for any nonempty squarefree product of residual primes.

In particular, the equal-sample convention is not cosmetic. Using zero
would make the word zero and would falsely saturate every residual on an
integer equality event.

## 4. Expectation-to-P205 implication

The P205 interface can be recovered directly. For an arbitrary positive
word `W`, let `E=AW`. Since `A=dA_0`, `p-1=ds_p`, and
`gcd(A_0,s_p)=1`,

\[
\gcd(E,p-1)
=d\gcd(A_0W,s_p)
=d\gcd(W,s_p).
\]

A cyclic group of order `p-1` has exactly `gcd(E,p-1)` solutions to
`x^E=1`. Therefore a uniform local unit returns with probability

\[
\alpha_p=\frac{\gcd(W,s_p)}{s_p}=\frac1{r_p};
\]

the same holds at `q`. CRT makes the two local coordinates independent for
a fresh uniform unit modulo `N`.

If exactly one local coordinate returns, `gcd(x^E-1,N)` is a proper factor.
If both return, the verified Miller square chain splits when the two exact
two-power orders differ. To check its lower bound from first principles,
let the two relevant cyclic groups have orders `2^{h_p}` and `2^{h_q}`,
and put `a=min(h_p,h_q)`, `b=max(h_p,h_q)`. Here `a>=1`, because both
prime-group orders and `A=N-1` are even. In `C_(2^h)`, the probabilities
of exact orders `1,2,...,2^h` are

\[
2^{-h},\quad 2^{0-h},\quad2^{1-h},\ldots,2^{h-1-h}.
\]

Thus the probability of equal exact two-power orders is

\[
2^{-a-b}\left(1+\sum_{j=1}^a4^{j-1}\right)
=\frac{4^a+2}{3\,2^{a+b}},
\]

and the split probability is

\[
\mu_{a,b}=1-\frac{4^a+2}{3\,2^{a+b}}\ge\frac12.
\]

Consequently, conditional on a fixed sampled word, the complete trial has
success probability

\[
S=\alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q
  +\mu_{a,b}\alpha_p\alpha_q.
\]

This is at least `mu_(a,b) max(alpha_p,alpha_q)`, and hence at least
`(1/2) max(1/r_p,1/r_q)`. For example, assume
`alpha_p>=alpha_q`. If `1-(2-mu)alpha_p` is nonnegative, the inequality is
immediate after subtracting `mu alpha_p`; if it is negative, replacing
`alpha_q` by the larger `alpha_p` can only decrease that difference and
leaves `(2-mu)alpha_p(1-alpha_p)>=0`.

Now take `W=W_Delta`. Pointwise,

\[
\frac1{r_i}=\frac{\gcd(s_i,W_\Delta)}{s_i}.
\]

Conditioning first on the word and then averaging gives

\[
\Pr(\text{factor})
\ge\frac12\mathbb E\max(1/r_p,1/r_q)
\ge\frac12\max_i\mathbb E(1/r_i),
\]

which is exactly `(P205-CE)`. At the simultaneous-saturation endpoint
`r_p=r_q=1`, the Miller term still gives probability at least one half;
global return is not a failure. The history-wise version is also valid:
the argument is conditional on each public history and needs only a fresh
iid integer pair and a later fresh unit at that history.

## 5. Divisor-source Parseval formula and subgroup bound

The independent exponent vector selects each divisor of

\[
A=\prod_{j=1}^k b_j^{a_j}
\]

once and with mass `1/T`, where `T=product_j(a_j+1)`. If `gcd(m,A)=1`,
all these divisors lie in `G_m=(Z/mZ)^times`. Define

\[
\mu_m(x)=\Pr(Z\equiv x\pmod m).
\]

For two independent samples, the total modular-collision probability is

\[
C_m=\sum_{x\in G_m}\mu_m(x)^2.
\]

Finite-abelian Parseval gives

\[
C_m=\frac1{|G_m|}\sum_{\chi\in\widehat G_m}
|\widehat\mu_m(\chi)|^2.
\]

Independence of the exponents gives

\[
\widehat\mu_m(\chi)
=\prod_{j=1}^k
\frac1{a_j+1}\sum_{e=0}^{a_j}\chi(b_j)^e.
\]

For squarefree `m`, `|G_m|=phi(m)`. Integer equality has exact probability

\[
\Pr(Z=Z')=T\left(\frac1T\right)^2=\frac1T.
\]

It is a subset of modular equality and is disjoint from the event defining
`kappa_m`. Hence `kappa_m=C_m-1/T`, which is exactly `(D)`.

The distribution is supported in the subgroup `H_m` generated by the
residues of the `b_j`. Therefore

\[
1=\left(\sum_{x\in H_m}\mu_m(x)\right)^2
\le h_m\sum_{x\in H_m}\mu_m(x)^2
=h_m C_m,
\]

and `(H)` follows after subtracting `1/T`.

The endpoint checks expose why the subtraction is essential. If `h_m=1`,
then `C_m=1` and `kappa_m=1-1/T`. If the `T` integer divisors occupy `T`
distinct residues, then `C_m=1/T` and `kappa_m=0`, even though the ordinary
modular collision probability is positive. The lower bound can be
nonpositive when `T<h_m`; the packet does not use it there. Under `(S)`,

\[
\kappa_\ell\ge\frac1{h_\ell}-\frac1T
\ge\frac1Q-\frac1{2Q}=\frac1{2Q}.
\]

Because `h_ell>=1`, hypothesis `h_ell<=Q` also forces the implicit endpoint
`Q>=1`.

## 6. Simultaneous capture and bit cost

Every prime `ell | s_i^perp` is coprime to `A`, so the divisor-source bound
applies. Across `R` independent divisor pairs, the probability that no
difference captures this fixed prime is

\[
(1-\kappa_\ell)^R
\le\left(1-\frac1{2Q}\right)^R
\le e^{-R/(2Q)}
\le\frac1{2n},
\]

where `log` in the definition of `R` is the natural logarithm (using base
two would only increase `R`).

If `omega(s_i^perp)` is its number of distinct prime divisors, then

\[
2^{\omega(s_i^\perp)}\le s_i^\perp<N<2^n,
\]

so `omega(s_i^perp)<n`. A union bound, without any independence assumption
between different primes, gives

\[
\Pr(\text{every residual prime is captured})
\ge1-\frac{\omega(s_i^\perp)}{2n}>\frac12.
\]

If `s_i^perp=1`, this event is vacuous and has probability one. On the
event, each captured rational prime occurs in some `Delta_t`, so
`Delta_t^n` supplies its full primary power. The leading `A^n` supplies all
primary powers supported on `A`. Therefore `s_i | W` exactly as claimed.

For a fresh later P205 unit, conditional success on this event is at least
one half. Thus

\[
\Pr(\text{complete bank factors})
\ge\frac12\Pr(s_i\mid W)\ge\frac14.
\]

The bit accounting is direct. A sampled divisor satisfies `Z<=A`, while a
nonzero difference of two distinct divisors is strictly below `A`; equal
samples give `Delta=1`. Hence

\[
\log_2 W
=n\log_2 A+n\sum_{t=1}^R\log_2\Delta_t
<(R+1)n^2.
\]

Thus the word has `O((R+1)n^2)` bits. Since
`R=O(Q(n) log n)`, a numerical-QP `Q` gives a numerical-QP output length.
The granted factorization permits direct exact exponent sampling; forming
the sampled divisors, differences, powers, product, and the P205 modular
power takes numerical-QP bit time. No difference is factored. Repetition
of independent constant-success banks preserves the Las Vegas guarantee.

The two proof-wording slips identified in the verdict occur only here:
`Z=A` is allowed, and an integer with logarithm below `n^2` can still have
exactly `n^2` bits. Neither changes this aggregate bound.

## 7. Exact `A=b^a` law and all endpoints

For a prime-power public integer `A=b^a`, write `T=a+1`. The sampled
divisors are `b^I` for uniform `I in {0,...,T-1}`. If
`h=ord_m(b)`, then

\[
b^I\equiv b^J\pmod m
\quad\Longleftrightarrow\quad
I\equiv J\pmod h.
\]

Write `T=qh+r`, with `0<=r<h`. Among the `T` exponents, exactly `r`
congruence classes have size `q+1` and `h-r` have size `q`. The number of
ordered unequal pairs in one class is `c(c-1)`, so the total is

\[
r(q+1)q+(h-r)q(q-1)
=h q(q-1)+2rq.
\]

Division by `T^2` proves `(P)`. Its boundary cases all agree with direct
counting.

- If `h=1`, then `q=T,r=0`, and `kappa_m=1-1/T`: all unequal pairs collide.
- If `r=0`, all `h` classes have the same size `q`, giving
  `h q(q-1)/T^2`.
- If `h=T`, then `q=1,r=0`, and `kappa_m=0`.
- If `h>T`, then `q=0,r=T`, and `kappa_m=0`.
- If `h<T<2h`, then `q=1` and only the `r=T-h` double-occupied classes
  contribute, giving `2r/T^2`.

Thus `h>=T` makes reduction injective on the complete integer support. The
total collision probability is still `1/T`, coming solely from identical
integer samples, but the useful distinct-sample energy is exactly zero.

## 8. Quotient-radix pushforward and entropy

Let `A=N-1=BH`. For a common fixed integer `u` with `1<=u<B`,

\[
uN=u(1+BH)=(uH)B+u.
\]

Since `0<u<B`, this is the Euclidean quotient-remainder decomposition: the
quotient is `uH` and the remainder is `u`. Complementation
`B -> H=A/B` is a bijection on the complete divisor set. On any restricted
support such as `B>u`, it remains an injective deterministic pushforward.

For two regular radix atoms with the same fixed `u`,

\[
uH_1\equiv uH_2\pmod m
\quad\Longleftrightarrow\quad
H_1\equiv H_2\pmod m
\]

whenever `gcd(m,u)=1`. The packet's stronger assumption
`gcd(m,uA)=1` also ensures that all complementary divisors lie in the unit
group used by the character formula. Thus multiplication by the quotient
carry preserves the distinct-sample modular collision law. It is a
deterministic function of the chosen radix and supplies no independent
random variable.

The endpoints are correctly scoped. At `B=A`, one has `H=1`, quotient `u`,
and remainder `u` for every `u<A`. At `u=1`, every `B>1` is regular. The
excluded atom `B=1` has quotient `N` and remainder zero, not quotient `A`
and remainder one, so it must be accounted for separately exactly as the
statement says. Collisions involving that public atom are not silently
included in the complementary-divisor formula. If `u` varied independently
between the two samples, or if `m` shared a factor with `u`, cancellation
could fail; the displayed claim uses one common `u` and its stated
coprimality condition, so it makes neither generalization.

## 9. Scope conclusion

The packet proves a conditional source theorem, not an all-input factoring
algorithm. It grants the complete factorization of `N-1`, and it does not
prove the hidden conditions `h_ell<=Q` for every prime of either exterior
residual. Formula `(CE)` applies to other public integer laws, including
products of recursively supplied bases, but by itself supplies no
inverse-QP distinct-integer collision lower bound for them.

The symbolic endpoint attacks found no counterexample to a boxed identity,
probability bound, complexity class, or stated scope. The two strict
wording slips in the proof have the local corrections stated in the verdict
and do not affect the PASS.
