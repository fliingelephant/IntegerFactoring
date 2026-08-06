# F35 hostile audit: the structural theorem is sound, but the sampler-level conclusion overclaims

**Audit verdict: FAIL AS WRITTEN.**

The core distinct-semiprime theorem is correct: under the stated strict
low-degree hypothesis, a polynomial bijection of the finite zero-product set
has a preserve/swap orientation in each CRT field; mixed orientations expose a
factor coefficientwise; and synchronized orientations preserve the stated
factor-free region.  The circuit truncation, small-factor scan, characteristic-
two handling, cardinality, and total-variation calculation also survive.

The exact submitted version nevertheless fails because Section 7 says that
the result **refutes an all-input zero-product sampler** merely from the move
model and an initializer with no independently useful mass.  That does not
follow.  A sampler may use a mixed-orientation move, in which case the audit
extracts a factor; this is a factoring reduction, not a contradiction or a
nonexistence proof.  The right conclusion is the quantitative factor-or-TV
dichotomy proved below.  The all-input sentence must be replaced,
not just softened stylistically.

There are also required precision repairs concerning the uniform degree and
circuit quantifiers, the boundary between adaptive selection and a piecewise
map, and the warm-start/Las-Vegas sentence.  None refutes the local algebraic
lemma, but all are needed before a corrected version can be reconstructed.

**Audited artifact:**
`experiments/F35_low_degree_zero_product_bijection_kill/RESULT.md`.

**Materials checked:** `PROMPT.md`; the F23 row of `REGISTRY.md`; P40 in
`PROVED.md`; and the F34 candidate, hostile audit, and reconstruction.  This
was the preregistered proof-only route.  No mathematical computation or finite
experiment was used, and the candidate was not edited.

## 1. Decisive finding: “refutes a sampler” is false without a factor-free premise

Put

\[
B_N=\Omega_N\setminus\mathcal A_N,
\qquad
\rho_N=\frac{|B_N|}{|\Omega_N|}
=\frac{2N-2}{(2p-1)(2q-1)}>\frac12.
\]

The proved pathwise statement is:

* if the initial state lies in \(\mathcal A_N\), and
* no inspected restriction coefficient has a proper gcd with \(N\),

then every realized move is orientation-synchronized and every later state
lies in \(\mathcal A_N\).  This is valid.

It does **not** say that an accurate sampler in this class cannot exist.  The
other branch of the theorem is that a coefficient reveals a factor.  That
branch is entirely compatible with a sampler existing, especially in a
factoring project.  Indeed, if \(e_p,e_q\in R\) are the complementary CRT
idempotents, then

\[
T(K,X)=
\bigl(e_pK+e_qX,\ e_pX+e_qK\bigr)
\]

is a degree-one bijection of \(\Omega_N\).  It preserves the axes modulo
\(p\), swaps them modulo \(q\), and has coefficients whose gcds reveal
\(p\) and \(q\).  Mixed low-degree bijections therefore exist; the theorem
shows that constructing one explicitly has already encoded a factor.  It
does not rule out an algorithm which obtains or discovers that factor.

The phrase “whose initializer has no independently useful mass” does not fix
the implication: even with a deterministic initializer in \(\mathcal A_N\),
the later maps may be factor-visible with constant probability.  Nor is the
conditional law on the “no-factor branch” the unconditional output law that a
sampler is normally required to approximate.  If the no-factor event has
small or zero probability, its conditional TV distance gives no contradiction
to an accurate unconditional sampler; when that event has probability zero,
the conditional law is not even defined.

### Exact replacement consequence

Monitor a realized run as follows.

1. At initialization, take gcds of both coordinates with \(N\).
2. Before every move, extract and gcd all four axis-restriction coefficient
   lists as in the candidate.

Let \(H\) be the event that one of these checks returns a proper factor.  On
\(H^c\), the initial state is in \(\mathcal A_N\), every move synchronizes,
and hence the terminal state is in \(\mathcal A_N\).  Thus, for every finite
or almost-surely finite stopping rule,

\[
\{Z_{\rm out}\in B_N\}\subseteq H.
\tag{1.1}
\]

If \(\mu\) is the unconditional terminal law and
\(d_{\rm TV}(\mu,\pi_N)\le\delta\), then

\[
\Pr(H)\ \ge\ \mu(B_N)
\ \ge\ \pi_N(B_N)-\delta
\ =\rho_N-\delta.
\tag{1.2}
\]

