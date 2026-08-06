# F44 kill-first result: explicit shifted Jacobi correlations are either gcd-degenerate or have only square-root-scale complete means

**Family:** F09.

**Status:** candidate obstruction; not promoted.  It still requires the
prescribed hostile audit and then a fresh proof-blind reconstruction.

**Classification:** evidence against the exact auxiliary mechanism that
forms polynomially many explicitly listed shifted Jacobi products, evaluates
them on fresh uniform residues, and tries to recover a factor from direct
zero tickets or ordinary empirical correlation means.  This is not evidence
against the whole higher-character family or against arbitrary processing of
a Jacobi transcript.

**Closest promoted routes and material difference.**  P15 is an algebraic
rank theorem for individually factor-swap-invariant multiplicative scalar
higher-residue labels: such labels retain only the diagonal phase.  F44
instead starts with the actually available quadratic Jacobi function and
uses nonlinear products at additively shifted arguments.  P49 studies
additive Fourier coefficients of the inverse graph \((u,u^{-1})\) and obtains
Kloosterman bounds.  F44 has a different source, different local sums
(hyperelliptic quadratic-character sums), and a different degeneracy
certificate (a shift difference rather than a Fourier frequency).  The
similar \(N^{-1/2}\) global scale is a conclusion, not an identification of
the mechanisms.

**Computation:** none.  This artifact is a proof-only mandatory kill-first
analysis.  No finite probe, computer algebra calculation, or numerical
experiment was run.

## 1. Quantifiers, source, and mandatory public preprocessing

Let

\[
 N=pq
\]

with distinct odd primes \(p,q\).  Exact identities below do not require
balance.  An asymptotic **fixed-balance family** means that there is a fixed
constant \(\Lambda\geq1\), independent of \(N\), such that

\[
 \Lambda^{-1}\sqrt N\leq p,q\leq\Lambda\sqrt N.
\tag{1.1}
\]

Let \(\chi_r\) be the quadratic character of \(\mathbb F_r\), extended by
\(\chi_r(0)=0\).  Let

\[
 \chi_N(z)=\left(\frac zN\right)
\]

be the Jacobi symbol, also extended by zero on nonunits.  Since \(N=pq\) is
squarefree,

\[
 \chi_N(z)=\chi_p(z\bmod p)\chi_q(z\bmod q)
\tag{1.2}
\]

for every integer \(z\), including nonunits.

An explicit shift multiset is a list

\[
 H=(h_1,\ldots,h_L),
\]

of residues modulo \(N\), with \(L\) and the total bit length of the list
polynomial in \(n=\lceil\log_2(N+1)\rceil\).  Its correlation is

\[
 Y_H(x)=\prod_{i=1}^L\chi_N(x+h_i),
 \qquad x\mathrel{\leftarrow}\mathbb Z/N\mathbb Z.
\tag{1.3}
\]

Normalize every shift to \(\{0,\ldots,N-1\}\).  Let \(E\) be the set of
distinct normalized shifts and let \(m_e\geq1\) be the multiplicity of
\(e\in E\).  Thus

\[
 Y_H(x)=\prod_{e\in E}\chi_N(x+e)^{m_e}.
\tag{1.4}
\]

Global duplicates must be collected before any parity argument.  For every
two distinct \(e,f\in E\), compute the individual screen

\[
 d_{e,f}=\gcd(e-f,N).
\tag{1.5}
\]

Do not replace these individual gcds by only a discriminant or a product of
differences: different pairs could contribute \(p\) and \(q\), making the
aggregate gcd equal to the uninformative value \(N\).

### Lemma 1.1 (complete collision dichotomy)

For distinct normalized shifts \(e,f\), exactly one of the following holds:

1. \(d_{e,f}=1\), and \(e,f\) are distinct modulo both \(p\) and \(q\);
2. \(d_{e,f}=p\), and they collide modulo \(p\) only;
3. \(d_{e,f}=q\), and they collide modulo \(q\) only.

