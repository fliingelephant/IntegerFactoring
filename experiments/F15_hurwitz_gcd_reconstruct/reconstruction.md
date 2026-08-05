# Independent reconstruction: Hurwitz one-sided-gcd collisions

This document proves the squarefree odd-semiprime theorem from the stated
premises.  It fixes the handedness conventions explicitly, and separates the
exact algebraic theorem from the unproved algorithmic premise that exact
uniform samples can be generated.

## 1. The order, involution, and norm

Let

\[
  \mathbb H_{\mathbb Q}=\mathbb Q+\mathbb Qi+\mathbb Qj+\mathbb Qk,
  \qquad i^2=j^2=k^2=ijk=-1,
\]

with \(k=ij=-ji\).  The normalized Hurwitz order is

\[
  \mathcal H=\mathbb Z\left[i,j,\frac{1+i+j+k}{2}\right].
\]

Writing \(x=a+bi+cj+dk\), its additive description is

\[
 \mathcal H=
 \{(a,b,c,d)\in\mathbb Z^4\}
 \mathbin{\sqcup}
 \{(a,b,c,d)\in(\mathbb Z+\tfrac12)^4\}.
\]

Quaternion conjugation, reduced trace, and reduced norm are

\[
 \bar x=a-bi-cj-dk,\qquad
 \operatorname{trd}(x)=x+\bar x=2a,\qquad
 \operatorname{nrd}(x)=x\bar x=a^2+b^2+c^2+d^2.
\]

Conjugation preserves \(\mathcal H\), the reduced trace and norm are integers
on \(\mathcal H\), and the norm is multiplicative.  Set

\[
  S_m=\{x\in\mathcal H:\operatorname{nrd}(x)=m\}.
\]

The norm-one group \(\mathcal H^\times\) has 24 elements.  Indeed, an integral
coordinate vector of norm one is one of the eight signed coordinate vectors,
and a half-integral one must have all four coordinates equal to \(\pm1/2\),
giving sixteen more.  Positivity of the norm shows that these, and only these,
are the units.

### Euclidean and principal-ideal lemma

The norm is a two-sided Euclidean function on \(\mathcal H\).  For any real
quaternion \(z\), round its four coordinates to integers.  The squared error
is at most one.  Equality can occur only when all four coordinate errors have
absolute value \(1/2\), in which case \(z\) itself differs from a Hurwitz
half-integral lattice point by zero.  Thus some \(q\in\mathcal H\) always
satisfies

\[
  \operatorname{nrd}(z-q)<1.
\]

For \(a,b\in\mathcal H\), \(b\ne0\), apply this to \(ab^{-1}\) to get
\(a=qb+r\) with \(\operatorname{nrd}(r)<\operatorname{nrd}(b)\), and to
\(b^{-1}a\) to get \(a=bq+r\) with the same inequality.  Choosing a
least-norm nonzero element in a one-sided ideal and dividing proves:

* every nonzero left ideal is \(\mathcal H d\);
* every nonzero right ideal is \(d\mathcal H\).

For nonzero \(d\), right or left multiplication by \(d\) has real determinant
\(\operatorname{nrd}(d)^2\).  Consequently

\[
 [\mathcal H:\mathcal H d]
 =[\mathcal H:d\mathcal H]
 =\operatorname{nrd}(d)^2. \tag{1}
\]

## 2. Odd local matrix models

For every odd prime \(r\), fix an algebra isomorphism

\[
  \phi_r:\mathcal H/r\mathcal H\overset\sim\longrightarrow M_2(\mathbb F_r).
\]

For completeness, such a splitting can be built directly.  Choose
\(x,y\in\mathbb F_r\) with \(x^2+y^2=-1\), and put

\[
 I=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 J=\begin{pmatrix}x&y\\y&-x\end{pmatrix}.
\]

Then \(I^2=J^2=-1\) and \(IJ=-JI\), so \(i\mapsto I,j\mapsto J\) gives the
desired isomorphism.  The equation \(x^2+y^2=-1\) always has a solution: if
\(-1\) is a square this is immediate, and otherwise it follows from the
surjectivity of the norm \(\mathbb F_{r^2}^{\times}\to\mathbb F_r^{\times}\).
The factor \(1/2\) in the Hurwitz basis is legitimate because \(r\) is odd.

Under every such splitting,

