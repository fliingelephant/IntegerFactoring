# F15 — Hurwitz one-sided-gcd collision kill

**Status:** self-audited. No hostile audit or proof-blind reconstruction has run;
under the project vocabulary this carries the same trust as candidate.

**Classification:** evidence against the exact auxiliary mechanism “take
polynomially many independently and uniformly oriented norm-\(N\) Hurwitz
representations and expose a factor through one-sided Euclidean gcd/ideal
collisions.” This is not a lower bound against designed nonuniform samplers,
sample-dependent nonlinear transforms, or noncommutative factoring methods in
general.

## Prior-route check

There is no close prior route in `FAILED.md`. The nearest routes are X03/F03,
which uses commutative polynomial gcd/rank localization, and X10/F09, which
studies orientation in cyclotomic ideals. The present route differs materially:
it uses the left/right Euclidean structure of the noncommutative Hurwitz order,
and its local obstruction is collision of projective row/image lines of rank-one
matrices.

## Setup

Let \(\mathcal H\) be the Hurwitz order and let

\[
S_N=\{\alpha\in\mathcal H:\operatorname{nrd}(\alpha)=N\},
\qquad N=pq,
\]

where \(p\ne q\) are odd primes. For each \(r\in\{p,q\}\), fix any splitting

\[
\iota_r:\mathcal H/r\mathcal H\simeq M_2(\mathbb F_r).
\]

The reduction \(A_r=\iota_r(\alpha)\) of any \(\alpha\in S_N\) has rank exactly
one: its determinant is zero, while rank zero would mean \(\alpha\in r\mathcal
H\) and hence \(r^2\mid\operatorname{nrd}(\alpha)\). Write

\[
R_r(\alpha)=\operatorname{row}(A_r),\qquad
I_r(\alpha)=\operatorname{im}(A_r),\qquad
K_r(\alpha)=\ker(A_r)
\]

for its projective row, image, and kernel lines. The row line determines the
kernel line, and the image line determines the left-kernel line.

## Theorem 1 — exact orientations and exact gcd law

Uniform \(\alpha\in S_N\) has

\[
(R_p(\alpha),R_q(\alpha))
\sim \operatorname{Unif}\bigl(\mathbf P^1(\mathbb F_p)\times
\mathbf P^1(\mathbb F_q)\bigr).
\]

In particular the two local row lines are independent. The analogous assertion
holds for image lines.

Let \(\alpha,\beta\) be independent uniform elements of \(S_N\), and let \(d_R\)
be a greatest common right divisor. Then

\[
\begin{array}{c|cccc}
\operatorname{nrd}(d_R)&1&p&q&N\\ \hline
\Pr&\dfrac{pq}{(p+1)(q+1)}&
\dfrac{q}{(p+1)(q+1)}&
\dfrac{p}{(p+1)(q+1)}&
\dfrac1{(p+1)(q+1)}.
\end{array}
\]

Consequently the exact probability of a proper right gcd is

\[
\boxed{\Pr(1<\operatorname{nrd}(d_R)<N)
=\frac{p+q}{(p+1)(q+1)}.}
\]

The same formula holds for a greatest common left divisor.

Computing both handednesses for each independent pair can increase the success
probability by at most a factor of two; no independence between the two gcd events
is assumed for this union bound.

There is an identical law for the most immediate noncommutative product test. For
independent uniform \(\alpha,\beta\), the local product \(A_rB_r\) is zero exactly
when

\[
I_r(\beta)=K_r(\alpha).
\]

These are independent uniform projective lines, so the event again has probability
\(1/(r+1)\), independently at \(p\) and \(q\). Hence the probability that
\(\alpha\beta\) is zero modulo exactly one factor is the same boxed value. This
covers the basic row/kernel/image incidence suggested by multiplying principal
one-sided ideals.

### Proof: representation count and orientation fibers

For odd \(m\), Jacobi's four-square formula gives \(r_4(m)=8\sigma(m)\).
Half-integral Hurwitz elements of norm \(m\) correspond, after doubling the
coordinates, to all-odd representations of \(4m\) by four squares. Modulo four,
a representation of \(4m\) has either zero or four odd coordinates. The all-even
ones are in bijection with the representations of \(m\), while

\[
r_4(4m)=8\sum_{\substack{d\mid4m\\4\nmid d}}d
=24\sigma(m).
\]

Thus the half-integral count is \(16\sigma(m)\), and

\[
|S_m|=24\sigma(m).
\]

For \(m=pq\), this is \(24(p+1)(q+1)\).

Left multiplication by the 24 Hurwitz units acts freely on \(S_N\) and preserves
both row lines. Conversely, suppose \(\alpha,\beta\in S_N\) have the same row line
modulo both \(p\) and \(q\). In \(M_2(\mathbb F_r)\), if rank-one matrices \(A,B\)
have the same row line, then

\[
B\operatorname{adj}(A)=0.
\]

Therefore \(\beta\bar\alpha\in p\mathcal H\cap q\mathcal H=N\mathcal H\), so