For two raw shifts that are congruent modulo \(N\), the corresponding gcd is
\(N\); this is a global duplicate, not a factor, and it is absorbed into one
multiplicity \(m_e\).

**Proof.**  A collision modulo \(r\in\{p,q\}\) is exactly the divisibility
\(r\mid e-f\).  Since \(N=pq\), the gcd in (1.5) records precisely which of
the two divisibilities hold.  Both hold exactly when the raw residues are
equal modulo \(N\).  Distinct normalized representatives exclude that last
case. \(\square\)

Consequently, the preprocessing has a factor-or-injectivity dichotomy:

* if some \(d_{e,f}\) is a proper divisor, the explicit coefficient
  \(e-f\) has already factored \(N\);
* otherwise the reduction map \(E\to\mathbb F_r\) is injective for both
  \(r=p,q\).

For a polynomial list of correlations, one may apply (1.5) to every pair in
the union of their distinct shifts.  This stronger global screen still costs
only polynomially many Euclidean gcds.  Every input to a gcd has
\(O(n)\) bits after normalization, so all preprocessing has uniform
polynomial bit complexity.

The rest of the proof works on the no-factor branch, where this injectivity
holds.  This qualification is essential.

This source is available from bare \(N\): exact uniform residues are sampled
by the usual rejection method from \(n\)-bit strings, the Jacobi symbol is
computed by the binary/Euclidean Jacobi algorithm, and every zero can be
accompanied by \(\gcd(x+e,N)\).  For an explicit polynomial list, all these
operations have uniform polynomial bit complexity and use no factor,
root-extraction oracle, or hidden local character convention.

## 2. Exact CRT factorization of every complete correlation

For \(r\in\{p,q\}\), define the local function

\[
 A_{H,r}(t)=\prod_{e\in E}\chi_r(t+e)^{m_e},
 \qquad t\in\mathbb F_r,
\tag{2.1}
\]

and its unnormalized and normalized complete sums

\[
 S_r(H)=\sum_{t\in\mathbb F_r}A_{H,r}(t),
 \qquad
 \mu_r(H)=\frac{S_r(H)}r.
\tag{2.2}
\]

Under CRT, a uniform \(x\bmod N\) is a pair of independent uniform
coordinates \((x_p,x_q)\).  Equation (1.2) gives, pointwise,

\[
 Y_H(x)=A_{H,p}(x_p)A_{H,q}(x_q).
\tag{2.3}
\]

Therefore the complete global mean factors exactly:

\[
 \boxed{
 \theta_H:=\mathbb E_xY_H(x)
 =\mu_p(H)\mu_q(H)
 =\frac{S_p(H)S_q(H)}N.}
\tag{2.4}
\]

There are no additive-character CRT twists here: the Jacobi symbol itself is
the product of the two local quadratic characters.

## 3. Multiplicity parity, zero roots, and the exact local formula

Set

\[
 O=\{e\in E:m_e\text{ is odd}\},
 \qquad
 A=E\setminus O,
\tag{3.1}
\]

and write

\[
 k=|O|,\qquad a=|A|,\qquad s=|E|=k+a.
\tag{3.2}
\]

The letter \(A\) here denotes the even-only support, not the local function
\(A_{H,r}\).  Define the monic squarefree polynomial

\[
 P_{O,r}(T)=\prod_{e\in O}(T+e)\in\mathbb F_r[T].
\tag{3.3}
\]

It is squarefree on the no-factor branch because the shifts remain distinct
modulo \(r\).

For a nonzero quadratic-character value, an even positive power is one and
an odd power is the value itself.  At a root, however,

\[
 \chi_r(0)^{2j}=0,
\]

not one.  Thus even multiplicities cannot simply be cancelled.

### Proposition 3.1 (exact local formula)

If \(O=\varnothing\), then

