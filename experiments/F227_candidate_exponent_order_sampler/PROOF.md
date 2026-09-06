# Proof of the F227 AP-exponent sampler boundary

## 1. Geometry and coprimality of the factor cell

The inequalities `p<q<2p` give

\[
\sqrt{N/2}<p<\sqrt N.
\tag{1}
\]

Hence `p` lies in `I_N`. Also, `q>sqrt(N)`, while `2p>sqrt(N)`.
Therefore the only integer in `I_N` having a nontrivial gcd with `N` is
`p` itself.

Every member of `C` has the same parity as the odd integer `p`, because
`L` is even. Thus every `x in C` is odd and `A_x=x-1` is even. Moreover,

\[
0<A_x<\sqrt N<q<2p.
\tag{2}
\]

The only possible positive multiple of `p` below `2p` is `p`, which is
odd. It cannot equal the even integer `A_x`. Consequently

\[
\gcd(A_x,N)=1
\qquad(x\in\mathcal C).
\tag{3}
\]

Factoring `A_x` therefore cannot directly expose a hidden factor of `N`.
The only direct candidate screen is `x=p`.

## 2. Proof of the AP gcd mean

Use the standard identity

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d).
\tag{4}
\]

Fix `d|m`, and put `g=gcd(d,L)`. The congruence

\[
c+jL\equiv0\pmod d
\tag{5}
\]

has no solution if `g` does not divide `c`. If it has a solution, its
solutions form one residue class modulo `d/g`. In any interval of `H`
consecutive indices, their number is at most

\[
\frac{Hg}{d}+1\le\frac{HL}{d}+1.
\tag{6}
\]

A law with largest atom `eta` assigns this solution set mass at most `eta`
times (6). Taking expectations in (4) and interchanging the finite sums
gives

\[
\begin{aligned}
\mathbb E_\mu\frac{\gcd(A_j,m)}m
&\le \frac\eta m
\sum_{d\mid m}\varphi(d)
\left(\frac{HL}{d}+1\right)\\
&=\eta\left[
\frac{HL}{m}\sum_{d\mid m}\frac{\varphi(d)}d+1
\right]\\
&\le\eta\left(\frac{HL\tau(m)}m+1\right).
\end{aligned}
\tag{7}
\]

Here `sum_(d|m) phi(d)=m`, and every summand `phi(d)/d` is at most one.
Taking `eta=1/H` proves Theorem A.

## 3. Local return probabilities

Fix `x` and abbreviate `A=A_x`. A uniform unit modulo `N` has independent
uniform reductions in `F_p^*` and `F_q^*`. Each group is cyclic. Therefore
the exact local return probabilities are

\[
\alpha_p(x)=\Pr(a^A=1\bmod p)
=\frac{\gcd(A,p-1)}{p-1},
\tag{8}
\]

\[
\alpha_q(x)=\Pr(a^A=1\bmod q)
=\frac{\gcd(A,q-1)}{q-1}.
\tag{9}
\]

Apart from the direct event `x=p`, every sound output of the declared
return/primary-testing channel requires a local return in at least one
field. Indeed:

- if neither field returns, `gcd(a^A-1,N)=1` and no primary test is valid;
- if exactly one returns, the gcd is proper; and
- if both return, the gcd is `N`, after which primary stripping can either
  split the fields or certify common support.

It follows by a union bound that

\[
\Pr(\text{useful}\mid x)
\le \mathbf1_{x=p}+\alpha_p(x)+\alpha_q(x).
\tag{10}
\]

The direct event has `mu`-mass at most `eta`. Applying (7) with
`m=p-1` and `m=q-1` proves

\[
\Pr(\text{useful})
\le
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
\tag{11}
\]

This argument grants all sound postprocessing after a global return. It
also grants the factorization of `A` for free. Thus neither can evade the
upper bound.

## 4. Asymptotic preterminal bound

Let `W=|I_N|`. Since `sqrt(N)>=p`,

\[
W\ge \left(1-\frac1{\sqrt2}\right)p-2.
\tag{12}
\]

The cell contains `p`, and any residue class in an interval of `W`
consecutive integers occurs at least `floor(W/L)` times. In every
nonterminal state,

\[
L<\frac{N^{1/4}}{S(n)}
<2^{1/4}p^{1/2}.
\tag{13}
\]

Equations (12)--(13) imply, for all sufficiently large `p`,

\[
H\ge c\frac pL
\tag{14}
\]

for one absolute constant `c>0`.

For completeness, the elementary divisor estimate

\[
\tau(m)=\exp\left(O\left(\frac{\log m}{\log\log m}\right)\right)
=m^{o(1)}
\tag{15}
\]