Equivalently,

\[
d_{\rm TV}(\mu,\pi_N)\ge \rho_N-\Pr(H).
\tag{1.3}
\]

This is the correct sampler-level theorem.  In particular:

* if the run is genuinely factor-free, \(\Pr(H)=0\), then its output is more
  than \(1/2\) from uniform;
* if \(\Pr(H)\) is negligible, its TV error is at least
  \(1/2-o(1)\); and
* if its TV error is at most a fixed \(\delta<1/2\), the monitor finds a
  factor with probability at least \(1/2-\delta\) (strictly more here).

For example, a TV-\(1/28\) sampler would expose a factor with probability
greater than \(13/28\) on every distinct-semiprime input to which the move
model applies.  Subject to the uniform runtime conditions in Section 7 below,
fresh repetition gives a Las Vegas **distinct-semiprime splitter**.  This is a
strong reduction, but it neither refutes the sampler nor by itself proves an
all-input factoring algorithm.

This logical overclaim is the reason for the FAIL AS WRITTEN verdict.

## 2. CRT-local bijectivity: pass

Let \(R\simeq\mathbf F_p\times\mathbf F_q\).  Applying CRT to both
coordinates gives the exact set product

\[
\Omega_N\simeq\Omega_p\times\Omega_q,
\qquad
\Omega_r=\{(a,b)\in\mathbf F_r^2:ab=0\}.
\]

For fixed polynomials \(F,G\in R[K,X]\), evaluation commutes with the two
coefficient projections.  Hence the global point map is exactly

\[
T=T_p\times T_q.
\]

Each \(T_r\) maps \(\Omega_r\) into itself: pair an arbitrary local point
with the origin in the other CRT component, lift it to \(\Omega_N\), and
reduce the zero-product global image.  This uses neither a factor algorithm
nor a coordinate-ring automorphism.

If \(T_p\) were noninjective, holding any \(q\)-component fixed would give a
global collision; similarly for \(T_q\).  If either local map omitted a
point, the product map would omit every global point with that local
component.  Therefore global bijectivity is equivalent here to bijectivity of
both local maps.  No hidden independence or surjectivity assumption occurs.

The extra closing parenthesis in the candidate's sentence
“\(T_p\times T_q\))” is only a typo.

## 3. Pointwise zero product versus a formal identity: pass, and the threshold is essential

On either source axis and over either field, write the two coordinate
restrictions as \(f,g\in\mathbf F_r[Z]\).  Because the point map lands in
\(\Omega_r\),

\[
f(t)g(t)=0\qquad(t\in\mathbf F_r).
\]

The formal product has

\[
\deg(fg)\le \deg f+\deg g\le 2D<r.
\]

A nonzero polynomial of degree below \(r\) cannot have all \(r\) field
elements as roots.  Hence \(fg=0\) as a formal polynomial.  Since
\(\mathbf F_r[Z]\) is a domain, \(f=0\) or \(g=0\).  This proves that each
whole source axis enters one target axis.  It is valid in every
characteristic.

There is no polynomial-function loophole below the strict degree-sum bound.
At the boundary there is one.  For any nontrivial partition
\(\mathbf F_r=A\mathbin{\dot\cup}B\),

\[
f(Z)=\prod_{a\in A}(Z-a),
\qquad
g(Z)=\prod_{b\in B}(Z-b)
\]

are both formally nonzero, have \(\deg f+\deg g=r\), and satisfy

\[
f(Z)g(Z)=Z^r-Z
\]

as a polynomial, hence have pointwise-zero product.  Thus the natural local
hypothesis really is

\[
\deg f+\deg g<r;
\]

the candidate's uniform sufficient condition \(2D<r\) is sound but not a
necessary formulation.

There are also genuine characteristic-scale non-oriented bijections, not just
pointwise-zero pairs.  For \(r\ge3\), let

\[
\delta_1(Z)=1-(Z-1)^{r-1}.
\]

On \(\Omega_r\), exchange the two points \((1,0)\) and \((0,1)\) and fix
every other point.  Its coordinate restrictions are

\[
\begin{array}{c|cc}
&F&G\\ \hline
(Z,0)&Z-\delta_1(Z)&\delta_1(Z)\\
(0,Z)&\delta_1(Z)&Z-\delta_1(Z),
\end{array}
\]