\[
 \boxed{S_r(H)=r-s,\qquad \mu_r(H)=1-\frac sr.}
\tag{3.4}
\]

If \(O\ne\varnothing\), put

\[
 C_r(O)=\sum_{t\in\mathbb F_r}\chi_r(P_{O,r}(t)),
 \qquad
 R_r(O,A)=\sum_{e\in A}\chi_r(P_{O,r}(-e)).
\tag{3.5}
\]

Then

\[
 \boxed{S_r(H)=C_r(O)-R_r(O,A).}
\tag{3.6}
\]

Every summand in \(R_r(O,A)\) is \(\pm1\).

**Proof.**  If \(O\) is empty, the local product equals one away from the
\(s\) distinct roots \(-e\), and zero at those roots, proving (3.4).

Now suppose \(O\ne\varnothing\).  Away from every root belonging to \(E\),
the even powers are one and the odd powers multiply to
\(\chi_r(P_{O,r}(t))\).  At a root \(-e\) with \(e\in O\), both the actual
product and \(\chi_r(P_{O,r})\) are zero.  At a root \(-e\) with \(e\in A\),
the actual product is zero but \(P_{O,r}(-e)\ne0\) by injectivity, so the
provisional character sum has one extra value
\(\chi_r(P_{O,r}(-e))\).  Subtracting precisely those values gives (3.6).
\(\square\)

### The exact standard theorem used

The Hasse--Weil theorem for a smooth projective geometrically connected
curve \(C/\mathbb F_r\) of genus \(g\) states

\[
 \bigl|\#C(\mathbb F_r)-(r+1)\bigr|\leq2g\sqrt r.
\tag{3.7}
\]

Apply it to the smooth projective model of

\[
 y^2=P_{O,r}(t).
\]

Squarefreeness and \(k\geq1\) make this curve geometrically connected.  If
\(k\) is odd, its genus is \((k-1)/2\), it has one rational point at
infinity, and

\[
 \boxed{|C_r(O)|\leq(k-1)\sqrt r.}
\tag{3.8}
\]

If \(k\) is even, monicity makes the leading coefficient a square, so the
curve has two rational points at infinity, genus \((k-2)/2\), and

\[
 \boxed{|C_r(O)+1|\leq(k-2)\sqrt r.}
\tag{3.9}
\]

These centered forms are sharper than blindly quoting
\((k-1)\sqrt r\).  In particular,

\[
 k=1\Longrightarrow C_r(O)=0,
 \qquad
 k=2\Longrightarrow C_r(O)=-1.
\tag{3.10}
\]

Combining (3.6), (3.8), and (3.9) gives the precise local bounds

\[
 \begin{array}{ll}
 k\text{ odd}:&
 |S_r(H)+R_r(O,A)|\leq(k-1)\sqrt r,\\[3pt]
 k\text{ even}:&
 |S_r(H)+R_r(O,A)+1|\leq(k-2)\sqrt r.
 \end{array}
\tag{3.11}
\]

Since \(|R_r(O,A)|\leq a\), both cases imply the convenient uniform
corollary

\[
 \boxed{
 O\ne\varnothing
 \quad\Longrightarrow\quad
 |S_r(H)|\leq(s-1)\sqrt r,
 \qquad
 |\mu_r(H)|\leq\frac{s-1}{\sqrt r}.}
\tag{3.12}
\]

For odd \(k\), use
\((k-1)\sqrt r+a\leq(k-1+a)\sqrt r=(s-1)\sqrt r\).
For even \(k\), use
\((k-2)\sqrt r+1+a\leq(k-2+1+a)\sqrt r=(s-1)\sqrt r\).

### Why every local square degeneration is publicly visible here

