# F46 proof-only kill: Lucas-torus factor gaps and the generic shared-exponent boundary

**Family:** F27, with comparisons to F02/P20--P21 and F07/P12.

**Status:** self-audited. This is the preregistered mandatory
proof-only kill test. No finite search, benchmark, or other mathematical
computation was run. No canonical durable-state file was changed.

**Closest prior routes and material difference.** F02/P20--P21 asks for a
polylogarithmic exact evaluator of an exponentially long multiplicative
order-threshold product. F07/P12 studies dense moment/spectral
representations of one modular-multiplication action. F27 instead produces
polynomially many ordinary, nonzero base/image equations in quadratic
norm-one tori, all carrying the magnitude of the same factor gap. Thus its
terminal question is a shared-exponent decoder, not the product evaluator of
F02 or the dense reconstruction premise tested by P12.

## Verdict

The algebraic proposal survives on the distinct odd-semiprime promise; the
identities themselves do not require balance. If

\[
N=pq,\qquad 3\le p<q
\]

are distinct primes, every denominator-clean sample has the pointwise
identity

\[
U_D(t)^{N-1}=U_D(t)^{q-p}
\]

in the local-sign orientation \((+,-)\), and the pointwise identity

\[
U_D(t)^{N-1}=U_D(t)^{-(q-p)}
\]

in orientation \((-,+)\). The orientations of a discriminant chosen
uniformly from the units conditional on Jacobi symbol \(-1\) are exactly
fair. A denominator pole is not a malformed sample: its gcd with \(N\)
returns the unique local split prime.

There is also a rigorous narrow kill. In \(K\) independently and randomly
encoded cyclic groups of a common prime order \(\ell\), even if all signs are
given to the algorithm, \(Q\) total generic operations/equality tests recover
a shared uniform exponent with probability at most

\[
\frac1\ell+
\frac{\binom{Q+3}{2}+3(K-1)}{\ell}
\le
\frac1\ell+
\frac{\binom{Q+3K}{2}}{\ell}.
\]

The corresponding bound for an exponent uniform on any known \(H\)-element
subset is \((1+C)/H\), with the same collision count \(C\). Thus merely
amortizing opaque, independently encoded prime-order relations does not give
polynomial-time recovery when \(K,Q\ll\sqrt\ell\) (or
\(K,Q\ll\sqrt H\)).

This does **not** kill F27. The actual Lucas rings have public coordinates,
zero divisors, cross-discriminant algebra, composite and unequal local group
orders, bases of nonmaximal order, and a factor gap that is fixed by the
input rather than uniform in a prime field. Interval algorithms and
coordinate-specific algorithms remain outside the theorem. The positive
survivor is therefore an exact, efficiently generated, promise-only
factor-gap relation plus a verified gap-to-factor map; the missing lemma is
a polynomial-time decoder exploiting structure absent from the generic
model. No all-input factoring reduction has been obtained.

## 1. Quadratic algebra, conjugation, norm, and units

Let \(N\) be odd, put \(R=\mathbb Z/N\mathbb Z\), take
\(D\in R^\times\), and define

\[
A_D=R[w]/(w^2-D).
\]

The map

\[
\overline{a+bw}=a-bw
\]

is an \(R\)-algebra involution. Its norm is

\[
\operatorname{Nm}(a+bw)
=(a+bw)(a-bw)=a^2-Db^2\in R.
\]

An element \(x\in A_D\) is a unit exactly when
\(\operatorname{Nm}(x)\in R^\times). One direction follows from

\[
x^{-1}=\overline x\,\operatorname{Nm}(x)^{-1};
\]

the other follows because conjugation preserves units and
\(\operatorname{Nm}(x)=x\overline x\). Hence

\[
T_D(R)=\{x\in A_D^\times:\operatorname{Nm}(x)=1\}
\]

is a group.

For \(t\in R\), the denominator \(1-tw\) is a unit exactly when

\[
z_D(t):=\operatorname{Nm}(1-tw)=1-Dt^2
\]

is a unit. In that event define

