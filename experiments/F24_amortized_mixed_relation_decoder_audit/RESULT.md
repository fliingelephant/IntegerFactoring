# Focused hostile audit of F24 — amortized mixed-relation decoder

**Audit verdict:** the candidate does **not** survive in its present form.  Its
balanced-semiprime probability lemma is sound (with slightly sharper
conditioning language), and its conditional reduction from an exact evaluator
to a promise Las Vegas factorer is sound.  The advertised evaluator obstruction
is not.  In particular, a balanced meet-in-the-middle split gives an exact
resultant/multipoint evaluator in

\[
  \widetilde O(2^{K/2})=N^{1/4+o(1)}
\]

modular work, rather than the candidate's \(2^K=N^{1/2+o(1)}\) Gray-code
evaluation.  This is still exponential in the input length, but it refutes the
wording that the displayed tensor/recursion/resultant is the strongest exact
compression and shows directly why formal degree and the \(2^K\)-dimensional
diagonal realization are not evaluator lower bounds.

No argument in the candidate excludes a polynomial-size arithmetic circuit, a
faster norm identity, or a characteristic-sensitive modular algorithm for
\(Q_K\).  The rigorous terminal gap is only that no such polynomial-time
evaluator has been supplied.  Therefore the exact version audited here must be
corrected before proof-blind reconstruction; reconstruction of the unchanged
candidate is **not warranted**.

## 1. Mixed traces and random weighting

### 1.1 The mixed-trace bound is valid under the right conditioning

For a fresh pair of independent P30 outputs, reduction at
\(r\in\{p,q\}\) gives nonzero rank-one matrices

\[
  B=uv^{\mathsf T},\qquad C=xy^{\mathsf T}.
\]

The identity

\[
  \operatorname{tr}(BC)
   =(v^{\mathsf T}x)(y^{\mathsf T}u)
\]

is exact.  Conditional on the accepted residual and completion randomness for
the two independent calls, P30 makes each row marginal and each image marginal
uniform on

\[
  \mathcal S_r,qquad s_r=|\mathcal S_r|
  =r-\left(\frac{-1}{r}\right).
\]

For fixed \(x\in\mathcal S_r\), its orthogonal projective line is also in
\(\mathcal S_r\), so independence of the two calls in fact gives

\[
  \Pr(v^{\mathsf T}x=0)=\frac1{s_r},
  \qquad
  \Pr(y^{\mathsf T}u=0)=\frac1{s_r}.
\]

The two events need not be independent because the row and image of one output
need not be independent.  The conclusion available from the P30 marginals is
the union bound

\[
  \Pr(r\mid\operatorname{trd}(\beta\gamma))
  \le \frac2{s_r}.
\]

Thus (2.1) is a valid conditional upper bound, not an exact law for the
divisibility event.  It remains valid after averaging over the residuals and
completion randomness and for every fresh pair conditional on all earlier
calls.  It would not remain a uniformity statement after conditioning on the
entire current call transcript, since that transcript fixes the output.

For \(N=pq\), nonunit retention therefore has probability at most

\[
  \eta=\frac2{s_p}+\frac2{s_q}.
\]

When \(p,q\ge53\), \(s_p,s_q\ge52\), hence
\(\eta\le1/13\).  Ignoring the earlier termination caused by a proper gcd, the
expected number of pair attempts needed for \(K\) retained units is at most

\[
  \frac{K}{1-\eta}\le\frac{13K}{12}.
\]

A gcd equal to \(N\) may be discarded; a proper gcd terminates with a valid
factor.  This repairs the quantifier around “attempts per retained unit” and
confirms that the optional mixed-trace prefix is expected polynomial time.

### 1.2 Random weighting erases all Hurwitz information

Let \(c_1,\ldots,c_K\) be any adaptively obtained residues that are units modulo
\(N\).  Conditional on their values and on every preceding transcript, fresh
independent uniform
\(\lambda_i\in\mathbb Z/N\mathbb Z\) give

\[
  a_i=\lambda_i c_i\pmod N
\]

as independent uniform residues modulo \(N\).  This is just invariance of the
uniform measure under multiplication by a unit.  CRT then makes the two entire
vectors

