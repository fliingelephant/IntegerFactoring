# Result: PASS

The SHA-256 digest of the statement is
`c25264a5fcc7490b734daeca8cff985d4071423c2e97f818c8f480e8653ea79c`,
as required. All claims and constants are correct. Here, “balanced” has its
usual strong meaning \(p,q=\Theta(\sqrt N)\). If it is instead used for the
weaker condition \(p,q=N^{1/2+o(1)}\), the first displayed asymptotic should
be read as \(N^{-1/2+o(1)}\), as it already is in Claim 3. In Claim 5, \(u\)
is the canonical representative in \(U_N\), consistently with the setup.

## 1. Signed fibres and the discriminant ticket

If \(d(u)=d\), then \(v(u)=u-d\). Requiring both \(u\) and \(u-d\) to be in
\(\{1,\ldots,N-1\}\) gives exactly

\[
\max(1,1+d)\leq u\leq\min(N-1,N-1+d).
\]

The inverse condition is \(u(u-d)\equiv1\pmod N\). Conversely, that
congruence makes \(u\) a unit, and under the displayed interval condition
\(u-d\) is its canonical inverse. This proves the asserted description of
\(F_d\).

For a member of the fibre, write

\[
u(u-d)=u\,v(u)=1+kN.
\]

Since \(1\leq u,v(u)\leq N-1\), one has
\(0\leq k\leq ((N-1)^2-1)/N=N-2\). Also,

\[
(2u-d)^2=d^2+4u(u-d)=d^2+4+4kN.
\]

For an odd prime \(r\), multiplication by \(2\) is invertible and

\[
u^2-du-1\equiv0\pmod r
\quad\Longleftrightarrow\quad
(2u-d)^2\equiv d^2+4\pmod r.
\]

The number of square roots of \(a\) modulo \(r\) is
\(1+(a/r)\), including the case \(a=0\). The Chinese remainder theorem
therefore gives

\[
R_N(d)=
\left(1+\left(\frac{d^2+4}{p}\right)\right)
\left(1+\left(\frac{d^2+4}{q}\right)\right).
\]

The canonical interval can only remove roots, so \(f_d\leq4\). Inversion is
a bijection \(F_d\to F_{-d}\), hence \(f_d=f_{-d}\). Finally, two canonical
representatives differ in absolute value by at most \(N-2\), so the fibre is
empty when \(|d|\geq N-1\).

For an observed pair \(uv\equiv1\pmod N\),

\[
d(u)^2+4=(u-v)^2+4\equiv(u+v)^2\pmod N.
\]

Modulo a prime divisor \(r\) of \(N\), divisibility of this discriminant by
\(r\) implies

\[
u+u^{-1}\equiv0\pmod r,
\qquad u^2\equiv-1\pmod r.
\]

There are at most two such nonzero residues modulo \(r\). A uniform element
of \(U_N\cong\mathbb F_p^*\times\mathbb F_q^*\) has uniform coordinates, so
the union bound gives

\[
\Pr(1<\gcd(d(u)^2+4,N)<N)
\leq \frac2{p-1}+\frac2{q-1}.
\]

A proper gcd is one of \(p,q\). For \(p,q=\Theta(\sqrt N)\), the displayed
bound is \(O(N^{-1/2})\).

## 2. Normalizer, useful mass, and total variation

The equation \(u^2\equiv1\pmod N\) has two roots modulo each odd prime and
therefore exactly four roots modulo \(N\). Thus exactly four states have
\(\delta=0\), and each contributes \(1\) to \(Z_N\). Using the fibre bounds,

\[
\begin{aligned}
Z_N
&=4+\sum_{d=1}^{N-2}\frac{f_d+f_{-d}}{d+1}\\
&\leq4+8\sum_{d=1}^{N-2}\frac1{d+1}
=8H_{N-1}-4.
\end{aligned}
\]

This proves \(4\leq Z_N\leq8H_{N-1}-4\).

The CRT sign choices \((1,1)\) and \((-1,-1)\) give \(1\) and \(N-1\).
The other two choices are mixed. For either mixed root \(a\), one of
\(\gcd(a-1,N)\) and \(\gcd(a+1,N)\) is \(p\), and the other is \(q\).
Consequently, for the two-element mixed set \(M_N\),

