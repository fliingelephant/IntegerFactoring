# Blind reconstruction: quadratic Fourier energy, sampling, and factoring

## Verdict and scope

The Fourier identity, the normalization formula, the sharp factor-revealing
mass bound, and the reduction from a sufficiently accurate sampler to complete
Las Vegas factoring are all valid.  They do **not**, by themselves, give an
unconditional factoring algorithm: the missing object is the explicit
factor-free sampler stated precisely in the final section.

The Markov-chain obstruction must be read with its quantifiers intact.  The
zero-atom calculation gives the general spectral-gap upper bound

\[
\operatorname{gap}(P)\leq \frac{S(N)}{2N^2}.
\]

It gives \(\Omega(N)\) worst-start mixing on the (in particular, balanced)
distinct-semiprime family, where \(S(N)=\Theta(N)\).  For unrestricted odd
\(N\), the lower-bound scale supplied by this eigenfunction is
\(N^2/S(N)\), not uniformly \(N\).  Thus a claim of a universal
\(\Omega(N)\) bound based only on this eigenfunction would need that
correction.

Throughout, residues are represented modulo \(N\),
\(\gcd(0,N)=N\), and total variation means

\[
d_{\rm TV}(\mu,\nu)=\sup_A|\mu(A)-\nu(A)|
  =\frac12\sum_x|\mu(x)-\nu(x)|.
\]

## 1. The quadratic Gauss-sum energy

Put

\[
e_N(t)=\exp(2\pi i t/N),\qquad
G_N(k)=\sum_{x\bmod N}e_N(kx^2).
\]

For odd \(N\), the change of variables

\[
u=x-y,\qquad v=x+y
\]

is a bijection on \((\mathbb Z/N\mathbb Z)^2\), because \(2\) is
invertible modulo \(N\).  Moreover, \(x^2-y^2=uv\).  Hence

\[
\begin{aligned}
|G_N(k)|^2
 &=\sum_{x,y\bmod N}e_N\bigl(k(x^2-y^2)\bigr)\\
 &=\sum_{u\bmod N}\sum_{v\bmod N}e_N(kuv).
\end{aligned}
\]

For fixed \(u\), the inner character sum is \(N\) if \(N\mid ku\),
and is zero otherwise.  If \(g=\gcd(k,N)\), exactly \(g\) residues
\(u\bmod N\) satisfy \(N\mid ku\).  Therefore

\[
\boxed{|G_N(k)|^2=N\gcd(k,N).}
\]

This includes \(k=0\): all \(N\) choices of \(u\) contribute, so both
sides equal \(N^2\).

Consequently the normalized Fourier-energy law is

\[
\pi_N(k)=\frac{|G_N(k)|^2}{\sum_{j\bmod N}|G_N(j)|^2}
          =\frac{\gcd(k,N)}{S(N)},
\qquad
S(N):=\sum_{j\bmod N}\gcd(j,N).
\]

## 2. Exact normalization

For every divisor \(d\mid N\), the number of residues \(k\bmod N\)
with \(\gcd(k,N)=d\) is \(\varphi(N/d)\).  This also covers \(d=N\),
using \(\varphi(1)=1\).  Grouping residues by their gcd gives

\[
\boxed{
S(N)=\sum_{d\mid N}d\,\varphi(N/d)
    =N\sum_{m\mid N}\frac{\varphi(m)}m.}
\]

The functions \(d\mapsto d\) and \(\varphi\) are multiplicative, so
their Dirichlet convolution \(S\) is multiplicative.  Equivalently, if
\(\gcd(A,B)=1\), CRT gives

\[
\gcd(k,AB)=\gcd(k_A,A)\gcd(k_B,B),
\]

and summing over the CRT product proves \(S(AB)=S(A)S(B)\).  It also
shows that, when the coprime factors are known,
\(\pi_{AB}=\pi_A\otimes\pi_B\) under CRT.

For a prime power,

\[
\begin{aligned}
S(p^a)
 &=p^a\left(1+\sum_{j=1}^a\frac{\varphi(p^j)}{p^j}\right)\\
 &=p^a\left(1+a\left(1-\frac1p\right)\right)\\
 &=\boxed{p^{a-1}\bigl((a+1)p-a\bigr)}.
\end{aligned}
\]

Thus, for \(N=\prod_i p_i^{a_i}\),

\[
\boxed{
\frac{S(N)}N
=\prod_i\left(1+a_i\left(1-\frac1{p_i}\right)\right).}
\]

## 3. Sharp mass on proper gcds

