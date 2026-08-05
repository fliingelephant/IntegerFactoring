# F13 Teichmuller lift kill

**Approach-family ID:** `F13_teichmuller_lift_kill`.

**Result:** the proposed extra \(p\)-adic digit is not retained input
information.  The map

\[
\tau_N(a)=a^N\pmod {N^2},\qquad N=pq,
\]

kills the full principal-unit kernel and leaves a twisted power map on the
Teichmuller quotient.  The direct principal-log/high-digit carrier has an
\(O(K/\sqrt N)\) success upper bound for \(K\) uniform samples on every
odd-prime pair \(p<q<2p\).  Hence a polylogarithmic collection has
exponentially small success in the input bit length on the infinite balanced
family supplied by Bertrand's postulate.

The additive defect and iterated-difference carriers can factor some small
instances, but their exact success probabilities decline sharply on the
tested balanced instances.  For the two tested twin-prime pairs, the
principal quotient contributes exactly zero additional probability.  These
finite tests are not a complexity lower bound and do not rule out a different,
component-selective construction in \(\mathbb Z/N^2\mathbb Z\).

## 1. The full principal subgroup is erased

CRT gives

\[
(\mathbb Z/N^2\mathbb Z)^\times
\simeq(\mathbb Z/p^2\mathbb Z)^\times
      \times(\mathbb Z/q^2\mathbb Z)^\times.
\]

The kernel of reduction to \((\mathbb Z/N\mathbb Z)^\times\) is exactly

\[
K=\{1+kN\pmod {N^2}:k\pmod N\}.
\]

Locally,

\[
1+kN\longmapsto
\bigl(1+p(qk),\;1+q(pk)\bigr),
\]

so

\[
k\pmod N\longmapsto(qk\pmod p,\;pk\pmod q)
\]

is a bijection onto the two local principal coordinates.  Nevertheless,

\[
(1+kN)^N\equiv1\pmod {N^2}.
\]

More generally, \((a+Nt)^N\equiv a^N\pmod {N^2}\), so \(\tau_N\) factors
through reduction modulo \(N\) and discards all input data in \(K\).

Writing the local Teichmuller lift as

\[
[x]_\ell=x^\ell\pmod {\ell^2},
\]

every local unit has the unique form \([x]_p(1+pu)\).  Therefore

\[
\tau_N(a)\equiv[a]_p^q\pmod {p^2},\qquad
\tau_N(a)\equiv[a]_q^p\pmod {q^2}.                 \tag{1}
\]

Thus the output is Teichmuller locally, but it is generally the twisted lift
\([a]_p^q,[a]_q^p\), not the canonical lift \([a]_p,[a]_q\).  The map is
multiplicative, not additive or generally idempotent.

Let

\[
\lambda=\operatorname{lcm}(p-1,q-1).
\]

On the Teichmuller quotient, \(\tau_N\) is the RSA-style exponent-\(N\) map.
It is invertible exactly when \(\gcd(N,\lambda)=1\).  Given the factor-aware
quantity

\[
d=N^{-1}\pmod\lambda,
\]

equation (1) untwists as \(\tau_N(a)^d=([a]_p,[a]_q)\).  R01 verified this
on every tested instance for which the inverse exists; it fails to exist for
\(N=3\cdot7\).  This recipe needs the hidden \(\lambda\).  No reduction here
shows that computing an untwist by some other method is equivalent to
factoring.

There is also no useful randomness inside \(K\): its explicit logarithm is
\(\log_N(1+kN)=k\pmod N\).  For uniform \(k\pmod N\),

\[
\Pr(1<\gcd(k,N)<N)=\frac{p+q-2}{N},               \tag{2}
\]

which is just random gcd sampling, while \(\tau_N\) sends every such element
to 1.

## 2. The hidden-exponent identity is an order problem

Put \(A=\tau_N(a)\) for a unit \(a\).  Its local orders divide \(p-1\) and
\(q-1\).  Since

\[
(N+1)-(p+q)=(p-1)(q-1),
\]

one obtains the exact identity

\[
\boxed{A^{N+1}=A^{p+q}\pmod {N^2}}.               \tag{3}
\]

For a known \(A\), equation (3) reveals only

\[
p+q\equiv N+1\pmod {\operatorname{ord}(A)}.
\]