\[
\pi(M_N)=\frac2{Z_N}
\geq\frac1{4H_{N-1}-2}.
\]

The elementary integral bound \(H_m\leq1+\log m\) gives

\[
\pi(M_N)\geq\frac1{4\log(N-1)+2}.
\]

Let \(Q\) be an output law with

\[
\lVert Q-\pi\rVert_{\rm TV}\leq
\varepsilon:=\frac1{8H_{N-1}-4}.
\]

Since \(\pi(M_N)\geq2\varepsilon\), the event form of total variation gives
\(Q(M_N)\geq\varepsilon\). Therefore \(C\log N\) independent runs have
failure probability at most
\((1-\varepsilon)^{C\log N}\leq e^{-C\varepsilon\log N}\), which is bounded
away from \(1\) for a suitable constant \(C\). This proves the claimed
constant factoring probability.

## 3. Uniform rejection

For a uniform proposal on the \(m=\varphi(N)\) units, the probability of
acceptance is

\[
\frac1m\sum_{u\in U_N}w(u)=\frac{Z_N}{m}.
\]

Conditional on acceptance, the probability of \(u\) is \(w(u)/Z_N\), so the
output is exactly \(\pi\), and the mean number of proposals is \(m/Z_N\).

After ordering \(p<q\), the smallest possible distinct odd primes are \(3\)
and \(5\). Monotonicity of \(1-1/r\) gives

\[
\frac{\varphi(N)}N
=\left(1-\frac1p\right)\left(1-\frac1q\right)
\geq\frac23\frac45=\frac8{15}.
\]

Together with \(Z_N\leq8H_{N-1}-4=O(\log N)\), this proves

\[
\frac{\varphi(N)}{Z_N}=\Omega\!\left(\frac N{\log N}\right).
\]

Since \(2^{n-1}<N\leq2^n\), this is exponential up to a polynomial factor in
\(n\).

If the proposal is uniform on all \(N\) residue classes and nonunits are
rejected, the success probability per proposal is \(Z_N/N\), so the mean
is \(N/Z_N\), not an improvement. The same conclusion holds with \(N-1\)
in place of \(N\) if zero is omitted.

Among nonzero residues, the number having a proper nonunit gcd with \(N\)
is \(p+q-2\). Thus its probability is \(O(1/p+1/q)\). The discriminant
ticket has probability at most the bound in Part 1. On balanced semiprimes,
their union is \(O(N^{-1/2+o(1)})\); multiplying this by any polynomial in
\(n\) still tends to zero. Hence these side exits do not give the named
sampler a polynomial-time factoring success probability.

## 4. Independent uniform-proposal Metropolis--Hastings

For distinct \(x,y\),

\[
\pi(x)P(x,y)
=\frac1{mZ_N}\min(w(x),w(y))
=\pi(y)P(y,x).
\]

Thus detailed balance holds, and the diagonal completion makes \(P\) a
reversible Markov kernel with stationary law \(\pi\).

The state \(1\) has weight \(1\). Therefore its exact probability of leaving
in one step is

\[
\ell=\sum_{y\ne1}\frac{w(y)}m=\frac{Z_N-1}{m}.
\]

Starting from \(1\), the probability of never leaving during the first \(t\)
steps is \((1-\ell)^t\geq1-t\ell\). If
\(t\leq m/(4(Z_N-1))\), this is at least \(3/4\). Since
\(\pi(1)=1/Z_N\leq1/4\),

\[
\lVert P^t(1,\cdot)-\pi\rVert_{\rm TV}
\geq P^t(1,\{1\})-\pi(1)\geq\frac12.
\]

The lower bound on \(m\) and upper bound on \(Z_N\) make this time scale
\(\Omega(N/\log N)\), proving the worst-start mixing claim.

Now let \(X_0\) be uniform on \(U_N\). A state can first enter \(M_N\) only
if \(X_0\in M_N\) or one of the first \(t\) independent uniform proposals
lies in \(M_N\). A union bound gives

\[
\Pr(X_t\in M_N)\leq\frac{2(t+1)}m.
\]

If \(t+1\leq m/(4Z_N)\), the right side is at most \(1/(2Z_N)\). Therefore

\[
\begin{aligned}
\lVert\mathcal L(X_t)-\pi\rVert_{\rm TV}
&\geq \pi(M_N)-\Pr(X_t\in M_N)\\
&\geq\frac{3}{2Z_N}\\
&\geq\frac{3}{2(8H_{N-1}-4)}
>\frac1{8H_{N-1}-4}.
\end{aligned}
\]

