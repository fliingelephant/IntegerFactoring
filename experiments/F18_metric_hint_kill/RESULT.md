# F18 kill-first report: manufactured metric hints from bare \(N\)

**Status:** candidate obstruction. This is the mandatory kill-first pass only. It has
not had a hostile audit or a proof-blind reconstruction.

**Classification:** method failure for two precise mechanisms:

1. scaled Fermat search through all numerical multipliers
   \(k\le \operatorname{poly}(\log N)\), with only
   \(\operatorname{poly}(\log N)\) near-square steps per multiplier; and
2. explicitly materializing or uniformly sampling the CRT wheel of auxiliary-prime
   tests that \(t^2-4N\) is a square.

This is not a lower bound against arbitrary \(N\)-dependent metric-hint generators,
large binary-encoded multipliers chosen without enumeration, implicit interval
decoders, Coppersmith-style partial-information algorithms, or metric information of
a different kind.

## Prior-route check and material difference

The closest prior route is F11/P19, which places the full Boolean multiplication
system in a Euclidean closest-vector instance. F06 also exposes factor bits through a
carry-state search. The present route is materially different: it uses the
one-dimensional Archimedean geometry of the divisor hyperbola and integer
difference-of-squares tests. It introduces no Boolean factor variables, no exact-CVP
oracle, and no terminal computation in a polynomial algebra over
\(\mathbb Z/N\mathbb Z\). A successful certificate ends in an integer square test and
exact division (with a gcd used only to identify which recovered integer factor
contains a prime of \(N\)).

## 1. What a useful metric hint would mean

Let

\[
N=pq,\qquad 2<p<q<2p
\]

be an odd balanced semiprime and put \(s=p+q\). An **additive trace hint of radius
\(B\)** is an integer \(h\) such that

\[
|h-s|\le B.
\]

If \(B=\operatorname{poly}(n)\), where
\(n=\lceil\log_2(N+1)\rceil\), the hint gives a deterministic polynomial-time split:
enumerate the \(2B+1\) integers \(t\) in its interval and test whether

\[
\Delta_t=t^2-4N
\]

is a nonnegative integer square. At \(t=s\),
\(\Delta_t=(q-p)^2\), and

\[
p=\frac{t-\sqrt{\Delta_t}}2,\qquad
q=\frac{t+\sqrt{\Delta_t}}2.
\]

All candidates are verified by exact multiplication. The work uses
\(O(B)\) arithmetic operations on \(O(n+\log(B+1))\)-bit integers.

By contrast, bare \(N\) gives only the lower endpoint \(2\sqrt N\). Even under
\(q<2p\),

\[
2\sqrt N\le s<\frac3{\sqrt2}\sqrt N,
\]

so the unconditional interval still has length \(\Theta(\sqrt N)\). The question is
therefore whether \(N\) can manufacture a much narrower location for \(s\), or an
equivalent approximation to the ratio \(q/p\), without already discovering a
divisor.

## 2. Scaled Fermat is an exact hint-to-factor mechanism

For a positive integer \(k\), set \(M=kN\). Fermat search starts at
\(A_0=\lceil\sqrt M\rceil\) and tests whether \(A^2-M\) is a square as \(A\) increases.
If a divisor allocation \(k=cd\) makes

\[
X=cp,\qquad Y=dq
\]

have the same parity, then

\[
A_* = \frac{X+Y}{2},\qquad
B_* = \frac{|X-Y|}{2},\qquad
A_*^2-B_*^2=kN.
\]

The exact real distance from the square-root threshold is

\[
A_*-\sqrt{kN}
=\frac{(\sqrt X-\sqrt Y)^2}{2}
=\frac{(X-Y)^2}{2(\sqrt X+\sqrt Y)^2}.
\tag{1}
\]

Thus a rational approximation \(c/d\approx q/p\) is precisely a metric hint. If the
right side of (1) is at most \(T=\operatorname{poly}(n)\), the scan finds the
difference of squares in polynomial time. When \(\gcd(k,N)=1\),
\(\gcd(X,N)=p\) and \(\gcd(Y,N)=q\); equivalently one may verify the recovered
integer factors directly.