\[
u=\frac{\beta\bar\alpha}{N}\in\mathcal H,
\qquad \operatorname{nrd}(u)=1,
\qquad \beta=u\alpha.
\]

Hence the row-line map is injective on left-unit orbits. Its domain and codomain
both have \((p+1)(q+1)\) elements, so it is a bijection. Every orientation pair
therefore has exactly 24 preimages. Conjugating the argument, or using right-unit
orbits, proves the image-line assertion.

### Proof: one-sided gcd

The Hurwitz order is left and right Euclidean. If \(d_R\) is a greatest common
right divisor, then

\[
\mathcal H\alpha+\mathcal H\beta=\mathcal H d_R.
\]

Modulo \(r\), the left ideal \(M_2(\mathbb F_r)A_r\) is the minimal left ideal
of matrices whose rows lie in \(R_r(\alpha)\). Two such ideals have proper sum
exactly when their row lines agree; distinct row lines span all of
\(M_2(\mathbb F_r)\). It follows that

\[
r\mid\operatorname{nrd}(d_R)
\quad\Longleftrightarrow\quad
R_r(\alpha)=R_r(\beta).
\]

Also \(\operatorname{nrd}(d_R)\mid N\), because \(d_R\) right-divides an element
of squarefree norm \(N\). Thus its norm is one of \(1,p,q,N\). The two equality
events have probabilities \(1/(p+1)\) and \(1/(q+1)\) and are independent, which
gives the table. Right ideals and image lines give the left-gcd version. \(\square\)

## Corollary 2 — polynomially many uniform samples do not reach birthday scale

For \(K\) independent uniform samples, testing every pair with one fixed
handedness succeeds with probability at most

\[
\binom K2\frac{p+q}{(p+1)(q+1)}.
\]

The exact probability of at least one row-line collision in the \(r\)-component
is the ordinary occupancy probability

\[
C_r(K)=1-\frac{(r+1)_K}{(r+1)^K}
\quad(K\le r+1),
\]

where \((r+1)_K\) is the falling factorial; it is one for \(K>r+1\). The two
local occupancy experiments are independent.
Existence of a proper pair is equivalent to the two complete equality partitions
being different; the displayed pairwise union bound is sufficient here and avoids
an unnecessary partition sum.

More generally, the local lattice generated from the minimal left ideals by sums
and intersections depends only on the equality partition of the row lines:
distinct minimal left ideals have zero intersection and full sum. Therefore any
construction using only these ideal sums, intersections, inclusions, equalities,
and ranks can differ between the two local components only if some local pair
collides. Its probability is at most

\[
\binom K2\left(\frac1{p+1}+\frac1{q+1}\right).
\]

A polynomial collection of cross-sample product-rank tests has the same type of
bound: each specified incidence has local probability \(1/(r+1)\), so a union
bound over the polynomially many specified incidences remains
\(\operatorname{poly}(\log N)(1/p+1/q)\).

On balanced semiprimes \(p<q<2p\), both bounds are
\(O(K^2/\sqrt N)\). For \(K=\operatorname{poly}(\log N)\), this is
exponentially small in the input bit length. Thus the natural route needs
\(K=\Theta(N^{1/4})\) samples to approach birthday scale, not
\(\operatorname{poly}(\log N)\). Bertrand's postulate supplies arbitrarily large
distinct prime pairs in this balanced range, so this is a genuine worst-case
family rather than a conditional density assumption.

## Fixed transforms and conjugation

The following checks prevent several apparent escapes, while deliberately leaving
adaptive/nonuniform constructions outside the claim.

1. **Different independent source samples.** Conditional on any public fixed
   transforms

   \[
   \alpha\longmapsto a\alpha b
   \quad\text{or}\quad
   \alpha\longmapsto a\bar\alpha b,
   \]

   where the multiplier norms are coprime to \(N\), each local multiplier is
   invertible. Conjugation permutes \(S_N\), left multiplication preserves a row
   line, and right multiplication acts projectively on it. Hence a transformed
   sample is still uniformly oriented. Comparisons coming from different source
   samples retain the exact probability in Theorem 1. A polynomial menu only
   multiplies the union bound by its polynomial size.

2. **Two unbarred transforms of one source.** Comparing \(\alpha b_1\) and
   \(\alpha b_2\) asks whether a uniform projective line is fixed by the relative
   projective transformation \(b_2^{-1}b_1\). A non-scalar element of
   \(PGL_2(\mathbb F_r)\) fixes at most two projective lines, so the local collision
   probability is at most \(2/(r+1)\). If the relative quaternion is scalar modulo
   exactly one of \(p,q\), the gcd of \(N\) with the three coordinates of its
   trace-free part already exposes that factor before any quaternion gcd. If it is
   scalar in both components, the two projective actions agree everywhere and the
   collision is simultaneous and trivial.

