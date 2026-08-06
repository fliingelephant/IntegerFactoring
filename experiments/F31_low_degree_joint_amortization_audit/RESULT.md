# F31 hostile audit: low-degree joint amortization

**Artifact audited:**
`experiments/F31_low_degree_joint_amortization_kill/RESULT.md`.

**Protocol:** proof-only hostile audit.  No computation was used.  The
candidate and canonical files were not edited.

## Verdict

**PASS WITH REQUIRED CORRECTIONS.**

The central deterministic theorem is correct.  If \(X\) is uniform on the
whole affine space \((\mathbb Z/N\mathbb Z)^k\), \(N=pq\) with distinct
primes, and every displayed integer polynomial has a nonzero *formal*
reduction over both prime fields, then a terminal gcd of their product has
proper-factor probability at most

\[
\left(\sum_j \deg F_j\right)\left(\frac1p+\frac1q\right).
\]

Shared variables, products, and a polynomial coupling every coordinate do
not weaken this bound.  Schwartz--Zippel is valid for arbitrary total
degree; the bound simply becomes vacuous when the degree reaches a field
size.  The coefficient-content alternative is also structurally correct,
and it is algorithmic for an explicit collected polynomial-size coefficient
list.

The report should not be promoted unchanged.  The following repairs are
required.

1. **Qualify randomized families.**  Conditioning and averaging proves the
   same inequality only when the local formal-nonidentity hypothesis holds
   for every supported coefficient choice (or almost surely), and when the
   degree budget is uniformly bounded.  With a random degree budget the
   right statement uses its expectation.  If a supported choice gives a
   local zero polynomial, that choice belongs to the coefficient-content
   branch and cannot be silently averaged into (0.1).
2. **Distinguish a formal zero polynomial from a zero polynomial
   function.**  A nonzero formal polynomial such as \(T^r-T\) in
   \(\mathbb F_r[T]\) vanishes at every field point.  It is still covered by
   Schwartz--Zippel, with the vacuous sharp bound \(r/r=1\); it is not a
   coefficient-content collapse.  Replace claims that the theorem “does
   not cover characteristic-specific polynomial identities” by the precise
   claim that its *sparse obstruction gives no information* at the required
   characteristic-scale degree.
3. **Keep full joint affine uniformity in every summary.**  Uniform
   marginals, or local uniformity on a relation space, do not suffice.  For
   example, if \(U\) is uniform and \(X_1=X_2=U\), both coordinates are
   uniform but the degree-one polynomial \(X_1-X_2\) vanishes surely.  The
   candidate's Section 7 states the correct full-affine hypothesis, but the
   broader phrases “locally uniform relations” and “a polynomial-size
   batch” must not be used without “jointly uniform affine coordinates.”
   Projective lines, conditioned fibres, and correlated batches remain
   outside the theorem.
4. **State the product identity cases exactly.**  Delete the duplicated
   words “a product the product.”  If a product is formally zero over
   exactly one prime field, an individual factor is a mixed formal identity.
   If it is formally zero over both, synchronization may arise either from
   one factor zero over both or from two different one-sided-zero factors.
   In the latter case the individual explicit contents still expose factors,
   although the product gcd itself is \(N\).
5. **Preserve the same-sample-adaptivity exclusion.**  Merely conditioning
   on a polynomial selected after seeing its evaluation point is invalid.
   The exact counterexample to the conditional root estimate is: after observing \(X=a\), select
   \(F_a(T)=T-a\) and evaluate it at \(T=X\).  Every selected polynomial has
   degree one, but the value is always zero.  Sequential adaptation is valid
   only on a genuinely fresh batch, after specializing the past, with a
   nonzero conditional polynomial at every reachable history.  A
   branch-free global symbolic polynomial may instead be analyzed at its
   global degree.
6. **Use circuit language narrowly.**  The extension is to branch-free,
   division-free arithmetic circuits, whose actual polynomial degree is
   bounded by circuit formal degree.  Polynomial circuit size alone gives
   no degree bound, and a succinct circuit need not expose the expanded
   coefficient content.  The candidate substantially says this already;
   the qualifier must accompany any promoted claim about circuits.

These are scope and quantifier repairs, not failures of the main
Schwartz--Zippel obstruction.

## 1. Deterministic theorem and CRT independence

Let

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k),
\qquad N=pq,
\]

with \(p\ne q\) prime.  CRT is an isomorphism of finite probability spaces,
not merely a bijection of rings, so

\[
(X_p,X_q)\sim
\operatorname{Unif}(\mathbb F_p^k)\times
\operatorname{Unif}(\mathbb F_q^k).
\]

In particular the complete local vectors are independent; this is stronger
than coordinatewise or marginal uniformity.

For fixed \(F_j\in\mathbb Z[X_1,\ldots,X_k]\), write

\[
f_{j,r}=F_j\bmod r,
\qquad d_j=\deg F_j,
\qquad D=\sum_j d_j.
\]

