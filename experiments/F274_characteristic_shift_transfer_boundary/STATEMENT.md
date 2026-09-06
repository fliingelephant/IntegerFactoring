# F274 — characteristic-shift and rational-gauge boundary for interval products

## Status and scope

This is a proof-only candidate with an author self-audit.  It studies a
characteristic-specific route left open by P223/F273: use translation in
characteristic \(r\), where the full cyclic shift has nilpotency index
exactly \(r\), to detect the balanced threshold

\[
 p\leq B<q.
\]

The packet proves three exact named-model boundaries.

1. The desired threshold is present in the full \(r\)-dimensional regular
   shift state, but every explicit linear shift subquotient of dimension at
   most \(B\) loses it in both CRT components.
2. Applying the corresponding high forward difference to an
   integer-coefficient polynomial retains \(B!\) as an integer factor.
   Dividing by \(B!\) removes the characteristic signal or invokes a
   nonunit denominator.
3. A rational finite-dimensional gauge can fast-forward a matrix cocycle
   only if its determinant is a rational shift coboundary.  A rising
   affine factor is not such a coboundary.  When a scalar cocycle is a
   coboundary, its long product is an ordinary endpoint telescope.

These are not lower bounds for arbitrary circuits or interval-product
evaluators.  Characteristic-dependent or semilinear gauges, nonlinear
states, implicitly compressed regular representations, determinant-one
matrix cocycles, integer-valued polynomial oracles, and adaptive algorithms
remain outside the theorems.

No C++ search or research computation belongs to this packet.

## 1. Balanced threshold

Let

\[
 N=pq,\qquad p<q<2p,
\tag{1}
\]

where \(p,q\) are distinct odd primes, and put

\[
 B=\lfloor\sqrt N\rfloor.
\tag{2}
\]

Then

\[
 \boxed{p\leq B<q.}
\tag{3}
\]

Only this threshold is used below.  The theorems do not claim to factor a
general composite or even to evaluate \(B!\bmod N\).

## 2. The full characteristic shift

For a prime \(r\), let

\[
 V_r=\{f:\mathbb F_r\longrightarrow\mathbb F_r\}.
\tag{4}
\]

This is an \(r\)-dimensional vector space.  Define the cyclic translation
and its forward-difference operator by

\[
 (T_rf)(x)=f(x+1),\qquad \Delta_r=T_r-I.
\tag{5}
\]

### Theorem 1 — exact regular-state threshold

The minimal polynomials of \(T_r\) and \(\Delta_r\) are respectively

\[
 \boxed{\mu_{T_r}(Z)=Z^r-1=(Z-1)^r,}
\tag{6}
\]

and

\[
 \boxed{\mu_{\Delta_r}(Z)=Z^r.}
\tag{7}
\]

Consequently,

\[
 \Delta_r^k=0\quad\Longleftrightarrow\quad k\geq r.
\tag{8}
\]

For the two components in (1), equations (3) and (8) give the exact
characteristic separator

\[
 \boxed{\Delta_p^B=0,\qquad \Delta_q^B\ne0.}
\tag{9}
\]

This is a rank statement about the full regular function spaces.  It does
not say that applying the operators to one public probe gives a nonzero
value modulo \(q\).

## 3. Explicit finite linear states lose the threshold

Call \(W_r\) a **linear shift subquotient** when it is a \(T_r\)-stable
subspace, quotient, or subquotient of \(V_r\), with the induced shift
denoted by \(\overline T_r\).  Put

\[
 \overline\Delta_r=\overline T_r-I.
\tag{10}
\]

### Theorem 2 — dimension barrier for the nilpotent mechanism

If

\[
 d_r=\dim_{\mathbb F_r}W_r,
\tag{11}
\]

then

\[
 \boxed{\overline\Delta_r^{\,d_r}=0.}
\tag{12}
\]

In particular, if \(d_p,d_q\leq d\leq B\), then

\[
 \boxed{
 \overline\Delta_p^{\,B}
 =\overline\Delta_q^{\,B}=0.}
\tag{13}
\]

Thus no such state retains the asymmetry in (9).  This includes an explicit
global free state of rank \(d\leq B\) whose reductions are shift
subquotients; a local rank drop only makes the dimensions smaller.

Let \(n=\lceil\log_2(N+1)\rceil\).  On balanced semiprimes,

\[
 p=2^{\Theta(n)}.
\tag{14}
\]

