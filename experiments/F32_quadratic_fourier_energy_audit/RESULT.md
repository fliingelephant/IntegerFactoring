# F32 hostile audit: quadratic Fourier energy

**Artifact audited:**
experiments/F32_quadratic_fourier_energy_kill/RESULT.md.

**Protocol:** fresh proof-only hostile audit. No computation was used. The
candidate and canonical files were not edited.

## Verdict

> **CLEAN PASS.**

The exact Gauss-energy identity, normalization, universal proper-factor mass,
semiprime specialization, conditional all-input Las Vegas reduction, and the
three stated naive-sampler obstructions are correct in their stated scopes. I
found no counterexample, quantifier failure, or hidden use of an unknown
factor in the unconditional claims.

The result remains only a conditional reduction. It does not construct the
required classical sampler. Computing an individual target weight by a gcd
may itself reveal a factor, and exact normalization on a semiprime reveals
the factor trace; the candidate explicitly quarantines both facts rather than
using either as a sampler. Thus this audit does not promote F32 to a factoring
algorithm.

## 1. Exact Gauss-energy identity

Let

\[
G_M(a)=\sum_{x\bmod M}e^{2\pi i a x^2/M}.
\]

If \(M\) is odd and \(\gcd(a,M)=1\), then

\[
\begin{aligned}
|G_M(a)|^2
&=\sum_{x,y\bmod M}e^{2\pi i a(x^2-y^2)/M}\\
&=\sum_{u,v\bmod M}e^{2\pi i auv/M}.
\end{aligned}
\]

The second equality is exact because
\((x,y)\mapsto(u,v)=(x-y,x+y)\) has determinant \(2\), hence is a
bijection modulo odd \(M\). For a fixed \(u\), the inner sum over \(v\) is
\(M\) exactly when \(M\mid au\), and is zero otherwise. Coprimality reduces
the first condition to \(u=0\), so

\[
|G_M(a)|^2=M.
\tag{1.1}
\]

Now let \(N\) be any odd positive integer and let \(0\le k<N\). Put

\[
d=\gcd(k,N),\qquad N=dM,\qquad k=da.
\]

The phase depends only on \(x\bmod M\), and each residue modulo \(M\) has
exactly \(d\) lifts modulo \(N\). Therefore

\[
G_N(k)=dG_M(a).
\]

For \(k\ne0\), \(a\) is a unit modulo \(M\), so (1.1) applies. For
\(k=0\), one has \(d=N\), \(M=1\), and \(G_1(0)=1\). Both cases give

\[
|G_N(k)|^2=d^2M=dN=N\gcd(k,N).
\tag{1.2}
\]

This covers every frequency, including zero, for every odd composite and in
fact for every odd \(N\). Oddness is essential to this proof and is not
silently extended to even moduli.

## 2. Normalization and multiplicativity

For each divisor \(d\mid N\), the residues with gcd exactly \(d\) are
\(k=dh\), where \(h\bmod N/d\) is a unit. Their number is
\(\varphi(N/d)\). Hence

\[
S(N)=\sum_{k\bmod N}\gcd(k,N)
=\sum_{d\mid N}d\,\varphi(N/d).
\tag{2.1}
\]

This is the Dirichlet convolution of the identity function with \(\varphi\).
Both functions are multiplicative, so \(S\) is multiplicative. Equivalently,
for coprime moduli CRT splits both the gcd class and its weight, giving the
same conclusion directly.

For \(N=p^e\), the \(d=p^e\) term contributes \(p^e\), while every one of
the remaining \(e\) terms equals \(p^{e-1}(p-1)\). Thus

\[
S(p^e)=p^e+e p^{e-1}(p-1)=p^e+e\varphi(p^e).
\tag{2.2}
\]

Equation (1.2) also gives

\[
\sum_{\ell\bmod N}|G_N(\ell)|^2=NS(N),
\]

so cancellation of the common factor \(N\) yields exactly

\[
\pi_N(k)=\frac{\gcd(k,N)}{S(N)}.
\]

There is no missing Parseval normalization or omitted frequency.

## 3. Universal proper-factor mass

Write

\[
N=\prod_{i=1}^t p_i^{e_i},\qquad
b_i=1-\frac1{p_i},\qquad
A=\frac{S(N)}N=\prod_i(1+e_i b_i),\qquad
B=\frac{\varphi(N)}N=\prod_i b_i.
\]

Only \(k=0\) has gcd \(N\), so its unnormalized weight is \(N\). The
unit frequencies have total weight \(\varphi(N)\). Every remaining residue
has a proper gcd. Consequently

\[
\rho(N)=1-\frac{N+\varphi(N)}{S(N)}
=1-\frac{1+B}{A}.
\tag{3.1}
\]

