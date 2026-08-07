# Fresh hostile whole-proof re-audit of F50

## Disposition

I audited
`experiments/F50_zero_product_defect_gibbs_kill/RESULT.md` at SHA-256

```text
bec5fbfb0de76677d78aa36187485b06848be9891a033fd1a1f91cf4ddfd88b1
```

The hash matches the requested artifact. I reconstructed the target, kernel,
implementation, factor-mass estimates, pathwise hitting theorem, both
adversarial families, total-variation witnesses, and scope boundary. I also
checked the promoted P43--P45 statements, the X37 closure record, and the
preserved first hostile audit.

The two mathematical defects found by the first audit are corrected. Section
1 now restricts the totient identity to a product of two distinct primes.
Section 5 now assumes $3\le p<q$, so a fixed upper bound on $q/p$ is a
genuine balance condition. The explanatory crossing claim is also stated only
as a length-two positive-probability path. I found no new false claim or
missing case within the artifact's stated scope.

This is an exact obstruction for the named scalar two-sector,
one-base-coordinate Gibbs construction and its coordinate-gcd extraction
rule. It is not an integer-factoring theorem and not a lower bound for the
explicitly excluded sampler classes.

## 1. Relation to P43, P44, P45, and X37

P43/X37 concerns the uniform law on

\[
\Omega_N=\{(k,x):kx=0\pmod N\}
\]

and the heat bath which always stays on that locus. F50 instead uses the graph
of multiplication on all of $R^2$, gives the complement of $\Omega_N$
positive weight, and can move between the two unit axes through a nonzero
residual. P43's cold in-locus lower bound therefore neither proves nor rules
out F50.

P44 applies to deterministic automorphisms of the coordinate algebra of
$KX=0$. P45 applies to polynomial-induced finite-set bijections
$\Omega_N\to\Omega_N$ under an explicit degree bound. An F50 update is a
stochastic, noninvertible heat-bath block update and usually leaves
$\Omega_N$. It is outside both the hypotheses and conclusions of P44 and
P45. The fact that $d=kx$ is redundant does not change this: the underlying
pair ranges over all of $R^2$, not only over the zero-product locus.

Thus F50 is a legitimate materially new test under X37's reopen boundary. Its
own negative conclusion is narrower than the open classes preserved by
P43--P45.

## 2. State count, target, and conditional zero-defect law

Let $R=\mathbb Z/N\mathbb Z$. The map

\[
(k,x)\longmapsto(k,x,kx)
\]

is a bijection from $R^2$ to $\widehat\Omega_N$, so the augmented state
space has $N^2$ states.

Fix $k$, and put $g=\gcd(k,N)$, $k=gk_0$, and $N=gN_0$. Since
$\gcd(k_0,N_0)=1$,

\[
kx=0\pmod N\quad\Longleftrightarrow\quad N_0\mid x.
\]

There are exactly $g$ such residues $x\bmod N$. Hence

\[
|G_N|=S(N):=\sum_{k\bmod N}\gcd(k,N),
\qquad |D_N|=N^2-S(N).
\]

Giving every good state weight $1$ and every defect state weight
$\lambda>0$ therefore gives

\[
Z_{N,\lambda}=S(N)+\lambda\bigl(N^2-S(N)\bigr).
\]

Every state in $G_N$ has the same weight. The target conditioned on
$d=0$ is consequently exactly uniform on $\Omega_N$, with no need to
compute $S(N)$ or $Z_{N,\lambda}$.

At $\lambda=1/N$,

\[
Z_{N,1/N}=N+(1-1/N)S(N),
\qquad
\gamma_N=\frac{S(N)}{N+(1-1/N)S(N)}.
\]

The $k=0$ summand in $S(N)$ is $N$; the other $N-1$ summands are at
least one. Thus $S(N)\ge2N-1$, and, for $N\ge2$,

\[
\gamma_N>
\frac{S(N)}{N+S(N)}
\ge\frac{2N-1}{3N-1}>\frac12.
\]

This verifies the claimed good-sector mass.

