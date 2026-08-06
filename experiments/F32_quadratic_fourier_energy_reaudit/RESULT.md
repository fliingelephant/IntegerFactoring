# F32 strengthened hostile re-audit: quadratic Fourier energy

**Artifact audited:**
`experiments/F32_quadratic_fourier_energy_kill/RESULT.md` (current 505-line
version).

**Comparison material read:** the earlier F32 hostile audit and the strict
proof-blind reconstruction.  The present audit rederived the changed
Section 6 rather than relying on either report.

**Protocol:** proof-only hostile audit; no computation was used.  The
candidate was not edited.

## Verdict

> **CLEAN PASS.**

The strengthened Section 6 is correct.  For the stated lazy
uniform-proposal independence-Metropolis kernel, the centered indicator of
the zero residue is an exact eigenfunction with eigenvalue

\[
1-\frac{S(N)}{2N^2}.
\]

This gives a worst-start \(\Omega(N)\) mixing lower bound and the claimed
spectral-gap upper bound on fixed-balance distinct-semiprime families.  The
separate proper-gcd hitting argument is also correct: along such a family,
any sequence of initial laws with \(o(1)\) mass on factor-revealing residues
requires \(\Omega(\sqrt N)\) steps to reach any fixed total-variation error
strictly below \(1/2\).

The exact Gauss-energy identity, the sharp all-odd-composite \(2/7\) useful
mass bound, and the conditional sampler-to-all-input-Las-Vegas reduction
remain unchanged and valid.  The candidate still does **not** supply the
missing factor-free sampler and therefore is not a factoring algorithm.

No mathematical correction is required.  The phrase “fixed small
total-variation error” in Section 6 can be read precisely as any fixed
\(\varepsilon<1/2\); the proof below records the exact inequality.  This is
a scope clarification, not a defect in the candidate.

## 1. Kernel and stationary law

Put

\[
w(x)=\gcd(x,N),\qquad
\pi(x)=\frac{w(x)}{S(N)},\qquad
S(N)=\sum_{z\bmod N}w(z).
\]

The chain stays put with probability \(1/2\).  On the active half-step it
proposes \(y\) uniformly and accepts with probability

\[
\alpha(x,y)=\min\!\left(1,\frac{w(y)}{w(x)}\right).
\]

For distinct states \(x,y\),

\[
P(x,y)=\frac1{2N}\min\!\left(1,\frac{w(y)}{w(x)}\right)
\]

and hence

\[
\pi(x)P(x,y)
=\frac{\min(w(x),w(y))}{2NS(N)}
=\pi(y)P(y,x).
\]

Thus detailed balance with \(\pi\) is exact.  All proposal probabilities
are positive and all acceptance probabilities are positive, so the chain is
irreducible; explicit laziness makes it aperiodic.  The diagonal probability
also includes accepted self-proposals and rejected proposals, but neither
changes the off-diagonal calculation.

The transition rule is implementable from public \(N\) using gcds and
uniform residues, but a proposed residue with proper gcd already reveals a
factor.  The candidate correctly treats this chain only as one attempted
sampler/factoring mechanism, not as a factor-free construction.

## 2. Exact zero-atom transition probabilities

The zero residue has weight \(w(0)=N\).  For \(y\ne0\),

\[
P(0,y)
=\frac1{2N}\frac{w(y)}N
=\frac{w(y)}{2N^2}.
\tag{2.1}
\]

For every \(x\ne0\), a proposal of zero is accepted with probability one,
so

\[
P(x,0)=\frac1{2N}.
\tag{2.2}
\]

Summing (2.1) gives the exact zero-state diagonal:

\[
P(0,0)
=1-\sum_{y\ne0}P(0,y)
=1-\frac{S(N)-N}{2N^2}.
\tag{2.3}
\]

This formula correctly includes every contribution to staying at zero:
the explicit lazy half-step, an active proposal of zero, and rejected active
proposals.

## 3. Exact eigenrelation

Let

