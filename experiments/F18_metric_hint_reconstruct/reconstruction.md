# Proof-blind reconstruction: metric-hint and explicit-wheel obstructions

**Status:** candidate independent reconstruction.

This is a proof-only note. I used no computation, so there is no run manifest.
The conclusions below are obstructions to two specified workflows, not a
classical polynomial-time factoring algorithm and not a lower bound for
factoring.

Throughout,

\[
N=pq,\qquad p<q<2p
\]

with distinct odd primes, and

\[
n=\lceil\log _2(N+1)\rceil.
\]

## 1. An additive approximation to the trace is enough

Let

\[
s=p+q.
\]

Suppose an explicitly represented integer or rational \(\widetilde s\) is
known with

\[
|\widetilde s-s|\le B(n),
\]

where \(B(n)\) is bounded by a fixed polynomial and the representation of
\(\widetilde s\) has polynomially many bits. Enumerate every integer \(t\) in

\[
[\widetilde s-B(n),\widetilde s+B(n)].
\]

There are at most \(2\lceil B(n)\rceil+2=\operatorname{poly}(n)\) such
integers. For each one, form

\[
D_t=t^2-4N.
\]

If \(D_t\ge 0\), compute its exact integer square root and test whether it is
a square. When it is, also test the parity and the proposed factors

\[
u=\frac{t-\sqrt{D_t}}2,
\qquad
v=\frac{t+\sqrt{D_t}}2
\]

by exact multiplication and by checking \(1<u,v<N\).

The true value \(t=s\) occurs in the enumeration, and

\[
D_s=(p+q)^2-4pq=(q-p)^2.
\]

It therefore returns \(u=p\) and \(v=q\). All tested integers have
\(O(n)\) bits: \(s<3p<3\sqrt N\), and adding a polynomial in \(n\) does not
change this bound. Integer multiplication, comparison, exact square root,
division by two, and verification are deterministic polynomial-bit
operations. Multiplying their cost by \(\operatorname{poly}(n)\) candidates
gives deterministic polynomial time.

This proves only the promised balanced-semiprime statement. It does not
produce the approximation \(\widetilde s\).

## 2. Polynomially bounded numerical multipliers can all be made bad

Here is the precise quantifier order. Let \(K,T\) be any two fixed functions
for which, for all sufficiently large \(n\),

\[
1\le K(n)\le C_K n^\kappa,
\qquad
0<T(n)\le C_T n^\tau
\tag{2.1}
\]

for fixed constants \(C_K,C_T,\kappa,\tau\). Then there are infinitely many
balanced semiprimes \(N=pq\), depending on \(K,T\), such that the following
holds simultaneously for every integer

\[
1\le h\le K(n).
\]

None of the Fermat test points

\[
a=\lceil\sqrt{hN}\rceil+j,
\qquad 0\le j\le \lfloor T(n)\rfloor,
\tag{2.2}
\]

has a factor-revealing difference-of-squares representation. Here
"factor-revealing" means that, for

\[
a^2-hN=b^2,
\qquad
u=a-b,\quad v=a+b,
\]

at least one of \(\gcd(u,N),\gcd(v,N)\) is a proper divisor of \(N\).
Using \(T(n)\) rather than \(\lfloor T(n)\rfloor\), or counting the starting
point as the first increment, changes only an inessential additive constant;
the construction below leaves a gap larger than \(T(n)+2\).

### 2.1 A fixed badly approximable target ratio

Set \(\alpha=\sqrt2\). For all positive integers \(c,d\),

\[
\left|\alpha-\frac cd\right|\ge \frac{\gamma}{d^2}
\tag{2.3}
\]

with, for example, \(\gamma=1/5\). Indeed, if \(c/d<3\), then

\[
\left|\sqrt2-\frac cd\right|
=\frac{|2d^2-c^2|}{d^2(\sqrt2+c/d)}
>\frac1{5d^2},
\]

because the numerator is a nonzero integer. If \(c/d\ge3\), the claimed
weaker bound is immediate.

We use the following standard unconditional consequence of the classical
prime number theorem: for every fixed \(A>0\), every sufficiently large
\(x\) has a prime in

\[
\left[x,x+\frac{x}{(\log x)^A}\right].
\tag{2.4}
\]

For completeness, (2.4) follows directly from the classical zero-free-region
error term

\[
\pi(x)=\operatorname{Li}(x)+O\!\left(xe^{-c\sqrt{\log x}}\right).
\]

The main-term change across the interval in (2.4) is asymptotic to
\(x/(\log x)^{A+1}\), which dominates the two endpoint errors.

Choose a fixed \(A>2\kappa\). For every sufficiently large prime \(p\), use
(2.4), with \(x=\alpha p\), to choose a prime \(q\) satisfying

