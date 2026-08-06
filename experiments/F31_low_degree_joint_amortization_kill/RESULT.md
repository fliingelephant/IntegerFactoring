# F31 kill-first: low-degree joint algebra does not amortize uniform CRT zeros

**Status:** promoted as P40 after a corrected hostile-audit sequence and a
fresh context-free proof-blind reconstruction.

**Family:** F22.

**Closest prior routes and material difference.**  P08 bounds uniform linear
gcd probes.  P31 bounds enumerated projective-line equality tickets, and P35
analyzes particular public relation lattices.  None of those results gives the
exact CRT law for a product of polynomial tests that may each couple every
coordinate of a full jointly uniform affine batch.  The present report does.
Locally, however, the product is still only an OR of polynomial-zero tickets;
its obstruction is charged to their aggregate formal degree without assuming
independence among them.

**Classification.**  This is evidence against the exact auxiliary claim that
a fully jointly uniform affine CRT batch becomes useful merely by multiplying
low-formal-degree polynomial zero tests that may use all its coordinates.  It
is **not** a genuine joint-decoder theorem: it does not cover a statistic that
combines information carried by typical nonzero outputs.  It is not a lower
bound for arithmetic circuits, because a polynomial-size
branch-free division-free circuit can have exponential formal degree.  It
does not cover nonuniform, projective, conditioned, or correlated arithmetic
sources, metric or order comparisons, or matching/Markov-chain samplers.  The
low-degree sparse obstruction does not rule out exponentially pooled products
or characteristic-scale formal polynomials: (0.3) still applies at their
actual degree, but may then be vacuous, and it supplies no automatic succinct
coefficient-content extractor.

No computation was used.

## Outcome

Let \(N=pq\) for distinct primes and let

\[
X=(X_1,\ldots,X_k)
\]

be uniform on \((\mathbb Z/N\mathbb Z)^k\).  Under CRT its two components
\(X_p\in\mathbb F_p^k\) and \(X_q\in\mathbb F_q^k\) are independent and
uniform.  Let

\[
F_1,\ldots,F_s\in\mathbb Z[X_1,\ldots,X_k],
\qquad d_j=\deg F_j,
\qquad D=\sum_{j=1}^s d_j,
\]

and suppose every \(F_j\) has a nonzero formal reduction over both
\(\mathbb F_p\) and \(\mathbb F_q\).  Define the actual reduced degrees

\[
\delta_{j,r}=\deg(F_j\bmod r),\qquad
\Delta_r=\sum_{j=1}^s\delta_{j,r},\qquad
u_r=\min\!\left(1,\frac{\Delta_r}{r}\right)
\quad(r=p,q).
\]

Thus \(\Delta_r\le D\), possibly strictly.  If

\[
\alpha_r=
\Pr\!\left[\prod_j(F_j\bmod r)(X_r)=0\right],
\]

then the exact proper-gcd probability is

\[
\alpha_p+\alpha_q-2\alpha_p\alpha_q,
\qquad 0\le\alpha_r\le u_r.
\tag{0.1}
\]

Consequently, with

\[
\Psi(u,v)=\max\{u,v,u+v-2uv\},
\]

the sharp envelope implied only by the two local degree bounds is

\[
\Pr\!\left(
  1<\gcd\!\left(N,\prod_{j=1}^sF_j(X)\right)<N
\right)
\le \Psi(u_p,u_q).
\tag{0.2}
\]

In particular, the simpler all-degree bound is

\[
\Pr\!\left(
  1<\gcd\!\left(N,\prod_{j=1}^sF_j(X)\right)<N
\right)
\le
\min\!\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}
\le
\min\!\left\{1,D\left(\frac1p+\frac1q\right)\right\}.
\tag{0.3}
\]

The polynomials may jointly depend on every sample coordinate.  Determinants,
Gram minors, cross-sample resultants after expansion, and entries of
noncommutative products are included whenever their total formal degree is
the displayed \(D\).  No independence among the \(s\) local zero events is
asserted or used.  Nevertheless, multiplication combines them only by OR on
each field side; CRT independence then turns the two local OR events into an
XOR.

