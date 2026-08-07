# F50 — a one-residual defect Gibbs sampler retains the rare-nonunit bottleneck

## Status and scope

**Status:** corrected candidate exact obstruction. A first hostile audit passed
the core theorem and required two literal scope corrections: the distinct-prime
qualification for a totient identity and an ordering of the balanced factors.
Both corrections are included below, and that failed audit remains preserved.
This artifact is proof-only. It uses no computation, web search, or literature
claim.

**Family:** materially new F23 follow-up.

**Closest prior route and material difference.** X37/P43 keeps every state in

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}
\]

and applies a one-coordinate heat bath inside that set. The construction below
leaves \(\Omega_N\). It stores the nonzero residual as an explicit defect,
gives the defect sector a positive public activity, and applies an exact Gibbs
update on the augmented law. The transition is stochastic and noninvertible.
Thus P44 and P45 do not cover it, and P43's in-locus heat-bath theorem does not
imply the obstruction below.

**Classification claimed here.** The most direct one-defect construction is
fully implementable from bare \(N\), and its target conditioned on zero defect is
exactly uniform on \(\Omega_N\). Nevertheless, its factor-bearing hitting time
is \(\Omega(\sqrt N)\) on balanced semiprimes and on prime squares. Explicit
total-variation lower bounds give the same obstruction to mixing. More
strongly, changing the one scalar defect activity cannot remove the hitting
bottleneck. This is a method failure for the named single-residual,
one-coordinate-refresh construction. It is not a lower bound for block moves,
multiple interacting defects, nonlocal arithmetic proposals, or general
augmented samplers.

The only structural analogy used by the term "JSV-style" here is: enlarge a
hard exact sector by defect states, give the sectors tuned positive weights,
and use exact local resampling. No external theorem is invoked.

## 1. Exact augmented state space and target

Let

\[
R=\mathbb Z/N\mathbb Z
\]

with residues represented by \(0,\ldots,N-1\). Define

\[
\widehat\Omega_N
=\{(k,x,d)\in R^3:d=kx\},
\]

where the equality is in \(R\). The defect coordinate is redundant but makes
the two sectors explicit:

\[
G_N=\{d=0\}\cong\Omega_N,
\qquad
D_N=\{d\ne0\}.
\]

For a positive rational activity \(\lambda\), assign unnormalized weight

\[
W_\lambda(k,x,d)=
\begin{cases}
1,&d=0,\\
\lambda,&d\ne0.
\end{cases}
\tag{1.1}
\]

Write

\[
S(N)=|\Omega_N|=\sum_{k\bmod N}\gcd(k,N).
\]

The target law is

\[
\widehat\pi_{N,\lambda}(k,x,d)
=\frac{W_\lambda(k,x,d)}
{Z_{N,\lambda}},
\qquad
Z_{N,\lambda}=S(N)+\lambda\bigl(N^2-S(N)\bigr).
\tag{1.2}
\]

Conditioned on \(G_N\), this law is exactly uniform on \(\Omega_N\), for every
\(\lambda>0\). The chain below never needs to compute either \(S(N)\) or
\(Z_{N,\lambda}\).

The canonical public choice is

\[
\boxed{\lambda=1/N.}
\tag{1.3}
\]

It assigns inverse ambient-fibre scale to one violated equation. Its good-sector
mass is

\[
\gamma_N
=\widehat\pi_{N,1/N}(G_N)
=\frac{S(N)}{N+(1-1/N)S(N)}.
\tag{1.4}
\]

Since the zero residue contributes \(N\) to \(S(N)\), while each of the other
\(N-1\) residues contributes at least one,

\[
S(N)\ge 2N-1.
\]

Consequently

\[
\gamma_N>
\frac{S(N)}{N+S(N)}
\ge\frac{2N-1}{3N-1}>\frac12.
\tag{1.5}
\]

Thus the public activity does not hide the desired sector behind an
exponentially small stationary probability.

A finer residual-by-residual calibration is not the canonical bare-\(N\)
choice. If

\[
M_N(d)=|\{(k,x)\in R^2:kx=d\}|,
\]

then assigning per-state activity proportional to \(1/M_N(d)\) gives every
residual value the same total mass. It also gives \(G_N\) only \(1/N\) of the
total mass because there are \(N\) residual values. Moreover, for every unit
\(d\),

\[
M_N(d)=\varphi(N):
\]

both coordinates must be units, and each unit \(k\) determines the unique
\(x=dk^{-1}\). On a product of two distinct primes, exact \(\varphi(N)\) gives
\(p+q=N+1-\varphi(N)\), and the resulting quadratic factors \(N\). Grouping
all nonzero residuals into one defect sector and using the public inverse scale
\(1/N\) avoids both defects. This observation does not rule out a different
computable nonconstant weight family.

