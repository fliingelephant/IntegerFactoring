# F153 hostile audit — FAIL on the section inference

## Verdict

**FAIL, with one narrow but material scope error.**  The displayed character,
torus-order, halving, Cayley, cross-discriminant, relative-norm, and
high-order-homomorphism identities are correct under their stated algebraic
hypotheses.  I found no sign error in the new equation (14).

The failure is the inference in Theorem 1 that one hidden orientation
character prevents two multiplicative lift rules from producing an
F152-style section disagreement.  A character on the base square-class
space does not select a unique section of the decorated extension.  Two
homomorphic sections over the same base character can differ by a nonzero
homomorphism into the root-of-one kernel.  That difference is exactly the
signal which F152 decodes.

This does not invalidate Theorems 2--5.  It means that their explicit
operation-by-operation obstructions cannot be upgraded to the broader title
and conclusion by character linearity alone.

## Frozen inputs

The requested hashes match exactly:

- `STATEMENT.md`:
  `f38c3a1558b7f2509a8fadfc7518ace67ef6fcb7522be003961c690ab0723419`;
- `PROOF.md`:
  `c6b612da25b716c44fc1844141509769d83c26f7e342047a29bfb90617de6ff6`.

I did not modify either frozen input or a durable ledger.

## 1. Exact point of failure

Equations (2)--(3) correctly prove that

\[
 [D]\longmapsto (D/p)
\]

is one linear character on the generated discriminant square-class span.
They also correctly prove that two word presentations of the same local
square class have the same value of this character.

They do **not** prove these later sentences:

> any relation-lift rule whose only hidden datum is the discriminant
> orientation factors through one homomorphism on the generated squareclass
> span;

and

> two such multiplicative rules cannot force an F152-style section
> disagreement.

The first sentence is ambiguous between “factors through the character” and
“is the same decorated section.”  The second sentence needs the latter, but
only the former was proved.

Formally, let `W` be the common parity span and let

\[
 0\longrightarrow K\longrightarrow \overline E
 \longrightarrow W\longrightarrow0
\]

be the F152 decorated extension.  If `h_1` and `h_2` are two sections, then

\[
 h_1h_2:W\longrightarrow K
\]

is a homomorphism.  It need not be zero.  Knowledge that both rules use the
same base character says nothing which forces this kernel homomorphism to
vanish.

### Small exact countermodel to the inference

Take

\[
 N=15,\qquad q_1=19,\qquad W=\mathbf F_2.
\]

The exact block `19` is a nonsquare integer, is a unit modulo `15`, and
satisfies

\[
 19\equiv4\pmod {15}.
\]

Both `2` and `7` are supplied square roots of this same public square class:

\[
 2^2\equiv7^2\equiv19\pmod {15}.
\]

Therefore

\[
 h_1(1)=\overline{(1,2)},
 \qquad
 h_2(1)=\overline{(1,7)}
\]

define two homomorphic F152 sections on the same one-bit base.  Their lift
quotient is

\[
 2\cdot7\cdot19^{-1}\equiv11\pmod {15},
 \qquad 11^2\equiv1\pmod {15}.
\]

It is non-global, and

\[
 \gcd(11-1,15)=5,
 \qquad
 \gcd(11+1,15)=3.
\]

This is not a factoring source and does not contradict any explicit torus
identity in F153.  It is a counterexample to the logical claim that a single
base character, by itself, rules out section disagreement.  To obtain that
conclusion, F153 must prove that the two operations induce the **same lift
map**, not only the same orientation character.

## 2. Character formulas

For every discriminant word,

\[
 \left(\frac Fp\right)=\eta,
 \qquad
 \left(\frac Fq\right)=(-1)^\delta\eta
\]

follows directly from multiplicativity of the Legendre symbol.  Equal local
square classes give equal `eta`.  If the word is square modulo both hidden
primes, then `eta=1` and `delta=0`.  These exact claims pass.

The safe conclusion is narrower:

> Discriminant orientation is one well-defined character and therefore
> cannot itself distinguish two presentations of the same local square
> class.

It does not determine the decorated lift attached to that presentation.

## 3. P55 exponent halving

With

\[
 m_p=p-\epsilon,
 \qquad m_q=q+\epsilon,
\]

the identity

\[
 N-1-\epsilon(q-p)=m_pm_q
\]

is correct.  Both local orders are even, so `m_p*m_q/2` remains divisible by
each order.  Hence both pointwise identities

\[
 U^{N-1}=U^{\epsilon(q-p)},
 \qquad
 U^{(N-1)/2}=U^{\epsilon(q-p)/2}
\]

