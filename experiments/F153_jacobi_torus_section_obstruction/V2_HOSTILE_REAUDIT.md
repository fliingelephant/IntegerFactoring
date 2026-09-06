# F153 V2 hostile re-audit — PASS after the section-scope repair

## Verdict

**PASS.** V2 repairs the material error in V1. It now proves only that the
Jacobi orientation is one character on the base square-class space. It also
states explicitly that this character does not determine a decorated
section. The exact section quotient, the `N=15` countermodel, all displayed
torus identities, the cross-discriminant algebra, and the large-order
homomorphism boundary are correct under the stated hypotheses.

This remains a narrow semiprime method classification. It is not a factoring
algorithm, a source theorem, or a lower bound for all coordinate algorithms.

## Frozen inputs

The requested hashes match exactly:

- `V2_STATEMENT.md`:
  `6bba6be5b6f8dd9f2a4810f7182fbc400029cc5026b55224809835a186123b3a`;
- `V2_PROOF.md`:
  `9fa532e12483b38497987fa798711ae69e356938c75c93836d5cf41a538c451d`.

I read the preserved V1 failed audit in full. I did not modify a frozen input
or a durable ledger.

## 1. The V1 failure is repaired

Equations (2)--(3) prove exactly that

\[
 [D]\longmapsto (D/p)
\]

is one character on the generated discriminant square-class space. V2 no
longer infers that this character selects a unique lift. Instead, for two
sections over the same parity span, it records the remaining kernel map

\[
 h_1h_2:W\longrightarrow R_N/\{+1,-1\}.
\]

This is correct because the repaired F152 quotient is an abelian
exponent-two group. The product of the two lifts has parity zero, and the
product is a homomorphism. For a distinct odd semiprime, a nonzero class in
this kernel is represented by a non-global square root of one and its sign
gcds factor `N`.

The exact cautionary example also checks:

\[
N=15,
\qquad
2^2\equiv7^2\equiv19\pmod {15},
\]

\[
2\cdot7\cdot19^{-1}\equiv11\pmod {15},
\qquad
\gcd(10,15)=5,
\qquad
\gcd(12,15)=3.
\]

Thus equal orientation characters can coexist with incompatible decorated
sections. V2 uses this fact rather than denying it.

## 2. Discriminant-word formulas

For every integer exponent, multiplicativity of the Legendre symbol gives

\[
\left(\frac Fp\right)=\eta,
\qquad
\left(\frac Fq\right)=(-1)^\delta\eta.
\]

Negative exponents cause no exception because every discriminant is a unit.
Equal local square classes have equal character values. If the unit word is
a square modulo `N`, both local symbols are one, so `eta=1` and `delta=0`.
These statements concern only the base character, as V2 now says.

## 3. The signed-gap halving

With

\[
m_p=p-\epsilon,
\qquad
m_q=q+\epsilon,
\qquad
g=q-p,
\]

direct expansion gives

\[
m_pm_q=N-1-\epsilon g.
\]

Each local torus is cyclic of the displayed order. Since both orders are
even, `m_p*m_q/2` remains divisible by each one. Hence, for every torus
point,

\[
U^{N-1}=U^{\epsilon g},
\qquad
U^{(N-1)/2}=U^{\epsilon g/2}.
\]

No generator assumption is used. A second uniform division by two through
the same exponent argument would need `4` to divide `m_p`, `m_q`, and `g`.
The first two conditions imply

\[
g\equiv-2\epsilon\pmod4,
\]

which contradicts the third. The statement correctly limits this obstruction
to the direct universal exponent-division argument. It does not rule out
extra halves for a selected point.

## 4. Cayley halving

The Cayley product law and its doubling specialization are correct:

\[
U_D(a)U_D(b)
=U_D\!\left(\frac{a+b}{1+Dab}\right),
\]

\[
U_D(s)^2=U_D(t)
\iff
Dt s^2-2s+t=0
\]

on the named unit branch. The quadratic discriminant is
`4(1-Dt^2)`. The substitutions

\[
r=1-Dts,
\qquad
s_\pm=\frac{1\pm r}{Dt}
\]