\[
\begin{aligned}
U_D(t)
&=\frac{1+tw}{1-tw}
=\frac{(1+tw)^2}{1-Dt^2}\\
&=\frac{1+Dt^2}{1-Dt^2}
 +\frac{2t}{1-Dt^2}w.
\end{aligned}
\]

The numerator and denominator have the same norm, so
\(U_D(t)\in T_D(R)\).

## 2. Exact local Cayley parametrization

Fix an odd prime \(r\nmid D\), write \(k=\mathbb F_r\), and put

\[
A_{D,r}=k[w]/(w^2-D),\qquad
T_D(k)=\ker(\operatorname{Nm}:A_{D,r}^\times\to k^\times).
\]

Let \(\chi_r(D)=(D/r)\).

### 2.1 The map and its inverse

The local Cayley map

\[
c_D:t\longmapsto \frac{1+tw}{1-tw}
\]

is a bijection

\[
\{t\in k:1-Dt^2\ne0\}
\xrightarrow{\ \sim\ }
T_D(k)\setminus\{-1\}.
\]

It never takes the value \(-1\), since

\[
1+tw=-(1-tw)
\]

would give \(2=0\). Conversely, write \(u=a+bw\in T_D(k)\). Its norm
equation is

\[
a^2-Db^2=1.
\]

If \(a=-1\), this forces \(b=0\), so \(u=-1\). Otherwise set

\[
t=\frac{b}{a+1}.
\]

Then

\[
1-Dt^2
=\frac{(a+1)^2-Db^2}{(a+1)^2}
=\frac{2}{a+1}\ne0.
\]

Substitution into the displayed coefficient formula for \(U_D(t)\) gives
its coefficients \(a\) and \(b\). This proves both surjectivity and the
inverse formula; uniqueness is immediate.

### 2.2 Pole counts and local group orders

If \(\chi_r(D)=+1\), choose \(\delta^2=D\). There are exactly two
denominator poles,

\[
t=\pm\delta^{-1}.
\]

The split isomorphism

\[
a+bw\longmapsto(a+b\delta,a-b\delta)
\]

identifies conjugation with interchange of the two coordinates and norm
with their product. Thus

\[
T_D(k)\simeq\{(x,x^{-1}):x\in k^\times\}\simeq k^\times,
\qquad |T_D(k)|=r-1.
\]

The \(r-2\) nonpole parameters therefore match the \(r-2\) elements after
excluding \(-1\).

If \(\chi_r(D)=-1\), there are no denominator poles and
\(A_{D,r}=\mathbb F_{r^2}\). Since

\[
w^r=wD^{(r-1)/2}=-w,
\]

conjugation is the Frobenius \(x\mapsto x^r\), and the displayed norm is the
field norm. Its kernel has order

\[
\frac{r^2-1}{r-1}=r+1.
\]

All \(r\) parameters match the \(r\) norm-one elements other than \(-1\).
In unified notation,

\[
|T_D(\mathbb F_r)|=r-\chi_r(D).
\]

## 3. CRT sampling and the exact denominator-gcd law

Now assume

\[
N=pq,\qquad 3\le p<q
\]

with \(p,q\) prime, and let \(D\in R^\times\) have Jacobi symbol

\[
\left(\frac DN\right)
=\left(\frac Dp\right)\left(\frac Dq\right)=-1.
\]

There is a unique split local prime. Write the orientation as

\[
(+,-) \quad\text{if}\quad
\left(\frac Dp\right)=+1,
\ \left(\frac Dq\right)=-1,
\]

and analogously for \((-,+)\).

For uniform \(t\in R\), its CRT components are independent uniform elements
of \(\mathbb F_p\) and \(\mathbb F_q\). Section 2 gives the complete gcd
law:

\[
\begin{array}{c|ccc}
\text{orientation}&\Pr(\gcd(z_D(t),N)=1)
&\Pr(\gcd(z_D(t),N)=p)&\Pr(\gcd(z_D(t),N)=q)\\ \hline
(+,-)&1-2/p&2/p&0\\
(-,+)&1-2/q&0&2/q.
\end{array}
\]

