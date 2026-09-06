# F276 V2 author self-audit

## Verdict

`PASS` as a corrected narrow proof-only candidate. Frozen V1 is preserved.
Fresh hostile and statement-only audits of V2 are required before promotion.

V1 overreached in one methodology sentence: reduction of the affine `c=0`
branch to constant powering does not prove that every public constant matrix
lacks a factor signal. V2 removes that claim. It preserves the proved
reduction and leaves separately justified constant-power candidates open.

## 1. Claim-to-proof check

1. The rational endpoint theorem is the pair-groupoid cocycle identity with
   one endpoint fixed. It proves a full matrix gauge, not only a determinant
   condition.
2. The separable length theorem is induction on the additive monoid. The
   determinant-one refinement uses the limit of a rational shift quotient
   and the absence of nonconstant rational periodic functions in
   characteristic zero.
3. The direct-summand theorem expands the transformed determinant along its
   first column. It uses a polynomial unimodular frame essentially.
4. Coordinate-ideal preservation uses both `M` and `M^{-1}`. It controls a
   whole state, row, or column, not a selected entry.
5. The affine `SL_2` theorem compares the three determinant coefficients and
   then uses the `2 by 2` Cayley-Hamilton identity. Its scalar recurrence is
   derived without commuting any ordered factors.
6. The rational factorial and Jordan examples are exact positive controls,
   but each fails an operational resource or unit gate.

## 2. Orientation and endpoint check

The product convention is

\[
 \Pi_A(a,m)=A(a+m-1)\cdots A(a).
\]

Thus adjacent products compose as `P(y,z)P(x,y)=P(x,z)`. The gauges in
Theorems A and B have the matching orientation

\[
 P(x,y)=G(y)(\cdots)G(x)^{-1}.
\]

No factor order was reversed in the proofs.

## 3. Denominator audit

Determinant one does not prove that the entries of a rational matrix or its
gauge are defined modulo `N`. Constant `det G` also does not remove
entrywise denominators. The statement requires a denominator-free normal
form or a gcd audit before every modular inverse.

The example `diag(X,X^{-1})` deliberately fails at `X=p`; it is retained as
the smallest algebraic control, not accepted as an algorithm.

## 4. Constant-alias audit

Theorem B does not call every constant power a decoy. A constant matrix can
have a factor-bearing entry. The Jordan control proves this explicitly.
The exact conclusion is that the varying interval has reduced to a
constant-power problem, whose state, construction, and selected-entry costs
must be counted independently.

For the Jordan control, explicit dimension is `H+1`, while an implicit
selected-entry query is precisely `binom(B,H)`. No QP evaluation claim is
made.

## 5. Affine-normal-form audit

The affine theorem is confined to one matrix `C+XD` in dimension two. The
factorization `C(I+XB_0)` does not make factors at different indices commute.
Only the `c=0` branch becomes upper triangular after the fixed rational
basis. The `c!=0` branch remains the ordered recurrence

\[
 y_{k+2}=(ck+a+c+d)y_{k+1}-y_k.
\]

No claim is transferred to quadratic entries, higher dimension, or a word
of several shears per step.

## 6. Semilinear boundary

Theorem A covers rational dependence on the two endpoints. Theorem B covers
a rational gauge times a length state that is a representation of the
ordinary additive monoid. It does not cover:

- a digit automaton whose merge law depends on scale;
- Frobenius or another characteristic-dependent semilinear map;
- floors, branches, or adaptive state;
- a nonlinear algebraic-group state not presented by (5); or
- an implicitly represented state of remote dimension.

Therefore F276 is not a general semilinear classification.

## 7. Search and evidence boundary

No C++ source, checker, compile, benchmark, local run, remote run, corpus, or
empirical result belongs to this packet. The named grammar has no candidate
that simultaneously passes `LOCAL`, `STATE`, `ENDPOINT`, `UNIT`, and
`SIGNAL`, so no resource-bearing search is authorized.

The generic affine branch remains open. A future search becomes justified
only after it supplies a proposed numerical-QP endpoint operation and an
exact target asymmetry, rather than only small-index divisibility samples.
The reducible branch is not a new varying-interval mechanism, but a separate
constant-power candidate can be studied if it supplies its own exact signal
law and construction-cost audit.

## 8. Deliberate nonclaims

F276 proves no general `SL_d` lower bound, no lower bound for arithmetic
circuits, no evaluator lower bound from holonomicity, no failure theorem for
the generic affine continuant, and no factoring algorithm.