\[
\alpha p\le q\le \alpha p+O\!\left(\frac p{(\log p)^A}\right).
\tag{2.5}
\]

There are infinitely many choices of \(p\), and for large \(p\), (2.5)
gives \(p<q<2p\). Put

\[
r=\frac qp.
\]

Since \(q<2p\), the bit length of \(N=pq\) satisfies
\(n=\Theta(\log p)\). Thus (2.1), (2.5), and the choice \(A>2\kappa\)
imply, for all sufficiently large selected pairs,

\[
|r-\alpha|\le \frac{\gamma}{2K(n)^2}.
\tag{2.6}
\]

Consequently, whenever \(1\le c,d\le K(n)\),

\[
\left|r-\frac cd\right|
\ge \frac{\gamma}{2d^2},
\qquad
\left|r-\frac dc\right|
\ge \frac{\gamma}{2c^2}.
\tag{2.7}
\]

The infinite family is allowed to depend on \(K,T\); in particular, the
accuracy exponent \(A\) was chosen after \(K\) was fixed.

### 2.2 Every allocation \(h=cd\) has a large AM--GM gap

For sufficiently large members of the family,

\[
p>K(n).
\tag{2.8}
\]

Hence \(\gcd(h,N)=1\) for every \(h\le K(n)\). Suppose a representation

\[
hN=u v=(a-b)(a+b)
\tag{2.9}
\]

reveals a proper divisor by a gcd with \(N\). Because \(N=pq\) and
\(\gcd(h,N)=1\), the two primes must be allocated to opposite sides of
(2.9). Therefore, for some positive integers \(c,d\) with \(cd=h\), its
unordered factor pair has one of the two forms

\[
\{u,v\}=\{cp,dq\}
\quad\hbox{or}\quad
\{u,v\}=\{cq,dp\}.
\tag{2.10}
\]

In particular \(c,d\le h\le K(n)\). From (2.7), the first allocation obeys

\[
|cp-dq|=pd\left|\frac cd-r\right|
\ge \frac{\gamma p}{2d}
\ge \frac{\gamma p}{2K(n)},
\tag{2.11}
\]

and the second obeys the same bound with \(c\) in place of \(d\):

\[
|cq-dp|=pc\left|r-\frac dc\right|
\ge \frac{\gamma p}{2K(n)}.
\tag{2.12}
\]

Write \(x,y\) for either allocated pair. Since \(c,d\le K(n)\) and
\(q<2p\),

\[
x+y\le 3K(n)p,
\qquad
(\sqrt x+\sqrt y)^2\le2(x+y)\le6K(n)p.
\tag{2.13}
\]

The exact scaled-Fermat AM--GM identity now gives

\[
\begin{aligned}
\frac{x+y}{2}-\sqrt{xy}
&=\frac{(\sqrt x-\sqrt y)^2}{2}\\
&=\frac{(x-y)^2}{2(\sqrt x+\sqrt y)^2}\\
&\ge \frac{\gamma^2p}{48K(n)^3}.
\end{aligned}
\tag{2.14}
\]

Here \(xy=hN\), and a difference-of-squares representation with factors
\(x,y\) must occur at

\[
a=\frac{x+y}{2}.
\]

Also \(p=2^{\Omega(n)}\), because \(N<2p^2\), whereas \(K(n)^3T(n)\) is
polynomial in \(n\). Thus, for every sufficiently large chosen pair,

\[
\frac{\gamma^2p}{48K(n)^3}>T(n)+2.
\tag{2.15}
\]

Since \(\lceil\sqrt{hN}\rceil<\sqrt{hN}+1\), equations (2.14)--(2.15)
place every factor-revealing value of \(a\) strictly more than \(T(n)+1\)
after the starting point. None occurs in (2.2).

### 2.3 Parity and divisor recovery

No allocation has been silently discarded. An integer difference of squares
has

\[
u=a-b\equiv a+b=v\pmod2.
\]

Because \(p,q\) are odd, a split allocation in (2.10) is parity-compatible
exactly when \(c\equiv d\pmod2\).

* If \(h\) is odd, all its allocations have \(c,d\) odd.
* If \(h\equiv2\pmod4\), no allocation can have equal parity; equivalently,
  \(hN\equiv2\pmod4\) is not a difference of two squares at all.
* If \(4\mid h\), only the allocations with \(c,d\) both even can occur.

The gap proof covered every \(c,d\), so in particular it covered every
parity-compatible allocation. Conversely, if (2.10) occurs, then (2.8)
ensures

\[
\gcd(cp,N)=p,\qquad \gcd(dq,N)=q
\]

or the corresponding swapped identities. Thus taking a gcd of either found
factor of \(hN\) with \(N\) really does recover a proper divisor. If both
\(p,q\) lie on the same side of (2.9), the two gcds are instead \(1\) and
\(N\), so that representation is not factor-revealing under the stated
definition.

