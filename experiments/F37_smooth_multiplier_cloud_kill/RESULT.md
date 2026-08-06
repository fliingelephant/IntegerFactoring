# F37 kill-first result: a smooth multiplier cloud loses to its own Fermat scale

**Status:** promoted as P47 after a first hostile audit required quantifier and
scope amendments, the amended whole artifact passed fresh hostile re-audit,
and a context-free proof-blind reconstruction succeeded. No computation was
used.

**Closest prior route.** X20/P26 proves failure when every *numerical*
multiplier \(k\leq\operatorname{poly}(n)\) is scanned. F37 is materially
different: one may write a much larger \(k\) in polynomially many bits, supply
its complete factorization, and let one Fermat scan pool all allocations
\(k=cd\) without enumerating the divisors.

P29/X23 identifies an exact or polynomial-additive factor-trace oracle as
promise-factoring-equivalent; it does not settle F37, whose proposed output is
a factor pair of \(kN\) followed by an integer gcd, not an explicitly evaluated
trace observable.

The result below proves:

1. an exact logarithmic ratio condition for a useful allocation;
2. a divisor-density versus \(k^{1/4}\) theorem ruling out a target-independent
   uniform all-real-ratio cover by one or polynomially many multiplier clouds;
3. an infinite family of actual odd semiprimes defeating **every** coprime
   multiplier with \(o(\sqrt n)\) bits, even when the multiplier is chosen
   adaptively from \(N\); and
4. no impossibility claim for general adaptive \(N\)-dependent multipliers with
   \(\Omega(\sqrt n)\), linear, or larger polynomial bit length.

Item 3 extends the small-numerical-\(k\) part of P26, but it does not close
the full F37 proposal.

## 1. Useful and useless factorizations of \(kN\)

Let

\[
N=pq,\qquad 2<p<q,
\]

where \(p,q\) are distinct odd primes. Suppose first that
\(\gcd(k,N)=1\). Every positive factor pair \(XY=kN\) has exactly one of
the following two types.

* **Split, hence useful.** The unknown primes lie on opposite sides. After
  exchanging the sides if necessary,

  \[
  X=cp,\qquad Y=dq,\qquad cd=k.
  \]

  Then

  \[
  \gcd(X,N)=p,\qquad \gcd(Y,N)=q.
  \]

  The swapped allocation \(X=cq,Y=dp\) is the same case with \(c,d\)
  exchanged.

* **Unsplit, hence useless.** Both unknown primes lie on one side. After
  exchanging the sides,

  \[
  X=cN,\qquad Y=d,\qquad cd=k,
  \]

  and the two intersections with \(N\) are \(N\) and \(1\).

An early square found by Fermat can therefore be useless. A valid algorithm may
continue the scan after checking

\[
\gcd(A-B,N),\qquad \gcd(A+B,N),
\]

but only split allocations count as successes.

There is no loss in restricting the genuinely new cloud analysis to
\(\gcd(k,N)=1\). If \(k\) comes with its complete prime factorization and

\[
1<\gcd(k,N)<N,
\]

that gcd already splits \(N\). If \(\gcd(k,N)=N\), the supplied prime-factor
list of \(k\) contains both \(p\) and \(q\); gcding its listed primes with
\(N\) again splits \(N\). Thus a non-coprime “multiplier success” has
manufactured an unknown prime before Fermat begins. It is not an
allocation-cloud success.

Parity also matters. Fermat's factors \(A-B,A+B\) have the same parity. Since
\(p,q\) are odd, a split allocation is representable only when

\[
c\equiv d\pmod 2.
\]

Thus odd \(k\) has only odd/odd allocations,
\(k\equiv2\pmod4\) has no difference-of-squares representation, and when
\(4\mid k\), only allocations giving at least one factor \(2\) to each side
are compatible. All upper bounds below deliberately count every divisor
allocation, including parity-incompatible ones, so parity can only strengthen
the obstruction.

## 2. Exact Fermat-gap condition

Put

\[
r=\frac qp,\qquad M=kN,\qquad
\lambda=\log\frac{c/d}{r}.
\]

For the split allocation \(X=cp,Y=dq\),

\[
XY=M,\qquad \frac XY=e^\lambda.
\]

Consequently, up to exchanging \(X,Y\),

\[
X=\sqrt M e^{\lambda/2},\qquad
Y=\sqrt M e^{-\lambda/2}.
\]

