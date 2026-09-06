# F233 candidate — shifted quotient banks are projective gap-ratio covers

## Status and boundary

This is a proof-only candidate.  It gives exact incidence and progress laws
for the hard P202 branch where both exclusive residual odd orders remain
large and rough.  It also proves that the residue-independent coverage of a
rectangular shifted-quotient bank is no stronger, up to a constant factor,
than enlarging the public smooth-prime cutoff.  It is not an actual-input
counterfamily and not an all-input factoring algorithm.

The closest prior routes are F228, F230, F231/P202, and the failed pre-run
F232 packets.  F228 identifies quotient carry support.  P202 gives the
exact projected return law for an arbitrary factored multiplier word.  F232
first proposed aggregating shifted quotient factors but its two numerical
packets failed before execution.  F233 differs materially by eliminating
the hidden factors from the incidence test: the complete large-prime source
is one finite projective cover of the actual integer gap ratio.

Let

\[
N=pq,\qquad p<q<2p,\qquad
n=\lceil\log_2(N+1)\rceil,\qquad
B=2^{\lfloor n/2\rfloor},
\]

where `p` and `q` are distinct odd primes.  Work in the zero-defect branch

\[
B\mid N-1,\qquad H={N-1\over B},\qquad g=q-p.
\tag{1}
\]

Put

\[
P=(p-1)_{\rm odd},\quad Q=(q-1)_{\rm odd},\quad
D=\gcd(P,Q),\quad s_p=P/D,\quad s_q=Q/D.
\tag{2}
\]

Fix public integers

\[
Y\ge\max(U,C,3),\qquad 1\le U<B,\qquad 1\le C<H.
\tag{3}
\]

The bank consists of every positive shifted quotient child

\[
A_{u,c}=uH+c,
\qquad 1\le u\le U,quad -C\le c\le C.
\tag{4}
\]

Even multipliers are allowed.  In branch (1), Euclidean division gives

\[
uN=(uH)B+u
\]

for every `u<B`, so all values in (4) are genuine shifted quotient children.

## Theorem A — exact gap-ratio incidence

Let `ell` be a prime divisor of `s_p` or `s_q` that is not already absorbed
by the P202 smooth and child-supported word.  Thus

\[
\ell>Y,\qquad \ell\nmid H.
\tag{5}
\]

Define the nonzero gap ratio

\[
\rho_\ell=gB^{-1}\pmod\ell
\tag{6}
\]

and the rectangular projective cover

\[
\mathcal R_\ell(U,C)
=\left\{cu^{-1}\pmod\ell:
1\le u\le U,\ 1\le |c|\le C\right\}.
\tag{7}
\]

Then

\[
\boxed{
\begin{aligned}
\ell\mid s_p:quad
&\ell\mid A_{u,c}
\iff ug+cB\equiv0\pmod\ell,\\
\ell\mid s_q:quad
&\ell\mid A_{u,c}
\iff -ug+cB\equiv0\pmod\ell.
\end{aligned}}
\tag{8}
\]

Because the shift interval is symmetric,

\[
\boxed{
\ell\text{ occurs in some bank child}
\iff \rho_\ell\in\mathcal R_\ell(U,C)
}
\tag{9}
\]

in either hidden orientation.

The paired children expose the same hidden gap integer.  For every `(u,c)`,
the squarefree product of residual primes captured from `s_p` by
`A_{u,c}` and from `s_q` by `A_{u,-c}` divides

\[
|ug+cB|.
\tag{10}
\]

This is an integer-specific law.  The source depends on the actual gap
`q-p`, not only on abstract cyclic-group operations.

## Theorem B — exact saturated residual and Las Vegas progress

Let

\[
W_0=\operatorname{lcm}(1,\ldots,Y)^n
\prod_{\substack{\ell\mid H\\\ell>Y}}\ell^n
\tag{11}
\]

and, after complete factorization and direct gcd screening of the bank, set

