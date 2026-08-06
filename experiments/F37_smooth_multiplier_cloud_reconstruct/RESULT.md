# Independent reconstruction: smooth multiplier clouds

All logarithms are natural unless a base is displayed. A factor pair means a
pair of positive integers. For a positive integer \(M\), the ordinary Fermat
scan is

\[
A_j=\lceil\sqrt M\rceil+j,\qquad j=0,1,2,\ldots,
\]

with a hit when \(A_j^2-M=B^2\) for an integer \(B\geq0\).

## 1. Factor-pair classification, parity, and exact gap

Let \(N=pq\), where \(p<q\) are distinct odd primes, and suppose a complete
prime factorization of \(k\) is known. First compute \(g=\gcd(k,N)\). If
\(1<g<N\), this already splits \(N\). If \(g=N\), the displayed prime
factorization of \(k\) contains a prime divisor of \(N\), so it also splits
\(N\). Thus only \(\gcd(k,N)=1\) is relevant to the multiplier argument.

Put \(M=kN\). In any ordered factorization \(XY=M\), each of \(p,q\) occurs
in exactly one of \(X,Y\), while the prime powers belonging to \(k\) can be
distributed between them. Consequently, up to reversing \(X,Y\), precisely
the following cases occur, with \(cd=k\):

\[
(X,Y)=(cp,dq),\qquad(cq,dp),\qquad(cN,d).
\]

In the first two cases the gcds with \(N\) are respectively \((p,q)\) and
\((q,p)\); in the last case they are \((N,1)\). Thus the first two cases are
the useful split pairs and the last case is unsplit. No coprimality between
\(c\) and \(d\) is needed.

Parity is essential. A pair \(X\leq Y\) is represented by the Fermat scan if
and only if \(X\equiv Y\pmod2\), because then and only then

\[
A=(X+Y)/2,\qquad B=(Y-X)/2
\]

are integers. Since \(p,q,N\) are odd, compatibility is equivalent to
\(c\equiv d\pmod2\). Hence:

* if \(k\) is odd, every such pair is compatible;
* if \(k\equiv2\pmod4\), no pair is compatible, consistently with an integer
  congruent to \(2\pmod4\) not being a difference of two squares;
* if \(4\mid k\), a pair is compatible exactly when the chosen distribution
  has \(c,d\) both even.

Now consider a useful allocation \(X=cp,\ Y=dq\), \(cd=k\), and set

\[
r=\frac qp,\qquad
\lambda=\log\frac{c/d}{r}=\log\frac{cp}{dq}.
\]

Since \(XY=M\), write \(X=\sqrt M e^{\lambda/2}\) and
\(Y=\sqrt M e^{-\lambda/2}\). Its real Fermat gap is exactly

\[
\begin{aligned}
G&=\frac{X+Y}{2}-\sqrt M
 =\sqrt{kN}\bigl(\cosh(\lambda/2)-1\bigr)\\
 &=\frac{(\sqrt X-\sqrt Y)^2}{2}
 =\frac{(cp-dq)^2}{2(\sqrt{cp}+\sqrt{dq})^2}.
\end{aligned}
\tag{1}
\]

The formula is invariant under interchanging the two factors, which sends
\(\lambda\) to \(-\lambda\).

Suppose the pair is parity-compatible and define

\[
\theta=\lceil\sqrt M\rceil-\sqrt M\in[0,1).
\]

Its scan index is the integer

\[
j=\frac{X+Y}{2}-\lceil\sqrt M\rceil=G-\theta.
\]

Thus for every \(T\geq0\), monotonicity of \(\cosh\) on \([0,\infty)\)
gives the exact equivalence

\[
j\leq T
\quad\Longleftrightarrow\quad
|\lambda|\leq
2\operatorname{arcosh}\!\left(1+\frac{T+\theta}{\sqrt{kN}}\right).
\tag{2}
\]

There is no scan index to which (2) applies for an incompatible pair.
Finally, \(\cosh u\geq1+u^2/2\) and \(\theta<1\) imply the necessary bound

\[
|\lambda|
\leq2\sqrt2\,\sqrt{T+1}\,(kN)^{-1/4}.
\tag{3}
\]

## 2. Continuous necessary-window theorem

Let \(\rho=\log r\), let \(I\subset\mathbb R\) be an interval of length
\(\ell\), and fix target-independent multipliers \(k_i\) and scan caps
\(T_i\geq0\). For a lower size bound \(N\geq S>0\), define

\[
R_i=2\sqrt2\,\sqrt{T_i+1}\,(k_iS)^{-1/4}
\]

and