There is also an exact four-case formal-identity alternative.  If a reduction of some
\(F_j\) is the zero formal polynomial over one prime field but not the other,
every integer coefficient of \(F_j\) is divisible by one of \(p,q\), while
not all are divisible by the other.  Hence the coefficient content of
\(F_j\) already contains a proper factor of \(N\).  For an explicit
polynomial-size coefficient representation with polynomial-bit coefficients,
that factor is deterministically extractable in polynomial bit complexity.
A nonzero formal polynomial such as \(T^r-T\) may nevertheless define the
zero function on \(\mathbb F_r\); it remains in the Schwartz--Zippel branch,
where its characteristic-scale degree makes the upper bound equal to one.

On balanced semiprimes, if \(D=\operatorname{poly}(\log N)\), (0.3) is
exponentially small in the input length.  An inverse-polynomial success bound
inside this model therefore requires either

1. total formal degree \(D\ge \sqrt N/\operatorname{poly}(\log N)\);
2. a characteristic-specific coefficient collapse; or
3. a source or decoder outside the theorem.

The first escape is real: repeated squaring in a branch-free division-free
circuit and succinct products can have exponential degree.  F02's
exponentially pooled-product problem lives exactly there.  Thus this result
distinguishes a genuine high-degree pooling mechanism from a low-degree
repackaging of one fully affine uniform batch; it does not declare all
amortization impossible.

## 1. Exact CRT experiment

Choose the standard representatives of \(X_i\) only to evaluate the integer
polynomials; divisibility of the result by \(p\) or \(q\) depends solely on
the corresponding residue.  CRT gives a probability-space isomorphism

\[
(\mathbb Z/N\mathbb Z)^k
\simeq
\mathbb F_p^k\times\mathbb F_q^k.
\tag{1.1}
\]

Consequently \(X_p\) and \(X_q\) are independent uniform vectors.  Write

\[
f_{j,r}=F_j\bmod r
\in\mathbb F_r[X_1,\ldots,X_k]
\qquad(r=p,q).
\tag{1.2}
\]

Formal reduction does not increase total degree.  Constant nonzero
polynomials have degree zero and no roots, so they cause no exceptional case
in the bounds below.

## 2. One polynomial zero test using a joint batch

The Schwartz--Zippel lemma over a finite field states that a nonzero
polynomial \(f\in\mathbb F_r[X_1,\ldots,X_k]\) of total degree \(d\) obeys

\[
\Pr_{Z\sim\operatorname{Unif}(\mathbb F_r^k)}[f(Z)=0]
\le \frac d r.
\tag{2.1}
\]

The right side may exceed one, in which case the inequality is merely loose.
No assumption \(d<r\) is needed for validity; that inequality is needed only
for a useful sparse conclusion.  In particular, a nonzero formal polynomial
may vanish as a function on all of \(\mathbb F_r^k\); \(T^r-T\) is the
smallest example.  Schwartz--Zippel still applies, but only with the vacuous
bound \(r/r=1\).  Such a zero function is not a coefficient-content collapse.

For one public joint polynomial \(F\) whose two reductions are nonzero, put

\[
\alpha_r=\Pr[f_r(X_r)=0].
\]

The proper-gcd event is exactly the exclusive-or of the two local zero events.
Using their CRT independence gives the exact formula

\[
\Pr(1<\gcd(N,F(X))<N)
=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).
\tag{2.2}
\]

In particular, writing \(\delta_r=\deg(f_r)\),

\[
\Pr(1<\gcd(N,F(X))<N)
\le \alpha_p+\alpha_q
\le \frac{\delta_p}{p}+\frac{\delta_q}{q}
\le \deg(F)\left(\frac1p+\frac1q\right).
\tag{2.3}
\]

Every coordinate of the batch may occur in \(F\), but (2.2) remains only the
XOR of two polynomial-zero events.  Calling this a genuine joint decoder
would overstate what the theorem analyzes.

## 3. Several outputs and one terminal gcd

Put

\[
P=\prod_{j=1}^sF_j.
\]

Under the standing nonidentity hypothesis define

\[
\delta_{j,r}=\deg f_{j,r},\qquad
\Delta_r=\sum_j\delta_{j,r}.
\]