If \(X,Y\) have the same parity, their Fermat point is

\[
A_*=\frac{X+Y}{2}
   =\sqrt M\cosh\!\left(\frac\lambda2\right),
\]

and the exact real gap above the square-root threshold is

\[
G_k(r;c)
=A_*-\sqrt M
=\sqrt{kN}\left(
  \cosh\!\left(\frac12\log\frac{c/d}{r}\right)-1
 \right).
\tag{1}
\]

Equivalently,

\[
G_k(r;c)
=\frac{(cp-dq)^2}
       {2(\sqrt{cp}+\sqrt{dq})^2}.
\tag{2}
\]

Let

\[
\theta_M=\lceil\sqrt M\rceil-\sqrt M\in[0,1).
\]

The scan starts at \(A_0=\lceil\sqrt M\rceil\). The exact scan index of this
allocation is

\[
j=A_*-A_0=G_k(r;c)-\theta_M.
\]

Hence a parity-compatible allocation occurs among indices \(0,\ldots,T\) if
and only if

\[
\left|\log\frac{c/d}{r}\right|
\leq
2\operatorname{arcosh}\!\left(
1+\frac{T+\theta_M}{\sqrt{kN}}
\right).
\tag{3}
\]

Replacing \(\theta_M<1\) gives the useful necessary bound

\[
\left|\log\frac{c/d}{r}\right|
\leq
2\sqrt2\,\frac{\sqrt{T+1}}{(kN)^{1/4}},
\tag{4}
\]

because \(\cosh x\geq1+x^2/2\). Thus the divisor cloud grows when \(k\)
acquires more divisors, but every cloud point simultaneously loses resolution
by \(k^{-1/4}\).

## 3. No polynomial list gives a uniform all-ratio cover

The following is a geometric covering theorem. It tests the proposed strong
lemma “the known allocation cloud covers every possible \(q/p\)” directly.
It does **not** turn the discrete prime-ratio problem into a lower bound for an
adaptive factoring algorithm.

### Theorem 1 (continuous necessary-window bound)

Fix a product scale \(S>0\), a log-ratio interval \(I\subset\mathbb R\) of
length \(\ell>0\), positive integers \(k_1,\ldots,k_m\), and nonnegative
integer scan caps \(T_1,\ldots,T_m\). Define

\[
R_i=2\sqrt2\,\frac{\sqrt{T_i+1}}{(k_iS)^{1/4}}
\]

and the continuous necessary-window surrogate

\[
\mathcal C=
\bigcup_{i=1}^m\ \bigcup_{c\mid k_i}
\left[
  2\log c-\log k_i-R_i,\,
  2\log c-\log k_i+R_i
\right].
\]

Even if every divisor allocation is declared parity-compatible,

\[
\operatorname{meas}(I\cap\mathcal C)
\leq
4\sqrt2\,S^{-1/4}
\sum_{i=1}^m
\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\tag{5}
\]

Every actual parity-compatible useful factor pair of an integer \(S=N\)
found through scan index \(T_i\) has \(\log(q/p)\in\mathcal C\) by (4).
Consequently a single list intended to provide these necessary windows for
**every** ratio in \(I\), with the list fixed independently of the target
point in \(I\), must satisfy

\[
\ell
\leq
4\sqrt2\,S^{-1/4}
\sum_{i=1}^m
\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\tag{6}
\]

#### Proof

For fixed \(k_i\), the possible logarithmic centers are

\[
\log(c/d)=2\log c-\log k_i,
\qquad c\mid k_i,\quad d=k_i/c.
\]

There are exactly \(\tau(k_i)\) of them. By (3)--(4), every actual useful pair
at product scale \(S\) lies in the interval about its center having radius at
most

\[
2\operatorname{arcosh}\!\left(
1+\frac{T_i+1}{\sqrt{k_iS}}
\right)
\leq
2\sqrt2\,\frac{\sqrt{T_i+1}}{(k_iS)^{1/4}}.
\]

The measure of a union is at most the sum of its interval lengths. Summing
twice this radius over all centers and all multipliers gives (5), and a
necessary-window cover of \(I\) must have measure at least \(\ell\).
\(\square\)

The divisor function cannot compensate for \(k^{-1/4}\). For every fixed
\(\varepsilon>0\), there is a constant \(C_\varepsilon\) such that

\[
\tau(k)\leq C_\varepsilon k^\varepsilon.
\tag{7}
\]