\[
 \phi_r(\bar z)=\operatorname{adj}(\phi_r(z)),\qquad
 \operatorname{trd}(z)\bmod r=\operatorname{tr}(\phi_r(z)),\qquad
 \operatorname{nrd}(z)\bmod r=\det(\phi_r(z)). \tag{2}
\]

Let \(N=pq\), where \(p\ne q\) are odd primes, and let \(\alpha\in S_N\).
For \(r\in\{p,q\}\), write \(A_r=\phi_r(\alpha\bmod r)\).  Equation (2)
gives \(\det A_r=0\).  Also \(A_r\ne0\): otherwise
\(\alpha\in r\mathcal H\), say \(\alpha=r\gamma\), which would make
\(r^2\mid\operatorname{nrd}(\alpha)=pq\).  Hence

\[
 \operatorname{rank} A_p=\operatorname{rank} A_q=1. \tag{3}
\]

For a rank-one matrix \(A\), define

* \(\rho(A)\in\mathbf P^1(\mathbb F_r)\) to be its one-dimensional row
  space;
* \(\iota(A)\in\mathbf P^1(\mathbb F_r)\) to be its one-dimensional image
  (column) space.

The splitting changes the coordinates of these lines, but not any equality
test used below.

## 3. Orbit-line bijections and the exact count

For a line \(L\subset\mathbb F_r^2\), define the minimal left ideal

\[
 J_r(L)=\{X\in M_2(\mathbb F_r):\text{each row of }X\text{ lies in }L\}.
\]

It has dimension two, and for rank-one \(A\),

\[
 M_2(\mathbb F_r)A=J_r(\rho(A)). \tag{4}
\]

Given \((L_p,L_q)\in\mathbf P^1(\mathbb F_p)\times
\mathbf P^1(\mathbb F_q)\), use the Chinese remainder theorem to define the
left ideal

\[
 I(L_p,L_q)=\{x\in\mathcal H:
   \phi_p(x)\in J_p(L_p),\ \phi_q(x)\in J_q(L_q)\}.
\]

Each local condition has codimension two, so

\[
 [\mathcal H:I(L_p,L_q)]=p^2q^2=N^2. \tag{5}
\]

The principal-ideal lemma gives \(I(L_p,L_q)=\mathcal H\alpha\), and (1),
(5) give \(\operatorname{nrd}(\alpha)=N\).  The CRT also makes each local
projection of this ideal onto \(J_r(L_r)\) surjective: lift the pair consisting
of a prescribed element of \(J_r(L_r)\) and zero at the other prime.
Reduction and (4) therefore show \(\rho(A_r)=L_r\).

Conversely, for \(\alpha\in S_N\), the ideal \(\mathcal H\alpha\) is
contained in the ideal prescribed by its two row lines.  Both have index
\(N^2\), so they are equal.  Finally,

\[
 \mathcal H\alpha=\mathcal H\beta,\quad
 \operatorname{nrd}(\alpha)=\operatorname{nrd}(\beta)=N
 \quad\Longleftrightarrow\quad
 \beta=u\alpha\text{ for some }u\in\mathcal H^\times.
\]

This proves the bijection

\[
 S_N/\mathcal H^\times_{\rm left}
 \overset\sim\longrightarrow
 \mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q),
 \qquad
 [\alpha]\longmapsto(\rho(A_p),\rho(A_q)). \tag{6}
\]

The unit action is free because a nonzero quaternion is invertible over
\(\mathbb Q\).  Since \(|\mathbf P^1(\mathbb F_r)|=r+1\), (6) gives

\[
 |S_N|=24(p+1)(q+1). \tag{7}
\]

The right-handed version is obtained from

\[
 K_r(C)=\{X\in M_2(\mathbb F_r):\operatorname{im}X\subset C\},
 \qquad A M_2(\mathbb F_r)=K_r(\iota(A)).
\]

Its CRT preimage is a right ideal of index \(N^2\), hence principal.  Therefore

\[
 S_N/\mathcal H^\times_{\rm right}
 \overset\sim\longrightarrow
 \mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q),
 \qquad
 [\alpha]\longmapsto(\iota(A_p),\iota(A_q)). \tag{8}
\]

## 4. Handed gcd conventions and their local control

The naming convention is the side on which the divisor occurs.