Let

\[
F_N=\{k\bmod N:1<\gcd(k,N)<N\}.
\]

There are \(\varphi(N)\) residues of gcd one, with total unnormalized
weight \(\varphi(N)\), and the sole residue of gcd \(N\) is zero, with
weight \(N\).  Hence

\[
\boxed{
\pi_N(F_N)=1-\frac{N+\varphi(N)}{S(N)}.}
\]

We now prove, sharply, that for every odd composite \(N\),

\[
\boxed{\pi_N(F_N)\geq\frac27,}
\]

with equality only for \(N=9\).

Write

\[
u_i=1-\frac1{p_i},\qquad
A=\frac{S(N)}N=\prod_i(1+a_i u_i),\qquad
B=\frac{\varphi(N)}N=\prod_i u_i.
\]

Every \(u_i\geq2/3\), since \(N\) is odd.  The desired inequality is
equivalent to

\[
5A\geq7(1+B). \tag{1}
\]

If \(N=p^a\) is a prime power, compositeness says \(a\geq2\), and the
difference between the two sides of (1) is

\[
5(1+au)-7(1+u)=(5a-7)u-2.
\]

This is nonnegative because \(a\geq2\) and \(u\geq2/3\).  Equality
forces \(a=2\) and \(u=2/3\), hence \(p=3\) and \(N=9\).  In fact the
prime-power mass has the useful closed form

\[
\pi_{p^a}(F_{p^a})
=\frac{(a-1)(p-1)}{(a+1)p-a}.
\]

Suppose instead that \(N\) has at least two distinct prime factors.
Increasing any exponent only increases \(A\), while leaving \(B\)
unchanged, so it is enough to put all exponents equal to one.  With
exactly two factors, say \(u,v\geq2/3\),

\[
5(1+u)(1+v)-7(1+uv)
=-2+5u+5v-2uv.
\]

This expression is increasing in each variable on \([2/3,1]\), and at
\(u=v=2/3\) it is \(34/9>0\).  With at least three distinct factors,

\[
5A\geq5(5/3)^3=625/27>14\geq7(1+B).
\]

Thus (1) is strict whenever there are at least two distinct prime
factors, completing both the bound and its equality classification.

### Distinct-semiprime formulas

Let \(N=pq\) for distinct odd primes \(p,q\), and put

\[
D=(2p-1)(2q-1)=4N-2p-2q+1.
\]

Then \(S(N)=D\), and all gcd classes are as follows.

| gcd value | number of residues | total \(\pi_N\)-mass |
|---:|---:|---:|
| \(1\) | \((p-1)(q-1)\) | \((p-1)(q-1)/D\) |
| \(p\) | \(q-1\) | \((N-p)/D\) |
| \(q\) | \(p-1\) | \((N-q)/D\) |
| \(N\) | \(1\) | \(N/D\) |

In particular,

\[
\boxed{
\pi_N(F_N)=\frac{2N-p-q}{D}
           =\frac12-\frac1{2D}.}
\]

If \(p,q=\Theta(\sqrt N)\), then the gcd-one and zero classes each
have asymptotic mass \(1/4\), while the two factor classes together
have asymptotic mass \(1/2\).

## 4. The sampler-to-factoring theorem

Here is the exact conditional hypothesis needed.  There is one uniform,
explicit classical algorithm \(\mathcal A\) such that, on every relevant
input \(M\), it

1. outputs a residue \(K\bmod M\) with law \(Q_M\) satisfying
   \(d_{\rm TV}(Q_M,\pi_M)\leq1/28\);
2. terminates almost surely;
3. has expected bit-operation cost at most a fixed polynomial
   \(P_t(\lceil\log_2(M+1)\rceil)\), and expected fair-bit cost at most a
   fixed polynomial \(P_b(\lceil\log_2(M+1)\rceil)\); and
4. uses no factorization, divisor advice, or equivalent oracle in its
   description or preprocessing.

The hypothesis may be stated for all integers; only odd composite inputs
are needed below.

For an odd composite \(M\), total variation and the sharp mass bound give

\[
Q_M(F_M)\geq\pi_M(F_M)-\frac1{28}
\geq\frac27-\frac1{28}=\boxed{\frac14}. \tag{2}
\]

Thus one sampler call followed by \(d=\gcd(K,M)\) produces a verified
proper divisor with probability at least \(1/4\).

### Complete algorithm

On input \(N\geq2\):

1. Remove the exact power of two dividing \(N\), recording that many
   factors \(2\).  If the odd remainder is one, stop.