Reduction can lower degree, so \(\Delta_r\le D\) can be strict.  Because a
polynomial ring over a field is an integral domain, the reduced product is
nonzero, has degree exactly \(\Delta_r\), and

\[
P(X_r)=0
\quad\Longleftrightarrow\quad
f_{j,r}(X_r)=0\text{ for at least one }j.
\tag{3.1}
\]

Hence, with \(\alpha_r=\Pr[P(X_r)=0]\), either Schwartz--Zippel on
the product or a union bound on its factors gives

\[
\alpha_r\le u_r:=\min\!\left(1,\frac{\Delta_r}{r}\right).
\tag{3.2}
\]

The two product-zero events are independent because each is a function of a
different independent CRT component.  Therefore their exact XOR probability
is

\[
\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\tag{3.3}
\]

The bilinear expression in (3.3) takes its maximum over
\([0,u_p]\times[0,u_q]\) at a corner.  Its four corner values are
\(0,u_p,u_q,u_p+u_q-2u_pu_q\), proving (0.2); the union bound proves
(0.3).  If \(u_p,u_q\le1/2\), the last corner is maximal, so in particular
\(D\le\min(p,q)/2\) yields the sharper valid bound

\[
\Pr(1<\gcd(N,P(X))<N)
\le \frac Dp+\frac Dq-\frac{2D^2}{pq},
\tag{3.4}
\]

with the sharper local-degree version obtained by replacing \(D/r\) with
\(\Delta_r/r\).  The proof allows one \(F_j\) to use the entire transcript
and allows the different \(F_j\)'s to share all variables.  Independence
among the alleged relations or output polynomials is never used; (3.1) is
precisely a local OR.

The same proof applies to a randomized coefficient family \(\Theta\) chosen
independently of \(X\), but only after conditioning on \(\Theta\).  If almost
every supported choice has nonzero formal reductions over both fields, then

\[
\Pr(1<\gcd(N,P_\Theta(X))<N)
=\mathbb E_\Theta[
  \alpha_p(\Theta)+\alpha_q(\Theta)
  -2\alpha_p(\Theta)\alpha_q(\Theta)].
\tag{3.5}
\]

Shared coefficient randomness can correlate the two conditional root
probabilities, so multiplying unconditional marginals would be invalid.  A
uniform local-degree budget \(\Delta_r(\Theta)\le B_r\) permits the envelope
\(\Psi(\min(1,B_p/p),\min(1,B_q/q))\).  Random integrable budgets always
permit the linear estimate

\[
\Pr(\text{proper gcd})
\le\mathbb E\!\left[
  \frac{\Delta_p(\Theta)}p+\frac{\Delta_q(\Theta)}q
\right].
\tag{3.6}
\]

A supported formal identity instead belongs to the pointwise four-case table
in Section 4 and cannot be averaged silently into the nonidentity theorem.

More generally, suppose successive **fresh** jointly uniform affine CRT
batches are used and the polynomial for the next batch may depend on all
earlier batches.  Conditional on each reachable history, the next batch is
still uniform, but the specialized polynomial in its fresh variables must
have nonzero formal reductions over both fields.  Conditional
Schwartz--Zippel followed by a union bound over a polynomial number of rounds
then charges the uniform or expected sum of the conditional actual reduced
degree budgets.
This does not cover choosing a polynomial after inspecting the same point on
which it is evaluated.  Indeed, after observing \(X=a\), the selector
\(F_a(T)=T-a\) has degree one but vanishes certainly at \(T=X\).  A
branch-free global symbolic polynomial may instead be analyzed at its actual
global degree.

## 4. The coefficient-content dichotomy

For an integer polynomial in collected canonical form, define its content by

\[
c(F)=\gcd\{|a|:\ a\text{ is an integer coefficient of }F\},
\tag{4.1}
\]

with \(c(0)=0\).  Formal reduction \(F\bmod r\)
is the zero polynomial exactly when \(r\mid c(F)\).

Suppose \(F\bmod p=0\) but \(F\bmod q\ne0\).  Then

\[
p\mid c(F),\qquad q\nmid c(F),
\]

and hence

