# Fresh hostile re-audit of F49 coherent Dickson-root selection

## Artifact and verdict

This audit checks
experiments/F49_coherent_dickson_root_kill/RESULT.md at SHA-256

b29bc27bc16766c52bbd8d4e83e6e7c4f67e49f7c2f6f615beddc11f3bffccd1.

I read the fixed statement, C54–C55, P57, X51, the complete candidate, and
the complete first failed audit. I then reconstructed the CRT and coordinate-
algebra arguments independently. I used no web search and no computational
experiment. The small exact witness below is checked by displayed arithmetic.

**Verdict: FAIL AS WRITTEN.** Section 5 still states a false simplification
for a genuine relation whose eliminated constant is the product output. The
intended orientation-edge conclusion is true, but the displayed case split
does not prove it. A concrete screened example below disproves the sentence as
written. The correction is small but mathematical, so this exact artifact
cannot receive a clean audit.

All other central claims survive the hostile re-derivation under the narrow
scope that the candidate itself states. In particular, this is not a factoring
algorithm. It proves only an endpoint dichotomy after one common idempotent has
already been established.

## 1. Decisive remaining defect: the constant can be the output

Section 5, item 3, says that after substituting one known constant
$s\in\{1,-1\}$, the two remaining nondegenerate variables satisfy

\[
 X_w=sX_u.
 \tag{1.1}
\]

That is correct when one of the two inputs of

\[
 X_w=X_uX_v
 \tag{1.2}
\]

is the constant. It is false when the output $X_w$ is the constant. In the
output-constant case the reduced equation is

\[
 s=X_uX_v,
 \tag{1.3}
\]

or, because the variables are units,

\[
 X_v=sX_u^{-1}.
 \tag{1.4}
\]

It is not $X_v=sX_u$ in general.

### Exact screened counterexample

Take

\[
 N=77=7\cdot11,\qquad e=N-1=76,\qquad a=24.
\]

The inverse of $24$ modulo $77$ is $61$. Direct local exponent calculation
gives

\[
 E(24)=24^{76}=53\pmod {77},
 \qquad E(61)=16=53^{-1}\pmod {77}.
\]

Indeed, $53\equiv4\pmod7$, $53\equiv9\pmod{11}$,
$16\equiv2\pmod7$, and $16\equiv5\pmod{11}$. Also

\[
 \gcd(53-16,77)=\gcd(37,77)=1,
\]

so both root pairs survive the candidate's nondegeneracy screen.

Use the genuine base relation

\[
 a_w=1=a_u a_v,
 \qquad a_u=24,\qquad a_v=61.
\]

Then $A_w=1$, so linear elimination gives $X_w=1$, while the remaining
relation is

\[
 1=X_uX_v.
\]

At the public $E$-endpoint,

\[
 (X_u,X_v)=(53,16),
\]

and at the public $E^{-1}$-endpoint the pair is $(16,53)$. Both pairs
satisfy $X_uX_v=1$, but neither satisfies $X_v=X_u$. Thus (1.1), under the
only possible relabeling of the two surviving original variables, is false.

The intended orientation conclusion nevertheless holds. The unequal corners
are $(53,53)$ and $(16,16)$. Their residuals in $X_uX_v-1$ are

\[
 53^2-1=36\pmod {77},
 \qquad 16^2-1=24\pmod {77},
\]

and both are units modulo $77$. Hence the actual output-constant equation
kills the unequal-orientation corners and keeps the equal-orientation corners.
The theorem is repairable, but the stated proof case is not correct.

### Exact algebraic correction

Section 5 must split item 3 by the position of the constant.

1. If an input is constant, the reduced relation is $X_w=sX_u$. Its two
   unequal normalized corners have unit residuals.