* A **right divisor** \(d\) of \(\alpha\) means \(\alpha=a d\).  A greatest
  common right divisor \(d_R\) of \(\alpha,\beta\) is a generator

  \[
    \mathcal H\alpha+\mathcal H\beta=\mathcal H d_R. \tag{9}
  \]

  It is unique up to multiplication by a unit on the left.  Every common right
  divisor divides \(d_R\) on the right.

* A **left divisor** \(d\) means \(\alpha=d a\).  A greatest common left
  divisor \(d_L\) is a generator

  \[
    \alpha\mathcal H+\beta\mathcal H=d_L\mathcal H. \tag{10}
  \]

  It is unique up to multiplication by a unit on the right.

Existence in (9), (10) follows from the principal-ideal lemma.  If
\(\alpha,\beta\in S_N\), multiplicativity shows that the norm of either common
divisor divides \(N\).

Reduce (9) modulo \(r\in\{p,q\}\).  By (4),

\[
 M_2A_r+M_2B_r
 =J_r(\rho(A_r))+J_r(\rho(B_r)).
\]

The right side has dimension two when the two row lines agree and dimension
four when they differ.  The reduction of \(\mathcal H d_R\) is therefore a
minimal left ideal in the first case and the whole matrix algebra in the
second.  Since \(\operatorname{nrd}(d_R)\mid N\), this is exactly

\[
 r\mid\operatorname{nrd}(d_R)
 \quad\Longleftrightarrow\quad
 \rho(A_r)=\rho(B_r). \tag{11}
\]

Likewise, (10) and the image ideals give

\[
 r\mid\operatorname{nrd}(d_L)
 \quad\Longleftrightarrow\quad
 \iota(A_r)=\iota(B_r). \tag{12}
\]

Equations (11), (12) are the handedness dictionary: **row lines control right
divisors; image lines control left divisors**.

## 5. Exact law for two uniform samples

By (6), a uniform \(\alpha\in S_N\) has a uniform row-line pair in
\(\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)\).  In particular,
its two prime components are independent.  Two independent uniform samples
give independent line pairs.  Therefore row-line equality has probability
\(1/(r+1)\) at \(r\), independently at \(p\) and \(q\).  From (11),

\[
\begin{array}{c|c}
 \operatorname{nrd}(d_R)&\Pr\\ \hline
 1&\dfrac{pq}{(p+1)(q+1)}\\[4pt]
 p&\dfrac{q}{(p+1)(q+1)}\\[4pt]
 q&\dfrac{p}{(p+1)(q+1)}\\[4pt]
 N&\dfrac{1}{(p+1)(q+1)}.
\end{array} \tag{13}
\]

The image-orbit bijection (8) gives exactly the same table for \(d_L\).

Nothing in (6) and (8) says that the row line and image line of the **same**
sample are independent.  They must not be treated as independent when a test
mixes handedness.  Only each fixed-handed marginal, and its two-prime product
structure, has been proved here.

## 6. Equivalent product-zero coordinate tests

For rank-one \(2\times2\) matrices,

\[
 \operatorname{im}(\operatorname{adj}B)=\ker B,
 \qquad
 \ker(\operatorname{adj}B)=\operatorname{im}B.
\]

It follows that

\[
 A\operatorname{adj}(B)=0
 \Longleftrightarrow \ker A=\ker B
 \Longleftrightarrow \rho(A)=\rho(B), \tag{14}
\]

and

\[
 \operatorname{adj}(A)B=0
 \Longleftrightarrow \iota(A)=\iota(B). \tag{15}
\]

Fix any integral \(\mathbb Z\)-basis of \(\mathcal H\).  For \(z\in\mathcal H\)
let

\[
 c_N(z)=\gcd(N,\text{the four integral basis coordinates of }z).
\]

Then (2), (14), and (15) show

\[
 \begin{aligned}
 r\mid c_N(\alpha\bar\beta)
   &\Longleftrightarrow \rho(A_r)=\rho(B_r),\\
 r\mid c_N(\bar\alpha\beta)
   &\Longleftrightarrow \iota(A_r)=\iota(B_r).
 \end{aligned} \tag{16}
\]

Thus either coordinate-content test has the same four-value law (13), and the
probability of a proper factor is the same proper-xor probability

\[
 \delta_{p,q}
 =\Pr(\text{equality at exactly one of }p,q)
 =\frac{p+q}{(p+1)(q+1)}. \tag{17}
\]

