# Proof-blind reconstruction: the screened coherent-orientation theorem

## Verdict and exact reading

The semiprime statement is correct under the following precise meanings.

1. A raw trial in part (ii) starts with an exactly uniform residue modulo
   (N).  A gcd first detects nonunits.  Conditional on reaching a unit, the
   power-map calculation has the exact failure law proved below.
2. In part (iii), the coordinate algebra is the algebra of the *screened and
   simplified* system.  In particular, a double root proved to be a global
   constant (1) or (-1) is replaced by its linear equation before the
   coordinate algebra is formed.  The unreduced quotient by
   ((X-s)^2) would contain a nilpotent and would not satisfy the claim.
3. A relation in part (iv) is a polynomial equality, a finite conjunction of
   polynomial equalities, or an equality computed by a public arithmetic
   straight-line circuit.  Division is permitted only by previously screened
   units.  An arbitrary Boolean predicate is not a polynomial relation.
4. A proved orientation component is one for which all endpoint residuals
   have been gcd-screened and the resulting signed orientation graph has
   passed its public cycle-consistency check.

With these necessary interpretations, all five parts follow.  The result is
a promise theorem for distinct odd semiprimes.  It does not give an all-input
factoring algorithm.

Throughout, put

\[
 R=\mathbb Z/N\mathbb Z\simeq \mathbb F_p\times\mathbb F_q,
 \qquad e=N-1,
 \qquad g=q-p,
\]

where (N=pq) and (3\leq p<q) are distinct odd primes.  All congruences and
gcds used by the algorithms are computed from public residues; the CRT is
used only in proofs unless the factorization is explicitly supplied.

## 1. Classification of all trace-compatible homomorphisms

We first need a rigidity lemma which does not assume that a homomorphism is a
power map.

**Lemma 1 (two-character rigidity).**  Let (A) be a group and let

\[
 \chi,\psi:A\longrightarrow K^\times
\]

be homomorphisms into a field.  If

\[
 \chi(a)+\chi(a)^{-1}=\psi(a)+\psi(a)^{-1}
 \quad\hbox{for every }a\in A,
\]

then (chi=\psi) or (chi=\psi^{-1}).

**Proof.**  For nonzero (x,y\in K),

\[
 x+x^{-1}=y+y^{-1}
 \iff (x-y)(xy-1)=0.
\]

Thus every (a\in A) belongs to

\[
 K_+=\ker(\chi\psi^{-1})
 \quad\hbox{or}\quad
 K_-=\ker(\chi\psi).
\]

Both are subgroups.  A group cannot be the union of two proper subgroups: if
(x\in K_+\setminus K_-) and (y\in K_-\setminus K_+), then (xy) is in
neither subgroup.  Hence one of (K_+,K_-) is all of (A), proving the
claim.  This also covers trivial and order-two images.  (square)

Let (H:R^\times\to R^\times) be an arbitrary group homomorphism satisfying

\[
 T(H(a))=T(E(a))\qquad(a\in R^\times),
\]

where (E(a)=a^e) and (T(z)=z+z^{-1}).  Project to each CRT field.  Lemma 1
shows independently that

\[
 H(a)_p=E(a)_p^{\epsilon_p},\qquad
 H(a)_q=E(a)_q^{\epsilon_q},
 \qquad \epsilon_p,\epsilon_q\in\{1,-1\},
\]

with signs fixed for the whole homomorphism, not signs depending on (a).
This step also rules out hidden cross-coordinate characters.

The four sign choices are four ordinary power maps.  Indeed,

\[
 e\equiv q-1\pmod{p-1},\qquad e\equiv p-1\pmod{q-1},
\]

whereas

\[
 g\equiv q-1\equiv e\pmod{p-1},\qquad
 g\equiv 1-p\equiv-e\pmod{q-1}.
\]

Therefore the choices ((+,+),(-,-),(+,-),(-,+)) give, respectively,

\[
 \boxed{E,\quad E^{-1},\quad G,\quad G^{-1}}.
\]

Some of these maps can coincide when a local image has exponent at most two.
The argument classifies maps, so such coincidences do not create a fifth
map.

