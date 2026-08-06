# F33 follow-up: quadratic energy is a positive zero-product marginal, but coordinate heat bath is slow

**Status:** promoted as P43 after two historical failed audits, a clean
whole-artifact hostile re-audit, and a fresh context-free proof-blind
reconstruction.

**Family:** F23.

**Closest prior route and material difference.**  F32 gives a spectral law
whose frequency weight is \(\gcd(k,N)\), then leaves a classical factor-free
sampler open.  P38 gives an almost-uniform positive perfect-matching sampler,
but no graph whose matchings encode factor witnesses.  The present report
connects those routes: \(\gcd(k,N)\) is exactly the number of witnesses to the
positive modular relation \(kx=0\).  It then tests only the most direct
random-scan coordinate heat-bath sampler on that lifted relation.

**Classification.**  This is a positive representation and conditional
reduction followed by evidence against one exact sampler.  It is not a
mixing lower bound for augmented-state chains, block updates, nonlocal
proposals, positive matching encodings, or other samplers for the quadratic
energy law.

No computation was used.

## Outcome

For every positive integer \(N\), define

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}.
\tag{0.1}
\]

Then

\[
\#\{x:kx=0\}=\gcd(k,N),
\qquad
|\Omega_N|=S(N):=\sum_{k\bmod N}\gcd(k,N).
\tag{0.2}
\]

Consequently, the first marginal of the uniform law on \(\Omega_N\) is

\[
\Pr(k)=\frac{\gcd(k,N)}{S(N)}.
\tag{0.3}
\]

For odd \(N\), this is exactly F32's normalized quadratic Fourier-energy
law.  A positive sampler for the zero-product relation is therefore a
classical realization of the required interference distribution.

There is even more useful mass when both coordinates may be inspected.  If
\(N\) is any odd composite and \((k,x)\) is uniform on \(\Omega_N\), then

\[
\Pr\bigl(\text{at least one of }k,x\text{ has a proper gcd with }N\bigr)
\ge\frac13.
\tag{0.4}
\]

Thus a sampler within total variation \(1/12\), returning an actual pair,
would expose a verified proper divisor with probability at least \(1/4\).
Together with deterministic primality testing and recursion, it would give
complete all-input Las Vegas factoring under the same expected-bit and
almost-sure-termination interface as F32.

This also weakens the positive-matching target.  It would suffice to build a
polynomial-size bipartite graph whose perfect matchings decode with one
positive constant multiplicity to every pair in \(\Omega_N\).  P38's
almost-uniform matching sampler would then implement the preceding pair
sampler.  The graph need not encode integer divisor witnesses directly.

The obvious coordinate sampler is nevertheless slow.  On \(\Omega_N\),
choose one coordinate uniformly and resample it uniformly from the
annihilator of the other.  This random-scan heat-bath chain is reversible
with the uniform stationary law.  For \(N=pq\), distinct odd primes, start
from \((1,0)\).  If

\[
h_N=N-\varphi(N)-1=p+q-2
\tag{0.5}
\]

is the number of proper-gcd residues, then before a factor appears each step
enters a factor-bearing state with conditional probability at most
\(h_N/N\).  Its factor hitting time has expectation

\[
\Omega\!\left(\frac{N}{p+q}\right),
\tag{0.6}
\]

and

\[
t_{\rm mix}(1/4)
\ge
\left\lfloor\frac{N}{8(p+q-2)}\right\rfloor
\tag{0.7}
\]

up to the harmless convention at time zero.  On every fixed-balance
semiprime family, both scales are \(\Omega(\sqrt N)\).

The positive lift is therefore exact, but on distinct squarefree semiprimes
the exact one-coordinate Gibbs update only moves the hidden-sector bottleneck
from frequency space to creating unequal local zero-product types by a rare
nonunit proposal.

## 1. Exact positive lift

Fix \(k\bmod N\), put

\[
d=\gcd(k,N),\qquad k=dk_0,\qquad N=dN_0.
\]

The congruence \(kx=0\pmod N\) is equivalent to

\[
N_0\mid k_0x.
\]

Since \(\gcd(k_0,N_0)=1\), it is equivalent to \(N_0\mid x\).  Exactly the
\(d\) residues

\[
0,N_0,2N_0,\ldots,(d-1)N_0
\]