2. If the output is constant, the reduced relation is $s=X_uX_v$. Put
   $A=A_u$ and $\delta=A-A^{-1}\in R^\times$. Genuine public
   multiplicativity gives $A_v=sA^{-1}$. Write

   \[
   X_u=A^{-1}+f\delta,
   \qquad
   X_v=sA-hs\delta,
   \qquad f^2=f,\quad h^2=h.
   \]

   The equation $s=X_uX_v$ vanishes at $f=h=0$ and $f=h=1$.
   At the two unequal corners its residuals are unit multiples of
   $\delta$. Therefore it imposes $h=f$.

After these two subcases are proved, the orientation edge used by the
connected-component theorem is valid in every constant position.

## 2. Dependency and trace-compatible homomorphisms

The use of P57 is correct. For $e=pq-1$ and $g=q-p$,

\[
 e\equiv g\pmod {p-1},
 \qquad e\equiv-g\pmod {q-1}.
\]

Thus $E=G$ locally at $p$, while $E=G^{-1}$ locally at $q$.

Theorem 2.1 also passes. If $H:R^\times\to R^\times$ is a homomorphism with
$T(H(a))=T(E(a))$ for every unit, then on an input $(1,b)$ its
$p$-coordinate satisfies

\[
 x+x^{-1}=2.
\]

Over $\mathbb F_p$, this is $(x-1)^2=0$, so $x=1$. Hence the
$p$-coordinate of $H$ kills the entire $q$-side subgroup. The symmetric
argument applies to the $q$-coordinate. Each remaining local homomorphism is
a power map on a cyclic group. P57's one-field trace theorem leaves the two
signs independently. The four sign pairs are exactly

\[
 E,\qquad E^{-1},\qquad G,\qquad G^{-1},
\]

with allowed coincidences. No local generator, order, or factor is needed by
the public computations; the CRT description is only the proof.

The quantifier in Theorem 2.1 is essential: it classifies global
trace-compatible homomorphisms. It does not say that arbitrary roots selected
from finitely many unrelated quadratics extend to such a homomorphism. The
candidate does not make that invalid extension later.

## 3. Anchor probability and factor-free construction

The anchor calculation passes exactly. The image sizes of the power map
$z\mapsto z^e$ in the two local unit groups are

\[
 h_p=\frac{p-1}{d},\qquad h_q=\frac{q-1}{d},\qquad
 d=\gcd(p-1,q-1).
\]

For a uniform unit, the image coordinates are independent and uniform, and
$h_p<h_q$. A full gcd of $E(a)-E(a)^{-1}$ means both local images are
self-inverse. The only no-factor/no-anchor outcomes are the synchronized
pairs $(1,1)$ and, when both image orders are even, $(-1,-1)$. Therefore
the conditional failure probability is

\[
 \frac{1+\mathbf 1_{2\mid h_p,\,2\mid h_q}}{h_ph_q}\le\frac12.
\]

If both orders are even, strict inequality gives $h_ph_q\ge8$. Otherwise
$h_ph_q\ge2$. Equality at $1/2$ is exactly $(h_p,h_q)=(1,2)$,
equivalently $q=2p-1$.

The raw-unit probability is at least $8/15$, so a factor or an anchor occurs
with probability at least $4/15$ per raw trial. Modular exponentiation,
inversion after a unit gcd, and all comparison gcds have polynomial bit cost.
This process is factor-free: $E(a)=a^{N-1}\bmod N$ is public. The process
does not compute $G$ or a mixed root.

The anchor statement does not itself connect the sampled anchor to a later
root component. Extraction must use a returned coordinate whose public root
difference is a unit, or an anchor that has explicitly been put in the same
coherent component. Section 7 supplies the valid local extraction. The phrase
“comparison with any unit-difference anchor” in Section 6 should be read with
this same-component qualification.

## 4. One-triangle coordinate algebra

Section 4 passes, including the case $C=C^{-1}$. Because
$A-A^{-1}$ and $B-B^{-1}$ are units, the two normalized root algebras are
separable Boolean algebras. Before imposing the root equation for $Z=XY$,
their tensor product is $R^4$, indexed by the four formal corners
$(f,h)\in\{0,1\}^2$.