## 2. A public constant-probability screen and its exact failure law

### 2.1 The trial

One raw trial is as follows.

1. Draw (a) exactly uniformly from (R).
2. Compute (d=\gcd(a,N)).  Return (d) if (1<d<N).  Retry if (d=N).
3. If (d=1), compute (y=a^{N-1}\bmod N), its inverse, and
   (d_0=\gcd(y-y^{-1},N)).
4. If (1<d_0<N), return (d_0).  If (d_0=1), return the public screened
   anchor (y), for which (y-y^{-1}) is a unit.
5. If (d_0=N), compute the two gcds
   (gcd(y-1,N)) and (gcd(y+1,N)).  Return either one that is proper.
   Otherwise retry.

Every returned divisor is checked by (1<d<N) and (d\mid N).  Every
returned anchor is checked by (gcd(y-y^{-1},N)=1).  Thus the routine is
Las Vegas.

### 2.2 Image orders

Let

\[
 d_* = \gcd(p-1,q-1),\qquad
 r=\frac{p-1}{d_*},\qquad
 s=\frac{q-1}{d_*}.
\]

Then (r<s), (gcd(r,s)=1), and (rs\geq2).  The two local images of the
power map (E) have exact orders

\[
 \begin{aligned}
 |\operatorname{im}E_p|
 &=\frac{p-1}{\gcd(p-1,pq-1)}
 =\frac{p-1}{d_*}=r,\\
 |\operatorname{im}E_q|
 &=\frac{q-1}{\gcd(q-1,pq-1)}
 =\frac{q-1}{d_*}=s.
 \end{aligned}
\]

For uniform (a\in R^\times), the two coordinates of (E(a)) are
independent and uniform in these two image subgroups.

The first difference screen fails to return an anchor or a factor only when
both local coordinates of (y) are in ({1,-1}).  The two later screens
factor in the mixed-sign cases.  Consequently, the whole unit stage fails
exactly when (y=1) or (y=-1) globally.  For arbitrary image orders (r,s)
the exact formula is

\[
 \Pr(\text{unit-stage failure})
 =\frac{1+\mathbf 1_{2\mid r}\mathbf 1_{2\mid s}}{rs}.
 \tag{2.1}
\]

A cyclic subgroup contains (-1) exactly when its order is even.  Here
(gcd(r,s)=1), so (r) and (s) cannot both be even.  Hence (2.1)
simplifies to

\[
 \boxed{\Pr(\text{unit-stage failure})=\frac1{rs}},\qquad
 \Pr(\text{unit-stage success})=1-\frac1{rs}\geq\frac12.
 \tag{2.2}
\]

This is the exact image-order failure law.

The density of units satisfies

\[
 \frac{\varphi(N)}N
 =\left(1-\frac1p\right)\left(1-\frac1q\right)
 \geq \frac23\cdot\frac45=\frac8{15}.
\]

Ignoring even the successful proper-nonunit cases, a raw uniform-residue
trial therefore returns a factor or an anchor with probability at least

\[
 \boxed{\frac8{15}\cdot\frac12=\frac4{15}}.
\]

If proper nonunits are counted, the exact raw-residue failure probability is
also available.  The only nonunit failure is (a=0), and
((p-1)(q-1)=d_*^2rs).  Thus

\[
 \Pr(\text{raw failure})
 =\frac1N+\frac{\varphi(N)}N\frac1{rs}
 =\boxed{\frac{1+d_*^2}{N}}.
 \tag{2.3}
\]

### 2.3 Uniformity and bit cost

An exact uniform residue is obtained by drawing (n) random bits and
rejecting integers at least (N).  Since (2^{n-1}\leq N<2^n), fewer than
two bit blocks are needed in expectation.  Modular binary exponentiation
uses (O(n)) modular multiplications.  With schoolbook arithmetic this is
(O(n^3)) bit operations; inversion and each gcd are (O(n^2)), and all
residues remain (O(n)) bits.  Repetition has mean at most (15/4) accepted
uniform-residue trials by the displayed lower bound and terminates almost
surely.  Random-bit use and total expected bit cost are polynomial in (n).

