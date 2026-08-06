# Independent reconstruction: Jacobi correlations after difference screening

## Verdict

**PASS, with the branch and asymptotic quantifiers made explicit below.**  The
bound \(\lvert S_r\rvert\le (s-1)\sqrt r\), and hence the small global mean,
is an odd-pattern statement: it requires \(O\ne\varnothing\).  The
all-even branch instead has \(S_r=r-s\) and mean close to one.  Exact recovery
of \(p+q\) requires \(s>0\).  Relative RMSE is defined only for a nonzero
target.  The constants in the two asymptotic sampling lower bounds hold for
all sufficiently large members of a fixed-balance family.  With those
necessary readings, every claimed formula follows.

The transcript comparison is also valid, but only for the channel that hides
the fresh sample \(x\) and releases one scalar product from it.  It does not
compare any of the richer observations listed at the end.

## 1. Normalization, screening, and CRT

Write the normalized multiset as

\[
 H=\{e^{m_e}:e\in E\},\qquad m_e\ge 1,
\]

where every shift has first been reduced modulo \(N\), equal residues have
been collected, and the elements of \(E\) are distinct modulo \(N\).  Put

\[
 O=\{e\in E:m_e\text{ is odd}\},\qquad A=E\setminus O,
 \qquad s=|E|,\quad k=|O|.
\]

For every unordered pair \(e\ne f\), compute
\(\gcd(e-f,N)\).  Because \(e-f\not\equiv0\pmod N\), this gcd is either one
or a proper factor.  On the branch where no factor is returned, all these
gcds are one.  Consequently, for each \(r\in\{p,q\}\), the reductions of
\(E\) modulo \(r\) are distinct: equality of two reductions would make
\(r\mid e-f\).  In particular, \(s\le p,q\).

Let \(\chi_r\) be the Legendre character on \(\mathbb F_r\), extended by
\(\chi_r(0)=0\), and define

\[
 f_r(u)=\prod_{e\in E}\chi_r(u+e)^{m_e},\qquad
 S_r=\sum_{u\in\mathbb F_r}f_r(u).
\]

For squarefree \(N=pq\), the extended Jacobi character satisfies
\((a\mid N)=\chi_p(a)\chi_q(a)\), including when one of the factors is zero.
Thus CRT gives, pointwise,

\[
 Y_H(x)=f_p(x\bmod p)f_q(x\bmod q).
\]

The two CRT coordinates of uniform \(x\bmod N\) are independent and uniform,
so the exact mean factorization is

\[
 \boxed{\quad \theta:=\mathbb E Y_H=\frac{S_p}{p}\frac{S_q}{q}
             =\frac{S_pS_q}{N}.\quad}                                      \tag{1}
\]

This argument also explains why merely reducing the exponents modulo two
would be wrong at roots: \(0^{2j}=0\), not one.

## 2. Exact local sums

If \(O=\varnothing\), then \(f_r(u)=1\) off the \(s\) distinct roots
\(-E\) and is zero at those roots.  Hence

\[
 \boxed{S_r=r-s.}                                                            \tag{2}
\]

Now suppose \(O\ne\varnothing\).  Define the squarefree polynomial and its
complete character sum by

\[
 P_{O,r}(X)=\prod_{o\in O}(X+o)\in\mathbb F_r[X],\qquad
 C_r(O)=\sum_{u\in\mathbb F_r}\chi_r(P_{O,r}(u)).
\]

The polynomial is squarefree because difference screening made its roots
distinct.  The odd-support roots already contribute zero to \(C_r\), but at
an even-only root \(-a\), \(a\in A\), the complete sum has the nonzero term
\(\chi_r(P_{O,r}(-a))\), whereas the original product has a zero from the
positive even power of \(u+a\).  Therefore, with

\[
 R_r(O,A)=\sum_{a\in A}\chi_r(P_{O,r}(-a))
          =\sum_{a\in A}\chi_r\!\left(\prod_{o\in O}(o-a)\right),
\]

one has the exact identity

\[
 \boxed{S_r=C_r(O)-R_r(O,A).}                                                \tag{3}
\]

Every summand in \(R_r\) is \(\pm1\), so \(|R_r|\le s-k\).

## 3. The centered Hasse--Weil bounds, including \(k=1,2\)

Consider the smooth projective model of

\[
 \mathcal C:\quad y^2=P_{O,r}(x).
\]

If \(k\) is odd, its genus is \(g=(k-1)/2\), and it has one rational point
at infinity.  Its affine point count is