The result concerns the complete numerical range \(1\le h\le K(n)\). It
does **not** cover a polynomial-size list of multipliers whose binary
encodings have polynomial length but whose numerical values may be
exponential in \(n\). For such a multiplier, \(c,d\) need not be polynomially
bounded, and neither (2.7) at the needed scale nor the lower bound (2.15)
follows.

## 3. Exact count and the explicit-wheel tradeoff

For an odd prime \(\ell\nmid N\), define

\[
W_\ell=\{t\bmod\ell:t^2-4N\text{ is a square modulo }\ell\},
\]

where zero counts as a square. Let

\[
m=\prod_{i=1}^k\ell_i
\]

be squarefree, with distinct odd primes \(\ell_i\nmid N\), and let

\[
W_m=\{t\bmod m:t\bmod\ell_i\in W_{\ell_i}\text{ for every }i\}.
\]

### 3.1 Exact local count

Over \(\mathbb F_\ell\), consider

\[
f(x)=x+\frac Nx,
\qquad x\in\mathbb F_\ell^\times.
\]

A trace \(t\) lies in the image of \(f\) exactly when

\[
X^2-tX+N
\]

has a root, equivalently when its discriminant \(t^2-4N\) is a square.
Moreover,

\[
f(x)=f(y)
\iff (x-y)(xy-N)=0.
\]

Thus the fibers are precisely the orbits of the involution
\(x\mapsto N/x\). Its fixed points solve \(x^2=N\), so their number is
\(1+\chi_\ell(N)\), where \(\chi_\ell\) is the Legendre symbol. Orbit
counting gives

\[
|W_\ell|
=\frac{(\ell-1)+(1+\chi_\ell(N))}{2}
=\frac{\ell+\chi_\ell(N)}2.
\tag{3.1}
\]

The Chinese remainder theorem then gives the exact formula

\[
|W_m|
=\prod_{\ell\mid m}\frac{\ell+\chi_\ell(N)}2,
\qquad
\frac{|W_m|}{m}
=2^{-k}\prod_{\ell\mid m}\left(1+\frac{\chi_\ell(N)}\ell\right).
\tag{3.2}
\]

In particular, because \(\ell\ge3\),

\[
|W_\ell|\ge\frac{\ell-1}{2}\ge\frac\ell3,
\qquad
|W_m|\ge\frac{m}{3^k}.
\tag{3.3}
\]

If the \(\ell_i\) are put in increasing order, then
\(\ell_i\ge2i+1\), and hence

\[
m\ge\prod_{i=1}^k(2i+1)\ge(k+1)!.
\]

It follows that

\[
k=O\!\left(\frac{\log m}{\log\log m}\right)
\quad\hbox{and}\quad
3^k=m^{o(1)}.
\tag{3.4}
\]

Combining (3.3)--(3.4),

\[
|W_m|=m^{1-o(1)}.
\tag{3.5}
\]

Here and below the assertion is along sequences for which the displayed
scale tends to infinity. The equality in exponent notation means that the
logarithmic exponent tends to one; the elementary lower bound is the part
used below.

### 3.2 The balanced trace interval

Writing \(r=q/p\in(1,2)\),

\[
\frac{s}{\sqrt N}=\sqrt r+\frac1{\sqrt r}.
\]

This function increases from \(2\) to \(3/\sqrt2\) on \((1,2)\). Thus all
balanced traces lie in the consecutive integer interval

\[
I_N=\left\{t\in\mathbb Z:
2\sqrt N<t<\frac3{\sqrt2}\sqrt N\right\},
\]

whose cardinality

\[
L=|I_N|=\left(\frac3{\sqrt2}-2\right)\sqrt N+O(1)
=\Theta(\sqrt N).
\tag{3.6}
\]

The true trace \(s\) is the unique integer in \(I_N\) whose discriminant is
an integer square. Indeed, if \(t^2-4N=y^2\), then \(t,y\) have the same
parity. They cannot both be odd because \(4N\equiv4\pmod8\), so

\[
a=\frac{t-y}{2},\qquad b=\frac{t+y}{2}
\]

are positive integers with \(ab=N\) and \(t=a+b\). The only unordered
factor pairs are \((1,N)\) and \((p,q)\); the first trace \(N+1\) lies well
above \(I_N\), and the second trace is \(s\).

The following two-regime statement is the exact consequence of the local
count.

#### Regime A: the modulus covers the interval, \(m\ge L\)

A literal materialization with one state for each CRT residue in \(W_m\)
has \(|W_m|\) states. Equations (3.3)--(3.4) imply uniformly for \(m\ge L\)
that

\[
|W_m|\ge L^{1-o(1)}.
\tag{3.7}
\]