\[
\pi_0=\pi(0)=\frac N{S(N)},
\qquad
f=\mathbf 1_{\{0\}}-\pi_0,
\qquad
\lambda=1-\frac{S(N)}{2N^2}.
\]

Since constants are fixed by a Markov kernel,

\[
(Pf)(x)=P(x,0)-\pi_0.
\]

For \(x\ne0\), (2.2) gives

\[
(Pf)(x)
=\frac1{2N}-\frac N{S(N)}
=-\frac N{S(N)}
 \left(1-\frac{S(N)}{2N^2}\right)
=\lambda f(x).
\tag{3.1}
\]

At zero, (2.3) gives

\[
\begin{aligned}
(Pf)(0)
&=1-\frac{S(N)-N}{2N^2}-\frac N{S(N)}\\
&=\left(1-\frac N{S(N)}\right)
  \left(1-\frac{S(N)}{2N^2}\right)\\
&=\lambda f(0).
\end{aligned}
\tag{3.2}
\]

Therefore

\[
\boxed{Pf=\lambda f}
\]

with no asymptotic approximation.  Also \(f\) is nonzero and has
\(\pi\)-mean zero, so this is a genuine nonconstant eigenmode.

For an arbitrary initial law \(\mu_0\), duality and iteration yield

\[
\mu_0P^t(0)-\pi_0
=\mu_0P^t f
=\lambda^t\mu_0f
=\lambda^t\bigl(\mu_0(0)-\pi_0\bigr).
\tag{3.3}
\]

Taking the event \(\{0\}\) in the variational definition of total
variation proves

\[
\boxed{
\|\mu_0P^t-\pi\|_{\mathrm{TV}}
\ge
|\mu_0(0)-\pi_0|\lambda^t.}
\tag{3.4}
\]

Thus the “every initial law” quantifier in the candidate is correct.  The
bound can of course be zero for an initializer whose zero mass is already
exactly \(\pi_0\), which the candidate explicitly acknowledges.

## 4. Worst-start mixing and constants

Now let \(N=pq\), where \(p,q\) are distinct odd primes in a fixed-balance
family.  From the exact normalizer,

\[
S(N)=(2p-1)(2q-1)=4N-2(p+q)+1.
\tag{4.1}
\]

Fixed balance implies \(p+q=\Theta(\sqrt N)\), and therefore

\[
\pi_0=\frac N{S(N)}
=\frac14+O(N^{-1/2}),
\tag{4.2}
\]

and

\[
\lambda
=1-\frac{S(N)}{2N^2}
=1-\frac2N+O(N^{-3/2}).
\tag{4.3}
\]

Start the chain at zero.  If its total-variation distance at time \(t\) is
at most \(\varepsilon\), (3.4) forces

\[
(1-\pi_0)\lambda^t\le\varepsilon.
\]

Consequently

\[
t_{\mathrm{mix}}(\varepsilon)
\ge
\frac{\log((1-\pi_0)/\varepsilon)}
     {-\log(1-S(N)/(2N^2))}.
\tag{4.4}
\]

For every fixed \(0<\varepsilon<3/4\), the numerator tends to the positive
constant \(\log((3/4)/\varepsilon)\), while

\[
-\log\!\left(1-\frac{S(N)}{2N^2}\right)
=\frac2N+O(N^{-3/2}).
\]

Hence (4.4) is \(\Omega(N)\).  At \(\varepsilon=1/4\), it gives precisely

\[
t_{\mathrm{mix}}(1/4)
\ge
\left(\frac N2+o(N)\right)\log 3.
\tag{4.5}
\]

This is a valid standard worst-start bound because zero is an allowed
starting state.  It does not assert slow mixing from every initializer.

Because the chain is reversible and lazy, its spectrum is real and
nonnegative.  The nonconstant eigenvalue \(\lambda\) therefore gives

\[
\boxed{
\operatorname{gap}(P)
\le 1-\lambda
=\frac{S(N)}{2N^2}
=\frac2N+O(N^{-3/2}).}
\tag{4.6}
\]