Before screening, two globally distinct odd-multiplicity shifts can collide
modulo one prime.  Their two local linear factors then merge to an even
power, so the local odd-root polynomial can lose degree, become a square, or
even become constant.  More general collisions can also merge an odd root
with an even-only excluded root.  Every such event contains a pair
\(e\ne f\) with \(r\mid e-f\).  If it occurs at exactly one CRT prime, Lemma
1.1 gives the explicit certificate

\[
 \gcd(e-f,N)=r.
\tag{3.13}
\]

If it occurs at both primes for the same pair, the two raw shifts are the
same residue modulo \(N\), their gcd is \(N\), and their multiplicities must
be collected globally.  Thus (3.8)--(3.12) omit no factor-free local square
case.

## 4. Global complete-mean bounds

If \(O\ne\varnothing\), equations (2.4) and (3.12) give

\[
 \boxed{
 |\theta_H|\leq\frac{(s-1)^2}{\sqrt N}.}
\tag{4.1}
\]

For a polynomial-size support, this is \(N^{-1/2+o(1)}\).  The special
one-shift case is exact:

\[
 s=1,\ O=E\quad\Longrightarrow\quad \theta_H=0.
\tag{4.2}
\]

If \(O=\varnothing\), equations (2.4) and (3.4) instead give the exact
near-one statistic

\[
 \boxed{
 \theta_H=\left(1-\frac sp\right)
          \left(1-\frac sq\right)
 =1-\frac{s(p+q)-s^2}{N}.}
\tag{4.3}
\]

The multiplicity values no longer matter once they are all even; only the
distinct support \(E\) matters.

## 5. The full one-correlation sample law and exact MSE

For every multiplicity pattern, \(Y_H\in\{-1,0,1\}\).  Moreover,

\[
 Y_H(x)^2=1
\]

exactly when none of the \(s\) distinct shifts is zero modulo either local
prime.  There are \(p-s\) allowed \(p\)-coordinates and \(q-s\) allowed
\(q\)-coordinates.  Hence

\[
 \boxed{
 \rho_H:=\mathbb E[Y_H^2]
 =\left(1-\frac sp\right)
  \left(1-\frac sq\right).}
\tag{5.1}
\]

This also shows that the no-factor branch necessarily has \(s\leq p,q\),
because the support injects into both fields.

The entire law of this one scalar is determined by \(\theta_H\) and
\(\rho_H\):

\[
 \Pr(Y_H=0)=1-\rho_H,
\quad
 \Pr(Y_H=1)=\frac{\rho_H+\theta_H}{2},
\quad
 \Pr(Y_H=-1)=\frac{\rho_H-\theta_H}{2}.
\tag{5.2}
\]

In particular,

\[
 \boxed{\operatorname{Var}(Y_H)=\rho_H-\theta_H^2.}
\tag{5.3}
\]

Let \(Y_1,\ldots,Y_m\) be iid copies evaluated on genuinely independent
uniform residues and put

\[
 \overline Y_m=\frac1m\sum_{i=1}^mY_i.
\]

Independence and unbiasedness give the exact mean-square error

\[
 \boxed{
 \mathbb E[(\overline Y_m-\theta_H)^2]
 =\frac{\rho_H-\theta_H^2}{m}.}
\tag{5.4}
\]

No probability tail assertion is being inferred from (5.4).

### 5.1 Relative-RMSE barrier for a nontrivial correlation

Suppose \(O\ne\varnothing\) and \(\theta_H\ne0\).  Relative RMSE at most
\(\eta>0\) is exactly the condition

\[
 \left(\mathbb E[(\overline Y_m-\theta_H)^2]\right)^{1/2}
 \leq\eta|\theta_H|,
\]

so (5.4) is equivalent to

\[
 \boxed{
 m\geq\frac{\rho_H-\theta_H^2}{\eta^2\theta_H^2}.}
\tag{5.5}
\]

Now let the support size satisfy \(s\leq T(n)\) for a fixed polynomial
\(T\), and restrict to any fixed-balance family (1.1).  Exponential growth
of \(p,q\) relative to \(T(n)\) gives, for all sufficiently large members of
the family,

