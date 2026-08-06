# F42 focused hostile audit: Newton basin obstruction

**Verdict: CLEAN PASS.**

**Artifact audited:** experiments/F42_newton_basin_kill/RESULT.md

**Audit status:** focused hostile audit only. This does not perform or replace
the required proof-blind reconstruction.

**Computation:** none. The candidate and this audit are proof-only.

## 1. Audit mandate and scope

I read the verification cadence in PROMPT.md, the preregistered F25 row in
REGISTRY.md, and the complete candidate artifact. I tried to refute the
candidate at each requested pressure point:

1. the global projective conjugacy and all exceptional points;
2. the exact preimages of the two roots;
3. the denominator-basin argument for primes congruent to \(3\pmod 4\);
4. every gcd identity in (4.4);
5. every row of the disjoint unit count and the numerator \(2p+2q-10\);
6. the raw residue sampler, its conditioning, and the numerator
   \(3p+3q-12\);
7. public units \(s\) chosen adaptively between fresh starts;
8. the PNT-in-arithmetic-progressions construction, balance constants, and
   bit-length conversion;
9. the restart and expected-cost conclusions; and
10. the exact boundary between named intrinsic tickets and excluded
    cross-iterate processing.

No mathematical objection survived. The proof establishes the narrow method
failure it claims and does not silently promote it to a lower bound for Newton
transcripts or for factoring.

## 2. Projective conjugacy and exceptional points

Let \(r\) be odd, \(s\in\mathbb F_r^\times\), and

\[
 F([X:Z])=[X^2+s^2Z^2:2XZ].
\]

For a common projective zero, the second coordinate forces \(XZ=0\). If
\(X=0\), the first coordinate is \(s^2Z^2\ne0\); if \(Z=0\), it is
\(X^2\ne0\). Thus the homogeneous quadratics have no common zero, even over
an algebraic closure, and \(F\) is a genuine degree-two morphism.

The matrix of

\[
 M([X:Z])=[X-sZ:X+sZ]
\]

has determinant \(2s\ne0\). Direct substitution gives

\[
 M(F([X:Z]))=[(X-sZ)^2:(X+sZ)^2]=S(M([X:Z])),
\]

where \(S([U:V])=[U^2:V^2]\). This is an identity of homogeneous maps, so it
does not depend on cancelling an affine denominator.

The four listed exceptional values are all correct:

| \(x\) | \(M(x)\) | \(F(x)\) |
| --- | --- | --- |
| \(s\) | \(0\) | \(s\) |
| \(-s\) | \(\infty\) | \(-s\) |
| \(0\) | \(-1\) | \(\infty\) |
| \(\infty\) | \(1\) | \(\infty\) |

There is no characteristic-two collision because the theorem assumes an odd
prime and \(s\ne0\). The two roots remain distinct at the endpoint \(r=3\).

Under \(S^k\), the only preimage of \(0\) is \(0\), and the only preimage of
\(\infty\) is \(\infty\). Applying \(M^{-1}\) proves, for every \(k\ge0\),

\[
 F^k(x_0)=s\iff x_0=s,
 \qquad
 F^k(x_0)=-s\iff x_0=-s.
\]

This includes \(k=0\) and proves the exact singleton root-basin claim.

## 3. Denominator basin for \(r\equiv3\pmod4\)

For \(r\equiv3\pmod4\), \(-1\) is a nonsquare. Since \(a=s^2\ne0\),
\(-a\) is also a nonsquare, so \(x^2+a\ne0\) for every
\(x\in\mathbb F_r\). Starting from \(x_0\ne0\), the denominator \(2x_k\)
is nonzero, and the next iterate cannot be zero because its numerator is
nonzero. Induction keeps every affine iterate finite and nonzero.

The alternative conjugacy check is sound: \(x_k=0\) means
\(z_0^{2^k}=-1\). For \(k\ge1\), the left side is a square while \(-1\) is
not; \(k=0\) is exactly the excluded zero start.

Combining this with the singleton root basins proves all three assertions in
(3.2), including the quantifier “for every \(k\ge0\).”

