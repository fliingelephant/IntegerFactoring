# F31 second fresh hostile re-audit: low-degree joint amortization

**Artifacts audited:**

- `experiments/F31_low_degree_joint_amortization_kill/RESULT.md`
- `experiments/F31_low_degree_joint_amortization_audit/RESULT.md`
- `experiments/F31_low_degree_joint_amortization_reaudit/RESULT.md`

**Protocol:** fresh proof-only audit of the twice-corrected candidate.  The
two scope edits required by the first re-audit were checked explicitly, and
the whole candidate was then reread for collateral wording or logical damage.
No computation was used.  The candidate and canonical files were not edited.

## Verdict

**CLEAN PASS.**

The two remaining scope defects are repaired exactly.  The candidate now says
that characteristic-scale nonzero formal polynomials, exponentially pooled
products, and high-degree branch-free division-free circuits remain
structurally subject to (0.1) at their actual formal degree.  It separately
says that the resulting bound may be vacuous and that the formal-identity
branch supplies no automatic polynomial-time coefficient-content extractor
from a succinct circuit.

The edits introduce no collateral overclaim.  The deterministic theorem,
randomized and fresh-batch quantifiers, formal-identity split, examples, and
balanced threshold remain correct.  This audit finds no correction remaining
before strict proof-blind reconstruction.

## 1. Exact scope edits

### 1.1 Classification

The Classification now makes three separate claims:

1. F31 concerns a fully jointly uniform affine CRT batch and a
   low-formal-degree polynomial decoder.
2. It is not a lower bound for polynomial-size arithmetic circuits, because a
   branch-free division-free circuit may have exponential formal degree.
3. Exponentially pooled products and characteristic-scale formal polynomials
   are not outside the structural theorem: (0.1) applies at their actual
   degree, but can be vacuous and does not create a succinct content extractor.

Those claims are mutually consistent.  The genuinely excluded source and
decoder types—nonuniform, projective, conditioned, correlated, metric,
order-based, and matching/Markov-chain mechanisms—remain listed separately.

### 1.2 Final scope section

Section 7 now reserves “does not cover” for mechanisms that are not fixed
polynomial-zero computations on the full affine source:

- metric or order branches;
- division or inversion paths requiring separate nonunit analysis;
- exponentially large same-sample adaptive branch families; and
- rational functions without denominator-zero control.

It then states separately:

> Characteristic-scale nonzero formal polynomials and high-degree branch-free
> division-free circuits are structurally covered at their actual formal
> degree.

The following sentence supplies both necessary limitations: (0.1) may be
vacuous, and a succinct-circuit formal identity does not yield an automatic
polynomial-time coefficient-content extractor.  This is the precise repair
requested by the prior re-audit.  It neither excludes high degree from the
theorem nor promotes the structural content dichotomy into an algorithm.

## 2. Core deterministic theorem

Let \(N=pq\) with distinct primes and

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k).
\]

CRT identifies this probability space with

\[
\operatorname{Unif}(\mathbb F_p^k)
\times
\operatorname{Unif}(\mathbb F_q^k),
\]

so the two complete local vectors are independent and uniform.  For
\(F_j\in\mathbb Z[X_1,\ldots,X_k]\), put

\[
f_{j,r}=F_j\bmod r,\qquad
d_j=\deg F_j,\qquad
D=\sum_jd_j.
\]

If every \(f_{j,r}\) is a nonzero formal polynomial, formal reduction cannot
increase degree and Schwartz--Zippel gives

\[
\Pr[f_{j,r}(X_r)=0]\le d_j/r.
\]

This remains valid when \(d_j\ge r\); only usefulness, not validity, is lost.
It also requires no independence between coordinates, monomials, output
polynomials, or alleged relations beyond the stated joint uniformity of the
entire affine CRT vector.

For \(P=\prod_jF_j\), the integral-domain property gives

\[
\Pr[P(X_r)=0]
\le
\sum_j\Pr[f_{j,r}(X_r)=0]
\le D/r.
\]

A proper terminal gcd requires at least one of the two local product-zero
events.  Hence

\[
\Pr\!\left(
  1<\gcd\!\left(N,\prod_jF_j(X)\right)<N
\right)
\le
D\left(\frac1p+\frac1q\right).
\]

For one output, independence of the two local vectors also gives the exact
exclusive-or probability

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).
\]

No independence between relations, factors, coordinates, or output
polynomials is used.  The theorem is a genuinely joint-decoder bound.

## 3. Formal identities and polynomial functions

The candidate continues to distinguish the following cases correctly.

- A zero formal polynomial over \(\mathbb F_r\) has every collected integer
  coefficient divisible by \(r\).
- A nonzero formal polynomial can nevertheless induce the zero function on
  \(\mathbb F_r^k\).  The example \(T^r-T\) remains in the
  Schwartz--Zippel branch, with the vacuous bound \(r/r=1\).

For a nonzero collected integer polynomial
\(F=\sum_\nu a_\nu X^\nu\), define

\[
c(F)=\gcd_\nu a_\nu.
\]

Then \(F\bmod r\) is the zero formal polynomial exactly when
\(r\mid c(F)\).  Thus