At the two equal corners, $XY$ is $C$ or $C^{-1}$. At a mixed corner, the
residual of the $Z$-root polynomial is a product of unit multiples of
$A-A^{-1}$ and $B-B^{-1}$. Hence the two mixed factors of $R^4$ are killed
and the two equal factors remain. The quotient is

\[
 R[f]/(f^2-f),
\]

with $h=f$. No inverse of $C-C^{-1}$ is used. Thus even a globally or
locally repeated $C$-root does not create a nilpotent in this particular
triangle quotient.

## 5. Degenerate roots, repeated variables, and components

The correction for an isolated double root is present and correct. If
$A_v-A_v^{-1}$ has full gcd and neither sign comparison factors, then
$A_v=s\in\{1,-1\}$ globally. The raw algebra

\[
 R[X_v]/((X_v-s)^2)
\]

has a nilpotent, so it cannot be called a constant coordinate algebra. Adding
the public linear equation $X_v=s$ and eliminating $X_v$ removes that
nilpotent without changing the $R$-valued roots. The candidate explicitly
limits its theorem to this linearly reduced system. Raw degenerate schemes
remain outside its scope.

The repeated-input case $u=v\ne w$ passes. When both remaining roots are
screened, the mismatch residual is

\[
 A_w-A_w^{-1}=A_u^2-A_u^{-2}\in R^\times,
\]

so the relation $X_w=X_u^2$ identifies the two normalized orientations.
A relation with at most one remaining nondegenerate variable cannot select an
orientation because both global public homomorphisms $E$ and $E^{-1}$
satisfy every genuine multiplicative relation.

The only unproved case in the written graph construction is the
output-constant case from Section 1 of this audit. Once that case is corrected,
every relation has corner values that are either zero or units. The full
coordinate algebra is then a product over Boolean assignments, and quotienting
by all relations retains exactly the assignments that are constant on each
connected component. It follows that one reduced component has algebra

\[
 R[f_j]/(f_j^2-f_j).
\]

Different components retain independent $f_j$. A shared eliminated constant
does not connect their remaining variables unless a reduced relation directly
does so. The candidate now states this correctly.

## 6. Shifted-root coherence and its quantifiers

For a screened shifted quadratic with public roots $A_i,B_i$, the change of
coordinate

\[
 Z_i=B_i+f_i(A_i-B_i)
\]

is valid because $A_i-B_i$ is a unit. The isolated quadratic gives one
independent idempotent $f_i$. It does not synchronize different shifts. The
candidate now says this explicitly.

For a section induced by one global $H$, the common-idempotent calculation is
correct. The $E$ and $E^{-1}$ sections select $A_i$ and $B_i$. Locally,
$G=E$ at $p$ and $G=E^{-1}$ at $q$, so the $G$-section has
$f_i=(1,0)$ under CRT for every retained screened pair. The
$G^{-1}$-section has the complementary idempotent. Thus all screened shifts
belonging to one such section use the same idempotent.

This is a conditional coherence statement. A family of quadratics is covered
only after explicit relations have been proved to put its variables in one
common-$f$ component, or when the discussion is restricted to the four
sections of one already assumed global $H$. Establishing such coherence is
not supplied by the quadratics. The candidate does not claim otherwise.

For literal quantifier safety, “for every shift” in Section 5 must mean “for
every retained screened shift.” At $k=0$, for example, the two public roots
coincide and the normalized $f_i$ is undefined. The surrounding screened scope
makes the intended meaning clear, but the corrected artifact should say it
explicitly.

## 7. Endpoint theorem and factor-free evaluation

Theorem 6.1 passes. In

\[
 \mathcal A=R[f]/(f^2-f),
\]

every class has the unique form

\[
 Q(f)=Q(0)(1-f)+Q(1)f.
\]

If both endpoints vanish, the class is zero. If the mixed idempotent
$e=(1,0)$ solves $Q(e)=0$, then