The direction of this inequality is correct: another eigenvalue closer to
one could only make the actual gap smaller.

## 5. Proper-gcd hitting from other initializers

For \(N=pq\), define

\[
B=\{x:1<\gcd(x,N)<N\}.
\]

There are exactly

\[
|B|=(q-1)+(p-1)=p+q-2
\tag{5.1}
\]

such residues.  If the current state lies outside \(B\), entry into \(B\)
requires the active half-step to propose an element of \(B\).  From a unit,
all such proposals are accepted; from zero, their acceptance probabilities
are smaller than one.  Thus, uniformly over \(x\notin B\),

\[
P(x,B)\le\frac{|B|}{2N}
=\frac{p+q-2}{2N}.
\tag{5.2}
\]

Let \(b_0=\mu_0(B)\).  Conditional on starting outside \(B\), the event of
being in \(B\) at time \(t\) implies that at least one of the first \(t\)
steps entered \(B\).  A union bound using (5.2) therefore gives

\[
\boxed{
\mu_0P^t(B)
\le b_0+\frac{t(p+q-2)}{2N}.}
\tag{5.3}
\]

No independence between steps is used here.

The target mass is exactly

\[
\pi(B)=\frac12-\frac1{2S(N)}.
\tag{5.4}
\]

Therefore, whenever \(\|\mu_0P^t-\pi\|_{\mathrm{TV}}\le\varepsilon\),
(5.3)--(5.4) imply the more explicit lower bound

\[
t\ge
\frac{2N}{p+q-2}
\left(
\frac12-\frac1{2S(N)}-\varepsilon-b_0
\right),
\tag{5.5}
\]

provided the parenthesis is positive.  Along a fixed-balance family, if
\(b_0=o(1)\) and \(\varepsilon<1/2\) is fixed, that parenthesis is bounded
below by a positive constant for all sufficiently large \(N\), while
\(N/(p+q-2)=\Theta(\sqrt N)\).  This proves the candidate's residual
\(\Omega(\sqrt N)\) obstruction with the initializer and accuracy
quantifiers made explicit.

An efficient initializer returning an explicit residue with constant mass
in \(B\) is already a constant-success factoring routine: compute its gcd
with \(N\) and verify the resulting divisor.  This interpretive statement
is correct.  It does not turn the hitting bound into a universal lower bound
for all possible warm starts or all Markov chains.

## 6. Recheck of the unchanged energy identity

For odd \(N\),

\[
G_N(k)=\sum_{x\bmod N}e^{2\pi i kx^2/N}.
\]

The direct change of variables

\[
(x,y)\mapsto(u,v)=(x-y,x+y)
\]

is bijective modulo odd \(N\).  Hence an even shorter direct derivation than
the candidate's gcd reduction is

\[
\begin{aligned}
|G_N(k)|^2
&=\sum_{u,v\bmod N}e^{2\pi i kuv/N}\\
&=N\,\#\{u\bmod N:ku\equiv0\pmod N\}\\
&=N\gcd(k,N).
\end{aligned}
\tag{6.1}
\]

This includes \(k=0\), for which both sides equal \(N^2\).  It uses
oddness exactly where stated; the all-input reduction removes even factors
before sampling.

The count of gcd classes remains

\[
S(N)=\sum_{d\mid N}d\varphi(N/d),
\]

and multiplicativity gives

\[
S(p^e)=p^e+e\varphi(p^e).
\tag{6.2}
\]

No factorization is used by the identity itself; factors enter only in the
proof of the universal mass bound and in obstruction analysis.

## 7. Recheck of the \(2/7\) useful-mass theorem

For

\[
N=\prod_i p_i^{e_i},\qquad
b_i=1-p_i^{-1},\qquad
A=\frac{S(N)}N=\prod_i(1+e_i b_i),\qquad
B=\frac{\varphi(N)}N=\prod_i b_i,
\]

the only non-factor-revealing classes are the units and zero.  Therefore

\[
\rho(N)=1-\frac{1+B}{A}.
\tag{7.1}
\]

