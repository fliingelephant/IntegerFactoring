# F18 hostile audit: manufactured metric hints

**Audited candidate:** experiments/F18_metric_hint_kill/RESULT.md

**Audit status:** survives with corrections. The two exact obstructions are valid,
but only at the candidate's deliberately narrow interfaces. In particular, this
report proves no lower bound against an implicit decoder or an \(N\)-dependent list
of large binary-encoded multipliers.

**Computation:** none. This is a proof-only audit, so there is no run manifest.

## 1. Verdict and required corrections

The following mathematical core survives.

1. On an odd balanced semiprime, an additive
   \(\operatorname{poly}(\log N)\)-radius hint for \(p+q\) gives a deterministic
   polynomial-time split by integer square tests.
2. For every fixed pair of eventual positive polynomial bounds \(K(n),T(n)\),
   there are infinitely many balanced semiprimes on which every numerical
   multiplier \(k\le K(n)\) has every factor-revealing Fermat representation more
   than \(T(n)\) increments from the square-root threshold.
3. For a squarefree product \(m\) of \(k\) distinct odd auxiliary primes not
   dividing \(N\), the literal CRT wheel has at least
   \(m^{1-O(1/\log\log m)}\) residue classes. Enumerating its classes, uniformly
   sampling a class when \(m\) covers the trace interval, or scanning every lift
   when it does not, takes exponentially many states or trials on a balanced
   trace interval.

Four wording repairs are necessary.

- The multiplier theorem is **per fixed \(K,T\)**. Its adversarial infinite
  family may depend on their degrees and coefficients. It does not exhibit one
  family defeating every polynomial at once.
- A difference-of-squares output gives \(X=A-B\), \(Y=A+B\) with \(XY=kN\).
  Unless \(k=1\), these are not themselves generally factors of \(N\). The
  factor-free recovery step is
  \(\gcd(X,N)\) (or \(\gcd(Y,N)\)), followed by exact division and multiplication
  verification. Alternatively, if a divisor allocation \(k=cd\) is separately
  known, one can test \(X/c,Y/d\). The candidate's phrase “verify the recovered
  integer factors directly” is otherwise misleading.
- A “useful rational multiplier” must mean positive integers \(c,d\), with
  \(cd=k\), such that \(cp\) and \(dq\) have the same parity and the resulting
  **actual Fermat representation** has polynomial threshold distance. A bare
  rational approximation without these integrality and parity conditions is not
  by itself the promised scan certificate.
- The wheel conclusion is an output-size and uniform-sampling obstruction for
  the literal representation. It is not a running-time lower bound for a
  compressed character-condition solver, a biased \(N\)-dependent sampler, or an
  interval decoder.

Subject to those repairs, no candidate theorem must be retracted.

## 2. Positive metric-hint reductions

Let \(N=pq\), \(2<p<q<2p\), and \(s=p+q\). Given an integer \(h\) and an explicit
bound \(B\) satisfying \(|h-s|\le B\), enumerate the integers in
\([h-B,h+B]\). For each \(t\), compute the exact integer square root of
\(\Delta_t=t^2-4N\), reject if it is negative or nonsquare, and otherwise test

\[
u=(t-\sqrt{\Delta_t})/2,\qquad v=(t+\sqrt{\Delta_t})/2
\]

when integral. At \(t=s\), these are \(p,q\). Every returned pair is checked by
\(uv=N\), so false candidates cause no correctness problem. If
\(B=\operatorname{poly}(n)\), this takes \(O(B)\) integer-square-root and
multiplication operations on \(O(n+\log(B+1))\)-bit values, hence polynomial bit
complexity by standard deterministic integer arithmetic.

The public balanced interval is genuinely exponential in bit length. Writing
\(r=q/p\in(1,2)\),

\[
\frac{s}{\sqrt N}=\sqrt r+\frac1{\sqrt r}
\]

lies in \([2,3/\sqrt2)\), and the possible interval has length
\((3/\sqrt2-2)\sqrt N=\Theta(\sqrt N)=2^{\Theta(n)}\).

For scaled Fermat, put \(X=cp\), \(Y=dq\), \(cd=k\), and assume \(X,Y\) have the
same parity. Then

\[
A_* - \sqrt{kN}
=\frac{X+Y}{2}-\sqrt{XY}
=\frac{(\sqrt X-\sqrt Y)^2}{2}
=\frac{(X-Y)^2}{2(\sqrt X+\sqrt Y)^2}.
\]

