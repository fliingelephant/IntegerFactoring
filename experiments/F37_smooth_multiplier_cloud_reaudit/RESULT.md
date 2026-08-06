# F37 fresh hostile re-audit: amended smooth multiplier cloud obstruction

**Artifact audited:** `experiments/F37_smooth_multiplier_cloud_kill/RESULT.md`

**Audit posture:** fresh whole-artifact hostile proof audit. I read
`AGENTS.md`, `PROMPT.md`, the F15 row of `REGISTRY.md`, P26, X20, the amended
candidate, and the first hostile audit in full. The first audit was used only
as a checklist for amendments A1--A7; its mathematical verdict was not
assumed.

**Computation:** none. This report is proof-only.

## Verdict

> **PASS AS WRITTEN.**

The amended artifact proves exactly two scoped obstructions:

1. A multiplier list fixed independently of the target log-ratio cannot make
   polynomially many polynomial-radius necessary Fermat windows cover a fixed
   positive-length real interval, irrespective of the numerical sizes of the
   multipliers.
2. For every fixed multiplier-bit bound \(B(n)=o(\sqrt n)\) and fixed
   polynomial scan bound \(T(n)\), an infinite balanced-semiprime family
   simultaneously defeats every coprime \(k\) with
   \(\log_2 k\le B(n)\) under direct useful-square/gcd extraction, including
   multipliers selected after seeing \(N\).

I found no false implication, missing case, constant error, or remaining
quantifier inflation. The candidate explicitly leaves open adaptive
\(\Omega(\sqrt n)\)-bit multipliers, concentration on the actual discrete
prime ratio, and joint decoding of nonsquare or multi-scan transcripts. It
does not claim a factoring lower bound or a solution to the top-level task.

## Required-amendment check

Every amendment required by the first audit is literally and consistently
present.

### A1: continuous surrogate and actual-pair implication

Theorem 1 now defines

\[
\mathcal C=\bigcup_i\bigcup_{c\mid k_i}
 [2\log c-\log k_i-R_i,\,2\log c-\log k_i+R_i]
\]

for arbitrary real product scale \(S>0\). It calls this a *continuous
necessary-window surrogate*, not the literal set of integer factorizations at
that scale. It separately states the valid bridge: when \(S=N\) is an integer,
every actual parity-compatible useful pair found through the specified scan
index has \(\log(q/p)\in\mathcal C\). Thus the measure theorem is not being
silently applied to nonexistent factor pairs at arbitrary real ratios.

### A2: target independence and uniform polynomial quantifiers

The candidate fixes constants \(C_0,D>0\), independent of \(n,S,i\), and
requires

\[
m(n)\le C_0n^D,
\qquad T_i(n)\le C_0n^D.
\]

It also says that the list may depend on \(n,S\), but is fixed independently
of the particular target point in \(I\). This is exactly the quantifier order
needed for the union-measure argument. No encoded-length hypothesis is used
in the geometric theorem; encoded length enters only in the later algorithmic
cost discussion.

### A3: equation (11) asymptotics

The exact inequality is retained:

\[
T+1\ge
\frac{\ell^2\sqrt{kS}}{32\tau(k)^2}.
\]

The shorthand \(\sqrt S\,k^{1/2-o(1)}\) is explicitly qualified as
\(k\to\infty\), with a fixed positive factor suppressed, and the bounded-
\(k\) case is directed back to the exact formula.

### A4: literal LCM mesh

The candidate gives the literal choices

\[
b=\left\lfloor\frac{m-2}{\sqrt2}\right\rfloor,
\qquad a=\operatorname{round}(b\sqrt r),
\]

which keep \(1\le a,b\le m\) for all sufficiently large \(m\) and uniformly
for \(1\le r\le2\). It also states the correct success requirement for the
nearest-center error,

\[
O\!\left(N^{-1/4}k_m^{-1/4}\sqrt{T+1}\right),
\]

rather than describing \(k_m^{-1/4}\) by itself as a radius.

### A5: fixed \(B,T\) and bit-length convention

