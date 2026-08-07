# F66 inverse-diagonal metric kill

**Family:** F24.

**Status:** proof-only kill test. No research computation was run.

**Verdict:** the diagonal weight has the desired factor-root mass, but all
three named access methods fail as a sampler proposal.

- **Target signal: PASS.** The two non-global zeroes have normalized mass
  \(\Omega(1/\log N)\).
- **Uniform rejection: FAIL.** Its expected proposal count is
  \(\Omega(N/\log N)\).
- **Uniform-proposal Metropolis--Hastings: FAIL.** Its worst-start mixing time
  is \(\Omega(N/\log N)\). From a uniform start, reaching the useful zeroes
  to the accuracy needed for factoring also takes \(\Omega(N/\log N)\) steps.
- **Nearest-neighbor steepest descent: FAIL as a guaranteed route.** It has a
  non-root two-state local plateau. The smallest clean minimum-height example
  proved here is \(N=209\). The plateau does not expose a factor through the
  fibre discriminant.

Here and below, polynomial time means polynomial in the bit length
\(n=\lceil\log _2N\rceil\), not polynomial in \(N\).

## 1. Closest route and material difference

The closest prior result is P49 in F24. P49 bounds public sparse additive
Fourier signals and fixed axis-aligned histogram signals of the uniform
inverse graph

\[
 \{(u,u^{-1}\bmod N):u\in(\mathbb Z/N\mathbb Z)^\times\}.
\]

It explicitly leaves curved or diagonal statistics, nonuniform sources, and
dissipative dynamics open.

This retry is materially different. It uses the nonlinear canonical distance

\[
 \delta_N(u)=|u-v|,
\]

where both \(u\) and its inverse \(v\) are represented in
\(\{1,\ldots,N-1\}\). It then reweights the inverse graph by

\[
 w(u)=\frac1{1+\delta_N(u)}.
\]

P49 does not cover this statistic or the proposed samplers. The obstruction
below is instead a sparse-fibre normalization theorem followed by exact
runtime and mixing bounds.

## 2. Setup

Let

\[
 N=pq,
\]

where \(p\ne q\) are odd primes, and put

\[
 U_N=\{u\in\{1,\ldots,N-1\}:\gcd(u,N)=1\}.
\]

For \(u\in U_N\), let \(v(u)\in\{1,\ldots,N-1\}\) be its canonical inverse:

\[
 uv(u)\equiv1\pmod N.
\]

Define the signed difference

\[
 s_N(u)=u-v(u)
\]

and \(\delta_N(u)=|s_N(u)|\). For an integer \(d\), define the signed fibre

\[
 F_d=\{u\in U_N:s_N(u)=d\},\qquad f_d=|F_d|.
\]

The target law is

\[
 \pi(u)=\frac{w(u)}{Z_N},\qquad
 Z_N=\sum_{x\in U_N}w(x).
\]

All weights are computable without the factors. The extended Euclidean
algorithm either returns \(v(u)\), or returns a nontrivial gcd when a proposed
residue is not a unit.

## 3. Exact signed-fibre equation

### Theorem 1: fibre equation and four-point bound

For every integer \(d\),

\[
 \boxed{
 F_d=
 \left\{
 u\in\mathbb Z:
 \begin{array}{l}
 \max(1,1+d)\le u\le\min(N-1,N-1+d),\\
 u^2-du-1\equiv0\pmod N
 \end{array}
 \right\}.}
 \tag{1}
\]

Equivalently, \(u\in F_d\) exactly when the interval condition in (1) holds
and, for some \(k\in\{0,\ldots,N-2\}\),

\[
 \boxed{u(u-d)=1+kN.}
 \tag{2}
\]

After completing the square, the same equation is

\[
 \boxed{(2u-d)^2=d^2+4+4kN.}
 \tag{3}
\]

Put \(\Delta_d=d^2+4\), and extend the Legendre symbol by
\(\left(\frac0r\right)=0\). The number of roots of the congruence in (1),
before the canonical interval cut, is exactly

\[
 \boxed{
 R_N(d)=
 \left(1+\left(\frac{\Delta_d}{p}\right)\right)
 \left(1+\left(\frac{\Delta_d}{q}\right)\right).}
 \tag{4}
\]

Consequently,

\[
 \boxed{f_d\le R_N(d)\le4.}
 \tag{5}
\]

Also, \(F_d\) is empty for \(|d|\ge N-1\), and inversion gives
\(f_d=f_{-d}\).

