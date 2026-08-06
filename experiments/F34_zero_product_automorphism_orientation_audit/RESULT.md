# F34 hostile audit: the semiprime automorphism obstruction is sound

**Audit verdict:** pass on the mathematical obstruction, with required
precision corrections before promotion.  I found no counterexample to the
field classification, CRT orientation dichotomy, factor extraction,
factor-free invariant, count, or total-variation conclusion.  The required
corrections concern the computational representation of an automorphism and
one ambiguous scope sentence; they do not change the theorem.

**Audited artifact:**
`experiments/F34_zero_product_automorphism_orientation_kill/RESULT.md`.

**Method:** proof-only hostile audit; no computation was used.  I read the
fixed `PROMPT.md`, `STATEMENT.md`, the F23 entries in `REGISTRY.md`,
`FAILED.md`, and `notes/Progress.md`, promoted result P41 in `PROVED.md`, and
the directly relevant F33 candidate.  F34's proof below does not rely on
F33's unverified status: the needed zero-product definitions and counts are
rederived.

## 1. Findings

No fatal mathematical finding was found.

1. **Required precision correction — circuit complexity.**  The sentence
   claiming “polynomial bit time” for an “explicit polynomial or branch-free
   arithmetic circuit” must specify the input measure and gate model.  The
   correct statement is polynomial in

   \[
   \log N+\text{the encoded circuit/formula length},
   \]

   for a division-free straight-line circuit over
   \(\mathbb Z/N\mathbb Z\) with \(+,-,\times\) gates (and any explicitly
   defined succinct power gates).  It becomes polynomial in \(\log N\) only
   when the sampler uniformly constructs circuits of size and coefficient
   bit length \(\operatorname{poly}(\log N)\).  Division/rational circuits,
   branching programs, and black-box evaluators are not covered without a
   new representation theorem.

2. **Required proof clarification — intrinsic first jet.**  The candidate's
   formal-differentiation claim is correct, but it should be justified in the
   quotient rather than by an unstated normal-form or cancellation
   assumption.  The intrinsic argument in Section 4 below supplies this.
   It also establishes explicitly that \((K,X)\) is fixed over
   \(R=\mathbb Z/pq\mathbb Z\), which is needed for congruence (0.1).

3. **Required wording correction — all-input scope.**  Item 6 should be split.
   F34 does not classify automorphisms over prime powers or general
   nonsquarefree bases.  Nevertheless, its obstruction on distinct
   semiprimes is enough to refute an *all-input automorphism-only sampler of
   the stated explicit, factor-free-start model*, because such a sampler must
   also work on those semiprimes.  It does not refute an all-input sampler
   which uses one of the excluded move types.

4. **Minor wording only.**  “Randomizing over automorphisms only randomizes a
   global preserve/swap bit” should read “as far as local-axis orientation is
   concerned.”  Unit scalings are of course randomized too; they simply do
   not change the invariant.

These are not refutations, so the failed-audit rule is not triggered.  A
broadened claim covering division circuits, black-box maps, finite-set
permutations, or nonsquarefree bases would be new mathematical content and
would require a fresh audit.

## 2. Field classification survives

Let

\[
A_F=F[K,X]/(KX).
\]

The equality

\[
(K)\cap(X)=(KX)
\]

in \(F[K,X]\) shows simultaneously that \((KX)\) is radical, that the two
minimal primes of \(A_F\) are

\[
P_K=(K),\qquad P_X=(X),
\]

and that \(P_K\cap P_X=0\) inside \(A_F\).  This is valid in every
characteristic, including characteristic two.

Every \(F\)-algebra automorphism permutes the two minimal primes and hence
fixes their sum

\[
\mathfrak m=P_K+P_X=(K,X).
\]

If \(P_K,P_X\) are preserved, the induced automorphisms of
\(A_F/P_X\simeq F[K]\) and \(A_F/P_K\simeq F[X]\) preserve the respective
origin ideals.  An \(F\)-algebra automorphism of \(F[T]\) sends \(T\) to
\(aT+b\) with \(a\ne0\): if substitution polynomials \(f,g\) are inverse,
then \(1=\deg(f\circ g)=\deg f\deg g\).  Origin preservation forces
\(b=0\).  Therefore

\[
\phi(K)\equiv uK\pmod{P_X},\qquad
\phi(X)\equiv vX\pmod{P_K}
\]

with \(u,v\in F^\times\).  Since both differences also lie in the other
minimal prime, zero intersection gives the exact equalities

\[
\phi(K)=uK,\qquad \phi(X)=vX.
\]