which agree at the common origin and combine into bivariate polynomials of
total degree at most \(r-1\).  This permutation splits each source axis
between target axes and is outside the candidate's low-degree regime.  It
confirms that characteristic-scale finite-set permutations must remain an
explicit escape.  It is not a counterexample to the stated theorem.

## 4. Distinct target axes and the origin: pass

The restriction of an injective \(T_r\) to a source axis is injective.  It
cannot collapse that \(r\)-point axis to the origin.  Once root counting
places both source axes in target axes, they also cannot both enter the same
target axis: their union is all of \(\Omega_r\), while a target axis has
only \(r\) points and

\[
|\Omega_r|=2r-1>r.
\]

Equivalently, each restricted injection into an \(r\)-point target axis is
already a bijection, so two such images cannot both be the same axis without
global collisions.  The source origin belongs to both source axes, and its
image therefore belongs to both distinct target axes.  Their intersection is
the target origin, proving

\[
T_r(0,0)=(0,0).
\]

Consequently every nonzero point of a source axis maps to a nonzero point of
its selected target axis.  This proof does not assume linearity of the
one-variable permutation polynomial.

## 5. Mixed orientation and coefficientwise gcd extraction: pass

Suppose the \(p\)-map preserves axes and the \(q\)-map swaps them.  Then,
as formal univariate polynomials,

\[
\begin{array}{c|cccc}
&F(K,0)&G(K,0)&F(0,X)&G(0,X)\\ \hline
\bmod p&\ne0&0&0&\ne0\\
\bmod q&0&\ne0&\ne0&0.
\end{array}
\]

For example, all coefficients of \(F(K,0)\) vanish modulo \(q\), while at
least one is nonzero modulo \(p\).  Any integer lift \(c\) of that residue
coefficient satisfies

\[
\gcd(c,N)=q.
\]

There is no cancellation ambiguity: “nonzero formal polynomial” means that
at least one already-collected coefficient is nonzero.  Reversing the mixed
orientation reverses \(p,q\).  Therefore every mixed orientation supplies a
proper coefficient gcd.

The converse used by the obstruction is only that absence of every proper
coefficient gcd rules out a mixed orientation.  It is correct.  A
synchronized map may still have a one-sided coefficient and reveal a factor;
the alternatives are not exclusive, but the no-factor implication remains
valid.

## 6. Truncated straight-line-circuit extraction: pass under explicit quantifiers

Let a division-free straight-line circuit over \(R\), with explicit residue
constants and \(+,-,\times\) gates, compute the exact formal output
polynomials \(F,G\).  Substitute \((K,X)=(Z,0)\), respectively \((0,Z)\),
and evaluate the circuit in

\[
R[Z]/(Z^{D+1}).
\]

The quotient projection is a ring homomorphism even though \(R\) has zero
divisors.  Therefore arbitrary high-degree intermediate terms and arbitrary
internal cancellations do not corrupt any coefficient of degree at most
\(D\).  If the exact final formal output has degree at most \(D\), its
remainder modulo \(Z^{D+1}\) is the entire restriction.  This directly
answers the cancellation concern.

Storing \(D+1\) reduced residues and using ordinary convolution costs
\(O(D^2)\) ring operations per multiplication gate and less per additive
gate.  Evaluating both substitutions for a two-output circuit of \(s\) gates
therefore costs \(O(sD^2)\) ring operations up to a constant factor.  Modular
reduction keeps every stored residue at \(O(\log N)\) bits.  The subsequent
\(4(D+1)\) integer gcds are polynomial-time.

The following qualifications must be stated in the candidate's theorem, not
left implicit:

1. The circuit must compute those exact low-formal-degree polynomials.  It is
   insufficient that the same point function happens to admit some unknown
   low-degree representative while the submitted circuit's formal output has
   characteristic-scale degree.
2. The bound \(D\) is a public **numeric** bound and, for a uniform
   polynomial-time claim, is bounded by one fixed polynomial in
   \(n=\lceil\log_2(N+1)\rceil\), independently of the input, random seed,
   history, step, and stopping time.  Saying separately of each realization
   that its degree is “polynomial” is not a uniform bound.
3. Let \(L\) denote total circuit encoding length, including all constant bit
   strings, rather than calling \(s\) both encoded size and gate count.  The
   bit bound is polynomial in \(L+D+n\), and is polynomial in \(n\) only
   under the corresponding uniform bounds.
