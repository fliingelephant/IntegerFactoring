# F39 hostile audit: the Fourier and discrepancy obstruction survives, with scope repairs

**Artifact audited:** `experiments/F39_inverse_metric_cloud_kill/RESULT.md`

**Audit mode:** proof-only.  No computation was performed.

**Verdict:** **PASS AFTER MINOR BUT MANDATORY WORDING AMENDMENTS.**  I did
not find a counterexample to any of the exact Fourier identities, the
factor-free coefficient bound, the discrepancy estimate, or the raw-mean
sample lower bound.  The mathematical core is suitable for proof-blind
reconstruction after the candidate makes the quantifier and scope repairs
listed in section 8 below.  In particular, this audit does **not** upgrade the
result to a factoring lower bound or to a lower bound for arbitrary processing
of a polynomial Fourier list.

## 1. CRT factorization and local table

The additive twists in (3)--(5) are correct.  If

\[
 u=u_pq\bar q_p+u_qp\bar p_q\pmod{pq},
\]

then coordinatewise inversion of a unit gives

\[
 u^{-1}=u_p^{-1}q\bar q_p+u_q^{-1}p\bar p_q\pmod{pq}.
\]

It follows directly that

\[
 e_N(au+bu^{-1})
 =e_p(\bar q_p(au_p+bu_p^{-1}))
  e_q(\bar p_q(au_q+bu_q^{-1})),
\]

and summation factors exactly as asserted in (4).  The same unit twist must
indeed occur on the two local arguments.  Omitting it would preserve the
zero/nonzero classification but not the actual Kloosterman parameter.

The three local cases are exhaustive and correct:

* \(S_r(0,0)=r-1\);
* if exactly one argument is nonzero, permutation of
  \(\mathbb F_r^\times\) gives \(-1\); and
* if both are nonzero, the prime Kloosterman Weil bound is
  \(|S_r(A,B)|\leq2\sqrt r\).

Dividing the nine products by \((p-1)(q-1)\) reproduces every entry of (7).
The four highlighted special cases have the right signs and magnitudes.  In
particular, when \(a=0\) and \(b\) is a unit, the two local \(-1\)'s multiply
to \(+1\), giving exactly \(1/\varphi(N)\).

One phrase in the proof should be cleaned up: CRT *idempotents* are not
themselves invertible.  What is true, and what the displayed calculation
uses, is that inversion of a unit is coordinatewise under the CRT and is
then recombined with the same idempotent basis.  This is expository only; it
does not affect (4).

## 2. Factor-free coefficient bound

For a nonzero residue-pair frequency, let

\[
 d=\gcd(a,b,N).
\]

If \(d=1\), neither prime can divide both coordinates.  Hence neither local
type is \(Z\), and each normalized local factor is at most
\(2\sqrt r/(r-1)\).  Thus

\[
 |\widehat\mu_N(a,b)|
 \leq \frac{4\sqrt{pq}}{(p-1)(q-1)}.
\]

This proves (10).  On a fixed balanced semiprime family it is actually
\(\Theta(N^{-1/2})\) as a numerical upper envelope, so the weaker notation
\(N^{-1/2+o(1)}\) is valid.

The zero-character exception is necessary.  The public-gcd qualification is
also necessary.  Note that \(d=1\) is a sufficient condition for the bound,
not a definition of a fully factor-free frequency: for example, separate
coordinate gcds can expose \(p\) and \(q\) even when the common three-way gcd
is one.  This only strengthens the obstruction, because (10) still applies
to such a cross-degenerate mode.  Whenever the prose uses “factor-free,” it
should mean that **all public gcd screens have no nontrivial proper divisor**.

## 3. The Kloosterman second-moment witness

Equation (12) is exact.  Writing

\[
 K(c)=\sum_{x\ne0}e_q(x+cx^{-1}),
\]

orthogonality in \(c\) gives

\[
 \sum_c|K(c)|^2
 =\sum_{x,y\ne0}e_q(x-y)
   \sum_c e_q(c(x^{-1}-y^{-1}))
 =q(q-1).
\]

Since \(K(0)=-1\), averaging over the \(q-1\) nonzero values of \(c\) gives

\[
 \max_{c\ne0}|K(c)|^2
 \geq \frac{q(q-1)-1}{q-1}
 =q-\frac1{q-1}.
\]

For the frequency \((p,pc)\), the \(p\)-local type is \(Z\), while
\(\bar p_qp=1\pmod q\) makes the \(q\)-local arguments exactly \((1,c)\).
Consequently (14) follows.  This example is existential and factor-aware,
as the candidate says; it does not manufacture a public high-bias frequency.
It does correctly refute an unqualified bound over all nonzero modes.