One elementary way to see the uniformity is to split into
\(L\le m\le L^2\), where (3.4) gives \(3^k=L^{o(1)}\), and \(m>L^2\),
where (3.4) eventually gives \(|W_m|\ge m^{1/2}>L\).

The true trace satisfies

\[
s^2-4N=(q-p)^2,
\]

so \(s\bmod m\in W_m\). Because an interval of cardinality at most \(m\)
contains at most one representative of each residue, an independent uniform
sample from the full set \(W_m\) hits the prescribed trace residue with
probability exactly \(1/|W_m|\). Sampling with replacement therefore takes
expected \(|W_m|=L^{1-o(1)}\) trials. A uniformly random ordering without
replacement takes \((|W_m|+1)/2\) trials on average, which has the same
asymptotic lower bound.

This is specifically uniform sampling from the full CRT wheel. It is not a
claim about a biased sampler or a procedure that can implicitly condition on
the target interval.

#### Regime B: the modulus is shorter than the interval, \(m\le L\)

Let

\[
A_m(I_N)=\#\{t\in I_N:t\bmod m\in W_m\}.
\]

Every residue modulo \(m\) occurs at least \(\lfloor L/m\rfloor\) times in
an interval of \(L\) consecutive integers. Hence

\[
\begin{aligned}
A_m(I_N)
&\ge \left\lfloor\frac Lm\right\rfloor |W_m|\\
&\ge \frac{L}{2m}\,|W_m|\\
&\ge \frac{L}{2\cdot3^k}
=L^{1-o(1)}.
\end{aligned}
\tag{3.8}
\]

For the last equality, if \(m\to\infty\), then (3.4) and \(m\le L\) give
\(3^k=L^{o(1)}\); if \(m\) stays bounded, \(3^k\) is merely a constant.
Therefore a workflow that explicitly visits every accepted lift in the
balanced interval processes \(L^{1-o(1)}\) candidates.

Equations (3.7)--(3.8) give the useful dichotomy:

* if \(m\ge L\), literal CRT-state materialization and unconditioned uniform
  sampling are near-linear in \(L\);
* if \(m\le L\), explicitly listing all wheel-accepted integer lifts is
  near-linear in \(L\).

### 3.3 Why the qualifications are necessary

The three costs cannot all be asserted for every \(m\) without their regime
or workflow qualifications.

First, if \(m=3\) is fixed, literal wheel materialization has only one or two
states, not \(L^{1-o(1)}\) states. The near-linear cost in that regime is the
number of accepted lifts, as in (3.8).

Second, when \(m>L\), the local count (3.2) alone gives no near-linear lower
bound for \(A_m(I_N)\). In fact one can make it equal to one with an enormous,
tailored modulus, using the uniqueness just proved.

For every false \(t\in I_N\setminus\{s\}\), the integer
\(D_t=t^2-4N\) is therefore a nonsquare. A standard consequence of
Dirichlet's theorem for the nonprincipal quadratic character associated with
the squarefree part of \(D_t\) gives infinitely many odd primes \(\ell\nmid N\)
for which \(D_t\) is a quadratic nonresidue modulo \(\ell\). Choose a
different such \(\ell_t\) for every false \(t\), and put

\[
m=\prod_{t\in I_N\setminus\{s\}}\ell_t.
\]

Then every false trace is rejected by at least one local test, while \(s\)
is accepted by every local test. Thus

\[
A_m(I_N)=1.
\]

This tailored \(m\) is vastly larger than \(L\), and constructing it already
used a literal pass over the interval. It is not an efficient factoring
method; it is an exact counterexample to an unconditional claim that every
modulus leaves \(L^{1-o(1)}\) accepted lifts.

Accordingly, the proved result is only an explicit-state/unconditioned-
uniform-sampling obstruction. It says nothing against compressed or implicit
representations of \(W_m\), adaptive selection of auxiliary primes, biased
decoders, interval-conditioned generation, or any other method that avoids
materializing the counted objects. Counting these wheel states is not a
general computational lower bound.

## 4. Scope of the reconstruction

The proved statements are:

1. a polynomial additive trace hint factors a promised balanced semiprime by
   exhaustive exact tests;
2. for each fixed pair \(K,T\) of polynomial numerical bounds, a family
   depending on those bounds defeats every scaled-Fermat search with
   \(h\le K(n)\) and at most \(T(n)\) increments, including every allocation
   and parity case; and
3. CRT trace wheels obey the exact count (3.2) and the explicit two-regime
   near-linear tradeoff (3.7)--(3.8).

None of these statements supplies the trace hint, rules out exponentially
large encoded multipliers, rules out compressed wheel decoding, or factors
arbitrary integers. In particular, they do not establish the top-level
factoring claim in `PROMPT.md`.