## 3. Screened inverse-root systems

### 3.1 Root screening and affine idempotents

For every public unit (A_v\in R^\times), start with

\[
 (X_v-A_v)(X_v-A_v^{-1})=0
 \tag{3.1}
\]

and put (delta_v=A_v-A_v^{-1}).  Compute
(gcd(\delta_v,N)).

* A proper gcd factors (N).
* If the gcd is (1), retain (v).  Its root difference is a unit.
* If the gcd is (N), then (A_v^2=1) in both CRT fields.  Screen
  (A_v-1) and (A_v+1).  A mixed local sign factors (N); otherwise
  (A_v) is the global constant (1) or (-1).  Replace (3.1) by the
  linear equation (X_v=A_v) and substitute it everywhere.

The last replacement is essential.  It preserves exactly the (R)-valued
solutions because (R) is reduced, and it removes the artificial nilpotent
that would remain in (R[X_v]/((X_v-A_v)^2)).

For a retained vertex define

\[
 f_v=\frac{X_v-A_v^{-1}}{A_v-A_v^{-1}}.
\]

Then (3.1) is equivalent, as an ideal after this invertible affine change,
to

\[
 f_v^2-f_v=0,
 \qquad
 X_v=A_v^{-1}+\delta_v f_v.
 \tag{3.2}
\]

Thus (f_v=1) selects (A_v), (f_v=0) selects (A_v^{-1}), and a mixed
CRT root is a nontrivial idempotent value of (f_v).

### 3.2 Endpoint screening for every multiplicative equation

Consider a public equation