\[
 \sum_{x\in\mathbb F_r}(1+\chi_r(P_{O,r}(x)))=r+C_r(O),
\]

so \(\#\mathcal C(\mathbb F_r)=r+1+C_r(O)\).  Hasse--Weil gives

\[
 \boxed{|C_r(O)|\le (k-1)\sqrt r\qquad(k\text{ odd}).}                       \tag{4}
\]

For \(k=1\), this says \(C_r=0\) exactly.  It can also be seen directly:
\(x\mapsto x+o\) permutes \(\mathbb F_r\), whose quadratic-character sum is
zero.

If \(k\) is even, its genus is \(g=(k-2)/2\).  Since the leading coefficient
of \(P_{O,r}\) is the square one, the smooth model has two rational points at
infinity.  Thus

\[
 \#\mathcal C(\mathbb F_r)=r+C_r(O)+2,
\]

and Hasse--Weil, centered at \(r+1\), gives the sharper shifted form

\[
 \boxed{|C_r(O)+1|\le (k-2)\sqrt r\qquad(k\text{ even}).}                    \tag{5}
\]

For \(k=2\), the genus is zero and (5) says \(C_r=-1\) exactly.  Thus no
exceptional small-degree convention is being hidden in (4)--(5).

For odd \(k\), (3)--(4) imply

\[
 |S_r|\le (k-1)\sqrt r+(s-k)\le (s-1)\sqrt r.
\]

For even \(k\ge2\), rewrite (3) as
\(S_r=(C_r+1)-(R_r+1)\).  Then

\[
 |S_r|\le (k-2)\sqrt r+(s-k+1)\le (s-1)\sqrt r.
\]

Here only \(\sqrt r\ge1\) was used in the last step.  Consequently, on the
odd-pattern branch \(O\ne\varnothing\), (1) yields

\[
 \boxed{|S_r|\le(s-1)\sqrt r,\qquad
        |\mathbb E Y_H|\le\frac{(s-1)^2}{\sqrt N}.}                          \tag{6}
\]

Notice the edge cases: for \(k=s=1\), both local sums and the global mean are
exactly zero; for \(k=2\), the \(-1\) center is essential.  Formula (6) is
false in general when \(O=\varnothing\), which is why its branch condition is
necessary.

## 4. Exact second moment, law, variance, and empirical MSE

Since \(Y_H\in\{-1,0,1\}\), its square is one exactly when none of the shifts
is a root modulo either prime.  There are \(r-s\) allowed residues in each
CRT coordinate.  Therefore

\[
 \boxed{\rho:=\mathbb E Y_H^2
     =\left(1-\frac{s}{p}\right)\left(1-\frac{s}{q}\right).}                \tag{7}
\]

Put

\[
 \zeta=1-\rho=\frac{s(p+q)-s^2}{N}=\frac{s(p+q-s)}N.                         \tag{8}
\]

The full law is determined by \(\theta\) and \(\rho\):

\[
 \boxed{
 \Pr(Y_H=0)=\zeta,\qquad
 \Pr(Y_H=1)=\frac{\rho+\theta}{2},\qquad
 \Pr(Y_H=-1)=\frac{\rho-\theta}{2}.}                                      \tag{9}
\]

It follows exactly that

\[
 \operatorname{Var}(Y_H)=\rho-\theta^2.                                    \tag{10}
\]

For \(m\) independent fresh samples and
\(\widehat\theta_m=m^{-1}\sum_{i=1}^mY_H(x_i)\), unbiasedness and
independence give

\[
 \boxed{\mathbb E(\widehat\theta_m-\theta)^2
        =\frac{\rho-\theta^2}{m}.}                                         \tag{11}
\]

## 5. Odd-pattern relative RMSE on fixed-balance families

Make the balance condition explicit: fix \(\Lambda\ge1\) independently of
\(N\), and suppose

\[
 p,q\le\Lambda\sqrt N.
\]

(Since \(pq=N\), this also gives \(p,q\ge\sqrt N/\Lambda\).)  Let
\(s=s(n)\) be bounded by a fixed polynomial in \(n=\lceil\log_2(N+1)\rceil\).
Then, on the odd-pattern branch,

\[
 \rho-\theta^2
 \ge 1-\frac{2\Lambda s}{\sqrt N}-\frac{(s-1)^4}{N}.                        \tag{12}
\]

The right side is at least \(1/2\) for every sufficiently large member of
the family.  If \(\theta\ne0\), the exact relative RMSE is

\[
 \frac{\sqrt{\mathbb E(\widehat\theta_m-\theta)^2}}{|\theta|}
 =\sqrt{\frac{\rho-\theta^2}{m\theta^2}}.
\]

Combining (6) and (12), relative RMSE at most \(\eta\) implies, for all such
sufficiently large inputs,

\[
 \boxed{m\ge \frac{N}{2\eta^2(s-1)^4}.}                                    \tag{13}
\]

This is an exact implication once the explicit eventual condition
\(2\Lambda s/\sqrt N+(s-1)^4/N\le1/2\) holds; it is not merely a heuristic
scaling statement.  A nonzero odd-pattern mean automatically excludes
\(s=1\).

If \(\theta=0\), relative error with denominator \(|\theta|\) is undefined;
there is no legitimate relative-RMSE conclusion.  The correct statement is
the additive one (11), namely MSE \(\rho/m\).  In particular, replacing a
zero denominator by an arbitrary convention would not prove (13).

## 6. Exact probability of obtaining a direct proper gcd

Here “direct proper gcd” must mean that for at least one individual shift
\(e\in E\),

\[
 1<\gcd(x+e,N)<N.
\]

By injectivity, each CRT coordinate of \(x\) is either not a root or selects
a unique root index.  Count CRT pairs according to those indices:

* a root only modulo \(p\): \(s(q-s)\) points;
* a root only modulo \(q\): \(s(p-s)\) points;
* roots modulo both primes at two different shifts: \(s(s-1)\) points.

Every point in these three disjoint classes gives a proper gcd, and every
proper-gcd point is in one of them.  If the same shift is the root modulo both
primes, there are \(s\) such points and its gcd is \(N\), not a proper factor.
Thus

\[
 \boxed{\Pr(\exists e\in E:1<\gcd(x+e,N)<N)
 =\frac{s(p+q-s-1)}N.}                                                       \tag{14}
\]

This differs from the probability \(\zeta\) of seeing a zero scalar by
exactly \(s/N\), the same-shift \(\gcd=N\) cases.  It also differs from the
probability that the gcd of the whole product is proper; (14) concerns
individual gcd identities.

## 7. The all-even branch

If every multiplicity is even, then (2) and (1) give

\[
 \theta=\rho=\left(1-\frac{s}{p}\right)\left(1-\frac{s}{q}\right)=1-\delta,
\]

where

\[
 \boxed{\delta=\frac{s(p+q)-s^2}{N}.}                                       \tag{15}
\]

For \(s>0\), exact knowledge of the exact mean gives

\[
 \boxed{p+q=\frac{N(1-\theta)+s^2}{s}.}                                    \tag{16}
\]

Together with \(pq=N\), this recovers \(p,q\) as the two integer roots of
\(X^2-(p+q)X+N\), equivalently by taking the exact square root of
\((p+q)^2-4N=(p-q)^2\).  For \(s=0\), the mean is identically one and (16)
is inapplicable, as it must be.

In this branch \(Y_H\) is Bernoulli on \(\{0,1\}\).  Estimating the deviation
with \(\widehat\delta=1-\widehat\theta_m\) gives

\[
 \mathbb E(\widehat\delta-\delta)^2=\frac{\delta(1-\delta)}m,
 \qquad
 \operatorname{relative\ RMSE}(\widehat\delta)
 =\sqrt{\frac{1-\delta}{m\delta}}.                                         \tag{17}
\]

Thus relative RMSE at most \(\eta\) requires exactly

\[
 m\ge\frac{1-\delta}{\eta^2\delta}.                                        \tag{18}
\]

On a fixed-balance family with polynomial positive \(s\), eventually
\(1-\delta\ge1/2\), while \(\delta\le2\Lambda s/\sqrt N\).  Consequently

\[
 \boxed{m\ge\frac{\sqrt N}{4\Lambda\eta^2s}
        =\Omega\!\left(\frac{\sqrt N}{\eta^2s}\right).}                    \tag{19}
\]

The relative target in (17)--(19) is the small deviation \(\delta=1-\theta\),
not the near-one raw mean \(\theta\).  Relative error for the latter would be
a different and much weaker criterion.

## 8. Public zero/one baseline and explicit \(\ell_1\)-bounded drift

The preceding facts extend by linearity to an explicit polynomial statistic.
Let

\[
 F(x)=\sum_{j=1}^M a_jY_{H_j}(x)
\]

be an explicitly listed collection of monomials, after normalization and
difference screening, and write \(s_j=|E_j|\).  Define the public baseline

\[
 b(H_j)=\mathbf 1_{\{O_j=\varnothing\}},\qquad
 B(F)=\sum_{j=1}^M a_jb(H_j).                                                \tag{20}
\]

This is exactly the monomial expectation under public independent fair
Rademacher variables: an all-even monomial has expectation one and every
other monomial has expectation zero.  No knowledge of \(p\), \(q\), or any
character sum is needed to compute (20); one only combines equal residues
modulo \(N\) and reads multiplicity parities.

Equations (6) and (15) give the deterministic drift bound

\[
 \boxed{
 |\mathbb EF-B(F)|
 \le \frac1{\sqrt N}\sum_{j:O_j\ne\varnothing}|a_j|(s_j-1)^2
 +\frac1N\sum_{j:O_j=\varnothing}|a_j|s_j(p+q-s_j).}                         \tag{21}
\]

Under \(\Lambda\)-balance this is at most

\[
 \frac1{\sqrt N}\left[
 \sum_{j:O_j\ne\varnothing}|a_j|(s_j-1)^2
 +2\Lambda\sum_{j:O_j=\varnothing}|a_j|s_j\right].                         \tag{22}
\]

In particular, if the explicit list length, maximum support size, and
\(\|a\|_1=\sum_j|a_j|\) are polynomial in \(n\), then the drift is
\(\operatorname{poly}(n)/\sqrt N\), hence exponentially small in \(n\) on
the fixed-balance family.  This conclusion needs the \(\ell_1\) condition:
cancellation in a compact symbolic representation or exponentially large
coefficients would not be controlled by (21).

There is also an exact fresh conditional version.  Let \(\mathcal F_{t-1}\)
be the complete past, let the explicit lists and coefficients of \(F_t\) be
\(\mathcal F_{t-1}\)-measurable, and then draw \(x_t\) uniformly and
independently modulo \(N\).  Conditional on any realized past, the lists are
fixed and CRT applies exactly as above.  Therefore

\[
 \left|\mathbb E[F_t(x_t)\mid\mathcal F_{t-1}]-B(F_t)\right|                \tag{23}
\]

obeys the right side of (21), with all its quantities evaluated at that
past.  Linearity means (23) may control the conditional mean of several
monomials on one fresh source; it does not by itself control their joint law.

## 9. Exact one-scalar TV distances

For an odd-support query, compare the scalar \(Y_H\) with a fair Rademacher
variable \(R\), so \(Q(1)=Q(-1)=1/2\) and \(Q(0)=0\).  From (9),

\[
\begin{aligned}
 d_{\rm TV}(\mathcal L(Y_H),\mathcal L(R))
 &=\frac12\left[
 \zeta+\left|\frac{\theta-\zeta}{2}\right|
       +\left|\frac{-\theta-\zeta}{2}\right|\right]\\
 &=\frac{\zeta}{2}+\frac{|\theta-\zeta|+|\theta+\zeta|}{4}\\
 &=\boxed{\frac{\zeta+\max(\zeta,|\theta|)}2},                             \tag{24}
\end{aligned}
\]

where the last equality uses
\(|a-b|+|a+b|=2\max(|a|,|b|)\).

For an all-even query, \(Y_H\) equals one with probability \(1-\zeta\) and
zero with probability \(\zeta\).  Against the constant-one reference,

\[
 \boxed{d_{\rm TV}(\mathcal L(Y_H),\delta_1)=\zeta.}                        \tag{25}
\]

Thus both claimed scalar distances are exact, including \(s=0\), when both
sides are identically one.

## 10. Sequential maximal-coupling hybrid

Consider an adaptive protocol which, at call \(i\), chooses \(H_i\) from its
past transcript, screens its differences, and then receives only
\(Y_{H_i}(x_i)\), where \(x_i\) is a new independent uniform residue and is
not itself released.  Let \(s_i\) be the distinct support size.  The reference
protocol uses the same adaptive controller and public randomness, but on an
odd-support query returns a new fair sign and on an all-even query returns
one.

Conditional on any common past before the first disagreement, the same
\(H_i\) is asked in both protocols and the real conditional scalar law is
exactly (9).  Couple that scalar maximally to its reference law.  If a
disagreement occurs, complete the two executions arbitrarily.  The coupling
inequality and a union bound show that transcript TV is at most the sum of
the conditional one-call distances along the common path.  This is the
standard sequential maximal-coupling hybrid; no independence between the
adaptively selected lists is asserted or needed.

Under \(\Lambda\)-balance,

\[
 \zeta_i=\frac{s_i(p+q-s_i)}N\le\frac{2\Lambda s_i}{\sqrt N}.
\]

For odd support, (24), \(\max(a,b)\le a+b\), and (6) give

\[
 d_i\le \zeta_i+\frac{|\theta_i|}{2}
 \le\frac{2\Lambda s_i+s_i^2/2}{\sqrt N}.                                  \tag{26}
\]

For even support, (25) gives

\[
 d_i\le\frac{2\Lambda s_i}{\sqrt N}.                                      \tag{27}
\]

If \(\sum_i s_i\le T\) pathwise (this may include an adaptive stopping
rule), then \(\sum_i s_i^2\le(\sum_i s_i)^2\le T^2\).  Hence

\[
 \boxed{d_{\rm TV}(\text{real transcript},\text{reference transcript})
 \le\frac{2\Lambda T+T^2/2}{\sqrt N}.}                                     \tag{28}
\]

As always, one may additionally cap the displayed upper bound by one.

The reference process itself is public and uniformly implementable.  From
the explicit query and public \(N\), it reduces shifts, combines duplicates,
and tests whether any multiplicity is odd.  It then flips one fair coin or
returns one.  It never needs \(p,q,\theta,\rho\).  The *maximal coupling* is
only an existential proof device and need not be implementable without the
factors; implementability of the reference simulator does not depend on
implementability of that coupling.

## 11. Exact scope of the channel statement

Bound (28) does **not** cover any of the following.

1. **The sampled \(x_i\).**  If \(x_i\) is retained or released, the real
   output is the publicly computable deterministic function \(Y_{H_i}(x_i)\),
   while the reference sign is not.  Marginalizing over a hidden \(x_i\) was
   essential to (24)--(25).
2. **Individual gcd identities.**  A zero product forgets which shift and
   which prime caused it.  Formula (14) shows that the richer gcd event even
   has a different exact probability.
3. **The per-shift character vector.**  Its zero locations and joint
   character relations are not determined by the law of one compressed
   product.
4. **Several correlations from the same \(x_i\).**  Their marginal bounds do
   not sum as fresh-channel bounds; shared-source algebraic relations can be
   exact.
5. **Same-source adaptation.**  A list chosen after seeing \(x_i\), a gcd, or
   another value from that same source is not past-measurable before a fresh
   uniform draw, so the conditional CRT law used in the hybrid is absent.
6. **Exact symbolic character sums or exact means.**  These expose \(S_pS_q\)
   or, in the all-even case, (16); they are not samples from the scalar
   channel.
7. **Arbitrary joint Jacobi processing.**  Data processing covers functions
   of the transcript already compared in (28), but it cannot enlarge that
   transcript to unreleased Jacobi symbols, shared samples, gcd labels, or an
   exponentially represented polynomial.  The \(\ell_1\) drift bound (21)
   controls expectations of explicitly expanded statistics, not arbitrary
   joint distributions.

Thus (28) is a correct but deliberately narrow observation-channel theorem,
not a generic indistinguishability theorem for algorithms that sample and
process Jacobi symbols themselves.

## 12. Uniformity and remaining edge conditions

For polynomial-size explicit lists, normalization uses modular reduction and
a dictionary or sorting; pairwise difference screening uses at most
quadratically many gcd computations.  All operands have \(O(n)\) bits, so
these are uniform polynomial-bit operations.  Multiplicity parity is public.
The extended Jacobi symbol is computable by the Euclidean/Jacobi algorithm
without factoring \(N\), and exact uniform residues modulo \(N\) can be drawn
by rejection from \(n\)-bit strings with constant expected trials.  An
explicit polynomial list of polynomial-bit rational coefficients makes the
baseline and its \(\ell_1\) accounting uniformly computable; arbitrary real
coefficients would not be a bit-complexity statement.

If screening returns a proper gcd, the no-factor character-sum analysis is
unneeded because a factor has already been obtained.  All statements above
are on the branch where every relevant list survives screening.  Empty
support has \(Y\equiv1\), \(S_r=r\), \(\rho=1\), zero drift, and zero TV.
The exact recovery formula and the all-even relative-deviation discussion
explicitly require \(s>0\).  None of the character-sum or sampling bounds by
itself supplies exact symbolic means or a general factoring algorithm.