Here is a self-contained proof. If \(k=\prod_p p^{e_p}\), then
\(\tau(k)=\prod_p(e_p+1)\). For \(p\geq2^{1/\varepsilon}\),

\[
e+1\leq2^e\leq p^{\varepsilon e}.
\]

For each of the finitely many smaller primes,
\(\sup_{e\geq0}(e+1)p^{-\varepsilon e}<\infty\). Multiplying those finitely
many suprema proves (7). Consequently

\[
\tau(k)k^{-1/4}=k^{-1/4+o(1)}.
\tag{8}
\]

Taking \(\varepsilon=1/8\) gives a uniform constant \(C\) with

\[
\tau(k)k^{-1/4}\leq Ck^{-1/8}\leq C.
\tag{9}
\]

Therefore suppose there are fixed constants \(C_0,D>0\), independent of
\(n,S,i\), such that

\[
m(n)\leq C_0n^D,
\qquad
0\leq T_i(n)\leq C_0n^D
\quad(1\leq i\leq m(n)).
\]

For each \(n,S\), the multiplier list may depend on \(n,S\), but one list is
fixed independently of the particular target point in \(I\). If
\(S=2^{\Theta(n)}\), the right side of (5) is

\[
\operatorname{poly}(n)S^{-1/4}=2^{-\Theta(n)}.
\]

It cannot cover even a fixed balanced interval such as

\[
\log r\in[\log(4/3),\log(3/2)].
\]

This geometric conclusion is independent of how large the \(k_i\) are.
Larger smooth multipliers have more allocations, but asymptotically only
\(k_i^{o(1)}\) of them, while the necessary resolution shrinks as
\(k_i^{-1/4}\). Polynomial encoded length is needed only when these windows
are interpreted as scans executed by a polynomial-time algorithm.

For a common cap \(T\), (6) also gives the explicit necessary tradeoff

\[
T+1\geq
\frac{\ell^2\sqrt S}
{32\left(\sum_i\tau(k_i)k_i^{-1/4}\right)^2}.
\tag{10}
\]

For one multiplier the exact bound is

\[
T+1\geq
\frac{\ell^2\sqrt{kS}}{32\tau(k)^2}
\tag{11}
\]

For fixed \(\ell>0\), this is
\(\sqrt S\,k^{1/2-o(1)}\) up to a fixed positive multiplicative factor as
\(k\to\infty\). For bounded \(k\), (11) itself is the statement.

For a polynomial-size list, (9) reduces (10) to

\[
T=\Omega\!\left(\frac{\sqrt S}{\operatorname{poly}(n)}\right),
\]

which is exponential in \(n\). This is the structural reason that
“exponentially many implicit allocations” does not imply adequate Fermat
resolution.

### A natural constructive cloud and why its growth loses

Let

\[
L_m=\operatorname{lcm}(1,2,\ldots,m),\qquad k_m=L_m^2.
\]

For every \(a,b\leq m\), both \(a,b\) divide \(L_m\), and

\[
c=L_m\frac ab,\qquad d=L_m\frac ba
\]

are integers satisfying \(cd=k_m\). Thus the cloud contains every ratio

\[
\frac cd=\left(\frac ab\right)^2.
\]

On \(1\leq r\leq2\), take

\[
b=\left\lfloor\frac{m-2}{\sqrt2}\right\rfloor,
\qquad
a=\operatorname{round}(b\sqrt r).
\]

For all sufficiently large \(m\), one has \(1\leq a,b\leq m\), and the
mean-value theorem on this compact interval gives, uniformly in \(r\),

\[
\left|2\log(a/b)-\log r\right|=O(1/m).
\]

Thus this is a genuine constructive paired-factor cloud with an
\(O(1/m)\) log mesh.

However, Chebyshev's bounds give

\[
\log L_m=\Theta(m),\qquad \log k_m=\Theta(m).
\]

Its guaranteed mesh improves only polynomially in \(m\), while a successful
polynomial-length scan requires the nearest-center error to be at most

\[
O\!\left(N^{-1/4}k_m^{-1/4}\sqrt{T+1}\right),
\qquad
k_m^{-1/4}=\exp(-\Theta(m)).
\]

The full cloud cannot repair this discrepancy: Theorem 1 counts all
\(\tau(k_m)\) allocations, not merely the displayed constructive subcloud.

## 4. An actual semiprime obstruction beyond P26

