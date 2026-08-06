# F42 candidate: finite-field Newton basins do not enlarge the known roots

**Status:** candidate. This is the preregistered proof-only mandatory
kill-first result for registry family F25. It has not yet undergone hostile
audit or proof-blind reconstruction.

**Computation:** none. Every statement below is symbolic.

## 1. Exact proposal being tested

Let \(N\) be odd, let \(s\in(\mathbb Z/N\mathbb Z)^\times\) be public, and
put \(a=s^2\bmod N\). The natural Newton proposal samples a uniform unit
\(x_0\) and iterates

\[
 T(x)=\frac{x+a/x}{2}=\frac{x^2+a}{2x}\pmod N.
 \tag{1.1}
\]

At every materialized step it may take ordinary gcds of the named data
intrinsic to this proposal:

* the public denominators \(2,s\) and the Newton denominator \(x_k\);
* the prospective numerator/next-denominator expression \(x_k^2+a\);
* the fixed-point (square-root) residual \(x_k^2-a\); and
* the two differences \(x_k-s\) and \(x_k+s\), which are the usual
  mixed-square-root extraction tests and also include the denominator of
  the Möbius coordinate used below.

The initial unit may be obtained by uniform residue rejection, with every
gcd encountered by that sampler counted as a factoring success rather than
silently discarded. The algorithm may make any number of iterations per
restart and fresh independent restarts. This artifact analyzes exactly
these tickets. It does not analyze pairwise collisions between distinct
orbit times, arbitrary functions of the nonzero orbit transcript, or other
rational maps.

The closest promoted routes are P44/P45. They concern automorphisms and
low-degree finite-set bijections of the zero-product scheme. The present
map is a degree-two noninvertible rational map, so it is outside those
theorems. P22 concerns principal digits modulo \(N^2\), not finite-field
basins. Thus F42 is a materially new kill test rather than a retry of a
closed claim.

## 2. Projective conjugacy, including every exceptional point

Let \(r\) be an odd prime and let \(s\in\mathbb F_r^\times\). Write
\(a=s^2\). The affine Newton map extends to the everywhere-defined
degree-two morphism

\[
 F:\mathbb P^1(\mathbb F_r)\longrightarrow\mathbb P^1(\mathbb F_r),
 \qquad
 [X:Z]\longmapsto [X^2+s^2Z^2:2XZ].
 \tag{2.1}
\]

The two displayed homogeneous coordinates have no common projective zero:
if \(XZ=0\), the first coordinate is respectively \(s^2Z^2\) or \(X^2\),
which is nonzero. Hence (2.1) really is a morphism, including at the affine
denominator zero \(x=0\).

Define the projective Möbius transformation

\[
 M([X:Z])=[X-sZ:X+sZ]
 \tag{2.2}
\]

and the squaring morphism \(S([U:V])=[U^2:V^2]\). The determinant of
\(M\) is \(2s\ne0\). Direct homogeneous calculation gives

\[
\begin{aligned}
 M(F([X:Z]))
 &= [X^2+s^2Z^2-2sXZ:X^2+s^2Z^2+2sXZ]\\
 &= [(X-sZ)^2:(X+sZ)^2]
 =S(M([X:Z])).
\end{aligned}
\tag{2.3}
\]

Thus \(M\circ F=S\circ M\) on **all** of \(\mathbb P^1\), not merely away
from denominators. In affine notation this is

\[
 z=\frac{x-s}{x+s},\qquad z(T(x))=z(x)^2,
 \tag{2.4}
\]

with (2.3), rather than illicit cancellation, defining the exceptional
values:

| \(x\) | \(z=M(x)\) | \(F(x)\) | interpretation |
| --- | --- | --- | --- |
| \(s\) | \(0\) | \(s\) | known positive root, fixed |
| \(-s\) | \(\infty\) | \(-s\) | known negative root, fixed |
| \(0\) | \(-1\) | \(\infty\) | affine Newton denominator fails |
| \(\infty\) | \(1\) | \(\infty\) | projective fixed point |

In particular, for every \(k\ge0\),

