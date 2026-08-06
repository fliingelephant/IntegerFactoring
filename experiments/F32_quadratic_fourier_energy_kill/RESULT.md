# F32 kill-first: quadratic Fourier energy puts constant mass on factors

**Status:** promoted as P41 after a strengthened hostile re-audit and a fresh
context-free proof-blind reconstruction.

**Family:** F23.

**Closest prior route and material difference.**  F07/P12 studies the
eigenphase support of modular multiplication and shows that natural moment
reconstruction can remain exponentially dense.  The present route uses a
different spectrum: the additive Fourier transform of the square-map
pushforward.  Its squared coefficient at frequency \(k\) is exactly
\(N\gcd(k,N)\) for odd \(N\).  Thus normalization gives constant, rather than
birthday-scale, mass to proper-gcd frequencies on every odd composite.

**Classification.**  This is a positive conditional reduction followed by
evidence against the two most immediate classical samplers.  It is not a
factoring algorithm: the required factor-free sampler remains missing.  The
result does not obstruct augmented-state chains, nonlocal proposals, positive
combinatorial encodings, or a direct sampler that never computes individual
frequency weights.

No computation was used.

## Outcome

For odd \(N\), define

\[
G_N(k)=\sum_{x\bmod N}\exp\!\left(\frac{2\pi i kx^2}{N}\right),
\qquad 0\le k<N.
\tag{0.1}
\]

Then

\[
\boxed{|G_N(k)|^2=N\gcd(k,N).}
\tag{0.2}
\]

Consequently the normalized quadratic Fourier-energy law is

\[
\pi_N(k)
=\frac{|G_N(k)|^2}{\sum_{\ell\bmod N}|G_N(\ell)|^2}
=\frac{\gcd(k,N)}{S(N)},
\qquad
S(N)=\sum_{\ell\bmod N}\gcd(\ell,N).
\tag{0.3}
\]

If \(N\) is any odd composite, then

\[
\boxed{
\Pr_{k\sim\pi_N}\bigl(1<\gcd(k,N)<N\bigr)\ge\frac27.}
\tag{0.4}
\]

Equality occurs at \(N=9\).  Therefore a classical sampler that, for every
odd \(N\), returns an actual residue with total-variation error at most
\(1/28\), almost-sure termination, and expected
\(\operatorname{poly}(\log N)\) bit and fair-random-bit cost would give an
all-input Las Vegas complete factorization algorithm.  Each sampler call
would expose a verified proper divisor with probability at least

\[
\frac27-\frac1{28}=\frac14.
\tag{0.5}
\]

This is genuine pooling: under the uniform frequency law, factor-divisible
frequencies have only \(N^{-1/2+o(1)}\) mass on balanced semiprimes.  The
energy weight multiplies those rare frequencies by their hidden gcd and
raises their total mass to nearly \(1/2\).

The obvious implementations do not realize that gain.

1. Uniform-proposal rejection with acceptance
   \(\gcd(k,N)/N\) has expected \(\Theta(N)\) proposals on balanced
   semiprimes.
2. The lazy independence-Metropolis chain with uniform proposals and target
   \(\pi_N\) has worst-start mixing time \(\Omega(N)\) on every fixed-balance
   semiprime family.  The zero atom supplies an exact slow eigenmode.  Even an
   initializer that repairs that atom but starts with negligible mass on
   proper-gcd residues faces an \(\Omega(\sqrt N)\) hitting obstruction.

An exact sampler need not use either mechanism and need not compute the
normalizing constant.  Those possibilities remain open.

## 1. The square-pushforward Fourier transform

Let

\[
\mu_N(y)=\#\{x\bmod N:x^2\equiv y\pmod N\}.
\tag{1.1}
\]

Its unnormalized additive Fourier transform is

\[
\widehat\mu_N(k)
=\sum_{y\bmod N}\mu_N(y)e^{2\pi i ky/N}
=\sum_{x\bmod N}e^{2\pi i kx^2/N}
=G_N(k).
\tag{1.2}
\]

Thus (0.3) is literally the normalized squared Fourier magnitude of the
square pushforward.  It is not the output distribution obtained merely by
sampling a uniform \(x\), computing \(x^2\), and applying a classical
Fourier transform; the multiplicities must interfere before squaring.