For \(t=\operatorname{poly}(n)\), the useful-root probability bound is
\(O(\operatorname{poly}(n)/N)\), hence negligible. This conclusion in fact
does not require balance.

## 5. The nearest-neighbor plateau and its minimum modulus

Let the congruence \(u^2+u-1\equiv0\pmod N\) hold for a canonical \(u\).
It is equivalent to \(u(u+1)\equiv1\pmod N\), so \(u,u+1\) are inverse
units. The residues \(0,1,-2,-1\) do not solve the quadratic; hence
\(2\leq u\leq N-3\), and all four line positions
\(u-1,u,u+1,u+2\) are canonical.

No prime divisor \(r\) of \(N\) can divide \(u-1\) or \(u+2\): substitution
of \(u\equiv1\) or \(u\equiv-2\pmod r\) into the quadratic gives \(1\equiv0\).
Thus both outer neighbors are units.

Put \(x=u-1\). If its inverse were \(x+1\), then
\((u-1)u\equiv1\), which together with \(u^2+u\equiv1\) gives
\(2u\equiv0\), impossible. If its inverse were \(x-1\), then
\((u-1)(u-2)\equiv1\), which gives \(2u\equiv1\); multiplying the original
quadratic by \(4\) then gives \(-1\equiv0\pmod N\), impossible. If \(x\)
were self-inverse, then
\((u-1)^2\equiv1\). Since \(u\) is a unit, this gives \(u\equiv2\pmod N\),
and the quadratic gives \(5\equiv0\pmod N\), contrary to
\(\gcd(N,5)=1\). Hence \(\delta(u-1)>1\).

Put \(y=u+2\). If its inverse were \(y-1\), then
\((u+2)(u+1)\equiv1\), which gives \(u\equiv-1\) and then
\(-1\equiv0\pmod N\). If its inverse were \(y+1\), then
\((u+2)(u+3)\equiv1\), which gives \(2u\equiv-3\); multiplying the
quadratic by \(4\) again gives \(-1\equiv0\pmod N\). If \(y\) were
self-inverse, then \((u+1)(u+3)\equiv0\). The unit \(u+1\) can be cancelled,
so \(u\equiv-3\), and the quadratic gives \(5\equiv0\pmod N\). Thus
\(\delta(u+2)>1\).

It follows that the distances on the four positions have the form
\(>1,1,1,>1\). Strict descent cannot leave either middle state. A
non-increasing line-neighbor rule can traverse the middle tie but cannot
cross either outer edge. The signed differences of the middle inverse pair
are \(-1\) and \(1\), so both have discriminant \(1^2+4=5\); its gcd with
\(N\) is trivial by hypothesis.

It remains to prove the minimality, rather than infer it from a computation.
For an odd prime \(r\ne5\), the quadratic has a root modulo \(r\) exactly
when \(5\) is a quadratic residue modulo \(r\). Since \(5\equiv1\pmod4\),
quadratic reciprocity gives

\[
\left(\frac5r\right)=\left(\frac r5\right),
\]

so an eligible prime satisfies \(r\equiv1\) or \(4\pmod5\). The prime \(5\)
is excluded by cleanliness. The two smallest distinct eligible odd primes
are therefore \(11\) and \(19\): the smaller odd primes \(3,7,13,17\) are
congruent to \(2\) or \(3\pmod5\). Hence every clean two-prime modulus with
a height-one plateau is at least \(11\cdot19=209\).

For existence at that bound,

\[
80^2+80-1=6479=31\cdot209.
\]

The stated inverse identities follow from

\[
79\cdot127=48\cdot209+1,
\quad 80\cdot81=31\cdot209+1,
\quad 82\cdot130=51\cdot209+1.
\]

Thus the distances at \(79,80,81,82\) are \(48,1,1,48\), and
\(\gcd(5,209)=1\).

## Scope

Each obstruction above uses a property specific to its named transition or
proposal rule. None supplies a lower bound for arbitrary samplers or larger,
structured moves. Conversely, the useful-mass argument is conditional on an
efficient sampler for \(\pi\). Therefore the final scope paragraph follows
from the proved statements and makes no broader factoring claim.