\[
 X_w=X_uX_v.
 \tag{3.3}

After substituting all global constants and identifying repeated symbols,
there are at most three distinct retained variables.  Evaluate the residual
of (3.3) at every assignment of their displayed endpoints.  There are at
most eight residuals.  Take the gcd of each residual with (N).

On the factor-free branch, every residual is either zero in (R) or a unit.
If an endpoint equality holds over only one CRT field, its residual instead
has a proper gcd and already factors (N).  Hence any relation retained as
genuine has a publicly proved global endpoint equality, not an assumed
local compatibility.

Endpoint inversion sends every solution of (3.3) to another solution.  A
constant occurrence is fixed by inversion only when that constant is an
involution.  For a public unit (s), first screen (s-s^{-1}); a genuine
two-endpoint relation forces this difference to vanish.  The later screens
of (s\pm1) either factor (N) or prove (s=1) or (s=-1) globally.

### 3.3 Distinct-variable product

Suppose first that (u,v,w) are distinct retained vertices.  Relabeling a
displayed pair by interchanging (A) and (A^{-1}) does not change its root
set.  After such a relabeling, a proved endpoint equality has the form

\[
 A_w=A_uA_v.
 \tag{3.4}

The all-inverse equality also holds.  These are the only endpoint
assignments satisfying (3.3).  For completeness, the residuals at the six
other assignments are, up to sign, unit multiples of one of the three root
differences.  Representative calculations are

\[
 \begin{aligned}
 A_w^{-1}-A_w&=-\delta_w,\\
 A_w-A_uA_v^{-1}&=A_u\delta_v,\\
 A_w-A_u^{-1}A_v&=A_v\delta_u,\\
 A_w^{-1}-A_uA_v^{-1}&=-A_v^{-1}\delta_u,\\
 A_w^{-1}-A_u^{-1}A_v&=-A_u^{-1}\delta_v.
 \end{aligned}
\]

The remaining case is (\delta_w).  All are units.  Therefore (3.3), in
the Boolean algebra defined by (3.2), is *exactly* the pair of orientation
equalities

\[
 f_u=f_v=f_w.
 \tag{3.5}
\]

Without relabeling, the conclusion is a signed version: each pair is either
(f_i=f_j) or (f_i=1-f_j).  The signs are determined by the publicly
verified endpoint assignment.

### 3.4 Repeated-variable cases

All repeated-position cases must be simplified before graph construction.

1. **Repeated inputs, distinct output:**
   (X_w=X_u^2).  If both vertices are retained and the aligned endpoint
   identity is (A_w=A_u^2), the two matching assignments are the endpoint
   and its inverse.  The two mismatched residuals are
   (pm(A_w-A_w^{-1})), which are units.  Hence the exact consequence is
   (f_w=f_u), up to a public orientation flip.

   If the output root is degenerate, do not divide by its root difference.
   The preceding screen first proves (X_w=s\in\{1,-1\}), and the equation
   becomes (s=X_u^2).  If it is genuine at both endpoints, then
   (s=A_u^2=A_u^{-2}), so it is an identity for both values of (f_u) and
   adds no edge.

2. **Output repeated as one input:**
   (X_u=X_uX_v), or symmetrically (X_v=X_uX_v).  Every root coordinate
   is a unit, so cancellation gives (X_v=1), respectively (X_u=1).
   A genuine system therefore eliminates that vertex as the global constant
   (1).  A retained nondegenerate vertex in this position means the
   equation is not a genuine two-endpoint relation.

3. **One symbol in all positions:** (X_u=X_u^2).  Unit cancellation gives
   (X_u=1).  It is a constant case, never a retained orientation edge.

These cases show why blindly treating every multiplication as a
three-vertex edge is incorrect.

### 3.5 Constant-position cases

The two important cases are different and must not be conflated.

**Constant product.**  Let

\[
 s=X_uX_v
 \tag{3.6}
\]

with distinct retained inputs.  A genuine endpoint and its inverse imply

\[
 s=A_uA_v=(A_uA_v)^{-1}=s^{-1}.
\]

After the involution gcd screens, (s) is globally (1) or (-1).  In an
aligned labeling, the matching assignments are again ((1,1)) and
((0,0)).  The two mismatched residuals are unit multiples of
(delta_u) and (delta_v).  Thus (3.6) gives exactly (f_u=f_v), up to
an orientation flip.

If the inputs in (3.6) are the same vertex, the equation is (s=X_u^2).
As in the degenerate-output square case, a genuine relation holds for both
endpoints and adds no edge.  It does not fix the orientation.

**Constant input.**  Let

\[
 X_w=sX_u
 \tag{3.7}

with distinct retained vertices.  If (A_w=sA_u) is one aligned endpoint,
then compatibility at the inverse endpoints requires

\[
 A_w^{-1}=sA_u^{-1}=s^{-1}A_u^{-1},
\]

so again (s=s^{-1}), and the screens prove (s=\pm1) or factor (N).
The two mismatched residuals are unit multiples of
(delta_w=s\delta_u).  Hence (3.7) gives exactly (f_w=f_u), up to a
public flip.

If (w=u), (3.7) reduces to (X_u=sX_u).  It is a tautology for (s=1)
and is impossible for (s=-1), since (2) and (X_u) are units.  It adds
no edge.

All remaining constant patterns reduce immediately:

* two constant inputs force the output to their checked product;
* a constant output and one constant input force the remaining input to a
  checked constant;
* three constants give a public equality check.

None can leave a genuine nondegenerate orientation vertex fixed to one
endpoint while preserving its inverse endpoint.

### 3.6 Exact component algebra

It remains to prove that the graph description is not merely a statement
about visible solutions.

For (k) retained vertices, before multiplicative equations are imposed,
the Boolean algebra is

\[
 B=R[f_1,\ldots,f_k]/(f_1^2-f_1,\ldots,f_k^2-f_k)
 \simeq \prod_{b\in\{0,1\}^k}R.
 \tag{3.8}
\]

The isomorphism is simultaneous evaluation at all Boolean assignments.  A
multiplicative residual becomes a tuple in this product.  On the screened
branch, each entry is either (0) or a unit.  Quotienting by that residual
keeps exactly the zero entries and kills exactly the unit entries.  The
case analyses above show that each genuine equation keeps precisely a
complementary endpoint pair and is exactly equivalent to its signed graph
edges.

Construct the signed orientation graph.  An edge records either
(f_v=f_u) or (f_v=1-f_u).  Run a parity search from one vertex of each
component.  If a cycle gives contradictory parity, the component has no
Boolean assignment.  Algebraically it would imply both (f=1-f) and
(f^2=f); since (2) is a unit, these relations imply (1=0).  A proved
coherent component is one which passes this public check.

In a connected coherent component choose one vertex switch (f).  Every
other (f_v) is then proved to be either (f) or (1-f), and there are
exactly two complementary global endpoint assignments.  From (3.8), its
exact coordinate algebra is therefore

\[
 \boxed{R[f]/(f^2-f)\simeq R\times R.}
 \tag{3.9}

No extra nilpotent or extra Boolean assignment remains.  An isolated
retained vertex is a one-vertex component and satisfies the same formula.
For (c) independent components the full algebra is instead

\[
 R[f_1,\ldots,f_c]/(f_1^2-f_1,\ldots,f_c^2-f_c),
 \tag{3.10}

so independent components must not be silently assigned one common switch.

### 3.7 Shifted quadratics

A screened quadratic with two distinct public roots can always be affinely
written with an idempotent.  That fact alone does not put several
quadratics in one component.  In particular, symmetric shifted-quadratic
identities do not prove that choices of their two roots have a common
orientation.

Such quadratics are covered by (3.9) only after all of the following have
been done explicitly: their root differences have been gcd-screened; any
degenerate roots have been linearly eliminated without division; genuine
multiplicative endpoint equations have been exhibited; every endpoint
residual has been screened; and the signed orientation graph has passed its
cycle-consistency check.  If the two roots are not an inverse pair, one
must additionally prove a valid affine or multiplicative normalization;
the mere equality of their symmetric sum and product is insufficient.

### 3.8 Cost of the preprocessing

There are at most eight endpoint residuals per original multiplication
equation.  Thus a public system with (M) vertices and equations needs
(O(M)) modular inversions, equality tests, and gcds, followed by a linear
graph-parity search.  All values are reduced modulo (N).  The bit cost is
polynomial in (n) and in the public encoding length.  It is polynomial in
(n) when that encoding length is polynomial in (n).  The algebraic
theorem itself holds for every finite system; finiteness alone does not give
a polynomial-time algorithm if the supplied system is superpolynomially
large.

## 4. Endpoint dichotomy inside one component

Let

\[
 C=R[f]/(f^2-f).

Every element of (C) has a unique endpoint form

\[
 c_0(1-f)+c_1f,
 \tag{4.1}
\]

where (c_0,c_1\in R).  They are obtained by evaluation at (f=0) and
(f=1).  After substituting the affine coordinate expressions from (3.2),
any public polynomial or arithmetic-circuit residual (P) therefore obeys

\[
 P=P(0)(1-f)+P(1)f\quad\hbox{in }C.
 \tag{4.2}

If the relation (P=0) accepts both public endpoints, then
(P(0)=P(1)=0) in (R), so (4.2) gives (P=0) identically in (C).  It
also accepts both mixed idempotents.  The same argument applies one residual
at a time to a finite conjunction.  This is the precise sense in which a
factor-free public relation accepting both endpoints is tautological.

Conversely, let (e_p\in R) denote the CRT idempotent which is (1) modulo
(p) and (0) modulo (q).  Suppose (P(e_p)=0).  Equation (4.2) then
gives

\[
 P(1)\equiv0\pmod p,
 \qquad
 P(0)\equiv0\pmod q.
\]

If the public endpoint (f=0) fails, then (P(0)\not\equiv0\pmod N), so

\[
 \gcd(P(0),N)=q.
\]

If the endpoint (f=1) fails, then (gcd(P(1),N)=p).  The other mixed
idempotent swaps (p) and (q).  For several equations, choose a residual
which fails at the endpoint.  Thus

\[
 \boxed{\text{mixed acceptance plus endpoint failure gives an endpoint gcd
 that factors }N.}
\]

For a straight-line circuit of size polynomial in (n), the two endpoint
residuals and their gcds have polynomial bit cost because every operation is
performed modulo (N).  A screened inverse gate is evaluated by the
extended Euclidean algorithm.  No dense expansion of the polynomial is
needed.

The statement would be false for an unrestricted predicate.  For example,
the disjunction “(f=0) or (f=1)” accepts both global endpoints and
rejects mixed idempotents.  Such branching predicates, order comparisons,
and metric selection rules are outside the polynomial-relation claim.

## 5. A mixed screened coordinate is equivalent to the factors

Let (A\in R^\times) be public and screened, so

\[
 \gcd(A-A^{-1},N)=1.

Suppose a returned coordinate (X) is mixed: it equals (A) in one CRT
field and (A^{-1}) in the other.  Then

\[
 \gcd(X-A,N)

is exactly one of (p,q).  At the matching coordinate the difference is
zero; at the other it is (pm(A-A^{-1})), which is nonzero.  This is a
deterministic polynomial-time reduction from a mixed screened coordinate to
factoring (N).

Conversely, given (p,q) and the same screened pair, compute the CRT
idempotent

\[
 e_p=q(q^{-1}\bmod p)\pmod N

and return

\[
 X=e_pA+(1-e_p)A^{-1}\pmod N.

This is a mixed coordinate.  Extended gcd and CRT have deterministic
polynomial bit cost.  Hence, for a supplied screened inverse-root instance,

\[
 \boxed{\text{producing a mixed coordinate}\ \equiv_{\rm deterministic\ poly}
 \ \text{knowing the factorization of }N.}

This is a witness/search equivalence on the screened promise.  It is not a
claim that a screened instance can always be generated deterministically
from (N) alone.  Part (ii) generates either such an anchor or a factor by
a constant-expected-trial Las Vegas procedure.  Also, no screened inverse
pair exists over a local (mathbb F_3^\times); if (p=3), the premise of a
returned screened coordinate is empty and the trial in part (ii) instead
has a local factor opportunity.  Given factors with (p,q\geq5), the public
choice (A=2) is screened because (2=2^{-1}\pmod r) would imply
(r\mid3).

## 6. Boundaries and exclusions

The proof establishes only the screened coherent-orientation theorem just
stated.  It does not cover the following mechanisms.

* **Independent components.**  They carry independent idempotents as in
  (3.10), not one hidden global switch.
* **Arbitrary cross-couplings.**  Nonmultiplicative equations can retain an
  arbitrary subset of Boolean assignments.  They need their own screened
  algebra analysis.
* **Auxiliary existential variables.**  Projection can change the accepted
  endpoint set and can correlate local witnesses differently.  It is not
  justified by the coordinate algebra of the visible variables.
* **Metric or order rules.**  Integer representatives, least roots,
  multiplicative orders, comparisons, and optimization are not polynomial
  identities in (R[f]/(f^2-f)).
* **Stochastic samplers.**  The algebra classifies exact solution sets, not
  distributions, biases, or correlations of a sampling algorithm.
* **Derivatives and lifts.**  Formal derivatives and information modulo
  (N^2) inspect data not present in the mod-(N) coordinate algebra.
* **Lucky distributions.**  Apart from the exact trial in part (ii), no
  inverse-polynomial probability is proved for special gcd events.
* **Shifted quadratics without proved coherence.**  Sharing symmetric
  coefficients or a claimed hidden origin does not create a graph edge.
* **All-input factoring.**  The proof assumes (N=pq) with distinct odd
  primes.  It does not cover primes, (p^2), even composites, products of
  three or more primes, repeated factors, or the recursion and primality
  bookkeeping required for complete factorization.

Thus the result isolates the missing step rather than solving it: once a
screened coherent component is reached, every exact public polynomial
relation either treats its two endpoints identically or exposes a factor;
and an actual mixed coordinate is already a factoring witness.

## Final conclusion

All five requested semiprime claims hold with the explicit screening,
coherence, algebraic-relation, and supplied-instance quantifiers above.  The
exact common theorem is the **screened coherent-orientation theorem**:
trace compatibility gives four homomorphisms; the public (E)-trial has
failure (1/(rs)) on units; every factor-free coherent multiplicative
component has coordinate algebra (R[f]/(f^2-f)); polynomial relations obey
the endpoint dichotomy; and a nontrivial idempotent coordinate is
deterministically equivalent to the factorization.

**RECONSTRUCTION SUCCEEDS**