If \(N=p^e\) is composite, then \(e\ge2\) and, for odd \(p\),
\(b\ge2/3\).  Thus

\[
\frac{1+B}{A}
=\frac{1+b}{1+eb}
\le\frac{1+b}{1+2b}
\le\frac57,
\]

with equality exactly for \(p=3,e=2\), namely \(N=9\).

If at least two distinct primes divide \(N\), selecting two indices and
weakening numerator and denominator in the safe directions gives

\[
\frac{1+B}{A}
\le
\frac{1+b_1b_2}{(1+b_1)(1+b_2)}
\le\frac{13}{25}<\frac57.
\]

The bivariate expression decreases in either variable on \((0,1]\), and
each \(b_i\ge2/3\).  Hence

\[
\boxed{\rho(N)\ge2/7}
\]

for every odd composite, sharply at \(N=9\).  The strengthened Metropolis
discussion does not alter this distribution or event.

## 8. Recheck of the conditional Las Vegas theorem

Suppose the stated sampler returns an explicit residue from a law within TV
distance \(1/28\) of \(\pi_M\) for every odd \(M\), with almost-sure
termination and expected cost polynomial in \(\log M\) (and the fixed
accuracy parameter).  At every odd composite recursion node,

\[
\Pr(1<\gcd(k,M)<M)
\ge\frac27-\frac1{28}
=\frac14.
\tag{8.1}
\]

Every accepted gcd is deterministically verified, so all returned splits
are correct.  Fresh invocations make each call independent of the preceding
failures.  The number of calls per composite node is almost surely finite
with expectation at most four.  Same-call dependence between runtime and
success is harmless: the event that call \(i\) is reached depends only on
earlier fresh calls, so the stopped expected cost is bounded by the
geometric sum of the unconditional one-call cost bounds.

Deterministic primality testing handles primes before any repetition, and
even factors are split explicitly.  Every proper split reduces the integer;
if there are \(r\) prime leaves counted with multiplicity, then
\(2^r\le N\), so \(r\le\log_2N\).  The binary recursion tree consequently
has \(O(\log N)\) nodes.  All operands have \(O(\log N)\) bits, and the
sampler premise separately bounds both bit operations and fair random bits.
Linearity of conditional expectation gives one fixed polynomial bound for
the full recursion, and the finite collection of almost-sure node loops
terminates almost surely.

Thus the reduction covers primes, even inputs, prime powers, repeated prime
factors, unbalanced inputs, and arbitrary composites exactly as claimed.
It remains conditional on the missing all-input sampler.

## 9. Scope and hidden-assumption audit

- The exact zero eigenmode closes only the stated lazy uniform-proposal
  independence-Metropolis kernel.  It says nothing about nonuniform,
  nonlocal, augmented-state, or nonreversible samplers.
- The \(\Omega(N)\) result is a standard worst-start mixing bound.  It is
  not asserted for an initializer with exactly the correct zero mass.
- The residual \(\Omega(\sqrt N)\) result is conditional on
  \(\mu_0(B)=o(1)\) along balanced distinct-semiprime inputs and fixed
  requested error below \(1/2\).  Equation (5.5) exposes all quantifiers.
- Computing \(w(x)=\gcd(x,N)\) is public polynomial-time arithmetic, but
  observing a proper value reveals a factor.  The candidate does not hide
  this fact or count the Metropolis chain as the missing factor-free sampler.
- Exact \(S(pq)\) reveals \(p+q\); no normalizing-constant oracle is assumed
  by the conditional sampler interface.
- Uniform rejection remains \(\Theta(N)\) in proposal count on balanced
  semiprimes, and direct uniform proper-gcd discovery remains
  \(\Theta(\sqrt N)\).  The strengthened Section 6 is compatible with both
  earlier obstructions.
- The candidate continues to label the factor-free sampler as the exact
  open dependency.  It neither claims a complete factoring algorithm nor a
  universal classical sampling lower bound.

The current strengthened candidate is ready to retain its clean-audit
status within this exact conditional and mechanism-specific scope.
