# F12 elliptic collision kill and torus barrier

**Approach-family ID:** `F12_elliptic_collision_kill`.

**Result:** the additive elliptic (x)-collision product is not an all-input
local separator at (m=\lfloor\sqrt N\rfloor).  On the explicit balanced
semiprime (N=101\cdot103), Hasse's bound forces its cleared value to vanish
in both local fields for every good curve and every affine point.  A retained
witness additionally shows this can happen with every denominator through
(m) nonzero in both fields.

The multiplicative-torus specialization has an exact conditional reduction:
a uniform polylogarithmic evaluator for its collision product would give a
Las Vegas polynomial-time factorer for every integer.  No such evaluator is
constructed here.  The exact recurrence found is linear in (m), so the
conditional reduction is a barrier statement, not a factoring advance.

## 1. Exact elliptic product

Let

\[
E:y^2=x^3+Ax+B
\]

be nonsingular over a field of characteristic other than (2,3), let (P)
be affine, and let \(\psi_n,\phi_n\) be the standard division polynomials, so

\[
x([n]P)=\frac{\phi_n(P)}{\psi_n(P)^2}.
\]

For (1\le i<j\), the division-polynomial recurrence and

\[
\phi_n=x\psi_n^2-\psi_{n+1}\psi_{n-1}
\]

give the polynomial identity

\[
\boxed{
\phi_i\psi_j^2-\phi_j\psi_i^2
=\psi_{i+j}\psi_{j-i}.}
\tag{1}
\]

Indeed, the two (x\psi_i^2\psi_j^2) terms cancel, and the remaining terms
are exactly the standard addition recurrence for the right-hand side.

Therefore the division-free numerator of the (x)-Vandermonde product is

\[
C_m(P)
=\prod_{1\le i<j\le m}
  \bigl(\phi_i\psi_j^2-\phi_j\psi_i^2\bigr)(P)
=\prod_{1\le i<j\le m}\psi_{i+j}(P)\psi_{j-i}(P).
\tag{2}
\]

When the denominators are nonzero,

\[
\prod_{i<j}\bigl(x([i]P)-x([j]P)\bigr)
=\frac{C_m(P)}{\prod_{k=1}^m\psi_k(P)^{2(m-1)}}.
\tag{3}
\]

Collecting equal indices in (2) gives

\[
C_m
=\prod_{d=1}^{m-1}\psi_d^{m-d}
 \prod_{s=3}^{2m-1}\psi_s^{c_s},
\qquad
c_s=\max\!\left(0,
\left\lfloor\frac{s-1}{2}\right\rfloor-
\max(1,s-m)+1\right).
\tag{4}
\]

For (m\ge3), every nonconstant index (2,3,\ldots,2m-1) has positive
exponent.  R06 checked (1) on all 45 pairs through (m=10), checked the
collected support through 203, and evaluated (2) on the retained witness.

### Exact order threshold and the denominator issue

Let (t=\operatorname{ord}(P)\).  For affine (P),

\[
\psi_k(P)=0\quad\Longleftrightarrow\quad [k]P=O
\quad\Longleftrightarrow\quad t\mid k.
\]

Equations (3)--(4) give the exact trichotomy

\[
\begin{array}{c|c|c}
t & \psi_1(P),\ldots,\psi_m(P) & C_m(P)\\ \hline
t\le m & \text{some denominator is zero} & 0\\
m<t\le2m-1 & \text{all are nonzero} & 0\\
t>2m-1 & \text{all are nonzero} & \ne0.
\end{array}
\tag{5}
\]

The middle interval is the (x(Q)=x(-Q)) ambiguity.  When (t>m), a
collision among ([1]P,\ldots,[m]P) cannot come from (t\mid(j-i)); it comes
from (t\mid(i+j)).  Such a pair exists exactly when (t\le2m-1), for
example (i=t-m,j=m).