No other gcd value occurs. In particular, a pole gives the unique split
prime as a proper factor, and a full gcd \(N\) is impossible because the
nonsplit component has no pole.

If one resamples \(t\) while keeping \(D\) fixed, a clean parameter appears
after expected

\[
\frac1{1-2/r_s}\le3
\]

trials, where \(r_s\in\{p,q\}\) is the split prime. Conditional on being
clean for this fixed \(D\), the local Cayley points are independent and
uniform on

\[
\bigl(T_D(\mathbb F_p)\setminus\{-1\}\bigr)
\times
\bigl(T_D(\mathbb F_q)\setminus\{-1\}\bigr).
\]

The word "uniform" here does not say that either point is a generator.

## 4. Exact orientation distribution, and why pair conditioning differs

Under CRT, each of the four pairs of nonzero Legendre signs contains

\[
\frac{p-1}{2}\frac{q-1}{2}
\]

units \(D\). Therefore, for \(D\) uniform in \(R^\times\) conditional on
Jacobi symbol \(-1\),

\[
\Pr((+,-))=\Pr((-,+))=\frac12.
\]

Independent choices of \(D\) give independent fair orientations. The
orientation remains hidden without the factors.

This statement is about choosing \(D\) first. There are three different
sampling procedures that must not be conflated.

1. **Keep \(D\), resample \(t\).** Choose a fair \(D\), and on a pole keep
   that \(D\) while resampling \(t\). The eventual clean relation still has
   exactly fair orientation, because every chosen \(D\) eventually produces
   one. The number of rejected \(t\)'s is nevertheless correlated with the
   orientation; fairness here is the marginal law of the retained \(D\), not
   a claim after conditioning on that retry count.

2. **Return the pole gcd.** A pole already returns \(p\) or \(q\), so an
   actual factoring routine should normally stop. Fairness of the initially
   chosen \(D\) is unchanged; conditioning afterward on the branch that did
   not factor is a different question.

3. **Condition or reject whole pairs.** If \((D,t)\) is sampled jointly and
   the whole pair is rejected unless its denominator is clean, the accepted
   orientation is not fair. Exactly

   \[
   \Pr((+,-)\mid\mathrm{clean})
   =\frac{1-2/p}{(1-2/p)+(1-2/q)},
   \]

   \[
   \Pr((-,+)\mid\mathrm{clean})
   =\frac{1-2/q}{(1-2/p)+(1-2/q)}.
   \]

   Since \(p<q\), clean-pair conditioning favors \((-,+)\), whose split
   prime is the larger one.

Averaging the gcd law over the initially fair \(D\) gives the further exact
law

\[
\Pr(\gcd(z_D(t),N)=p)=\frac1p,
\quad
\Pr(\gcd(z_D(t),N)=q)=\frac1q,
\]

\[
\Pr(\gcd(z_D(t),N)=1)=1-\frac1p-\frac1q.
\]

Thus conditioning one-shot survivors produces the bias above, whereas
retaining \(D\) during \(t\)-resampling preserves fair signs.

## 5. The pointwise signed factor-gap identity

Put

\[
g=q-p>0.
\]

CRT gives

\[
T_D(R)\simeq T_D(\mathbb F_p)\times T_D(\mathbb F_q).
\]

For every local norm-one element, its exponent may be reduced modulo the
local group order from Section 2. The four required congruences are

\[
\begin{array}{c|c|c|c|c}
\text{orientation}&\text{prime}&|T_D(\mathbb F_r)|
&N-1\pmod{|T_D(\mathbb F_r)|}
&\text{gap exponent}\\ \hline
(+,-)&p&p-1&q-1&g\equiv q-1\\
(+,-)&q&q+1&-p-1&g\equiv-p-1\\
(-,+)&p&p+1&-q-1&-g\equiv-q-1\\
(-,+)&q&q-1&p-1&-g\equiv p-1.
\end{array}
\]

For example, modulo \(q+1\) one has \(q\equiv-1\), so both \(N-1\) and
\(g\) are congruent to \(-p-1\) in orientation \((+,-)\). The other rows
are identical one-line reductions.