satisfy it.  This proves the first identity in (0.2); summing the fibre sizes
proves the second, and uniform marginalization proves (0.3).

For odd \(N\), F32 proves independently that

\[
\left|\sum_{y\bmod N}e^{2\pi i ky^2/N}\right|^2
=N\gcd(k,N).
\]

The common normalization therefore identifies (0.3) with the quadratic
Fourier-energy law.  Equation (0.2), unlike the Fourier identity, holds for
even \(N\) as well.

CRT also gives the structural product

\[
\Omega_N\cong\prod_{r^e\parallel N}\Omega_{r^e}.
\tag{1.1}
\]

For a prime \(r\),

\[
\Omega_r
=\bigl(\mathbb F_r\times\{0\}\bigr)
\cup
\bigl(\{0\}\times\mathbb F_r\bigr),
\qquad
|\Omega_r|=2r-1.
\tag{1.2}
\]

Thus, at a prime-field CRT component, the lifted state space is the union of
two coordinate axes.  Their common origin carries no intrinsic choice of
axis.  This description does not extend verbatim to prime powers: in
\(\Omega_{r^e}\), the condition is \(v_r(k)+v_r(x)\ge e\), so there are
intermediate valuation strata such as \((r,r^{e-1})\), not just two axes.

For a distinct squarefree semiprime, the exact interpretation uses three
local types.  At \(r\in\{p,q\}\), write

\[
H=(\mathbb F_r^\times\times\{0\}),\qquad
V=(\{0\}\times\mathbb F_r^\times),\qquad
O=\{(0,0)\}.
\tag{1.3}
\]

Neither coordinate has a proper gcd with \(N\) exactly when the two CRT
components have the same type: \((H,H)\), \((V,V)\), or \((O,O)\).  At
least one coordinate exposes a proper gcd exactly when the two local types
differ.  This statement does not assign an artificial axis label to a local
origin.

## 2. Proper-factor mass when both coordinates are readable

Let

\[
A_N=\{(k,x)\in\Omega_N:
\gcd(k,N),\gcd(x,N)\in\{1,N\}\}.
\tag{2.1}
\]

If neither coordinate has a proper gcd, each coordinate is either a unit or
zero.  Two units cannot have zero product.  Hence, for every composite
\(N\),

\[
A_N=
\bigl((\mathbb Z/N\mathbb Z)^\times\times\{0\}\bigr)
\mathbin{\dot\cup}
\bigl(\{0\}\times(\mathbb Z/N\mathbb Z)^\times\bigr)
\mathbin{\dot\cup}
\{(0,0)\},
\tag{2.2}
\]

and therefore

\[
|A_N|=2\varphi(N)+1.
\tag{2.3}
\]

Write, as in F32,

\[
N=\prod_{i=1}^t p_i^{e_i},\qquad
b_i=1-\frac1{p_i},
\]

\[
\frac{S(N)}N=\prod_i(1+e_ib_i),
\qquad
\frac{\varphi(N)}N=\prod_i b_i.
\tag{2.4}
\]

We prove

\[
\frac{2\varphi(N)+1}{S(N)}\le\frac23
\tag{2.5}
\]

for every odd composite.

First suppose \(t=1\).  Write \(N=p^e\), where \(p\ge3\) and \(e\ge2\),
and \(b=1-1/p\).  Inequality (2.5) is

\[
\frac{2b+p^{-e}}{1+eb}\le\frac23.
\tag{2.6}
\]

For \(e=2\), this reduces to

\[
2\left(1-\frac1p\right)+\frac3{p^2}\le2,
\]

which holds for \(p\ge3\).  For \(e=3\), it follows from
\(3/p^3\le2\).  For \(e\ge4\), the left side of the cross-multiplied
inequality only decreases as \(e\) grows.

Now suppose \(t\ge2\).  Choose the two smallest distinct prime factors and
write their \(b\)-values as \(b_1,b_2\).  Since the primes are distinct and
odd, after ordering

\[
b_1\ge\frac23,
\qquad
b_2\ge\frac45.
\tag{2.7}
\]

All omitted factors increase \(S(N)/N\) and do not increase
\(\varphi(N)/N\): an extra exponent leaves the latter ratio unchanged,
whereas an extra distinct prime decreases it.  Also,

\[
\frac1N\le(1-b_1)(1-b_2).
\]

It is therefore enough to show