The side statement for \(r\equiv1\pmod4\) is also correct. If
\(r-1=2^\nu u\) with \(u\) odd, then in the cyclic group of order
\(2^\nu u\), the equation \(z^{2^k}=-1\) has
\(\gcd(2^k,r-1)=2^k\) solutions when \(1\le k<\nu\), and is insoluble when
\(k\ge\nu\). This is used only to police scope.

## 4. Every identity in (4.4)

Take distinct primes \(p,q\equiv3\pmod4\), \(N=pq\), a public unit \(s\),
and a uniform unit \(x_0\). CRT makes the two coordinates independent and
uniform on \(\mathbb F_p^\times\) and \(\mathbb F_q^\times\).

For either local prime \(r\):

* \(x_k\ne0\), so neither \(r\mid x_k\) nor \(r\mid2x_k\);
* \(x_k^2+a\ne0\), so the prospective numerator has no local zero;
* \(x_k^2-a=0\) exactly when \(x_0\in\{s,-s\}\pmod r\);
* \(x_k-s=0\) exactly when \(x_0=s\pmod r\); and
* \(x_k+s=0\) exactly when \(x_0=-s\pmod r\).

Because \(N\) is squarefree, these statements lift exactly to

\[
\begin{aligned}
 \gcd(2x_k,N)&=1,\\
 \gcd(x_k^2+a,N)&=1,\\
 \gcd(x_k^2-a,N)&=p^{E_p}q^{E_q},\\
 \gcd(x_k-s,N)&=p^{E_p^+}q^{E_q^+},\\
 \gcd(x_k+s,N)&=p^{E_p^-}q^{E_q^-}.
\end{aligned}
\]

Thus (4.4) is correct for every \(k\ge0\), not merely in distribution at a
fixed time. The public checks of \(2\) and \(s\) are both \(1\). Since
\(a=s^2\), a separate check of \(a\) would also be \(1\).

The materialized denominator at the next step is covered by the first
identity at \(k+1\). The fixed-point consecutive difference is not an
omitted cross-time ticket:

\[
 x_{k+1}-x_k=\frac{a-x_k^2}{2x_k}.
\]

Because \(2x_k\) is a unit, its gcd is exactly the residual gcd already
listed. The derivative numerator similarly reduces to the residual.
Longer-period comparisons \(x_{k+t}-x_k\) for \(t\ge2\), and arbitrary
functions of several orbit values, are genuinely different cross-iterate
tests and are explicitly excluded rather than silently claimed.

## 5. Exact unit counts, including \(p=3\)

Over \(\mathbb F_r^\times\), \(s\) and \(-s\) are distinct and occupy two
of the \(r-1\) units. Hence there are \(r-3\) nonroot units. The five
disjoint CRT classes have counts

\[
 (p-3)(q-3),\quad 2(q-3),\quad 2(p-3),\quad 2,\quad 2.
\]

Their sum is \((p-1)(q-1)\), so no unit class is omitted or counted twice.

The one-local-root classes yield a proper residual gcd. Among the four
both-root classes, two have equal signs and are the public roots
\(x_0=\pm s\), hence yield no proper gcd; the other two have opposite signs
and yield complementary proper gcds from \(x_0-s\) and \(x_0+s\).
Therefore the exact successful-unit count is

\[
 2(q-3)+2(p-3)+2=2p+2q-10,
\]

and the failure count is

\[
 (p-3)(q-3)+2.
\]

This remains valid at \(p=3\), or symmetrically \(q=3\). Then \(p-3=0\),
so every nonzero \(p\)-coordinate is a root. The unit total becomes
\(2(q-1)\), the success count becomes \(2q-4\), and the only failures are
the two same-sign global roots. All counts remain nonnegative and (4.6)
remains exact.

## 6. Raw sampler and adaptive public \(s\)

Among all \(N\) residue classes, the counts for gcd \(1,p,q,N\) are

\[
 (p-1)(q-1),\quad q-1,\quad p-1,\quad1.
\]

Redrawing only the zero class makes the first nonzero residue uniform on the
\(N-1\) nonzero classes. Conditional on a unit, it is uniform on the units,
so the unit-ticket count may be added directly to the proper zero-divisor
counts:

\[
 (q-1)+(p-1)+(2p+2q-10)=3p+3q-12.
\]

