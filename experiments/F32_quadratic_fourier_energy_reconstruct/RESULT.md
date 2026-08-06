# Proof-blind reconstruction: quadratic Fourier energy

## Verdict

**RECONSTRUCTED.** All of the bare mathematical claims are valid with the precise qualifications below. In particular, “proper gcd” must mean the factor-revealing event

\[
\mathcal U_N=\{k\bmod N:1<\gcd(k,N)<N\},
\]

and the sampler-to-factoring theorem needs total-variation error strictly smaller than \(2/7\). The convenient fixed choice \(\delta=1/14\) gives a per-call split probability at least \(3/14\).

This was reconstructed symbolically, with no computation. I did not open or read `REGISTRY.md`, `notes/Progress.md`, or any path whose basename begins `F32_`. In particular, the destination directory and result file were not inspected before this write. Only the explicitly permitted general-context files were consulted.

## 1. Exact quadratic Fourier energy

Let \(N\) be odd, put \(e_N(t)=\exp(2\pi i t/N)\), and define

\[
G_N(k)=\sum_{x\bmod N}e_N(kx^2).
\]

Then, for every residue \(k\bmod N\), including \(k=0\),

\[
\boxed{|G_N(k)|^2=N\gcd(k,N)},
\]

where \(\gcd(0,N)=N\).

Indeed,

\[
|G_N(k)|^2
=\sum_{x,y\bmod N}e_N\bigl(k(x^2-y^2)\bigr).
\]

Because \(2\) is invertible modulo odd \(N\), the map

\[
(x,y)\longmapsto (u,v)=(x-y,x+y)
\]

is a bijection of \((\mathbb Z/N\mathbb Z)^2\). Hence

\[
|G_N(k)|^2
=\sum_{u\bmod N}\sum_{v\bmod N}e_N(kuv)
=N\#\{u\bmod N:ku\equiv0\pmod N\}.
\]

The kernel of multiplication by \(k\) on \(\mathbb Z/N\mathbb Z\) has size \(\gcd(k,N)\). For \(k=0\), this gives \(|G_N(0)|^2=N^2\), as required. Oddness is essential to this proof and to the displayed formula; even inputs must not be silently included.

Define

\[
S(N)=\sum_{k\bmod N}\gcd(k,N).
\]

The normalized nonnegative Fourier-energy law is therefore

\[
\boxed{\pi_N(k)=\frac{|G_N(k)|^2}{\sum_j|G_N(j)|^2}
=\frac{\gcd(k,N)}{S(N)}}.
\]

The atom at zero is substantial: \(\pi_N(0)=N/S(N)\). Dropping it changes both the law and the later sampler analysis.

## 2. The normalizer \(S(N)\)

There are \(\varphi(N/d)\) residues with gcd exactly \(d\), including the case \(d=N\), for which \(\varphi(1)=1\). Thus

\[
\boxed{S(N)=\sum_{d\mid N}d\,\varphi(N/d)
=N\sum_{e\mid N}\frac{\varphi(e)}e}.
\]

Equivalently, \(S=\operatorname{id}*\varphi\). It is multiplicative. This also follows directly from CRT: for \((a,b)=1\),

\[
\gcd(k,ab)=\gcd(k\bmod a,a)\gcd(k\bmod b,b),
\]

so the sum factors and \(S(ab)=S(a)S(b)\).

For a prime power,

\[
\boxed{S(p^a)=p^{a-1}\bigl((a+1)p-a\bigr)
=p^a\left(1+a\left(1-\frac1p\right)\right)}.
\]

One transparent count is that, for every \(0\le j<a\), the total weight of residues with gcd \(p^j\) is

\[
p^j\varphi(p^{a-j})=p^{a-1}(p-1),
\]

while the sole residue with gcd \(p^a\) contributes \(p^a\).

Consequently, if \(N=\prod_i p_i^{a_i}\), and

\[
r_i=1-\frac1{p_i},\qquad
T=\frac{S(N)}N=\prod_i(1+a_i r_i),\qquad
R=\frac{\varphi(N)}N=\prod_i r_i,
\]

