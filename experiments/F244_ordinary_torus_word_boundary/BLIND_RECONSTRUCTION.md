# F244 blind reconstruction

## Verdict and authenticated source

**PASS, with the sampler and scope qualifications stated below.**

I reconstructed the numbered mathematical claims from the statement alone.
The authenticated `STATEMENT.md` SHA-256 is

```text
ace1c3ec745c64b4ac9383b8620720791a3c87b065307a2702baa63f1607a70a
```

The identities (4)--(8), (10)--(18), and (20) are unconditional.  Inequality
(9), and the interpretation of (19) as a probability statement, use the
standard clean F242 interface: conditional on an orientation, the two local
cyclic-group elements are independent and uniform, and the powering routine
tests the ordinary two-adic ladder.  I derive the probability implication
from that interface below.  Equiprobability of the four orientations by
itself would not imply (9).

The packet proves a boundary for the displayed signed-power grammar and for
common-order accumulation.  It does not prove an obstruction to factoring by
an algorithm outside that grammar.  The phrases about incidental zero-divisor
screens and a quarter-bit terminal have the narrower meanings made explicit
in Sections 6 and 7 below.

## 1. Prime-by-prime proof of the common-capacity identity

For a prime (r), write

\[
x_a=v_r(p-a),\qquad y_b=v_r(q-b),
\]

and put (X=v_r(A)), (Y=v_r(B)).

First suppose that (r) is odd.  Since
(gcd(p-1,p+1)=2), at most one of (x_+,x_-) is nonzero,
and its value is (X).  The same statement holds for (y_+,y_-)
and (Y).  Therefore

\[
v_r\left(\operatorname{lcm}_{a,b} d_{a,b}\right)
=\max_{a,b}\min(x_a,y_b)=\min(X,Y)=v_r(G).
\]

At (r=2), an odd integer has one shifted neighbor of 2-adic
valuation (1).  Hence, as unordered pairs,

\[
\{x_+,x_-\}=\{1,U-1\},\qquad
\{y_+,y_-\}=\{1,V-1\}.
\]

Both (U) and (V) are at least (3).  It follows that

\[
\max_{a,b}\min(x_a,y_b)
=\min(U-1,V-1)=\min(U,V)-1=v_2(G/2).
\]

Combining the odd and dyadic valuations proves

\[
\operatorname{lcm}_{a,b}d_{a,b}=G/2. \tag{4}
\]

This also records the exact 2-adic loss: it is always one factor of (2),
not a bound up to a power of (2).

## 2. Pairwise coprimality and the residual product

For every prime (r),

\[
v_r(t_{p,a})=\max(x_a-Y,0),\qquad
v_r(t_{q,b})=\max(y_b-X,0). \tag{21}
\]

For odd (r), the two (p)-side residuals cannot both contain (r),
because at most one of (x_+,x_-) is nonzero.  The same argument applies on
the (q) side.  A (p)-side and a (q)-side residual also cannot both
contain (r): that would give

\[
x_a>Y\ge y_b\quad\hbox{and}\quad y_b>X\ge x_a,
\]

which is impossible.

Equation (21) also settles (r=2).  On either one side, the shifted neighbor
with valuation (1) is completely removed because (U,V\ge3), so at most
one residual on that side can be even.  If a (p)-residual were even, then
some (x_a>V), which implies (U>V).  If a (q)-residual were even, then
some (y_b>U), which implies (V>U).  These conditions cannot occur
together.  Thus all four residuals are pairwise coprime, including at (2).

Let

\[
D=\prod_a\gcd(p-a,B)\prod_b\gcd(q-b,A).
\]

For an odd prime (r), the preceding one-shift support gives

\[
v_r(D)=2\min(X,Y)=v_r(G^2).
\]

For (r=2), set

\[
S=\sum_a\min(x_a,V)+\sum_b\min(y_b,U)=v_2(D).
\]

If (U=V), neither pair is truncated and (S=2U).  If (U<V), the first
sum is (U), while the second is

\[
\min(1,U)+\min(V-1,U)=1+U;
\]

thus (S=2U+1).  The case (V<U) is symmetric.  Consequently

\[
v_2(D)=2\min(U,V)+\mathbf 1_{U\ne V}=v_2(2^\delta G^2).
\]

Therefore (D=2^\delta G^2), and division of (AB) by (D) proves

\[
\prod_a t_{p,a}\prod_b t_{q,b}
=\frac{AB}{2^\delta G^2}. \tag{6}
\]

