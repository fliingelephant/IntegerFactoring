# F31 fresh hostile re-audit: low-degree joint amortization

**Artifacts audited:**

- `experiments/F31_low_degree_joint_amortization_kill/RESULT.md`
- `experiments/F31_low_degree_joint_amortization_audit/RESULT.md`

**Protocol:** fresh proof-only hostile re-audit of the corrected candidate,
including all six repairs required by the first audit.  No computation was
used.  The candidate and canonical files were not edited.

## Verdict

**PASS WITH REQUIRED CORRECTIONS.**

The deterministic Schwartz--Zippel theorem, its product version, the exact
formal-identity classification, the fresh-batch adaptive extension, all five
examples, and the balanced-semiprime threshold survive re-audit.  Five of the
six requested repairs are complete, and the substantive parts of the circuit
repair are complete.  One narrow but repeated scope wording remains: the
candidate twice says that characteristic-scale or high-degree polynomial
computations are not “covered.”  A fixed polynomial computed by such a circuit
is still covered structurally by the theorem at its actual formal degree.  What
fails is the *sparse obstruction* when that degree makes \(D/r\) vacuous; in the
succinct-circuit identity branch, efficient coefficient-content extraction is
also not supplied.

This is not a gap in (0.1), and no new theorem-level correction is required.
The two scope summaries must nevertheless be made exact before a strict blind
reconstruction, because they presently conflict with the candidate's own
correct formal-polynomial/function distinction.

## 1. Core theorem rechecked

Let

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k),
\qquad N=pq,
\]

where \(p\ne q\) are prime.  CRT identifies this probability space with the
product of independent uniform spaces

\[
\mathbb F_p^k\times\mathbb F_q^k.
\]

For fixed \(F_j\in\mathbb Z[X_1,\ldots,X_k]\), let
\(f_{j,r}=F_j\bmod r\), \(d_j=\deg F_j\), and \(D=\sum_jd_j\).  If every
\(f_{j,r}\) is a nonzero formal polynomial, Schwartz--Zippel gives

\[
\Pr[f_{j,r}(X_r)=0]\le d_j/r
\]

without requiring \(d_j<r\).  Shared variables and joint dependence on every
batch coordinate do not affect this estimate.  Since a product over a field
vanishes at a point exactly when at least one factor vanishes there,

\[
\Pr\!\left[\prod_j f_{j,r}(X_r)=0\right]\le D/r.
\]

A proper gcd requires one of the two local product-zero events, so

\[
\Pr\!\left(
  1<\gcd\!\left(N,\prod_jF_j(X)\right)<N
\right)
\le D\left(\frac1p+\frac1q\right).
\]

For a single output, independence of the two complete local vectors also
justifies the candidate's exact XOR formula

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).
\]

No independence between relations, factors, coordinates, or output
polynomials is used.  The theorem therefore really is a joint-decoder bound,
not an argument assuming independent lucky tickets.

## 2. The six required repairs

### 2.1 Randomized-family quantifiers: repaired

The corrected Section 3 now requires the coefficient choice to be independent
of the sampled batch and to have nonzero formal reductions over both fields
almost surely.  It distinguishes a uniform degree cap \(D_*\) from a random
integrable degree budget, for which conditioning gives

\[
\Pr(\text{proper gcd})
\le \mathbb E[D]\left(\frac1p+\frac1q\right).
\]

It also sends every supported mixed formal identity to the coefficient-content
branch instead of silently averaging it into the sparse theorem.  These are
the necessary quantifiers.  Allowing a null set of bad coefficient choices is
harmless; a positive-mass bad choice is not.

### 2.2 Formal zero versus zero function: substantive repair complete,
summary wording incomplete

Sections 2 and 5 correctly distinguish:

- the zero *formal polynomial*, whose coefficients all vanish locally and
  which belongs to the content analysis; and
- a nonzero formal polynomial such as \(T^r-T\) that induces the zero function
  on \(\mathbb F_r\).

Schwartz--Zippel still applies to the second object.  At degree \(r\), its
bound is \(r/r=1\), so the result is true and vacuous rather than inapplicable.
No hypothesis \(d<r\) is hidden in the proof.

The remaining defect is in Section 7.  Its lead says “It also does not cover”
and the ensuing list includes “characteristic-scale nonzero polynomial
functions whose Schwartz--Zippel bound is vacuous.”  That item is structurally
covered by (0.1).  The list should instead say that the sparse obstruction does
not rule out such polynomials, and it should use “nonzero formal polynomials”
rather than the now-dangerous shorthand “nonzero polynomial functions.”

### 2.3 Full joint affine uniformity: repaired

The Outcome, Sections 1--3, the examples, the threshold, and the final boxed
scope all retain the full hypothesis

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k).
\]

The candidate now expressly excludes projective, conditioned, biased, and
correlated sources.  It also includes the decisive counterexample
\(X_1=X_2=U\): both marginals are uniform, but \(X_1-X_2\) vanishes surely.
Thus neither coordinatewise uniformity nor local uniformity on a proper
relation space is being substituted for joint uniformity on the full affine
space.

### 2.4 Product identity cases: repaired

With

\[
Z_r=\{j:f_{j,r}\text{ is the zero formal polynomial}\},
\]

the corrected Section 4 gives the exact exhaustive split:

1. \(Z_p=Z_q=\varnothing\): the product is formally nonzero over both fields,
   so the probability theorem applies.
