# F40 candidate: bounded-degree fibre bias is diffuse, visibly asymmetric, or synchronized

**Status:** candidate kill-first theorem and counterexample. No hostile audit or
proof-blind reconstruction has run.

**Family:** F14, Hurwitz one-sided gcd and projective-orientation relations.

**Computation:** none. This is a proof-only artifact.

## 1. Exact question and model

Let

\[
N=pq,
\qquad A=\mathbb Z/N\mathbb Z,
\]

where \(p\ne q\) are odd primes, and let \(R\in A^\times\). At a local
prime \(r\in\{p,q\}\), write

\[
\chi_r=\left(\frac{-1}{r}\right),
\qquad
C^-_r=\{(x,y)\in\mathbb F_r^2:x^2+y^2=-R\},
\qquad
s_r=|C^-_r|=r-\chi_r.
\]

The source point is uniform on \(C^-_r\). Unlike P30, a completion may now
inspect that point. It returns

\[
(z,w)=\Phi_R(x,y),
\qquad z^2+w^2=R,
\]

and hence the rank-one local quaternion matrix belonging to

\[
\beta=x+yi+zj+wk.                                      \tag{1}
\]

When the line is passed through a Hurwitz gcd, retain P30's global hypotheses:
the auxiliary modulus is squarefree, \(\beta\) is primitive, and the one-sided
gcd has norm \(N\). Then the right-gcd output inherits the row line and the
left-gcd output inherits the image line. The local atom theorem itself needs
only \(R\ne0\), which makes (1) a nonzero rank-one matrix.

There are two bounded-degree representations to which the result below
applies.

1. **Rational branches.** Branch \(b\) is supplied by homogeneous forms
   \(Z_b,W_b,H_b\in A[X,Y,T]\) of one common degree \(d_b\le D\), with

   \[
   Z_b^2+W_b^2=R H_b^2
   \quad\bmod (X^2+Y^2+RT^2).                           \tag{2}
   \]

   On its domain it returns \((Z_b/H_b,W_b/H_b)\). A denominator is inverted
   only after its gcd with \(N\) is checked. Thus a nonunit denominator either
   already returns a factor or is not an allowed no-factor execution. An
   equivalent affine input format of degree at most \(D\) is first homogenized
   to one common degree by powers of \(T\).

2. **Algebraic branches (local geometric version).** After reduction at a
   local prime \(r\), normalize every irreducible component
   \(\Gamma_{b,r,j}\) of the graph that the selector is allowed to use. The
   two conics are in their plane embeddings. Put

   \[
   a_{b,r,j}=\deg(\pi_-^*\mathcal O(1)|_{\Gamma_{b,r,j}}),
   \qquad
   c_{b,r,j}=\deg(\pi_+^*\mathcal O(1)|_{\Gamma_{b,r,j}}).
                                                               \tag{3}
   \]

   The advertised local degree budget \(E_r\) bounds the sum of
   \(a_{b,r,j}+c_{b,r,j}\), with scheme-theoretic multiplicities, over every
   selectable component of every displayed branch. Every selectable
   source-dominating component must have nonconstant induced line map;
   a constant source-dominating component is classified as a degeneration
   and is outside the nonconstant atom theorem. Vertical components are
   included in the same total-degree accounting. This is a genuinely
   multivalued local relation: a selector may choose any available graph
   point over the current source point. No claim is made here that such a
   graph or its local decomposition is globally computable without factors.

In either model the execution may choose arbitrarily among \(B\) displayed
branches as a function of the current fibre point. It must output on every
source point, using a branch defined there. Input-dependent rejection and
conditioning are not part of this model. A branch's formulas must be fixed
before the fresh source point is drawn; past-transcript-dependent choices are
allowed after conditioning on that past.

The degree-degeneration conclusion below needs one further, deliberately
explicit accessibility hypothesis. After a public parametrization of
\(\overline C^-\), the composed projective row or image map must be available
as a pair of homogeneous binary forms over \(A\). Supplying only an opaque
division/root circuit or a multivalued graph is not enough.