3. **Self-conjugation.** For rank-one \(A\in M_2(\mathbb F_r)\),

   \[
   \operatorname{row}(A)=\operatorname{row}(\operatorname{adj}A)
   \quad\Longleftrightarrow\quad \operatorname{tr}(A)=0.
   \]

   Indeed \(\operatorname{adj}A=\operatorname{tr}(A)I-A\); equality of the two
   one-dimensional row spaces would make \(\operatorname{tr}(A)I\) have rank at
   most one unless the trace is zero. Consequently a right gcd of \(\alpha\) and
   \(\bar\alpha\) is proper exactly when \(\gcd(\operatorname{tr}\alpha,N)\) is
   proper. Conjugation has only repackaged an ordinary coefficient gcd.

4. **One barred and one unbarred fixed transform.** Put \(X=AB\) and
   \(Y=\operatorname{adj}(A)C\). Since rank-one matrices have the same row line
   exactly when \(X\operatorname{adj}(Y)=0\),

   \[
   \operatorname{row}(AB)=
   \operatorname{row}(\operatorname{adj}(A)C)
   \quad\Longleftrightarrow\quad
   \operatorname{tr}\bigl(B\operatorname{adj}(C)A\bigr)=0.
   \]

   Here we used \(ATA=\operatorname{tr}(TA)A\) for rank-one \(A\). The right side
   is an explicit linear form in the four coordinates of \(\alpha\). Any asymmetric
   local collision is therefore already exposed by the ordinary gcd of this scalar
   with \(N\). A useful inverse-polynomial zero-density theorem for a family of
   such forms would be a separate commutative separator, not an advantage supplied
   by the Euclidean quaternion gcd.

These statements cover fixed unit/coprime left-right transforms, with optional
conjugation, and pairwise gcds. They do not cover a transform chosen from hidden
sample-dependent information or a nonlinear canonicalization procedure.
Left-handed analogues follow by reversing multiplication, or equivalently by
conjugating the displayed right-handed statements.

## Sampling audit

There are three different sampling claims, and only the first is standard.

* Finding **some** four-square representation of an arbitrary integer is available
  by unconditional randomized expected-polynomial algorithms; Rabin--Shallit give
  such algorithms (their operation counts translate to polynomial bit complexity
  because all operands have polynomially many input bits).
* Those algorithms do not, merely by finding a representation, prove an exact
  uniform distribution on \(S_N\), or even on its projective orientation pairs.
  Multiplying one output by random left units does not change its row orientation;
  random right units explore at most the constant-size projective image of the
  24-element unit group and cannot uniformize \((p+1)(q+1)\) orientations.
* No unconditional expected-\(\operatorname{poly}(\log N)\) exact-uniform sampler
  is established by this route. This is a missing algorithmic premise, not a
  nonexistence theorem. Exact counting would itself reveal the factors on a
  semiprime, because

  \[
  |S_N|=24(p+1)(q+1)=24(N+p+q+1),
  \]

  but exact sampling need not in general compute the cardinality, so this does not
  prove sampling hard.

Background references for the distinction are Rabin and Shallit,
[*Randomized Algorithms in Number Theory*](https://doi.org/10.1002/cpa.3160390713),
and Pollack and Treviño,
[*Finding the Four Squares in Lagrange's Theorem*](https://pollack.uga.edu/finding4squares.pdf),
which establish unconditional expected-polynomial find-one algorithms. Their
find-one guarantees are not exact-uniform-sampling guarantees.

## Arbitrary nonuniform distributions: exact boundary

Let \(\mu\) be any distribution on
\(\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)\), with marginals
\(\mu_p,\mu_q\). For two independent draws from \(\mu\), the proper-right-gcd
probability is exactly

\[
\sum_L\mu_p(L)^2+\sum_M\mu_q(M)^2
-2\sum_{L,M}\mu(L,M)^2.
\]

Thus nonuniformity can defeat the uniform obstruction: a distribution concentrated
on one \(p\)-line and spread over \(q\)-lines has large proper-gcd probability.
The missing task is to construct such an asymmetrically concentrated distribution
without knowing \(p,q\), and to sample it in unconditional expected
\(\operatorname{poly}(\log N)\) bit complexity. Nothing above rules that out.

## Conclusion and retry condition

No materially new surviving mechanism was found inside the proposed uniform
Hurwitz-gcd family. Even granting exact uniform samples for free, polynomially many
one-sided gcds and pure ideal collisions have exponentially small success on
balanced semiprimes. Fixed unit/coprime transforms preserve that obstruction or
reduce a collision to an already-computable scalar gcd; conjugation does not by
itself add information.

A retry is materially new only if it supplies at least one of:

1. a factor-free sampler with a proved inverse-polynomial asymmetric collision
   energy under the exact nonuniform formula above;
2. an adaptive/nonlinear transform whose local fixed locus has proved
   inverse-polynomial density and whose defining scalar coefficients do not already
   expose the same factor; or
3. a non-collision quaternion invariant not determined by equality partitions of
   projective row/image lines.

## Computation

No computation was used. All claims above are symbolic, so there is no run or
manifest for this family.