Every fixed numerical quasipolynomial
\(Q(n)=2^{O((\log n)^k)}\) satisfies

\[
 Q(n)<p\leq B
\tag{15}
\]

for all sufficiently large balanced inputs.  Therefore an explicitly
stored \(Q(n)\)-dimensional shift subquotient cannot preserve the regular
nilpotency threshold.  This is not a storage lower bound for an implicit or
succinct representation that does not enumerate a basis.

The subquotient and intertwining hypotheses are essential.  An arbitrary
matrix sequence over \(\mathbb F_r\) need not be a quotient of cyclic
translation on all field functions.

## 4. Polynomial probes retain the factorial

To separate this statement from cyclic wraparound, let the ordinary
forward difference on integer polynomials be

\[
 (\delta F)(X)=F(X+1)-F(X).
\tag{16}
\]

### Theorem 3 — integral divided-difference factor

For every \(F\in\mathbb Z[X]\), every \(a\in\mathbb Z\), and every
\(k\geq0\),

\[
 \boxed{\delta^kF(a)\in k!\,\mathbb Z.}
\tag{17}
\]

More explicitly, if

\[
 F(X)=\sum_{m\geq0}c_mX^m,
\tag{18}
\]

then

\[
 \boxed{
 \frac{\delta^kF(a)}{k!}
 =\sum_{m\geq k}c_m
   \sum_{t=k}^{m}\binom mt a^{m-t}S(t,k)
 \in\mathbb Z,}
\tag{19}
\]

where \(S(t,k)\) is a Stirling number of the second kind.

The sharp control is

\[
 \boxed{\delta^kX^k\big|_{X=0}=k!.}
\tag{20}
\]

For \(k=B\), every entry of a vector or matrix of
integer-coefficient polynomial probes is therefore divisible by \(B!\).
On (1), \(p\mid B!\) and \(q\nmid B!\).  Such a characteristic-zero
polynomial probe has retained the factorial as a common integer factor;
it has not supplied an independently evaluated normalization.

Equation (17) is an algebraic divisibility statement, not an evaluator
lower bound.  A multiplier in (19) can also vanish modulo \(q\), and a
hypothetical algorithm may exploit structure not represented by the
displayed factorization.

The normalized divided difference

\[
 \frac{\delta^BF(a)}{B!}
\tag{21}
\]

removes the universal \(p\)-factor.  Direct modular division by \(B!\) is
invalid because \(B!\) is a zero divisor modulo \(N\).  If the quotient is
instead evaluated from the integer on the right side of (19), that
normalized value no longer contains the universal factorial signal.

The coefficient hypothesis in Theorem 3 is exact.  Integer-valued
polynomials such as \(\binom XB\) need not satisfy (17): their rational
monomial-basis denominators can contain \(B!\).  Treating such a remote
binomial value as a primitive evaluator is outside this theorem.

## 5. Rational scalar shift gauges

Let \(\tau h(X)=h(X+1)\) on \(\mathbb Q(X)\).  Two monic irreducible
polynomials over \(\mathbb Q\) lie in the same **translation orbit** when
one is obtained from the other by an integer shift of \(X\).  For

\[
 R\in\mathbb Q(X)^*,
\tag{22}
\]

write \(v_P(R)\) for the exponent of a monic irreducible \(P\) in its
factorization.  Each translation orbit contains only finitely many
divisors of a fixed rational function.

### Theorem 4 — exact rational coboundary criterion

There exists \(h\in\mathbb Q(X)^*\) such that

\[
 \boxed{R(X)=\frac{h(X+1)}{h(X)}}
\tag{23}
\]

if and only if both conditions hold:

1. \(R(X)\longrightarrow1\) as \(X\longrightarrow\infty\);
2. for every translation orbit \(\mathcal O\),

\[
 \boxed{\sum_{P\in\mathcal O}v_P(R)=0.}
\tag{24}
\]

Whenever (23) holds,

\[
 \boxed{
 \prod_{j=0}^{m-1}R(X+j)
 =\frac{h(X+m)}{h(X)}.}
\tag{25}
\]

Thus this scalar grammar has an exact dichotomy: it has no rational gauge,
or its complete interval product is an endpoint telescope.

For example,

\[
 R(X)=\frac{X+1}{X}
\tag{26}
\]

has the gauge \(h(X)=X\), while

\[
 \boxed{R(X)=X}
\tag{27}
\]

has no rational gauge.  More generally, a nonconstant polynomial or a
product of affine factors with positive net degree fails the condition at
infinity.