For every algorithmic rational/binary-form claim, all displayed degrees,
branch counts, coefficient-list lengths, and coefficient bit lengths are
assumed polynomial in \(n=\lceil\log_2N\rceil\). These assumptions make
evaluation, coefficient reduction, determinants, subresultants, and integer
gcds uniformly polynomial bit cost. They are essential; the word “degree” by
itself is not an algorithmic representation.

## 2. A nonconstant branch has small atoms

Fix \(r\mid N\). Choose, only for the local proof, \(s,t\in\mathbb F_r\)
with \(s^2+t^2=-1\). As in P30, split the Hurwitz algebra by

\[
i\longmapsto
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
j\longmapsto
\begin{pmatrix}s&t\\t&-s\end{pmatrix}.
\]

Put

\[
A_c=sz+tw,
\qquad B_c=tz-sw.
\]

Then (1) becomes

\[
\beta_r=
\begin{pmatrix}
x+A_c&y+B_c\\
-y+B_c&x-A_c
\end{pmatrix}.                                           \tag{4}
\]

For a rational branch, after clearing its denominator, its first row is
represented on \(\overline C^-\) by

\[
P_b=XH_b+T(sZ_b+tW_b),
\qquad
Q_b=YH_b+T(tZ_b-sW_b).                                  \tag{5}
\]

Both forms have degree at most \(D+1\). The row-line map extends uniquely
across the finitely many zero-first-row points because \(\overline C^-\) is a
smooth projective curve and \(\mathbb P^1\) is proper. The extension is also
the actual row line obtained from the second row of (4). If both forms in (5)
vanish identically on the conic, use the second row instead. Its two forms
cannot also vanish identically, since \(R\ne0\) makes \(\beta\) nonzero at
every source point. Thus the identically-zero chart, including the extreme
anti-isometry chart, does not escape the argument.

For a proposed line \(L=[u:v]\), every source point mapping to \(L\), including
a zero-first-row point, is a zero of

\[
vP_b-uQ_b.                                                \tag{6}
\]

If the projective row map is nonconstant, (6) is not identically zero on the
conic for any \(L\). Bézout therefore gives

\[
\#f_{b,r}^{-1}(L)\le 2(D+1).                              \tag{7}
\]

This count is over the algebraic closure and includes multiplicities, so it
already covers all rational exceptional points. Points at infinity can only
decrease the affine count. Poles at which the branch is not selected produce
no output; if another branch handles such a point, that point is charged to
the other branch.

The same proof applies to the image line, using the first column

\[
[\,XH_b+T(sZ_b+tW_b):-YH_b+T(tZ_b-sW_b)\,].             \tag{8}
\]

If that column vanishes identically, use the second column. Again both columns
cannot vanish identically.

There is an invariant local version for an algebraic component. On
\(\Gamma_{b,r,j}\subset\overline C^-\times\overline C^+\), the two
coordinates in (5) or (8), with the completion coordinate homogenized by its
own projective variable, are sections of \(\mathcal O(1,1)\). If the induced
line map is nonconstant on the normalization of a source-dominating
component, a point fibre is a proper hyperplane section and has degree at
most

\[
a_{b,r,j}+c_{b,r,j}.                                     \tag{9}
\]

Projecting the intersection to the source conic cannot increase the number of
distinct source points. This proves (9) even if the graph has several points
over a source point and the execution chooses among them. A vertical
component contributes only its finite source image and is charged to the same
positive total degree. Nonreduced components are charged with multiplicity.
A constant source-dominating component is not covered by (9).

Consequently, if every selectable rational branch (or selectable local graph
component) is nonconstant, an arbitrary point-dependent selector obeys the
following atom bounds. For the displayed probability-law notation in the
rational model, assume a unit-defined branch is selected at every source
point of the fixed failure transcript:

\[
\boxed{
\max_L\Pr(f_r(x,y)=L)
\le
\min\left(1,\frac{2B(D+1)}{r-\chi_r}\right)}              \tag{10}
\]

in the rational model, and

\[
\boxed{
\max_L\Pr(f_r(x,y)=L)
\le
\min\left(1,\frac{E_r}{r-\chi_r}\right)}                 \tag{11}
\]