For four positive integers, their minimum is at most their geometric mean.
Also (AB=(p^2-1)(q^2-1)<p^2q^2=N^2).  Hence

\[
\min(t_{p,+},t_{p,-},t_{q,+},t_{q,-})
\le \left(\frac{AB}{2^\delta G^2}\right)^{1/4}
<\frac{\sqrt N}{2^{\delta/4}\sqrt G}, \tag{7}
\]

with the asserted strict final inequality.  This is only a square-root
bound in general.

## 3. The square exponent and the clean probability implication

For orientation ((a,b)), (J=ab), so

\[
(N-J)(N+J)=N^2-1. \tag{8}
\]

The local residual formula is exact.  Modulo (p-a), one has
(p\equiv a), and therefore

\[
N^2-1\equiv (aq)^2-1=q^2-1=B\pmod {p-a}.
\]

Thus

\[
\frac{p-a}{\gcd(p-a,N^2-1)}
=\frac{p-a}{\gcd(p-a,B)}=t_{p,a}.
\]

The analogous reduction modulo (q-b) gives (t_{q,b}).

Here is the probability step in a form that makes its interface dependency
explicit.  Fix an orientation and write

\[
x=t_{p,a},\qquad y=t_{q,b},\qquad
\alpha=1/x,\qquad\beta=1/y.
\]

In a cyclic local group of order (m), a uniform element is annihilated by
an exponent (E) with probability
(gcd(E,m)/m).  Hence the two local annihilation probabilities are
(alpha) and (eta).  They are independent in the clean CRT sampler.
If exactly one local component is annihilated, the gcd screen returns a
factor.

If both are annihilated, condition on that event.  Each local component is
then uniform in its (E)-torsion subgroup.  Both torsion subgroups have even
order: (N) is odd, so (8\mid N^2-1), and each local order (p-a) or
(q-b) is even.  The usual two-adic powering ladder separates the primes
whenever the two local elements have different 2-primary orders.

For completeness, if the two cyclic 2-primary groups have orders (2^s)
and (2^t), with (s,t\ge1), and (R,S) are the 2-adic exponents of the
orders of independent uniform elements, then, for (s\le t),

\[
\Pr(R=S)
=\frac{4^s+2}{3\,2^{s+t}}\le\frac12.
\]

Thus the ladder separates with conditional probability at least (1/2).
The clean powered-factor probability for this orientation is consequently
at least

\[
\begin{aligned}
P_{a,b}
&\ge \alpha(1-\beta)+\beta(1-\alpha)+\tfrac12\alpha\beta\\
&=\alpha+\beta-\tfrac32\alpha\beta\\
&\ge\tfrac14(\alpha+\beta),
\end{aligned}
\]

because the difference in the last line is
(	frac34(\alpha+\beta-2\alpha\beta)\ge0).

The four orientations are equiprobable.  Each one-sided residual occurs in
two orientations, so averaging gives

\[
\Pr(\mathrm{factor})
\ge\frac18\sum_{z\in
\{t_{p,+},t_{p,-},t_{q,+},t_{q,-}\}}\frac1z. \tag{9a}
\]

AM--GM applied to the four reciprocals gives

\[
\frac18\sum_z\frac1z\ge\frac1{2(\prod_z z)^{1/4}}. \tag{9b}
\]

Using (6),

\[
\frac1{2(\prod_z z)^{1/4}}
=\frac{2^{\delta/4-1}\sqrt G}{(AB)^{1/4}}
>\frac{2^{\delta/4-1}\sqrt G}{\sqrt N}, \tag{10}
\]

as claimed.

The proof above verifies the implication from the clean sampler interface.
If “clean sampler” did not include conditional local uniformity,
independence, and the two-adic ladder, those properties would have to be
proved separately; orientation equiprobability alone is insufficient.

## 4. Exact signed-power support

Let (h=\operatorname{ord}_\ell(N)), where (ell) is odd and
(ell\nmid N).  If (h\nmid k), then (N^k\not\equiv1\pmod\ell).
If (k=hr), odd-prime LTE applied to ((N^h)^r-1) gives

\[
v_\ell(N^k-1)=v_\ell(N^h-1)+v_\ell(r),
\]

which proves (11).

The congruence (N^k\equiv-1\pmod\ell) holds exactly when (h) is even
and (k\equiv h/2\pmod h).  Equivalently,
(k=(h/2)u) with (u) odd.  In that case, LTE applied to
((N^{h/2})^u+1) gives