2. Exactly one of \(Z_p,Z_q\) is nonempty: an individual factor is zero
   formally over one field and nonzero over the other, so its explicit content
   exposes the corresponding prime.
3. Both are nonempty: the product is formally zero over both fields.  This can
   be caused by one synchronized factor or, when the sets have no common
   member, by different one-sided-zero factors.  In the latter case the product
   gcd is \(N\), while the individual explicit contents still expose the
   primes.

The cases may coexist syntactically when a synchronized factor and additional
one-sided factors are both present; this does not alter the classification or
its conclusions.  The zero integer polynomial is separately excluded from the
content convention.

### 2.5 Fresh-batch versus same-sample adaptation: repaired

The adaptive extension is now restricted to a genuinely fresh jointly uniform
affine CRT batch at every round.  Conditional on every reachable past, the
specialized polynomial in the new variables must remain formally nonzero over
both fields.  Conditional Schwartz--Zippel and the tower property then charge
the uniform or expected sum of the conditional degree budgets; an adaptive
stopping rule does not invalidate this calculation when the charged rounds are
included in that sum.

The report also gives the correct same-sample counterexample.  After observing
\(X=a\), choosing \(F_a(T)=T-a\) and evaluating it at \(T=X\) produces certain
vanishing despite degree one.  A branch-free global symbolic computation can
instead be analyzed as its actual fixed global polynomial.  The candidate no
longer makes an invalid conditioning claim for same-sample selection.

### 2.6 Circuit scope and content extraction: substantive repair complete,
summary wording incomplete

Section 4 correctly restricts its circuit language to branch-free,
division-free arithmetic circuits and to their actual formal degrees.  It
states both essential limitations:

- polynomial circuit size does not imply polynomial formal degree; repeated
  squaring can produce exponential degree; and
- the structural coefficient-content dichotomy for the expanded polynomial
  does not give a polynomial-time content extractor from a succinct circuit.

The Classification and Section 6 likewise correctly say that F31 is not a
circuit lower bound.

Two summary phrases should be aligned with those correct statements.  The
Classification says the result “does not cover ... exponentially pooled
products,” and Section 7 lists “high-degree circuits and implicit exponential
products” under “does not cover.”  A fixed branch-free division-free circuit
still computes a polynomial to which the structural theorem applies.  The
proper statement is that F31 supplies no useful *low-degree sparse
obstruction* once the actual degree is characteristic-scale or exponential,
and supplies no automatic succinct content extraction in the formal-identity
branch.

## 3. Coefficient-content branch

For a nonzero collected integer polynomial \(F=\sum_\nu a_\nu X^\nu\), let

\[
c(F)=\gcd_\nu a_\nu.
\]

Then \(F\bmod r\) is the zero formal polynomial exactly when \(r\mid c(F)\).
Consequently

\[
F\bmod p=0,
\qquad F\bmod q\ne0
\quad\Longrightarrow\quad
\gcd(N,c(F))=p,
\]

and symmetrically for \(q\).  For a canonical collected sparse or dense list
of polynomially many polynomial-bit coefficients, this content and terminal
integer gcd are computable in polynomial bit complexity.  The candidate
correctly withholds that algorithmic conclusion for succinct circuits with
potentially exponentially many expanded monomials and cancellations.

No hidden appeal to polynomial identity testing or to factoring occurs in the
explicit-list argument.

## 4. Examples and asymptotic threshold

The examples remain correct under their now-explicit hypotheses.

- A locally nonconstant affine form on the full affine space has exactly
  \(r^{k-1}\) roots.
- A product charges the sum of the formal degrees even when all factors share
  variables.
- A \(t\times t\) determinant of affine-linear entries has degree at most
  \(t\), and the corresponding Gram determinant has degree at most \(2t\).
- A scalar entry of a product of \(K\) matrices with affine-linear entries is
  an ordinary commutative polynomial of degree at most \(K\); matrix-order
  noncommutativity does not change that fact.
- A simultaneous rank-drop event is contained in the zero set of any one
  locally nonzero defining minor.  The selected minor may differ between the
  two characteristics; absence of every nonzero minor in one characteristic
  while one survives in the other gives a mixed content separator.

For \(p\le q\le\kappa p\), both primes are
\(\Theta_\kappa(\sqrt N)\), hence

\[
\Pr(\text{proper gcd})=O_\kappa(D/\sqrt N).
\]

If \(n=\lceil\log_2(N+1)\rceil\) and \(D\le n^A\), this is

\[
2^{-n/2+O_\kappa(\log n)}.
\]

Conversely, a success probability at least \(n^{-B}\) under the theorem's
nonidentity hypotheses requires

\[
D=\Omega_\kappa(\sqrt N/n^B).
\]

This is a necessary degree scale only.  It neither constructs a successful
high-degree decoder nor rules one out.

## 5. Required final edits

Before blind reconstruction, make only the following scope repair.

1. In the Classification, replace “does not cover ... exponentially pooled
   products” by language saying that the low-degree sparse obstruction does
   not rule them out.
2. In Section 7, keep genuinely out-of-model mechanisms in the “does not
   cover” list, but move characteristic-scale nonzero formal polynomials and
   high-degree branch-free division-free circuits to a separate sentence:
   (0.1) still applies at their actual formal degree, may be vacuous, and does
   not provide succinct coefficient-content extraction.

After those edits, this re-audit finds no remaining objection to a strict
proof-blind reconstruction.  No canonical promotion is warranted before that
reconstruction.