Recovering a sufficiently large period, or combining enough local periods
from several bases, is the same scalar order-spectrum bottleneck as the F07
route.  R01's rounded \(2\sqrt N\) probes produced no proper gcd.  In the
closest-factor cases the rounded exponent equals \(p+q\), making the defect
zero in both components rather than separating them.  No low-dimensional
classical extraction of \(p+q\) follows from (3).

## 3. Iteration contains no surviving principal log

For every \(r\ge1\),

\[
\tau_N^r(a)\equiv[a]_p^{q^r}\pmod {p^2},\qquad
\tau_N^r(a)\equiv[a]_q^{p^r}\pmod {q^2}.          \tag{4}
\]

Both sides are Teichmuller elements.  Consequently, if
\(\tau_N^{r+1}(a)-\tau_N^r(a)\) vanishes modulo a local prime, uniqueness of
the lift makes it vanish modulo that prime squared as well.  There is no
second-stage principal coordinate to inspect.

For uniform units, define the local equality probabilities

\[
P_p=\frac{\gcd(q-1,p-1)}{p-1},\qquad
P_q(r)=\frac{\gcd(p^r(p-1),q-1)}{q-1}.
\]

The exact proper-gcd probability of the \(r\)-th difference is

\[
P_p(1-P_q(r))+(1-P_p)P_q(r).                      \tag{5}
\]

For odd balanced primes \(p<q<2p\), \(p\nmid q-1\), so (5) is independent of
\(r\) and both local probabilities use
\(g=\gcd(p-1,q-1)\).  Synchronization can be complete: on
\(N=3\cdot7\), both local probabilities equal 1 for all three tested
differences, and the exact proper-gcd probability is 0.

## 4. Additive defect is a scalar Frobenius test

Consider

\[
\Delta(a,b)=\tau_N(a+b)-\tau_N(a)-\tau_N(b).
\]

Modulo \(p\) and \(q\), respectively,

\[
\Delta\equiv(a+b)^q-a^q-b^q\pmod p,
\qquad
\Delta\equiv(a+b)^p-a^p-b^p\pmod q.              \tag{6}
\]

This is the scalar specialization of the AKS/Frobenius binomial error.  The
lift to \(N^2\) refines its local valuation but does not make the map
universally additive.

For a local prime \(\ell\), let

\[
F_{\ell,e}(x)=[x]_\ell^e,
\qquad
G_{\ell,e}(t)=F_{\ell,e}(t+1)-F_{\ell,e}(t)-1.
\]

For unit \(a,b\), multiplicativity reduces the valuation of \(\Delta(a,b)\)
to that of \(G(a/b)\).  Classify it as 0, 1, or 2 according as it is not
divisible by \(\ell\), is divisible by \(\ell\) but not \(\ell^2\), or is
zero modulo \(\ell^2\).  Write the exact local distribution as
\(\pi_{\ell,c}\).

For independent uniform unit inputs, first compute \(\gcd(\Delta,N)\).  If
that is \(N\), compute

\[
\gcd(\Delta/N,N).
\]

This two-stage carrier succeeds exactly when the two local valuation
categories differ, hence with probability

\[
\boxed{1-\sum_{c=0}^2\pi_{p,c}\pi_{q,c}}.         \tag{7}
\]

The extra principal quotient contributes only

\[
\pi_{p,1}\pi_{q,2}+\pi_{p,2}\pi_{q,1}.           \tag{8}
\]

On all three larger balanced tests, every local count in category 1 was
zero, so (8) was exactly zero.

For a twin-prime pair \(q=p+2>3\), the local maps reduce to \(x^3\) at \(p\)
and \(x^{-1}\) at \(q\).  The exact category counts are

\[
(p-2,0,1),\qquad(q-4,0,3).
\]

The roots are exact Teichmuller equalities, not valuation-1 events.  Thus

\[
\Pr(\text{two-stage success})
=\frac{4(p-2)}{(p-1)(p+1)}=\Theta(1/p),           \tag{9}
\]

and the second stage adds zero.  R01 verified (9) at \((101,103)\) and
\((10007,10009)\).  Infinitely many twin primes are not known, so (9) is not
used as an unconditional asymptotic lower-bound claim.

## 5. The explicit high digit has a balanced-family probability bound

For \(B_r=\tau_N^r(a)\), let \(b_r\in[0,N)\) be its reduction modulo \(N\)
and define

\[
H_r=\frac{B_r-b_r}{N}\pmod N.                    \tag{10}
\]