\[
\frac{2b_1b_2+(1-b_1)(1-b_2)}
{(1+b_1)(1+b_2)}
\le\frac23.
\tag{2.8}
\]

After clearing the positive denominator, this is

\[
1-5b_1-5b_2+7b_1b_2\le0.
\tag{2.9}
\]

The left side is bilinear, so its maximum on
\([2/3,1]\times[4/5,1]\) occurs at a corner.  It is negative at all four
corners.  This proves (2.5).

Combining (2.3) and (2.5), the uniform probability of
\(\Omega_N\setminus A_N\) is at least \(1/3\), proving (0.4).  The bound is
asymptotically sharp along prime squares as the prime tends to infinity.

For a distinct semiprime \(N=pq\), the exact formulas are

\[
S(N)=(2p-1)(2q-1),
\qquad
|A_N|=2(p-1)(q-1)+1,
\tag{2.10}
\]

and

\[
\Pr(\Omega_N\setminus A_N)
=1-\frac{2(p-1)(q-1)+1}{(2p-1)(2q-1)}
>\frac12.
\tag{2.11}
\]

The strict inequality follows from \(2p+2q>5\).

## 3. Conditional samplers and positive matching graphs

Assume a uniform routine which, on odd \(M\ge3\) and rational
\(\delta>0\), returns an actual pair in \(\Omega_M\), has law within total
variation \(\delta\) of uniform, terminates almost surely, and has expected
bit and fair-random-bit cost polynomial in
\(\log M+\log\delta^{-1}\), with one fixed polynomial independent of the
factorization.

On an odd composite, invoke it with \(\delta=1/12\), compute the two gcds,
and accept either verified proper divisor.  Equations (0.4) and total
variation give success at least \(1/4\) per fresh invocation.  F32's
conditional-expectation argument then applies verbatim: no independence
between one call's runtime and its success is required.  Deterministic
primality testing, direct even splitting, fresh retries, exact division, and
recursion over at most \(2n-1\) nodes give complete all-input Las Vegas
factoring with one fixed expected polynomial bit/fair-bit bound.

There is a concrete sufficient matching hypothesis.  Suppose a uniform
polynomial-time builder returns, for every needed modulus \(N\), a
polynomial-size unweighted bipartite graph \(G_N\).  Suppose further that a
uniform deterministic algorithm decodes every perfect matching of \(G_N\)
to a pair in \(\Omega_N\), represents the two residues with \(O(\log N)\)
bits each, and runs in time polynomial in \(\log N+|G_N|\).  Finally, suppose
one positive integer \(c_N\) is the number of matching preimages of every
pair in \(\Omega_N\).  Uniform matchings then push forward to uniform
zero-product pairs.  P38's rational Jerrum--Sinclair--Vigoda implementation
supplies an actual almost-uniform matching in expected polynomial bit and
fair-bit cost, so the pair-sampler reduction above applies.

This graph condition is weaker than requiring one equal matching fibre for
every positive integer factorization \(xy=N\).  It is not constructed here.
P38's terminal-deletion subcube theorem still blocks several direct local
encodings, while P42's closed internal-edge COPY and AND gadgets show why one
may not transfer that boundary to all closed or globally filtered graphs.

## 4. The random-scan coordinate heat-bath chain

For \(y\bmod N\), let

\[
\operatorname{Ann}_N(y)=\{z\bmod N:zy=0\}.
\]

From \((k,x)\in\Omega_N\), one heat-bath step is:

1. with probability \(1/2\), replace \(k\) by a uniform element of
   \(\operatorname{Ann}_N(x)\);
2. otherwise, replace \(x\) by a uniform element of
   \(\operatorname{Ann}_N(k)\).

This is the random-scan Gibbs sampler for the uniform law on \(\Omega_N\).
For two states differing only in \(k\), the transition probability is

\[
\frac1{2|\operatorname{Ann}_N(x)|}
\]

in both directions; the same holds for an \(x\)-update.  Detailed balance
therefore holds with the uniform law.  The chain is irreducible because one
may set either coordinate to zero and then resample the other arbitrarily,
and it is aperiodic because it has self-loops.

Once \(g=\gcd(y,N)\) is known, the annihilator has the explicit description

\[
\operatorname{Ann}_N(y)
=\left\{j\frac Ng:0\le j<g\right\}.
\tag{4.1}
\]