\[
W_{U,C}=\operatorname{lcm}\left(
W_0,\left\{\operatorname{rad}(A_{u,c})^n\right\}_{u,c}
\right).
\tag{12}
\]

Raising each exposed prime to `n` gives maximal primary saturation without
introducing new prime support.  The surviving residuals are exactly

\[
\boxed{
r_p=\prod_{\substack{\ell^e\parallel s_p\\
\ell>Y,\ \ell\nmid H,\
\rho_\ell\notin\mathcal R_\ell(U,C)}}\ell^e,
\qquad
r_q=\prod_{\substack{\ell^e\parallel s_q\\
\ell>Y,\ \ell\nmid H,\
\rho_\ell\notin\mathcal R_\ell(U,C)}}\ell^e.
}
\tag{13}

If a bank gcd is proper, it already factors `N`.  Otherwise choose a fresh
uniform unit `x mod N`, put

\[
a=x^{2^n}\pmod N,
\qquad A=W_{U,C}H,
\]

and apply complete factor-first stripping.  For any accumulated common
certificate `M|D`, its exact factor-or-strict-growth probability is

\[
\boxed{
{1\over r_p}+{1\over r_q}-{1\over r_pr_q}
-{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
}
\tag{14}

Thus lcm aggregation does not create an additional probabilistic channel.
It changes (14) only through the prime incidences in (9).

## Theorem C — the universal coverage radius is only QP-smooth scale

For every prime `ell>max(U,C)` and every nonzero residue `h mod ell`, a
shifted child can capture `ell` precisely when

\[
h\in\mathcal R_\ell(U,C).
\]

The rectangular cover has the two sharp, elementary bounds

\[
\boxed{
\ell\le C(U+1)
\quad\Longrightarrow\quad
\mathcal R_\ell(U,C)=\mathbb F_\ell^*,
}
\tag{15}

and

\[
\boxed{
\ell-1>2CU
\quad\Longrightarrow\quad
\mathcal R_\ell(U,C)\ne\mathbb F_\ell^*.
}
\tag{16}

More exactly,

\[
|\mathcal R_\ell(U,C)|\le\min(\ell-1,2CU).
\tag{17}

Hence if a hypothetical hidden ratio were uniform in
`F_ell^*`, its exact hit probability would be
`|R_ell|/(ell-1)`, at most `2CU/(ell-1)`.  No such uniformity is asserted
for the actual gap ratio.

There is also no large-prime reuse across different slopes.  If

\[
\ell>2UC,qquad
\ell\mid uH+c,qquad
\ell\mid vH+d,
\]

then

\[
ud-vc=0.
\tag{18}

Thus the two pairs represent the same rational projective slope.  After
deduplicating slopes, each prime above `2UC` can occur in at most one bank
child.  Repeated child factorization and lcm aggregation cannot amplify a
missed large prime.

If `U,C,Y` have numerical-QP value, then so does

\[
Y_*:=\max(Y,2UC+1).
\tag{19}

A plain P202 smooth word through `Y_*` absorbs every prime for which this
rectangular bank could have a residue-independent coverage guarantee.
Therefore the bank's only possible advantage on the large-rough survivor is
the actual number-theoretic assertion

\[
\rho_\ell\in\mathcal R_\ell(U,C)
\]

for enough exclusive residual primes of one hidden factor.  Finite-field
coverage, generic mixing, complete child factorization, and lcm aggregation
do not prove that assertion.

## Cost boundary

There are `U(2C+1)` children.  Each obeys

\[
\operatorname{bits}(A_{u,c})
\le {n\over2}+O(\log(U+C+2)).
\]

For numerical-QP `U,C`, this is a fixed contraction for all sufficiently
large `n`.  Conditional on a correct all-input recursive dispatcher, the
bank and the factored word have numerical-QP total size and bit cost.  The
missing assertion is source density, not arithmetic accounting.