## 4. Sparse Fourier observables

After duplicate modes are combined and the zero character is removed,
linearity and (10) give

\[
 \left|\mathbb E_{\mu_N}F-\mathbb E_{\lambda_N}F\right|
 \leq \sum_j|c_j|\,\delta_N=A\delta_N.
\]

There is no missing phase or cancellation assumption here; the triangle
inequality is enough.  The \(\ell^1\)-coefficient hypothesis is essential,
and the candidate states it.  Polynomial sparsity alone would not prevent
exponentially large coefficients from rescaling a tiny expectation.

This theorem controls the population expectation of a fixed linear
trigonometric observable, and ordinary empirical estimation of that
expectation.  It does **not** control arbitrary nonlinear processing of the
entire vector

\[
 (e_N(a_ju+b_ju^{-1}))_{j\leq M}.
\]

The candidate's disclaimer says this, but the final shorthand “fails ... for
public polynomial Fourier lists” is broader than the proved proposition and
must be narrowed as specified in section 8.

## 5. Erdős--Turán--Koksma and all hidden modes

The ETK form in (18) is valid for an atomic probability measure.  A
tensor-product Selberg majorant/minorant gives an absolute two-dimensional
constant, truncation error \(O((H+1)^{-1})\), and reciprocal product weights.
Boundary regularity is not required with the stated half-open convention.

The local majorant

\[
 \frac{|S_r(a,b)|}{r-1}
 \leq \alpha_r+\mathbf 1_{r\mid a,\ r\mid b}
\]

is valid in all three local cases.  Multiplying the two local bounds gives

\[
 \alpha_p\alpha_q+\alpha_pI_q+\alpha_qI_p+I_pI_q.
\]

The total reciprocal weight of the square is correctly computed as

\[
 (1+L(H))^2-1.
\]

For the sublattice on which both coordinates are divisible by \(r\), the
one-coordinate reciprocal weight is

\[
 1+\frac2r\sum_{k\leq H/r}\frac1k=1+M_r(H),
\]

so its nonzero two-coordinate weight is exactly
\((1+M_r(H))^2-1\).  Finally, when \(H<N\), the product indicator \(I_pI_q\)
can occur only at \((0,0)\), which ETK excludes.  These observations yield
(24) with the coefficients in the right places.

At \(H=N-1\),

\[
 \left\lfloor\frac{N-1}{p}\right\rfloor=q-1,
 \qquad
 \left\lfloor\frac{N-1}{q}\right\rfloor=p-1.
\]

On \(p\asymp q\asymp\sqrt N\), the four contributions in (24) have orders

\[
 N^{-1},\qquad
 N^{-1/2}\log^2N,\qquad
 N^{-3/4}\log N,\qquad
 N^{-3/4}\log N,
\]

up to absolute/balance constants.  Thus (26) is correct.  In particular,
the factor-aware \(N^{-1/4}\)-scale modes do not create a missing leading
term: they occupy a prime-spaced sublattice, and its reciprocal ETK weight
supplies the necessary suppression.

The rectangle and histogram conversions are also correct:
inclusion--exclusion uses four anchored rectangles, and summing the resulting
coordinate errors gives (28).  The notation \(d_{\rm TV}(\theta,a)\) assumes
the \(B\) bins are a disjoint exhaustive partition, so that both vectors are
probability vectors.  This is standard for “histogram,” but should be stated.
For a mere list of possibly overlapping rectangles, retain the \(\ell^1\)
bound and do not call half of it total variation.

The population discrepancy statement is uniform over rectangles.  It
therefore remains true for every realized rectangle even if a rectangle is
selected after seeing data.  What does not automatically extend to such a
selection is the one-bin empirical MSE argument, because selection can
overfit the same samples.  The candidate's conservative exclusion of
sample-adaptive partitions is therefore harmless, but it should be
understood as an empirical-inference limitation rather than a failure of the
population discrepancy bound.

## 6. Exact empirical MSE and fourth moment

For \(X=e_N(au+bu^{-1})\), \(|X|=1\), so with
\(Y=X-\mu\),

\[
 \mathbb E|Y|^2=1-|\mu|^2.
\]

Independence eliminates cross terms and proves (29) exactly.  Therefore
(30) is a necessary and sufficient condition for the stated relative-RMSE
criterion.  If \(0<|\mu|\leq\delta_N\), substituting the upper bound on
\(|\mu|\) gives the lower bound in (31).  There is no reversal of inequality.