The complementary count is \((p-3)(q-3)+2\), and the two sum to \(pq-1\).
Equations (5.1) and (5.2) are exact. The number of draws through zero
redraws is geometric with nonzero probability \((N-1)/N\), so its mean is
\(N/(N-1)<2\).

For fixed \(s\), fresh complete restarts have exact product law
\(1-(1-\theta_{\rm raw})^K\), hence the union bound
\(\le K\theta_{\rm raw}\).

The adaptive-\(s\) statement is valid with its stated qualification. After
any failure history, if the algorithm chooses a public value already known
to be a unit and then draws a fresh independent uniform start, each local
target set still has size two. Thus the conditional success probability is
unchanged, regardless of the history-dependent unit choice. Sampling a new
candidate \(s\) that can be a nonunit would add a gcd ticket and is not a
“factor-free choice.” Choosing \(s\) from the current orbit through an
additional decoder is also explicitly excluded.

## 7. Infinite balanced family and constants

For fixed \(\lambda>1\), the prime number theorem in arithmetic progressions
gives

\[
 \pi(\lambda X;4,3)-\pi(X;4,3)
 \sim \frac{(\lambda-1)X}{2\log X},
\]

which tends to infinity. Thus \([X,2X]\) contains at least two distinct
primes congruent to \(3\pmod4\) for all sufficiently large \(X\). The
intervals \([3^j,2\cdot3^j]\) are pairwise disjoint because the next lower
endpoint is \(3^{j+1}>2\cdot3^j\). Choosing two primes from each gives
infinitely many distinct \(N_j=p_jq_j\) with \(q_j/p_j\le2\).

For \(p_j,q_j\in[X_j,2X_j]\),

\[
 \theta_{\rm raw}
 =\frac{3p_j+3q_j-12}{p_jq_j-1}
 \le\frac{12X_j}{X_j^2-1}
 \le\frac{24}{X_j}
 \le\frac{48}{\sqrt{N_j}}
\]

for \(X_j\ge2\). The last inequality uses
\(\sqrt{N_j}\le2X_j\). The same interval bounds give
\(\theta_{\rm unit}=O(X_j^{-1})=O(N_j^{-1/2})\).

Since \(n_j=\lceil\log_2(N_j+1)\rceil\), \(N_j\) and \(2^{n_j}\) differ
only by a fixed factor. Hence
\(N_j^{-1/2}=2^{-n_j/2+O(1)}\). The candidate needs only the upper bound,
although balance also supplies the matching lower order if “this is” is read
as a theta-order statement.

For every fixed polynomial \(K\),

\[
 K(n_j)\theta_{\rm raw}=2^{-\Omega(n_j)}.
\]

This proves negligible success for polynomially many fresh restarts. Since
all named ticket events are invariant in \(k\), adding iterations inside a
restart does not change that probability. Repeat-until-success is geometric
with mean
\(1/\theta_{\rm raw}=\Omega(\sqrt{N_j})=2^{\Omega(n_j)}\).
Each restart incurs at least one random draw and one gcd, so expected bit
cost is already exponential; orbit arithmetic can only increase it.

## 8. Scope and final verdict

The artifact checks every ticket named in its algorithm class:

* public \(2,s\), and implicitly \(a=s^2\);
* the current and next Newton denominator;
* the numerator \(x_k^2+a\);
* the residual \(x_k^2-a\); and
* the two root/Möbius differences \(x_k\mp s\).

It neither uses nor claims a result about longer cross-iterate collisions,
orders, arbitrary transcript decoders, correlated starts, primes
\(1\pmod4\), prime powers, Hensel lifts, stochastic or piecewise dynamics,
real or metric rounding, other rational maps, or general factoring
algorithms. The prime, prime-power, even-input, and arbitrary-composite
comments correctly police this boundary. The distinct balanced semiprime
family suffices to kill only the proposed all-input large-basin mechanism.

Accordingly, classification as **method failure** for the exact F25
Newton-basin hope is justified. I found no unsupported quantifier, incorrect
count, missing named ticket, or hidden generalization requiring amendment.

**Final audit verdict: CLEAN PASS.**
