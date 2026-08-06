# F31 third fresh hostile re-audit: amended low-degree local OR/XOR obstruction

**Artifact audited:**
`experiments/F31_low_degree_joint_amortization_kill/RESULT.md` (current amended
version).

**Comparison material read:** the first hostile audit, both earlier re-audits,
and the proof-blind reconstruction.

**Protocol:** proof-only hostile audit.  No mathematical computation was run.
The candidate and canonical files were not edited.

## Verdict

**CLEAN PASS.**

The amendments prompted by the proof-blind reconstruction are correct.  In
particular, the candidate now uses the actual degrees after reduction in each
characteristic, gives the exact CRT exclusive-or probability, optimizes it
over the full degree-bound rectangle, conditions correctly on random
coefficients, and states all four formal-zero cases exactly.  It also retracts
the earlier interpretive overclaim: this is not a genuine joint-decoder
theorem.  A product over a field only ORs its factors' zero events, and CRT
turns the two local OR events into an XOR.

I find no mathematical or quantifier correction still required.  The theorem
remains deliberately narrow: it does not obstruct high-actual-degree succinct
pooling, non-affine or correlated sources, same-sample selection, metric
decoders, rational or branching computations, or statistics that combine
typical nonzero values.  Those are scope limitations, not defects in the
stated result.

## 1. Fixed-polynomial theorem

Let \(N=pq\), where \(p\ne q\) are prime, and let

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k).
\]

CRT identifies this probability space with the product of independent uniform
spaces

\[
\mathbb F_p^k\times\mathbb F_q^k.
\]

For fixed \(F_j\in\mathbb Z[X_1,\ldots,X_k]\), write

\[
f_{j,r}=F_j\bmod r,
\qquad
\delta_{j,r}=\deg f_{j,r},
\qquad
\Delta_r=\sum_j\delta_{j,r}
\]

when all the displayed reductions are formally nonzero.  If
\(D=\sum_j\deg F_j\), then reduction can lower total degree but cannot increase
it, so

\[
\Delta_r\le D.
\]

Because a polynomial ring over a field is an integral domain,

\[
g_r:=\prod_j f_{j,r}\ne0,
\qquad
\deg g_r=\Delta_r.
\]

Schwartz--Zippel therefore gives, with

\[
\alpha_r=\Pr[g_r(X_r)=0],
\qquad
u_r=\min\left(1,\frac{\Delta_r}{r}\right),
\]

the valid all-degree estimate

\[
0\le\alpha_r\le u_r.
\]

No inequality \(\Delta_r<r\) is needed for validity.  At characteristic-scale
degree the estimate may simply become vacuous.  Shared variables among all
the factors do not affect this argument.

The terminal gcd is proper exactly when one, but not both, of the two local
products vanishes.  Since the two events are functions of the independent
vectors \(X_p\) and \(X_q\), the exact probability is

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\]

This verifies equations (0.1), (2.2), and (3.3) of the candidate.  The only
independence used here is independence between the complete \(p\)- and
\(q\)-components.  There is no independence assumption among factors,
relations, coordinates, or their local zero events.

## 2. The rectangular envelope and all caps

Set

\[
h(a,b)=a+b-2ab.
\]

On the rectangle \([0,u]\times[0,v]\), this bilinear function attains its
maximum at a corner.  The four corner values are

\[
0,\qquad u,\qquad v,\qquad u+v-2uv.
\]

Thus

\[
\Psi(u,v)=\max\{u,v,u+v-2uv\}
\]

is exactly the sharp envelope implied by the two rectangular constraints
alone.  The candidate does not overstate this as an attainability theorem for
every arbitrary pair \(u,v\).

The simpler chain

\[
h(\alpha_p,\alpha_q)
\le \alpha_p+\alpha_q
\le \frac{\Delta_p}{p}+\frac{\Delta_q}{q}
\]

and the trivial probability cap prove

\[
\Pr(\text{proper gcd})
\le
\min\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}
\le
\min\left\{1,D\left(\frac1p+\frac1q\right)\right\}.
\]

All needed caps are present.

If \(u,v\le1/2\), then

\[
u+v-2uv\ge u,
\qquad
u+v-2uv\ge v,
\]

so the final corner is maximal.  If \(D\le\min(p,q)/2\), both
\(D/p\) and \(D/q\) are at most \(1/2\).  On this rectangle \(h\) is
coordinatewise nondecreasing, because its partial derivatives are
\(1-2b\) and \(1-2a\).  Hence the candidate's sharpened bound

\[
\Pr(\text{proper gcd})
\le
\frac Dp+\frac Dq-\frac{2D^2}{pq}
\]