\[
  (a_1\bmod p,\ldots,a_K\bmod p),
  \qquad
  (a_1\bmod q,\ldots,a_K\bmod q)
\]

independent and individually uniform.

This part of the candidate is correct, but it removes rather than uses the
Hurwitz structure.  The same distribution is obtained by drawing each \(a_i\)
uniformly modulo \(N\) directly.  Unit retention, the mixed traces, P30, and P31
are dispensable for the terminal decoder and its factoring reduction.  P30 is
needed only to certify the optional way of manufacturing units; P31's
wrong-hand and CRT-line results are not needed at all after direct random
sampling.

## 2. Threshold constants and local probability

Assume exactly the candidate's promise

\[
  N=pq,\qquad 53\le p<q<2p,
\]

with \(p,q\) distinct odd primes.  Put

\[
  h=\lfloor\sqrt N\rfloor,
  \quad b=\lfloor\log_2h\rfloor,
  \quad K=b-3,
  \quad T=2^K,
  \quad m=T-1.
\]

Here \(K\ge2\).  From \(2^b\le h<2^{b+1}\), exactly

\[
  \frac h{16}<T\le\frac h8.                         \tag{2.1}
\]

Since \(h>\sqrt N-1\),

\[
  m>\frac{\sqrt N}{16}-\frac{17}{16}
   =\frac{\sqrt N-17}{16}.                          \tag{2.2}
\]

Also

\[
  p<\sqrt N<q,qquad
  p>\frac{\sqrt N}{\sqrt2},qquad
  q<\sqrt{2N}.                                      \tag{2.3}
\]

For \(\mu_r=m/r\), (2.1)--(2.3) imply the candidate's loose but valid constants

\[
  a:=\frac1{32\sqrt2}<\mu_p,\mu_q
  <U:=\frac{\sqrt2}{8}.                             \tag{2.4}
\]

For the lower bound, \(r\le q<\sqrt{2N}\) and (2.2) give

\[
  \mu_r>
  \frac{\sqrt N-17}{16\sqrt{2N}}
  =\frac{1-17/\sqrt N}{16\sqrt2}
  >\frac1{32\sqrt2},
\]

because \(\sqrt N>53>34\).  For the upper bound,

\[
  \mu_p<\frac{\sqrt N}{8p}
        =\frac1{8}\sqrt{\frac qp}<\frac{\sqrt2}{8},
  \qquad
  \mu_q<\frac{\sqrt N}{8q}<\frac18.
\]

Thus there is no error in \(K\), the floor losses, or the displayed \(a,U\)
constants.

For a fixed prime \(r\in\{p,q\}\), let

\[
  L_S=\sum_{i\in S}a_i,
  \qquad
  Z_r=\#\{\varnothing\ne S\subseteq[K]:L_S=0\pmod r\}.
\]

Every \(L_S\) is uniform.  For distinct nonempty \(S,T\), their two incidence
vectors are linearly independent: two nonzero \(0/1\) vectors that are scalar
multiples have the same support, and an occupied coordinate then forces the
scalar to be \(1\), hence the vectors to be equal.  This argument works in every
characteristic, in particular in every odd characteristic used here.  The
linear map to \((L_S,L_T)\) has rank two, so the two sums, and hence their zero
indicators, are independent.

Consequently

\[
  \mathbb EZ_r=\mu_r,
  \qquad
  \operatorname{Var}(Z_r)=\mu_r\left(1-\frac1r\right),
\]

and, for \(E_r=\{Z_r>0\}\),

\[
  \frac{\mu_r}{\mu_r+1-1/r}
  \le \Pr(E_r)\le\mu_r.                             \tag{2.5}
\]

The lower bound is the exact second-moment/Paley--Zygmund value; the upper
bound is the union bound and is below one by (2.4).  In particular

\[
  \frac1{32\sqrt2+1}<\Pr(E_r)<\frac{\sqrt2}{8}.
\]

The events \(E_p,E_q\) are independent because they are functions of the two
independent CRT vectors, not merely because individual subset sums are
pairwise independent.  Therefore

