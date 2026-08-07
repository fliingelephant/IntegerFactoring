# Hostile audit of F50 zero-product defect Gibbs sampler

## Disposition

I audited candidate SHA-256
22f3d9ce32525f62c68468da11425fe4c8e1afe8eeeb5b1f9436a690454b4e72.
The core obstruction is correct. The target normalization, Gibbs
conditionals, qualitative Markov-chain properties, fair-bit implementation,
pathwise scalar-activity hazard bound, semiprime and prime-power counts,
stationary factor mass, hitting lower bounds, and total-variation witnesses all
survive re-derivation.

The artifact nevertheless fails literally in two places.

1. Section 5 never orders $p$ and $q$. Therefore its condition that $q/p$ is
   bounded does not imply balance. Take $q=3$ and let $p>3$ range over
   primes. Then $q/p\le 1$, but

   \[
   \frac{N}{p+q-2}=\frac{3p}{p+1}<3,
   \]

   while $\sqrt N=\sqrt{3p}\to\infty$. Thus the premise at lines 446--450
   does not imply its conclusion. The intended theorem is correct after
   assuming $p<q$ or replacing the premise by
   $\max(p/q,q/p)\le C$ for one fixed $C$.
2. Under the standard definition in which a semiprime may be a prime square,
   line 147's identity $p+q=N+1-\varphi(N)$ is false. For
   $N=9=3^2$, the right side is $9+1-6=4$, not $6$. The identity is valid
   for a product of two distinct primes. The candidate itself distinguishes
   “distinct semiprime” from “prime square” elsewhere, so this qualifier must
   be explicit.

Neither defect damages the intended lower bound. Prime squares independently
give an infinite $\Omega(\sqrt N)$ family, and the semiprime proof works under
the symmetric fixed-balance condition. They are still false universal
sentences in the submitted text, so this exact version cannot pass.

## 1. State space, normalizer, and sector mass

The map

\[
(k,x)\longmapsto(k,x,kx)
\]

is a bijection from $R^2$ to $\widehat\Omega_N$. Hence the augmented state
space has $N^2$ states. If $g=\gcd(k,N)$, write $k=gk_0$ and
$N=gN_0$, with $\gcd(k_0,N_0)=1$. Then

\[
kx=0\pmod N
\iff N_0\mid x,
\]

so there are exactly $g$ choices of $x\bmod N$. Therefore

\[
|G_N|=S(N)=\sum_{k\bmod N}\gcd(k,N),
\qquad
|D_N|=N^2-S(N),
\]

and

\[
Z_{N,\lambda}=S(N)+\lambda(N^2-S(N)).
\]

All states in $G_N$ have weight one. Conditioning on $G_N$ is consequently
the uniform law on $\Omega_N$. No normalizer is needed to evaluate a Gibbs
conditional.

At $\lambda=1/N$,

\[
Z_{N,1/N}=N+(1-1/N)S(N),
\qquad
\gamma_N=\frac{S(N)}{N+(1-1/N)S(N)}.
\]

The term $k=0$ contributes $N$ to $S(N)$, and the other $N-1$ terms
contribute at least one each. Thus $S(N)\ge 2N-1$. For every input $N\ge2$,

\[
\gamma_N>
\frac{S(N)}{N+S(N)}
\ge \frac{2N-1}{3N-1}>\frac12.
\]

The public-activity sector bound is exact.

For the residual refinement, every $d$ has at least one representation
$d=1\cdot d$. Giving a state of residual $d$ weight proportional to
$1/M_N(d)$ makes the total weight of each of the $N$ residual fibres equal,
so $G_N$ has mass $1/N$. If $d$ is a unit, $kx=d$ forces both coordinates
to be units; each of the $\varphi(N)$ choices of $k$ determines
$x=dk^{-1}$. Hence $M_N(d)=\varphi(N)$. Only the subsequent unqualified
distinct-prime identity needs correction.

## 2. Gibbs conditional and chain properties

Fix $x$, let $g=\gcd(x,N)$, and let

\[
A_x=\{a:ax=0\pmod N\}
=\{jN/g:0\le j<g\}.
\]

The conditional normalizer for refreshing $k$ is

\[
g+\lambda(N-g).
\]

Thus the zero-sector probability is

\[
\frac{g}{g+\lambda(N-g)}.
\]