## 2. Exact Gauss-energy identity

First let \(M\) be odd and \(\gcd(a,M)=1\).  Expanding the square magnitude
gives

\[
|G_M(a)|^2
=\sum_{x,y\bmod M}e^{2\pi i a(x^2-y^2)/M}.
\tag{2.1}
\]

Because \(2\) is invertible modulo \(M\), the map

\[
(x,y)\longmapsto(u,v)=(x-y,x+y)
\tag{2.2}
\]

is a bijection on \((\mathbb Z/M\mathbb Z)^2\), and
\(x^2-y^2=uv\).  Hence

\[
|G_M(a)|^2
=\sum_{u\bmod M}\sum_{v\bmod M}e^{2\pi i auv/M}.
\tag{2.3}
\]

For fixed \(u\), the inner additive-character sum is \(M\) if
\(M\mid au\) and zero otherwise.  Coprimality leaves only \(u=0\), so

\[
|G_M(a)|^2=M.
\tag{2.4}
\]

Now take arbitrary \(k\bmod N\), put

\[
d=\gcd(k,N),\qquad N=dM,\qquad k=da.
\]

If \(k=0\), then \(d=N,M=1\), and the argument below still gives the right
value.  The phase in (0.1) depends only on \(x\bmod M\):

\[
e^{2\pi i kx^2/N}=e^{2\pi i ax^2/M}.
\]

Every residue modulo \(M\) has exactly \(d\) lifts modulo \(N\), whence

\[
G_N(k)=dG_M(a).
\tag{2.5}
\]

When \(M>1\), \(\gcd(a,M)=1\), so (2.4) applies; for \(M=1\),
\(G_1(0)=1\).  In either case,

\[
|G_N(k)|^2=d^2M=dN=N\gcd(k,N),
\]

proving (0.2).  No factorization of \(N\) and no prime-power Gauss-sum
formula was used in the identity.

## 3. Normalization and exact proper mass

For every divisor \(d\mid N\), exactly \(\varphi(N/d)\) residues
\(k\bmod N\) have \(\gcd(k,N)=d\).  Therefore

\[
S(N)=\sum_{d\mid N}d\,\varphi(N/d).
\tag{3.1}
\]

This arithmetic function is multiplicative.  At a prime power,

\[
\begin{aligned}
S(p^e)
&=p^e+\sum_{j=0}^{e-1}p^j\varphi(p^{e-j})\\
&=p^e+e\,p^{e-1}(p-1)
=p^e+e\varphi(p^e).
\end{aligned}
\tag{3.2}
\]

Write

\[
N=\prod_{i=1}^t p_i^{e_i},
\qquad
b_i=1-\frac1{p_i},
\qquad
A=\frac{S(N)}N=\prod_{i=1}^t(1+e_i b_i),
\qquad
B=\frac{\varphi(N)}N=\prod_{i=1}^t b_i.
\tag{3.3}
\]

The weight of \(k=0\) is \(N\), and the total weight of the unit frequencies
is \(\varphi(N)\).  All other residues have a proper gcd.  Thus their exact
stationary mass is

\[
\rho(N)
=1-\frac{N+\varphi(N)}{S(N)}
=1-\frac{1+B}{A}.
\tag{3.4}
\]

It remains to bound the last ratio for every odd composite.

### 3.1 One distinct prime

If \(t=1\), compositeness gives \(e_1\ge2\).  Put
\(b=b_1\ge2/3\).  Then

\[
\frac{1+B}{A}
=\frac{1+b}{1+e_1b}
\le\frac{1+b}{1+2b}.
\tag{3.5}
\]

The final expression decreases with \(b\), so

\[
\frac{1+B}{A}
\le
\frac{1+2/3}{1+4/3}
=\frac57.
\tag{3.6}
\]

The inequalities are equalities for \(N=3^2\).

### 3.2 At least two distinct primes

Choose two indices.  Since every remaining factor of \(A\) is at least one
and every remaining factor of \(B\) is at most one,

\[
\frac{1+B}{A}
\le
\frac{1+b_1b_2}{(1+b_1)(1+b_2)}.
\tag{3.7}
\]

The displayed function decreases in each variable on \((0,1]\).  Since
\(b_1,b_2\ge2/3\),