Thus an actual allocation whose displayed distance is polynomial gives a
polynomial-step scan. When \(\gcd(k,N)=1\), a factor-revealing allocation has
\(\gcd(X,N)\in\{p,q\}\), so the scan ends in a verified gcd-derived split. All
identities and the bit-length claim here are correct.

## 3. Hostile reconstruction of the bounded-multiplier obstruction

Fix eventual positive nondecreasing polynomial bounds \(K,T\). It is harmless to
replace them by integer ceilings. Let \(D=\deg K\); for some constant \(C\),
\(K(n)\le Cn^D\) for all sufficiently large \(n\).

For positive \(c,d\le K\), irrationality of \(\sqrt2\) and integrality give

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}
>\frac1{3K}.
\tag{A1}
\]

The analytic input used by the candidate is standard and unconditional: the
de la Vallée Poussin form of the prime number theorem implies, for every fixed
\(A>0\), that every sufficiently large interval

\[
[x-x/(\log x)^A,\;x+x/(\log x)^A]
\tag{A2}
\]

contains a prime. Indeed the main term in the difference of prime-counting
functions is \(\asymp x/(\log x)^{A+1}\), while the classical error
\(O(xe^{-c\sqrt{\log x}})\) is smaller. This is a named standard theorem, not a
web-derived or conjectural premise.

Take arbitrarily large primes \(p\), apply (A2) at \(x=\sqrt2p\), and choose \(A>2D\).
For all sufficiently large choices, any resulting prime \(q\) obeys
\(p<q<3p/2\), and its input length satisfies
\(n\le 2\log_2p+O(1)\). After increasing the threshold to absorb \(C\) and the
change of logarithm base, the interval width yields

\[
\left|\frac qp-\sqrt2\right|\le\frac1{6K(n)^2}.
\tag{A3}
\]

This resolves the apparent circularity that \(K\) is evaluated at the bit length
of the not-yet-chosen \(q\). Since there are arbitrarily large prime \(p\), the
construction gives infinitely many distinct odd balanced semiprimes.

For \(c,d\le K(n)\), (A1)--(A3) imply

\[
\left|c-d\frac qp\right|
\ge |c-d\sqrt2|-d\left|\frac qp-\sqrt2\right|
>\frac1{6K(n)}.
\tag{A4}
\]

Eventually \(p,q>K(n)\). Fix \(k\le K(n)\), and let \(XY=kN\) be any positive
factorization for which \(\gcd(X,N)\) is proper. Because \(\gcd(k,N)=1\), exactly
one of \(p,q\) lies in each side. After relabeling the two coefficient variables,

\[
X=cp,\qquad Y=dq,\qquad cd=k,\qquad c,d\le K(n).
\]

The alternative orientation \(X=cq,Y=dp\) is covered by interchanging \(c,d\) in
(A4). Hence

\[
|X-Y|>\frac{p}{6K(n)}.
\]

Also \(X,Y<(3/2)K(n)p\), so the deliberately loose bound
\((\sqrt X+\sqrt Y)^2<6K(n)p\) holds. Therefore every factor-revealing
representation satisfies

\[
\frac{X+Y}{2}-\sqrt{kN}
>\frac{p}{432K(n)^3}.
\tag{A5}
\]

If \(A_0=\lceil\sqrt{kN}\rceil\), its integer scan index is at least the right side
of (A5) minus \(1\). Meanwhile

\[
p=2^{n/2+O(1)},
\]

whereas \(K(n)^3T(n)\) is polynomial. Thus (A5) exceeds \(T(n)+1\) for all
sufficiently large members of the constructed family. This covers every divisor
allocation and is stronger than needed because it did not use the same-parity
restriction. Earlier representations with gcd \(1\) or \(N\) do not affect the
claim, because the theorem explicitly permits the scan to ignore them.

This proves the corrected bounded-multiplier theorem. It says nothing about a
polynomial-size list of multipliers of numerical magnitude
\(2^{\operatorname{poly}(n)}\): their binary representations and the arithmetic
on \(kN\) can still have polynomial length.

## 4. Hostile reconstruction of the CRT-wheel obstruction

Let \(\ell\nmid N\) be an odd prime and

\[
f_\ell(x)=x+Nx^{-1}\quad(x\in\mathbb F_\ell^\times).
\]

