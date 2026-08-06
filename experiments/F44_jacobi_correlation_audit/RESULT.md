# F44 focused hostile audit

**Artifact audited:** `experiments/F44_jacobi_correlation_kill/RESULT.md`

**Audit mode:** proof-only.  I ran no computation and used no finite
certificate.  I read the candidate in full and checked it against the fixed
task, the F09 registry entry, X10/P15, X43/P49, and the corresponding progress
entries.

## Verdict

**PASS.**  I found no mathematical error, quantifier failure, hidden factoring
call, or unsupported inference in the candidate's stated scope.  The artifact
is ready for the required fresh proof-blind reconstruction.

The pass is deliberately narrow.  In particular, the sequential
total-variation theorem is valid only for the compressed observation channel
stated in Section 8: a selector sees prior compressed products (and exogenous
public coins), then a fresh source is drawn independently and only its one
scalar product is returned.  The sampled residue, the per-shift Jacobi vector,
same-source reuse, and individual gcd/zero identities are not part of that
channel.  The candidate states all of these exclusions.  Dropping any one of
them would invalidate the hybrid argument and would require a new audit.

## 1. Collision screening and multiplicities

After normalization and collection of global duplicates, two distinct shifts
have a nonzero difference modulo (N=pq).  Its gcd with (N) is therefore
exactly (1,p), or (q).  These cases respectively mean no local collision,
a collision only modulo (p), or a collision only modulo (q).  A collision
at both primes would be equality modulo (N), which collection has removed.
Thus the claimed factor-or-local-injectivity dichotomy is exact.

The insistence on screening each difference separately is necessary.  A
product of differences can contain both (p) and (q) and have gcd (N),
whereas the individual differences expose the two proper factors.  Screening
the union of a polynomial explicit list, and screening each newly realized
adaptive shift against the accumulated union, uses polynomially many gcds and
gives injectivity at both fields on every continuing branch.  If an adaptive
menu instead manufactures a factor-bearing difference, that is a successful
gcd branch, not a branch covered by the small-signal conclusion; the artifact
says so.

Collecting multiplicities before taking parity is also correct.  It prevents a
global duplicate from masquerading as a one-prime collision and makes the odd
support (O) and even-only support (A) well-defined over both local fields.

## 2. Exact CRT mean and zeros

For every integer (z), including a nonunit,

\[
 \chi_N(z)=\chi_p(z)\chi_q(z),
\]

because all three characters are extended by zero.  CRT sends uniform
(x\bmod N) to independent uniform local coordinates, so the product
correlation factors pointwise and its complete mean is exactly

\[
 \theta_H=\frac{S_p(H)S_q(H)}{pq}.
\]

No additive-character twist or independence assumption is missing.

Even positive powers cannot be cancelled at roots.  On the locally injective
branch, if (O=\varnothing), the product is one off the (s) distinct roots
and zero at them, hence (S_r=r-s).  If (O\ne\varnothing), the provisional
sum of \(\chi_r(P_O(t))\) already vanishes at the odd-support roots.  At each
even-only root it has the one extra nonzero value
\(\chi_r(P_O(-e))\).  Subtracting precisely these values proves

\[
 S_r=C_r(O)-R_r(O,A).
\]

Every term of (R_r) is indeed (\pm1), since local injectivity keeps an
even-only root away from every odd-support root.

## 3. Centered Hasse--Weil bounds and edge cases

For squarefree monic (P_O) of degree (k\ge1), the smooth projective model
of (y^2=P_O(t)) is geometrically connected.  The affine point count is
(r+C_r).

* If (k) is odd, the genus is ((k-1)/2) and there is one rational point at
  infinity.  Hasse--Weil gives 
  \(|C_r|\le(k-1)\sqrt r\).
* If (k) is even, the genus is ((k-2)/2).  Monicity gives two rational
  points at infinity, so the centered quantity is (C_r+1), and
  \(|C_r+1|\le(k-2)\sqrt r\).

The potentially dangerous low-degree cases are correct: (k=1) gives
(C_r=0), and (k=2) gives (C_r=-1).  A nonempty even-only set merely
contributes (a) signs through (R_r); it does not alter the curve or its
infinity correction.

Consequently, for odd (k),

\[
 |S_r|\le(k-1)\sqrt r+a\le(s-1)\sqrt r,
\]

and, for nonzero even (k),

\[
 |S_r|\le(k-2)\sqrt r+1+a\le(s-1)\sqrt r.
\]

This verifies the uniform local bound and hence

\[
 |\theta_H|\le (s-1)^2/\sqrt N
\]

whenever the odd support is nonempty.  All possible local square
degenerations of the explicit linear-factor product require a local collision;
those collisions were already either collected globally or exposed by an
individual difference gcd.

## 4. Scalar law, RMSE, and direct gcd tickets

The square (Y_H^2) is one exactly when neither local coordinate hits any of
the (s) roots.  Injectivity gives the exact second moment

\[
 \rho_H=(1-s/p)(1-s/q).
\]

For a random variable supported on 
\(\{-1,0,1\}\), its mean and second moment give exactly the three
probabilities stated in the candidate, and therefore

\[
 \operatorname{Var}(Y_H)=\rho_H-\theta_H^2,
 \qquad
 \mathbb E(\bar Y_m-\theta_H)^2
 =\frac{\rho_H-\theta_H^2}{m}
\]

for iid fresh calls.