Theorem 2 declares fixed functions

\[
B:\mathbb N\to\mathbb R_{\ge0},
\qquad T:\mathbb N\to\mathbb Z_{\ge0},
\]

with \(B(n)/\sqrt n\to0\) and \(T\) bounded by one fixed polynomial. The
family may depend on these functions. It explicitly notes that
\(\log_2 k\) and conventional binary length differ by at most one, so the
claimed \(o(\sqrt n)\)-bit regime is literal.

### A6: represented-list generation and recursive cost

Section 5 requires uniform polynomial list cardinality, polynomial total
encoding length for each multiplier and its complete factorization,
polynomial-time generation when the list is not supplied, and one uniform
polynomial scan cap. It does not charge only for scan arithmetic while leaving
multiplier/factorization generation unspecified.

The conditional splitter-to-complete-factorization reduction uses the
nondecreasing polynomially bounded majorant

\[
P^*(n)=\max_{s\le n}P(s),
\]

bounds the recursion by at most \(n\) leaves and \(n-1\) split nodes, invokes
fresh calls, sums conditional expectations, and explicitly proves
almost-sure termination from the finite number of reached almost-surely
terminating calls.

### A7: direct useful-square/gcd scope

Both the theorem discussion and final boundary say that Theorem 2 obstructs
only a direct method whose success requires an individually useful Fermat
square followed by intersection with \(N\). Nonsquare residues, complete scan
transcripts, joint decoding across multipliers, and other metric observables
are expressly open.

## Independent mathematical audit

### 1. Factor-pair classification, gcd preprocessing, and parity

Let \(N=pq\) with distinct odd primes and \(\gcd(k,N)=1\). Unique
factorization assigns \(p,q\) either to opposite sides of \(XY=kN\), giving
after relabeling

\[
X=cp,\qquad Y=dq,\qquad cd=k,
\]

or to the same side, giving

\[
X=cN,\qquad Y=d,\qquad cd=k.
\]

The former intersects \(N\) in \(p,q\); the latter intersects it in \(N,1\).
These cases are exhaustive. The swapped useful orientation is obtained by
exchanging the roles of \(c,d\), so no allocation is omitted.

For noncoprime \(k\), \(1<\gcd(k,N)<N\) already splits the semiprime. If
\(N\mid k\), the promised complete prime-factor list of \(k\) contains both
\(p\) and \(q\), and gcding listed primes with \(N\) exposes them. The
candidate therefore does not count hidden factor access as a cloud success.

A difference-of-squares pair \(A-B,A+B\) has equal parity. Since \(p,q\) are
odd, a useful allocation is representable exactly when \(c\equiv d\pmod2\).
Thus odd \(k\) permits odd/odd allocations, \(v_2(k)=1\) permits none, and
\(v_2(k)\ge2\) requires powers of two on both sides. Counting all divisors in
an upper bound is safe because it only adds parity-incompatible centers.

### 2. Exact Fermat index and necessary log window

For \(r=q/p\), \(M=kN\), and

\[
\lambda=\log\frac{c/d}{r},
\]

a useful allocation satisfies \(XY=M\) and \(X/Y=e^\lambda\). Up to exchange,

\[
X=\sqrt M e^{\lambda/2},
\qquad Y=\sqrt M e^{-\lambda/2}.
\]

For equal parity, \(A_*=(X+Y)/2\) is an integer and

\[
G=A_*-\sqrt M
=\sqrt M\bigl(\cosh(\lambda/2)-1\bigr)
=\frac{(X-Y)^2}{2(\sqrt X+\sqrt Y)^2}.
\]

Writing \(A_0=\lceil\sqrt M\rceil\) and
\(\theta_M=A_0-\sqrt M\in[0,1)\), the exact scan index is
\(j=A_*-A_0=G-\theta_M\). Since \(A_*\ge\sqrt M\) and is integral, it is
indeed at least \(A_0\); no negative-index case is hidden. Solving \(j\le T\)
gives equation (3) exactly.