It follows, pointwise for **every** \(U\in T_D(R)\), that

\[
U^{N-1}=U^g \quad\text{in orientation }(+,-),
\]

and

\[
U^{N-1}=U^{-g} \quad\text{in orientation }(-,+).
\]

Negative powers are legitimate because \(U\) is a unit. In particular these
identities hold for every denominator-clean Cayley sample. They require
neither a generator nor a probabilistic order assertion.

## 6. Uniform generation and bit complexity

Let \(n=\lceil\log_2(N+1)\rceil\), and let \(M(n)\) denote the bit cost of
multiplying two \(n\)-bit integers. Everything up to the missing decoder is
uniformly computable in polynomial bit complexity.

An exact uniform discriminant can be generated without knowing \(p,q\):
sample a uniform residue \(D\bmod N\), compute \(d=\gcd(D,N)\), return \(d\)
if it is proper, retry if \(d=N\), and otherwise compute the Jacobi symbol
and accept exactly when it is \(-1\). Conditional on acceptance this is
uniform over the required set. On the distinct odd-semiprime promise, one
raw draw is accepted with probability

\[
\frac{\varphi(N)}{2N}
=\frac{(p-1)(q-1)}{2pq}\ge\frac4{15},
\]

unless a nonunit draw has already exposed a factor. Exact uniform residues
use expected \(O(n)\) fair bits by ordinary rejection from \(n\)-bit strings.

For a uniform \(t\), compute \(z=1-Dt^2\bmod N\) and its gcd with \(N\). A
proper gcd is a factor. If it is 1, extended Euclid gives \(z^{-1}\bmod N\),
and the two coefficients of \(U_D(t)\) are

\[
a=(1+Dt^2)z^{-1},\qquad b=2tz^{-1}\pmod N.
\]

Multiplication in \(A_D\) is

\[
(a+bw)(c+dw)=(ac+Dbd)+(ad+bc)w,
\]

so it uses \(O(1)\) modular multiplications. Binary powering to
\(V=U^{N-1}\) uses \(O(n)\) such ring multiplications. With fast gcd and
extended gcd, one complete relation therefore costs

\[
O\bigl(nM(n)+M(n)\log n\bigr)
\]

bit operations; the classical bound \(M(n)=O(n^2)\) is already polynomial.
All stored coefficients have \(O(n)\) bits. Producing \(K\) relations costs
\(O(KnM(n))\) expected bit operations and \(O(Kn)\) expected random bits,
unless a denominator or discriminant gcd factors \(N\) first. If clean
relations with fair orientations are specifically required, resample \(t\)
for the same \(D\), at expected multiplicative cost at most 3.

## 7. Exact conditional gap-to-factor reduction

The deterministic map from a candidate gap \(h\) to factors is elementary
and fully verifiable:

1. Reject unless \(0<h<N\).
2. Compute \(\Delta=h^2+4N\) and \(s=\lfloor\sqrt\Delta\rfloor\).
3. Reject unless \(s^2=\Delta\), \(s\equiv h\pmod2\), and
   \(1<(s-h)/2<(s+h)/2<N\).
4. Put
   \[
   p'=(s-h)/2,\qquad q'=(s+h)/2,
   \]
   and return them only after exact verification \(p'q'=N\).

For \(h=g=q-p\),

\[
g^2+4N=(q-p)^2+4pq=(p+q)^2,
\]

so this returns exactly \(p,q\). Conversely, every accepted output is an
actual nontrivial factorization, even off promise. Integer squaring, square
root, parity, and multiplication on \(O(n)\)-bit values have polynomial bit
cost. A polynomial-time decoder cannot hide a superpolynomial output: a
candidate with more than \(n\) bits is rejected immediately.

Consequently, suppose a decoder has the following **promise contract**. For
every distinct odd semiprime \(N=pq\), from \(K=\operatorname{poly}(n)\)
explicit triples

\[
(D_i,U_i,V_i),\qquad V_i=U_i^{N-1},
\]