\[
\frac{1+B}{A}
\le
\frac{1+4/9}{(1+2/3)^2}
=\frac{13}{25}
<\frac57.
\tag{3.8}
\]

Equations (3.4), (3.6), and (3.8) prove (0.4).

For a distinct-prime semiprime, the exact formulas specialize to

\[
S(pq)=(2p-1)(2q-1)=4N-2(p+q)+1
\tag{3.9}
\]

and

\[
\rho(pq)
=\frac{2N-p-q}{4N-2p-2q+1}
=\frac12-\frac1{2S(pq)}.
\tag{3.10}
\]

Thus the useful mass is just below one half, even on balanced inputs.
Equation (3.9) also shows that an exact normalizing-constant oracle is already
a trace oracle:

\[
p+q=\frac{4N+1-S(pq)}2.
\tag{3.11}
\]

This does not show that approximate sampling is hard; a sampler need not
evaluate \(S(N)\) explicitly.

## 4. Conditional all-input Las Vegas factorization

Assume a classical routine \(\mathcal S\) with the following interface.  On
every odd \(M\ge3\) and rational accuracy \(\delta>0\), it returns an actual
residue \(k\in\{0,\ldots,M-1\}\); its law is within total variation
\(\delta\) of \(\pi_M\); it terminates almost surely; and its expected bit
and fair-random-bit cost is
\(\operatorname{poly}(\log M,\log\delta^{-1})\), with one fixed polynomial
independent of the factorization of \(M\).

At a recursion node \(M>1\):

1. Run deterministic polynomial-time primality testing.  If \(M\) is prime,
   return it as a leaf.
2. If \(M\) is even, return the verified split \(2\cdot(M/2)\).
3. Otherwise invoke \(\mathcal S(M,1/28)\) with fresh randomness, compute
   \(d=\gcd(k,M)\), and verify \(1<d<M\).  Accept such a \(d\); reject
   \(d=1\) or \(d=M\) and repeat.

For every odd composite, (0.4) and total-variation contraction for the proper
gcd event give per-call success at least \(1/4\).  Hence the number of calls
at that node has expectation at most four and is finite almost surely.
Every accepted split is verified, so no sampling error can produce an
incorrect output.

Recursively process both factors, merge equal prime leaves into exponents,
and verify the final powered product.  If the original factorization has
\(r\) prime leaves counted with multiplicity, then \(2^r\le N\), so
\(r\le n\), where \(n=\lceil\log_2(N+1)\rceil\).  The recursion tree has at
most \(2r-1\le2n-1\) nodes.  Fresh calls have expected polynomial cost
independent of earlier rejection events, so conditional expectation and
linearity give one fixed expected polynomial bound for the full tree.  No
independence between a call's own runtime and its own success is needed.
The finite tree and almost-sure geometric loops give almost-sure termination.

This covers primes, even inputs, prime powers, repeated factors, unbalanced
factors, and arbitrary composites.  It is conditional only on the sampler.

## 5. Why uniform rejection does not implement the sampler

The most direct exact rejection sampler proposes uniform \(k\bmod N\) and
accepts it with probability

\[
\frac{\gcd(k,N)}{N}.
\tag{5.1}
\]

The accepted law is exactly \(\pi_N\), but one proposal is accepted with
probability

\[
\frac1N\sum_{k\bmod N}\frac{\gcd(k,N)}N
=\frac{S(N)}{N^2}.
\tag{5.2}
\]

For \(N=pq\) with \(p\le q\le\kappa p\), (3.9) gives
\(S(N)=\Theta_\kappa(N)\).  The expected number of proposals is therefore
\(\Theta_\kappa(N)\), exponential in the input length.

Moreover, evaluating the numerator in (5.1) already computes the candidate
factor.  Uniform proposals encounter a proper gcd with probability

\[
\frac{p+q-2}{N}=\Theta_\kappa(N^{-1/2})
\tag{5.3}
\]

on this family.  Stopping as soon as that happens improves the scale only to
\(\Theta(\sqrt N)\), still exponential in \(\log N\).

## 6. The independence-Metropolis bottleneck

Consider the natural lazy chain on \(\mathbb Z/N\mathbb Z\):