\[
\begin{aligned}
 \Pr(E_p\mathbin\triangle E_q)
 &=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)\\
 &\ge
 \delta:=\frac{2}{32\sqrt2+1}
       \left(1-\frac{\sqrt2}{8}\right)>0.           \tag{2.6}
\end{aligned}
\]

The candidate's second-moment and XOR calculations are therefore sound.  The
constants are deliberately non-tight but fixed independently of \(N,p,q\).

## 3. Exact local OR and the promise reduction

Define

\[
  Q_K(a_1,\ldots,a_K)
   =\prod_{\varnothing\ne S\subseteq[K]}L_S\pmod N.
\]

For each \(r=p,q\), the field property gives exactly

\[
  Q_K\equiv0\pmod r\quad\Longleftrightarrow\quad E_r. \tag{3.1}
\]

Since \(N=pq\) is squarefree with two prime factors,

\[
  1<\gcd(Q_K,N)<N
  \quad\Longleftrightarrow\quad
  E_p\mathbin\triangle E_q.                         \tag{3.2}
\]

Thus, if a **uniform exact** evaluator computed \(Q_K\bmod N\) in
\(\operatorname{poly}(\log N,K)\) bit operations, direct independent sampling
of the \(a_i\)'s followed by (3.2) would be a Las Vegas factorer on the displayed
balanced-semiprime promise.  Every returned gcd is verified; (2.6) makes the
number of trials geometrically dominated with mean at most \(1/\delta\), and
the probability of never terminating is zero.

This is the strongest valid algorithmic consequence.  It is **not** an
all-input factoring reduction.  Nothing here gives a success bound for
unbalanced semiprimes, prime powers, repeated factors, even composites, or
integers with three or more prime factors.  “Factoring-grade” can legitimately
mean only “sufficient to factor the stated balanced distinct-semiprime
promise”; it must not be read as equivalence to the all-input statement in
`PROMPT.md`.

## 4. The claimed evaluator obstruction fails as stated

### 4.1 What the literal constructions do prove

The following representation-specific facts in the candidate are correct.

* The displayed diagonal Kronecker operator has dimension \(T=2^K\), its
  determinant is \(Q_K\), and explicitly traversing its diagonal takes \(T-1\)
  factors.
* The dense polynomial \(F_K(x)\) has degree \(T\), and the literal unshared
  recursion
  \(F_k(x)=F_{k-1}(x)F_{k-1}(x+a_k)\) has \(T\) leaves if it is expanded in that
  manner.
* The full Boolean quotient algebra
  \(\mathbb Z[a,e]/(e_i^2-e_i)\) has rank \(T\); its direct multiplication matrix
  and the corresponding full Boolean norm/resultant materialization have
  exponential rank.
* Gray-code enumeration evaluates \(Q_K\) with \(T-1\) modular products and
  polynomial working space.
* A literal reachable-residue table has many entries on the random inputs used
  by the reduction.  If \(D_r\) is the number of distinct local subset sums and
  \(C_r\) the number of colliding unordered pairs, then
  \(D_r\ge T-C_r\) and

  \[
    \mathbb ED_r\ge T-\binom T2/r
      =T\left(1-\frac{T-1}{2r}\right).
  \]

  Since \(T/r<U\), this is a fixed positive fraction of \(T\).

These facts rule out only those literal materializations.  The last estimate is
an expectation for an explicit support table, not a lower bound on compressed
state, circuit size, or even typical storage without an additional
concentration argument.

### 4.2 An exact meet-in-the-middle norm cuts the work to \(2^{K/2}\)

Partition \([K]=A\mathbin{\dot\cup}B\), with
\(|A|=\lfloor K/2\rfloor\) and
\(|B|=\lceil K/2\rceil\).  Put

\[
  x_U=\sum_{i\in U}a_i
  \quad(\varnothing\ne U\subseteq A),
  \qquad
  y_V=\sum_{i\in V}a_i
  \quad(\varnothing\ne V\subseteq B),
\]

and define, over \(\mathbb Z/N\mathbb Z\),

\[
  P_A(X)=\prod_{\varnothing\ne U\subseteq A}(X+x_U),
  \qquad
  R_B(X)=\prod_{\varnothing\ne V\subseteq B}(X-y_V).
\]