### One distinct prime

If \(N=p^e\) is composite, then \(e\ge2\) and, because \(N\) is odd,
\(b=1-1/p\ge2/3\). Therefore

\[
\frac{1+B}{A}
=\frac{1+b}{1+eb}
\le\frac{1+b}{1+2b}
\le\frac57.
\tag{3.2}
\]

The last function is strictly decreasing in \(b\). Equality in all steps
requires \(e=2\) and \(b=2/3\), hence \(N=9\). Directly,
\(S(9)=21\), and the proper class has total weight \(6\), so
\(\rho(9)=2/7\).

### At least two distinct primes

Choose two indices. Since \(e_i\ge1\), all omitted denominator factors are
at least one, and all omitted factors of \(B\) are at most one. Hence

\[
\frac{1+B}{A}
\le
\frac{1+b_1b_2}{(1+b_1)(1+b_2)}.
\tag{3.3}
\]

For

\[
f(x,y)=\frac{1+xy}{(1+x)(1+y)},
\]

one has

\[
\frac{\partial f}{\partial x}
=\frac{y-1}{(1+x)^2(1+y)}\le0,
\]

and symmetrically in \(y\). Since both selected \(b_i\)'s are at least
\(2/3\),

\[
\frac{1+B}{A}
\le f(2/3,2/3)=\frac{13}{25}<\frac57.
\tag{3.4}
\]

Thus every odd composite satisfies \(\rho(N)\ge2/7\), with equality only
at \(N=9\). The proof covers arbitrary exponents and any number of distinct
prime factors; it is not a semiprime-only estimate.

## 4. Distinct-semiprime specialization

For distinct primes \(p,q\), multiplicativity and (2.2) give

\[
S(pq)=(2p-1)(2q-1)=4pq-2p-2q+1.
\tag{4.1}
\]

The proper gcd classes have weights

\[
p\varphi(q)+q\varphi(p)=p(q-1)+q(p-1)=2pq-p-q.
\]

Therefore

\[
\rho(pq)
=\frac{2pq-p-q}{4pq-2p-2q+1}
=\frac12-\frac1{2S(pq)}.
\tag{4.2}
\]

Solving (4.1) for the trace gives

\[
p+q=\frac{4N+1-S(N)}2.
\]

Thus an exact normalization oracle on a promised semiprime is already a
factor-trace oracle, exactly as the candidate warns. No such oracle is used
in the conditional sampler reduction.

## 5. Conditional sampler-to-Las-Vegas reduction

Assume the candidate's one fixed classical sampler, called with
\(\delta=1/28\). Let \(E_M\) be the event that an output residue has a
proper gcd with an odd composite \(M\). Total variation controls every
event, so

\[
\Pr_{\mathcal S}[E_M]
\ge \pi_M(E_M)-\frac1{28}
\ge\frac27-\frac1{28}=\frac14.
\tag{5.1}
\]

The sampler always returns an actual residue. Computing and checking its gcd
therefore turns approximation error only into a rejected trial, never an
incorrect split.

The expected-cost assertion survives arbitrary correlation between a call's
runtime and its own success. To see this explicitly, fix a node \(M\), let
\(C_i\) be the bit cost of fresh call \(i\), and let \(K\) be the first
successful call. The event \(K\ge i\) depends only on calls before \(i\),
so it is independent of the fresh randomness, and hence the cost, of call
\(i\). If \(P(n,c)\) is a monotone fixed polynomial bounding one call at
input length at most \(n\) and accuracy-bit parameter \(c\), then

\[
\begin{aligned}
\mathbb E\!\left[\sum_{i=1}^{K}C_i\right]
&=\sum_{i\ge1}\mathbb E[\mathbf 1_{\{K\ge i\}}C_i]\\
&\le P(n,c)\sum_{i\ge1}(3/4)^{i-1}\\
&\le4P(n,c).
\end{aligned}
\tag{5.2}
\]

The identical argument applies to the fair-random-bit count. No independence
between \(C_i\) and the success of call \(i\) is assumed. Equation (5.1)
also gives \(\Pr(K=\infty)=0\).

All recursive factors are at most the original \(N\), so every arithmetic
operand has \(O(n)\) bits. Deterministic primality testing, Euclidean gcd,
exact division, multiplication, merging exponents, and final product
verification have a fixed polynomial bit bound, say \(Q(n)\), per node. If
the complete factorization has \(r\) prime leaves counted with multiplicity,
then \(2^r\le N\), hence \(r\le n\), and the binary recursion tree has at
most \(2n-1\) nodes. Thus the complete expected cost is bounded by a fixed
polynomial of the form

\[
(2n-1)\bigl(Q(n)+4P(n,\lceil\log_2 28\rceil)\bigr),
\tag{5.3}
\]