then \(S(N)=NT\) and \(\varphi(N)=NR\).

## 3. Universal factor-revealing mass

The only non-factor-revealing gcd values are \(1\) and \(N\). Their total \(\pi_N\)-weight is respectively \(\varphi(N)/S(N)\) and \(N/S(N)\). Therefore

\[
\boxed{\pi_N(\mathcal U_N)
=\frac{S(N)-\varphi(N)-N}{S(N)}
=1-\frac{1+R}{T}}.
\]

For every odd composite \(N\),

\[
\boxed{\pi_N(\mathcal U_N)\ge\frac27},
\]

with equality if and only if \(N=9\).

Proof of sharpness and equality cases:

1. If \(N=p^a\), then \(a\ge2\), \(r=1-1/p\ge2/3\), and

   \[
   \frac{N+\varphi(N)}{S(N)}=\frac{1+r}{1+ar}
   \le \frac{1+r}{1+2r}\le\frac57.
   \]

   The first equality requires \(a=2\), and the second requires \(r=2/3\), hence \(p=3\). Thus equality occurs exactly at \(N=3^2\). Equivalently, for every odd prime power,

   \[
   \pi_{p^a}(\mathcal U_{p^a})
   =\frac{(a-1)(p-1)}{(a+1)p-a}.
   \]

2. Suppose \(N\) has at least two distinct prime divisors. Increasing any exponent only increases \(T\), so it is enough to bound

   \[
   F_m(r_1,\ldots,r_m)
   =\frac{1+\prod_i r_i}{\prod_i(1+r_i)}.
   \]

   Adding a further positive \(r\) strictly decreases this expression, since

   \[
   \frac{1+Rr}{(1+R)(1+r)}<1.
   \]

   For two variables, \((1+rs)/((1+r)(1+s))\) decreases in each of \(r,s<1\). Distinct odd primes have smallest values \(2/3\) and \(4/5\), so

   \[
   \frac{N+\varphi(N)}{S(N)}\le\frac{23}{45},
   \qquad
   \pi_N(\mathcal U_N)\ge\frac{22}{45},
   \]

   with equality in this subcase exactly at \(N=3\cdot5=15\). This is already strictly stronger than \(2/7\).

If “proper divisor” is instead taken to include \(1\), then the event \(\gcd(k,N)<N\) has mass

\[
1-\frac{N}{S(N)}=1-\frac1T\ge\frac47,
\]

again with equality only at \(N=9\). This is not the event useful for factoring.

## 4. Distinct semiprimes

Let \(N=pq\) for distinct odd primes \(p,q\), and put

\[
D=S(pq)=(2p-1)(2q-1)=4pq-2p-2q+1.
\]

The law splits into four gcd classes:

| gcd class | number of residues | total \(\pi_N\)-mass |
|---|---:|---:|
| \(1\) | \((p-1)(q-1)\) | \((p-1)(q-1)/D\) |
| \(p\) | \(q-1\) | \(p(q-1)/D\) |
| \(q\) | \(p-1\) | \(q(p-1)/D\) |
| \(pq\) | \(1\), namely \(0\) | \(pq/D\) |

In particular,

\[
\boxed{\pi_{pq}(\mathcal U_{pq})
=\frac{2pq-p-q}{(2p-1)(2q-1)}
=\frac12-\frac1{2(2p-1)(2q-1)}}.
\]

Conditioned on obtaining a factor-revealing residue,

\[
\Pr(\gcd(k,N)=p\mid\mathcal U_N)
=\frac{p(q-1)}{2pq-p-q},
\]

and the analogous probability for \(q\) is \(q(p-1)/(2pq-p-q)\).

For balanced semiprimes (both primes \(\Theta(\sqrt N)\)), all four class masses are \(1/4+O(N^{-1/2})\), and the useful mass is \(1/2+O(N^{-1})\) (in fact, it is just below \(1/2\) by the exact formula above).