\[
\gcd(N,c(F))=p.
\tag{4.2}
\]

The symmetric case yields \(q\).  If both reductions vanish, \(N\mid c(F)\)
and the identity is synchronized rather than separating.  If neither
vanishes, Sections 2--3 apply.

Because polynomial rings over fields are integral domains, define

\[
Z_r=\{j:f_{j,r}\text{ is the zero formal polynomial}\}.
\]

When \(Z_r=\varnothing\), retain the definition
\(\alpha_r=\Pr[P(X_r)=0]\).  The exact behavior of the **product gcd** is:

| \(Z_p\) | \(Z_q\) | exact proper-gcd probability |
|---|---|---|
| empty | empty | \(\alpha_p+\alpha_q-2\alpha_p\alpha_q\) |
| nonempty | empty | \(1-\alpha_q\) |
| empty | nonempty | \(1-\alpha_p\) |
| nonempty | nonempty | \(0\) |

Thus Sections 2--3 apply only in the first row.  In either middle row an
individual factor is a mixed formal identity and its explicit content factors
\(N\), although the displayed product gcd succeeds only when the other side
does not also vanish on the sampled point.  In the last row the product is
formally zero over both fields and its gcd is always \(N\).  This synchronized
product may come from one factor zero over both, or from different
one-sided-zero factors.  For example, \(F_1=p\) and \(F_2=q\) each exposes a
proper factor separately, while their product is \(N\) and never does.
Individual contents must therefore be inspected before multiplication.

For a canonical sparse or dense list of at most \(\operatorname{poly}(n)\)
coefficients, each of at most \(\operatorname{poly}(n)\) bits, (4.1)--(4.2)
are computed by ordinary integer gcds in polynomial bit complexity.  This
does not imply a low degree for a sparse representation: binary-encoded
exponents can be exponentially large even when the term list is short.  This
algorithmic conclusion is intentionally not asserted for a succinct
arithmetic circuit with exponentially many expanded monomials.  Extracting
the content after cancellations may itself be difficult, and the circuit can
also carry exponential formal degree.  The structural dichotomy remains
true, but it is not a circuit lower bound or an automatic factoring algorithm.
Circuit language below always means a branch-free division-free arithmetic
circuit and its actual formal degree; polynomial circuit size alone supplies
no degree bound.

### Formal zero versus zero function

A formal polynomial \(H\in\mathbb F_r[X_1,\ldots,X_k]\) induces the zero
function on \(\mathbb F_r^k\) exactly when

\[
H\in (X_1^r-X_1,\ldots,X_k^r-X_k).
\tag{4.3}
\]

Indeed, division by these monic polynomials gives a unique remainder of
individual degree below \(r\) with the same values, and induction on the
variables shows that such a remainder vanishes everywhere only when it is
formally zero.  Hence formal nonzero does not imply functional nonzero:
\(X_1^r-X_1\) is the basic counterexample.  This is consistent with
Schwartz--Zippel, whose total-degree bound is then the vacuous value one.
Conversely, if every individual degree is below \(r\), formal and functional
zero coincide even when total degree exceeds \(r\).

## 5. Examples of what the degree budget covers

The following common pooling operations stay inside the theorem.

1. **Linear pooling.**  A locally nonconstant affine-linear combination of all
   sample coordinates has zero probability exactly \(1/r\) at a local field;
   a nonzero constant has probability zero and the zero polynomial is the
   identity case.  Adding more inputs does not increase the degree.
2. **Polynomial-size products.**  Multiplying \(K\) scalar tickets gives total
   degree equal to the sum of their degrees.  This is algebraically the same
   union of rare zero sets even though it ends in one gcd.
3. **Determinants and Gram minors.**  A determinant of a \(t\times t\) matrix
   of linear transcript entries has degree at most \(t\); a Gram determinant
   has degree at most \(2t\).  Joint dependence among all rows does not change
   the root bound.  A formal-zero determinant belongs to Section 4, while a
   nonzero formal determinant that is only a zero function remains covered
   with a possibly vacuous characteristic-scale degree bound.