generated as above with \(D_i\) chosen first and \(t_i\) resampled for that
same \(D_i\), it returns \(|q-p|\) with probability at least
\(1/\operatorname{poly}(n)\) in polynomial bit time. The signs may remain
hidden; they are independent fair signs by Section 4. Then repeatedly
generate a transcript, run the decoder, and apply the verified map above.
A discriminant or denominator gcd may terminate even earlier. Every returned
factor is correct, and independent retries have polynomial expectation and
terminate almost surely. Thus such a decoder gives a Las Vegas polynomial-
time algorithm for the **distinct odd semiprime promise problem**.

This is not an all-input reduction. For a prime square, every unit has
Jacobi symbol \(+1\) with respect to the squared prime factor, so the stated
orientation source is absent. Prime powers require lifted local groups and
are not covered by the field-order argument. With three or more distinct
prime factors, Jacobi \(-1\) allows many sign patterns and \(N-1\) does not
collapse to one two-factor gap. The square-discriminant reconstruction
\(g^2+4N=(p+q)^2\) is specifically two-factor. No reduction from arbitrary
composites, repeated factors, even inputs, or complete recursive
factorization to this decoder has been proved. Balance is unnecessary for
the identities, but any claimed short-interval decoder would introduce an
additional quantitative balance promise.

## 8. A multi-group generic shared-exponent theorem

### 8.1 Model and quantifiers

Let \(\ell\) be prime. For \(1\le i\le K\), let
\(G_i=\langle g_i\rangle\) be a cyclic group of order \(\ell\). Give each
group its own tagged label set and an independently uniform random bijection

\[
\xi_i:\mathbb F_\ell\longrightarrow\mathcal L_i,
\qquad x\longmapsto\text{the opaque label of }g_i^x.
\]

The label sets are disjoint by their group tags. Fix arbitrary public signs
\(\sigma_i\in\{+1,-1\}\). Draw \(e\) uniformly from
\(\mathbb F_\ell\), independently of all encodings, and give the algorithm

\[
\xi_i(0),\qquad \xi_i(1),\qquad \xi_i(\sigma_i e)
\]

for every \(i\). Supplying the identity labels only strengthens the
algorithm.

The algorithm may know \(K,\ell\), all signs, and the exponent's prior. It
may be randomized, adaptive across all \(K\) transcripts, nonuniform in
these public parameters, and computationally unbounded between oracle
calls. Its group access is generic: multiplication, inverse, or known-scalar
powering takes previously received handles from one tagged group and returns
one handle in that same group. No cross-group operation, pairing, coordinate
inspection, or guessed unreceived handle is allowed. Equality of handles may
be tested. Count at most \(Q\) total generic operations and equality tests;
only the operations create new handles. The output is one scalar
\(\widehat e\in\mathbb F_\ell\).

The probability below is jointly over uniform \(e\), the \(K\) independent
random encodings, and the algorithm's coins. For every algorithm satisfying
the preceding quantifiers,

\[
\Pr[\widehat e=e]
\le
\min\!\left\{1,
\frac1\ell+
\frac{\binom{Q+3}{2}+3(K-1)}{\ell}
\right\}.
\tag{1}
\]

In particular this is

\[
\frac1\ell+O\!\left(\frac{(Q+K)^2}{\ell}\right),
\]

with an absolute, explicit constant. It implies
\(Q+3K=\Omega(\sqrt\ell)\) for constant recovery probability.

### 8.2 Formal-expression proof

Fix the algorithm's coins and run an ideal symbolic oracle. In group \(i\),
associate to every handle an affine formal exponent

\[
f(X)=a+bX\in\mathbb F_\ell[X].
\]

The three initial expressions are \(0,1,\sigma_iX\). A group product adds
two affine expressions, inversion negates one, and known-scalar powering
multiplies one by a known scalar. Even if a scalar is selected adaptively
from random opaque labels, it is fixed once this ideal transcript is fixed,
so the resulting expression remains affine. The symbolic oracle assigns a
fresh uniformly random unused label to every new formal expression and
reuses the old label exactly when the coefficient pairs \((a,b)\) are
identical. These proof-side expressions are not shown to the algorithm.