Equivalently, the principal logarithm of \(B_rb_r^{-1}\) is
\(H_rb_r^{-1}\); since \(b_r\) is a unit, it has the same gcd with \(N\) as
\(H_r\).

For odd \(p<q<2p\), the exponent maps in (4) permute both local unit groups.
For fixed residue modulo \(p\), the CRT representative has the form
\(b=\alpha+pk\), and the condition \(p\mid H_r\) selects one residue class
of \(k\pmod p\).  Among the \(q-1\) possible nonzero residues modulo \(q\),
this gives at most \(\lceil q/p\rceil=2\) choices.  Reversing the roles gives
at most one choice.  Therefore, for every \(r\ge1\),

\[
\Pr(p\mid H_r)\le\frac2{q-1},\qquad
\Pr(q\mid H_r)\le\frac1{p-1}.                    \tag{11}
\]

For any fixed collection of \(K\) iterates of a uniform unit, without
assuming independence,

\[
\Pr\bigl(\exists r:\ 1<\gcd(H_r,N)<N\bigr)
\le K\left(\frac2{q-1}+\frac1{p-1}\right)
\le\frac{3K}{p-1}.                               \tag{12}
\]

Bertrand's postulate supplies a prime \(q\in(p,2p)\) for every prime \(p\),
so (12) applies on an infinite balanced semiprime family.  Since
\(p=\Theta(\sqrt N)\), any \(K=\operatorname{poly}(\log N)\) gives
\(O(\operatorname{poly}(\log N)/\sqrt N)\) success.  This closes the uniform
random, small-collection version of the high-digit/log carrier.  It does not
rule out a specially constructed deterministic or adaptive base family.

## 6. Exact finite evidence

R01 exhaustively computed the local additive distributions, used the exact
group formulas for iterated differences, exhaustively checked all principal
coordinates and high digits when \(N\le50{,}000\), and checked fixed bases
and pairs on the larger instances.

| \(p,q\) | additive two-stage | one iterated difference | three high digits |
| --- | ---: | ---: | ---: |
| 3,5 | \(7/8\) | \(1/2\) | \(1/2\) exact |
| 3,7 | \(11/12\) | \(0\) | \(1/4\) exact |
| 5,7 | \(1/2\) | \(1/2\) | \(1/4\) exact |
| 7,11 | \(1/2\) | \(2/5\) | \(31/60\) exact |
| 11,13 | \(3/10\) | \(3/10\) | \(37/120\) exact |
| 13,17 | \(9/32\) | \(5/12\) | \(9/32\) exact |
| 101,103 | \(33/850\) | \(33/850\) | \(571/10200\) exact; \(\le151/1700\) |
| 1009,1013 | \(673/170016\) | \(503/63756\) | \(\le757/85008\) |
| 10007,10009 | \(3335/8345004\) | \(3335/8345004\) | \(\le7505/8345004\) |

For \(101\cdot103\), each single high digit succeeds with exact probability
\(13/680\).  For \(10007\cdot10009\), none of the 144 fixed small unit pairs
or 64 fixed small bases produced an additive, iterated, high-digit, or rounded
identity factor hit.  The additive expected independent trial counts on the
three larger inputs are, exactly,

\[
\frac{850}{33},\qquad
\frac{170016}{673},\qquad
\frac{8345004}{3335}.
\]

Small-instance success is therefore not evidence of an inverse-polynomial
guarantee on balanced inputs.

## 7. Boundary of the kill

A nontrivial idempotent modulo \(N^2\) is already a CRT orientation and
immediately exposes a factor.  A unit idempotent is only 1, while
\(\tau_N(a)\) remains a unit for unit \(a\).  Constructing a nontrivial
idempotent from these values would require a component-selective order or
additivity mismatch; that is precisely the missing step.

The conclusions are carrier-specific:

- the principal-unit/log premise is structurally killed because \(\tau_N\)
  erases the full input kernel;
- the explicit high-digit carrier is probability-killed for polylogarithmic
  uniform collections on an infinite balanced family;
- the iterated and hidden-\(p+q\) routes reduce to scalar order behavior;
- the additive route is an \(N^2\) valuation refinement of scalar AKS-style
  Frobenius error, with exact finite failures of the hoped-for principal
  gain.

No claim is made that factoring reduces to untwisting, that order finding is
classically hard, or that every possible \(N^2\)-based construction is
impossible.