With the convention
\(\operatorname{Res}(f,g)=\prod_{f(\rho)=0}g(\rho)\) for monic \(f\), one has the
polynomial identity

\[
\begin{aligned}
 Q_K
 &=\left(\prod_{U\ne\varnothing}x_U\right)
   \left(\prod_{V\ne\varnothing}y_V\right)
   \prod_{\substack{U\ne\varnothing\\V\ne\varnothing}}(x_U+y_V)\\
 &=(-1)^{m_B}P_A(0)R_B(0)
   \operatorname{Res}(R_B,P_A),                    \tag{4.1}
\end{aligned}
\]

where \(m_B=2^{|B|}-1\).  Equivalently, avoiding every sign convention,

\[
  Q_K=P_A(0)
      \left(\prod_{V\ne\varnothing}y_V\right)
      \left(\prod_{V\ne\varnothing}P_A(y_V)\right). \tag{4.2}
\]

This identity remains exact over the composite coefficient ring; it does not
use CRT factors or divide by a possibly nonunit residue.

Let \(s=2^{\lceil K/2\rceil}\).  Enumerate the two half-sum lists in \(O(s)\)
additions, build \(P_A\) with a product tree, and evaluate it at all \(y_V\)
with the usual monic product/remainder tree.  Polynomial remainders require
division only by monic polynomials; repeated evaluation points cause no
problem.  Standard fast polynomial arithmetic over
\(\mathbb Z/N\mathbb Z\) (or a uniform Kronecker-substitution implementation)
therefore evaluates (4.2) in

\[
  \widetilde O(s)\text{ modular coefficient operations}
  \quad\text{and}\quad
  \widetilde O(s\,\operatorname{poly}(n,K))\text{ bit operations}, \tag{4.3}
\]

with \(\widetilde O(sn)\) stored coefficient bits.  Since
\(2^K=\Theta(\sqrt N)\), this is \(N^{1/4+o(1)}\) time and space.

The Sylvester matrix for the resultant in (4.1) has dimension
\(O(2^{K/2})\), not \(2^K\).  More importantly, its root structure permits the
faster product/multipoint computation above.  This is an explicit fast norm
identity omitted by the candidate.  It remains exponential in \(n\) and hence
does not solve the evaluator problem, but it invalidates the candidate's
“strongest exact compression” and any suggestion that \(2^K\) operations are
intrinsic.

### 4.3 Minimal polynomial and hyperplane divisibility are too narrow

Over \(\mathbb Q(a_1,\ldots,a_K)\), the formal subset sums are distinct, so the
unmodified diagonal subset-sum operator does have minimal polynomial

\[
  \prod_{S\subseteq[K]}(X-L_S)
\]

of degree \(2^K\).  A \(d\)-dimensional linear operator that is required to
retain that entire spectrum must have \(d\ge2^K\).  Computing the one symmetric
scalar \(\prod_{S\ne\varnothing}L_S\), however, does not require retaining the
operator or its spectrum.  Formula (4.2) is already a counterexample to that
inference.  At a finite-field specialization, subset sums may also collide and
the specialized minimal polynomial can have smaller degree; the candidate's
expected-distinct-support estimate does not convert the formal minimal
polynomial into a circuit lower bound.

The hyperplane lemma is correct only with its characteristic-zero polynomial
quantifier made explicit.  If
\(A\in\mathbb Q[a_1,\ldots,a_K]\) vanishes identically on every hyperplane
\(L_S=0\), then \(L_S\mid A\) for each \(S\).  The \(L_S\)'s are distinct
nonassociate irreducibles, so

\[
  Q_K\mid A,
  \qquad
  \deg A\ge2^K-1.                                  \tag{4.4}
\]

Hence a determinant of a \(d\times d\) matrix whose entries have formal degree
at most \(e\) must satisfy \(de\ge2^K-1\), if its determinant has that
characteristic-zero vanishing property.  This says nothing about the circuit
size of high-degree entries, modular functions that depend on the
characteristic or modulus, branching algorithms, or other exact evaluators.
A short straight-line program can have exponential formal degree by repeated
squaring.

The symmetry of \(Q_K\) makes the logical gap concrete.  For \(K=3\), with
\(e_1,e_2,e_3\) the elementary symmetric polynomials,