is valid.  Replacing \(D/p,D/q\) by
\(\Delta_p/p,\Delta_q/q\) gives the sharper local-degree version.  There is no
sign error in the negative cross term and no missing low-degree hypothesis.

## 3. Random coefficient families

Let \(\Theta\) be coefficient randomness independent of the evaluated batch
\(X\).  Conditional on \(\Theta=\theta\), the polynomial family is fixed and
the two CRT sample components remain independent.  Therefore the exact
conditional formula is

\[
h(\alpha_p(\theta),\alpha_q(\theta)),
\]

and the unconditional probability is

\[
\mathbb E_\Theta[
  \alpha_p(\Theta)+\alpha_q(\Theta)
  -2\alpha_p(\Theta)\alpha_q(\Theta)].
\]

The candidate correctly does **not** replace the expected product by a
product of unconditional marginals.  Shared coefficient randomness can
correlate the two conditional root probabilities even though the CRT sample
is independent after conditioning.

If the actual local degree sums have uniform bounds \(B_p,B_q\), rectangle
inclusion gives

\[
\Pr(\text{proper gcd})
\le
\Psi\left(
  \min(1,B_p/p),
  \min(1,B_q/q)
\right).
\]

For random integrable degree budgets, the pointwise linear bound instead
gives

\[
\Pr(\text{proper gcd})
\le
\mathbb E\left[
  \frac{\Delta_p(\Theta)}p+
  \frac{\Delta_q(\Theta)}q
\right].
\]

This remains valid when the displayed sum exceeds one, so no extra cap is
needed for correctness.  The candidate also explicitly requires the local
formal-nonidentity hypothesis almost surely and routes formal-zero
realizations through the pointwise four-case table instead of averaging them
silently into this theorem.

## 4. Fresh adaptation and the same-sample boundary

The adaptive paragraph has the right conditioning order.  After any reachable
history, the next batch must still be fresh and uniform on the full affine CRT
space, and the specialized polynomial in its fresh variables must be formally
nonzero in both characteristics.  Conditional Schwartz--Zippel bounds each
new local zero event.  A union bound and the tower property then charge the
uniform or expected sum of the conditional actual reduced-degree budgets.
Independence between rounds is unnecessary.

The candidate makes no corresponding claim for a polynomial selected after
the point being evaluated has already been inspected.  Its example

\[
F_a(T)=T-a,\qquad a=X,
\]

correctly shows that the conditional degree-one root estimate can fail
completely: the selected polynomial vanishes at the reused point with
probability one.  This example need not itself produce a proper gcd; it
refutes the conditional Schwartz--Zippel step for same-sample selection, which
is exactly the claim for which it is used.

## 5. Exact formal-zero/content table

For a collected integer polynomial, let \(c(F)\) be the gcd of the absolute
values of its coefficients, with \(c(0)=0\).  Then

\[
F\bmod r=0\text{ formally}
\quad\Longleftrightarrow\quad
r\mid c(F).
\]

Thus a factor formally zero modulo \(p\) but nonzero modulo \(q\) has

\[
\gcd(N,c(F))=p,
\]

and symmetrically for \(q\).  This is a structural statement for every
integer polynomial and an algorithmic statement when the collected
coefficient list is explicitly available with polynomial total access and
coefficient bit complexity.

Let

\[
Z_r=\{j:f_{j,r}\text{ is the zero formal polynomial}\}.
\]

The candidate's complete product table is exact:

| \(Z_p\) | \(Z_q\) | proper-gcd probability |
|---|---|---|
| empty | empty | \(\alpha_p+\alpha_q-2\alpha_p\alpha_q\) |
| nonempty | empty | \(1-\alpha_q\) |
| empty | nonempty | \(1-\alpha_p\) |
| nonempty | nonempty | \(0\) |

For example, in the second row the product is always zero modulo \(p\), and
is nonzero modulo \(q\) precisely off the \(q\)-side root event.  Moreover,
because \(Z_q\) is empty, every \(j\in Z_p\) is a one-sided formal-zero factor,
so its individual content exposes \(p\).  The symmetric reasoning proves the
third row.  In the final row the product is always zero modulo both primes,
whether synchronization comes from one two-sided factor or from different
one-sided factors.  The example \(F_1=p,F_2=q\) correctly shows why individual
contents must be inspected before multiplication.

The candidate does not claim that the final row always exposes a proper
factor: if the only zero factor is synchronized, its content gcd can be
\(N\).  This distinction is stated correctly.

## 6. Formal zero versus zero function

For \(H\in\mathbb F_r[X_1,\ldots,X_k]\), the vanishing ideal of the full
affine space is exactly