are mutually inverse and give `r^2=1-Dt^2`. The clean denominator
assumptions also make `r` a unit. Opposite global roots select local halves
which differ by the unique nonidentity two-torsion point `-1` in both
components. Mixed roots have a non-global root-of-one quotient and already
factor `N`. The exclusions and gcd screens are stated narrowly enough.

## 5. Product discriminants and relative norms

For `F=DE`, both local characters equal

\[
\eta=\epsilon(D)\epsilon(E).
\]

The local torus orders are `p-eta` and `q-eta`, and

\[
(p-\eta)(q-\eta)
=N-1-\eta(p+q-2\eta).
\]

Therefore every `W in T_F` obeys

\[
W^{N-1}=W^{\eta(p+q-2\eta)}.
\]

The two branches are exactly `p+q-2` and `-(p+q+2)`.

The conjugation-preserving algebra-map classification is also exact. Writing
the image of `w_D` as `a+bw_E`, compatibility with conjugation forces
`a=0`, and preservation of the defining equation forces

\[
b^2=D/E.
\]

Such a unit exists modulo `N` exactly when the two hidden orientations are
equal. Globally opposite roots differ by conjugation. Any two roots which
are not global opposites have a non-global root-of-one quotient.

In the free rank-four algebra, the three sign involutions have the stated
fixed rank-two subalgebras. Applying them to `UV` gives exactly

\[
\operatorname{Nm}_{B/A_D}(UV)=U^2,
\quad
\operatorname{Nm}_{B/A_E}(UV)=V^2,
\quad
\operatorname{Nm}_{B/A_F}(UV)=1.
\]

These formulas classify only the displayed relative norms. V2 explicitly
leaves non-norm coordinate operations open.

## 6. P55 and P57 attribution

The attribution is accurate and conservative.

- P55 already proves the general local order formula
  `|T_D(F_r)|=r-(D/r)` and the Jacobi-minus-one signed-gap identity. Equation
  (14) is an immediate product-discriminant use of that formula, not a new
  order principle.
- When `eta=1`, both local tori split. Under the split-torus identification,
  equation (14) is P57's ordinary `p+q-2` power identity.
- The explicit all-nonsplit `-(p+q+2)` companion is not recorded in P55 or
  P57. It is a correct repository increment, but it supplies neither its
  branch bit nor its hidden exponent.

## 7. Ordinary high order

For nonsquare `D modulo r`, the source and target orders are `r-1` and
`r+1`. The order of any homomorphic image divides both, hence divides two.
This proves exactly that an ordinary large-order certificate cannot retain
large order through a homomorphism into the nonsplit local torus.

This theorem must not be read more broadly. It does not prove that every
order-two image is useless, and it does not cover a non-homomorphic
coordinate map or a torus-native large-order algorithm. V2 states those
limits. Its Kummer calculation is also correct under the cited F151
nondegeneracy conditions: `x^2-1` is a local square, so
`D^{-1}(x^2-1)` has character `(D/r)`, while the retained `x` coordinate has
only the discriminant-free Chebyshev relations.

## 8. Quasipolynomial scope

F153 makes no running-time or success-probability claim for a factoring
algorithm. Its two quasipolynomial phrases are proposed next gates:

1. construct an explicit coordinate map in quasipolynomial work; or
2. prove inverse-quasipolynomial density for a factor-correlated invariant.

Neither is asserted as achieved. An inverse-quasipolynomial success bound
would still need efficient verification, repetition, total bit-length
control, and an all-input extension before it could meet the repository's
fixed goal. F153 claims none of these.

The phrase “smallest live algebra” is research prioritization, not a proved
minimality theorem. The audited mathematical result is only the exact
rank-four construction and the failure of its three relative norms.

## Final scope

The repaired result proves an operation-specific boundary for distinct odd
semiprimes. It does not prove that a common decorated section is forced by
Jacobi orientation, and it does not rule out an additional coordinate,
carry, lift, determinant, resultant, derivative, or non-norm invariant.
Within this exact scope, no remaining mathematical error was found.

A fresh statement-only blind reconstruction is now appropriate.