\[
 Q(1)=0\pmod p,\qquad Q(0)=0\pmod q.
\]

Consequently, any nonzero endpoint value has a proper gcd with $N$. The case
$e=(0,1)$ swaps the primes. For a finite system, if an endpoint fails, one
equation fails there and the same argument applies to that equation.

The endpoint evaluations are factor-free under the candidate's word
“explicit”: the coefficients and arithmetic expression must be available
from public data, and setting every component variable to its known $A$-root
or $B$-root requires neither $p,q$, nor $e=(1,0)$. A polynomial-time
algorithmic use also requires a polynomial-size arithmetic representation;
merely saying that there are polynomially many relations does not control the
size of each relation. The algebraic theorem itself is independent of this
representation issue and is correct.

The one-variable theorem cannot be applied to several independent $f_j$, to an
equation whose effect on those components has not been reduced, or to a system
with auxiliary existential witnesses. The candidate excludes all three cases.
It also excludes inequalities, canonical representative rules, random
root-selection laws, derivatives, and lifts. Therefore no forbidden
quantifier extension remains in Sections 6, 8, or 9.

## 8. Extraction and whether the result hides factoring

For a screened pair $A,A^{-1}$ and a nontrivial idempotent
$e\in\{(1,0),(0,1)\}$,

\[
 X=A^{-1}+e(A-A^{-1})
\]

agrees with $A$ at exactly one hidden prime and with $A^{-1}$ at the other.
Since $A-A^{-1}$ is a unit, the two comparison gcds are exactly $p$ and $q$.
Conversely, known factors construct the two nontrivial CRT idempotents and
therefore every mixed section. This is a deterministic polynomial-bit
equivalence on the stated promise.

So the mixed-root task does re-express factoring. The candidate is honest
about this: it calls the result an extraction theorem, not a construction. The
anchor sampler, the coordinate algebra, and the endpoint theorem never produce
a nontrivial idempotent. They show only that a one-component explicit
polynomial equation is either true at both public endpoints, exposes a factor
through a public endpoint gcd, or still asks for that idempotent.

The result therefore does not prove the fixed factoring statement. It covers
only distinct odd semiprimes and only the screened, linearly reduced,
one-common-idempotent polynomial interface. Prime powers, repeated prime
factors, even inputs, products of three or more primes, recursion, success
probability for a mixed-root solver, and a uniform Las Vegas bit bound remain
open exactly as the candidate says.

## 9. Exact required corrections

Before this candidate can receive a clean hostile audit:

1. Replace Section 5, item 3, by separate constant-input and constant-output
   cases. In the output-constant case use $s=X_uX_v$, equivalently
   $X_v=sX_u^{-1}$, and give the normalized four-corner calculation that
   proves $f_v=f_u$. Do not state $X_v=sX_u$ for that case.
2. Update the sentence after the case list so that its unit-mismatch proof
   explicitly covers both positions of the constant. The $N=77$ example above
   must no longer contradict any displayed reduced equation.
3. Qualify the shifted-section phrase “for every shift” as “for every retained
   screened shift,” because a degenerate shift has no normalized idempotent
   coordinate.
4. Qualify Section 6's comparison sentence to use a returned screened
   coordinate in the same mixed section/component. A separately sampled
   public anchor does not by itself supply the corresponding mixed value.
5. If the endpoint conclusion is stated algorithmically, define an explicit
   relation as a public, factor-free, polynomial-size arithmetic expression.
   This prevents hidden factor-dependent coefficients or exponentially large
   expressions from being counted as a polynomial-time endpoint test.

The first two items repair the remaining mathematical proof gap. The last
three make the existing screened, same-component, factor-free quantifiers
literal. No change to the candidate's narrow endpoint theorem is otherwise
required. Because the proof case changes mathematically, the corrected
artifact requires a new clean hostile audit before any proof-blind
reconstruction or promotion.

FAIL AS WRITTEN