## 5. Precise conditional sampler-to-factoring theorem

### Theorem

Suppose there is a uniform classical randomized algorithm \(A\) with the following guarantee. For every odd \(M\ge3\) and every requested accuracy \(0<\delta<1\), a fresh invocation:

1. returns an explicit residue \(K\in\{0,\ldots,M-1\}\);
2. terminates almost surely;
3. has output law \(\mu_{M,\delta}\) satisfying

   \[
   \|\mu_{M,\delta}-\pi_M\|_{\mathrm{TV}}\le\delta;
   \]

4. uses expected bit operations and expected independent fair random bits bounded by fixed polynomials in \(\log M\) and \(\log\delta^{-1}\).

Fresh invocations mean that the algorithm is reset and supplied independent fair-bit streams. Then every integer \(N\ge2\) has a complete all-input classical Las Vegas factorization algorithm with expected bit complexity and expected fair-bit complexity polynomial in \(\log N\).

It is enough that the sampler be available at any one fixed error \(\delta_0<2/7\). For concreteness, call it at \(\delta_*=1/14\).

### One split

For an odd composite \(M\), total variation controls every event, so

\[
\Pr_{\mu_{M,\delta_*}}(1<\gcd(K,M)<M)
\ge \frac27-\frac1{14}=\frac3{14}=:c.
\]

Repeat fresh calls until \(d=\gcd(K,M)\) satisfies \(1<d<M\). Each returned \(d\) is deterministically verified and is an actual divisor, so the procedure never returns a wrong split. After \(r\) failed calls the probability of still having no split is at most \((1-c)^r=(11/14)^r\). Hence the number of calls is almost surely finite and has expectation at most \(1/c=14/3\).

### Runtime/output correlation

No independence between a call’s runtime and its success is needed. Let \((C_i,I_i)\) be the cost and success indicator of the \(i\)-th fresh call. The pairs are independent across calls, but \(C_i\) and \(I_i\) may be arbitrarily correlated within a pair. If \(\tau=\min\{i:I_i=1\}\) and \(s=\Pr(I_i=1)\ge c\), then

\[
\begin{aligned}
\mathbb E\left[\sum_{i=1}^{\tau}C_i\right]
&=\sum_{i\ge1}\mathbb E\left[C_i
  \mathbf 1\{I_1=\cdots=I_{i-1}=0\}\right]\\
&=\sum_{i\ge1}\mathbb E[C_i](1-s)^{i-1}
=\frac{\mathbb E[C_1]}s.
\end{aligned}
\]

The event multiplying \(C_i\) depends only on earlier calls. The same argument separately bounds bit operations, fair bits, and the polynomial-time gcd checks. Thus a correlation such as “successful samples take longer” does not invalidate the expectation bound. By contrast, merely having correct one-call marginals from a persistent, cross-call-correlated black box would be insufficient: all calls could share one hidden failure coin. Resettable fresh randomness (or a uniform conditional success bound after every history) is essential.

### Complete factorization and all input classes

On input \(N\):

1. Remove all powers of \(2\) by exact division.
2. On every remaining recursive factor \(M\), run a deterministic polynomial-time primality test. If \(M\) is prime, emit it.
3. If \(M\) is odd and composite, run the split procedure above and recurse on \(d\) and \(M/d\).
4. Combine equal prime leaves to recover their multiplicities, and verify their product is \(N\).

Prime inputs terminate at the primality test rather than entering an impossible sampling loop. Prime powers need no promise or special oracle: for \(M=p^a\), the useful-mass formula above is at least \(2/7\), and a useful sample returns some \(p^j\), \(1\le j<a\). Recursion handles repeated factors. Deterministic perfect-power detection and recursion on the base may be added, but are not needed for the proof.