For the residual-fibre observation, every $d$ has a representation
$d=1\cdot d$, so $M_N(d)>0$. Per-state weight proportional to
$1/M_N(d)$ gives each of the $N$ residual fibres equal total weight and
therefore gives $G_N$ mass exactly $1/N$. If $d$ is a unit and
$kx=d$, both $k$ and $x$ are units. Every one of the
$\varphi(N)$ choices of $k$ determines the unique
$x=dk^{-1}$, so $M_N(d)=\varphi(N)$. For $N=pq$ with distinct
primes,

\[
\varphi(N)=(p-1)(q-1)=N-p-q+1,
\]

and hence $p+q=N+1-\varphi(N)$; the quadratic
$T^2-(p+q)T+N$ recovers the two primes. This is exactly the
distinct-prime qualification missing from the first version. It does not
assert the false identity for prime squares.

## 3. Exact Gibbs conditional and Markov-chain properties

Fix $x$, let $g=\gcd(x,N)$, and define

\[
A_x=\{a\in R:ax=0\}
=\{jN/g:0\le j<g\}.
\]

There are $g$ points of weight $1$ and $N-g$ points of weight
$\lambda$. Thus the exact conditional normalizer is

\[
g+\lambda(N-g),
\]

and the probability of selecting the zero-defect sector is

\[
\frac{g}{g+\lambda(N-g)}.
\]

For $\lambda=1/N$, multiplication by $N$ gives

\[
\Pr(A_x\mid x)=\frac{Ng}{Ng+N-g},
\]

and the point probabilities are