\[
 F^k(x_0)=s\iff x_0=s,
 \qquad
 F^k(x_0)=-s\iff x_0=-s.
 \tag{2.5}
\]

Indeed, under \(M\) these assertions are
\(z_0^{2^k}=0\iff z_0=0\) and
\(z_0^{2^k}=\infty\iff z_0=\infty\). The two exact root basins therefore
contain one field point each; iteration never manufactures a new square
root.

## 3. Why primes \(3\bmod4\) eliminate every denominator basin

Now suppose \(r\equiv3\pmod4\). Since \(a=s^2\ne0\), the element
\(-a\) is a nonsquare. Therefore

\[
 x^2+a\ne0 \quad\text{for every }x\in\mathbb F_r.
 \tag{3.1}
\]

If \(x_0\ne0\), induction in (1.1) shows that every affine iterate is finite
and nonzero: an iterate can equal zero only if the preceding numerator
\(x^2+a\) vanishes, and (3.1) forbids this. Equivalently, \(x_k=0\) would
mean \(z_0^{2^k}=-1\). For \(k\ge1\), the left side is a square in
\(\mathbb F_r^\times\), whereas \(-1\) is not. The case \(k=0\) is exactly
the excluded start \(x_0=0\).

Consequently, from any nonzero start and for every \(k\ge0\),

\[
 x_k\ne0,
 \qquad
 x_k^2+a\ne0,
 \qquad
 x_k^2-a=0\iff x_0\in\{s,-s\}.
 \tag{3.2}
\]

This is the exact local obstruction: on a finite field there is no metric
attraction, and on the congruence class \(3\bmod4\) even the affine pole has
no nonzero backward basin.

The congruence restriction is essential. If
\(r-1=2^\nu u\) with \(u\) odd and \(\nu\ge2\), then
\(z^{2^k}=-1\) has exactly \(2^k\) solutions for \(1\le k<\nu\) and none
for \(k\ge\nu\). Thus primes \(1\bmod4\) can have genuine denominator
preimages. This possible input-specific success does not repair an
all-input algorithm in the presence of the infinite obstruction family
below.

## 4. Complete CRT ticket law from a uniform unit

Let

\[
 N=pq,
 \qquad p\ne q,
 \qquad p\equiv q\equiv3\pmod4,
 \tag{4.1}
\]

and let \(s\in(\mathbb Z/N\mathbb Z)^\times\). Conditional on \(x_0\)
being a uniform unit, its two CRT coordinates are independent and uniform in
\(\mathbb F_p^\times\) and \(\mathbb F_q^\times\). For
\(r\in\{p,q\}\), define

\[
 E_r^+=[x_0\equiv s\pmod r],\qquad
 E_r^-=[x_0\equiv-s\pmod r],\qquad
 E_r=E_r^+\vee E_r^-.
 \tag{4.2}
\]

The events \(E_r^+\) and \(E_r^-\) are disjoint, and

\[
 \Pr(E_r)=\frac2{r-1}.
 \tag{4.3}
\]

Equations (2.5) and (3.2) give, simultaneously for **every** \(k\ge0\),

\[
\begin{aligned}
 \gcd(2x_k,N)&=1,\\
 \gcd(x_k^2+a,N)&=1,\\
 \gcd(x_k^2-a,N)&=p^{E_p}q^{E_q},\\
 \gcd(x_k-s,N)&=p^{E_p^+}q^{E_q^+},\\
 \gcd(x_k+s,N)&=p^{E_p^-}q^{E_q^-}.
\end{aligned}
\tag{4.4}
\]

Here an indicator is used as an exponent, so a false event contributes
factor \(1\). The public checks \(\gcd(2,N)\) and \(\gcd(s,N)\) are also
\(1\). Formula (4.4) accounts for the Newton inverse denominator, the
future-denominator numerator, the residual, both mixed-root tests, and the
Möbius exceptional denominator. It also proves that repeating any of these
tests at later orbit times creates no new event.

The exact disjoint table is as follows.