If \(x=\operatorname{arcosh}(1+u)\), then
\(u=\cosh x-1\ge x^2/2\), so \(x\le\sqrt{2u}\). With
\(u=(T+\theta_M)/\sqrt{kN}\), this yields the necessary bound

\[
\left|\log\frac{c/d}{r}\right|
\le 2\sqrt2\frac{\sqrt{T+1}}{(kN)^{1/4}}.
\]

The direction is used correctly: after replacing \(\theta_M\) by \(1\), the
candidate claims necessity, not sufficiency.

### 3. Continuous measure theorem and constants

For fixed \(k_i\), the centers are
\(2\log c-\log k_i\) for \(c\mid k_i\), hence there are exactly
\(\tau(k_i)\) counted centers. Each interval has radius

\[
R_i=2\sqrt2\,(T_i+1)^{1/2}(k_iS)^{-1/4}.
\]

Summing interval lengths \(2R_i\), with overlaps only reducing measure, gives

\[
\operatorname{meas}(I\cap\mathcal C)
\le4\sqrt2 S^{-1/4}
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\]

Thus the constant in (5) is correct. If one target-independent list supplies
necessary windows for every point of \(I\), then \(I\subseteq\mathcal C\),
giving (6).

The divisor estimate is also uniform. For fixed \(\varepsilon>0\), primes
\(p\ge2^{1/\varepsilon}\) obey
\(e+1\le2^e\le p^{\varepsilon e}\). Each of the finitely many smaller primes
has finite
\(\sup_{e\ge0}(e+1)p^{-\varepsilon e}\), and multiplying these finitely many
suprema gives one constant independent of \(k\). Hence

\[
\tau(k)\le C_\varepsilon k^\varepsilon,
\qquad
\tau(k)k^{-1/4}=k^{-1/4+o(1)}.
\]

At \(\varepsilon=1/8\), every multiplier contributes at most one fixed
constant before the common \(S^{-1/4}\sqrt{T_i+1}\) factor. A uniformly
polynomial list with uniformly polynomial caps therefore has total measure
\(\operatorname{poly}(n)S^{-1/4}=2^{-\Theta(n)}\) when
\(S=2^{\Theta(n)}\), too small for a fixed positive-length interval. This
argument is independent of multiplier magnitude, but crucially not of the
target point; the candidate keeps that distinction.

With common cap \(T\), squaring (6) gives

\[
T+1\ge
\frac{\ell^2\sqrt S}
{32(\sum_i\tau(k_i)k_i^{-1/4})^2},
\]

because \((4\sqrt2)^2=32\). For one multiplier this becomes equation (11),
including its factor \(\sqrt k\). No sign or reciprocal is reversed.

### 4. LCM cloud

For (L_m=\operatorname{lcm}(1,\ldots,m)) and (k_m=L_m^2), the displayed

\[
c=L_m a/b,\qquad d=L_m b/a
\]

are integers whenever \(a,b\le m\), satisfy \(cd=k_m\), and have
\(c/d=(a/b)^2\). The concrete rounding choice keeps \(a,b\le m\). Since
(|a-b\sqrt r|\le1/2), and (a/b,\sqrt r) stay in a fixed compact positive
interval, the logarithm is Lipschitz there and the log-mesh error is
(O(1/m)) uniformly.

Chebyshev's standard bounds give (\log L_m=\Theta(m)), so
(k_m^{-1/4}=\exp(-\Theta(m))). The displayed rational subcloud alone does
not prove that other divisors fail, but the candidate does not make that
mistake: Theorem 1 already counts all (\tau(k_m)) centers, and
(\tau(k_m)=k_m^{o(1)}) cannot offset the (k_m^{-1/4}) penalty in a uniform
continuum cover.

### 5. Prime-pair family and simultaneous adaptive multipliers

The cited de la Vallée Poussin estimate

\[
\pi(x)=\operatorname{Li}(x)+O(xe^{-a\sqrt{\log x}})
\]