\[
\Pr(k'=a\mid x)=
\begin{cases}
N/(Ng+N-g),&a\in A_x,\\
1/(Ng+N-g),&a\notin A_x.
\end{cases}
\]

The $x$-refresh is symmetric. Because $d$ is determined by the two base
coordinates, this is formally a $(k,d)$-block refresh conditional on $x$,
or an $(x,d)$-block refresh conditional on $k$. Calling it a
one-coordinate refresh refers to the independent $R^2$ representation and
does not invalidate the Gibbs calculation.

For states $y=(k,x,kx)$ and $y'=(k',x,k'x)$, a $k$-refresh satisfies

\[
\widehat\pi(y)P(y,y')
=\frac{W(k,x)W(k',x)}
{2Z\sum_{a\in R}W(a,x)}
=\widehat\pi(y')P(y',y).
\]

The same identity holds for an $x$-refresh. Their random-scan mixture is
reversible and stationary.

For every positive $\lambda$, every conditional point probability is
positive. From any state, a $k$-refresh can choose any prescribed $k'$,
after which an $x$-refresh can choose any prescribed $x'$. Hence two
updates in that scan order reach any target state with positive probability.
The chain is irreducible. Retaining the refreshed coordinate's current value
also has positive probability, so every state has a self-loop and the chain
is aperiodic. The refresh discards the old coordinate and is stochastic; it
is not an invertible point map.

## 4. Exact fair-bit implementation and bit cost

The canonical conditional uses only public arithmetic.

First compute $g=\gcd(x,N)$. If $1<g<N$, this computation has already
returned a verified factor; continuing the transition does not treat that
factor as hidden advice.

For an exact $A/B$ coin, take
$m=\lceil\log_2 B\rceil$ fair bits, reject the resulting integer if it is
at least $B$, and otherwise compare it with $A$. Since
$2^m<2B$ unless acceptance is already certain, the expected number of
rounds is less than two. Here

\[
B=Ng+N-g\le N^2,
\]

so a round uses $O(\log N)$ bits.

Conditional on $A_x$, exact uniform sampling of
$j\in\{0,\ldots,g-1\}$ and output of $jN/g$ gives the desired law.
Conditional on the complement, sample uniformly in $R$ and reject members
of $A_x$. If $g<N$, then $g\mid N$ implies $g\le N/2$, so this
rejection accepts with probability at least $1/2$. If $g=N$, the
complement sector has probability zero. All rejection loops have geometric
tails and terminate almost surely.

Euclid, multiplication, division, reduction, comparison, and membership in
$A_x$ all act on integers of $O(\log N)$ bits; even $Ng$ has only
$O(\log N)$ bits in asymptotic notation. Schoolbook arithmetic therefore
gives a fixed polynomial expected bit bound per transition. The expected
fair-bit count is $O(\log N)$, including the random-scan choice. There is
no precision approximation and no factoring, order-finding, or sampling
oracle.

## 5. Stationary factor mass and the conditional factoring reduction

Let

\[
F_N=\{(k,x,d):1<\gcd(k,N)<N
\text{ or }1<\gcd(x,N)<N\}.
\]

Inside $G_N$, a state outside $F_N$ must have each coordinate either zero
or a unit. A unit coordinate forces the other coordinate to be zero. Hence
the no-factor good states are exactly

\[
(u,0),\quad(0,u),\quad(0,0),
\qquad u\in R^\times,
\]

and

\[
|F_N\cap G_N|=S(N)-2\varphi(N)-1.
\tag{5.1}
\]

The P43 one-third statement can be recovered directly. The gcd sum is
multiplicative, and

\[
S(p^a)=p^{a-1}((a+1)p-a)=p^a+a\varphi(p^a),
\]

so

\[
\frac{S(p^a)}{\varphi(p^a)}
=a+1+\frac1{p-1}.
\]

Consequently, multiplicativity gives

\[
\frac{S(N)}{\varphi(N)}
=\prod_{p^a\mathbin\Vert N}
\left(a+1+\frac1{p-1}\right).
\]

If an odd composite is $p^a$, $a\ge2$, then

\[
S(p^a)-3\varphi(p^a)
=p^{a-1}\bigl((a-2)(p-1)+1\bigr)\ge3.
\]

Using (5.1),

\[
3|F_N\cap G_N|-S(N)
=2(S(N)-3\varphi(N))-3>0.
\]

If $N$ has at least two distinct odd prime factors, at least two factors in
the displayed product for $S(N)/\varphi(N)$ are strictly greater than two.
Thus $S(N)>4\varphi(N)$; also $\varphi(N)\ge8$. The same expression
$2S-6\varphi-3$ is again positive. Therefore every odd composite has

\[
\frac{|F_N\cap G_N|}{S(N)}>\frac13.
\]

Combining this with $\gamma_N>1/2$ gives

\[
\widehat\pi_{N,1/N}(F_N\cap G_N)>\frac16.
\]

If a terminal law $\nu$ is within TV distance $1/24$ of the augmented
target, the event inequality for total variation gives

\[
\nu(F_N)\ge\nu(F_N\cap G_N)
>\frac16-\frac1{24}=\frac18.
\]

Every accepted gcd is checked by exact division. Under the conditional
hypothesis of one fixed expected-polynomial, almost-surely terminating
sampler, independent fresh calls therefore take at most eight calls in
expectation. Deterministic primality testing, direct removal of factors of
two, exact division, and recursive splitting use only $O(\log N)$ factor
tree nodes. Fresh-call cost is independent of the event that the call is
reached, so correlation between a call's own runtime and success causes no
gap in the stopped-cost calculation. This proves the conditional all-input
Las Vegas reduction invoked from P43. F50 does not claim that its slow chain
satisfies the sampler hypothesis.

## 6. Pathwise hazard, including every positive scalar activity

The residues split into zero, units, and proper nonunits. Put

\[
H_N=\{a:1<\gcd(a,N)<N\},
\qquad
h_N=|H_N|=N-\varphi(N)-1.
\]

For composite $N$, $h_N>0$. Before the first visit to $F_N$, both
coordinates are in $U_N\cup\{0\}$. This remains true after every survival
history; no independence assumption is needed.

If the held coordinate is zero, every candidate refreshed value has zero
defect and weight one. The refresh is uniform on $R$, and its factor hazard
is exactly $h_N/N$.

If the held coordinate is a unit, its annihilator is $\{0\}$. At canonical
activity, zero has conditional weight one and every nonzero value has weight
$1/N$. The $h_N$ proper nonunits therefore have total probability

\[
\frac{h_N}{2N-1}<\frac{h_N}{N}.
\]

Consequently, conditional on every complete survival history, the next-step
hazard is at most
$\alpha_N=h_N/N$. If
$T_F=\inf\{t\ge1:X_t\in F_N\}$, induction on conditional survival gives

\[
\Pr(T_F>t)\ge(1-\alpha_N)^t.
\]

It also gives

\[
\Pr(T_F\le t)\le t\alpha_N,
\]

either by summing the conditional hazards or by
$1-(1-\alpha_N)^t\le t\alpha_N$. Tail summation yields

\[
\mathbb E T_F
=\sum_{t\ge0}\Pr(T_F>t)
\ge\frac1{\alpha_N}
=\frac{N}{h_N}.
\]

For arbitrary $\lambda>0$, the zero-held hazard remains $h_N/N$, while
the unit-held hazard is exactly

\[
\frac{h_N\lambda}{1+(N-1)\lambda}
<\frac{h_N}{N-1}.
\]

Thus every positive fixed scalar activity, even one granted with
factor-dependent information, satisfies

\[
\mathbb E T_F\ge\frac{N-1}{h_N}.
\]

The argument is history-by-history. Random scan, deterministic scan,
adaptive scan selection, or extra laziness cannot increase the per-refresh
hazard above these bounds. This verifies the claimed all-positive-scalar
pathwise obstruction.

## 7. Balanced distinct semiprimes

Let $N=pq$ with distinct odd primes $3\le p<q$. The nonzero multiples of
$p$ number $q-1$, the nonzero multiples of $q$ number $p-1$, and the
two sets are disjoint. Hence

\[
h_N=p+q-2.
\]

Multiplicativity of $S$ and $S(r)=2r-1$ for a prime $r$ give

\[
S(N)=(2p-1)(2q-1)<4N.
\]

Using (5.1) and
$\varphi(N)=(p-1)(q-1)$,

\[
|F_N\cap G_N|
=(2p-1)(2q-1)-2(p-1)(q-1)-1
=2N-2.
\]

At canonical activity,

\[
Z_{N,1/N}=N+(1-1/N)S(N)<N+S(N)<5N.
\]

A distinct odd semiprime has $N\ge15$, so

\[
\widehat\pi_{N,1/N}(F_N)
\ge\frac{2N-2}{Z_{N,1/N}}
>\frac{2N-2}{5N}>\frac13.
\]

The public start $X_0=(1,0,0)$ is outside $F_N$. The pathwise theorem
therefore gives

\[
\mathbb E_{X_0}T_F\ge\frac{N}{p+q-2}.
\]

For every integer

\[
0\le t\le\left\lfloor\frac{N}{12(p+q-2)}\right\rfloor,
\]

the hitting bound gives $\mu_t(F_N)\le1/12$. Testing the event $F_N$ in
the definition of total variation gives

\[
d_{\mathrm{TV}}(\mu_t,\widehat\pi_{N,1/N})
\ge\widehat\pi_{N,1/N}(F_N)-\mu_t(F_N)>\frac14.
\]

Now suppose $q/p\le C$ for one fixed constant $C$. Since the corrected
hypothesis includes $p<q$, $r=q/p,\ 1<r\le C$, and

\[
\frac{N}{p+q-2}
>\frac{pq}{p+q}
=\sqrt N\frac{\sqrt r}{1+r}
\ge\sqrt N\frac{\sqrt C}{1+C}.
\]

Thus any infinite fixed-balance family has an
$\Omega(\sqrt N)$ hitting lower bound and an
$\Omega(\sqrt N)$ worst-start TV mixing lower bound. Since
$\sqrt N$ is exponential in the binary input length, neither is
polynomial in $\log N$. The specified random scan consumes one fair
coordinate-choice bit per transition, so the transition lower bound also
lower-bounds its fair-bit and bit cost. The ordering correction removes the
one-sided-ratio counterexample from the first audit.

## 8. Prime powers, including $p=2$

Let $N=p^a$, $a\ge2$, and
$\varphi=\varphi(N)=N-N/p$. There are $N/p-1$ nonzero nonunits, so

\[
h_N=N/p-1.
\]

The zero residue contributes $N$ to $S(N)$. For each of the $a$
possible nonzero $p$-adic valuation strata, the number of residues times
their gcd contribution is $\varphi(N)$. Therefore

\[
S(N)=N+a\varphi.
\]

Removing the $2\varphi+1$ unit-axis/origin states gives

\[
B_N:=|F_N\cap G_N|=N+(a-2)\varphi-1.
\]

The canonical normalizer is

\[
Z_{N,1/N}
=S(N)+\frac{N^2-S(N)}N
=2N+a\varphi-1-a\varphi/N.
\]

Direct subtraction gives

\[
4B_N-Z_{N,1/N}
=2N+(3a-8)\varphi-3+a\varphi/N.
\]

For $a\ge3$, one has $N\ge8$, $3a-8\ge1$, and
$2N-3+a\varphi/N>0$, so the full expression is positive. For
$a=2$, substitution of $N=p^2$ and
$\varphi=p^2-p$ reduces the expression to

\[
2p-1-2/p.
\]

This is positive for every prime, and at $p=2$ it equals $2$. Hence no
odd-characteristic assumption is hidden here, and

\[
\widehat\pi_{N,1/N}(F_N)
\ge\frac{B_N}{Z_{N,1/N}}>\frac14
\]

for every prime power $p^a$, including powers of two.

From $X_0=(1,0,0)$,

\[
\mathbb E T_F
\ge\frac{p^a}{p^{a-1}-1}>p.
\]

For every integer

\[
0\le t\le
\left\lfloor\frac{p^a}{8(p^{a-1}-1)}\right\rfloor,
\]

one has $\mu_t(F_N)\le1/8$, and therefore

\[
d_{\mathrm{TV}}(\mu_t,\widehat\pi_{N,1/N})>\frac18.
\]

For $a=2$, the expectation exceeds $p=\sqrt N$, and the TV witness lasts
for $\Omega(p)$ transitions. Varying $p$ through the primes supplies the
prime-square obstruction. If $p$ is fixed and $a\to\infty$, this
particular lower bound is only constant order; the artifact states that
limitation explicitly. It makes no claim that prime powers are hard to
factor by other methods.

## 9. Explanatory claims and exact reopen scope

For units $u,v$,

\[
(0,u,0)\longrightarrow(v,u,vu)\longrightarrow(v,0,0)
\]

is a valid two-transition path of positive probability. Its middle state has
nonzero defect, so F50 genuinely crosses the unit-axis orientation barrier
which the P43 heat bath cannot cross inside $\Omega_N$. The statement is
about path length and positive probability, not constant expected time to a
prescribed $v$.

The scalar which balances the total weights of the two sectors is

\[
\lambda_*=\frac{S(N)}{N^2-S(N)}.
\]

For a distinct semiprime,

\[
S(N)=4N-2(p+q)+1,
\qquad
p+q=\frac{4N+1-S(N)}2,
\]

so exact access to $S(N)$, and hence exact access to this calibration,
reveals the factor sum. The scalar-activity hazard theorem is stronger: it
grants any positive scalar anyway and still proves the lower bound.

A scalar Metropolis update which first proposes the refreshed residue
uniformly cannot accept a proper nonunit unless it first proposes one. Before
the first hit, that event has probability $h_N/N$ per proposal, regardless
of the acceptance rule. This supports exactly the Metropolis sentence in the
artifact.

The proved boundary is the following: one common good-state weight, one
positive common defect-state weight, and an exact one-base-coordinate
conditional refresh. The same hazard reasoning survives scan-order changes
and laziness, and uniform-proposal Metropolis cannot improve the proposal
hazard. It does not cover a nonconstant residual weight $w(d)$, a nonuniform
arithmetic proposal, a block update, several interacting defects, an
auxiliary/lifted chain, a joint arithmetic decoder which forms new
factor-bearing combinations from a transcript, a charged warm start with
useful mass, or a direct sampler. Such a decoder or proposal changes the
operation which creates or detects a CRT stratum; it is not refuted by the
coordinate event $F_N$.

Section 1 expressly leaves computable nonconstant residual weights open.
Sections 7--8 expressly leave block moves, multiple defects, nonlocal
arithmetic proposals, positive-combinatorial paths, and useful warm starts
open. The final conclusion is tied to the named transition and to the
factor-bearing set defined in Section 3. Read with those explicit
qualifications, the reopen condition is narrow and matches what the proof
actually establishes.

## Verdict

The target and conditional law are exact. The Gibbs sampler is reversible,
irreducible, aperiodic, and exactly implementable with the claimed expected
fair-bit and bit cost. The stationary factor masses, history-conditioned
hazard inequalities, semiprime and prime-power counts, $p=2$ edge case,
hitting lower bounds, and TV witnesses all check. The two prior literal
errors are repaired, and the exclusions prevent the obstruction from being
read as a theorem about broader augmented or nonlocal samplers.

PASS AS WRITTEN