- with probability \(1/2\), stay put;
- otherwise propose uniform \(y\bmod N\) and accept it from \(x\) with
  probability
  \[
  \min\!\left(1,\frac{\gcd(y,N)}{\gcd(x,N)}\right).
  \tag{6.1}
  \]

This is a reversible independence-Metropolis chain with stationary law
\(\pi_N\).  Write \(w(x)=\gcd(x,N)\),
\(\pi_0=\pi_N(0)=N/S(N)\), and

\[
f=\mathbf 1_{\{0\}}-\pi_0.
\]

For \(y\ne0\), the transition probabilities to and from the zero state are

\[
P(0,y)=\frac{w(y)}{2N^2},
\qquad
P(y,0)=\frac1{2N}.
\tag{6.2}
\]

Direct substitution at zero and away from zero gives the exact eigenrelation

\[
Pf=\lambda f,
\qquad
\lambda=1-\frac{S(N)}{2N^2}.
\tag{6.3}
\]

Consequently, for every initial law \(\mu_0\),

\[
\mu_0P^t(0)-\pi_0
=\lambda^t(\mu_0(0)-\pi_0),
\]

and therefore

\[
\|\mu_0P^t-\pi_N\|_{\mathrm{TV}}
\ge |\mu_0(0)-\pi_0|\lambda^t.
\tag{6.4}
\]

For a balanced distinct semiprime \(N=pq\), (3.9) gives

\[
\pi_0=\frac14+O(N^{-1/2}),
\qquad
\lambda=1-\frac2N+O(N^{-3/2}).
\]

Starting at zero, (6.4) implies, for every fixed
\(0<\varepsilon<3/4\),

\[
t_{\mathrm{mix}}(\varepsilon)
\ge
\frac{\log((1-\pi_0)/\varepsilon)}
     {-\log(1-S(N)/(2N^2))}
=\Omega(N).
\tag{6.5}
\]

In particular,
\(t_{\mathrm{mix}}(1/4)\ge(N/2+o(N))\log3\), and the spectral gap is at
most \(S(N)/(2N^2)=2/N+O(N^{-3/2})\).  This is a worst-start lower bound;
an initializer with exactly the correct zero mass can kill this eigenmode.

There is still a factor-class obstruction for any initializer that places
little mass on

\[
B=\{x:1<\gcd(x,N)<N\}.
\]

If \(b_0=\mu_0(B)\), entering \(B\) from outside requires an active uniform
proposal in \(B\), whose probability per step is at most
\((p+q-2)/(2N)\).  Thus

\[
\mu_0P^t(B)\le b_0+\frac{t(p+q-2)}{2N}.
\tag{6.6}
\]

Since \(\pi_N(B)=1/2+o(1)\), an initializer with \(b_0=o(1)\) still needs
\(\Omega(\sqrt N)\) steps for a fixed small total-variation error.  An
efficient initializer with constant explicit mass in \(B\) is already a
constant-success factoring routine, because a gcd reveals a factor.  These
arguments close only this uniform-proposal chain; no universal Markov-chain
lower bound is claimed.

## 7. What remains open

The quadratic energy law already performs the desired amortization at the
level of probability mass: exponentially sparse useful frequencies receive
constant total weight.  The missing operation is a classical factor-free
sampler with polynomial bit complexity.

The following are not ruled out:

- an augmented state space, analogous in spirit to adding near-perfect states
  in a matching chain, that connects the hidden gcd sectors rapidly;
- a nonlocal proposal kernel whose construction does not already reveal a
  proper gcd;
- an exact positive combinatorial representation of \(|G_N(k)|^2\) with a
  rapidly mixing marginal sampler;
- a hierarchical sampler that obtains interval masses without evaluating the
  factor-revealing exact normalization; or
- a different quadratic or higher-degree phase family with an easier
  factor-free spectral sampler.

A retry is materially new only if it supplies such a sampler and proves its
all-stream totality, total-variation error, almost-sure termination, and
expected polynomial bit/fair-random-bit cost, or if it changes the energy law
while retaining an all-input inverse-polynomial proper-factor mass.  Merely
sampling uniform frequencies, exact-rejecting by \(\gcd(k,N)\), or using the
uniform independence-Metropolis chain is covered by Sections 5--6.