Thus the relevant clean-collision threshold is (2m-1), not (m).
Scanning failed denominators detects the first line of (5), but that is an
ECM-style mechanism distinct from compressing the cleared collision product.

## 2. Balanced Hasse synchronization kills the separator

For a good reduction modulo a prime \(\ell\), Hasse gives

\[
\#E(\mathbf F_\ell)\le \ell+1+2\sqrt\ell.
\]

Consequently, if

\[
\left\lfloor\ell+1+2\sqrt\ell\right\rfloor\le2m-1,
\tag{6}
\]

then every nonidentity local point has order at most (2m-1), and (5)
forces (C_m=0) for every curve and point with good reduction.

Take

\[
N=10403=101\cdot103,
\qquad m=\lfloor\sqrt N\rfloor=101,
\qquad2m-1=201.
\]

The two Hasse upper bounds are only 122 and 124.  Hence, for **every** short
Weierstrass curve having good reduction at both primes and every global
affine point,

\[
C_m(P)\equiv0\pmod {101},
\qquad
C_m(P)\equiv0\pmod {103}.
\]

Since (N) is squarefree, (C_m(P)\equiv0\pmod N) and

\[
\gcd(C_m(P),N)=N.
\]

This is distribution-independent: randomizing the curve or point cannot make
the cleared product separate these factors.  A singular local curve is not
an escape for this construction; a nonunit discriminant already exposes a
factor before the collision calculation.

### A clean synchronized witness

The retained curve and CRT point are

\[
E:y^2=x^3+x+5,
\qquad P=(5461,5889)\pmod N.
\]

Its discriminant residue is 9942, a unit modulo (N).  Locally:

| Field | Local point | \(\#E\) | Point order | First collision for \(m=101\) |
| --- | --- | ---: | ---: | --- |
| \(\mathbf F_{101}\) | \((7,31)\) | 112 | 112 | \(x([11]P)=x([101]P)\) |
| \(\mathbf F_{103}\) | \((2,18)\) | 106 | 106 | \(x([5]P)=x([101]P)\) |

Both orders lie strictly between 101 and 201.  Thus every multiple through
101 is affine in both fields, while the displayed index sums, 112 and 106,
cause clean (\pm)-collisions.  R09 checked all multiples and all
(x)-collisions.  R01 found the same witness at the slightly larger search
length (m=\lceil\sqrt N\rceil=102); R09 is the floor-threshold recheck.

### Exact probability for arbitrary local group structures

For a fixed finite elliptic group

\[
G\cong\mathbf Z/a\mathbf Z\times\mathbf Z/b\mathbf Z,
\qquad a\mid b,
\]

the number of points killed by (e) is

\[
|G[e]|=\gcd(e,a)\gcd(e,b).
\]

Möbius inversion gives the number of points of exact order (d):

\[
B_G(d)=\sum_{e\mid d}\mu(d/e)\gcd(e,a)\gcd(e,b).
\]

Define

\[
A_G(T)=\sum_{d\le T}B_G(d),
\qquad
\alpha_G(T)=\frac{A_G(T)}{|G|}.
\]

For independent uniform local points, the probability that the cleared
product vanishes in exactly one of two fields is

\[
\alpha_{G_p}(T)(1-\alpha_{G_q}(T))
+(1-\alpha_{G_p}(T))\alpha_{G_q}(T),
\qquad T=2m-1.
\tag{7}
\]

For uniform nonidentity points, replace \(\alpha_G\) by

\[
\alpha_G^*(T)=\frac{A_G(T)-1}{|G|-1}.
\]

Any randomized curve distribution merely averages (7) over its induced
local group distributions.  On the balanced example, Hasse forces every
such \(\alpha^*\) to equal 1, so the separation probability is exactly zero.
On unbalanced inputs it can be nonzero, but (7) shows that success depends on
the two complete order distributions; no universal mismatch follows from the
collision identity.

Modulo a prime power (p^e), reduction modulo (p) still determines whether
the integer product is divisible by (p).  Higher (p)-adic valuations only
determine how much of (p^e) enters the gcd.  They do not repair simultaneous
vanishing at every distinct prime.

## 3. What the elliptic factorization does and does not compress

Equation (4) compresses \(\binom m2\) pair factors to (2m-2) distinct
division-polynomial values.  That is an (O(m^2)\)-to-(O(m)\) algebraic
compression, not a polylogarithmic circuit in the input length
(\log m\).  No uniform polylogarithmic evaluator for the entire weighted
product is established here, and polynomial degree alone cannot prove that
none exists.

More importantly, even an ideal evaluator would return zero modulo both
factors on the balanced example.  Computation speed cannot repair the
separation failure.

## 4. Multiplicative-torus specialization

For the orbit

\[
1,a,a^2,\ldots,a^{m-1},
\]

directly grouping pairs by (d=j-i) gives

\[
\boxed{
D_m(a)=\prod_{0\le i<j<m}(a^i-a^j)
=a^{\binom m3}S_m(a),
\qquad
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}.}
\tag{8}
\]