#### Proof

If \(s_N(u)=d\), then \(v=u-d\). The condition
\(1\le v\le N-1\) gives the interval in (1), and \(uv\equiv1\pmod N\)
gives its congruence. These steps are reversible, so (1) is exact. The bounds
on \(u\) and \(v\) give \(0\le k\le N-2\), proving (2). Equation (3) is
four times (2), followed by completing the square.

For an odd prime \(r\), multiplication by \(2\) is invertible, and

\[
 u^2-du-1\equiv0\pmod r
 \quad\Longleftrightarrow\quad
 (2u-d)^2\equiv\Delta_d\pmod r.
\]

A square equation modulo \(r\) has
\(1+\left(\frac{\Delta_d}{r}\right)\) roots. CRT multiplies the two local
counts, which proves (4). The canonical interval can only remove roots, so
(5) follows. Finally, inversion exchanges \(u\) and \(v\), hence exchanges
\(d\) and \(-d\). \(\square\)

### Public discriminant ticket

For an observed inverse pair, the same discriminant is also

\[
 \Delta_{s_N(u)}=(u-v)^2+4\equiv(u+v)^2\pmod N.
 \tag{6}
\]

Therefore

\[
 1<\gcd(\Delta_{s_N(u)},N)<N
\]

is an immediate public factor ticket. This check does not need \(p\) or
\(q\).

It does not rescue polynomially many uniform proposals on balanced
semiprimes. Modulo a prime \(r\mid N\), the event \(r\mid\Delta_{s_N(u)}\)
is exactly \(u^2\equiv-1\pmod r\), which has at most two local solutions.
Thus, for uniform \(u\in U_N\),

\[
 \Pr\bigl(1<\gcd(\Delta_{s_N(u)},N)<N\bigr)
 \le \frac2{p-1}+\frac2{q-1}.
 \tag{7}
\]

This is \(O(N^{-1/2})\) on every fixed balanced semiprime family.

## 4. The target has inverse-polynomial useful mass

### Theorem 2: logarithmic normalizer

Let \(H_m=\sum_{j=1}^m1/j\). Then

\[
 \boxed{4\le Z_N\le8H_{N-1}-4.}
 \tag{8}
\]

There are exactly four zeroes of \(\delta_N\). Two are the global roots
\(1,N-1\). The other two are the mixed CRT roots of \(x^2=1\pmod N\), and
each reveals a factor. If \(M_N\) denotes this two-element useful set, then

\[
 \boxed{
 \pi(M_N)=\frac2{Z_N}
 \ge\frac1{4H_{N-1}-2}
 \ge\frac1{4\log(N-1)+2}.}
 \tag{9}
\]

In particular, \(\pi(M_N)=\Omega(1/n)\).

#### Proof

CRT gives four roots of \(u^2=1\pmod N\), so \(f_0=4\). Theorem 1 gives
\(f_d\le4\) for every other signed difference. Therefore

\[
\begin{aligned}
 Z_N
 &=\sum_{d=-(N-2)}^{N-2}\frac{f_d}{1+|d|}\\
 &\le4+8\sum_{d=1}^{N-2}\frac1{1+d}
 =8H_{N-1}-4.
\end{aligned}
\]

The lower bound follows from the four weight-one zeroes.

The two mixed roots have CRT signs \((1,-1)\) and \((-1,1)\). For either
one, \(\gcd(u-1,N)\) or \(\gcd(u+1,N)\) is \(p\) or \(q\). Their total
unnormalized weight is exactly two. This proves (9), using
\(H_m\le1+\log m\). \(\square\)

Thus an efficient sampler within total-variation distance

\[
 \varepsilon\le\frac1{8H_{N-1}-4}
 \tag{10}
\]

would still return a useful root with probability at least
\(1/(8H_{N-1}-4)\). Repeating it \(O(\log N)\) times would factor with
constant probability. The signal is strong enough. Access to it is the
problem.

## 5. Uniform rejection is exponentially slow

Consider exact rejection sampling with a uniform proposal on \(U_N\). Since
\(0<w(u)\le1\), accept \(u\) with probability \(w(u)\). Conditional on
acceptance, the output law is exactly \(\pi\). Its acceptance probability and
expected proposal count are

\[
 a_{\rm rej}=\frac{Z_N}{\varphi(N)},
 \qquad
 \mathbb E T_{\rm rej}=\frac{\varphi(N)}{Z_N}.
 \tag{11}
\]