\[
\mathcal C=
\bigcup_i\ \bigcup_{c\mid k_i}
\left[
2\log c-\log k_i-R_i,\,
2\log c-\log k_i+R_i
\right].
\]

For a useful allocation, define \(c\) to be the coefficient attached to
\(p\), and put \(d=k_i/c\). Then

\[
\lambda=2\log c-\log k_i-\rho.
\]

If this pair is reached by scan \(T_i\), (3) and \(N\geq S\) force
\(\rho\in\mathcal C\). This also covers the swapped allocation: name the
coefficient attached to \(p\) as \(c\); equivalently, the divisor set is
closed under \(c\leftrightarrow k_i/c\).

Subadditivity of Lebesgue measure gives

\[
\begin{aligned}
\operatorname{meas}(I\cap\mathcal C)
&\leq\sum_i2\tau(k_i)R_i\\
&=4\sqrt2\,S^{-1/4}
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\end{aligned}
\tag{4}
\]

In particular, a necessary condition for these windows to cover all of
\(I\) is the covering/scan tradeoff

\[
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}
\geq\frac{\ell S^{1/4}}{4\sqrt2}.
\tag{5}
\]

Writing \(w_i=\tau(k_i)k_i^{-1/4}\), Cauchy--Schwarz also gives

\[
\sum_i(T_i+1)
\geq\frac{\ell^2S^{1/2}}{32\sum_iw_i^2}.
\tag{6}
\]

These are necessary conditions, not sufficiency statements: a point in a
window can still fail because of parity or because the exact arcosh window is
smaller.

### Self-contained divisor bound

For every fixed \(\varepsilon>0\), there is \(C_\varepsilon<\infty\) such
that

\[
\tau(k)\leq C_\varepsilon k^\varepsilon\qquad(k\geq1).
\tag{7}
\]

Indeed, factor \(k=\prod p^{a_p}\). For
\(p\geq2^{1/\varepsilon}\), the elementary inequality
\(a+1\leq2^a\) gives \(a+1\leq p^{\varepsilon a}\). There are only
finitely many smaller primes, and for each of them

\[
C_{p,\varepsilon}
=\sup_{a\geq0}(a+1)p^{-\varepsilon a}<\infty
\]

because an exponential dominates a linear function. Multiplication over the
finitely many small primes, with
\(C_\varepsilon=\prod C_{p,\varepsilon}\), proves (7).

Now let the list and every cap be bounded by one fixed polynomial:

\[
m(n)\leq P(n),\qquad T_i(n)\leq P(n).
\]

Take \(\varepsilon=1/8\). Since \(k_i\geq1\), (7) gives

\[
\tau(k_i)k_i^{-1/4}
\leq C_{1/8}k_i^{-1/8}\leq C_{1/8}.
\]

If \(S(n)\geq2^{\alpha n}\) for some fixed \(\alpha>0\) and all large
\(n\), the right side of (4) is at most

\[
4\sqrt2C_{1/8}\,2^{-\alpha n/4}
P(n)\sqrt{P(n)+1}=o(1).
\]

It therefore cannot cover any interval whose length is bounded below by a
fixed positive constant. This conclusion is independent of the magnitudes
of the multipliers.

## 3. The lcm construction and its loss

Let

\[
L_m=\operatorname{lcm}(1,2,\ldots,m),\qquad k_m=L_m^2.
\]

For \(m\geq6\) and \(1\leq r\leq2\), put

\[
b=\left\lfloor\frac{m-2}{\sqrt2}\right\rfloor,\qquad
a=\operatorname{round}(b\sqrt r).
\]

Either choice at a rounding tie is harmless. We have

\[
b\geq m/4,\qquad b\leq b\sqrt r\leq m-2,\qquad
|a-b\sqrt r|\leq\tfrac12.
\]

It follows that \(1\leq a,b\leq m\), so both divide \(L_m\). Hence

\[
c=L_m\frac ab,\qquad d=L_m\frac ba
\]

are positive integers and \(cd=L_m^2=k_m\). Moreover

\[
\frac cd=\left(\frac ab\right)^2.
\]

Writing \(t=b\sqrt r\), one has

\[
\left|\log\frac at\right|\leq\frac1b
\]

because \(|a/t-1|\leq1/(2b)\) and
\(|\log(1+u)|\leq|u|/(1-|u|)\). Therefore the literal uniform log-mesh
bound is

\[
\left|\log\frac{(c/d)}r\right|
=2\left|\log\frac{a}{b\sqrt r}\right|
\leq\frac2b\leq\frac8m.
\tag{8}
\]

On the other hand,