| local initial-root type | number of units | residual gcd | result |
| --- | ---: | --- | --- |
| neither \(p\)- nor \(q\)-coordinate is a root | \((p-3)(q-3)\) | \(1\) | no ticket |
| \(p\)-coordinate only is a root | \(2(q-3)\) | \(p\) | factor \(p\) |
| \(q\)-coordinate only is a root | \(2(p-3)\) | \(q\) | factor \(q\) |
| both are roots with the same sign | \(2\) | \(N\) | \(x_0=\pm s\), known root only |
| both are roots with opposite signs | \(2\) | \(N\) | the two difference gcds are \(p,q\) |

For example, in the last row, if
\(x_0\equiv s\pmod p\) and \(x_0\equiv-s\pmod q\), then

\[
 \gcd(x_0-s,N)=p,
 \qquad
 \gcd(x_0+s,N)=q.
 \tag{4.5}
\]

All four local-root combinations are fixed by Newton, so the same statement
holds at every later time. In the one-local-root rows, one of the two
difference gcds also returns the same factor, but the residual has already
done so.

It follows that the exact success probability per accepted uniform-unit
restart, for any number \(L\ge0\) of Newton iterations, is

\[
 \boxed{
 \theta_{\rm unit}(p,q)
 =\frac{2(q-3)+2(p-3)+2}{(p-1)(q-1)}
 =\frac{2p+2q-10}{(p-1)(q-1)}.}
 \tag{4.6}
\]

The complementary failure count is

\[
 (p-3)(q-3)+2.
 \tag{4.7}
\]

Thus the claimed independent large basins do not exist. There are only the
two initially sampled roots in each local field.

## 5. The unit sampler's gcd tickets

For completeness, sample a uniform residue
\(Y\in\{0,1,\ldots,N-1\}\) and compute \(g=\gcd(Y,N)\). The exact counts
are

| \(g\) | number of residues |
| --- | ---: |
| \(1\) | \((p-1)(q-1)\) |
| \(p\) | \(q-1\) |
| \(q\) | \(p-1\) |
| \(N\) | \(1\), namely \(Y=0\) |

A proper gcd is an immediate success, \(Y=0\) is redrawn, and a unit is
accepted. Ignoring zero redraws, the first decisive residue is uniform
among the \(N-1\) nonzero residues. A complete restart, consisting of this
sampler followed by any number of Newton steps when a unit is accepted, has
exact success probability

\[
\begin{aligned}
 \theta_{\rm raw}(p,q)
 &=\frac{(q-1)+(p-1)+(2p+2q-10)}{N-1}\\
 &=\boxed{\frac{3p+3q-12}{pq-1}}.
\end{aligned}
\tag{5.1}
\]

Its exact failure probability is

\[
 1-\theta_{\rm raw}
 =\frac{(p-3)(q-3)+2}{pq-1}.
 \tag{5.2}
\]

The expected number of raw residues used before the zero redraw is resolved
is \(N/(N-1)<2\). Hence the sampler is efficient, but its own useful
zero-divisor mass is only the same \(1/p+1/q\) scale as the root tickets.

For \(K\) fresh independent complete restarts, the exact success probability
is

\[
 1-(1-\theta_{\rm raw})^K\le K\theta_{\rm raw}.
 \tag{5.3}
\]

The exact law is unchanged if the public unit \(s\) is selected anew before
each fresh uniform start as a function of prior failures: conditional on any
such factor-free choice, the two local target sets still have sizes \(2\)
and the fresh unit has the same law. This observation does not cover a
choice of \(s\) made from the current orbit by some additional decoder.

## 6. Infinite balanced obstruction family

The prime number theorem in arithmetic progressions states

\[
 \pi(X;4,3)\sim\frac12\operatorname{Li}(X).
 \tag{6.1}
\]

Therefore, for every fixed \(\lambda>1\),

\[
 \pi(\lambda X;4,3)-\pi(X;4,3)
 \sim\frac{(\lambda-1)X}{2\log X},
 \tag{6.2}
\]

so the interval \([X,\lambda X]\) contains at least two distinct primes
congruent to \(3\pmod4\) for all sufficiently large \(X\).