4. Both the global-bijection property and the final formal-degree property are
   semantic promises supplied by the sampler's proof.  This extractor does
   not certify either promise.

The malformed `+ ext{the encoded constant length}` in equation (4.3) also
needs typographical repair.

This extraction is consistent with P40.  P40 asserts no coefficient-content
extractor for an arbitrary succinct high-actual-degree circuit.  F35 can
expand the restrictions only because the public numeric degree cap makes the
truncated coefficient vector polynomially long.  Sparse powers and
repeated-squaring circuits of characteristic-scale degree remain outside
F35.

## 7. Trial division, bit assumptions, and characteristic two: pass with a uniformity repair

On a distinct semiprime \(N=pq\), sequentially computing
\(\gcd(N,j)\) for

\[
j=2,3,\ldots,2D
\]

finds a proper factor if either prime is at most \(2D\): the scan reaches
that prime before it can reach a multiple of both distinct primes.  If every
gcd is trivial, then \(p,q>2D\), which is exactly the strict root-counting
condition.  The scan costs \(O(D)\) gcds and is polynomial in \(n\) only
under the fixed numeric bound from Section 6.

Characteristic two causes no algebraic exception.  If one factor is \(2\)
and \(D\ge1\), the first scan entry finds it.  If \(D=0\), then
\(2D<2\) already, and the field proof remains valid (indeed constant
coordinates cannot give the hypothesized bijection of \(\Omega_2\)).  The
TV count also remains strict for \(\{p,q\}=\{2,3\}\).

For an adaptive expected-polynomial-time monitor, the report should also
state the total-cost condition.  If the realized circuits have gate counts
\(s_i\), a uniform \(D\le P(n)\), and
\(\mathbb E[\sum_i s_i]\le Q(n)\), then the expected extraction overhead is
at most a polynomial multiple of \(P(n)^2Q(n)\).  A per-move statement alone
does not establish the total expected bit bound of an unbounded adaptive run.

## 8. Adaptive and state-dependent mixtures: the invariant passes, but the model boundary must be explicit

For every realized history, freeze the selected circuit and its explicit
constants.  If that circuit is a global low-degree bijection of all
\(\Omega_N\), the one-move theorem applies.  If no coefficient gcd is
proper, it maps \(\mathcal A_N\) to itself.  Induction is pathwise, so no
independence, stationarity, reversibility, time homogeneity, or fixed choice
distribution is needed.  Selection may depend on the current state, the
whole public transcript, and fresh randomness.

The candidate simultaneously says this and excludes “state-wise branching
programs.”  The intended boundary needs this exact wording:

* **covered:** a state-dependent selector which materializes, at each realized
  history, an explicit circuit that is itself promised to be a global
  bijection of \(\Omega_N\); and
* **not covered:** a piecewise aggregate transformation
  \(z\mapsto T_z(z)\) which is bijective only after stitching branches
  together, when the individual branch circuit \(T_z\) is not a promised
  global bijection, or when no extractable global circuit is materialized.

Without this distinction, “arbitrary state-dependent mixtures” can be read
as covering the excluded piecewise model.  This is a scope repair, not a
counterexample to the pathwise invariant in the covered model.

## 9. Warm starts: the structural statement passes; the Las Vegas wording must be narrowed

For \(z\in R\) with \(N=pq\), a gcd fails to be proper exactly when \(z\)
is a unit or zero.  If \((k,x)\in\Omega_N\) and both coordinates have this
property, the product constraint rules out two units.  The point is therefore
one of

\[
(R^\times,0),\quad(0,R^\times),\quad(0,0),
\]

namely it lies in \(\mathcal A_N\).  Conversely those points reveal no
proper coordinate gcd.  Hence membership in \(B_N\) is exactly the event
that at least one coordinate gcd is proper.

Thus an initializer with outside mass \(\varepsilon_N\) exposes a factor
with exactly that probability when both coordinate gcds are checked.  A
freshly repeatable, polynomial-expected-cost initializer with a uniform
lower bound \(\varepsilon_N\ge1/P(n)\) gives a Las Vegas splitter on the
distinct-semiprime subfamily.  The candidate should not call this an
unqualified “Las Vegas factoring route”: it has not handled arbitrary
composites, and the repeatability, cost, and uniform success lower bound are
part of the claim.

The inverse-polynomial/negligible prose is also not a clean exhaustive
dichotomy for arbitrary input-indexed success probabilities.  Equation
(1.2) is both sharper and fully quantitative; it should replace that prose.
When all selected maps synchronize, membership in \(\mathcal A_N\) is in
fact preserved exactly, so the outside mass is unchanged, not amplified.