If the primes are swapped, \(\phi\) induces origin-preserving isomorphisms
between the two polynomial-ring quotients rather than endomorphisms of each
one.  Applying the same degree argument and then zero intersection gives

\[
\phi(K)=uX,\qquad \phi(X)=vK.
\]

Thus the preserve/swap classification is exhaustive.  There is no finite-
field exception: a polynomial which merely induces a permutation of the
finite zero-product point set need not be an automorphism of this coordinate
ring, and the candidate explicitly excludes that different model.

The apparent contravariance of `Spec` creates no gap.  The induced point map
associated with a pullback \(\phi\) sends an evaluation \(s:A_F\to F\) to
\(s\circ\phi\), so its coordinates are obtained by evaluating
\(\phi(K),\phi(X)\).  Replacing \(\phi\) by its inverse would in any event
leave the preserve/swap bit unchanged.

## 3. CRT dichotomy and global form survive

Let \(R=\mathbb Z/pq\mathbb Z\) for distinct primes.  CRT gives an
injective, indeed isomorphic, decomposition

\[
A_R\simeq A_{\mathbb F_p}\times A_{\mathbb F_q}.
\]

An \(R\)-algebra automorphism fixes the base idempotents, and base change of
it and its inverse gives automorphisms \(\Phi_p,\Phi_q\) of the two field
factors.  The field result therefore applies independently in the two
components.

It follows first that both reductions of \(\Phi(K),\Phi(X)\) have zero
constant term.  CRT then makes the global constant terms zero, so
\(\Phi(K),\Phi(X)\in(K,X)\); applying the same argument to \(\Phi^{-1}\)
shows that \((K,X)\) is fixed.  Hence the first-jet matrix \(J_\Phi\) is
well-defined.

If, for example, the \(p\)-map preserves and the \(q\)-map swaps, its four
entries have supports

\[
\begin{array}{c|cccc}
&a&b&c&d\\ \hline
\bmod p&\ne0&0&0&\ne0\\
\bmod q&0&\ne0&\ne0&0.
\end{array}
\]

Thus \(a,d\) are divisible by \(q\) and not by \(p\), while \(b,c\) are
divisible by \(p\) and not by \(q\).  Computing ordinary integer gcds with
\(N\) recovers \(q,q,p,p\), respectively.  The reverse orientation reverses
the roles.  No knowledge of \(p\) or \(q\) is used by the extractor.

Conversely, an entry of \(R\) whose gcd with \(N\) is not proper is either a
unit (nonzero in both field components) or zero (zero in both).  If all four
entries have this property, the two local monomial support patterns cannot
differ.  Therefore the orientations are synchronized.

The stronger global conclusion is also valid.  In the preserving case,
choose CRT lifts \(u,v\in R^\times\) of the two pairs of nonzero local
scalars.  Both components of \(\Phi(K)-uK\) and
\(\Phi(X)-vX\) vanish; injectivity of the displayed CRT decomposition gives

\[
\Phi(K)=uK,\qquad \Phi(X)=vX.
\]

The swapping case is identical.  This avoids the candidate's slightly
informal phrase “all coefficients vanish”: no particular polynomial normal
form is needed.  In fact the same argument shows that even a mixed
orientation automorphism is globally linear, with a matrix whose reduction
in each field is monomial; F34 only needs the synchronized specialization.

## 4. Jacobian extraction is valid under the corrected model

There is a canonical quotient

\[
A_R\longrightarrow
B:=R[K,X]/(K,X)^2,
\]

because \(KX\in(K,X)^2\).  Consequently the constant and linear parts of an
element of \(A_R\) are independent of the chosen raw polynomial
representative.  Adding a multiple of \(KX\), reducing intermediate
products by \(KX=0\), or performing polynomial cancellations cannot change
the first jet.

For a division-free circuit, evaluate every gate directly in \(B\), storing
a triple \((c,\alpha,\beta)\) for \(c+\alpha K+\beta X\).  Addition is
componentwise and multiplication is