Take \(X_j=3^j\), set \(\lambda=2\), and choose two distinct such primes

\[
 X_j\le p_j<q_j\le2X_j.
 \tag{6.3}
\]

The intervals are disjoint as \(j\) grows, so this gives infinitely many
distinct semiprimes \(N_j=p_jq_j\), with \(q_j/p_j\le2\). They form a
fixed balanced family. On this family,

\[
 \theta_{\rm unit}=O(X_j^{-1}),
 \qquad
 \theta_{\rm raw}=O(X_j^{-1})=O(N_j^{-1/2}).
 \tag{6.4}
\]

For an explicit constant, when \(X_j\ge2\), (5.1) gives

\[
 \theta_{\rm raw}
 \le\frac{12X_j}{X_j^2-1}
 \le\frac{24}{X_j}
 \le\frac{48}{\sqrt{N_j}}.
 \tag{6.5}
\]

If \(n_j=\lceil\log_2(N_j+1)\rceil\), this is
\(2^{-n_j/2+O(1)}\). For every fixed polynomial \(K(n)\), polynomially many
restarts therefore have success probability at most

\[
 K(n_j)\theta_{\rm raw}(p_j,q_j)
 =2^{-\Omega(n_j)}.
 \tag{6.6}
\]

The number of iterations within each restart is irrelevant to (6.6), even
if it is much larger than polynomial, because all tickets in (4.4) are
time-invariant. If the natural algorithm instead repeats fresh restarts
until a ticket occurs, it terminates almost surely, but the expected number
of restarts is exactly \(1/\theta_{\rm raw}=\Omega(\sqrt N)\) on this
family. Since every restart performs at least one random draw and one gcd,
this is exponential in the input bit length even before charging the
modular arithmetic inside an orbit.

## 7. The exact killed claim and scope boundary

**Candidate theorem.** For every distinct-prime semiprime
\(N=pq\) with \(p\equiv q\equiv3\pmod4\), every public unit \(s\), and every
uniform-unit start, projective Newton iteration for the known square
\(a=s^2\) is conjugate to squaring. All affine iterates remain units; a
local square root occurs at any time if and only if it was present initially;
and all Newton-denominator, numerator, square-residual, and mixed-root gcd
tickets have the exact time-independent law (4.4). The success probability
is (4.6), or (5.1) when exact residue-rejection sampling is charged. On an
infinite fixed balanced family both are \(O(N^{-1/2})\), so polynomially
many iterations and restarts have negligible success and
repeat-until-success has exponential expected cost.

This is **method failure** for the exact F25 hope that finite-field Newton
dynamics creates large independent \(\pm s\) attraction basins. It is not
evidence that bare \(N\) cannot manufacture a metric hint, and it is not a
factoring lower bound.

The theorem deliberately does not cover:

* cross-iterate collision/order tests or arbitrary nonlinear processing of
  the nonzero orbit transcript;
* other rational maps or a different known polynomial;
* primes \(1\bmod4\), whose denominator-preimage trees can be nontrivial;
* prime powers or \(p\)-adic/Hensel lifts, where valuation genuinely gives
  Newton attraction;
* stochastic resets within an orbit, nonuniform or correlated starts,
  auxiliary state, or nonlocal kernels;
* adaptive/piecewise or canonical real rounding, magnitude comparisons, or
  any other dissipative metric dynamics; or
* even inputs, primes, arbitrary composites, or a complete all-input
  factoring algorithm.

For even \(N\), the public divisor \(2\) is already available and division
by \(2\) in (1.1) is not the relevant issue. For a prime input no proper gcd
can occur. For \(p^e\), CRT independence into two fields is absent and this
argument makes no assertion about valuations. The infinite distinct
balanced semiprime family is sufficient only to refute the proposed
all-input Newton-basin mechanism in its stated form.

**Positive escape found:** none within the preregistered algorithm class.
The denominator preimages for primes \(1\bmod4\), \(p\)-adic lifts, and
cross-orbit transcript tests are genuine reopen conditions, not conclusions
of this kill result.