## 2. Exact stochastic transition

Use random-scan Gibbs resampling. Choose one of \(k,x\) with one fair bit and
resample that coordinate from its exact conditional law. Recompute
\(d=kx\bmod N\).

For example, hold \(x\) fixed and put

\[
g=\gcd(x,N),
\qquad
A_x=\{a\in R:ax=0\}
=\{jN/g:0\le j<g\}.
\]

There are \(g\) zero-defect choices and \(N-g\) defect choices. Under the
canonical activity, first choose the zero-defect sector with probability

\[
\frac{Ng}{Ng+N-g};
\tag{2.1}
\]

otherwise choose the defect sector. Conditional on the chosen sector, sample
uniformly from \(A_x\) or \(R\setminus A_x\), respectively. Equivalently, the
point probabilities are

\[
\Pr(k'=a\mid x)=
\begin{cases}
\displaystyle\frac{N}{Ng+N-g},&a\in A_x,\\[6pt]
\displaystyle\frac{1}{Ng+N-g},&a\notin A_x.
\end{cases}
\tag{2.2}
\]

The update of \(x\) is symmetric. For general activity \(\lambda\), replace
(2.1) by

\[
\frac{g}{g+\lambda(N-g)}.
\tag{2.3}
\]

These are full-coordinate heat-bath moves. They remove proposal rejection as a
possible explanation for slow movement; the scalar Metropolis variant is
treated separately in Section 7.

### Stationarity and qualitative chain properties

Equation (2.2) is the exact conditional distribution derived from (1.1).
Therefore each coordinate update satisfies detailed balance with
\(\widehat\pi_{N,1/N}\), and so does their random mixture. Every conditional
point probability is positive. Two updates in a specified coordinate order can
therefore move between any two states with positive probability. The chain is
irreducible. Resampling the current coordinate value has positive probability,
so it is aperiodic. The update forgets the old coordinate and is not an
invertible state map.

### Uniform fair-bit implementation

No unknown factor is used.

1. Compute \(g=\gcd(x,N)\) by the integer Euclidean algorithm. A proper value
   of \(g\) is already a valid output, but the sampler can also continue.
2. Sample the rational coin (2.1). For integers \(0\le A\le B\), an exact
   \(A/B\) coin is obtained by drawing uniformly below the next power of two,
   rejecting values at least \(B\), and comparing the accepted value with
   \(A\). The expected number of rounds is less than two. Here \(B<N^2+N\).
3. To sample from \(A_x\), sample \(j\) uniformly in \(\{0,\ldots,g-1\}\)
   by the same fair-bit rejection and return \(jN/g\).
4. To sample from the complement, sample uniformly in \(R\) and reject points
   in \(A_x\). If \(g<N\), then \(g\mid N\) gives \(g\le N/2\), so the
   expected number of trials is at most two. If \(g=N\), the complement has
   zero sector probability and is not sampled.

Each transition terminates almost surely. It uses \(O(\log N)\) expected fair
bits and polynomial bit time. All stored integers have \(O(\log N)\) bits.
Schoolbook arithmetic already gives one fixed polynomial bound; faster
arithmetic is unnecessary for the claim.

## 3. Factor extraction and the conditional positive boundary

At the initial state and after every transition, compute

\[
\gcd(k,N),\qquad \gcd(x,N).
\]

Return either value if it is strictly between \(1\) and \(N\). Every return is
a verified factor. Define the factor-bearing set

\[
F_N=\{(k,x,d):1<\gcd(k,N)<N
\text{ or }1<\gcd(x,N)<N\}.
\tag{3.1}
\]

Within \(G_N\), this is exactly the useful part of the uniform zero-product
relation. By P43, it has at least one third of uniform \(\Omega_N\)-mass for
every odd composite. Equations (1.4)--(1.5) therefore give

\[
\widehat\pi_{N,1/N}(F_N\cap G_N)>\frac16.
\tag{3.2}
\]

Hence a terminal draw within total variation \(1/24\) of the augmented target
would reveal a proper factor with probability greater than \(1/8\), without
even using factor-bearing defect states. Fresh verified calls and recursive
splitting would then give the same all-input Las Vegas reduction as P43.

The construction therefore has the correct target, sector mass, exact
transition, and extraction rule. Its failure is dynamical.

## 4. Exact rare-nonunit lemma

Let

\[
U_N=R^\times,
\qquad
H_N=\{a\in R:1<\gcd(a,N)<N\},
\qquad
h_N=|H_N|=N-\varphi(N)-1.
\tag{4.1}
\]

Assume in this section that \(N\) is composite, so \(h_N>0\).
Before the monitored chain reaches \(F_N\), both coordinates lie in

\[
C_N=(U_N\cup\{0\})^2.
\tag{4.2}
\]

This makes the one-step factor hazard exact.

### Lemma 4.1 — canonical activity

Start from any state in \(C_N\), and let

\[
T_F=\inf\{t\ge1:X_t\in F_N\}.
\]

For the activity \(1/N\), conditional on \(T_F>t\), the probability of
entering \(F_N\) at transition \(t+1\) is at most

\[
\alpha_N=\frac{h_N}{N}.
\tag{4.3}
\]

Consequently, for every integer \(t\ge0\),

\[
\Pr(T_F>t)\ge(1-\alpha_N)^t,
\qquad
\Pr(T_F\le t)\le t\alpha_N,
\qquad
\mathbb E T_F\ge\frac{N}{h_N}.
\tag{4.4}
\]

### Proof

On the survival event, the coordinate held fixed by an update is either zero
or a unit.

If it is zero, every candidate for the refreshed coordinate has zero defect
and equal weight. The refresh is uniform on \(R\), so its probability of
landing in \(H_N\) is exactly \(h_N/N\).

If the held coordinate is a unit, its annihilator is \(\{0\}\). Formula
(2.2) assigns each nonzero residue probability \(1/(2N-1)\), so the factor
probability is

\[
\frac{h_N}{2N-1}<\frac{h_N}{N}.
\]

The bound holds after every survival history. Multiplying the conditional
survival bounds proves the first inequality in (4.4). A union bound proves the
second. Summing the tail probabilities proves

\[
\mathbb E T_F
=\sum_{t\ge0}\Pr(T_F>t)
\ge\sum_{t\ge0}(1-\alpha_N)^t
=1/\alpha_N.
\]

\(\square\)

### Lemma 4.2 — retuning the scalar activity does not help

For every \(\lambda>0\), the corresponding Gibbs chain has conditional
factor hazard at most

\[
\frac{h_N}{N-1}
\tag{4.5}
\]

before \(T_F\). Thus

\[
\mathbb E T_F\ge\frac{N-1}{h_N}.
\tag{4.6}
\]

Indeed, a zero held coordinate again gives probability \(h_N/N\). A unit
held coordinate gives

\[
\frac{h_N\lambda}{1+(N-1)\lambda}
<\frac{h_N}{N-1}.
\tag{4.7}
\]

This statement even grants a factor-dependent or otherwise ideal scalar
activity. The obstruction is not a poor choice of \(\lambda\). It is the
single-coordinate uniformity inside the zero and defect sectors.

## 5. Balanced-semiprime kill

Let

\[
N=pq
\]

for distinct odd primes \(3\le p<q\). Put \(h=p+q-2\). These are exactly the nonzero
residues divisible by \(p\) or \(q\), so \(h_N=h\).

The exact zero-product count and the factor-bearing good-state count are

\[
S(N)=(2p-1)(2q-1)<4N,
\qquad
|F_N\cap G_N|=2N-2.
\tag{5.1}
\]

For completeness, \(\varphi(N)=N-p-q+1\), and the good states with neither
coordinate exposing a factor are the \(2\varphi(N)+1\) unit-axis points and
the origin. Subtracting this from \(S(N)\) gives \(2N-2\).

For canonical activity,

\[
Z_{N,1/N}=N+(1-1/N)S(N)<N+S(N)<5N.
\]

Every distinct odd semiprime is greater than six, hence

\[
\widehat\pi_{N,1/N}(F_N)
\ge\frac{2N-2}{Z_{N,1/N}}
>\frac{2N-2}{5N}>\frac13.
\tag{5.2}
\]

Start the chain at the public state

\[
X_0=(1,0,0).
\]

Lemma 4.1 gives the exact hitting obstruction

\[
\boxed{\mathbb E_{X_0}T_F\ge\frac{N}{p+q-2}.}
\tag{5.3}
\]

Let \(\mu_t\) be the law of \(X_t\). For every integer

\[
0\le t\le\left\lfloor\frac{N}{12(p+q-2)}\right\rfloor,
\]

one has \(\mu_t(F_N)\le1/12\). Using (5.2),

\[
\boxed{
d_{\rm TV}(\mu_t,\widehat\pi_{N,1/N})
\ge\widehat\pi_{N,1/N}(F_N)-\mu_t(F_N)
>\frac14.}
\tag{5.4}
\]

If \(q/p\) is bounded by one fixed constant, then, because \(p<q\),

\[
\frac{N}{p+q-2}=\Omega(\sqrt N).
\]

Thus both monitored factor hitting and worst-start mixing take exponentially
many transitions in the input bit length on every such balanced-semiprime
family. Each transition uses at least the coordinate-choice fair bit, so the
same lower bound applies to fair-bit and bit cost.

## 6. Prime-power kill

Let

\[
N=p^a,
\qquad a\ge2,
\]

where \(p\) is prime. Write \(\varphi=\varphi(N)=N-N/p\). Then

\[
h_N=N/p-1,
\qquad
S(N)=N+a\varphi.
\tag{6.1}
\]

The good states with a proper coordinate gcd have cardinality

\[
B_N=S(N)-(2\varphi+1)
=N+(a-2)\varphi-1.
\tag{6.2}
\]

For canonical activity,

\[
Z_{N,1/N}=2N+a\varphi-1-a\varphi/N.
\tag{6.3}
\]

Moreover,

\[
4B_N-Z_{N,1/N}
=2N+(3a-8)\varphi-3+a\varphi/N>0.
\tag{6.4}
\]

For \(a\ge3\), positivity is immediate from \(3a-8\ge1\). For \(a=2\),
the right side reduces to

\[
2p-1-2/p>0.
\]

Therefore

\[
\widehat\pi_{N,1/N}(F_N)
\ge B_N/Z_{N,1/N}>\frac14.
\tag{6.5}
\]

Starting again from \((1,0,0)\), Lemma 4.1 gives

\[
\boxed{
\mathbb E T_F\ge
\frac{p^a}{p^{a-1}-1}>p.}
\tag{6.6}
\]

For every integer

\[
0\le t\le
\left\lfloor\frac{p^a}{8(p^{a-1}-1)}\right\rfloor,
\]

one has \(\mu_t(F_N)\le1/8\), and hence

\[
\boxed{
d_{\rm TV}(\mu_t,\widehat\pi_{N,1/N})>\frac18.}
\tag{6.7}
\]

In particular, for prime squares \(N=p^2\), both bounds are
\(\Omega(p)=\Omega(\sqrt N)\). Prime powers with fixed small \(p\) do not
give an asymptotic lower bound in \(\log N\); prime squares already refute a
uniform polynomial-bit sampler based on this chain. This does not say that
prime powers are hard to factor by other means.

## 7. Why the defect did not help

The residual \(d\) gives a length-two positive-probability path from one unit
axis to the other:

\[
(0,u,0)\longrightarrow(v,u,vu)\longrightarrow(v,0,0)
\]

for units \(u,v\). That repairs the orientation bottleneck visible in an
in-locus heat bath. It does not create a nontrivial CRT stratum. A useful
zero-product pair must contain a proper nonunit coordinate. Until the first
such coordinate appears, the exact Gibbs conditional is uniform within each
relevant residue class, so it can only draw that coordinate at its raw density
\(h_N/N\).

The formally ideal sector-balancing activity

\[
\lambda_*=\frac{S(N)}{N^2-S(N)}
\]

would give equal total good and defect mass, but it does not change this fact.
Lemma 4.2 grants every positive scalar activity and still obtains the same
order of hitting lower bound. On a product of two distinct primes, exact
\(S(N)\) also determines \(p+q\), so \(\lambda_*\) is not a free public quantity; that issue is
secondary to the activity-independent hazard theorem.

A raw scalar Metropolis version is no better. It must first propose the new
coordinate uniformly, so an accepted proper nonunit can occur with probability
at most \(h_N/N\) per transition.

## 8. Exact reopen condition

A materially new retry must change the operation that creates CRT strata. It
must not only change the scalar activity, laziness, scan order, acceptance
probability, or redundant encoding of the single residual.

One sufficient change of framework would be an explicit factor-free **joint
move** which, from \(C_N\), gives inverse-polynomial probability in
\(\log N\) to a state with a proper-nonunit coordinate without first drawing
that coordinate from a uniform residue or uniform complement. Possible forms
that are outside the theorem are:

- a block update of \((k,x)\) from a succinctly sampled solution family;
- a lifted state with two or more defects and a defect-combination or
  cancellation operation;
- a positive-combinatorial path move whose endpoint law amplifies valuation
  strata;
- a charged warm start with a proved factor-free law and inverse-polynomial
  useful mass.

Any such proposal must specify its exact target invariance, fair-bit
implementation, bit lengths, and all-input hitting or mixing proof. Without an
operation of this kind, the rare-nonunit lemma applies pathwise before the first
factor and defeats polynomially many transitions.

## 9. Candidate conclusion

The one-residual public-activity Gibbs sampler is a genuine augmented,
stochastic, noninvertible F23 construction. It is exact and factor-free, and
its zero-defect conditional law is the desired uniform law on \(\Omega_N\).
It nevertheless fails on the first adversarial families. The sharp obstruction
is not an eigenvalue calculation or an automorphism invariant: every successful
path must first create a proper nonunit, while the named transition exposes one
only at raw residue density. Balanced semiprimes and prime squares therefore
force \(\Omega(\sqrt N)\) expected transitions.