\[
(c,\alpha,\beta)(c',\alpha',\beta')
=
(cc',\;c\alpha'+c'\alpha,\;c\beta'+c'\beta).
\]

This takes a constant number of arithmetic operations modulo \(N\) per
gate.  Equivalently, \(\alpha,\beta\) are the two formal derivatives at the
origin.  The four linear coefficients of the two output gates are exactly
\(J_\Phi\), even if the submitted raw formulas are not in quotient normal
form and even in positive characteristic.

For a circuit of encoded size \(s\), this costs \(O(s)\) ring operations and
bit time polynomial in \(s+\log N\), followed by four polynomial-time integer
gcds.  This is polynomial in the factoring input length only when
\(s=\operatorname{poly}(\log N)\), as any claimed polynomial-time transition
builder must ensure.  No expansion to the possibly enormous formal degree is
needed.

Efficient certification that an arbitrary circuit is an automorphism is not
used in the implication.  Semantically, if the submitted map really is an
automorphism, the theorem applies and its first jet is extractable.  A
factoring/sampling construction must prove that semantic premise for its own
maps.  If it instead supplies only an opaque evaluation oracle, a rational
expression not regular at the node, or a finite-set permutation, it has left
F34's stated model.

## 5. The invariant, adaptivity, and warm starts survive

For any residue \(z\bmod N\),

\[
\gcd(z,N)\in\{1,N\}
\]

holds exactly when \(z\) is a unit or \(z=0\).  If \(kx=0\), two units are
impossible.  Hence the pairs with no proper coordinate gcd are exactly

\[
\mathcal A_N=
(R^\times\times\{0\})\ \dot\cup\
(\{0\}\times R^\times)\ \dot\cup\
\{(0,0)\}.
\]

Multiplication by a unit and coordinate swapping preserve zero and the unit
set.  Every synchronized automorphism therefore preserves
\(\mathcal A_N\), and, being bijective, preserves its complement as well.
This is pointwise, so it remains true when the next global automorphism is
chosen adaptively from the entire preceding history or at random.  If a
chosen automorphism has mixed local orientation, the four-gcd test factors
\(N\) before the move; otherwise membership in \(\mathcal A_N\) cannot
change.  State-dependent mixture weights do not affect this conclusion.

The warm-start boundary can be stated more strongly than in the candidate.
If an explicit polynomial-time initializer has probability \(\varepsilon\)
of landing outside \(\mathcal A_N\), simply taking the two coordinate gcds
is already a factor attempt of success \(\varepsilon\).  On a no-mixed-map
run, subsequent synchronized automorphisms cannot increase that probability.
Thus an inverse-polynomial \(\varepsilon\) is itself a Las Vegas factoring
route by verified repetition, while negligible \(\varepsilon\) cannot
approach a target having more than one-half mass outside the invariant set.
This is a scope boundary, not a loophole in the start-in-\(\mathcal A_N\)
theorem.

## 6. Counting and total variation survive exactly

At a prime \(r\), the zero-product set is the union of two axes and has
\(2r-1\) points.  CRT therefore gives

\[
|\Omega_{pq}|=(2p-1)(2q-1).
\]

The three disjoint pieces of \(\mathcal A_N\) have

\[
|\mathcal A_N|=2\varphi(N)+1=2(p-1)(q-1)+1.
\]

Subtraction gives

\[
|\Omega_N\setminus\mathcal A_N|=2pq-2=2N-2.
\]

Moreover,

\[
2(2N-2)-(2p-1)(2q-1)=2p+2q-5>0,
\]

including the characteristic-two case \(\{p,q\}=\{2,3\}\).  Hence the
uniform useful-pair mass is strictly greater than \(1/2\).  If \(\mu\) is
supported on \(\mathcal A_N\), the event
\(\Omega_N\setminus\mathcal A_N\) immediately yields

\[
\|\mu-\pi\|_{\mathrm{TV}}
\ge \pi(\Omega_N\setminus\mathcal A_N)>\frac12.
\]

No stationarity, independence, or mixing-time premise is hidden in this
argument.

## 7. Scope limits are genuine and correctly preserved

The following are not adverse findings; they are mathematically different
models.

- **Endomorphisms/noninvertible moves.**  Minimal-prime permutation and the
  quotient-isomorphism argument use invertibility.  A noninvertible
  polynomial update or stochastic kernel is not classified.
- **Finite-set permutations.**  Especially over finite fields, distinct
  coordinate-ring elements may induce the same function on rational points,
  and nonlinear permutation functions need not be scheme automorphisms.
  F34 deliberately concerns the latter.
- **Auxiliary kernels and lifted chains.**  Projections of moves on a larger
  state space need not act as automorphisms of \(A_R\), so the invariant need
  not apply.
- **Opaque or branch-dependent maps.**  An evaluator with no accessible
  polynomial circuit, or a state-wise branch that is not merely a choice
  among global automorphisms, lies outside the Jacobian-extraction claim.
- **Warm starts.**  They are handled only through their immediately readable
  useful mass, as explained above; F34 is not a construction or lower bound
  for arbitrary initializer generation.
- **Prime powers and nonsquarefree bases.**  Nilpotents invalidate the field
  lifting used for the global monomial form.  This exclusion is essential,
  not cosmetic: over \(\mathbb Z/4\mathbb Z\), for example,
  \(K\mapsto K+2K^2,\ X\mapsto X\) is a nonlinear automorphism of the node
  (it is its own inverse).  F34 makes no classification there.

The semiprime theorem is nevertheless uniform in distinct \(p,q\), does not
assume balance or oddness, and never uses the unknown factors in the
extractor.

## 8. Novelty and final disposition

P41 closes uniform rejection, direct uniform-gcd discovery, and one
independence-Metropolis chain.  F33 studies random-scan coordinate heat bath.
F34 instead proves an exact orbit obstruction for arbitrary nonlocal,
adaptive compositions of explicit coordinate-algebra automorphisms.  This
is a materially distinct and strictly structural negative result.  Its
scope statement correctly leaves noninvertible, finite-set, augmented,
positive-matching, and other non-automorphism samplers open.

After making the representation and scope wording corrections in Findings
1--4, the candidate has survived this hostile audit and is suitable for the
required proof-blind reconstruction.  It is not a factoring algorithm and
does not close F23; it closes only the named automorphism-move subfamily.

## 9. Amendment verification

**AMENDMENT VERIFIED PASS.**

I checked the amended
`experiments/F34_zero_product_automorphism_orientation_kill/RESULT.md`
against every required correction above and scanned the complete patch for
regressions.  The candidate itself was not edited by this auditor.

1. **Fixed ideal and intrinsic first jet — verified.**  The amendment first
   obtains zero local constant terms from the field classification, uses CRT
   to place both global coordinate images in \((K,X)\), and repeats the
   argument for the inverse.  Those two inclusions prove equality of the
   ideal under the automorphism.  It then defines the first jet through the
   canonical quotient \(A_R/(K,X)^2\).  Because the defining relation
   \(KX\) lies in \((K,X)^2\), this is independent of raw representatives
   and does not assume a quotient normal form or invalid cancellation.

2. **Division-free circuit model and complexity — verified.**  The amended
   claim is expressly limited to straight-line circuits over \(R\) with
   \(+,-,\times\) gates and encoded residue constants.  Its triple rule

   \[
   (c,\alpha,\beta)(c',\alpha',\beta')
   =(cc',c\alpha'+c'\alpha,c\beta'+c'\beta)
   \]

   is exactly multiplication modulo \((K,X)^2\).  It uses constant work per
   gate, so the bit cost is polynomial in \(\log N\) plus the encoded circuit
   length, and the text now explicitly requires uniformly
   \(\operatorname{poly}(\log N)\)-size/encoding circuits for a factoring-
   time claim.  Division/rational circuits, branching descriptions without
   an accessible global automorphism circuit, and black-box evaluators are
   excluded.  No high-degree expansion is assumed.

3. **Global CRT equality — verified.**  The amended proof chooses CRT lifts
   of the two local nonzero scalars and invokes injectivity of
   \(A_R\simeq A_{\mathbb F_p}\times A_{\mathbb F_q}\) on the *elements*
   \(\Phi(K)-uK\) and \(\Phi(X)-vX\).  It no longer relies on informal
   coefficientwise vanishing or an unstated normal form.

4. **Orientation-only randomization — verified.**  The amendment qualifies
   the statement explicitly as one about local-axis orientation and notes
   that unit scalings may also vary.  This removes the prior literal
   overstatement without weakening the invariant.

5. **All-input semiprime scope — verified.**  Prime powers and nonsquarefree
   bases are now listed separately as unclassified.  The amended text
   correctly observes that failure on every distinct semiprime refutes an
   all-input sampler only when that sampler remains inside the explicit,
   automorphism-only, factor-free-start model on those inputs.  Samplers
   using excluded move types remain open.

6. **Regression scan — clean.**  Equation (2.3), its ring-operation count,
   the ideal argument, and the revised exclusions are mutually consistent.
   Adaptive or random selection among accessible global automorphisms remains
   covered; a state-wise branch which is not such a selection remains outside
   scope.  No new characteristic, contravariance, CRT, counting, gcd, or
   total-variation error was introduced.

The amended candidate therefore passes this hostile-audit stage and may
proceed to the required proof-blind reconstruction.  This verdict remains
limited to the exact semiprime automorphism obstruction and does not promote
F34 or the broader F23 sampler family by itself.