This is a genuine positive reduction. Its missing step is to manufacture the needed
rational approximation from bare \(N\).

## 3. Obstruction to all polynomially bounded multipliers

### Theorem F18.1

Fix any nondecreasing polynomials \(K(n)\) and \(T(n)\). There are infinitely many odd
balanced semiprimes \(N=pq\) for which no Fermat scan of \(kN\), over any

\[
1\le k\le K(n),
\]

can expose \(p\) or \(q\) within its first \(T(n)\) increments. This remains true if
the method tries every such \(k\), every divisor allocation of \(k\), and ignores
earlier difference-of-squares representations whose recovered factors have trivial
gcd with \(N\).

### Proof

Use the badly approximable target ratio \(\alpha=\sqrt2\). For all positive integers
\(c,d\le K\),

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}
>\frac1{3K},
\tag{2}
\]

because the numerator is a nonzero integer and
\(c+d\sqrt2<(1+\sqrt2)K<3K\).

Classical effective prime-number-theorem bounds imply the following standard fact:
for every fixed \(A>0\), every sufficiently large interval

\[
\left[x-\frac{x}{(\log x)^A},
      x+\frac{x}{(\log x)^A}\right]
\]

contains a prime. (The usual de la Vallée Poussin error term is much smaller than
the interval's main term.) Choose an arbitrarily large prime \(p\), and then a prime
\(q\) in such an interval around \(\sqrt2p\), with \(A\) large enough for the fixed
polynomial \(K\). Since
\(n=\log_2(pq)+O(1)=2\log_2p+O(1)\), this gives, for infinitely many pairs,

\[
\left|\frac qp-\sqrt2\right|
\le \frac1{6K(n)^2}.
\tag{3}
\]

For large \(p\), these are distinct odd primes and \(p<q<3p/2\). Combining (2) and
(3), for every \(c,d\le K(n)\),

\[
\left|c-d\frac qp\right|
\ge |c-d\sqrt2|-d\left|\frac qp-\sqrt2\right|
>\frac1{6K(n)}.
\tag{4}
\]

Now fix \(k\le K(n)\). Since \(p,q>K(n)\), we have \(\gcd(k,N)=1\). Any integer
factorization \(XY=kN\) for which \(\gcd(X,N)\) is proper must put exactly one of
\(p,q\) into \(X\). Hence, after possibly swapping \(X,Y\) and \(p,q\),

\[
X=cp,\qquad Y=dq,\qquad cd=k,
\]

with \(c,d\le K(n)\). Equation (4) gives

\[
|X-Y|\ge \frac{p}{6K(n)}.
\]

Also \(X,Y<\tfrac32K(n)p\), and consequently

\[
(\sqrt X+\sqrt Y)^2<6K(n)p.
\]

Substitution in (1) yields

\[
\frac{X+Y}{2}-\sqrt{kN}
>\frac{p}{432K(n)^3}.
\tag{5}
\]

The integer scan distance is at least the right side of (5) minus 1. But
\(p=2^{n/2+O(1)}\), whereas \(K,T\) are fixed polynomials. For all sufficiently
large members of the family,

\[
\frac{p}{432K(n)^3}-1>T(n).
\]

Thus no difference-of-squares representation capable of splitting \(N\) occurs in
the scanned range, for any \(k\le K(n)\). \(\square\)

### Scope of F18.1

The theorem kills a complete natural workflow, not the general metric-hint question.
In particular, a polynomial-time algorithm may write down a multiplier with
\(\operatorname{poly}(n)\) bits but exponentially large numerical value, without
enumerating all smaller multipliers. F18.1 does not exclude an \(N\)-dependent rule
that chooses polynomially many such large multipliers and proves one of them useful.
Showing that no such rule exists would be a complexity lower bound and is not claimed.

## 4. A bare-\(N\) square-residue wheel and its explicit-state obstruction

There is a factor-free way to manufacture exact public constraints on the trace
\(s=p+q\). For an odd auxiliary prime \(\ell\nmid N\), define

\[
W_\ell(N)
=\left\{x+Nx^{-1}:x\in\mathbb F_\ell^\times\right\}.
\]

Then

\[
t\in W_\ell(N)
\quad\Longleftrightarrow\quad
t^2-4N\text{ is a square in }\mathbb F_\ell.
\tag{6}
\]

The true trace belongs to this set because
\(s^2-4N=(q-p)^2\). This is not a computation over \(\mathbb Z/N\mathbb Z\), and a
survivor is checked by an integer square test rather than a zero-divisor gcd.

The involution \(x\mapsto N/x\) has two fixed points when \(N\) is a quadratic residue
modulo \(\ell\), and none otherwise. Every other orbit has size two, and (6) has no
larger fibers over the field. Hence

\[
|W_\ell(N)|=\frac{\ell+\left(\frac N\ell\right)}2.
\tag{7}
\]

For a squarefree product of \(k\) distinct odd auxiliary primes,

\[
m=\prod_{i=1}^k\ell_i,
\]

CRT gives the exact wheel

\[
W_m(N)=\prod_{i=1}^kW_{\ell_i}(N),
\qquad
|W_m(N)|
=\prod_{i=1}^k\frac{\ell_i+\left(\frac N{\ell_i}\right)}2.
\tag{8}
\]

Each prime supplies roughly one bit of rejection, but it also enlarges the CRT state
space. Since \((\ell_i-1)/(2\ell_i)\ge1/3\),

\[
|W_m(N)|\ge \frac{m}{3^k}.
\tag{9}
\]

Distinct odd primes satisfy
\(m\ge (k+2)!/2\), so

\[
k=O\!\left(\frac{\log m}{\log\log m}\right).
\]

Consequently

\[
|W_m(N)|
\ge m\exp\!\left(-O\!\left(\frac{\log m}{\log\log m}\right)\right)
=m^{1-O(1/\log\log m)}.
\tag{10}
\]

For balanced factors the public interval containing \(s\) has length
\(L=\Theta(\sqrt N)=2^{\Theta(n)}\). If \(m\ge L\), explicitly constructing the
wheel already materializes \(L^{1-o(1)}\) or more residue classes. A uniform sample
from those classes hits the one class \(s\bmod m\) with probability at most
\(1/|W_m(N)|=2^{-\Omega(n)}\). If \(m\le L/2\), every accepted residue has at least
\(L/(2m)\) lifts in any interval of length \(L\), so an explicit candidate scan has at
least

\[
\frac{L}{2\cdot3^k}=L^{1-o(1)}
\]

candidates. For \(L/2<m<L\), the wheel list itself still has \(L^{1-o(1)}\) entries.

Thus local square tests do manufacture valid public information, but the literal CRT
wheel neither produces a polynomial-radius metric hint nor gives a polynomial-time
sampler for the true trace.

### Scope of the wheel obstruction

Equations (7)--(10) are representation and sampling bounds for the explicit wheel.
They do not rule out an implicit decoder that finds the few integers in a target
interval without listing all CRT classes, nor an exact interval-counting method for
the simultaneous character conditions. Proving such a decoder polynomial-time would
be materially new; asserting that it is hard would merely restate the missing step.

## 5. Surviving result and next missing lemma

The useful positive statement is exact:

> A polynomial-radius approximation to \(p+q\), or a polynomial-step scaled-Fermat
> rational approximation to \(q/p\), gives a verified split using only integer metric
> computations.

The two obvious bare-\(N\) manufacturers do not meet it. Polynomially bounded
multipliers fail on an infinite balanced semiprime family (F18.1), while explicit
auxiliary-prime square wheels retain \(L^{1-o(1)}\) state on a trace interval of
length \(L\).

The next decisive lemma must be one of the following, stated constructively rather
than as a hardness premise:

1. an explicit \(N\)-dependent rule producing
   \(\operatorname{poly}(n)\) binary-encoded rational multipliers, one of which has
   polynomial Fermat distance for every composite \(N\), with a proved selection or
   success bound; or
2. a uniform implicit interval decoder for the constraints
   \(t^2-4N\in(\mathbb F_{\ell_i})^2\) that runs in
   \(\operatorname{poly}(n)\) bit operations and returns the integer-square survivor
   with inverse-polynomial probability, without enumerating the CRT wheel.

No finite computation was used in this report, so there is no computation manifest.