\[
  Q_3=e_1e_3(e_1e_2-e_3).
\]

Thus seven displayed linear factors and an eight-state diagonal operator
collapse to a small symmetric formula.  No analogous polynomial-size formula
for arbitrary \(K\) is supplied here, but neither the degree, the formal roots,
nor (4.4) proves that one is absent.  Finite-field identities could in principle
give further specializations; finite-field collisions do not invalidate the
formal statements, but they make the attempted passage from those statements
to modular evaluation hardness still less justified.

Accordingly, the candidate may say only:

1. the named full diagonal, dense recursion, full Boolean resultant, raw
   support table, and Gray-code implementations are exponential;
2. the meet-in-the-middle evaluator (4.2) is a better explicit exponential
   upper bound; and
3. no polynomial-time exact evaluator is currently supplied.

It may not call this an “exponential evaluation-rank obstruction” without
qualifying that the rank belongs to a chosen linearization, and it may not call
any displayed representation the strongest possible exact compression.

### 4.4 Hypercube and factorial interpretations do not close the evaluator gap

There is another exact interpretation.  Give every edge in direction \(i\) of
the \(K\)-dimensional hypercube weight \(a_i\), and let \(\tau_K(a)\) be its
weighted spanning-tree polynomial.  The weighted Laplacian is a Kronecker sum
whose eigenvalues are

\[
  2L_S=2\sum_{i\in S}a_i
  \qquad(S\subseteq[K]).
\]

The matrix-tree theorem therefore gives, with \(T=2^K\),

\[
  \tau_K(a)
   =\frac1T\prod_{S\ne\varnothing}2L_S
   =2^{T-K-1}Q_K.                                  \tag{4.5}
\]

Equivalently, over the odd moduli considered here,

\[
  Q_K=2^{K+1-T}\tau_K(a),
\]

where the negative exponent denotes multiplication by the corresponding unit
power of \(2^{-1}\bmod N\).  The cofactor determinant has dimension \(T-1\), and
Kronecker-sum diagonalization reproduces the same subset-product formula.  This
is a useful succinct interpretation, not a smaller general evaluator and not a
lower bound: no polynomial-\(K\) arbitrary-weight spanning-tree formula is
proved absent.

A structured specialization makes the warning even clearer.  If

\[
  a_i=u2^{i-1}\qquad(1\le i\le K),
\]

then the nonempty integer subset sums are exactly \(u,2u,\ldots,(T-1)u\), so

\[
  Q_K=u^{T-1}(T-1)!\pmod N.                         \tag{4.6}
\]

Thus the Boolean norm contains an ordinary batch-factorial specialization.
This does not preserve the independent-random-weight probability theorem, but
it reinforces the connection to F02/P21 and shows again that the number of
formal linear factors is not an evaluation lower bound.  Neither (4.5) nor
(4.6) supplies a polynomial-\(K\) evaluator for arbitrary weights.

## 5. Complexity ledger after correction

For the optional Hurwitz prefix, P30 supplies expected polynomial bit and
random-bit complexity per primitive output.  Two fresh outputs per pair,
\(K=O(n)\), and the retention bound in Section 1 keep the whole prefix expected
polynomial.  Quaternion coordinates and
\(\operatorname{trd}(\beta\gamma)\) have \(O(n)\) bits; indeed

\[
  |\operatorname{trd}(\beta\gamma)|\le2N.
\]

But the prefix should simply be deleted from the clean theorem.

For direct sampling, rejection from \(n\)-bit strings accepts with probability
at least \(1/2\), so one exact uniform residue modulo \(N\) uses \(O(n)\)
expected random bits.  A weighting trial uses \(K=O(n)\) residues and therefore
\(O(n^2)\) expected random bits.  With the constant expected trial count from
(2.6), this remains \(O(n^2)\) up to a fixed factor.  Modular additions,
multiplications, and the final gcd use \(O(n)\)-bit residues (ordinary products
before reduction have \(O(n)\) bits with a larger constant).

There are now two honest explicit time/space tradeoffs.