in the corrected local algebraic-graph model. No independence of the branch
choice from the current point was used: the preimage of \(L\) is merely
contained in the union of the selectable component preimages.

If evaluation of a rational branch instead returns a factor because a
denominator is a proper zero divisor, the unconditional formulation is

\[
\Pr(\text{no-factor output with line }L)
\le \frac{2B(D+1)}{r-\chi_r}.                            \tag{11a}
\]

This is not silently renormalized after conditioning on the no-factor event.
Equivalently, (10) applies as a conditional distributional statement only
when a unit-defined branch is selected on every source point of the fixed
failure transcript.

The linear dependence on the actual projective degree is sharp. A degree-\(e\)
map \(\mathbb P^1\to\mathbb P^1\) can have a fibre of \(e\) distinct rational
points. Thus bounded degree gives \(O(D/r)\), not exact uniformity.

## 3. Fresh-call collisions and fixed exceptional targets remain sparse

Condition on the entire past transcript, so that the next call's displayed
maps are fixed before its fresh uniform source point. Let

\[
\mu_r=\min\left(1,\frac{2B(D+1)}{r-\chi_r}\right)         \tag{12}
\]

or use the right side of (11). Two outputs from fresh independent source
draws collide in the relevant local line with probability at most \(\mu_r\),
because after conditioning on the first line the second distribution has
maximum atom \(\mu_r\). More generally, the next branch list may be chosen
from the past transcript: after conditioning on that past, the new source
draw is fresh and the same bound applies. A fixed projective transform only
permutes the target lines; choosing after the draw among a displayed menu of
\(T\) transforms costs a factor \(T\). The probability of landing in the at
most fourteen nontrivial Hurwitz-unit stabilizer lines is at most
\(14\mu_r\).

It follows by conditioning and a union bound that polynomially many
past-predictable branch lists, fresh calls, cross-call pair comparisons,
fixed targets, displayed transform menus, and exceptional-stabilizer tests
still have probability

\[
O\!\left(\operatorname{poly}(n)\left(\frac1p+\frac1q\right)\right)            \tag{13}
\]

of producing one of these named rare-line tickets. On an infinite balanced
family this is exponentially small in \(n\).

Equation (13) says nothing about a nonlinear decoder that combines typical
nonzero values from many outputs. It also says nothing when a selectable
branch is constant: that omitted case is real, not a proof artifact. Most
importantly, it does not apply to two line maps evaluated on the same source
point. Two nonconstant maps can agree, or differ by a fixed projective
transform, identically; P31's relation
\(\operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta\) for one fixed
completion is an in-family example. Same-source row--image relations and
other coupled decoders require their own algebraic analysis.

## 4. One-sided degree degeneration is coefficient-visible under the stated representation

Here is the exact algebraic visibility statement. Suppose a labelled branch's
composed line map is supplied after parametrization as

\[
F=[P(U,V):Q(U,V)],                                        \tag{14}
\]

where \(P,Q\in A[U,V]\) are homogeneous of common degree
\(e=\operatorname{poly}(n)\). For \(r\in\{p,q\}\), if they are not both zero,
let

\[
\delta_r=e-\deg\gcd(P_r,Q_r)                              \tag{15}
\]

be the degree of the reduced local projective map. Homogenization includes a
degree drop at infinity; no leading-coefficient exception is being hidden.

If \(\delta_p\ne\delta_q\), a deterministic polynomial-size coefficient list
contains a proper zero divisor. Indeed, the homogeneous subresultant sequence
of \(P,Q\) determines \(\deg\gcd(P_r,Q_r)\) over every field. Since the two gcd
degrees differ, some subresultant coefficient (or an asymmetric
leading/content coefficient) is zero modulo exactly one of \(p,q\). For its
canonical integer lift \(c\),

\[
1<\gcd(c,N)<N.                                            \tag{16}
\]

