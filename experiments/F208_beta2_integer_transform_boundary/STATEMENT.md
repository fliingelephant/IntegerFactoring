# F208 candidate — integer transforms relocate the beta-two selector to a hidden divisor shell

## Status and scope

This is a frozen, self-audited, proof-only candidate. It studies the first
twisted divisor coefficient from P179,

\[
 A(N)=\sum_{d\mid N}d\chi_4(d),
\]

on balanced distinct odd semiprimes. It proves exact identities and exact
relocations inside these named models:

1. reciprocal-floor and Dirichlet-hyperbola transforms;
2. totalized floor reciprocity;
3. Dedekind and cotangent reciprocity;
4. triangular Hermite-normal-form determinant shells;
5. diagonal reduced binary quadratic forms and the principal class;
6. pair-symmetric divisor representation totals; and
7. exact Archimedean magnitude extraction.

It supplies no evaluator for \(A(N)\), no selector algorithm, and no
top-level factoring result. It is not a lower bound against nonlinear
integer algorithms, compressed signed divisor-OR evaluation, adaptive floor
or cotangent aggregates, implicit class-group navigation, asymmetric
representation statistics, or a future one-child recursive construction.

Let

\[
 N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Put

\[
 B=\lfloor\sqrt N\rfloor,\qquad
 \chi=\chi_4,\qquad
 \eta=\chi(N)\in\{+1,-1\}.
\]

For \(d\geq1\), define the exact divisor jump

\[
 J_d(N)=
 \left\lfloor\frac Nd\right\rfloor
 -
 \left\lfloor\frac{N-1}{d}\right\rfloor
 =\mathbf1_{d\mid N}.
\]

## 1. Exact reciprocal-floor shell

Pair every divisor at most \(B\) with its complementary divisor. Then

\[
 \boxed{
 A(N)=
 \sum_{d\leq B}\chi(d)
 \left(
 d+\eta\left\lfloor\frac Nd\right\rfloor
 \right)J_d(N).}
\]

Only \(d=1,p\) survive. Consequently, for the publicly corrected value

\[
 T=A(N)-(1+\eta N),
\]

one has

\[
 \boxed{T=\chi(p)(p+\eta q).}
\]

In particular,

\[
 \boxed{\operatorname{sgn}T=\eta\chi(p)=\chi(q)}
\]

and the selector bit itself is

\[
 \boxed{
 \chi(p)=\sum_{2\leq d\leq B}\chi(d)J_d(N).}
\]

For the opposite-character branch \(N\equiv3\pmod4\),

\[
 \boxed{
 T=A(N)-(1-N)=\chi(p)(p-q).}
\]

Thus the reciprocal-floor transform relocates the sign to a signed OR over
the divisor events below \(\sqrt N\). It does not evaluate that OR.

## 2. Totalized reciprocity has one hidden gcd spike

For odd \(d\), define

\[
\begin{aligned}
 \Delta_N(d)
 &=
 \sum_{i=1}^{(N-1)/2}
 \left\lfloor\frac{id}{N}\right\rfloor
 +
 \sum_{j=1}^{(d-1)/2}
 \left\lfloor\frac{jN}{d}\right\rfloor\\
 &\qquad-
 \frac{(d-1)(N-1)}4.
\end{aligned}
\]

Exact totalized floor reciprocity gives

\[
 \boxed{\Delta_N(d)=\frac{\gcd(d,N)-1}{2}.}
\]

Balance implies

\[
 \frac B2<p\leq B<2p.
\]

Hence \(p\) is the unique integer in \((B/2,B]\) having a nontrivial gcd
with \(N\). Therefore

\[
 \boxed{
 2\sum_{\substack{B/2<d\leq B\\ d\ {\rm odd}}}
 \chi(d)\Delta_N(d)
 =\chi(p)(p-1).}
\]

The absolute value of this aggregate plus one is \(p\). This is an exact
factoring-equivalence statement about this declared aggregate, not an
algorithm for evaluating it. Termwise Euclidean evaluation scans
\(2^{\Theta(\log N)}\) candidates.

## 3. Dedekind and cotangent contraction starts with the gcd

Write

\[
 ((x))=
 \begin{cases}
 x-\lfloor x\rfloor-\tfrac12,&x\notin\mathbb Z,\\
 0,&x\in\mathbb Z,
 \end{cases}
\]

and define

\[
 s(h,k)=
 \sum_{r=0}^{k-1}
 \left(\left(\frac rk\right)\right)
 \left(\left(\frac{hr}{k}\right)\right).
\]

For \(g=\gcd(h,k)\),

\[
 \boxed{s(h,k)=s(h/g,k/g).}
\]

The classical cotangent expression is nonsingular only when \(g=1\). If
\(g>1\), its second cotangent has exactly \(g-1\) poles, at

\[
 r=j\,k/g,\qquad 1\leq j<g.
\]

Thus the standard continued-fraction reciprocity contraction either retains
the full modulus on a unit slope, or first extracts \(g\). For \(h=p,k=N\),
the reduced pair is \((1,q)\), but it appears only after the proper gcd
\(p\) is known.

This does not exclude a compressed aggregate of many unit-slope Dedekind
sums or another nonlinear use of their exact rational values.

## 4. The triangular HNF count is the same determinant shell

Use the triangular Hermite-normal-form convention

\[
 H_{a,b,d}=
 \begin{pmatrix}
 d&b\\
 0&a
 \end{pmatrix},
 \qquad
 a,d>0,\quad 0\leq b<a.
\]

Then

\[
 \boxed{
 A(N)=
 \sum_{\substack{ad=N\\0\leq b<a}}\chi(a).}
\]

Equivalently, if

\[
 \mathcal C(X)=
 \sum_{\substack{a,d\geq1\\ad\leq X}}
 \sum_{0\leq b<a}\chi(a),
\]

then

\[
 \boxed{A(N)=\mathcal C(N)-\mathcal C(N-1).}
\]

The cumulative lattice region may be rearranged by the hyperbola method, but
its adjacent determinant shell is exactly the divisor jump in Section 1.

## 5. The diagonal reduced form already contains the factor

The positive definite primitive form

\[
 \boxed{[p,0,q]}
\]

has discriminant \(-4N\). It is reduced because \(0\leq p<q\), and it is
ambiguous because its middle coefficient is zero. Among literal diagonal
reduced forms \([a,0,c]\) of discriminant \(-4N\), the only possibilities
with \(a\leq c\) are the public principal form \([1,0,N]\) and
\([p,0,q]\).

The latter is not principal: it represents \(p\), whereas
\([1,0,N]\) cannot represent \(p\). Its leading coefficient has character
\(\chi(p)\). Thus locating this nontrivial diagonal form returns the hidden
factor rather than a smaller public class-group state. This statement does
not exclude an implicit class-group statistic that extracts only the
character bit.

## 6. Pair-symmetric representation totals erase the hard branch

Suppose a divisor weight satisfies

\[
 W_N(d)=W_N(N/d).
\]

If \(\eta=-1\), then

\[
 \boxed{
 \sum_{d\mid N}\chi(d)W_N(d)=0.}
\]

Thus every representation total whose divisor formula has this
pair-symmetric twisted weight deletes the opposite-character orientation.
The asymmetric weight \(W_N(d)=d\) in \(A(N)\) is precisely what retains it.

For comparison, the ordinary two-square count satisfies

\[
 r_2(N)=4(1+\chi(p))(1+\chi(q)).
\]

When \(\eta=1\),

\[
 r_2(N)=8(1+\chi(p)),
\]

so two-square representability restates the sign selector on that branch.
When \(\eta=-1\), \(r_2(N)=0\) for both orientations.

No algorithm for deciding the required representation predicate is supplied.

## 7. Exact Archimedean magnitude is the difference-of-squares witness

The corrected magnitude is

\[
 |T|=
 \begin{cases}
 p+q,&\eta=+1,\\
 q-p,&\eta=-1.
 \end{cases}
\]

Accordingly,

\[
 \boxed{|T|^2-4N=(q-p)^2\quad(\eta=+1)}
\]

and

\[
 \boxed{|T|^2+4N=(p+q)^2\quad(\eta=-1).}
\]

Exact magnitude extraction therefore returns the ordinary
difference-of-squares witness. It is not a smaller recursive child. The sign
alone remains the one-bit target described in Section 1.

## Exact remaining gap

The surviving target is an implicit evaluation of

\[
 \sum_{2\leq d\leq B}\chi(d)J_d(N)
\]

without locating the nonzero divisor event term by term. F208 proves no
lower bound against such an evaluator. A nonlinear integer statistic,
adaptive signed aggregate, support-preserving smaller child, or globally
nested recursive selector remains open.