The complex-valued fourth-moment step is also sound.  Expanding
\(|\sum_iY_i|^4\), every nonzero mixed term either has one index occurring
four times or is one of the finitely many two-pair patterns.  Since
\(|Y_i|\leq2\), this gives

\[
 \mathbb E\left|m^{-1}\sum_iY_i\right|^4\leq C m^{-2}
\]

for an absolute \(C\).  When \(|\mu|\leq1/2\),
\(\mathbb E|Y|^2\geq3/4\).  For
\(Z=|\overline X_m-\mu|^2\), Paley--Zygmund at (say) half its mean then gives
absolute \(c_0,c_1>0\) with

\[
 \Pr(Z\geq c_1^2/m)\geq c_0.
\]

Thus (32) is valid for complex \(X\); no unjustified choice of a real
projection is being made.

There is, however, a quantifier that the prose must make explicit.  The
argument proves that if

\[
 m<\frac{c_1^2}{\eta^2|\mu|^2},
\]

then relative error exceeds \(\eta|\mu|\) with probability at least \(c_0\).
It therefore rules out success probability greater than \(1-c_0\) (for
example, any target confidence \(1-c_0/2\)).  It does not, from the displayed
Paley--Zygmund constants alone, prove the same lower bound for **every**
fixed confidence above \(1/2\).  The phrase “fixed-confidence” must either be
defined as confidence at least \(1-c_0/2\), or replaced by “at a sufficiently
high absolute constant confidence.”  No change is needed to the exact RMSE
lower bound.

## 7. Histogram sampling and rejection tickets

For a fixed bin, (33) is the exact Bernoulli variance identity.  If both its
area and complementary area are at least inverse-polynomial in \(\log N\),
then (27) and the exponentially smaller discrepancy imply
\(\theta(1-\theta)\geq1/\operatorname{poly}(\log N)\) for all sufficiently
large balanced inputs.  For a nonzero deviation
\(\Delta=\theta-\operatorname{area}(R)\) with
\(|\Delta|\leq4D_N^*=N^{-1/2+o(1)}\), relative RMSE requires

\[
 m\geq\frac{\theta(1-\theta)}{\eta^2|\Delta|^2}
 =N^{1-o(1)}.
\]

The Bernoulli fourth-moment analogue is valid after
\(m\theta(1-\theta)=\Omega(1)\), which is only an inverse-polynomial-in-
\(\log N\) burn-in under the regular-bin hypothesis.  Its confidence wording
needs the same \(c_0\) qualification as the Fourier-character argument.

The rejection-ticket probability is also exact.  Among the \(N\) residues,
there are \(q-1\) with gcd exactly \(p\) and \(p-1\) with gcd exactly \(q\),
for total probability

\[
 \frac{p+q-2}{N}=N^{-1/2+o(1)}.
\]

The residue zero is a rejection with gcd \(N\), not a factor ticket, and was
correctly omitted.  A polynomial in \(\log N\) number of proposals has
negligible probability of seeing such a ticket.

## 8. Mandatory amendments before reconstruction/promotion

The candidate is mathematically salvageable without changing any theorem
formula.  Make these textual repairs:

1. In section 3, replace “proper divisor” by “nontrivial proper divisor
   \(1<d<N\).”  Literally, \(1\) is a proper divisor, so the current bullet
   says every ordinary gcd screen factors \(N\).
2. Define “factor-free frequency” using all stated public gcd screens, or
   say merely “common-gcd-free” when only \(\gcd(a,b,N)=1\) is intended.
3. Replace the unqualified fixed-confidence inference after (32) by the
   quantified statement: for the absolute \(c_0,c_1\) in (32), confidence
   greater than \(1-c_0\) requires
   \(m\geq c_1^2/(\eta^2|\mu|^2)\).  Apply the same wording to the regular-bin
   claim.  The relative-RMSE statement remains unchanged.
4. In the candidate verdict, replace “fails ... for public polynomial
   Fourier lists” by “fails for ordinary empirical means of public
   polynomial Fourier lists, and for polynomial-\(\ell^1\) linear
   combinations of those means.”  Arbitrary nonlinear joint processing of
   the list was not bounded.
5. State that histogram TV in (28) refers to a disjoint exhaustive
   rectangular partition.  For overlapping rectangle lists, only the
   coordinate and summed absolute-deviation bounds are asserted.
6. Optionally replace “CRT idempotents are preserved by inversion” with the
   precise coordinatewise-inversion wording from section 1 of this audit.

Subject to these amendments, the hostile audit passes.  The required next
stage is a fresh context-free proof-blind reconstruction; this audit is not
that reconstruction and makes no promotion recommendation beyond sending the
amended theorem to that stage.
