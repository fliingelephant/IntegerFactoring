# Proof-blind statement — inverse-diagonal target and three sampler obstructions

Reconstruct or refute every claim below from this file only. Do not read the
candidate, its audit, `PROVED.md`, `FAILED.md`, `REGISTRY.md`, or
`notes/Progress.md`. Use no numerical search as proof. Give a self-contained
PASS/FAIL result and identify any false scope or constant.

## Setup

Let $N=pq$, where $p\ne q$ are odd primes. Let

\[
U_N=\{u\in\{1,\ldots,N-1\}:\gcd(u,N)=1\}.
\]

For $u\in U_N$, let $v(u)\in\{1,\ldots,N-1\}$ be its canonical inverse.
Define

\[
d(u)=u-v(u),\qquad \delta(u)=|d(u)|,
\qquad w(u)=\frac1{1+\delta(u)}.
\]

For an integer $d$, let $F_d=\{u\in U_N:d(u)=d\}$ and $f_d=|F_d|$. Put

\[
Z_N=\sum_{u\in U_N}w(u),
\qquad \pi(u)=\frac{w(u)}{Z_N}.
\]

Polynomial time means polynomial in $n=\lceil\log_2N\rceil$.

## Claims

### 1. Exact signed fibres

For every integer $d$,

\[
F_d=\left\{u\in\mathbb Z:
\max(1,1+d)\le u\le\min(N-1,N-1+d),\quad
u^2-du-1\equiv0\pmod N\right\}.
\]

Equivalently, each member satisfies

\[
u(u-d)=1+kN,\qquad 0\le k\le N-2,
\]

and

\[
(2u-d)^2=d^2+4+4kN.
\]

Writing $\Delta_d=d^2+4$ and extending the Legendre symbol by
$(0/r)=0$, the number of congruence roots before the canonical interval cut
is

\[
R_N(d)=
\left(1+\left(\frac{\Delta_d}{p}\right)\right)
\left(1+\left(\frac{\Delta_d}{q}\right)\right).
\]

Therefore $f_d\le4$, $f_d=f_{-d}$, and $F_d$ is empty for
$|d|\ge N-1$.

For an observed inverse pair,

\[
\Delta_{d(u)}\equiv(u+v(u))^2\pmod N.
\]

A proper $\gcd(\Delta_{d(u)},N)$ is an immediate factor. For uniform
$u\in U_N$, its probability is at most

\[
\frac2{p-1}+\frac2{q-1},
\]

which is $O(N^{-1/2})$ on balanced semiprimes.

### 2. The metric target has useful inverse-polynomial mass

Let $H_m=\sum_{j=1}^m1/j$. Then

\[
4\le Z_N\le8H_{N-1}-4.
\]

Exactly four states have $\delta=0$. They are the four roots of one modulo
$N$. Two are global, and the two mixed CRT roots reveal proper factors. If
$M_N$ is the two-element mixed set, then

\[
\pi(M_N)=\frac2{Z_N}
\ge\frac1{4H_{N-1}-2}
\ge\frac1{4\log(N-1)+2}.
\]

Thus a sampler within total-variation distance

\[
\frac1{8H_{N-1}-4}
\]

of $\pi$ still outputs a useful root with probability at least that amount.
$O(\log N)$ independent reruns then give constant factoring probability.

### 3. Uniform rejection is exponentially slow

Propose a uniform unit and accept it with probability $w(u)$. Conditional on
acceptance, the output is exactly $\pi$. Its expected proposal count is

\[
\frac{\varphi(N)}{Z_N}.
\]

Since $\varphi(N)\ge8N/15$, this is

\[
\Omega(N/\log N),
\]

which is exponential in $n$. Uniform proposals over all residues do not
improve the sampler-completion cost. On balanced semiprimes, nonunit gcds and
the public discriminant ticket occur with only $O(N^{-1/2+o(1)})$ probability
per proposal, so polynomially many trials do not rescue this named sampler.

### 4. Independent uniform-proposal Metropolis--Hastings is slow

Let $m=\varphi(N)$. For $x\ne y$, use

\[
P(x,y)=\frac1m\min\left(1,\frac{w(y)}{w(x)}\right)
\]

and place the remaining probability on $x$. This chain is reversible with
stationary law $\pi$.

From the public root $1$, the exact one-step leave probability is

\[
\ell=\frac{Z_N-1}{m}.
\]

For every integer $t\le m/(4(Z_N-1))$,

\[
\|P^t(1,\cdot)-\pi\|_{\rm TV}\ge\frac12.
\]

Thus worst-start mixing takes $\Omega(N/\log N)$ steps.

If $X_0$ is uniform on $U_N$, the chain can enter $M_N$ only when the start
or a uniform proposal is in $M_N$. Hence

\[
\Pr(X_t\in M_N)\le\frac{2(t+1)}m.
\]

When $t+1\le m/(4Z_N)$,

\[
\|\mathcal L(X_t)-\pi\|_{\rm TV}
\ge\frac{3}{2Z_N}
>\frac1{8H_{N-1}-4}.
\]

In polynomially many steps, its actual useful-root probability is negligible
on balanced semiprimes.

### 5. Nearest-neighbor descent has sealed local minima

Consider strict descent on the line neighbors $x-1,x+1$ using $\delta$.
Screen a nonunit neighbor by gcd. A non-increasing variant may cross ties.

If $N$ is odd, $\gcd(N,5)=1$, and

\[
u^2+u-1\equiv0\pmod N,
\]

then $u$ and $u+1$ are inverse units and both have $\delta=1$. The outer
neighbors $u-1$ and $u+2$ are units and have $\delta>1$. The pair
$\{u,u+1\}$ is therefore a closed minimum for both strict descent and any
non-increasing rule restricted to line neighbors. Its fibre discriminant is
$5$, so the discriminant gcd gives no factor under the hypothesis.

The smallest clean minimum-height example with two distinct odd prime factors
is

\[
N=209=11\cdot19,
\]

where

\[
79^{-1}=127,\quad80^{-1}=81,\quad82^{-1}=130\pmod{209}
\]

in canonical representatives. The four distances at $79,80,81,82$ are
$48,1,1,48$, and $\gcd(5,209)=1$.

## Scope

The target distribution has enough useful mass for factoring if sampled
efficiently. The claims rule out only uniform rejection, independent
uniform-proposal Metropolis--Hastings, and nearest-neighbor descent as
guaranteed polynomial-time access methods. They do not rule out every
sampler, larger moves, block-guided proposals, nonuniform sources, or other
factor screens. No factoring algorithm or general sampling lower bound is
claimed.