Again, (16) does not make the row and image tests on one sample or one pair
independent.

## 7. Birthday bound and the justified menu extension

For \(K\) independent uniform samples and all \(\binom K2\) pairs in one fixed
handedness, the union bound and (17) give

\[
 \Pr(\text{some pair returns a proper factor})
 \le {K\choose2}\frac{p+q}{(p+1)(q+1)}. \tag{18}
\]

No independence between different pairs is needed for (18).  If \(p\) and
\(q\) are balanced, meaning their ratio is bounded above and below by fixed
positive constants, then \(\delta_{p,q}=\Theta(N^{-1/2})\).  A success
probability bounded below by a positive constant therefore requires

\[
 K=\Omega(N^{1/4}). \tag{19}
\]

There is a precise, limited extension to local ideal computations.  The
minimal left ideals \(J_r(L)\) satisfy

\[
 J_r(L)+J_r(M)=
 \begin{cases}J_r(L)&L=M,\\M_2(\mathbb F_r)&L\ne M,\end{cases}
 \qquad
 J_r(L)\cap J_r(M)=
 \begin{cases}J_r(L)&L=M,\\0&L\ne M.\end{cases} \tag{20}
\]

Hence every iterated sum, intersection, or vector-space-rank computation on a
fixed-handed collection of reduced principal ideals is determined solely by
the equality partition of its projective lines.  If the local structural
outputs at \(p\) and \(q\) differ, some pair of lines is equal at exactly one
prime.  Thus any fixed menu of such operations on the same \(K\) raw ideals is
still covered by (18), regardless of how many redundant expressions the menu
contains.  The image/right-ideal version is identical.

More generally, a predetermined menu of \(T\) comparisons, each between
orientations coming from distinct independent samples after a fixed
projective bijection, has success probability at most \(T\delta_{p,q}\).  In
particular a menu polynomial in the input length \(\log N\) remains negligible
on balanced semiprimes.  This statement does **not** cover arbitrary matrix
linear combinations, mixed-handed tests, non-bijective local maps, or adaptive
sample distributions.

## 8. Fixed transforms

### 8.1 Distinct independent sources

Let \(\alpha_s\) be independent uniform elements of \(S_N\), and let

\[
 x_s=a_s\alpha_s b_s,
 \qquad a_s,b_s\in\mathcal H,
 \qquad \gcd(\operatorname{nrd}(a_s)\operatorname{nrd}(b_s),N)=1.
\]

At \(r=p,q\), the fixed matrices \(A_s=\phi_r(a_s)\) and
\(B_s=\phi_r(b_s)\) are invertible, and

\[
 \rho(\phi_r(x_s))=\rho(\phi_r(\alpha_s))B_s,
 \qquad
 \iota(\phi_r(x_s))=A_s\iota(\phi_r(\alpha_s)). \tag{21}
\]

Each is a projective permutation, so fixed transforms preserve exact uniform
local orientations and independence between distinct sources.  The same is
true for random transforms independent of the sources after conditioning on
their values, provided their norms are always coprime to \(N\).

Let \(d_R\) be a greatest common right divisor of two such transformed
samples.  Even when the transforms are non-units, the exact statement is

\[
 \gcd(\operatorname{nrd}(d_R),N)
 \in\{1,p,q,N\}
\]

with the probabilities in (13).  The analogous statement holds for a greatest
common left divisor.  One must not silently replace this by a law for the full
norm.  If

\[
 M_s=\operatorname{nrd}(a_s)\operatorname{nrd}(b_s),
\]

then only

\[
 \operatorname{nrd}(d_R)\mid\gcd(NM_1,NM_2) \tag{22}
\]

is automatic.  For example, if \(x_1=\alpha_1c\) and
\(x_2=\alpha_2c\) for a non-unit \(c\) of norm coprime to \(N\), then \(c\)
is already a common right divisor, so its multiplier primes occur in the full
gcd norm.  If \(\gcd(M_1,M_2)=1\), (22) rules out such extra primes and the
full norm again has table (13).

If a transform norm is not coprime to \(N\), its local matrix can be singular
and (21) need not be a projective permutation.  That case has a different law;
moreover \(\gcd(N,\operatorname{nrd}(a_s)\operatorname{nrd}(b_s))\) should be
checked first because it may already be a factor.

### 8.2 Two right transforms of one source