\[
v_\ell(N^k+1)=v_\ell(N^{h/2}+1)+v_\ell(u),
\]

and otherwise the valuation is zero.  This proves (12).

If (ell\mid p-a), then (p\equiv a\pmod\ell), so
(N\equiv aq\pmod\ell).  Thus (11)--(12) are controlled by the order of
(aq); the (q-b) statement is symmetric.

## 5. Sequential CRT/Linnik construction and the input-length link

I now construct the infinite family in (13)--(16).  Use Linnik's theorem in
the following standard uniform form: there are absolute constants (C_L)
and (L) such that the least prime in every reduced residue class modulo
(M) is at most (C_LM^L).

Let (X) tend to infinity.  Repeated use of Bertrand's theorem supplies
four distinct primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_-
\quad\text{between }X\text{ and }16X.
\]

Take all four larger than (3).  Choose primitive roots modulo each marker
prime.

Use CRT to prescribe (p) by

\[
\begin{array}{lll}
p\equiv13\pmod {72},
&p\equiv 1\pmod{\lambda_+},
&p\equiv-1\pmod{\lambda_-},\\
p\equiv g_+\pmod{\rho_+},
&p\equiv g_-\pmod{\rho_-},
\end{array} \tag{22}
\]

where each (g_b) is a primitive root modulo (ho_b).  This is a reduced
class.  Linnik therefore supplies a prime (p) in it, with

\[
p\le C_1X^{4L}. \tag{23}
\]

After (p) is fixed, consider every prime (r>3) dividing (p^2-1).
For (r=\lambda_a), prescribe (q) to be a primitive root modulo (r).
For every other such (r), choose any nonzero residue other than
(1) and (-1); such a residue exists because (r\ge5).  Also prescribe

\[
q\equiv11\pmod {72},\qquad
q\equiv1\pmod{\rho_+},\qquad
q\equiv-1\pmod{\rho_-}. \tag{24}
\]

There is no CRT conflict.  In particular, neither (ho_b) divides
(p^2-1), because (p) is primitive modulo (ho_b>3), and hence is not
(pm1) there.  The resulting class is reduced.  Its modulus is at most

\[
72\rho_+\rho_-\operatorname{rad}(p^2-1)
\le C_2X^2p^2.
\]

Another application of Linnik gives a prime (q) with

\[
q\le C_3(X^2p^2)^L
\le C_4X^{,2L+8L^2}. \tag{25}
\]

The congruences modulo (8) in (22) and (24) are different, so (p\ne q).
Both primes are odd.

The marker divisibilities and primitive-root conditions are exactly
(14)--(15).  The congruences modulo (72) give

\[
\begin{array}{c|cc}
&2\text{-adic}&3\text{-adic}\\ \hline
p-1&v_2=2&v_3=1\\
p+1&v_2=1&v_3=0\\
q-1&v_2=1&v_3=0\\
q+1&v_2=2&v_3=1.
\end{array}
\]

For every prime (r>3) dividing (p^2-1), construction (24) makes
(q\not\equiv\pm1\pmod r).  Therefore no such (r) divides any shifted
common divisor.  The displayed 2- and 3-adic table now gives

\[
d_{+,+}=2,qquad d_{+,-}=12,qquad
d_{-,+}=2,qquad d_{-,-}=2. \tag{16}
\]

By (4), this also gives (G=24).

It remains to prove that the marker primes are exponential in the input
length, rather than merely large in the construction parameter.  From
(23)--(25), for

\[
K=8L^2+6L
\]

and an absolute (C_5),

\[
N=pq\le C_5X^K.
\]

Thus (n\le K\log_2X+O(1)).  For example, after discarding finitely many
members, (c=1/(2K)) gives

\[
\lambda_+,\lambda_-,\rho_+,\rho_->X>2^{cn}. \tag{13}
\]

As (X\to\infty), the marker primes, and hence (p,q,N), are unbounded;
passing to distinct values gives an infinite family.  This proves the
required input-length link with one absolute (c>0).

## 6. The adaptive numerical-bit-length signed-word quantifier

Fix any numerical quasipolynomial (Q(n)).  It satisfies

\[
Q(n)=2^{o(n)}.
\]

For a marker prime (ell), the construction makes the other factor a
primitive root modulo (ell).  If (g) is primitive modulo (ell), then