\[
\((X_1^r-X_1,\ldots,X_k^r-X_k)\).
\]

Division by these monic generators gives a unique remainder of individual
degree below \(r\) with the same evaluations.  Induction on the variables
shows that such a remainder cannot vanish everywhere unless it is formally
zero.  The candidate's equation (4.3) and its proof are therefore correct.

In particular, \(X_1^r-X_1\) is formally nonzero but functionally zero and
remains in the Schwartz--Zippel branch at the vacuous bound \(r/r=1\).  Also,
if every individual degree is below \(r\), the evaluation map is injective
even when total degree is at least \(r\).  These statements are consistent
and no formal identity is being inferred merely from universal vanishing.

## 7. Representation and degree claims

The representation distinctions are now correct.

- For an explicit canonical dense or sparse coefficient list of polynomial
  size with polynomial-bit coefficients, taking coefficient gcds is
  polynomial-bit work.  In the sparse case, a binary exponent can have an
  exponentially large value while using only polynomially many bits; term
  count is therefore not a degree bound.
- A fixed branch-free division-free arithmetic circuit denotes a formal
  polynomial, so the probability theorem applies semantically at its actual
  reduced degrees.
- Polynomial circuit size does not bound actual formal degree: repeated
  squaring gives exponential degree.  Cancellation over the integers and
  reduction modulo the two primes can lower the actual degrees differently.
- The expanded coefficient content and even the relevant formal identities
  need not be efficiently exposed from a succinct circuit.  The structural
  content dichotomy is not an automatic circuit algorithm or a circuit lower
  bound.

The bit-complexity statement is scoped to an explicit polynomial-size
coefficient representation; it does not assert polynomial processing of a
super-polynomial-length sparse encoding.  The determinant, Gram-minor,
matrix-product, and rank-drop examples likewise claim only their stated
formal-degree bounds and do not smuggle in a coefficient extractor for a
succinct circuit.

## 8. Balanced threshold

If \(p\le q\le\kappa p\) for fixed \(\kappa\), then

\[
p\ge\sqrt{N/\kappa},
\qquad
q\ge\sqrt N,
\]

and hence

\[
\frac1p+\frac1q
\le
\frac{\sqrt\kappa+1}{\sqrt N}.
\]

Therefore

\[
\Pr(\text{proper gcd})
=O_\kappa(D/\sqrt N).
\]

With \(n=\lceil\log_2(N+1)\rceil\) and \(D\le n^A\), this upper bound is

\[
2^{-n/2+O(\log n)}.
\]

Conversely, if the success probability within the theorem's nonidentity
model is at least \(n^{-B}\), comparison with the upper bound forces

\[
D=\Omega_\kappa(\sqrt N/n^B).
\]

This is only a necessary actual-degree scale.  The candidate explicitly says
that sparse polynomials and polynomial-size branch-free division-free
circuits can reach it, and that useful local XOR mass plus factor-free
evaluation remain separate obligations.  It therefore makes no
representation-size or factoring lower-bound claim.

## 9. Interpretation and promotion boundary

The revised interpretation is exact:

\[
\prod_j f_{j,r}(X_r)=0
\quad\Longleftrightarrow\quad
\exists j\; f_{j,r}(X_r)=0.
\]

Thus this mechanism does not combine information from typical nonzero
outputs.  It is a local OR of rare algebraic-zero tickets, followed by the
CRT XOR that a proper gcd tests.  Allowing every factor to depend on every
coordinate makes the zero sets dependent, but does not change this logical
OR or its aggregate-degree root bound.

No wording in the amended Classification, Outcome, examples, threshold, or
reopen condition now calls this a genuine joint decoder.  High-degree pooling
and a statistic that reconstructs from ubiquitous nonzero information remain
open rather than being declared impossible.

### Required corrections

None.

### Scope limitations that must remain attached to any promoted statement

1. \(N=pq\) with distinct primes for the exact displayed CRT table.
2. Full joint affine uniformity of the evaluated batch, not merely uniform
   marginals or a uniform distribution on a relation variety.
3. Fixed coefficients, coefficient randomness independent of the evaluated
   batch, or adaptation only to a genuinely fresh batch.
4. Actual reduced formal-degree budgets or proved valid upper bounds on them;
   term count and circuit size alone are not degree bounds.
5. Polynomial zero tests combined by a product; no rational, branching,
   metric, projective, conditioned, or typical-nonzero joint decoder is
   covered.

Subject to those stated boundaries, the current amended F31 result is ready
for promotion after the root verifies that the proof-blind reconstruction is
accepted as the required independent reconstruction step.