2. On every current odd factor \(M\), run a deterministic
   polynomial-bit-time primality test.  If \(M\) is prime, record it.
3. If \(M\) is composite, repeatedly call \(\mathcal A(M)\) with fresh
   independent fair bits, compute \(d=\gcd(K,M)\), and discard the trial
   unless \(1<d<M\).
4. When a proper divisor is obtained, recurse on \(d\) and \(M/d\).
   Finally sort equal prime leaves into exponents and verify their product
   is the original input.

Every accepted split is correct because it is checked by an exact gcd and
integer division.  Every leaf is prime because it is accepted only after
an exact primality test.  No distributional assumption is used for
correctness; the distribution is used only to bound the wait.

This covers prime inputs, powers of two, odd prime powers, repeated prime
factors, and arbitrary composites.  In particular, no perfect-power
promise or squarefreeness is used.  If a split has overlapping prime
support on its two sides, recursion still terminates and the final
collection simply contains repeated prime leaves.

### Almost-sure termination and runtime/output correlation

At a fixed composite \(M\), fresh calls give independent copies of a pair
\((T_i,I_i)\), where \(T_i\) is the full cost of the sampler call and gcd,
and \(I_i\) indicates a proper divisor.  The runtime \(T_i\) may be
arbitrarily correlated with its own success indicator \(I_i\).  Let

\[
K=\min\{i:I_i=1\},\qquad q=\Pr(I_i=1)\geq1/4.
\]

The event \(\{K\geq i\}\) depends only on earlier trials and is therefore
independent of \(T_i\).  Tonelli's theorem gives

\[
\begin{aligned}
\mathbb E\left[\sum_{i=1}^{K}T_i\right]
 &=\sum_{i\geq1}\mathbb E[\mathbf 1_{\{K\geq i\}}T_i]\\
 &=\sum_{i\geq1}(1-q)^{i-1}\mathbb E[T_1]\\
 &=\frac{\mathbb E[T_1]}q
 \leq4\mathbb E[T_1]. \tag{3}
\end{aligned}
\]

So no unjustified independence between success and same-trial runtime is
being assumed.  The identical argument applies to fair-bit usage.
Moreover, \(\Pr(K=\infty)=0\), and each individual sampler call terminates
almost surely, so every split is found almost surely.

For the global bound, let \(n=\lceil\log_2(N+1)\rceil\).  A complete split
tree has at most \(n\) prime leaves, since their product is at most \(N\)
and every leaf is at least two; consequently it has fewer than \(2n\)
nodes.  Every node has at most \(n\) bits.  Let \(C(n)\) be a fixed
polynomial bounding one gcd, division, primality test, and the other local
integer bookkeeping, and replace \(P_t,P_b\) by monotone polynomial upper
bounds if necessary.  Enumerate the potential tree nodes in depth-first
order and assign zero cost to nonexistent slots.  Conditional on the
entire history before any existing composite-node slot, (3) bounds its
expected split cost by

\[
4(P_t(n)+C(n)).
\]

This bound is uniform in the random value of that node.  Hence correlations
between the successful trial, the divisor returned, and the shapes and
costs of later subtrees do not affect the estimate.  One explicit global
polynomial bound is

\[
\boxed{
\mathbb E[T(N)]
\leq 2n\bigl(C(n)+4(P_t(n)+C(n))\bigr)+C(n).}
\]

Likewise the expected number of fair bits is at most
\(8nP_b(n)\), up to any polynomially bounded random bits included in
\(C\) (the stated construction can take primality testing deterministic).
The finite split tree and almost-surely finite wait at every internal node
also prove almost-sure termination of the whole recursion.  Therefore the
hypothesized sampler yields a complete all-input classical Las Vegas
factoring algorithm in expected \(\operatorname{poly}(\log N)\) bit cost.

## 5. Auditing elementary exact methods

### Exact uniform-proposal rejection

There is a factor-free exact sampler, but it is too slow.  Repeatedly:

1. draw \(U\) uniformly from \(\mathbb Z/N\mathbb Z\);
2. compute \(g=\gcd(U,N)\);
3. draw \(V\) uniformly from \(\{0,\ldots,N-1\}\), and accept \(U\) iff
   \(V<g\).

For one iteration,

\[
\Pr(U=k\text{ and accept})=\frac1N\frac{\gcd(k,N)}N.
\]

The acceptance probability is \(S(N)/N^2\), and conditioning on acceptance
therefore gives exactly \(\pi_N\).  The exact expected number of proposals
is