\[
\log L_m=\psi(m)=m+o(m)
\]

by the prime number theorem; the weaker Chebyshev estimate
\(\psi(m)=\Theta(m)\) suffices. Consequently

\[
k_m^{-1/4}=L_m^{-1/2}=\exp(-\Theta(m)).
\tag{9}
\]

Thus the \(O(1/m)\) center approximation in (8) does not imply a short
Fermat scan. To make a window radius comparable with \(1/m\) already has
the scale

\[
T+1\asymp\frac{L_mS^{1/2}}{m^2},
\]

which is exponential in \(m\) when \(S\) is bounded below by a positive
constant. More invariantly, even using every divisor center, (7) with
\(\varepsilon=1/8\) gives

\[
\tau(k_m)k_m^{-1/4}
\leq C_{1/8}k_m^{-1/8}
=C_{1/8}L_m^{-1/4}=\exp(-\Theta(m)).
\]

So polynomial scan caps leave exponentially vanishing total necessary-window
measure. The construction is a genuine mesh construction; the
\(k^{-1/4}\) gap scaling is precisely why it loses. It makes no independent
parity guarantee.

## 4. Adaptive short multipliers

Fix any functions

\[
B:\mathbb N\to\mathbb R_{\geq0},\qquad
T:\mathbb N\to\mathbb Z_{\geq0}
\]

such that \(B(n)/\sqrt n\to0\) and \(T(n)\) is bounded by a fixed
polynomial. We prove that there are infinitely many products \(N=pq\) of
distinct odd primes, with \(q/p\) bounded above and below by positive
constants, such that, for

\[
n=\lceil\log_2(N+1)\rceil,
\]

the following holds simultaneously for every positive integer \(k\): if
\(\gcd(k,N)=1\) and \(\log_2k\leq B(n)\), no parity-compatible useful
factor pair of \(kN\) occurs at a Fermat index \(j\leq T(n)\). The universal
quantifier over \(k\) permits \(k\) to be selected after \(N\) is known.

### Prime ratios exponentially close to \(\sqrt2\)

The classical de la Vallee Poussin error term says that, for some \(A>0\),

\[
\pi(x)=\operatorname{Li}(x)
+O\!\left(xe^{-A\sqrt{\log x}}\right).
\tag{10}
\]

It implies that for some \(a>0\), every sufficiently large interval

\[
[x-h,x+h],\qquad h=xe^{-a\sqrt{\log x}},
\tag{11}
\]