suffices. One quick proof splits the prime factors of `m` at
`y=sqrt(log m)`. There are at most `y` small primes, each exponent is at
most `log_2 m`, so their contribution to `log tau(m)` is
`O(y log log m)`. The total multiplicity of primes above `y` is at most
`log m/log y`, and `e+1<=2^e`, so their contribution is
`O(log m/log log m)`.

Balance gives `q=Theta(p)` and `n=Theta(log p)`. A numerical-QP function
of `n` is `p^{o(1)}`. If `eta H` is numerical QP, equations (11), (13),
(14), and (15) give

\[
\begin{aligned}
\Pr(\text{useful})
&\le (\eta H)\left[
\frac3H+
\frac{L\tau(p-1)}{p-1}+
\frac{L\tau(q-1)}{q-1}
\right]\\
&=O\!\left(p^{-1/2+o(1)}\right)
=2^{-\Omega(n)}.
\end{aligned}
\tag{16}
\]

Conditioning on an adaptive history fixes `N,L,s` and the next candidate
law. If the law remains QP-diffuse and the next base is fresh uniform,
the same proof applies conditionally. A numerical-QP number of trials is
`2^{o(n)}`. The conditional union bound preserves `2^(-Omega(n))` total
useful mass. This proves Theorem B.

## 5. Fixed-base return progression

Now fix a public unit `a`. Enumerate the cell as

\[
x_j=x_0+jL\qquad(0\le j<H).
\tag{17}
\]

Let `j_p` be the index with `x_(j_p)=p`. Reduction modulo `p` returns
exactly when

\[
o_p\mid x_j-1.
\tag{18}
\]

This linear congruence is solvable because `j=j_p` is a solution. Put

\[
g_p=\gcd(o_p,L),\qquad u_p=o_p/g_p.
\tag{19}
\]

After division by `g_p`, the step `L/g_p` is invertible modulo `u_p`.
Thus (18) describes exactly one residue class of indices modulo `u_p`.
An interval of `H` consecutive indices contains at least
`floor(H/u_p)` such indices.

## 6. Every nonstale p-return is useful

Take any candidate for which the `p`-side returns.

- If it is `x=p`, the direct gcd gives `p`.
- If the `q`-side does not return, `gcd(a^A-1,N)=p`.
- If both sides return, both local orders divide the completely factored
  exponent `A`.

In the last case, use factor-first order stripping. For each prime divisor
`ell` of the current exponent `E`, test

\[
\gcd(a^{E/\ell}-1,N).
\tag{20}
\]

If the gcd is `N`, replace `E` by `E/ell` and repeat. If it is proper,
return the factor. If it is one, retain that primary exponent. If the
whole process returns no factor, the two local order valuations agree at
every prime, and the final value is

\[
E=o_p=o_q.
\tag{21}
\]

Its complete factorization is inherited from `A`, and the usual primary
tests certify `E|p-1` and `E|q-1`. If `E` does not divide `L`, adjoining
it strictly enlarges `L`.

Therefore a `p`-return can fail to be useful only in the stale case

\[
o_p=o_q\mid L.
\tag{22}
\]

For a nonstale base, every index in the return progression is useful, so

\[
\Pr(\text{useful})
\ge\frac{\lfloor H/u_p\rfloor}{H}
\ge\frac1{u_p}-\frac1H.
\tag{23}
\]

If `H>=2u_p`, this is at least `1/(2u_p)`. If `u_p<=Q(n)` but
`H<2Q(n)`, enumerate the entire cell and compute `gcd(x,N)`; one entry is
`p`.

Every `A_x` has at most `n/2+O(1)` bits. A numerical-QP number of such
recursive children gives a recurrence of the form

\[
T(n)\le Q(n)T(n/2+O(1))+Q(n).
\tag{24}
\]

On iterating through `O(log n)` size halvings, the product of the QP
factors is still

\[
2^{(\log n)^{O(1)}}.
\tag{25}
\]

This proves Theorem C and isolates the remaining source criterion.

## 7. Rough-order corollary

Every prime divisor of

\[
u_p=\frac{o_p}{\gcd(o_p,L)}
\tag{26}
\]

is a prime divisor of `o_p`. If the latter order is `T`-rough, then either
`u_p=1` or `u_p>T`. Hence `u_p<=Q<T` forces `u_p=1`, which is equivalent to
`o_p|L`.

When `o_p|L`, the relations `o_p|p-1` and `x\equiv p\pmod L` imply
`o_p|x-1` for every `x in C`. Thus every candidate returns modulo `p`.
Section 6 then gives a factor or new support unless
`o_p=o_q|L`. This proves Corollary D.