For a unit (a\in\mathbf F_\ell^*\) of order (t), the exact off-by-one
threshold is

\[
S_m(a)=0
\quad\Longleftrightarrow\quad
t\le m-1;
\qquad
S_m(a)\ne0
\quad\Longleftrightarrow\quad
t\ge m.
\tag{9}
\]

R04 checked (8) symbolically for (m=2,\ldots,10), directly modulo two
semiprimes, and exhaustively counted all units.

### Distinct semiprimes

Let (N=pq), (p<q), and (m=\lfloor\sqrt N\rfloor).  Then

\[
p\le m<q.
\]

Every unit has \(\operatorname{ord}_p(a)\le p-1\le m-1\), so (p\mid S_m(a)).
If (a\bmod q) is primitive, then

\[
\operatorname{ord}_q(a)=q-1\ge m,
\]

so (q\nmid S_m(a)).  Therefore

\[
\gcd(S_m(a),N)=p.
\]

Conditional on a uniform unit modulo (N), the exact success probability is

\[
\frac{1}{q-1}\sum_{\substack{d\mid q-1\\d\ge m}}\varphi(d),
\tag{10}
\]

and is at least the primitive-root probability

\[
\frac{\varphi(q-1)}{q-1}.
\]

The retained exhaustive counts are:

| \(N=pq\) | \(m\) | Exact success | Primitive lower bound |
| --- | ---: | ---: | ---: |
| \(101\cdot103\) | 101 | \(16/51\) | \(16/51\) |
| \(11\cdot101\) | 33 | \(3/5\) | \(2/5\) |

### Elementary inverse-log probability bound

If the distinct prime divisors of (t) are
\(r_1<\cdots<r_k\), then (r_i\ge i+1).  Since (r/(r-1)) decreases,

\[
\frac{t}{\varphi(t)}
=\prod_{i=1}^k\frac{r_i}{r_i-1}
\le\prod_{i=1}^k\frac{i+1}{i}
=k+1
\le1+\log_2t.
\]

Hence

\[
\frac{\varphi(t)}t\ge\frac1{1+\log_2t}.
\tag{11}
\]

To sample, choose (a) uniformly from (1,\ldots,N-1) and first compute
(g=\gcd(a,N)).  A nonunit immediately gives a proper factor.  Conditional
on (g=1), CRT makes the local residues uniform and independent.  Because
nonunits are already successes, (11) is also a lower bound on the
unconditional success probability of a trial.

## 5. Conditional all-input reduction

Assume a **uniform** algorithm

\[
\operatorname{Eval}(N,a,m)=S_m(a)\bmod N
\]

runs in time polynomial in \(\log N+\log m\), without knowing the
factorization of (N).

Let

\[
N=\prod_{i=1}^r p_i^{e_i}
\]