It need not, and in general cannot efficiently, be enumerated.  To sample it
exactly, draw \(j\) uniformly from \(\{0,\ldots,g-1\}\) by fair-bit rejection
and return \(jN/g\pmod N\).  The rejection loop terminates almost surely and
uses expected \(O(\log N)\) fair bits and expected polynomial bit time.  If
\(1<g<N\), computing \(g\) has already factored \(N\).  Before that happens
on a semiprime, \(g\) is either 1 or \(N\): the update is therefore either
forced to zero or is an ordinary uniform residue.  The lower bound below
does not hide a hard transition implementation.

## 5. Hidden-type hitting and mixing lower bound

Let \(N=pq\) for distinct odd primes, and retain \(A_N\) from (2.1).  Its
complement consists exactly of factor-bearing states.  The number of
residues with proper gcd is

\[
h_N=N-\varphi(N)-1=p+q-2.
\tag{5.1}
\]

From a state \((u,0)\) with \(u\) a unit, an \(x\)-update is forced to keep
\(x=0\), while a \(k\)-update is uniform modulo \(N\).  Hence its one-step
probability of entering \(\Omega_N\setminus A_N\) is
\(h_N/(2N)\).  The same holds on the other unit axis.  From \((0,0)\),
either chosen coordinate is uniform, and the probability is \(h_N/N\).
Thus, conditional on every history which has remained in \(A_N\), the next
step exits with probability at most

\[
\frac{h_N}{N}.
\tag{5.2}
\]

Start from \((1,0)\), and let \(T\) be the first entrance time into the
factor-bearing complement.  A conditional union bound gives, for every
integer \(t\ge0\),

\[
\Pr(T\le t)\le\frac{t h_N}{N}.
\tag{5.3}
\]

Taking \(m=\lfloor N/(2h_N)\rfloor\),

\[
\mathbb E T
=\sum_{t\ge0}\Pr(T>t)
\ge\sum_{t=0}^{m}\left(1-\frac{t h_N}{N}\right)
=\Omega\!\left(\frac N{h_N}\right).
\tag{5.4}
\]

For mixing, if

\[
t\le\left\lfloor\frac{N}{8h_N}\right\rfloor,
\]

then the time-\(t\) law assigns mass at least \(7/8\) to \(A_N\).  By
(2.11), the uniform stationary law assigns mass strictly below \(1/2\) to
\(A_N\).  The total-variation distance is therefore greater than \(3/8\),
which proves (0.7) under the usual integer-time convention.

If \(p\le q\le\kappa p\), then

\[
h_N=p+q-2=\Theta_\kappa(\sqrt N),
\]

so (5.4) and (0.7) are both \(\Omega_\kappa(\sqrt N)\), exponential in the
input bit length.

This is the local-type mismatch obstruction described after (1.3): while one
coordinate is a unit, the other is pinned to zero, and reaching unequal CRT
types requires a uniform proposal to hit a nonunit in an unknown component.

## 6. What remains open

The positive representation is exact and removes cancellation from the
description of the desired law.  What remains missing is a sampler which
uses that representation without paying the uniform nonunit hitting scale.

The following mechanisms are not ruled out:

- a JSV-style augmented state space of near-zero-product defects which joins
  the local axes without first proposing a nonunit residue;
- a block heat bath, a modified coordinate-update scheme, or a nonlocal
  arithmetic proposal with a proved factor-free transition rule and rapid
  mixing;
- an efficiently generated warm start whose law is not concentrated on the
  unhelpful set \(A_N\);
- a polynomial-size positive matching graph for zero-product witnesses with
  controlled multiplicity;
- a globally filtered internal-edge graph, block code, or multiplication-
  specific matching construction of the kind left open by P38 and P42;
- a direct classical spectral sampler not expressed as a Markov chain on
  \(\Omega_N\); or
- another phase family whose positive lift has more connected local fibres.

A retry is materially new only if it supplies one of these constructions
with a symbolic all-stream polynomial bit/fair-bit bound, or proves a wider
sampler theorem in a precisely named model.  For the exact kernels and starts
analyzed there and here, reusing uniform rejection, uniform-proposal
independence Metropolis, or the random-scan single-coordinate heat bath is
covered by F32 and this report.  This does not cover new efficiently generated
initial laws or modified coordinate kernels.