All subresultants are fraction-free determinants of \(O(e)\)-dimensional
Sylvester matrices, and there are \(O(e^2)\) displayed coefficients. Thus
(16) is found in polynomial bit time without division modulo \(N\). If
\(P,Q\) vanish identically in exactly one component, an ordinary coefficient
content gcd already gives (16). Equivalently, one can dehomogenize in both
projective charts and use the two ordinary subresultant sequences.

In particular, “constant modulo \(p\), nonconstant modulo \(q\)” is visible.
The same argument detects any unequal reduced degrees, not just degree zero.
It applies branch by labelled binary-form pair. No corresponding visibility
theorem is claimed for a multivalued algebraic graph: an eliminant can mix
components and multiplicities, and a separate determinantal representation
theorem would be required.

A public parametrization does not require a square root or a factor. Given
one public point \((a,b)\in C^-(A)\), put

\[
\begin{aligned}
X&=a(U^2-V^2)-2bUV,\\
Y&=b(U^2-V^2)+2aUV,\\
T&=U^2+V^2.
\end{aligned}                                             \tag{17}
\]

Then

\[
X^2+Y^2=-RT^2,                                            \tag{18}
\]

and \(a^2+b^2=-R\in A^\times\) makes the three forms in (17) base-point-free
in both CRT components. Thus (17) parametrizes the projective conic over both
fields simultaneously. If the composed line coordinates themselves are not
available over \(A\) (for example, only a local split or an opaque algebraic
root circuit is known), (14) is an extra hypothesis rather than a consequence
of the word “completion.”

The same parametrization also gives an exact polynomial-time same-fibre
sampler once \((a,b)\) is known. Draw \((U,V)\) uniformly modulo \(N\), reject
only when \(\gcd(U,V,N)=N\), and return a factor if that gcd is proper. Then
test \(T=U^2+V^2\): return a factor when \(\gcd(T,N)\) is proper, reject when it
is \(N\), and otherwise divide \(X,Y\) by the unit \(T\). Every projective
parameter has exactly \(\varphi(N)\) unimodular representatives, so,
conditional on the no-factor affine branch, the resulting point is exactly
uniform on the CRT product of the two affine conics. Starting from uniform
vectors, the direct no-factor affine-output probability is exactly

\[
\prod_{r\in\{p,q\}}\frac{(r-1)(r-\chi_r)}{r^2},          \tag{18a}
\]

because the nonzero-vector step contributes \(1-1/r^2\) and the affine
fraction of the resulting projective conic is
\((r-\chi_r)/(r+1)\). This product is bounded below by an absolute constant
for distinct odd primes. Proper vector or \(T\)-gcds already factor \(N\);
simultaneous-zero cases are rejected. Hence neither a hidden factor nor
costly conditioning is needed to reuse one accepted residual, and standard
exact rejection from a power-of-two range keeps random-bit cost polynomial.

The qualification “exactly one CRT component” is essential. If
\(\delta_p=\delta_q\), all degree predicates can vanish or survive modulo both,
and their gcds are only \(N\) or \(1\). Equal degree does not mean equal local
values or equal local maps.

## 5. A degree-one constantizer refutes the naive atom claim

The excluded constant case occurs by a very simple, factor-free identity.
Work in the public Gaussian subalgebra \(A[i]\). Suppose one source point and
one completion for the same residual are already available:

\[
u_0=x_0+y_0i,
\quad
u_0\bar u_0=-R,
\qquad
c_0=z_0+w_0i,
\quad
c_0\bar c_0=R.                                            \tag{19}
\]

Because \(R\) is a unit, define publicly

\[
h=u_0^{-1}c_0=\frac{\bar u_0c_0}{-R}.                     \tag{20}
\]

No square root and no unknown-factor operation occurs. Its Gaussian norm is

\[
h\bar h=-1.                                               \tag{21}
\]

Now hold \(h\) fixed and, for every fresh \(u=x+yi\) on the same source fibre,
complete by

\[
c=\Phi_R(u)=uh=z+wi.                                      \tag{22}
\]

This is a degree-one linear completion and

\[
c\bar c=(u\bar u)(h\bar h)=R.                             \tag{23}
\]

More importantly,