\[
\operatorname{ord}_\ell(g)=\ell-1,qquad
\operatorname{ord}_\ell(-g)
=\frac{\ell-1}{\gcd(\ell-1,1+(\ell-1)/2)}
\ge\frac{\ell-1}{2}.
\]

Consequently every one of the four marker orders
(h=\operatorname{ord}_\ell(N)) is at least ((\ell-1)/2).

Suppose a word (W) of form (17) has numerical binary length at most
(Q(n)).  Each of its factors is at most (W), while

\[
N^{k_j}-1\ge N^{k_j}/2.
\]

It follows that every (k_j\le Q(n)+1).  For all sufficiently large family
members,

\[
Q(n)+1<\frac{\ell-1}{4}\le\frac h2
\]

for every marker (ell), because (ell>2^{cn}) whereas (Q(n)=2^{o(n)}).
Equations (11)--(12) then show that no marker divides any factor
(N^{k_j}-\sigma_j).  Powers and products cannot introduce a new prime
divisor, so

\[
\gcd(W,\lambda_+\lambda_-\rho_+\rho_-)=1. \tag{18}
\]

This proof is pointwise in the final word.  Therefore the choices of
(s,k_j,e_j,\sigma_j) can depend adaptively on all prior observations: on
every realized branch whose final integer has grammar (17) and numerical
binary length at most (Q(n)), (18) holds.  The statement does **not** cover
a compressed formal expression whose numerical value has more than (Q(n))
bits, nor a final exponent or integer outside grammar (17).

For orientation ((a,b)), modulo (lambda_a) one has

\[
N-ab\equiv a(q-b)\not\equiv0,
\]

because (q) is primitive modulo (lambda_a>3), and hence is not
(pm1).  Together with (18), this shows that (lambda_a) survives in the
(p)-side residual after the base and (W).  Similarly,

\[
N-ab\equiv b(p-a)\not\equiv0\pmod{\rho_b},
\]

so (ho_b) survives on the (q) side.

Under the same clean uniform-local-element interface as in Section 3, local
annihilation has probability at most (1/\lambda_a) and
(1/\rho_b), respectively.  Every clean powered factor event is contained
in their union.  Therefore

\[
\Pr(\mathrm{clean\ powered\ factor}\mid a,b)
\le\frac1{\lambda_a}+\frac1{\rho_b}
\le2^{1-cn}. \tag{19}
\]

This remains valid when (W) is selected from the sampled element: an
exponent coprime to (ell) cannot annihilate an element whose order has a
nontrivial (ell)-part.  Adaptivity can select among exponents, but (18)
makes every allowed selection coprime to all four markers.

For the standard sampler's constant number of incidental tests of uniformly
sampled values for divisibility by (p) or (q), the probability is
(O(1/p+1/q)=2^{-\Omega(n)}), since (p) and (q) exceed their respective
markers up to an immaterial constant.  The same conclusion holds for a
fixed number of bounded-degree polynomial zero tests.  It is not a claim
about an unspecified screen with an unbounded number of roots.

A numerical-quasipolynomial number of fresh trials has total success
probability at most

\[
2^{o(n)}2^{-\Omega(n)}=2^{-\Omega(n)}
\]

by the conditional union bound, including adaptive trial selection.  Thus
this signed-word trial mechanism cannot give a quasipolynomial-time solver
for this family.  This conclusion is not a factoring lower bound: another
mechanism can fall outside the word grammar or the clean powered-factor
event.

## 7. Common-order accumulation

Every exact order common to the two local cyclic groups in orientation
((a,b)) divides (d_{a,b}).  Equation (16) therefore implies that the lcm
of all common-order information from the four sign orientations divides
(12).  Combining a residue modulo such an order with a known residue
modulo (2^t) can produce modulus no larger than

\[
\operatorname{lcm}(2^t,12)=3\cdot2^t\qquad(t\ge2), \tag{20}
\]

which is only a constant-factor enlargement.  This verifies the formal
modulus claim.  Its “quarter-bit terminal” interpretation applies only to
methods whose additional information consists of these common orders; it
does not constrain the excluded difference, carry, quotient, retained-
relation, or other factoring mechanisms.

## Final scope assessment

The exact conservation law, the one-word square exponent, the signed-power
support formulas, the infinite CRT/Linnik obstruction family, its
exponential marker-to-input relation, and the adaptive numerical-bit-length
quantifier all reconstruct.  The result remains a special-family boundary
for a named exponent grammar.  It is neither an all-input factoring
algorithm nor a general lower bound for classical factoring.