Let \(L=\lceil\log_2(N+1)\rceil\). A complete binary split tree has \(\Omega(N)\) prime leaves counted with multiplicity and at most \(\Omega(N)-1\) internal nodes, while \(\Omega(N)\le\log_2N<L\). Every intermediate integer has at most \(L\) bits. Thus there are \(O(L)\) primality tests, split nodes, and bookkeeping operations. At each split node the conditional expected sampler and gcd cost is bounded by a fixed polynomial in \(L\). Summing conditional expectations over at most \(O(L)\) nodes gives a fixed polynomial in \(L\). The recursion is finite almost surely, so this is a complete Las Vegas algorithm, not merely a one-factor routine.

### Sharpness of the TV threshold for this reduction

At \(N=9\), \(\pi_9(\mathcal U_9)=2/7\). Move all of that mass to \(k=0\), leaving the other probabilities unchanged. The resulting law has total-variation distance exactly \(2/7\) from \(\pi_9\) and never produces a useful gcd. Therefore a guarantee \(\delta\le2/7\) with equality allowed does not imply a positive split probability by this argument; \(\delta<2/7\) is the sharp uniform threshold.

The theorem also genuinely needs an actual accessible residue. A probability oracle, an implicit quantum state, or an unspecified sample of a coarsening does not automatically provide an integer on which the Euclidean algorithm can be run.

## 6. Exact sampling given a factorization, and circular constructions

The converse reduction is easy and clarifies hidden assumptions. Given the prime factorization \(N=\prod p_i^{a_i}\), CRT makes \(\pi_N\) a product of its prime-power laws because both gcd and \(S\) multiply.

For a component \(p^a\), choose a gcd exponent \(J\in\{0,\ldots,a\}\) with integer weights

\[
\Pr(J=j)=\frac{p-1}{a(p-1)+p}\quad(0\le j<a),
\qquad
\Pr(J=a)=\frac{p}{a(p-1)+p}.
\]

If \(J=a\), output \(0\bmod p^a\). Otherwise choose a uniform unit \(u\bmod p^{a-J}\) and output \(p^J u\bmod p^a\). Combine the independent components by CRT. Exact finite weighted choices and uniform residues can be generated from fair bits by binary rejection with constant expected overhead; uniform-unit rejection succeeds with probability at least \(2/3\). The total bit and fair-bit costs are polynomial in \(\log N\).

Thus complete factorization gives an exact efficient sampler, while any all-input explicit sampler within fixed TV error below \(2/7\) gives Las Vegas factoring. The two tasks are polynomial-time interreducible in this model. A purported “direct” sampler that first uses the prime factors or CRT decomposition is therefore circular as a new factoring method.

Even the exact normalizer can hide factoring. For a distinct semiprime,

\[
S(pq)=4N-2(p+q)+1,
\qquad
p+q=\frac{4N+1-S(N)}2.
\]

Exact knowledge of \(S(N)\) then recovers \(p,q\) as the roots of \(X^2-(p+q)X+N\). A construction that assumes \(S(N)\), \(\pi_N(0)\), or the gcd-class sizes exactly has not avoided factoring. Computing \(\gcd(k,N)\) for a supplied \(k\), however, is ordinary polynomial-time arithmetic; the hard part is producing the correctly biased residue efficiently.

## 7. Audit of the obvious samplers on balanced semiprimes

Throughout this section let \(N=pq\) with distinct balanced odd primes and write \(D=(2p-1)(2q-1)\). Thus

\[
D=4N+O(\sqrt N),\qquad \frac ND=\frac14+O(N^{-1/2}).
\]

All costs below are exponential in the input length \(\Theta(\log N)\).

### 7.1 Uniform rejection

Propose \(K\) uniformly modulo \(N\), compute \(g=\gcd(K,N)\), and accept with probability \(g/N\). The probability of returning a particular \(k\) in one trial is \(\gcd(k,N)/N^2\), so conditioning on acceptance gives exactly \(\pi_N\). The one-trial acceptance probability and exact expected proposal count are