4. **Matrix and noncommutative products.**  An entry of a product of \(K\)
   matrices whose entries are linear in their respective samples has degree at
   most \(K\).  Noncommutativity changes the polynomial's coefficients, not
   the Schwartz--Zippel argument for a fixed scalar entry.
5. **Polynomially many minors or coordinates.**  Taking one terminal gcd of
   \(N\) with their product charges the sum of all formal degrees.  A rank-drop
   event defined by simultaneous vanishing is no more likely than the
   vanishing of any one locally nonzero defining minor.  The chosen nonzero
   defining minor may differ between \(p\) and \(q\); if no such minor exists
   in one characteristic while one exists in the other, the formal
   coefficient-content branch applies.

These examples explain why a fully jointly uniform affine polynomial batch is
not by itself an amortization theorem.  Uniform marginals do not suffice: if
\(X_1=X_2=U\) for one uniform \(U\), both coordinates are uniform while
the degree-one polynomial \(X_1-X_2\) vanishes surely.  A successful joint
construction must be analyzed by what information its combined observable
retains, not by how many relations were fed into it.

## 6. Balanced asymptotic threshold

Fix a balance constant \(\kappa\) and suppose

\[
p\le q\le\kappa p.
\]

Then \(p,q=\Theta(\sqrt N)\), so (0.3) gives

\[
\Pr(\text{proper terminal gcd})
\le O_\kappa\!\left(\frac D{\sqrt N}\right).
\tag{6.1}
\]

If \(D\le n^A\) for a fixed \(A\), the right side is

\[
2^{-n/2+O(\log n)},
\tag{6.2}
\]

where \(n=\lceil\log_2(N+1)\rceil\).  Conversely, within the nonidentity
model, an asserted success probability at least \(n^{-B}\) is compatible
with (6.1) only if

\[
D=\Omega_\kappa(\sqrt N/n^B).
\tag{6.3}
\]

This is a necessary degree scale, not a sufficient construction.  A
polynomial-size branch-free division-free arithmetic circuit may reach it:
repeated squaring can double formal degree at each multiplication, and a
succinct product can represent exponentially many zero tickets.  Evaluating
such a circuit is therefore the material escape, not a contradiction to the
theorem.  Whether its local exclusive-or mass is large and whether it has a
shared factor-free evaluator remain separate proof obligations.

## 7. Exact scope and reopen condition

The theorem assumes full affine uniformity of the CRT variables.  It does not
automatically apply to uniform projective lines, conics, conditioned
four-square fibres, low-dimensional codes, or any biased arithmetic source;
those require their own zero-count theorem.  It also does not cover:

- comparisons of integer magnitudes, nearest-vector rules, order statistics,
  or other metric branches;
- division or inversion paths on which a nonunit is encountered (that failure
  already exposes a factor and must be analyzed directly);
- an exponentially large adaptive branch family;
- rational functions without separately controlling denominator-zero events.

Characteristic-scale nonzero formal polynomials and high-degree branch-free
division-free circuits are structurally covered at their actual formal degree.
For them (0.3) may be vacuous, so the low-degree sparse obstruction gives no
useful exclusion; in a succinct-circuit formal-identity branch it also gives
no automatic polynomial-time coefficient-content extractor.

The exact local-product obstruction is:

> For a full jointly uniform affine CRT batch, a product of explicit
> polynomial zero tests with nonzero local formal reductions pays its
> aggregate actual degree in the component-selective-zero probability.
> Polynomially many variables and polynomial total degree still give
> exponentially small mass on balanced semiprimes.

This is not genuine joint decoding.  Locally the product is a
cancellation-free OR of rare zero tickets, and CRT turns the two local OR
events into an XOR.  A genuine decoder would instead have to combine
information carried by typical nonzero evaluations (or evaluate a
characteristic-scale pooled observable succinctly).  Such a mechanism is
outside this result.

A retry is materially new only if it supplies a factor-free source with a
proved nonuniform zero law, an explicit characteristic-selective identity, a
succinct exponential-degree evaluator with an inverse-polynomial XOR theorem,
or a nonalgebraic joint decoder whose information is not a polynomial zero
event.  Merely replacing a list of polynomially many scalar gcds by their
product, determinant, or another polynomial-degree contraction is covered.