Distinct odd primes satisfy

\[
 \varphi(N)=N\left(1-\frac1p\right)\left(1-\frac1q\right)
 \ge\frac8{15}N.
 \tag{12}
\]

Combining (8), (11), and (12) gives

\[
 \boxed{
 \mathbb E T_{\rm rej}
 \ge\frac{8N/15}{8H_{N-1}-4}
 =\Omega\!\left(\frac N{\log N}\right).}
 \tag{13}
\]

If the proposal is instead uniform over all residues and nonunits are
rejected, the weighted acceptance probability is \(Z_N/N\). This is no
better.

A raw nonunit proposal can itself reveal a factor through its gcd with
\(N\). There are \(p+q-2\) such nonzero residues. On balanced semiprimes its
probability is \(N^{-1/2+o(1)}\) per proposal. Equation (7) gives the same
type of upper bound, \(O(N^{-1/2})\), for the discriminant ticket.
Polynomially many proposals in \(n\) do
not make either side event inverse-polynomial.

Therefore the exact rejection sampler exists but is not a polynomial-time
sampler.

## 6. Uniform-proposal Metropolis--Hastings is exponentially slow

Let \(m=\varphi(N)\). The independent uniform-proposal MH kernel is, for
\(x\ne y\),

\[
 P(x,y)=\frac1m\min\left(1,\frac{w(y)}{w(x)}\right),
 \tag{14}
\]

with the remaining mass placed on \(P(x,x)\). It is reversible with
stationary law \(\pi\), since

\[
 \pi(x)P(x,y)=\frac{\min(w(x),w(y))}{Z_Nm}
 =\pi(y)P(y,x).
\]

### Theorem 3: a sticky known root

Start the chain at the public global root \(x=1\). Its one-step probability
of leaving \(1\) is exactly

\[
 \ell=\frac{Z_N-1}{m}.
 \tag{15}
\]

For every integer

\[
 t\le\frac{m}{4(Z_N-1)},
\]

\[
 \boxed{\|P^t(1,\cdot)-\pi\|_{\rm TV}\ge\frac12.}
 \tag{16}
\]

Hence the usual worst-start mixing time, even at constant total-variation
accuracy, is

\[
 \boxed{\Omega\!\left(\frac N{\log N}\right).}
 \tag{17}
\]

#### Proof

At \(x=1\), \(w(x)=1\), so a proposal \(y\ne1\) is accepted with
probability \(w(y)\). Summing gives (15). The event that the chain never
leaves \(1\) during the first \(t\) steps has probability

\[
 (1-\ell)^t\ge1-t\ell\ge\frac34.
\]

Thus \(P^t(1,\{1\})\ge3/4\). But
\(\pi(1)=1/Z_N\le1/4\), which proves (16). Equations (8) and (12) give
(17). \(\square\)

### Uniform initialization also misses the useful mass

Let \(X_0\) be uniform on \(U_N\), and let \(M_N\) be the two mixed roots.
The chain can enter \(M_N\) only when its initial state or one of its uniform
proposals lies in \(M_N\). Therefore the union bound gives

\[
 \Pr(X_t\in M_N)\le\frac{2(t+1)}m.
 \tag{18}
\]

If \(t+1\le m/(4Z_N)\), then

\[
 \|\mathcal L(X_t)-\pi\|_{\rm TV}
 \ge \pi(M_N)-\Pr(X_t\in M_N)
 \ge\frac{3}{2Z_N}
 >\frac1{8H_{N-1}-4}.
 \tag{19}
\]

This is precisely the inverse-polynomial accuracy scale needed to preserve a
constant fraction of the factor-root mass. In polynomially many steps, (18)
also makes the chain's actual probability of returning a useful root
negligible on balanced semiprimes.

Thus neither the known easy start nor a uniform easy start yields an
efficient sampler. Starting from an already useful mixed root would already
require solving the factoring task.

## 7. Nearest-neighbor descent has a clean local trap

Use the natural line neighbors \(x-1,x+1\). If a neighbor is a nonunit, its
gcd with \(N\) factors \(N\). Otherwise, a strict steepest-descent rule moves
only to a smaller value of \(\delta_N\). A non-increasing variant can also
move across ties.

The first tempting small plateau is at \(N=55\):

\[
 \delta_{55}(6),\delta_{55}(7),\delta_{55}(8),\delta_{55}(9)
 =(40,1,1,40).
\]