\[
F\bmod p=0,\qquad F\bmod q\ne0
\quad\Longrightarrow\quad
\gcd(N,c(F))=p,
\]

and symmetrically for \(q\).  For an explicit collected list of polynomially
many polynomial-bit coefficients, this factor is computable in polynomial bit
complexity.

Let

\[
Z_r=\{j:f_{j,r}\text{ is the zero formal polynomial}\}.
\]

The product classification remains exhaustive:

1. \(Z_p=Z_q=\varnothing\): the nonidentity probability theorem applies.
2. Exactly one of \(Z_p,Z_q\) is nonempty: an individual mixed formal identity
   has explicit content exposing a prime.
3. Both are nonempty: the product is formally zero in both fields, either
   through a synchronized factor or through different one-sided-zero factors.
   In the latter case the product gcd is \(N\), while the individual explicit
   contents expose the primes.

The zero integer polynomial is treated separately.  For a succinct circuit,
the structural statements remain true after formal expansion, but neither
polynomial circuit size nor the structural dichotomy supplies an efficient
expanded-content algorithm.  The corrected summaries now preserve this exact
distinction.

## 4. Randomization and adaptation

The randomized-family paragraph retains all necessary quantifiers.  The
coefficient choice is independent of \(X\), and almost every supported choice
must have nonzero formal reductions over both fields.  A uniform degree cap
\(D_*\) gives the deterministic bound with \(D_*\); a random integrable budget
gives

\[
\Pr(\text{proper gcd})
\le
\mathbb E[D]\left(\frac1p+\frac1q\right).
\]

A positive-mass mixed formal identity is routed to the content branch rather
than averaged into this inequality.

The adaptive paragraph remains limited to successive **fresh**, jointly
uniform affine CRT batches.  After conditioning on every reachable history,
the specialized polynomial in the fresh variables must be formally nonzero in
both characteristics.  Conditional Schwartz--Zippel and a union bound then
charge the uniform or expected sum of the conditional degree budgets.

Same-sample selection remains explicitly excluded.  After observing \(X=a\),
the selector \(F_a(T)=T-a\), evaluated at \(T=X\), vanishes certainly despite
degree one.  A branch-free global symbolic computation can instead be treated
as its one fixed global polynomial at its actual degree.  The corrected scope
language does not weaken either side of this distinction.

## 5. Joint-uniformity boundary and examples

Every summary retains full joint affine uniformity, not uniform marginals.
The example \(X_1=X_2=U\) correctly shows why: both coordinates are uniform,
but \(X_1-X_2\) vanishes surely.

The five pooling examples remain within their stated degree budgets.

1. A locally nonconstant affine form on the full affine space has local root
   probability exactly \(1/r\).
2. A product of nonzero scalar tickets has degree equal to the sum of their
   degrees, regardless of shared variables.
3. A \(t\times t\) determinant of affine-linear entries has degree at most
   \(t\), and the corresponding Gram determinant has degree at most \(2t\).
4. A scalar entry of a product of \(K\) matrices with affine-linear entries is
   a commutative polynomial of degree at most \(K\); noncommutativity of matrix
   order does not change that scalar fact.
5. A simultaneous rank-drop event is contained in the zero set of any one
   locally nonzero defining minor.  The chosen minor may differ between the
   two fields, and a minor formally zero in one field but nonzero in the other
   belongs to the content-separator branch.

No example was broadened by the scope corrections.  Projective lines,
conditioned fibres, correlated batches, rational functions, divisions, and
metric decoders still require separate arguments.

## 6. Balanced threshold and high-degree escape

If

\[
p\le q\le\kappa p,
\]

then \(p,q=\Theta_\kappa(\sqrt N)\) and

\[
\Pr(\text{proper terminal gcd})
=O_\kappa(D/\sqrt N).
\]

For \(n=\lceil\log_2(N+1)\rceil\) and \(D\le n^A\), this is

\[
2^{-n/2+O_\kappa(\log n)}.
\]

Conversely, a success probability at least \(n^{-B}\) under the nonidentity
hypotheses requires

\[
D=\Omega_\kappa(\sqrt N/n^B).
\]

This is only a necessary degree scale.  Repeated squaring and succinct
products can attain characteristic-scale or exponential formal degree in a
polynomial-size branch-free division-free circuit.  At that actual degree,
(0.1) remains true but may say only that a probability is at most a number
greater than or equal to one.  Constructing a succinct evaluator with
inverse-polynomial local exclusive-or mass remains an open mechanism, not a
contradiction to F31.

## 7. Reconstruction readiness

All six repairs required by the first audit are now present:

1. randomized-family formal-nonidentity and degree quantifiers;
2. formal zero polynomial versus zero polynomial function;
3. full joint affine uniformity in every summary;
4. exact product formal-identity cases;
5. fresh-batch versus same-sample adaptation; and
6. branch-free division-free circuit scope, actual degree, and no automatic
   succinct content extraction.

The second scope repair is internally consistent with the theorem, examples,
and reopen condition.  This re-audit finds no remaining correction and
therefore clears F31 for a strict proof-blind reconstruction.  It does not by
itself authorize canonical promotion before that reconstruction succeeds.