\[
 \rho_H\geq\frac{9}{16},
 \qquad
 \theta_H^2\leq\frac{(s-1)^4}{N}\leq\frac1{16}.
\tag{5.6}
\]

Thus \(\rho_H-\theta_H^2\geq1/2\), and (4.1), (5.5) imply

\[
 \boxed{
 m\geq\frac{N}{2\eta^2(s-1)^4}
 \geq\frac{N}{2\eta^2T(n)^4}.}
\tag{5.7}
\]

This is \(N^{1-o(1)}\) raw samples for constant or inverse-polynomial
relative RMSE.  If the actual mean is smaller than the Weil upper bound, the
exact requirement (5.5) is only larger.

If \(\theta_H=0\), relative error is undefined; it is not legitimate to
divide by the mean and announce an infinite sample lower bound.  There is
simply no nonzero population mean to decode.  The exact absolute MSE is

\[
 \mathbb E[\overline Y_m^2]=\frac{\rho_H}{m},
\tag{5.8}
\]

which is asymptotic to \(1/m\) for polynomial \(s\) on a balanced family.

Equations (5.5)--(5.8) are RMSE statements about the ordinary empirical
mean.  They are not arbitrary-confidence lower bounds.  Such a claim would
need a separate anti-concentration or testing argument; none is asserted
here.

### 5.2 Direct local-zero/gcd tickets

Every evaluated shift may be screened by \(\gcd(x+e,N)\).  On the
factor-free difference branch, the probability that at least one of the
\(s\) shifts supplies a proper factor is exactly

\[
 \boxed{
 \tau_H
 =1-\rho_H-\frac{s}{N}
 =\frac{s(p+q-s-1)}{N}.}
\tag{5.9}
\]

Indeed, \(1-\rho_H\) is the probability that some shifted value is a
nonunit.  The only nonunit cases that fail to give a proper factor are the
\(s\) points \(x=-e\bmod N\), where one shifted value has gcd \(N\); all
other shifts are then units because every pairwise difference has gcd one.
Every other local-zero event has a shift with gcd \(p\) or \(q\).

On a fixed-balance family,

\[
 \tau_H=O_\Lambda(s/\sqrt N).
\tag{5.10}
\]

Therefore a polynomial total number of explicitly evaluated fresh
shift-residue pairs has only \(N^{-1/2+o(1)}\) total direct-gcd success
probability by the union bound.  Pooling polynomially many such lucky
relations does not make the direct zero ticket inverse-polynomial.  This says
nothing about a joint decoder for their nonzero signs.

## 6. The synchronized even-multiplicity statistic

When \(O=\varnothing\), the output is precisely the zero-avoidance indicator,
so \(\theta_H=\rho_H\).  Its deviation from the public baseline one is

\[
 \boxed{
 \delta_H:=1-\theta_H
 =\frac{s(p+q)-s^2}{N}.}
\tag{6.1}
\]

Under fixed balance and polynomial \(s\),

\[
 0\leq\delta_H
 \leq s\left(\frac1p+\frac1q\right)
 \leq\frac{2\Lambda s}{\sqrt N}
 =N^{-1/2+o(1)}.
\tag{6.2}
\]

Thus even multiplicities create a synchronized near-one statistic, but not
a larger factor-dependent raw metric signal.  Raising multiplicities does
not change (6.1); enlarging the explicit support only helps linearly, and a
polynomial support remains exponentially below characteristic scale.

This tiny bias is not mathematically useless.  If \(s>0\) and an oracle
returned the complete mean **exactly**, then

\[
 p+q=\frac{N(1-\theta_H)+s^2}{s},
\tag{6.3}
\]

after which \(p,q\) are the roots of \(X^2-(p+q)X+N\).  Hence exact symbolic
evaluation of the complete sum is factor-sufficient on this semiprime
promise and is explicitly outside the killed mechanism.