Now take one uniform \(\alpha\in S_N\) and
\(x_1=\alpha b_1,x_2=\alpha b_2\), with both transform norms coprime to
\(N\).  At \(r\), put \(B_i=\phi_r(b_i)\) and let

\[
 T_r=B_1B_2^{-1}\in\operatorname{PGL}_2(\mathbb F_r).
\]

For \(L=\rho(A_r)\),

\[
 LB_1=LB_2\quad\Longleftrightarrow\quad LT_r=L. \tag{23}
\]

Thus the relative projective element is \(B_1B_2^{-1}\), in that order.  Let
\(f_r\) be its number of fixed points on \(\mathbf P^1(\mathbb F_r)\).  A
non-scalar \(2\times2\) matrix has at most two projective eigenlines, so
\(f_r\le2\); a scalar has \(f_r=r+1\).  Since the row components of one
uniform sample at \(p\) and \(q\) are themselves independent, the exact
proper-xor probability for this comparison is

\[
 \frac{f_p(q+1-f_q)+f_q(p+1-f_p)}{(p+1)(q+1)}. \tag{24}
\]

When both relative elements are non-scalar, (24) is at most

\[
 \frac2{p+1}+\frac2{q+1}=O(N^{-1/2})
\]

for balanced semiprimes.

The apparent exceptional case in which scalarity holds at exactly one prime
is not hidden.  Put

\[
 z=b_1\bar b_2,\qquad z^0=z-\bar z.
\]

Modulo \(r\),

\[
 \phi_r(z)=\det(B_2)B_1B_2^{-1}.
\]

Because \(r\) is odd, a matrix is scalar iff its trace-free part is zero.
Consequently

\[
 g_{\rm sc}=\gcd(N,\text{the integral coordinates of }z^0) \tag{25}
\]

is exactly the product of the primes at which \(T_r\) is scalar.  Equivalently,
one may take the gcd with the three integer coefficients of
\(z-\bar z\) along \(i,j,k\).  If scalarity mismatches between \(p\) and
\(q\), (25) is already the proper factor.  If (25) is 1, both local elements
are non-scalar and the fixed-point bound applies.  If (25) is \(N\), both are
scalar and this pair collides at both primes, yielding no proper xor.

For two fixed left transforms of one source and an image-line/left-gcd test,
the identical argument uses the relative column action
\(A_2^{-1}A_1\).

## 9. Conjugation and mixed barred/unbarred forms

### 9.1 Self-conjugation

Let \(A=A_r\) be nonzero rank one and let \(t=\operatorname{tr}A\).  Since
\(\operatorname{adj}A=tI-A\),

\[
 \rho(A)=\rho(\operatorname{adj}A)
 \quad\Longleftrightarrow\quad t=0, \tag{26}
\]

and the same equivalence holds for image lines.  The forward implication is
worth checking: if the two row spaces agree and \(t\ne0\), then
\(tI=A+\operatorname{adj}A\) would have its row space inside one line, which
is impossible.  The reverse implication is \(\operatorname{adj}A=-A\).

Thus comparison of \(\alpha\) with \(\bar\alpha\) collides locally exactly
when

\[
 \operatorname{trd}(\alpha)\equiv0\pmod r. \tag{27}
\]

The same fact follows from Cayley--Hamilton:
\(A^2=tA\), so the corresponding product-zero test is zero exactly when
\(t=0\).  Therefore

\[
 \gcd(N,\operatorname{trd}(\alpha))
\]

already returns the product of the self-conjugating local primes.  A proper
self-conjugation mismatch is a direct trace gcd, not an additional independent
birthday event.

### 9.2 The valid central linear-form reduction

For central integers \(a,b\), define

\[
 F_{a,b}(\alpha)=a\alpha+b\bar\alpha.
\]

The exact global identities are

\[
 F_{a,b}(\alpha)=(a-b)\alpha+b\operatorname{trd}(\alpha), \tag{28}
\]

and

\[
 \operatorname{nrd}(F_{a,b}(\alpha))
 =(a-b)^2N+ab\operatorname{trd}(\alpha)^2. \tag{29}
\]

At \(r\mid N\), put again \(t=\operatorname{tr}A\).  Then

\[
 \det(aA+b\operatorname{adj}A)=ab\,t^2. \tag{30}
\]

This completely describes the local reduction:

* If \(t\ne0\) and \(a,b\ne0\pmod r\), the genuinely mixed form is
  invertible, not rank one.
* If \(t\ne0\) and exactly one coefficient is nonzero, the form is a scalar
  multiple of \(A\) or of \(\operatorname{adj}A\).
* If \(t=0\), then \(\operatorname{adj}A=-A\) and the form is
  \((a-b)A\), unless it is the zero matrix.

Thus central barred/unbarred one-source linear forms reduce to coefficient
gcds, the trace gcd (27), and the two pure orientations \(A\) and
\(\operatorname{adj}A\).  In particular, a difference between the primes
caused by a coefficient being zero is already exposed by a gcd of that fixed
coefficient with \(N\), and a difference caused by self-conjugation is exposed
by the trace gcd.

More generally, for central coefficients,

\[
 \sum_s(a_s\alpha_s+b_s\bar\alpha_s)
 =\sum_s(a_s-b_s)\alpha_s
  +\left(\sum_s b_s\operatorname{trd}(\alpha_s)\right)1. \tag{31}
\]

Equation (31) legitimately eliminates the bars, but sums involving several
sources need not remain rank one.  No collision lower bound for arbitrary
multi-source linear forms, noncentral quaternion coefficients, or nonlinear
expressions follows from the present theorem.

## 10. Exclusions, sampling premise, and retry boundary

### Why \(2\) is excluded

The Hurwitz order is ramified at 2.  Its reduction modulo 2 is not the simple
matrix algebra \(M_2(\mathbb F_2)\); it has non-semisimple behavior, and the
minimal-ideal/projective-line classification used in (3)--(20) fails.  The
use of \(1/2\), trace-free parts, and scalar tests also explicitly required odd
characteristic.

### Why repeated primes are excluded

For norm divisible by \(r^2\), a reduction can be zero, and a nonzero
rank-one reduction no longer records the full local valuation.  At norm
\(r^2\), local ideals include both the scalar ideal \(r\mathcal H\) and
depth-two oriented ideals.  One projective line is therefore insufficient,
and there is no independent two-prime CRT pair.  Thus neither the product
parameter space in (6) nor the squarefree valuation argument in (11) applies.

### Exact-uniform sampling is a premise, not an algorithm here

The probability statements assume iid exact-uniform draws from the finite set
\(S_N\).  The orbit theorem proves what their orientations would be; it does
not provide an efficient exact-uniform sampler.  In particular, an algorithm
that merely finds one representation of \(N\) by four squares has produced
one element, not a uniform orbit in (6) or (8).  Randomizing that one element
by left units stays in the same row-line orbit.  Any claimed factoring runtime
must separately prove the distribution and cost of its sampler.

### Boundary of the negative conclusion

The proved retry obstruction is limited to:

1. iid exact-uniform samples;
2. one fixed handedness at a time;
3. all-pairs collisions, or a fixed menu of comparisons between independent
   uniform orientations after invertible local transforms;
4. reduced one-sided-ideal sums, intersections, and ranks whose local content
   is only the equality partition in (20);
5. the explicitly audited same-source transform, conjugation, and central
   barred/unbarred cases above.

It does not rule out adaptive or nonuniform samplers, distributions engineered
to satisfy trace or orientation constraints, mixed row/image methods, singular
transforms, arbitrary quaternion polynomial identities, or quaternion
factoring methods not reducible to these collision predicates.  It also says
nothing about the cost of producing exact-uniform samples.  Within the stated
boundary, polynomially many retries in \(\log N\) cannot overcome the balanced
semiprime birthday scale; reaching constant collision probability requires
\(\Omega(N^{1/4})\) samples.

## 11. Verdict

All three core claims are true with the conventions above:

* \(|S_N|=24(p+1)(q+1)\), and every local reduction at \(p,q\) has rank one;
* left-unit orbits are parametrized by local row lines, while right-unit orbits
  are parametrized by local image lines;
* greatest common right divisors are controlled by row equality and greatest
  common left divisors by image equality, with the exact law (13).

The product-zero test and birthday bound follow exactly.  The necessary
qualifications are that row and image orientations of one sample have not been
shown independent, non-unit transforms only preserve the law of the
\(N\)-part of a gcd unless their extra norm factors are mutually coprime, and
same-source or conjugate comparisons obey the separate fixed-point and trace
tests above.