have at least two distinct prime factors and put

\[
s=\sum_i e_i.
\]

The weighted geometric mean (N^{1/s}) lies strictly between the smallest
and largest distinct primes.  Therefore

\[
m_s=\lfloor N^{1/s}\rfloor
\quad\text{satisfies}\quad
p_{\min}\le m_s<p_{\max}.
\tag{12}
\]

Also (2\le s\le\operatorname{bitlength}(N)), because (N\ge2^s).
Thus an algorithm that does not know (s) scans

\[
k=2,3,\ldots,\operatorname{bitlength}(N),
\qquad m_k=\lfloor N^{1/k}\rfloor.
\]

At the hidden index (k=s), a unit whose residue modulo
(q=p_{\max}) is primitive satisfies

\[
p_{\min}\mid S_{m_s}(a),
\qquad
q\nmid S_{m_s}(a).
\]

Hence \(\gcd(S_{m_s}(a),N)\) is proper and nontrivial.  Repeated prime
powers cause no problem: the gcd contains at least one copy of
(p_{\min}), possibly more, while its (q)-adic valuation is zero.  R07
verified the complete exponent scan on

\[
3087=3^2\cdot7^3
\quad\text{and}\quad
1452=2^2\cdot3\cdot11^2,
\]

where (s=5,m_s=4), obtaining gcds 9 and 12 respectively.

Fresh uniform samples make this Las Vegas: the result is always checked by a
gcd, and (11) bounds the expected number of trials by
(1+\log_2N).  If (n=\operatorname{bitlength}(N)) and one evaluator call
costs (T(n)), scanning all (k) costs (O(nT(n)+\operatorname{poly}(n)))
per trial and

\[
O(n^2T(n)+\operatorname{poly}(n))
\]

in expectation.  Primality testing, exact perfect-power detection, and
recursion turn the splitter into complete factorization.  For example, R07
checked the perfect-power split (225=15^2).

This proves:

> A uniform polylogarithmic exact evaluator for (S_m(a)\bmod N) implies a
> Las Vegas polynomial-time algorithm for integer factorization on all
> inputs.

### The missing evaluator

Let

\[
P_m(a)=\prod_{d=1}^{m}(1-a^d).
\]

The genuine recurrence supplied by (8) is

\[
S_{m+1}=S_mP_m,
\qquad
P_{m+1}=P_m(1-a^{m+1}).
\tag{13}
\]

It uses \(\Theta(m)\) sequential ring operations.  Cyclotomic collection is
also only a formal compression:

\[
S_m(a)=(-1)^{\binom m2}
\prod_{e=1}^{m-1}\Phi_e(a)^{
h_em-e h_e(h_e+1)/2},
\qquad
h_e=\left\lfloor\frac{m-1}{e}\right\rfloor,
\tag{14}
\]

and still has (m-1) displayed factors.  Divide-and-conquer splitting
introduces cross-products at new offsets rather than closing on a fixed
polylogarithmic state.  None of (13)--(14) is a polylogarithmic evaluator.

Conversely, degree arguments do not prove a super-polylogarithmic circuit
lower bound: degree yields only a logarithmic multiplication-depth bound.
The correct conclusion is therefore conditional.  The hypothesized
evaluator already implies factoring by the theorem above; assuming it is not
progress toward factoring unless the evaluator is explicitly constructed.

## Scope

The balanced counterexample kills universal separation by the cleared
elliptic (x)-collision product at the proposed square-root orbit length.
It does not rule out ordinary denominator-based ECM behavior, other orbit
lengths, extra coordinates, or instance-specific success on unbalanced
inputs.

The torus theorem is a rigorous reduction, including off-by-one thresholds,
sampling, repeated factors, perfect powers, and expected cost.  It is not an
unconditional factoring algorithm because its sole expensive step—the
uniform polylogarithmic evaluation of (S_m\)—remains unproved and
unconstructed.