does imply a prime in
([x-xe^{-b\sqrt{\log x}},x+xe^{-b\sqrt{\log x}}]) for any fixed
(0<b<a) and all sufficiently large (x). The main-term difference is
asymptotic to (2xe^{-b\sqrt{\log x}}/\log x), whereas the total endpoint
error is (O(xe^{-a\sqrt{\log x}})); their ratio tends to zero.

Take (x=\sqrt2p) along arbitrarily large primes (p). The interval is
eventually contained in ((p,2p)), so its prime (q) is distinct, odd, and
balanced. Since

\[
n=\log_2(pq)+O(1)=2\log_2p+O(1),
\]

one fixed (\gamma>0) gives

\[
|q/p-\sqrt2|\le e^{-\gamma\sqrt n}
\]

on all sufficiently large family members.

Let (K=2^{B(n)}). Because (B(n)=o(\sqrt n)), the last estimate is
eventually at most (1/(6K^2)). This is one bound fixed before (k) is
chosen, so all following estimates hold simultaneously for every
(1\le k\le K), not merely for a preselected multiplier.

For every (cd=k), irrationality of (\sqrt2) gives

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}
>\frac1{3k},
\]

because the numerator is a nonzero integer and (c,d\le k). Also

\[
d|q/p-\sqrt2|
\le\frac{d}{6K^2}
\le\frac1{6k},
\]

using (d\le k\le K). Therefore

\[
|c-d(q/p)|>\frac1{6k}.
\]

Exchanging (c,d) supplies the identical estimate needed for the swapped
orientation (X=cq,Y=dp). Thus every useful allocation satisfies

\[
|X-Y|>\frac p{6k},
\qquad X+Y<3kp,
\qquad (\sqrt X+\sqrt Y)^2<6kp.
\]

Substitution in the exact gap identity gives

\[
G>\frac{p^2/(36k^2)}{12kp}
=\frac p{432k^3}.
\]

The constant (432) is therefore correct. Uniformly over (k\le K),

\[
\log\frac p{432k^3}
\ge \frac{\log2}{2}n-3(\log2)B(n)-O(1)
=\Theta(n),
\]

which exceeds (\log(T(n)+1)=O(\log n)). Hence (G>T+1) eventually. Since
(j=G-\theta_M>G-1), the exact integer scan index satisfies (j>T).
Parity-incompatible pairs are not differences of integer squares, so all
useful cases are covered.

The theorem quantifies over every eligible coprime (k) before any adaptive
selection. It therefore covers deterministic selections, randomized
selections pointwise, and polynomial lists in this size regime. If a selected
multiplier is noncoprime, gcd preprocessing or its promised factorization has
already exposed a prime; that is correctly separated from a Fermat-cloud hit.

### 6. Cost and scope

For a (b)-bit multiplier, the scanned integers and all arithmetic operands
have (O(n+b+\log(T+1))) bits. Under the represented-list conditions already
listed under A6, polynomially many scans with polynomial caps use polynomial
bit complexity. The candidate does not enumerate divisors and does not need
to: each square test pools all factor pairs of (kN).

The final negative statement is no broader than the proof. An infinite
distinct-odd-semiprime family is sufficient to refute a universal guarantee
for this direct method, but it is not an all-input splitter. The conditional
recursion paragraph is explicitly conditional and does not convert F37 into
a positive factoring result.

## Remaining open cases are preserved

The report does not close any of the following:

* adaptive (N)-dependent multipliers having (\Omega(\sqrt n)) bits;
* target-dependent concentration on the actual discrete prime ratio;
* joint use of several nonsquare scan residues or complete transcripts;
* non-Fermat metric observables or non-gcd extraction; or
* the required classical all-input Las Vegas factoring algorithm.

Those exclusions are stated in the candidate itself. I found no sentence in
the amended artifact that silently promotes the continuous surrogate into an
adaptive discrete lower bound, or the short-multiplier theorem into a general
factoring obstruction.

## Final disposition

All seven historical amendments are incorporated, and the amended
mathematics survives a fresh hostile reconstruction.

> **PASS AS WRITTEN.**