\[
\boxed{\frac{N^2}{S(N)}.}
\]

For a distinct balanced semiprime,

\[
\frac{N^2}{S(N)}
=\frac{N^2}{4N-2p-2q+1}
=\frac N4\bigl(1+O(N^{-1/2})\bigr).
\]

An exact uniform integer in \([0,N-1]\) can be generated from fair bits
by drawing \(b=\lceil\log_2N\rceil\) bits and rejecting values at least
\(N\); the acceptance probability exceeds \(1/2\).  Thus each proposal
uses expected \(\Theta(\log N)\) fair bits and polynomially many bit
operations.  On balanced semiprimes this rejection sampler uses
\(\Theta(N\log N)\) fair bits and \(N\,\operatorname{poly}(\log N)\)
expected bit operations.  That is exponential in the input length.

### Direct uniform-residue gcd search

Drawing \(U\) uniformly and returning \(\gcd(U,N)\) when it is proper is
faster than the preceding exact sampler, but still not polynomial in the
input length.  For \(N=pq\), the successful residues are the nonzero
multiples of \(p\) or \(q\), of which there are

\[
(q-1)+(p-1)=p+q-2.
\]

Thus the exact success probability per draw is

\[
\frac{p+q-2}{N},
\]

and the expected number of gcd trials is

\[
\boxed{\frac{N}{p+q-2}=\Theta(\sqrt N)}
\]

for balanced semiprimes.  Its fair-bit cost is
\(\Theta(\sqrt N\log N)\), and its bit cost is
\(\sqrt N\,\operatorname{poly}(\log N)\).

There is also a formal direct mixture representation.  The identity

\[
\gcd(k,N)=\sum_{d\mid\gcd(k,N)}\varphi(d)
\]

shows that one could choose a divisor \(d\mid N\) with probability

\[
\frac{(N/d)\varphi(d)}{S(N)}
\]

and then choose uniformly among the \(N/d\) multiples of \(d\).  The
resulting probability of \(k\) is exactly \(\gcd(k,N)/S(N)\).  This is a
distributional identity, not a factor-free efficient implementation:
sampling that divisor law by enumerating or factorizing the divisor
lattice already exposes the unknown factors.

## 6. Lazy independence Metropolis: exact obstruction

Let \(g(x)=\gcd(x,N)\).  Consider independence Metropolis with target
\(\pi_N\), uniform proposal \(q(y)=1/N\), and acceptance probability

\[
\alpha(x,y)=\min\left\{1,\frac{g(y)}{g(x)}\right\}.
\]

Make it lazy by doing nothing with probability \(1/2\) and taking one
Metropolis proposal with probability \(1/2\).  For \(x\ne y\),

\[
P(x,y)=\frac1{2N}\min\left\{1,\frac{g(y)}{g(x)}\right\}.
\]

The usual detailed-balance identity here is immediate:

\[
\pi(x)\frac1N\alpha(x,y)
=\frac1N\min\{\pi(x),\pi(y)\},
\]

which is symmetric in \(x,y\).  Thus \(P\) is reversible with stationary
law \(\pi_N\).  Notice that the acceptance ratio cancels the unknown
normalizer; the chain is implementable using gcds, but implementation is
not the same as rapid mixing.

The zero residue is the unique state of maximal weight \(N\).  Put

\[
f(x)=\mathbf 1_{\{0\}}(x)-\pi_N(0)
    =\mathbf 1_{\{0\}}(x)-\frac N{S(N)}.
\]

For every \(x\ne0\), a proposal of zero is accepted, so
\(P(x,0)=1/(2N)\).  From zero,

\[
P(0,y)=\frac{g(y)}{2N^2}\quad(y\ne0),
\]

and hence

\[
P(0,0)=1-\frac{S(N)-N}{2N^2}.
\]

Substitution in the two cases \(x=0\) and \(x\ne0\) gives the exact
eigenrelation

\[
\boxed{
Pf=\lambda_0 f,
\qquad
\lambda_0=1-\frac{S(N)}{2N^2}.}
\]

Since \(f\) is nonconstant, reversibility gives

\[
\boxed{
\operatorname{gap}(P)\leq1-\lambda_0
=\frac{S(N)}{2N^2}.}
\]

More directly, starting at zero and applying the eigenrelation \(t\)
times yields

\[
P^t(0,0)-\pi_N(0)
=\lambda_0^t\bigl(1-\pi_N(0)\bigr),
\]

so