* Gray-code evaluation performs \(2^K-1=N^{1/2+o(1)}\) modular products and
  additions and uses \(O(n+K)\) extra working bits.
* Meet-in-the-middle evaluation performs
  \(N^{1/4+o(1)}\) bit work and uses \(N^{1/4+o(1)}\) space.  Coefficients can be
  reduced modulo \(N\) throughout, but the coefficient arrays and packed
  polynomial-multiplication operands have exponential total bit length.

Forming the full integer product before reduction can have
\(O(2^K n)\) bits, as the candidate says, but neither explicit evaluator needs
to do that.  Both evaluators are still exponential in \(n\); no arithmetic
operation count has become a polynomial bit-complexity result.

## 6. Corrected strongest theorem

The following is the strongest theorem justified by the surviving argument.

> **Corrected F24 theorem (balanced-promise Boolean subset norm).**  Let
> \(N=pq\) with distinct odd primes \(53\le p<q<2p\), and set
> \(K=\lfloor\log_2\lfloor\sqrt N\rfloor\rfloor-3\).  If
> \(a_1,\ldots,a_K\) are independent uniform residues modulo \(N\), then the
> Boolean subset norm
>
> \[
> Q_K=\prod_{\varnothing\ne S\subseteq[K]}\sum_{i\in S}a_i\pmod N
> \]
>
> has
>
> \[
> \Pr(1<\gcd(Q_K,N)<N)\ge
> \frac{2}{32\sqrt2+1}\left(1-\frac{\sqrt2}{8}\right).
> \]
>
> Therefore a uniform exact
> \(\operatorname{poly}(\log N,K)\)-bit evaluator for \(Q_K\bmod N\) would give
> a classical Las Vegas polynomial-time factorer for this balanced
> distinct-semiprime promise.  Independently of any Hurwitz construction,
> \(Q_K\) can currently be evaluated by the explicit meet-in-the-middle
> product/multipoint algorithm in \(N^{1/4+o(1)}\) bit time and space, or by
> Gray-code enumeration in \(N^{1/2+o(1)}\) time and polynomial space.  The
> literal full diagonal and Boolean-resultant realizations have rank \(2^K\),
> and the characteristic-zero union polynomial has degree \(2^K-1\), but these
> facts do not lower-bound general arithmetic-circuit or modular evaluation
> complexity.

The optional trace construction adds only the ancillary fact that independent
P30 outputs produce a unit \(c\) with probability at least
\(1-2/s_p-2/s_q\), after which a uniform multiplier recreates exactly the direct
uniform distribution.  It strengthens neither the decoder nor its scope.

## 7. Classification and reconstruction verdict

Once the uniform weights are introduced, F24 is no longer essentially an F14
Hurwitz route.  X24/P30 is the closest source-law result for the optional prefix,
but it is not the closest terminal mechanism.  The terminal gap is closer to
F02/P20--P21: an exponentially long structured modular product has the desired
local zero predicate, literal materializations are expensive, and a uniform
polylogarithmic evaluator remains unproved.  P21 is also the relevant warning
that factor count, formal degree, and a literal two-child recurrence are not
arithmetic-circuit lower bounds.  The factorial specialization (4.6) and
ordinary batch-product methods give the same warning, while the hypercube norm
(4.5) and meet-in-the-middle formula (4.2) are the corresponding exact
compressions here.  The family should therefore be reclassified as a generic
structured-product/evaluator route, with the Hurwitz construction noted only as
dispensable provenance.

The positive probability theorem is a genuine balanced-semiprime promise
lemma, not a factoring algorithm under `PROMPT.md`.  The explicit algorithms
remain exponential, and no result covers arbitrary inputs or recursive complete
factorization.

**Proof-blind reconstruction verdict:** **no for this version.**  The audit has
introduced a mathematically stronger evaluator and has retracted the candidate's
central “strongest compression/exponential evaluation rank” wording.  Under the
verification cadence, this is a substantive mathematical correction, not a
prose-only edit.  A revised candidate should first incorporate (4.1)--(4.3),
limit every lower-bound statement to its named representation, delete the
Hurwitz dependency from the main theorem, and state only the balanced promise.
Only that corrected version would be appropriate for a fresh proof-blind
reconstruction.