For raw sampling, \(Y_H\) is Bernoulli with success probability
\(1-\delta_H\).  Estimating the useful deviation by
\(\widehat\delta=1-\overline Y_m\) gives

\[
 \mathbb E[(\widehat\delta-\delta_H)^2]
 =\frac{\delta_H(1-\delta_H)}m.
\tag{6.4}
\]

If \(\delta_H>0\), relative RMSE at most \(\eta\) therefore requires

\[
 m\geq\frac{1-\delta_H}{\eta^2\delta_H}
 =\Omega_\Lambda\!\left(\frac{\sqrt N}{\eta^2s}\right)
\tag{6.5}
\]

for polynomial \(s\) on a fixed-balance family.  Relative estimation of the
near-one mean itself is easy but irrelevant: it estimates the known baseline
one rather than resolving \(\delta_H\).  The exact probability of seeing no
zero in \(m\) trials is \((1-\delta_H)^m\); no broader testing lower bound is
claimed.

## 7. Polynomial lists and polynomial-\(\ell^1\) linear expectations

Let \(H_1,\ldots,H_J\) be an explicit polynomial list whose union has passed
every pairwise screen (1.5).  Let \(s_j=|E_j|\), let \(O_j\) be its
odd-multiplicity support, and let the total explicit support budget be at
most \(T\), so \(s_j\leq T\).  Define the public reference value

\[
 b_j=\begin{cases}
 1,&O_j=\varnothing,\\
 0,&O_j\ne\varnothing.
 \end{cases}
\tag{7.1}
\]

For coefficients \(c_1,\ldots,c_J\) with

\[
 \sum_{j=1}^J|c_j|\leq B,
\tag{7.2}
\]

linearity of expectation, (4.1), and (6.2) give on a fixed-balance family