Equation (25) is an identity over \(\mathbb Q(X)\).  Reduction modulo a
composite modulus is valid only after every denominator used at the chosen
endpoints is proved to be a unit.  A proper denominator gcd already gives
a factor; a saturated denominator gcd does not.  No cancellation through
an undefined modular inverse is authorized.

## 6. Rational matrix gauges

Let

\[
 A(X),G(X)\in\operatorname{GL}_d(\mathbb Q(X))
\tag{28}
\]

and suppose

\[
 \boxed{G(X+1)=A(X)G(X).}
\tag{29}
\]

Then

\[
 \boxed{
 \det A(X)=\frac{\det G(X+1)}{\det G(X)}.}
\tag{30}
\]

### Corollary 4.1 — determinant obstruction

The determinant cocycle of every rationally gauge-trivial matrix system
must satisfy Theorem 4.  In particular, if

\[
 \det A(X)=X^eR_0(X),\qquad e\ne0,
\tag{31}
\]

and \(R_0\) is a rational shift coboundary, then no rational \(G\)
satisfying (29) exists.

This is only a necessary condition.  It is silent when
\(\det A=1\), and it does not prove that every determinant-coboundary
matrix cocycle has a rational gauge.  A determinant-one lift may store a
factor-sensitive projective, off-diagonal, or nonlinear invariant not seen
by (30).

When a rational gauge does exist, ordered multiplication gives

\[
 \boxed{
 A(X+m-1)\cdots A(X)
 =G(X+m)G(X)^{-1}.}
\tag{32}
\]

Again, this is an operational modular fast-forward only after unit
denominators and quasipolynomial representation costs are proved.

## 7. Search decision and surviving seam

No C++ search is justified for the following grammar:

- explicit \(Q(n)\)-dimensional subquotients of the regular cyclic shift;
- integer-polynomial probes of \(\delta^B\);
- rational gauges whose determinant contains an uncancelled rising affine
  factor; or
- scalar rational gauges without the orbit test (24).

Such a search can only rediscover a state that loses the characteristic
threshold, a factorial-bearing difference, a nongauge, or an endpoint
telescope.

A future symbolic search becomes materially new only after it supplies at
least one of these exact objects:

1. a nonlinear or semilinear public state whose local action is not a
   linear subquotient of \(V_r\);
2. an implicit QP-cost representation of the \(r\)-state regular shift
   that can extract a certified \(p/q\) rank difference without enumerating
   \(r\) coordinates;
3. a determinant-one or determinant-coboundary matrix cocycle with a
   factor-sensitive non-determinant invariant and a total QP endpoint
   evaluator; or
4. a characteristic-dependent gauge whose construction uses only public
   data and no hidden local Frobenius, factor, order, or nonunit inverse.

Before any implementation, the proposed object must pass these theory
gates:

- exact state and intertwining semantics;
- determinant-orbit audit;
- denominator unit audit;
- proof that all coefficients and endpoint operations are numerical QP;
- proof that no local characteristic or factor is supplied as advice; and
- a symbolic local rank or value law that is asymmetric for the intended
  \(p,q\), not merely on finite samples.

Useful future positive and negative controls are already exact:

- positive full-state control: \(\mu_{\Delta_r}=Z^r\);
- positive factorial control: \(\delta^BX^B(0)=B!\);
- positive telescope: \((X+1)/X=\tau X/X\);
- negative scalar gauge: \(X\);
- determinant-one decoy:

\[
 G(X)=\begin{pmatrix}1&X\\0&1\end{pmatrix},\qquad
 A(X)=G(X+1)G(X)^{-1}
     =\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\tag{33}
\]

The last system fast-forwards but contains no interval-product signal.  A
finite search must reject it as a telescope rather than count it as a lead.

## Exact exclusions

F274 proves no:

1. lower bound for arbitrary arithmetic, algebraic, or Boolean circuits;
2. lower bound for the uniform interval-product evaluator left open by
   P221;
3. impossibility theorem for nonlinear, semilinear, characteristic-specific,
   adaptive, or implicit-state algorithms;
4. theorem about arbitrary finite-dimensional matrix sequences that are not
   regular-shift subquotients;
5. evaluator lower bound from the divisibility in Theorem 3;
6. rational-gauge obstruction for determinant-one systems;
7. numerical quasipolynomial evaluator;
8. integer-factoring algorithm; or
9. computational or empirical result.