\[
\boxed{
\|P^t(0,\cdot)-\pi_N\|_{\rm TV}
\geq
\left(1-\frac{S(N)}{2N^2}\right)^t
\left(1-\frac N{S(N)}\right).} \tag{4}
\]

For \(N=pq\) with distinct odd primes, \(S(N)=D\leq4N\).  Also
\(D/N=(2-1/p)(2-1/q)\geq3\), since the smallest possible distinct odd
primes are \(3,5\).  Therefore \(1-N/D\geq2/3\), and for
\(t\leq N/8\), Bernoulli's inequality gives

\[
\left(1-\frac{D}{2N^2}\right)^t
\geq1-\frac{tD}{2N^2}\geq\frac34.
\]

The right side of (4) is then at least \(1/2\).  In particular the
worst-start mixing time to TV \(1/28\) is \(\Omega(N)\), already on
balanced distinct semiprimes, and the spectral-gap upper bound there is
\(D/(2N^2)=\Theta(1/N)\).

### The residual hitting obstruction

Avoiding the zero initialization does not make a uniform-proposal chain
polylogarithmic.  For \(N=pq\), let \(F=F_N\).  It has
\(|F|=p+q-2\) states.  From any state outside \(F\), entry into \(F\) in
the next lazy step requires proposing a member of \(F\), so its conditional
probability is at most

\[
\frac{|F|}{2N}=\frac{p+q-2}{2N}. \tag{5}
\]

For any initializer \(\nu_N\), a union bound therefore gives, with
\(\tau_F\) the first hitting time,

\[
\Pr_{\nu_N}(\tau_F\leq t)
\leq\nu_N(F)+t\frac{p+q-2}{2N}. \tag{6}
\]

Along balanced semiprimes, (5) is \(\Theta(N^{-1/2})\), whereas the target
mass

\[
\pi_N(F)=\frac12-\frac1{2D}
\]

is bounded away from zero.  Hence any family of initializers satisfying
\(\nu_N(F)=o(1)\) needs \(\Omega(\sqrt N)\) steps either to hit a proper
gcd with constant probability or to make the chain's final law have the
factor-class mass required for fixed small TV error.  The uniform
initializer has \(\nu_N(F)=(p+q-2)/N=\Theta(N^{-1/2})\), so it is covered
by this obstruction.  The bound applies even to an algorithm that checks
every proposal and stops immediately upon seeing a factor class.

## 7. Hidden factoring and the exact remaining gap

The closed form for \(S(N)\) is mathematically explicit but is not thereby
an efficient factor-free normalization algorithm.  This circularity is
already exact on distinct semiprimes:

\[
S(pq)=4N-2(p+q)+1
\quad\Longrightarrow\quad
p+q=\frac{4N+1-S(N)}2.
\]

Knowing exact \(S(N)\) therefore gives the roots of
\(X^2-(p+q)X+N\) and factors \(N\).  Thus a proposed sampler whose first
step is to compute this normalizer exactly has hidden the semiprime
factoring task.

Likewise, CRT factorization of \(\pi_N\) into its prime-power laws is an
excellent structural identity, but implementing it requires the unknown
prime powers.  Sampling gcd valuations on each \(p^a\) component and
recombining by CRT is a sampler given the factorization, not a factoring
algorithm.  The divisor-mixture construction above has the same issue.
This does not say that every exact sampler must explicitly compute the
factorization—the slow rejection sampler is a counterexample—it says that
normalizer-based and factorized implementations cannot be credited as
factor-free efficient samplers.

The precise unresolved lemma in this route is therefore:

> Construct one uniform classical fair-bit algorithm which, from the
> binary representation of every odd \(N\) and without any factorization
> advice or equivalent oracle, outputs a law \(Q_N\) on
> \(\mathbb Z/N\mathbb Z\) satisfying
> \(d_{\rm TV}(Q_N,\pi_N)\leq1/28\), terminates almost surely, and has both
> expected bit complexity and expected fair-bit complexity bounded by a
> fixed polynomial in \(\log N\).

If that lemma is supplied, Section 4 is a complete all-input Las Vegas
factoring proof.  Exact uniform rejection takes \(\Theta(N)\) iterations
on balanced semiprimes; direct uniform gcd search and the residual
Metropolis hitting mechanism take \(\Theta(\sqrt N)\)-scale trials; and
the zero-start Metropolis chain takes \(\Omega(N)\) steps to mix.  The
normalizer and factorized shortcuts use the information being sought.
Accordingly, none of those constructions fills the stated sampler gap.
