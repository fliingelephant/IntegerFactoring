# Proof of the F241 collision-energy theorem

## 1. The deterministic word

Put `A=N-1`.  P205 gives

\[
\gcd(A,p-1)=\gcd(A,q-1)=d.
\]

Since `p-1=ds_p` and `d|A`, write `A=dA_0`.  Then

\[
d\gcd(A_0,s_p)=\gcd(A,p-1)=d,
\]

so `gcd(A_0,s_p)=1`.  The same argument applies to `s_q`.  Consequently a
rational prime occurring in `s_i` also occurs in `A` exactly when it occurs
in `d`.

If `ell^e || s_i` and `ell | A`, then

\[
v_\ell(A^n)=n v_\ell(A)\ge n>e.
\]

The last inequality follows from `ell^e <= s_i < N < 2^n`.  Thus `A^n`
contains the full `ell`-primary part of `s_i`.  It contains none of the
primary parts whose rational primes do not divide `A`.  Hence

\[
{s_i\over\gcd(s_i,A^n)}=s_i^\perp.
\]

Also `log_2(A^n)<n^2`, which proves the word-length claim.  Substitution in
the P205 lower bound proves the deterministic success implication.

## 2. Primary saturation by one difference

Fix `s<N` and write `s=product ell^e`.  If `ell | Delta`, then

\[
v_\ell(\Delta^n)\ge n>e.
\]

If `ell` does not divide `Delta`, its primary part is absent.  Therefore

\[
\gcd(s,\Delta^n)
=\prod_{\ell^e\parallel s}
\ell^{e\,1_{\ell\mid\Delta}}.
\]

For every fixed `Delta`, expand this as

\[
\gcd(s,\Delta^n)
=\prod_{\ell^e\parallel s}
\left(1+(\ell^e-1)1_{\ell\mid\Delta}\right).
\]

After expansion, the term indexed by a nonempty set `S` has expectation

\[
\Pr\left(\prod_{\ell\in S}\ell\mid\Delta\right)
=\Pr\left(Z\ne Z',\ Z\equiv Z'
\pmod{\prod_{\ell\in S}\ell}\right)
=\kappa_{\prod_{\ell\in S}\ell}.
\]

The empty term is one.  Division by `s` proves `(CE)`.

For P205,

\[
{1\over r_i}={\gcd(s_i,W_\Delta)\over s_i}.
\]

Condition on the sampled word.  P205 gives factor probability at least

\[
{1\over2}\max(1/r_p,1/r_q).
\]

Average over the word and use

\[
\mathbb E\max(X,Y)\ge\max(\mathbb EX,\mathbb EY).
\]

This proves `(P205-CE)`.  Conditional independence at each public history
gives the same proof history by history.

## 3. Exact uniform-divisor formula

Let `mu_m` be the distribution of a uniform divisor of `A` in the finite
abelian group `G_m`.  The probability of a modular collision is

\[
C_m=\sum_{x\in G_m}\mu_m(x)^2.
\]

Fourier Parseval gives

\[
C_m={1\over|G_m|}\sum_{\chi\in\widehat G_m}
|\widehat\mu_m(\chi)|^2.
\]

The divisor exponents are independent, so

\[
\widehat\mu_m(\chi)
=\prod_{j=1}^k
{1\over a_j+1}\sum_{e=0}^{a_j}\chi(b_j)^e.
\]

There are exactly `T` distinct integer divisors, all with mass `1/T`.
Thus

\[
\Pr(Z=Z')={1\over T},
\qquad
\kappa_m=C_m-{1\over T},
\]

which proves `(D)`.

The law is supported on `H_m`.  Cauchy--Schwarz gives

\[
C_m=\sum_{x\in H_m}\mu_m(x)^2
\ge {1\over h_m}.
\]

Subtracting `1/T` proves `(H)`.

## 4. The conditional bank

Under `(S)`, every rational prime `ell | s_i^perp` obeys

\[
\kappa_\ell\ge {1\over Q}-{1\over2Q}={1\over2Q}.
\]

Across `R` independent pairs, the chance that no difference is divisible
by this `ell` is at most

\[
(1-1/(2Q))^R\le e^{-R/(2Q)}\le {1\over2n}.
\]

The integer `s_i^perp<N<2^n` has fewer than `n` distinct rational prime
divisors.  A union bound shows that every one of them occurs in some
difference with probability at least `1/2`.  Raising each difference to
the `n`th power supplies its complete hidden primary power.  The leading
factor `A^n` supplies all complementary primaries, so `s_i|W`.

On this event P205 succeeds with probability at least `1/2` using a fresh
unit.  Multiplication gives total probability at least `1/4`.

Every divisor and every difference is below `A<N`, so each factor
`Delta_t^n` has fewer than `n^2` bits.  This gives total word length
`O((R+1)n^2)`.

## 5. Exact prime-power obstruction

For `A=b^a`, two uniform divisors are `b^I,b^J`, where `I,J` are uniform
in `{0,...,T-1}`.  If `h=ord_m(b)`, their residues agree exactly when

\[
I\equiv J\pmod h.
\]

Write `T=qh+r`.  There are `r` residue classes containing `q+1` exponents
and `h-r` classes containing `q` exponents.  The number of ordered unequal
pairs in equal residue classes is

\[
r(q+1)q+(h-r)q(q-1)
=h q(q-1)+2rq.
\]

Division by `T^2` proves `(P)`.  If `h>=T`, every exponent has a distinct
residue, and the numerator is zero.

Finally, `N=1+BH` gives

\[
uN=u+(uH)B
\]

for `1<=u<B`.  Complementation `B -> A/B` is a bijection on the divisor
set.  At `u=1`, this is the Euclidean quotient for every `B>1`; `B=1` is
one explicit exceptional atom.  This proves the stated pushforward radix
interpretation and completes the proof.