after enlarging \(Q\) to include the final verification. A bounded number of
almost-surely terminating node loops gives almost-sure termination of the
whole recursion.

Primality testing handles prime inputs before sampling. Even nodes split by
the verified factor \(2\); odd composite nodes use (5.1). Prime powers,
repeated factors, unbalanced factors, and composites with more than two
distinct primes require no additional promise. This verifies the candidate's
all-input conditional claim and its bit/fair-bit quantifiers.

## 6. Uniform rejection and direct uniform-gcd stopping

Under a uniform proposal \(k\bmod N\), accepting with probability
\(\gcd(k,N)/N\) produces an accepted mass proportional to
\(\gcd(k,N)\), hence exactly \(\pi_N\). The average acceptance probability
is

\[
\frac{S(N)}{N^2}.
\]

For a distinct semiprime, (4.1) gives \(S(N)=\Theta(N)\), so the expected
proposal count is

\[
\frac{N^2}{S(N)}=\Theta(N).
\tag{6.1}
\]

This remains an exponential bit-time scale even if proposal generation,
gcd evaluation, and the exact rational acceptance coin are each charged only
polynomial cost.

For \(N=pq\), the number of residues with proper gcd is

\[
\varphi(q)+\varphi(p)=p+q-2.
\]

Thus direct stopping on the first proper gcd of a uniform proposal succeeds
per proposal with probability

\[
\frac{p+q-2}{N}.
\tag{6.2}
\]

If \(p\le q\le\kappa p\) for fixed \(\kappa\), (6.2) is
\(\Theta_\kappa(N^{-1/2})\), and the expected proposal count is
\(\Theta_\kappa(\sqrt N)\). Both lower-bound statements are correctly
scoped to the displayed mechanisms and do not claim a general sampling
lower bound.

## 7. Independence-Metropolis bottleneck

Let \(g(x)=\gcd(x,N)\). For distinct states, the lazy uniform-proposal
kernel has flow

\[
\pi_N(x)P(x,y)
=\frac1{2NS(N)}\min(g(x),g(y)),
\]

which is symmetric in \(x,y\). Hence detailed balance and stationarity of
\(\pi_N\) are exact; the normalizing constant is not needed to run the
acceptance ratio.

For \(N=pq\) and the unit set \(U\), a proposal from a unit is always
accepted. The one-step probability of leaving \(U\) is therefore

\[
a_N=\frac12\frac{N-\varphi(N)}N
=\frac{p+q-1}{2N}.
\tag{7.1}
\]

Also

\[
\pi_N(U)=\frac{\varphi(N)}{S(N)}<\frac12.
\]

Starting at any unit, the event of never leaving in the first \(t\) steps
has probability

\[
(1-a_N)^t\ge1-ta_N.
\]

For every integer \(t\le1/(8a_N)\), the time-\(t\) law consequently puts
at least \(7/8\) on \(U\), while stationarity puts less than \(1/2\)
there. Its total-variation distance is therefore greater than \(3/8\), so

\[
t_{\rm mix}(1/4)
\ge\frac1{8a_N}
=\frac{N}{4(p+q-1)}.
\tag{7.2}
\]

Integer rounding can only strengthen this real-valued lower bound. On every
fixed-balance family, the right side is
\(\Omega_\kappa(\sqrt N)\). This is a worst-start mixing lower bound for
the stated lazy independence chain, not for augmented-state chains, nonlocal
proposals, warm starts that somehow already encode a factor, or arbitrary
samplers.

## 8. Hidden-assumption and prior-work checks

- The factors \(p_i\) are used only to prove arithmetic identities and
  probability bounds. The conditional recursion itself is given only \(M\),
  sampler output residues, and public polynomial-time arithmetic.
- Evaluating \(\gcd(k,N)\) at a useful frequency reveals the factor. This is
  intentional verification at the terminal step. It also explains why the
  displayed rejection and Metropolis implementations do not constitute a
  factor-free realization of the pooled law.
- Exact knowledge of \(S(pq)\) reveals \(p+q\), but the sampler premise does
  not assume an exact normalization oracle. Approximate sampling need not
  compute \(S\) explicitly.
- The closest promoted spectral boundary, P12/F07, concerns modular-
  multiplication order spectra and dense moment reconstruction. It neither
  proves nor contradicts the square-pushforward energy identity. The F32
  route is materially different in both spectrum and terminal missing lemma.
- The candidate consistently states that the factor-free sampler is missing.
  Accordingly it does not meet the top-level success criterion in PROMPT.md,
  and it makes no inflated hardness claim from the three naive mechanisms.

No required correction remains. The candidate is ready for a strict
proof-blind end-to-end reconstruction within this exact scope.
