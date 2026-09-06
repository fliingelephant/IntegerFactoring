# Proof of the F227 V2 AP-exponent sampler boundary

## 1. Fixed conventions and factor-cell geometry

The input length and uniform envelope are (Q0)--(Q2). In particular, for
the fixed constants in (Q2),

\[
\log_2\mathcal Q(n)=O((\log n)^{k_*})=o(n).
\tag{1}
\]

No constant in this estimate depends on a later history or stage.

The inequalities `p<q<2p` give

\[
\sqrt{N/2}<p<\sqrt N.
\tag{2}
\]

Hence `p` lies in `I_N`. Also, `q>sqrt(N)`, while `2p>sqrt(N)`.
Therefore the only integer in `I_N` having a nontrivial gcd with `N` is
`p` itself.

Every member of `C` has the same parity as the odd integer `p`, because
`L` is even. Thus every `x in C` is odd and `A_x=x-1` is even. Moreover,

\[
0<A_x<\sqrt N<q<2p.
\tag{3}
\]

The only possible positive multiple of `p` below `2p` is `p`, which is
odd. It cannot equal the even integer `A_x`. Consequently

\[
\gcd(A_x,N)=1
\qquad(x\in\mathcal C).
\tag{4}
\]

Factoring `A_x` cannot directly expose a hidden factor of `N`. The only
direct candidate screen is `x=p`.

## 2. Proof of the AP gcd mean

Use the identity

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d).
\tag{5}
\]

Fix `d|m`, and put `g=gcd(d,L)`. The congruence

\[
c+jL\equiv0\pmod d
\tag{6}
\]

has no solution if `g` does not divide `c`. If it has a solution, its
solutions form one residue class modulo `d/g`. In any interval of `H`
consecutive indices, their number is at most

\[
\frac{Hg}{d}+1\le\frac{HL}{d}+1.
\tag{7}
\]

A law with largest atom `eta` assigns this solution set mass at most `eta`
times (7). Taking expectations in (5) and interchanging the finite sums
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
\tag{8}
\]

Here `sum_(d|m) phi(d)=m`, and each `phi(d)/d` is at most one. Taking
`eta=1/H` proves Theorem A.

## 3. Local returns and the one-trial bound

Fix `x` and abbreviate `A=A_x`. A uniform unit modulo `N` has independent
uniform reductions in `F_p^*` and `F_q^*`. Each group is cyclic. Therefore

\[
\alpha_p(x)=\Pr(a^A=1\bmod p)
=\frac{\gcd(A,p-1)}{p-1},
\tag{9}
\]

\[
\alpha_q(x)=\Pr(a^A=1\bmod q)
=\frac{\gcd(A,q-1)}{q-1}.
\tag{10}
\]

Apart from `x=p`, every sound output of the declared return/primary-testing
channel requires a local return in at least one field:

- if neither field returns, `gcd(a^A-1,N)=1` and no primary test is valid;
- if exactly one returns, the gcd is proper; and
- if both return, the gcd is `N`, after which primary stripping can split
  the fields or certify common support.

Thus

\[
\Pr(\text{useful}\mid x)
\le \mathbf1_{x=p}+\alpha_p(x)+\alpha_q(x).
\tag{11}
\]

The direct event has `mu`-mass at most `eta`. Applying (8) with `m=p-1`
and `m=q-1` gives

\[
\Pr(\text{useful})
\le
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
\tag{12}
\]

This grants all sound postprocessing after a global return and grants the
factorization of `A` for free. Neither can evade the upper bound. Equation
(12) proves (B1), and `eta=1/H` proves (B2).

For an exact computational sampler, repeatedly draw a uniform residue
modulo `N`, compute its gcd with `N`, accept on gcd one, return a factor on a
proper gcd, and retry on gcd `N`. Ignoring the zero residue makes the next
draw uniform on the `N-1` nonzero residues. Exactly `p+q-2` of them are
proper nonunits. Thus the probability of factoring before accepting a unit
is

\[
\frac{p+q-2}{N-1}=O(1/p).
\tag{12a}
\]

This is smaller than `p^(-1/2+o(1))` and is absorbed in (18)--(19).

## 4. Uniform preterminal asymptotics

Let `W=|I_N|`. Since `sqrt(N)>=p`,

\[
W\ge \left(1-\frac1{\sqrt2}\right)p-2.
\tag{13}
\]

Any residue class in an interval of `W` consecutive integers occurs between
`floor(W/L)` and `ceil(W/L)` times. In the nonterminal range,

\[
L<\frac{N^{1/4}}{S(n)}
\le N^{1/4}<2^{1/4}p^{1/2}.
\tag{14}
\]

Equations (13)--(14) give, for absolute constants `c_1,c_2>0` and every
sufficiently large `N`,

\[
c_1\frac pL\le H\le c_2\frac pL.
\tag{15}
\]

The elementary uniform divisor bound

\[
\tau(m)=\exp\left(O\left(\frac{\log m}{\log\log m}\right)\right)
=m^{o(1)}
\tag{16}
\]

suffices. For completeness, split the prime factors of `m` at
`y=sqrt(log m)`. There are at most `y` small primes, each exponent is at
most `log_2 m`, so their contribution to `log tau(m)` is
`O(y log log m)`. The total multiplicity of primes above `y` is at most
`log m/log y`, and `e+1<=2^e`, so their contribution is
`O(log m/log log m)`. All implied constants here are absolute.