On a fixed-balance family with polynomial (s), sufficiently large inputs
have (\rho_H\ge9/16) and
\(\theta_H^2\le(s-1)^4/N\le1/16\).  For
\(\theta_H\ne0\), the claimed relative-RMSE lower bound follows exactly.
For (\theta_H=0\), the candidate correctly refuses to define relative error
and states only the absolute MSE.  It does not turn an MSE identity into an
arbitrary-confidence testing lower bound.

The direct-gcd probability is also exact.  The nonunit event has probability
(1-\rho_H).  Exactly the (s) global points (x=-e\bmod N) give only gcd
(N); all other nonunit points give at least one gcd (p) or (q).  Hence

\[
 \tau_H=1-\rho_H-s/N
 =\frac{s(p+q-s-1)}N.
\]

The fixed-balance (O_\Lambda(s/\sqrt N)) bound and its polynomial-union
consequence follow.

## 5. All-even pattern

When every multiplicity is even, (Y_H) is exactly the indicator that all
shifted values are units.  Thus (\theta_H=\rho_H), and

\[
 \delta_H=1-\theta_H
 =\frac{s(p+q)-s^2}{N}.
\]

For (s>0), exact knowledge of this mean recovers
(p+q=[N(1-\theta_H)+s^2]/s), after which the quadratic with product (N)
recovers the two primes.  The candidate properly puts exact symbolic
evaluation outside the killed mechanism.

For raw Bernoulli sampling, the deviation estimator has variance
\(\delta_H(1-\delta_H)/m\).  Since polynomial (s) is eventually much less
than (p,q) on a fixed-balance family, (1-\delta_H) is bounded below and
\(\delta_H\le2\Lambda s/\sqrt N\).  This proves the stated
\(\Omega_\Lambda(\sqrt N/(\eta^2s))\) relative-RMSE requirement for the
deviation.  No claim is made for small exceptional members before the
asymptotic regime or for estimating the irrelevant near-one baseline itself.

## 6. Lists, conditioning, and the scalar transcript hybrid

For an explicit list, the reference baseline (b_H) is publicly computable
from multiplicity parity: zero for nonempty odd support and one for all-even
support.  The triangle inequality gives the displayed

\[
 \frac{B\max(T^2,2\Lambda T)}{\sqrt N}
\]

bound for every coefficient vector with polynomial \(\ell^1\) budget.  This
uses only linearity of expectation, so shared-source dependence between
coordinates neither helps nor invalidates that one statement.  The artifact
correctly declines to extend it to a nonlinear function of the vector.

For a past-measurable realized menu followed by a genuinely fresh independent
source, conditioning freezes the menu and restores exactly the fixed-menu
calculation.  Rich past transcripts are allowed for this conditional-mean
claim.  Same-source selection is not.

For completeness, I reconstructed the stronger sequential theorem.  For one
odd-pattern call, with \(\zeta=1-\rho\), comparison with a fair Rademacher law
gives

\[
 d_{\rm TV}
 =\frac12\left(\zeta+rac{|\theta-\zeta|}{2}
                         +\frac{|\theta+\zeta|}{2}\right)
 =\frac{\zeta+\max(\zeta,|\theta|)}2.
\]

For an all-even call, comparison with the constant-one law gives exactly
(d_{\rm TV}=\zeta\).  Combining the complete-mean and zero-mass bounds yields
the candidate's per-call epsilon.

The public reference process is implementable without (p) or (q): run the
same selector recursively on its own prior reference scalars; after a
screened menu (H) is chosen, output an independent fair sign if its odd
support is nonempty and output one otherwise.  Difference-gcd screens are
public deterministic computations in both processes.  An existential maximal
coupling may use the unknown exact real law, but implementability of a coupling
is neither required nor claimed; the reference marginal itself is explicit.

On every common history the selectors choose the same menu.  Maximal coupling
therefore bounds the conditional first-separation probability by the per-call
epsilon, and the first-separation union bound proves the adaptive kernel
hybrid.  If a run terminates at a public difference gcd, one may append a
common absorbing terminal symbol; this does not change the proof.  With
\(\sum_t s_t\le T\) on every execution,

\[
 \sum_t s_t^2\le(\sum_t s_t)^2\le T^2,
\]

so the total bound is exactly

\[
 \frac{2\Lambda T+T^2/2}{\sqrt N}.
\]

This argument would be false if the selector were allowed to observe or reuse
the sampled (x_t), because the scalar marginal coupling does not couple the
joint pair ((x_t,Y_t)).  It would likewise be false for the per-shift vector
or several products sharing a source.  Those are expressly excluded in the
audited artifact.

## 7. Scope, complexity, and evidence discipline

Every list operation, normalization, pairwise gcd, exact uniform rejection
sample, Jacobi evaluation, and scalar product has uniform polynomial bit
complexity under the explicit polynomial list/round/support budgets.  The
only imported mathematical result is the standard Hasse--Weil theorem, whose
exact statement and curve application are supplied.  No local characters,
unknown factors, exact complete-sum evaluator, or factoring-equivalent oracle
is invoked by the mechanism.

The artifact ran no computation and claims no finite evidence.  It makes no
claim about the whole per-shift vector, same-source reuse, nonlinear joint
processing, dense or succinct characteristic-scale supports, exact symbolic
sums, other characters/sources, or factoring hardness.  Its similarity in
scale to P49 does not reuse the Kloosterman mechanism, and it does not inflate
P15's individually invariant scalar-character theorem to nonlinear or
vector-valued carriers.

No repair is required for this version.  Promotion still requires the fresh,
context-free proof-blind reconstruction prescribed by `PROMPT.md`.