\[
\beta(u)=u+(uh)j=u(1+hj).                                 \tag{24}
\]

At both \(p\) and \(q\), \(u\) is invertible because \(u\bar u=-R\) is a
unit. Left multiplication by \(u\) therefore preserves the row line, giving

\[
\operatorname{row}_r\beta(u)=
\operatorname{row}_r(1+hj)                                \tag{25}
\]

for every point on the whole fibre. Thus the local row atom is \(1\), not
\(O(1/r)\), even though the completion has degree one.

There is a dual degree-one construction. Put

\[
c=h\bar u.
\]

Using \(ju=\bar u j\), one gets

\[
\beta(u)=(1+hj)u,
\]

so the image line is constant in both CRT components.

This construction can be made from exactly the globally supplied base
completion in (19); it does not hide a local square root. It is also the
minimal-left/right-ideal construction in elementary form: the norm-zero seed
\(\alpha=1+hj\) defines one global minimal ideal, and multiplication by the
varying unit \(u\) merely gives different representatives of that same ideal.

There is a completely explicit coefficient-clean example. Take

\[
N=21,
\quad R=1,
\quad u_0=2-4i,
\quad c_0=-1,
\quad h=2+4i.                                             \tag{26}
\]

Then

\[
u_0\bar u_0=20\equiv-1,
\qquad
c_0\bar c_0=1,
\qquad
h\bar h=20\equiv-1\pmod{21}.                             \tag{27}
\]

The completion is

\[
z=2x-4y,
\qquad
w=4x+2y,                                                  \tag{28}
\]

and

\[
\alpha=1+2j+4k,
\qquad
\operatorname{nrd}(\alpha)=1+2^2+4^2=21.                 \tag{29}
\]

Every nonzero coefficient in (28)--(29) is a unit modulo \(21\), and the
content is primitive. Constancy holds modulo both \(3\) and \(7\), so every
variation minor/subresultant vanishes modulo all of \(N\); no proper
coefficient gcd is forced. This is a small explicit counterexample to both of
the unqualified assertions

* “bounded-degree fibre dependence is diffuse,” and
* “a constant composed line map necessarily exposes a coefficient factor.”

For a completely explicit matrix check, the public values \(s=2,t=4\)
satisfy \(s^2+t^2=-1\pmod {21}\). Substituting (28) gives

\[
A_c=2z+4w=-x,\qquad B_c=4z-2w=y,
\]

and hence

\[
\beta=
\begin{pmatrix}0&2y\\0&2x\end{pmatrix}.
\tag{29a}
\]

The row line is \([0:1]\) everywhere, using the second row when the first is
zero, and the only surviving scalar coefficient \(2\) is a unit modulo
\(21\).

## 6. What simultaneous constancy does and does not reveal

“Simultaneous” means constant in both CRT components. It does **not** mean
that the two constants are the same numerical projective point. A single
global projective line or minimal ideal over
\(A\simeq\mathbb F_p\times\mathbb F_q\) is precisely an arbitrary pair

\[
(L_p,L_q)\in\mathbb P^1(\mathbb F_p)\times
\mathbb P^1(\mathbb F_q).                                 \tag{30}
\]

The reductions \(L_p\) and \(L_q\) may look completely different. Their
being represented by one global CRT object does not supply a proper zero
divisor. Local constants \(\lambda_p\ne\lambda_q\) therefore do not contradict
the failure of coefficient visibility: both local degrees are zero, so all
degree-drop predicates are synchronized.

Cloning the line also does not by itself manufacture a P28 factor. Pairwise
gcds of clones see equality at both primes. The twelve-unit stabilizer
extractor succeeds only if

\[
\operatorname{Stab}_{A_4}(L_p)\ne
\operatorname{Stab}_{A_4}(L_q).                            \tag{31}
\]

That is a separate exceptional-line property, not a consequence of
constancy. Generic local lines have trivial stabilizer at both primes, so
(31) can fail identically. More concretely, P30's supported line set has
\(r-\chi_r\) elements and at most fourteen are exceptional. For sufficiently
large \(p,q\), choose a nonexceptional line in each component and combine the
corresponding base data by CRT; the resulting global constantizer has trivial
stabilizer at both primes and the complete P28 unit menu fails
deterministically.