Balance gives `q=Theta(p)`. Definition (Q0) gives

\[
\log_2p=\frac n2+O(1).
\tag{17}
\]

From (1), `Q(n)=p^{o(1)}`, where this `o(1)` depends only on the fixed
constants `C_*` and `k_*`. If `eta H<=Q(n)`, equations (12), (14)--(17)
give, uniformly over every admissible history,

\[
\begin{aligned}
\Pr(\text{useful}\mid\text{history})
&\le \mathcal Q(n)\left[
\frac3H+
\frac{L\tau(p-1)}{p-1}+
\frac{L\tau(q-1)}{q-1}
\right]\\
&\le p^{-1/2+o(1)}.
\end{aligned}
\tag{18}
\]

Because the `o(1)` in (18) is uniform, there are fixed `c_0>0` and `n_0`
depending only on `Q` such that (B5) holds for every `n>=n_0` and every
admissible history.

Now expose an adaptive bank one trial at a time. On every history with no
earlier useful trial, the definition of `Q`-diffuse supplies the same atom
bound and a fresh independent uniform base. Therefore (B5) applies
conditionally at every one of at most `Q(n)` stages. The conditional union
bound gives

\[
\Pr(\text{some useful trial})
\le\mathcal Q(n)2^{-c_0n}
=2^{-\Omega(n)},
\tag{19}
\]

with constants independent of the input, history, and stage. This proves
Theorem B. It does not cover joint processing of nonreturn values, because
such processing is not a declared per-trial exit.

## 5. Fixed-base return progression

Fix a public unit `a` and enumerate the cell as

\[
x_j=x_0+jL\qquad(0\le j<H).
\tag{20}
\]

Let `j_p` be the index with `x_{j_p}=p`. Reduction modulo `p` returns
exactly when

\[
o_p\mid x_j-1.
\tag{21}
\]

This congruence is solvable because `j=j_p` is a solution. Put

\[
g_p=\gcd(o_p,L),\qquad u_p=o_p/g_p.
\tag{22}
\]

After division by `g_p`, the step `L/g_p` is invertible modulo `u_p`.
Thus (21) describes exactly one residue class of indices modulo `u_p`.
An interval of `H` consecutive indices contains at least
`floor(H/u_p)` such indices.

## 6. Every nonstale p-return is useful

Take a candidate for which the `p`-side returns.

- If it is `x=p`, the direct gcd gives `p`.
- If the `q`-side does not return, `gcd(a^A-1,N)=p`.
- If both sides return, both local orders divide the completely factored
  exponent `A`.

In the last case, use factor-first order stripping. For each prime divisor
`ell` of the current exponent `E`, test

\[
\gcd(a^{E/\ell}-1,N).
\tag{23}
\]

If the gcd is `N`, replace `E` by `E/ell` and repeat. If it is proper,
return the factor. If it is one, retain that primary exponent. If the whole
process returns no factor, the two local order valuations agree at every
prime, and the final value is

\[
E=o_p=o_q.
\tag{24}
\]

Its complete factorization is inherited from `A`, and the primary tests
certify `E|p-1` and `E|q-1`. If `E` does not divide `L`, adjoining it
strictly enlarges `L`. Therefore a `p`-return can fail to be useful only in
the stale case

\[
o_p=o_q\mid L.
\tag{25}
\]

For a nonstale base, every index in the return progression is useful, so

\[
\Pr(\text{useful})
\ge\frac{\lfloor H/u_p\rfloor}{H}
\ge\frac1{u_p}-\frac1H.
\tag{26}
\]

If `u_p<=Q(n)` and `H>=2Q(n)`, this is at least `1/(2Q(n))`. If
`H<2Q(n)`, enumerate the whole cell and compute `gcd(x,N)`; one entry is
`p`.

On the sampling branch, the expected number of candidates before progress is
at most `2Q(n)`. Every `A_x<sqrt(N)` has at most `n/2+O(1)` bits. After the
one fixed enlargement of `Q` allowed in (Q2), the remaining per-trial public
arithmetic is bounded by `Q(n)`. Hence a recursive routine supplied with the
postulated nonstale base satisfies (C4).

At recursion depth `i`, the bit length is at most `n/2^i+O(1)`. Taking logs
of the product of branching envelopes gives

\[
\sum_{i=0}^{O(\log n)}
O\!\left((\log(n/2^i+2))^{k_*}\right)
=O((\log n)^{k_*+1}).
\tag{27}
\]

Thus (C4) is numerical QP. This proves Theorem C, including its conditional
cost statement.

## 7. Rough-order corollary

Every prime divisor of

\[
u_p=\frac{o_p}{\gcd(o_p,L)}
\tag{28}
\]

is a prime divisor of `o_p`. If the latter order is `T(n)`-rough, then
either `u_p=1` or `u_p>T(n)`. Hence `u_p<=Q(n)<T(n)` forces `u_p=1`, which
is equivalent to `o_p|L`.

When `o_p|L`, the relations `o_p|p-1` and `x\equiv p\pmod L` imply
`o_p|x-1` for every `x in C`. Thus every candidate returns modulo `p`.
Section 6 gives a factor or new support unless `o_p=o_q|L`. This proves
Corollary D.