\[
\boxed{\Pr(\mathrm{accept})=\frac{S(N)}{N^2}=\frac D{N^2}},
\qquad
\boxed{\mathbb E[\#\mathrm{proposals}]=\frac{N^2}{D}
=\frac N4+O(\sqrt N)}.
\]

This is an exact sampler, but not a polynomial-in-\(\log N\) one. The equivalent rejection of uniform pairs \((k,u)\) until \(ku\equiv0\pmod N\) has the same acceptance probability, since the number of such pairs is \(S(N)\).

### 7.2 Direct uniform gcd trial factoring

If one ignores acceptance and simply stops as soon as a uniform proposal has a nontrivial gcd, then

\[
\boxed{\Pr(1<\gcd(K,N)<N)=\frac{p+q-2}{N}},
\qquad
\boxed{\mathbb E[\#\mathrm{proposals}]=\frac{N}{p+q-2}=\Theta(\sqrt N)}.
\]

When \(p/q\to1\), this is asymptotic to \(\sqrt N/2\). This observation is faster than waiting for the rejection sampler to accept, but still exponential in \(\log N\). If the rejection implementation opportunistically uses a nontrivial intermediate gcd and then samples using the recovered factors, it has merely switched to this \(\Theta(\sqrt N)\)-trial factoring method; it has not obtained a polylogarithmic sampler.

### 7.3 Lazy uniform-proposal independence Metropolis

Let \(w(x)=\gcd(x,N)\). The non-lazy independence-Metropolis kernel proposes \(y\) uniformly and accepts with probability

\[
\alpha(x,y)=\min\left(1,\frac{w(y)}{w(x)}\right).
\]

Its lazy version \(P=(I+K)/2\) is reversible with stationary law \(\pi_N\), because the off-diagonal flow is proportional to \(\min(w(x),w(y))\).

The singleton \(0\) gives an exact slow mode. Put \(\pi_0=\pi_N(0)=N/S(N)\) and \(f=\mathbf 1_{\{0\}}-\pi_0\). Directly,

\[
P(0,y)=\frac{w(y)}{2N^2}\quad(y\ne0),
\qquad
P(x,0)=\frac1{2N}\quad(x\ne0),
\]

and hence

\[
\boxed{Pf=\lambda f,\qquad
\lambda=1-\frac{S(N)}{2N^2}}.
\]

For any initial law \(\mu_0\),

\[
\mu_0P^t(0)-\pi_0
=\lambda^t\bigl(\mu_0(0)-\pi_0\bigr),
\]

so

\[
\boxed{\|\mu_0P^t-\pi_N\|_{\mathrm{TV}}
\ge |\mu_0(0)-\pi_0|\lambda^t}.
\]

In particular, the worst-case mixing time satisfies, for \(0<\varepsilon<1-\pi_0\),

\[
t_{\mathrm{mix}}(\varepsilon)
\ge
\frac{\log((1-\pi_0)/\varepsilon)}{-\log(1-S(N)/(2N^2))}.
\]

On balanced semiprimes,

\[
\pi_0=\frac14+O(N^{-1/2}),
\qquad
\lambda=1-\frac2N+O(N^{-3/2}),
\]

so, for each fixed \(\varepsilon<3/4\), the displayed lower bound is

\[
\left(\frac N2+o(N)\right)
\log\frac{3/4}{\varepsilon}.
\]

For example, \(t_{\mathrm{mix}}(1/4)\ge (N/2+o(N))\log3\). The same eigenmode proves \(\Omega(N)\) mixing from the natural uniform initialization whenever the requested error is a fixed constant below \(1/4\), because then \(|\mu_0(0)-\pi_0|=1/4+o(1)\). It also yields the spectral-gap upper bound

\[
\operatorname{gap}(P)\le\frac{S(N)}{2N^2}=\frac2N+O(N^{-3/2}).
\]

This is a mixing lower bound in transition steps; the ordinary implementation additionally spends polynomially many bit operations and \(\Theta(\log N)\) fair bits per uniform proposal.

The exact zero-mode bound is deliberately not overclaimed. An initializer with exactly the correct zero mass kills that eigencomponent. There is still a factor-class obstruction for any initializer that places little mass on

\[
B=\{x:1<\gcd(x,N)<N\}.
\]

If \(b_0=\mu_0(B)\), entering \(B\) from outside requires an active uniform proposal in \(B\), whose per-step probability is \((p+q-2)/(2N)\). Therefore

\[
\mu_0P^t(B)\le b_0+\frac{t(p+q-2)}{2N}.
\]

Since \(\pi_N(B)=1/2+o(1)\), any initialization with \(b_0=o(1)\) still needs \(\Omega(\sqrt N)\) steps for fixed small TV error. Conversely, an efficient initializer that already puts constant probability on explicit residues in \(B\) is itself a constant-success factoring routine, because taking a gcd exposes \(p\) or \(q\).

## 8. Counterexample and hidden-assumption audit

- **Even moduli:** the \((x-y,x+y)\) substitution is not invertible. The exact energy formula proved here is only for odd \(N\); factor out \(2\) before invoking it.
- **Zero residue:** \(k=0\) has weight \(N\), not weight \(1\), and has asymptotic target mass \(1/4\) on balanced semiprimes. Omitting it corrupts the normalizer, the useful-mass bound, and the Metropolis analysis.
- **Meaning of proper:** \(\gcd=1\) is a proper divisor under one convention but reveals no factor. The factoring event is strictly \(1<\gcd<N\).
- **TV threshold:** \(2/7\) is sharp for the event argument; equality is insufficient, as the \(N=9\) mass-transfer counterexample shows.
- **Prime loop:** a prime has zero useful mass. Deterministic primality testing must precede repetition.
- **Powers and repeated factors:** they cannot be excluded by a squarefree or semiprime promise. The universal bound includes prime powers, and the recursive tree counts multiplicity.
- **Cross-call dependence:** correct marginals do not imply eventual success under persistent correlation. Fresh independent invocations are part of the reduction.
- **Runtime/success dependence:** same-call correlation is harmless, but only after the stopped-sum expectation is proved as above; multiplying two expectations without justification is not enough.
- **Randomness model:** an ideal uniform real or uncosted exact Bernoulli is not a fair-bit algorithm. Expected fair bits must be counted. Rational rejection sampling supplies them, but does not fix the exponential proposal counts of the audited schemes.
- **Hidden factorization:** prime-power decomposition, CRT components, exact gcd-class sizes, and on semiprimes even exact \(S(N)\) already reveal the sought arithmetic information. They may prove the converse sampler construction, but cannot be assumed in a new factoring algorithm.
- **Scope of the sampler:** a guarantee only for balanced semiprimes does not support recursion on arbitrary factors. The conditional theorem assumes every odd modulus, while primes are detected before sampling.

## 9. What remains unresolved by these audits

The analysis rules out only the stated implementations:

- uniform rejection has exact expected cost \(\Theta(N)\) on balanced semiprimes;
- direct uniform-gcd trials take \(\Theta(\sqrt N)\);
- lazy independence Metropolis with uniform proposals has an \(\Omega(N)\) standard mixing obstruction, and even an initializer that repairs the zero atom but cannot already produce factor-revealing residues faces the stated \(\Omega(\sqrt N)\) hitting obstruction.

It does **not** prove a lower bound for all classical samplers. Unresolved by these arguments are nonuniform arithmetic proposals, nonreversible or auxiliary-variable chains, exact combinatorial samplers, coupling-from-the-past constructions, and other direct algorithms that avoid uniform rare-event discovery. A specially warm Metropolis initialization with the relevant target macro-masses is also outside the exact zero-eigenmode lower bound—but producing constant mass on the nontrivial-gcd classes already gives a factoring algorithm.

Most importantly, an all-input explicit sampler for \(\pi_N\) with fixed TV error below \(2/7\), almost-sure termination, and expected polynomial bit/fair-bit cost remains exactly as strong as classical Las Vegas factoring under the reductions above. Naming such a sampler without proving its construction and costs merely relocates the original factoring problem.