Assume every \(f_{j,r}\) is a nonzero formal polynomial for
\(r\in\{p,q\}\).  Formal reduction may lower degree, so
\(\deg f_{j,r}\le d_j\).

Schwartz--Zippel over the set \(S=\mathbb F_r\) gives, for every nonzero
formal polynomial of total degree \(d\),

\[
\Pr[f(Z)=0]\le d/r.
\]

The usual induction proof does not require \(d<r\).  When \(d/r>1\), the
inequality remains true but useless.  It also permits arbitrary sharing of
variables: no independence among monomials, factors, or output polynomials
is invoked.

For one \(F\), let

\[
\alpha_r=\Pr[f_r(X_r)=0].
\]

The two zero events depend on independent local vectors, hence

\[
\Pr(1<\gcd(N,F(X))<N)
=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
\le \deg(F)\left(\frac1p+\frac1q\right).
\]

This verifies the candidate's exact CRT and single-joint-polynomial claims.

## 2. Products and shared variables

Put \(P=\prod_jF_j\).  Because each
\(\mathbb F_r[X_1,\ldots,X_k]\) is an integral domain,

\[
P(X_r)=0
\quad\Longleftrightarrow\quad
f_{j,r}(X_r)=0\text{ for at least one }j.
\]

Therefore, without expanding the product,

\[
\Pr[P(X_r)=0]
\le \sum_j\Pr[f_{j,r}(X_r)=0]
\le D/r.
\]

A proper gcd is contained in the union of the two local zero events, which
proves

\[
\Pr(1<\gcd(N,P(X))<N)
\le D\left(\frac1p+\frac1q\right).
\]

In fact, for fixed coefficients the two product-zero events are independent,
so an XOR formula analogous to the single-output formula is available.  The
union bound is enough and remains valid without using that extra fact.

This proof confirms that products and shared variables cause no gap.  It is
also clear why the statement is not just a union over independent samples:
one \(F_j\) may contain every coordinate and the \(F_j\)'s may share every
variable.  The only union in the multi-output version is a union of their
zero sets.

## 3. Formal identities and coefficient content

For a collected integer polynomial \(F=\sum_\nu a_\nu X^\nu\), its formal
reduction modulo \(r\) is zero exactly when \(r\mid a_\nu\) for every
\(\nu\).  Thus, with

\[
c(F)=\gcd_\nu a_\nu,
\]

the mixed case

\[
F\bmod p=0,
\qquad
F\bmod q\ne0
\]

gives

\[
\gcd(N,c(F))=p,
\]

and symmetrically for \(q\).  If both formal reductions vanish, the content
is divisible by \(N\) and this particular identity is synchronized.  The
zero integer polynomial belongs to this latter case and must be treated
separately because its content is convention-dependent.

For an explicit collected list with polynomially many polynomial-bit integer
coefficients, ordinary integer gcd computes this factor in polynomial bit
complexity.  This algorithmic conclusion does not transfer to a succinct
arithmetic circuit: even a low-degree polynomial in polynomially many
variables may have exponentially many expanded monomials, and cancellations
may hide the collected coefficients.  The structural content statement
still holds after expansion, but no efficient extraction theorem follows.

The exact product classification is as follows.  Let

\[
Z_r=\{j:f_{j,r}\text{ is the zero formal polynomial}\}.
\]

- If \(Z_p=Z_q=\varnothing\), the product is formally nonzero in both fields
  and the probability theorem applies.
- If exactly one of \(Z_p,Z_q\) is nonempty, some individual factor is a
  mixed formal identity and its explicit content factors \(N\).
- If both are nonempty, the product is formally zero in both fields.  This
  can be caused by \(Z_p\cap Z_q\ne\varnothing\), or by distinct factors in
  \(Z_p\setminus Z_q\) and \(Z_q\setminus Z_p\).  The product is synchronized;
  in the second subcase the individual explicit factors nevertheless expose
  the primes.

This is the precise repair to Section 4.

## 4. Randomization and adaptation

Let \(C\) be public randomness independent of \(X\), and condition on
\(C=c\).  If every supported \(c\) gives nonzero local formal reductions and
has \(D(c)\le D_*\), the deterministic proof gives

\[
\Pr(\text{proper gcd})
\le D_*\left(\frac1p+\frac1q\right).
\]

If only \(\mathbb E D(C)<\infty\) is known, the corresponding bound is

\[
\Pr(\text{proper gcd})
\le \mathbb E[D(C)]\left(\frac1p+\frac1q\right),
\]

again under the almost-sure formal-nonidentity condition.  Coefficient
choices violating that condition require the separate identity analysis;
there is no unconditional averaging shortcut.