Theorem 1 refutes a uniform continuum-covering lemma, but an adaptive algorithm
choosing \(k=k(N)\) needs to hit only the ratio encoded by its input. The next
theorem is deliberately narrower and does handle adaptivity: it defeats all
multipliers whose binary length is \(o(\sqrt n)\). It makes no claim above that
range.

### Theorem 2 (all \(o(\sqrt n)\)-bit multipliers fail on one infinite family)

Fix functions

\[
B:\mathbb N\to\mathbb R_{\geq0},
\qquad
T:\mathbb N\to\mathbb Z_{\geq0},
\]

such that \(B(n)/\sqrt n\to0\) and \(T(n)\) is bounded above by one fixed
polynomial. There are infinitely many distinct odd balanced semiprimes

\[
N=pq,\qquad p<q<2p,
\]

such that the following holds simultaneously for every integer \(k\) with

\[
\log_2 k\leq B(n),\qquad \gcd(k,N)=1.
\]

The conventional binary length \(\lfloor\log_2k\rfloor+1\) differs from
\(\log_2k\) by at most one, so this is exactly the same
\(o(\sqrt n)\)-bit regime. The infinite family may depend on the two fixed
functions \(B,T\).

No useful factor pair of \(kN\) occurs through Fermat scan index \(T(n)\):
every parity-compatible useful pair has index greater than \(T(n)\), and every
other useful pair is not a difference of two integer squares. The multiplier
may be selected adaptively as an arbitrary function of \(N\), and its
factorization may be supplied for free.

Equivalently, on this family every such multiplier either intersects \(N\)
nontrivially—and its known factorization already exposes a prime—or its smooth
allocation cloud gives no useful split within the polynomial scan.

#### Proof

Use the classical de la Vallée Poussin prime-number-theorem error term

\[
\pi(x)=\operatorname{Li}(x)
       +O\!\left(xe^{-a\sqrt{\log x}}\right)
\]

for some \(a>0\). Choosing any smaller positive exponent shows that, for all
sufficiently large \(x\), the interval

\[
\left[x-xe^{-b\sqrt{\log x}},
      x+xe^{-b\sqrt{\log x}}\right]
\]

contains a prime. Indeed, its main-term prime count is
\(\asymp xe^{-b\sqrt{\log x}}/\log x\), which dominates the two endpoint
errors when \(0<b<a\).

Take arbitrarily large primes \(p\), apply this at \(x=\sqrt2p\), and choose a
prime \(q\) in the displayed interval. The resulting semiprimes are balanced
and, for a fixed \(\gamma>0\), satisfy

\[
\left|\frac qp-\sqrt2\right|
\leq e^{-\gamma\sqrt n}
\tag{12}
\]

for all sufficiently large members, because \(n=\Theta(\log p)\).

Put \(K=2^{B(n)}\). Since \(B(n)=o(\sqrt n)\), (12) eventually gives

\[
\left|\frac qp-\sqrt2\right|\leq\frac1{6K^2}.
\tag{13}
\]

Let \(k\leq K\) and \(cd=k\). Irrationality of \(\sqrt2\) and integrality give

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}
>\frac1{3k},
\tag{14}
\]

because \(c,d\leq k\). Writing \(r=q/p\), equations (13)--(14) imply

\[
|c-dr|
\geq |c-d\sqrt2|-d|r-\sqrt2|
>\frac1{3k}-\frac1{6k}
=\frac1{6k}.
\tag{15}
\]

Indeed, \(d|r-\sqrt2|\leq1/(6k)\) follows from \(d\leq k\leq K\) and
\(k^2\leq K^2\). Exchanging \(c,d\) gives the same bound for the swapped
orientation.

For a useful allocation \(X=cp,Y=dq\), (15) yields

\[
|X-Y|=p|c-dr|>\frac p{6k}.
\]

Also \(X+Y<3kp\), and hence

\[
(\sqrt X+\sqrt Y)^2\leq2(X+Y)<6kp.
\]

Using (2), every useful allocation has

\[
A_*-\sqrt{kN}>\frac p{432k^3}.
\tag{16}
\]

Now \(\log p=\Theta(n)\), whereas \(\log k=o(\sqrt n)\). Therefore

\[
\frac p{432k^3}>T(n)+1
\]

eventually. Since the integer scan index is greater than the real gap minus
one, it exceeds \(T(n)\). This bound covered all allocations; discarding the
parity-incompatible ones changes nothing. \(\square\)