The equivalence

\[
t\in\operatorname{im}f_\ell
\iff t^2-4N\text{ is a square in }\mathbb F_\ell
\tag{A6}
\]

is exact. The forward direction uses
\((x-Nx^{-1})^2\); in the reverse direction the roots of
\(X^2-tX+N\) are nonzero because \(N\not\equiv0\pmod\ell\).

Moreover

\[
f_\ell(x)=f_\ell(y)
\iff x=y\text{ or }xy=N.
\]

Thus its fibers are precisely the orbits of \(x\mapsto N/x\). That involution has
two fixed points if \((N/\ell)=1\) and none if \((N/\ell)=-1\), giving

\[
|W_\ell(N)|=\frac{\ell+(N/\ell)}2.
\tag{A7}
\]

For \(m=\prod_{i=1}^k\ell_i\) with distinct such primes, CRT makes the conditions
independent as a Cartesian product, so

\[
|W_m(N)|=\prod_i\frac{\ell_i+(N/\ell_i)}2
\ge \frac{m}{3^k}.
\tag{A8}
\]

The inequality uses
\((\ell_i-1)/(2\ell_i)\ge1/3\). On ordering the distinct odd primes, the weak but
sufficient estimate \(\ell_i\ge i+2\) gives

\[
m\ge\frac{(k+2)!}{2}.
\]

Stirling's bound then yields

\[
k=O\!\left(\frac{\log m}{\log\log m}\right),
\qquad
|W_m(N)|\ge
m\exp\!\left(-O\!\left(\frac{\log m}{\log\log m}\right)\right).
\tag{A9}
\]

These are valid for arbitrary choices of the distinct auxiliary primes; no
equidistribution assumption is present.

Let \(I\) be the public balanced trace interval and let its integer-point count be
\(L=\Theta(\sqrt N)=2^{\Theta(n)}\). The candidate's three cases are exhaustive.

- If \(m\ge L\), literal wheel materialization has at least
  \(L^{1-o(1)}\) classes. A uniform class sample selects the particular class
  \(s\bmod m\) with probability exactly \(1/|W_m(N)|=2^{-\Omega(n)}\).
- If \(m\le L/2\), each residue class has at least
  \(\lfloor L/m\rfloor\ge L/(2m)\) representatives in \(I\). Explicitly scanning
  all accepted lifts therefore examines at least
  \(|W_m(N)|L/(2m)\ge L/(2\cdot3^k)=L^{1-o(1)}\) integers.
- If \(L/2<m<L\), (A9) already gives
  \(|W_m(N)|=L^{1-o(1)}\).

For the first case, the lower-bound function in (A9) is eventually increasing, so
replacing \(m\) by its lower bound \(L\) is legitimate. For the second,
\(m\le L\) and the factorial bound imply
\(k=O(\log L/\log\log L)\), which justifies the displayed \(L^{1-o(1)}\) rather
than merely asserting it.

These counts do **not** show that every accepted candidate must be individually
tested. Simultaneous character conditions might admit an implicit interval
algorithm, and an \(N\)-dependent nonuniform sampler might place far more mass on
the true residue. Neither exists in the candidate, but neither is refuted by its
counting theorem. The candidate states this boundary correctly.

## 5. Exact surviving theorem

The candidate should be retained in the following form.

> **Corrected F18 obstruction.** A known polynomial-radius trace hint, or an
> actual polynomial-distance scaled-Fermat representation with the required
> integrality and parity, deterministically splits an odd balanced semiprime in
> polynomial bit complexity. Conversely, for every fixed pair of polynomial
> bounds \(K,T\), infinitely many odd balanced semiprimes defeat the workflow that
> enumerates all numerical \(k\le K(n)\) and scans \(T(n)\) Fermat increments.
> Also, for squarefree products of distinct odd auxiliary primes, the literal CRT
> square-residue wheel has \(L^{1-o(1)}\) explicit state or lift candidates on a
> balanced trace interval of length \(L=\Theta(\sqrt N)\). None of these facts
> excludes polynomially many \(N\)-dependent, exponentially large numerical
> multipliers encoded in polynomially many bits, biased sampling, or a compressed
> interval decoder.

This is a method failure for the two stated workflows, not evidence that bare \(N\)
cannot manufacture some other metric side information. It supplies no top-level
factoring algorithm.