For $\lambda=1/N$, this is $Ng/(Ng+N-g)$, and

\[
P(k'=a\mid x)=
\begin{cases}
N/(Ng+N-g),&a\in A_x,\\
1/(Ng+N-g),&a\notin A_x.
\end{cases}
\]

These formulas agree with Sections 2.1--2.3.

Although $d$ is displayed as a coordinate, the move refreshes the block
$(k,d)$ conditional on $x$, with $d$ then determined by $kx$. For
$y=(k,x,kx)$ and $y'=(k',x,k'x)$, a $k$-refresh satisfies

\[
\widehat\pi(y)P(y,y')
=\frac{W(k,x)W(k',x)}
       {2Z\sum_a W(a,x)}
=\widehat\pi(y')P(y',y).
\]

The same calculation holds for an $x$-refresh. Their equal random mixture is
reversible and stationary.

For positive $\lambda$, every conditional point has positive probability.
From any $(k,x,kx)$, first refresh $k$ to a prescribed $k'$, and then refresh
$x$ to a prescribed $x'$. This reaches $(k',x',k'x')$ with positive
probability, including the $1/4$ probability of selecting that scan order.
The chain is irreducible. Retaining the current coordinate has positive
probability, so every state has a self-loop and the chain is aperiodic. The
update is stochastic and does not define an invertible point map.

## 3. Exact fair-bit and bit cost

The implementation uses only public arithmetic.

- Euclid computes $g=\gcd(x,N)$. If $1<g<N$, this is already a verified
  factor; it is not a hidden input to the transition.
- To sample an $A/B$ coin, choose
  $m=\lceil\log_2 B\rceil$ fair bits, reject the resulting integer when it is
  at least $B$, and otherwise test whether it is below $A$. The acceptance
  probability is greater than $1/2$ unless no rejection is needed, so the
  expected number of rounds is less than two. Here
  $B=Ng+N-g\le N^2$.
- A uniform point of $A_x$ is $jN/g$ for uniform $0\le j<g$.
- If $g<N$, divisibility $g\mid N$ gives $g\le N/2$. Uniform rejection from
  $R\setminus A_x$ therefore accepts with probability at least $1/2$. When
  $g=N$, that sector has conditional probability zero.

All rejection loops have geometric tails and terminate almost surely. Each
transition uses $O(\log N)$ expected fair bits. Gcd, multiplication, division,
comparison, and reduction act on $O(\log N)$-bit integers, so schoolbook
algorithms give one fixed polynomial expected bit bound. The claimed upper
cost and the one scan-choice bit per transition are valid for the specified
implementation.

## 4. Factor mass and the conditional factoring implication

A zero-product state with neither coordinate exposing a proper gcd must have
one of the forms

\[
(u,0),\quad(0,u),\quad(0,0),
\qquad u\in R^\times.
\]

Thus, for every composite $N$,

\[
|F_N\cap G_N|=S(N)-2\varphi(N)-1.
\]

The one-third bound imported from P43 can also be derived directly. Both $S$
and $\varphi$ are multiplicative, and

\[
S(p^a)=p^{a-1}((a+1)p-a),
\qquad
\frac{S(p^a)}{\varphi(p^a)}
=a+1+\frac1{p-1}.
\]

If an odd composite is $p^a$ with $a\ge2$, then

\[
S(p^a)-3\varphi(p^a)
=p^{a-1}\bigl((a-2)(p-1)+1\bigr)\ge3.
\]

If it has at least two distinct prime factors, at least two factors in the
displayed product ratio exceed two, so $S(N)>4\varphi(N)$, with ample
integral slack. In either case $S(N)\ge3\varphi(N)+2$. Hence

\[
3|F_N\cap G_N|-S(N)
=2S(N)-6\varphi(N)-3>0,
\]

and the useful conditional mass is greater than $1/3$. Since
$\gamma_N>1/2$,

\[
\widehat\pi_{N,1/N}(F_N\cap G_N)>1/6.
\]

If an efficiently generated terminal law is within TV $1/24$ of the target,
its factor probability is greater than $1/8$. Under the uniform almost-sure
and expected-polynomial cost assumptions of P43, independent retries,
deterministic primality testing, direct removal of factors of two, exact
division, and a factor tree with $O(\log N)$ nodes give the claimed all-input
Las Vegas reduction. The TV assertion alone would not supply a runtime
theorem, but the candidate explicitly invokes P43's full conditional
reduction.

## 5. Pathwise hazard for every positive scalar activity

The residue set splits disjointly into zero, $\varphi(N)$ units, and

\[
h_N=N-\varphi(N)-1
\]

proper nonunits. For composite $N$, $h_N>0$. Before the first visit to $F_N$,
each coordinate is zero or a unit.

If the held coordinate is zero, every refreshed value has zero defect and
weight one. The refresh is uniform on $R$, so its factor hazard is exactly
$h_N/N$, independently of $\lambda$.

If the held coordinate is a unit, its annihilator is $\{0\}$. At canonical
activity, zero has conditional weight $1$, while every nonzero residue has
weight $1/N$. Each nonzero point has probability $1/(2N-1)$, and the factor
hazard is

\[
\frac{h_N}{2N-1}<\frac{h_N}{N}.
\]

Thus, after every survival history, the canonical hazard is at most
$\alpha=h_N/N$. Iterated conditioning gives

\[
\Pr(T_F>t)\ge(1-\alpha)^t,
\qquad
\Pr(T_F\le t)\le t\alpha,
\]

and tail summation gives

\[
\mathbb E T_F\ge\sum_{t\ge0}(1-\alpha)^t
=\frac{N}{h_N}.
\]

For an arbitrary positive scalar activity, the unit-held hazard is exactly

\[
\frac{h_N\lambda}{1+(N-1)\lambda}
<\frac{h_N}{N-1},
\]

while the zero-held hazard $h_N/N$ is also below $h_N/(N-1)$. The same
history-by-history argument yields

\[
\mathbb E T_F\ge\frac{N-1}{h_N}.
\]

This proof is pathwise and uses no independence assumption. The hazard
inequality even survives if a positive scalar is selected adaptively at each
update, although a changing activity does not in general retain one fixed
stationary target. The candidate's fixed, possibly factor-dependent, scalar
statement is safe.

## 6. Distinct semiprimes

For $N=pq$ with distinct primes,

\[
S(N)=S(p)S(q)=(2p-1)(2q-1),
\qquad
h_N=(q-1)+(p-1)=p+q-2.
\]

The nonzero multiples of $p$ and the nonzero multiples of $q$ are disjoint.
The no-factor zero-product states number $2\varphi(N)+1$. Consequently

\[
|F_N\cap G_N|
=(2p-1)(2q-1)-2(p-1)(q-1)-1
=2N-2.
\]

For canonical activity,

\[
Z_{N,1/N}=N+(1-1/N)S(N)<N+S(N)<5N.
\]

A distinct odd semiprime has $N\ge15$, so

\[
\widehat\pi(F_N)
\ge\frac{2N-2}{Z_{N,1/N}}
>\frac{2N-2}{5N}>\frac13.
\]

The public start $(1,0,0)$ is outside $F_N$. The pathwise lemma proves

\[
\mathbb E T_F\ge\frac{N}{p+q-2}.
\]

For every integer $t\le\lfloor N/(12(p+q-2))\rfloor$,

\[
\mu_t(F_N)
\le\Pr(T_F\le t)
\le\frac{t(p+q-2)}N
\le\frac1{12}.
\]

Testing the event $F_N$ in total variation gives

\[
d_{\rm TV}(\mu_t,\widehat\pi)
\ge\widehat\pi(F_N)-\mu_t(F_N)>\frac14.
\]

These calculations are correct. Only the one-sided ratio condition used to
turn them into $\Omega(\sqrt N)$ fails. Under the corrected symmetric balance
assumption $p\le q\le Cp$,

\[
\frac{N}{p+q-2}>
\frac{pq}{p+q}
=\sqrt N\frac{\sqrt{q/p}}{1+q/p}
\ge\sqrt N\frac{\sqrt C}{1+C}.
\]

The last constant is valid for $1\le q/p\le C$. Hence the intended hitting
and mixing lower bounds are $\Omega(\sqrt N)$, exponential in the binary input
length. Because the named random scan consumes one fair coordinate-choice bit
per transition, the fair-bit and bit-cost lower bounds follow.

## 7. Prime powers

Let $N=p^a$, $a\ge2$, and $\varphi=N-N/p$. Splitting residues by their
$p$-adic valuation gives $a$ nonzero valuation strata, each contributing
$\varphi$ to the gcd sum, while zero contributes $N$. Therefore

\[
h_N=N/p-1,
\qquad
S(N)=N+a\varphi.
\]

Removing the $2\varphi+1$ no-factor zero-product states gives

\[
B_N=|F_N\cap G_N|=N+(a-2)\varphi-1.
\]

The canonical normalizer is

\[
Z_{N,1/N}=2N+a\varphi-1-a\varphi/N.
\]

Direct subtraction yields

\[
4B_N-Z_{N,1/N}
=2N+(3a-8)\varphi-3+a\varphi/N.
\]

For $a\ge3$, $3a-8\ge1$, so this is positive. For $a=2$, it equals

\[
2p-1-2/p>0
\]

for every prime $p$, including $p=2$. Thus

\[
\widehat\pi(F_N)\ge B_N/Z_{N,1/N}>1/4.
\]

The pathwise bound and the same TV event give

\[
\mathbb E T_F\ge
\frac{p^a}{p^{a-1}-1}>p
\]

and, whenever $t\le\lfloor p^a/(8(p^{a-1}-1))\rfloor$,

\[
\mu_t(F_N)\le1/8,
\qquad
d_{\rm TV}(\mu_t,\widehat\pi)>1/8.
\]

For $a=2$, both time scales are
$\Omega(p)=\Omega(\sqrt N)$. For fixed $p$ and growing $a$, this bound is
only constant order, exactly as the candidate says. The case $p=2$ causes no
algebraic exception.

## 8. Scope and explanatory claims

The activity-independent theorem covers exactly a two-level target: one common
weight on $d=0$, one positive scalar weight on every $d\ne0$, and a
one-coordinate exact heat-bath refresh. It also covers arbitrary scan order
for the hitting argument, because either held coordinate is zero or a unit
before the hit. A coordinate-wise Metropolis kernel that first proposes a
uniform residue has the same proposal-hazard upper bound $h_N/N$, regardless
of its acceptance rule.

It does not cover a computable nonconstant residual weight $w(d)$, a
nonuniform coordinate proposal, a block move, several interacting defects, an
auxiliary or lifted chain, a warm start already carrying useful mass, or a
direct sampler. Section 1 correctly leaves nonconstant weights open. The final
classification must retain that exclusion.

The arrows

\[
(0,u,0)\to(v,u,vu)\to(v,0,0)
\]

prove a length-two positive-probability path between the unit axes. They do not
prove constant expected time to a prescribed $v$, whose point probability is
small. The phrase “in constant time” is harmless only if it means path length.
The exact wording is “by a two-transition positive-probability path.” No
quantitative lower bound relies on this sentence.

The ideal scalar

\[
\lambda_*=\frac{S(N)}{N^2-S(N)}
\]

does balance total good and defect weight. For distinct $N=pq$,

\[
p+q=\frac{4N+1-S(N)}2,
\]

so exact access to this normalizer is factor-revealing. For a prime square,
perfect-square detection already supplies the repeated prime. This is another
reason not to use the bare word “semiprime” for the distinct-prime formula.

The result remains only a method failure for the exact cold-start,
scalar-activity Gibbs construction. It is not a factoring algorithm, a lower
bound for general augmented sampling, or evidence against nonconstant,
nonlocal, lifted, positive-combinatorial, or warm-start routes.

## Smallest exact correction

The mathematical core needs no change. Make these literal edits:

1. In Section 1, replace “On a semiprime” before
   $p+q=N+1-\varphi(N)$ by “On a product of two distinct primes.”
2. In Section 5, either add $p<q$ when $N=pq$ is introduced, or replace
   “$q/p$ is bounded by one fixed constant” by
   “$\max(p/q,q/p)$ is bounded by one fixed constant.”
3. For unambiguous explanatory prose, replace “cross ... in constant time”
   by “has a length-two positive-probability path across.” This third edit
   does not alter a theorem.

After the first two corrections, every substantive obstruction claimed by the
candidate is proved above. Because the Section 5 quantifier is mathematically
false in the submitted version, this exact artifact must not advance
unchanged.

FAIL AS WRITTEN