For the construction (19)--(25), the constant line is exactly the line of the
base quaternion

\[
\beta_0=u_0+(u_0h)j=u_0(1+hj).                            \tag{32}
\]

If the base point came from P30's residual-only uniform fibre, this line has
P30's uniform supported law. P28--P30 already bound the probability of (31)
by \(O(1/p+1/q)\). Constantization makes arbitrarily many identical copies of
that one draw; it does not amplify the chance that the draw belonged to the
exceptional stabilizer set.

Thus simultaneous constant bias can be maximal as a distributional bias and
still be neutral for the tested direct equality, stabilizer-menu, and
unequal-degree coefficient detectors. This is not information-theoretic
neutrality: metric functions of the public seed and nonlinear joint
statistics remain available and are not analyzed here. A positive use would
need a factor-free rule that selects a global seed whose two local constants
have a provably mismatched extractable property with inverse-polynomial
probability. The degree-one identity does not supply such a selector.

## 7. Exact theorem, verdict, and retry conditions

> **F40 bounded-degree fibre-map boundary.** For a uniform point on
> \(x^2+y^2=-R\) over an odd field, a nonconstant row- or image-line map induced
> by a rational completion represented by degree-\(D\) homogeneous forms has
> every atom at most
> \(2(D+1)/(r-\left(\frac{-1}{r}\right))\). An arbitrary selector among \(B\)
> nonconstant displayed branches has atom at most
> \(2B(D+1)/(r-\left(\frac{-1}{r}\right))\), interpreted as an unconditional
> no-factor-output subprobability when denominator gcds can terminate with a
> factor. More generally, after local reduction and componentwise
> normalization, selectable nonconstant graph components have total atom at
> most their summed \(\mathcal O(1,1)\)-degree divided by the source-fibre
> size; a constant source-dominating component is a degeneration. Poles, zero
> first rows/columns, points at infinity, vertical components, and
> multiplicities are included in these bounds. If the composed
> projective map is explicitly available over \(\mathbb Z/N\mathbb Z\) as
> polynomial-degree binary forms, unequal reduced degrees in the two CRT
> components expose a factor through a coefficient/content/subresultant gcd.
> This coefficient theorem does not extend automatically to a multivalued
> algebraic graph.
> Neither conclusion covers simultaneous degeneration: a public base source
> point and completion produce a degree-one completion whose row (or image)
> line is constant at both primes and which need expose no coefficient factor.

**Candidate verdict:** the naive auxiliary claim “every bounded-degree
fibre-dependent completion is diffuse or immediately factors” is **refuted**
by the degree-one constantizer. The corrected nonconstant-or-asymmetric
statement is **proved** under the explicit representation assumptions above.
It kills fixed or polynomially many nonconstant bounded-degree branches for
fresh-call collisions, fixed targets/menus, and exceptional-stabilizer
events. It does not close same-source paired maps or all P28--P31 relations.
Simultaneous constant bias survives algebraically but, in the displayed
construction, only clones one already sampled hidden ideal and has no
all-input extraction guarantee for the tested direct detectors.

**Retry conditions.** A materially new F14 source-side attempt must do at
least one of the following:

1. give a factor-free selector for a simultaneously degenerate global ideal
   with a proved inverse-polynomial local mismatch, rather than merely cloning
   an arbitrary base ideal;
2. use a characteristic-scale-degree or superpolynomial-branch map with a
   uniform polynomial-time succinct evaluator;
3. use metric/piecewise/canonical-integer branching, an opaque but justified
   division/root circuit, stochastic or dissipative completion, or adaptive
   resampling whose conditioning cost is proved;
4. decode typical nonzero information from many outputs through a genuinely
   nonlinear joint statistic rather than unioning line atoms.

No claim here applies to those cases, to magnitude comparisons, to noisy
dynamics, or to a completion rule whose polynomial-size representation and
uniform bit cost have not been exhibited.