are valid for every torus point, including nongenerators.

The obstruction to a second uniform division is also correct.  A pointwise
quarter identity obtained by the same exponent division would require
`4 | m_p`, `4 | m_q`, and `4 | q-p`.  The first two conditions imply

\[
 q-p\equiv-2\epsilon\pmod4,
\]

which contradicts the third.  The statement correctly limits this to the
direct exponent-division proof; it does not claim that individual points
cannot have further halves.

## 4. Cayley halving

The Cayley law gives

\[
 U_D(s)^2=U_D(t)
 \iff Dt s^2-2s+t=0
\]

on the clean unit branch.  The discriminant is `4(1-Dt^2)`.  The
substitution

\[
 r=1-Dts
\]

gives `r^2=1-Dt^2`, and the inverse formula

\[
 s=(1\pm r)/(Dt)
\]

is correct.  A solution cannot introduce a zero `1+Ds^2` denominator in
either local field.

Opposite global roots select halves which differ by the global torus point
`-1`.  Mixed CRT roots have a quotient which is a non-global square root of
one, so their sign gcds already factor `N`.  These claims pass.

## 5. The new cross-discriminant exponent identity

For `F=DE` and `eta=epsilon(D)epsilon(E)`, both local characters of `F` are
`eta`.  Therefore the local torus orders are `p-eta` and `q-eta`, and

\[
 (p-\eta)(q-\eta)
 =N-1-\eta(p+q-2\eta).
\]

It follows pointwise that

\[
 \boxed{W^{N-1}=W^{\eta(p+q-2\eta)}}.
\]

The two signs in the statement are correct:

- same orientations: `eta=1`, exponent `p+q-2`;
- opposite orientations: `eta=-1`, exponent `-(p+q+2)`.

This identity is a correct repository increment, but its conceptual novelty
is limited.  It is an immediate application of P55's already-promoted local
order formula `|T_F(F_r)|=r-(F/r)`.  The `eta=1` branch is also the split
torus form of P57's ordinary `p+q-2` power identity.  The explicitly written
all-nonsplit `-(p+q+2)` branch is new in the repository, but it uses the same
order-product mechanism and supplies neither `eta` nor the hidden sum.  It
is a useful boundary identity, not a new factor source.

## 6. Cross-discriminant algebra and norms

A conjugation-preserving `R`-algebra map must send

\[
 w_D\longmapsto b w_E,
 \qquad b^2=D/E.
\]

The map is an isomorphism exactly when such a unit `b` exists.  For two
Jacobi-minus-one discriminants this is equivalent to equal orientations.
The synchronized roots `b,-b` differ by global conjugation.  A mixed pair
has a non-global root-of-one quotient and therefore factors.

In the biquadratic algebra, the three stated involution norms of `UV` are
indeed

\[
 U^2,\qquad V^2,\qquad1.
\]

Thus the specific product-plus-relative-norm operation produces no new
cross lift.  The exclusions for non-norm coordinate operations are stated
correctly.

## 7. High-order transfer

For nonsquare `D` modulo an odd prime `r`, the source and target orders are
`r-1` and `r+1`.  Every group-homomorphic image has order dividing their
gcd, which is two.  Thus an ordinary high-order certificate cannot be
preserved in the nonsplit local component by such a homomorphism.  F153 also
correctly leaves non-homomorphic coordinate maps and a torus-native
large-order algorithm open.

The Kummer-coordinate statement repeats the already-audited F151 boundary
and is correct under that boundary's nondegeneracy assumptions.

## 8. Independent finite check

I performed an exact exhaustive check over every pair of distinct odd primes
through `31`, both local orientations, every local torus point, and every
clean Cayley parameter in those fields.  The check covered:

- 2,844 local P55 gap and half-exponent cases;
- 2,844 local cross-discriminant sum-exponent cases; and
- 2,752 Cayley halves.

It found no failed identity or exceptional sign branch.  This finite check
supports the algebraic proofs; it does not repair the section inference.

## Required repair

Preserve this failed version.  A repaired version can keep all exact
equations and operation-specific obstructions, but it must do both of these:

1. replace the generic no-disagreement claim by the proved statement that
   orientation is one well-defined base character; and
2. limit the final no-disagreement conclusion to each explicitly analysed
   lift operation, unless equality of two induced decorated sections is
   separately proved.

The repaired title should not say that character compatibility alone
prevents a section disagreement.  After this scope repair, a fresh hostile
re-audit and a fresh statement-only reconstruction are appropriate.