Let \(q_i\) be the number of operation outputs in group \(i\), so

\[
\sum_iq_i\le Q.
\]

At most

\[
m_i\le3+q_i
\]

formal expressions have appeared in group \(i\). A surprise collision at a
concrete exponent \(x\) means that two distinct affine formal expressions in
the same group evaluate equally at \(X=x\). Their nonzero affine difference
has at most one root in \(\mathbb F_\ell\). Hence the set \(B\) of exponents
that can cause any surprise collision along this ideal run satisfies

\[
|B|\le C:=\sum_{i=1}^K\binom{m_i}{2}
\le\sum_{i=1}^K\binom{3+q_i}{2}.
\tag{2}
\]

Convexity, with \(\sum_iq_i\le Q\), gives

\[
C\le\binom{Q+3}{2}+3(K-1)
\le\binom{Q+3K}{2}.
\tag{3}
\]

Pairs with the same slope and different constant terms actually have no
root, so (2) is deliberately an upper bound.

For \(e\notin B\), every distinct encountered formal expression evaluates
to a distinct group element within its group. The ideal assignment of
random unused labels can then be extended to a uniformly random full
encoding \(\xi_i\). Under this coupling the real and ideal transcripts are
identical until termination. This remains true under full adaptivity: any
first deviation would itself be a collision among expressions already
created on the common ideal prefix, and is therefore charged to \(B\).

The ideal transcript, including the algorithm's output, is independent of
the uniform \(e\). Thus its chance of guessing \(e\) is exactly at most
\(1/\ell\). The real execution can differ only on the collision event, whose
probability is at most \(C/\ell\). Equations (2)--(3) prove (1). Averaging
the argument over the algorithm's coins proves the randomized case. Notice
that the proof charges all pairs of materialized handles, so it is still
valid if label equality is noticed without an explicitly counted equality
query.

### 8.3 A known subset or interval

The same proof works without change when \(e\) is uniform on any fixed,
public subset \(S\subseteq\mathbb F_\ell\) of size \(H\), including a
cyclic or ordinary interval embedded without ambiguity. Every distinct
affine pair has at most one collision point in \(S\), so

\[
\Pr[\widehat e=e]
\le
\min\left\{1,\frac{1+C}{H}\right\}.
\tag{4}
\]

If the algorithm outputs a list of at most \(L\) candidates, the numerator
1 in (4) becomes \(L\). For an arbitrary nonuniform prior \(\mu\), the same
coupling yields the useful but sometimes vacuous bound

\[
\Pr[\widehat e=e]\le(C+1)\max_x\mu(x).
\tag{5}
\]

The \(\Theta(\sqrt H)\) generic scale in (4) is consistent with baby-step--
giant-step and interval discrete-log methods; it does not say that intervals
are unusable. In particular, if a separate promise made \(H\) polynomial in
\(n\), this generic bound would itself permit polynomial work.

## 9. Exact scope of the generic kill

The theorem in Section 8 does not model the actual F27 transcript for each
of the following independent reasons.

* **Public, correlated encodings.** A Lucas element is the explicit pair
  \(a+bw\) over the same ring \(\mathbb Z/N\mathbb Z\), not a random opaque
  label. Coordinates can be inspected, combined with integer arithmetic,
  and subjected to gcds with \(N\). Random-encoding simulation deliberately
  removes all of this information.

* **Cross-discriminant coordinate algebra.** Different \(D_i\) still use
  public coefficient pairs over one base ring. An algorithm may form
  polynomial or rational coordinate relations, resultants, gcds, or
  discriminant-changing maps across samples. The generic model tags the
  groups and forbids every cross-group operation. No claim is made that such
  explicit relations are useful or useless.

* **Composite and unequal orders.** The actual local orders are
  \(p-1,p+1,q-1,q+1\), selected by orientation. They are generally composite
  and unequal, and the global norm-one group is a product of two cyclic
  groups. Different orientations even select different order pairs. There
  is no common prime order \(\ell\) in the construction.