\[
\begin{aligned}
 \left|
 \mathbb E\sum_{j=1}^Jc_jY_{H_j}
 -\sum_{j=1}^Jc_jb_j
 \right|
 &\leq
 \sum_{O_j\ne\varnothing}|c_j|\frac{(s_j-1)^2}{\sqrt N}
 +\sum_{O_j=\varnothing}|c_j|\frac{2\Lambda s_j}{\sqrt N}\\
 &\leq
 \boxed{\frac{B\max(T^2,2\Lambda T)}{\sqrt N}.}
\tag{7.3}
\end{aligned}

Thus polynomially many correlations and a polynomial \(\ell^1\) coefficient
budget still have only \(N^{-1/2+o(1)}\) population drift from the public
zero/one reference.  A polynomial list without an \(\ell^1\) bound could
multiply an exponentially small mean by an exponentially large numerical
coefficient, so list size alone is not the right statement.

Equation (7.3) concerns linear expectation combinations.  If several
correlations are evaluated on the same fresh \(x\), their coordinates can be
strongly dependent; (7.3) remains true by linearity, but no claim is made
about nonlinear functions of that vector.

## 8. Fresh adaptive scalar calls: conditional means and a transcript hybrid

Let \(\mathcal F_{t-1}\) be the entire transcript before round \(t\).  Allow
the next explicit menu of shift multisets and its coefficients to be any
\(\mathcal F_{t-1}\)-measurable function, subject to the declared polynomial
size and \(\ell^1\) budgets.  First run every individual difference gcd for
that realized menu and between every new shift and every previously explicit
shift.  Thus the accumulated union has passed (1.5).  A proper gcd ends the
round with a factor.  Otherwise draw

\[
 x_t\mathrel{\leftarrow}\mathbb Z/N\mathbb Z
\]

uniformly and independently of \(\mathcal F_{t-1}\), and evaluate the menu.
Conditioned on \(\mathcal F_{t-1}\), the realized shifts and coefficients are
fixed while \(x_t\) has independent uniform CRT coordinates.  Therefore all
of (2.4)--(7.3) apply conditionally, with the realized parameters:

\[
 \left|
 \mathbb E[Z_t\mid\mathcal F_{t-1}]
 -b_t
 \right|
 \leq
 \frac{B_t\max(T_t^2,2\Lambda T_t)}{\sqrt N},
\tag{8.1}
\]

where \(Z_t\) is the menu's linear combination and \(b_t\) its public
reference combination.  Summing polynomially many rounds preserves an
exponentially small bound when the total budgets are polynomial.

This conditional statement does not say that the past transcript cannot
teach an algorithm how to choose a future factor-revealing difference.  If
it does, the mandatory gcd screen succeeds.  Nor does it cover choosing the
next shift after observing \(\chi_N(x_t+h)\) while reusing that same \(x_t\):
then the shift multiset itself depends on the source being averaged.
Same-source adaptation and nonlinear processing of the accumulated vector
transcript remain outside scope.

There is a stronger statement for the **compressed scalar observation
channel**.  It comes from its exact three-point law (5.2), not from turning an
MSE calculation into an unsupported confidence claim.

Put

\[
 \zeta_H=1-\rho_H
 =\frac{s(p+q)-s^2}{N}.
\tag{8.2}
\]

If \(O\ne\varnothing\), let \(Q_H\) be a public fair Rademacher sign:
\(Q_H(1)=Q_H(-1)=1/2\).  Using (5.2), the exact total variation distance is

\[
\begin{aligned}
 d_{\rm TV}(\mathcal L(Y_H),Q_H)
 &=\frac12\left(
 \zeta_H+\frac{|\theta_H-\zeta_H|}{2}
               +\frac{|\theta_H+\zeta_H|}{2}
 \right)\\
 &=\frac{\zeta_H+\max(\zeta_H,|\theta_H|)}2\\
 &\leq \zeta_H+\frac{|\theta_H|}{2}.
\end{aligned}
\tag{8.3}
\]

If \(O=\varnothing\), let \(Q_H\) be the constant-one law.  Then

\[
 \boxed{d_{\rm TV}(\mathcal L(Y_H),Q_H)=\zeta_H.}
\tag{8.4}
\]

Consequently every nonempty screened scalar call satisfies, on a
fixed-balance family,

\[
 d_{\rm TV}(\mathcal L(Y_H),Q_H)
 \leq
 \frac{2\Lambda s+(s-1)^2/2}{\sqrt N}.
\tag{8.5}
\]

Now consider an adaptive sequence of scalar calls in which \(H_t\) is chosen
from the earlier **scalar** observations and public randomness, while each
\(Y_{H_t}\) is evaluated on its own fresh independent \(x_t\).  Couple the
public randomness in the real and reference processes.  As long as their
histories agree, they choose the same \(H_t\); maximally couple the real next
scalar to its reference law \(Q_{H_t}\).  Equation (8.5) bounds the
conditional probability that the histories first separate at that call.
The union bound therefore proves the standard sequential-kernel hybrid
inequality

\[
 d_{\rm TV}(\mathcal L(Y_{H_1},\ldots,Y_{H_R}),
            \mathcal L(Q_{H_1},\ldots,Q_{H_R}))
 \leq
 \sup_{\text{reachable common paths}}
 \sum_{t=1}^R\varepsilon(H_t),
\tag{8.6}
\]

where \(\varepsilon(H)\) denotes the right side of (8.5).  Empty
correlations are deterministic one and may simply be deleted.  If every
possible execution has total distinct-support budget

\[
 \sum_{t=1}^Rs_t\leq T,
\]

then \(\sum_ts_t^2\leq T^2\), and hence

\[
 \boxed{
 d_{\rm TV}(\text{real compressed-scalar transcript},
            \text{public reference transcript})
 \leq\frac{2\Lambda T+T^2/2}{\sqrt N}.}
\tag{8.7}

For polynomial \(T\), this is \(N^{-1/2+o(1)}\).  By data processing, (8.7)
also bounds the advantage of any nonlinear decision rule applied only to
this adaptive fresh-call scalar transcript.  This is an observation-channel
theorem, not a general factoring-hardness result: \(N\) itself remains known
to both processes.

Most importantly, (8.7) does not cover the vector

\[
 (\chi_N(x_t+h):h\in E_t),
\]

the identities of individual zero/gcd events, multiple correlations sharing
one \(x_t\), shifts chosen after inspecting values at that same \(x_t\), or
any other whole-Jacobi-transcript processing.  Those observations are richer
than the single compressed product \(Y_{H_t}\) and remain open.  Direct
proper-gcd flags alone have the separate sparse bound (5.9)--(5.10).

## 9. Candidate verdict and exact boundary

The preregistered explicit fresh-correlation mechanism has the following
narrow factor-or-small-signal theorem.

1. After global duplicates are collected, every one-prime shift collision
   exposes that prime through one explicitly screened difference gcd.
2. On the no-factor branch, every local odd-root polynomial is squarefree.
   The complete global mean factors into two exact local character sums.
3. A correlation with at least one odd multiplicity has
   \(|\theta_H|\leq(s-1)^2/\sqrt N\).  For polynomial \(s\), ordinary raw
   empirical estimation of a nonzero mean to relative RMSE needs
   \(N^{1-o(1)}\) iid samples; a zero mean has no relative signal.
4. An all-even correlation is only the synchronized zero-avoidance
   indicator.  Its factor-dependent deviation from one is
   \([s(p+q)-s^2]/N=O_\Lambda(s/\sqrt N)\), and resolving that deviation by
   raw relative-RMSE estimation needs \(N^{1/2-o(1)}\) samples.
5. Polynomial explicit lists, polynomial-\(\ell^1\) linear combinations,
   and past-measurable menus evaluated on genuinely fresh independent
   residues preserve these population-scale bounds.  Polynomial pooling of
   direct local-zero tickets also remains exponentially sparse.
6. More strongly, an adaptive sequence that observes only one compressed
   scalar product per fresh source is within \(N^{-1/2+o(1)}\) total
   variation of a public sequence of fair signs/constant ones under a
   polynomial total support budget.  This does not cover the individual
   Jacobi-value vectors used to form those products.

This is a method failure for direct gcd tickets and ordinary empirical means
of explicit polynomial-size fresh shifted-Jacobi correlations.  It is not a
factoring lower bound, a computational indistinguishability theorem, or a
claim that bare \(N\) cannot manufacture a factor-correlated metric hint.

The following remain explicitly open:

* vector- or multiset-valued local orientation information, including the
  anti-diagonal information left outside P15;
* dense or succinct characteristic-scale shift energy, where exponentially
  many shifts are represented and evaluated without expansion;
* exact symbolic evaluation of complete character sums (which (6.3) shows
  can itself be factor-sufficient);
* same-source adaptive nonlinear tests and nonlinear processing of the
  per-shift value vectors;
* arbitrary joint processing of the whole Jacobi transcript, including
  correlations between many coordinates evaluated on one source;
* other multiplicative characters and genuinely factor-oriented carriers;
* any factor-asymmetric or nonuniform arithmetic source.

**Exact retry condition.**  A materially new retry must supply at least one
of: a polynomial-time succinct evaluator for characteristic-scale shifted
energy; a nonlinear or joint transcript statistic with a proved
inverse-polynomial factor-asymmetric signal; an exact complete-sum evaluator
that is not already factoring-equivalent by construction; a same-source
adaptive rule with a proved all-input gain; or a different character/source
whose CRT components do not merely multiply two synchronized square-root
scale local means.  Merely adding polynomially many explicit fresh shifts,
fresh iid samples, or polynomial-\(\ell^1\) linear combinations is covered by
the obstruction above.