contains a prime. To see this directly, choose \(a\) smaller than the error
exponent in (10). The difference of the two logarithmic-integral main terms
is asymptotic to \(2h/\log x\), whereas the combined errors are
\(O(xe^{-A'\sqrt{\log x}})\) for some \(A'>a\). The error/main-term ratio
tends to zero, so the prime-count difference is positive.

Take any sequence of odd primes \(p\to\infty\), apply (11) at
\(x=\sqrt2p\), and choose a prime \(q\) in that interval. For all large
\(p\),

\[
p<q<2p,\qquad
\delta:=\left|\frac qp-\sqrt2\right|
\leq Ce^{-a'\sqrt{\log p}}
\tag{12}
\]

for fixed positive constants \(C,a'\). These are distinct odd balanced
semiprimes. Since \(p^2<N<2p^2\), their bit lengths satisfy

\[
n=2\log_2p+O(1).
\tag{13}
\]

After decreasing a constant and discarding finitely many terms, (12)--(13)
give

\[
\delta\leq e^{-\gamma\sqrt n}
\tag{14}
\]

for some fixed \(\gamma>0\). Because \(B(n)=o(\sqrt n)\), all sufficiently
large members of this sequence satisfy

\[
\delta\leq\frac1{6\,2^{2B(n)}}.
\tag{15}
\]

This is where the exact \(o(\sqrt n)\) multiplier-length threshold enters.

### Uniform Diophantine separation and transfer

For all positive integers \(c,d\), with \(k=cd\),

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}
>\frac1{3cd}=\frac1{3k}.
\tag{16}
\]

Indeed, the numerator is a nonzero integer and
\(c+d\sqrt2<3cd\). The same statement holds after interchanging \(c,d\).

Let \(k\leq2^{B(n)}\). From (15), \(c,d\leq k\), and
\(k^2\leq2^{2B(n)}\), (16) gives simultaneously

\[
\begin{aligned}
|c-d(q/p)|
&\geq|c-d\sqrt2|-d\delta>\frac1{6k},\\
|d-c(q/p)|
&\geq|d-c\sqrt2|-c\delta>\frac1{6k}.
\end{aligned}
\tag{17}
\]

The first line handles \(cp,dq\); the second handles the swapped allocation
\(cq,dp\).

For either allocation, (17) makes the factor difference larger than
\(p/(6k)\). Also \(c,d\leq k\) and \(q<2p\), so

\[
2(\sqrt{cp}+\sqrt{dq})^2<12kp
\]

in the first allocation, and the identical bound holds with \(p,q\) swapped
between \(c,d\). The exact gap identity therefore gives

\[
G>\frac{p^2/(36k^2)}{12kp}
=\frac{p}{432k^3}.
\tag{18}
\]

The constants are uniform over every allowed \(k,c,d\).

For completeness, (13) can be made into the explicit lower bound

\[
p>\frac{2^{n/2}}{\sqrt6}
\]

for all large members of the sequence: use \(N+1<3p^2\) and the definition
of \(n\). Hence, uniformly for \(k\leq2^{B(n)}\),

\[
\frac{p}{432k^3}
>\frac{2^{n/2-3B(n)}}{432\sqrt6}
>T(n)+1
\tag{19}
\]

for all sufficiently large selected \(N\). The last inequality follows
because \(B(n)=o(\sqrt n)\), while \(T\) is polynomial.

Finally, if a useful pair is parity-incompatible, it is absent from the
Fermat scan. If it is compatible, its index satisfies

\[
j=G-\theta>T(n)+1-\theta>T(n),
\]

because \(0\leq\theta<1\). In fact \(kN\) is nonsquare under
\(\gcd(k,N)=1\), so \(\theta>0\), but only the upper bound is needed.
This proves the claimed simultaneous adaptive theorem, including the swapped
allocation and the integer-index conclusion.

## 5. Representation, recursion, and exact scope

“Known complete factorization of \(k\)” is not a zero-cost oracle in a
uniform algorithm. An explicit list must account for:

* generation and storage of every multiplier and its prime-power
  factorization encoding;
* the number and bit lengths of the listed primes and exponents;
* generation or enumeration of any divisor centers actually used; and
* all operands in multiplication, square testing, and gcd computations.

Even if a factorization with binary-encoded exponents is a compressed
description, explicitly forming \(M=kN\) and an ordinary Fermat scan operand
requires \(\Theta(n+\log_2k)\) bits. Thus a polynomial-bit-complexity
implementation of this literal scan must keep those operand lengths
polynomial; a symbolic compressed representation does not remove this cost
unless a different, fully analyzed algorithm replaces the integer scan. The
continuous estimate above is stronger in one respect: its failure of
polynomial-size, polynomial-cap continuous coverage does not depend on
\(\log k_i\) at all.

There is a standard conditional reduction from an **every-composite**
splitter to complete factorization, but it must not be inferred from a
semiprime-only statement. If a Las Vegas routine split every composite
\(m\)-bit integer in expected time \(P(m)\), recursively apply it after a
polynomial-time primality test. Define the nondecreasing polynomial majorant
\[
P^*(n)=\max_{1\leq s\leq n}P(s);
\]
it is polynomially bounded because \(P\) is. There are at most
\(\log_2N<n\) prime factors counted with multiplicity, hence fewer than
\(n\) split calls, and every operand has at most \(n\) bits. Thus every
conditional expected split cost is at most \(P^*(n)\), and linearity of
expectation gives \(O(nP^*(n))\) expected splitter time plus polynomial
bookkeeping. A finite sequence of almost-surely terminating calls terminates
almost surely. This reduction is valid only under the every-composite
hypothesis, which has not been established here.

The proved scope is therefore precise:

* (4)--(7) obstruct target-independent continuous multiplier clouds with a
  polynomial list and polynomial scan caps on any fixed positive log
  interval when \(S=2^{\Theta(n)}\). This is only a continuous
  necessary-window obstruction, not an adaptive discrete factoring lower
  bound.
* The constructed semiprime family additionally defeats direct
  useful-square/factor-pair/gcd extraction through a polynomial Fermat cap
  for **every** coprime adaptive multiplier of \(o(\sqrt n)\) bits, even
  when the multiplier is selected after seeing \(N\). Early unsplit hits
  have only trivial/full intersections with \(N\).
* The argument does not rule out adaptive multipliers of
  \(\Omega(\sqrt n)\) bits, concentration on actual prime ratios outside
  the proved short-multiplier regime, joint decoding from nonsquare values
  or a larger transcript, other metric observables, or any different
  factoring mechanism. In particular it proves no all-input factoring
  lower bound and leaves all-input classical factoring open.

RECONSTRUCTED