However, the signed difference on the middle pair is \(d=\pm1\), so

\[
 \gcd(d^2+4,55)=\gcd(5,55)=5.
\]

This plateau itself reveals a factor and is not a clean obstruction.

### Theorem 4: a factor-free minimum-height plateau

For \(N=209=11\cdot19\), the four consecutive units
\(79,80,81,82\) satisfy

\[
 79^{-1}=127,qquad80^{-1}=81,qquad81^{-1}=80,qquad82^{-1}=130
 \pmod {209}.
\]

Indeed,

\[
 79\cdot127=48\cdot209+1,
 \quad
 80\cdot81=31\cdot209+1,
 \quad
 82\cdot130=51\cdot209+1.
\]

Hence

\[
 \boxed{
 \delta_{209}(79),\delta_{209}(80),
 \delta_{209}(81),\delta_{209}(82)
 =(48,1,1,48).}
 \tag{20}
\]

The plateau states \(80,81\) are not roots. Their discriminant ticket is

\[
 \gcd(1^2+4,209)=1.
\]

All four displayed states are units. Strict descent stops at \(80\) or
\(81\). A rule that permits only non-increasing tie moves is confined to the
two-cycle \(80\leftrightarrow81\). It reaches neither a zero nor a nonunit.

This is the smallest clean obstruction within the minimum-positive
\(\delta=1\) class. To see this, a state with inverse \(u+1\) obeys

\[
 u^2+u-1\equiv0\pmod N,
\]

whose discriminant is \(5\). If \(5\nmid N\), a root requires \(5\) to be a
quadratic residue modulo both prime factors. Quadratic reciprocity gives

\[
 \left(\frac5r\right)=1
 \quad\Longleftrightarrow\quad
 r\equiv\pm1\pmod5
\]

for odd primes \(r\ne5\). The two smallest such primes are \(11\) and
\(19\), so \(N\ge209\). Equality is attained because

\[
 80^2+80-1=31\cdot209.
\]

More generally, assume \(\gcd(N,5)=1\) and
\(u^2+u-1\equiv0\pmod N\). Then \(u-1\) and \(u+2\) are units: substituting
\(u=1\) or \(u=-2\) in the polynomial gives \(1\). They cannot have
distance zero or one. Write \(u^2\equiv1-u\pmod N\). For \(x=u-1\), the
three conditions that would give \(\delta_N(x)\le1\) reduce to

\[
\begin{array}{c|c}
\text{condition}&\text{consequence}\pmod N\\ \hline
x^2=1&3u=1,\ \text{hence }9(u^2+u-1)=-5,\\
x(x+1)=1&2u=0,\\
x(x-1)=1&2u=1,\ \text{hence }4(u^2+u-1)=-1.
\end{array}
\]

The first row contradicts \(\gcd(N,5)=1\), and the other rows contradict
oddness and the quadratic. For \(y=u+2\), the corresponding three
consequences are

\[
 3u=-4,\qquad u=-1,\qquad2u=-3.
\]

The first again gives \(9(u^2+u-1)=-5\); the other two give respectively
\(u^2+u-1=-1\) and \(4(u^2+u-1)=-1\). Thus every such adjacent inverse pair
is a sealed two-state local minimum, not an isolated accident at \(209\).

This obstruction refutes a universal monotone-convergence claim. By itself,
it does not prove a lower bound for random-start descent, because no basin
mass lower bound is proved here.

## 8. Final classification

The curved diagonal statistic survives the P49 thin-signal obstruction. Its
fibre geometry is unusually favorable: at most four units have any fixed
signed difference, so harmonic reweighting gives the two useful zeroes
inverse-polynomial target mass.

The proposed access mechanism does not survive:

1. uniform rejection pays the reciprocal mean weight and needs
   \(\Omega(N/\log N)\) proposals;
2. uniform-proposal MH has the same bottleneck as a sticky high-weight state
   and needs \(\Omega(N/\log N)\) steps;
3. nearest-neighbor descent has a factor-free non-root local plateau, so it
   has no global convergence theorem.

**Overall sampler proposal: FAIL.** Do not promote this as a factoring route
with any of the three named samplers.

What remains open is materially narrower: construct a different factor-free
sampler for \(w/Z_N\), or a different dynamics with a proved polynomial
hitting law. Such a method must avoid both the \(Z_N/\varphi(N)\) global
proposal bottleneck and the local plateaus above. This report proves no lower
bound for every possible sampler of the diagonal target.