* **Non-generator bases.** A Cayley point is uniform only on the local torus
  with \(-1\) removed. Its order may be any divisor of the local torus
  order. Section 5 is pointwise precisely so that it does not assume
  generation; Section 8 fixes generators.

* **Different exponent prior.** For a fixed input \(N\), the gap \(q-p\) is
  deterministic. Across any chosen family of semiprimes its distribution is
  neither proved uniform nor even naturally valued in one common prime
  field. Bound (5) becomes vacuous for a point mass. An average-case generic
  bound therefore cannot be promoted to a worst-case factoring lower bound.

* **Intervals remain live.** A balance promise may put \(q-p\) in a known
  interval, and interval discrete-log methods have a different quantitative
  target. Equation (4) only gives a birthday-scale generic bound for a
  *uniform* interval exponent. It neither supplies nor rules out an explicit
  Lucas-coordinate interval algorithm, and it does not justify any
  unproved distribution for factor gaps.

* **Ring operations can expose factors.** Equality is not the only terminal
  observation over \(\mathbb Z/N\mathbb Z\). A nonunit coordinate,
  denominator, determinant, or cross-relation can yield a proper gcd. The
  prime-order group oracle has no zero divisors and no analogue of this
  output channel.

Accordingly, the proved generic statement supports only this narrow
classification: **method failure for the assertion that polynomially many
independently random-encoded prime-order base/image relations, by their
number alone, force polynomial-time shared-exponent recovery.** It does not
say that multiple relations are useless outside that model.

## 10. Relation to F02/P20--P21 and F07/P12

P20's surviving multiplicative-torus target is a uniform exact evaluator for

\[
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}\pmod N.
\]

Its zero predicate tests a local order threshold, and the conditional P20
reduction covers arbitrary integers after perfect-power handling and
recursion. P21 rules out only several literal compressions: fixed positive
binomial lists, one-lcm replacement, the literal two-child recurrence, and
displayed grouping/materialization shortcuts. It proves no general circuit
lower bound.

F27 neither evaluates that exponential product nor compresses its factors.
It computes \(K\) ordinary powers \(U_i^{N-1}\) in polynomial time and asks a
decoder to use their typical nonzero values. The generic lower bound here is
not a circuit lower bound for \(S_m\), so it does not close P20's evaluator
gap or strengthen P21 beyond its stated scope. Conversely, a future P20
evaluator would already give all-input factoring and would not need F27's
promise-only gap decoder.

P12 proves that standard point and trace probes of one modular-
multiplication operator can have exponentially large dense support on an
unconditional fixed-pair family. It expressly leaves adaptive binary-index
queries, sparse descriptions, arbitrary probes, resampling, and non-Prony
algorithms open. Section 8 allows arbitrary adaptive generic operations and
therefore addresses a different abstraction, but only after replacing
explicit modular arithmetic by independent opaque prime-order encodings and
making the exponent uniform. Neither theorem subsumes the other. In
particular, this generic theorem cannot be cited as a lower bound against
F07's explicit arithmetic algorithms, while P12 supplies no shared-
exponent lower bound for F27.

## 11. Precise survivor and next decisive test

What survives is the following exact conditional mechanism:

* factor-free, polynomial-bit generation of explicit Lucas-torus relations;
* a proper factor on every denominator pole;
* exact fair hidden orientations when \(D\) is chosen first and \(t\) is
  resampled for that fixed \(D\);
* the pointwise common-magnitude equations
  \(V_i=U_i^{\pm(q-p)}\); and
* a deterministic, fully verified polynomial-bit map from \(q-p\) to the two
  promised factors.

The next decisive test must therefore be coordinate-specific: give a
uniform polynomial-time algorithm that recovers the magnitude from these
explicit \(A_{D_i}\) coordinates on every stated distinct-semiprime input,
with a symbolic success and bit-complexity proof. Legitimate mechanisms
include a proved interval method under an explicit promise, cross-
discriminant algebra, unequal-order CRT information, or a deliberately
nonuniform sample distribution. Any such result must then separately bridge
the present distinct-semiprime promise to prime powers, repeated factors,
and arbitrary composites before it can address the top-level statement.