For sequential adaptation, let \(H_{t-1}\) be the full past and let \(Z_t\)
be a fresh independent uniform affine CRT batch.  After conditioning on
\(H_{t-1}=h\), the next output must be regarded as a polynomial in the fresh
variables \(Z_t\).  If at every reachable \(h\) its two local specializations
are nonzero formal polynomials and its conditional fresh-variable degree is
at most \(D_t(h)\), conditional Schwartz--Zippel and a union bound give the
sum (or expected sum) of those budgets.  Specialization can turn a globally
nonzero expression into the zero polynomial, so the reachable-history
condition is essential.

No such conditioning is legitimate when the same point is first inspected
and then used to select its test polynomial.  The degree-one selector
\(F_a(T)=T-a\) with \(a=X\) makes the local zero event certain, so it is the
smallest counterexample to the claimed conditional Schwartz--Zippel root
estimate.  (Its gcd is synchronized and therefore does not itself factor
\(N\).)  An implicit branch family can be exponentially large even when its
selection algorithm has polynomial running time.

## 5. Audit of the examples

The five examples are valid with their stated hypotheses and the following
precision.

1. A nonconstant affine-linear form on the full affine space has exactly
   \(r^{k-1}\) zeros and hence local zero probability \(1/r\).  This does not
   hold merely from uniform coordinate marginals.
2. A product of \(K\) scalar tickets has degree at most the sum of their
   degrees.  Shared variables do not change this.  A polynomial-size number
   of polynomial-degree tickets remains in the sparse regime; a succinct
   exponentially long product need not.
3. A \(t\times t\) determinant of affine-linear entries has degree at most
   \(t\).  A Gram determinant has degree at most \(2t\) when the underlying
   vector coordinates are affine-linear.  Characteristic-specific or
   dimension-forced determinant identities belong to the formal-identity
   branch if they are formal zero, and to the high-degree/vacuous branch if
   they are only zero as functions.
4. A scalar entry of a product of \(K\) matrices with affine-linear scalar
   entries is an ordinary commutative polynomial of degree at most \(K\),
   even though matrix multiplication is noncommutative.  The theorem applies
   entrywise.  It does not cover inversions or a branch taken on a nonunit.
5. A local rank-drop event is an intersection of minor-zero events.  If a
   defining minor is a nonzero formal polynomial locally, rank drop is a
   subset of its zero event and inherits its degree bound.  The witnesses for
   the \(p\)- and \(q\)-bounds may be different minors.  If no defining minor
   is formally nonzero in one characteristic while one is nonzero in the
   other, there is instead a coefficient-content rank separator.  A product
   of minors detects their union, not their simultaneous vanishing, but its
   larger union is still bounded by the sum of degrees.

Thus none of the linear, determinant/Gram, noncommutative-product, or
rank-drop examples refutes the theorem.  Their promotion should retain the
explicit linear-entry and full-affine-source hypotheses.

## 6. Balanced threshold

If \(p\le q\le\kappa p\), then

\[
\frac1p+\frac1q=O_\kappa(N^{-1/2}).
\]

Hence

\[
\Pr(\text{proper gcd})=O_\kappa(D/\sqrt N).
\]

For \(n=\lceil\log_2(N+1)\rceil\) and \(D\le n^A\), this is

\[
2^{-n/2+O_\kappa(\log n)}.
\]

Conversely, an inverse-polynomial success claim \(\Pr\ge n^{-B}\) under all
the theorem's nonidentity hypotheses requires

\[
D=\Omega_\kappa(\sqrt N/n^B).
\]

This is only a necessary degree scale.  Schwartz--Zippel supplies no useful
upper obstruction once \(D\) is comparable with a hidden prime.  A
branch-free division-free polynomial-size circuit can have that exponential
formal degree by repeated squaring, so this argument is not a lower bound on
polynomial-size arithmetic circuits.

## 7. Novelty and exact boundary

The route is materially distinct from the cited prior results.

- P08 computes an exact sparse probability for one specialized linear
  polynomial-gcd probe.  F31 proves the general full-affine polynomial-zero
  bound and permits one polynomial to couple all coordinates.
- P31 treats projective-line distributions, normalization, and fixed
  comparison menus.  Those sources are not full affine space, so F31 does
  not subsume P31 or its surviving same-source dependence.
- P35 concerns deterministic public kernel/output lattices and particular
  metric quotients.  F31 neither subsumes those lattice statements nor
  addresses their surviving metric boundary.
- F02 is the genuine high-degree escape.  Exponential formal degree can make
  the F31 bound vacuous; constructing a succinct shared evaluator with useful
  local XOR mass remains a separate open problem.

Accordingly the corrected result is legitimate evidence against one exact
mechanism: **jointly uniform affine CRT coordinates fed to a fixed or
fresh-batch-adaptive, low-total-degree, polynomial-zero decoder**.  It is not
evidence against projective or conditioned relations, same-sample adaptive
selection, metric decoders, succinct high-degree circuits, or general
polynomial-time joint computation.

After the six corrections above, the candidate is suitable for a strict
proof-blind reconstruction.  No canonical promotion is warranted before
that reconstruction.