For example, Theorem 2 covers every fixed bit-length bound

\[
\log_2 k=O(n^\alpha),\qquad \alpha<\frac12,
\]

including numerical multipliers far larger than any polynomial in \(n\).

## 5. Bit complexity, ratio range, and the exact surviving gap

If \(k\) has \(b\) bits, then \(kN\), every scanned \(A\), the square
\(A^2-kN\), its exact square root, and all gcd operands have
\(O(n+b+\log(T+1))\) bits. A represented scan family has polynomial total
bit complexity provided that (i) its list has uniformly polynomial
cardinality, (ii) the total encoding of each multiplier together with its
supplied complete factorization has polynomial length, (iii) producing that
represented list, when it is not supplied as input, costs polynomial time,
and (iv) all scan caps are bounded by one uniform polynomial. Standard
integer multiplication, ceiling-square-root, subtraction, exact-square
testing, and gcd algorithms then give polynomial total work. The
exponentially many divisors are not enumerated; the square test genuinely
pools them. Merely asserting short multiplier values does not pay for an
unspecified rule which manufactures their complete factorizations.

The obstruction is geometric, not an omitted divisor-enumeration cost. In
terms of \(b=\log_2 k+O(1)\), one multiplier's total ratio-measure
contribution in (5), apart from the common
\(N^{-1/4}\sqrt{T+1}\), is

\[
\tau(k)k^{-1/4}=2^{-b/4+o(b)}.
\]

Thus increasing the intermediate length from \(n\) to \(n+b\) makes the
aggregate cloud coverage exponentially smaller in \(b\), despite the maximal
divisor count.

The ratio range creates a second pressure. Since

\[
\frac cd=\frac{c^2}{k}\in[1/k,k],
\]

a multiplier meant to cover ratios as large as \(R\) needs \(k\geq R\) merely
to reach them. Increasing \(k\) then tightens every Fermat window by
\(k^{-1/4}\), while its number of windows grows only as \(k^{o(1)}\).
Theorem 1 fails already on a fixed balanced ratio interval, before unbalanced
inputs are considered.

A successful useful scan on an arbitrary composite would return

\[
1<\gcd(A-B,N)<N
\]

or the analogous gcd with \(A+B\). If an almost-surely terminating splitter
with expected cost at most \(P(s)\) were proved for **every** composite
\(s\)-bit input, replace \(P\) if necessary by the nondecreasing polynomial
majorant

\[
P^*(n)=\max_{s\leq n}P(s).
\]

Deterministic primality testing plus fresh recursive calls on \(d\) and
\(N/d\) gives at most \(n\) prime leaves and \(n-1\) split nodes, because
every prime factor is at least \(2\). Conditioning on the history before each
reached call, expectations sum to at most \((2n-1)P^*(n)\), plus polynomial
exact-division, primality, and output-verification cost. The recursion contains
only finitely many reached calls, so almost-sure termination of each call
implies almost-sure termination of the whole recursion. This covers even
inputs, repeated factors, and prime powers. A positive theorem only for
distinct semiprimes does not supply the required every-composite splitter.
For the negative direction, an infinite distinct-odd-semiprime family is
enough to refute a claimed universal guarantee within Theorem 2's direct
useful-pair multiplier range.

The exact boundary is:

* **Killed:** a target-independent uniform all-real-ratio necessary-window
  cover by one or polynomially many known-factorization multipliers and
  polynomial Fermat scans, regardless of multiplier magnitude; and, on the
  constructed semiprime family, the direct useful-square/gcd extraction method
  for every multiplier of \(o(\sqrt n)\) bits, even under adaptive selection.
* **Not killed:** a polynomial-time rule which uses \(N\) to choose one or a
  polynomial list of multipliers with \(\Omega(\sqrt n)\) (in particular
  \(O(n)\) or larger polynomial) bits and proves that the cloud hits the actual
  discrete prime ratio \(q/p\); or an algorithm which jointly decodes
  nonsquare scan residues or several complete scan transcripts without
  requiring any individually useful factor pair. The measure theorem cannot
  be applied after the cloud is allowed to depend on the input whose ratio it
  must hit.

Any retry of the direct useful-pair route must therefore supply a genuinely
adaptive concentration theorem for the actual prime ratio, not a statement
that smoothness or a large divisor count makes the allocation ratios uniformly
dense. A genuinely joint transcript decoder is materially different and
remains open.