## 10. Cardinality and total variation: pass

Each local zero-product set is two \(r\)-point axes meeting once, so

\[
|\Omega_N|=(2p-1)(2q-1).
\]

The three disjoint pieces of \(\mathcal A_N\) have size

\[
|\mathcal A_N|=2(p-1)(q-1)+1.
\]

The difference is

\[
|B_N|=(2p-1)(2q-1)-2(p-1)(q-1)-1=2pq-2=2N-2.
\]

Moreover,

\[
2|B_N|-|\Omega_N|=2p+2q-5>0
\]

for distinct primes, including \(2,3\).  Therefore \(\rho_N>1/2\).  If a
law is supported on \(\mathcal A_N\), the event \(B_N\) witnesses TV
distance at least \(\rho_N>1/2\).  All displayed counts and the strict
inequality are correct.

## 11. Relation to F34 and exact all-input scope

The comparison with F34 needs one precision correction.  Over a distinct
semiprime, F34 proves that every coordinate-algebra automorphism has an exact
linear scaling/swap point action.  What F34 allows to have arbitrarily high
degree is the **submitted circuit or polynomial representative**, from which
it extracts only the intrinsic first jet.  F35 covers a semantically larger
class of finite-set point bijections, but requires the submitted exact formal
outputs to have the public low-degree cap so their full axis restrictions can
be extracted.  The representation-level obstruction models are therefore
incomparable in that sense; saying simply that F34 “allows arbitrarily large
polynomial degree” obscures its exact linear semantic classification.

The distinct-semiprime restriction is legitimate for testing an all-input
proposal: an all-input sampler must also meet its claimed law and runtime on
every distinct semiprime.  But failure to stay factor-free on that subfamily
does not refute the sampler.  The exact conclusion is:

> On every distinct-semiprime input, after the small-factor scan, any sampler
> whose realized moves satisfy the explicit uniform low-degree global-
> bijection model obeys (1.2).  Hence it either exposes a factor with the
> stated probability or has the stated TV error.

No claim is proved for prime-power geometry, general nonsquarefree rings,
noninvertible kernels, high-degree succinct permutations, auxiliary-state
kernels, or nonmaterialized piecewise/opaque maps.  It is valid to say that
a **factor-free** all-input sampler confined to this move model is ruled out
on the distinct-semiprime subfamily.  It is not valid to say that every
all-input sampler in the move model is refuted.

## 12. Exact required corrections

Before this version can pass, the candidate must make all of the following
changes.

1. Replace Section 7's assertion that the theorem “refutes an all-input
   zero-product sampler” by the monitored factor-or-TV theorem (1.1)--(1.3).
   Reserve “refutes” for a sampler additionally promised to be factor-free
   (or give an explicit quantitative upper bound on the total detection event
   \(H\)).
2. Clarify that TV approximation refers to the unconditional terminal law.
   State the supported-on-\(\mathcal A_N\) result conditionally only when the
   no-factor event has positive probability.
3. State one fixed public numeric degree bound \(D\le P(n)\) uniform over all
   realized inputs, histories, random seeds, moves, and stopping times.  State
   that the submitted circuit computes the exact formal polynomials of that
   degree, not merely an equivalent finite-set function.
4. Separate gate count from total encoded bit length, repair equation (4.3),
   and state the total expected extraction overhead for an adaptive run.
5. State that both global bijectivity and the final formal-degree cap are
   promises justified by the proposed sampler, not properties certified by
   truncated evaluation.
6. Distinguish adaptive selection among materialized global bijection circuits
   from a piecewise/state-wise map whose branches are not themselves global
   promised bijections.
7. Replace the warm-start “Las Vegas factoring route” sentence by the exact
   distinct-semiprime statement with fresh repeatability, polynomial expected
   trial cost, and a uniform inverse-polynomial lower bound; preferably subsume
   it into (1.2).
8. Qualify the F34 comparison as a difference in submitted representation and
   semantic map class, and fix the two typographical errors identified above.

After correction 1, the sampler-level mathematical conclusion is genuinely
different from the audited version, so the failed-audit rule requires audit
of the amendment before proof-blind reconstruction.  No new proof is needed
for the core low-degree orientation theorem itself; every hostile check of
that theorem passed.
