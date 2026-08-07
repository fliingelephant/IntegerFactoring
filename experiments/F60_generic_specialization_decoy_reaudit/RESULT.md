# F60 corrected candidate — fresh whole-artifact hostile re-audit

**Candidate:** `experiments/F60_generic_specialization_decoy/RESULT.md`
**Verified candidate SHA-256:**
`804d0776a1ba446b3e604cb19a7b6abdae4ed052589ae62723bf23b6e48b6c93`
**Verdict:** **PASS**, with the narrow scope stated by the candidate.

I read the failed first audit before the corrected candidate. I treated all
eight required corrections from that audit as binding. I then checked the
corrected proof from the definitions, recomputed the retained F59 artifact
hashes, and inspected the D02 provenance records and D03 symbolic source and
output. I did not run a research computation.

The corrected result proves a conditional source filter. It does not prove
that the quotient is nonzero, that a nonzero quotient has a non-global root,
or that any all-input polynomial-time sampler creates such a root.

## 1. Binding corrections

All eight required corrections are present and mathematically effective.

1. The general quotient is now (K_N/U_N), not
   (K_N/K_{\rm gen}).
2. The text explicitly gives a generic useful relation with
   (gcd(d_c,N)=N), so a specialization gap is no longer claimed to be
   necessary.
3. The result says that a useful relation can be specialization-only or
   generic with a nonunit root denominator.
4. It identifies (K_N/K_{\rm gen}) with the factor-bearing quotient only
   under the extra condition (U_N=K_{\rm gen}), for example when every
   lift denominator (D_i) is coprime to (N).
5. It states the remaining source target using (K_N/U_N) and the induced
   non-global root map.
6. It proves the exact denominator identity and uses it to compute (U_N).
7. It states that the generic kernel is relative to the selected public lift
   and that the D03 lifts depend on (N), the branch, and its provenance.
8. It says precisely that deletion of the raw (N-1) path removes those raw
   occurrences, while duplicate (N-2) provenance supplies the same retained
   relation values.

The old counterexample therefore no longer refutes the verdict, algorithm,
or remaining-gap statement.

## 2. Core square-kernel algebra

### 2.1 Specialization containment — PASS

If a polynomial (F\in\mathbb Q[T]) is a square in (mathbb Q(T)), write
(F=(P/Q)^2) with coprime (P,Q\in\mathbb Q[T]). Then
(P^2=FQ^2). Unique factorization makes (Q) constant, so (F=S^2) for
some (S\in\mathbb Q[T]).

For (c\in K_{\rm gen}), evaluation gives

\[
\prod_i A_i(N)^{c_i}=S_c(N)^2.
\]

The left side is an integer. A rational number whose square is an integer is
an integer. Hence (S_c(N)\in\mathbb Z), and
(K_{\rm gen}\subseteq K_N). Positivity of the numeric product fixes its
positive root up to the sign of (S_c(N)).

### 2.2 Unit-denominator theorem — PASS

Because every (A_i(0)=1), a generic root has
(S_c(0)=\pm1). If (d_cS_c\in\mathbb Z[T]), then

\[
d_c(S_c(T)-S_c(0))\in T\mathbb Z[T].
\]

At (T=N), this is zero modulo (N). When
(gcd(d_c,N)=1), cancellation gives
(S_c(N)\equiv\pm1\pmod N). The exact positive root has the same global
sign property. No unproved cancellation modulo (N) is used.

### 2.3 The (gcd=N) useful generic relation — PASS

For

\[
N=15,\qquad
S(T)=1-\frac45T+\frac1{15}T^2,\qquad A(T)=S(T)^2,
\]

one has (S(0)=1), (S(15)=4), and (A(15)=16\equiv1\pmod {15}).
The least coefficient denominator of (S) is (15), so its gcd with (N)
is the whole modulus. Nevertheless, the generic relation gives

\[
\gcd(4-1,15)=3,\qquad \gcd(4+1,15)=5.
\]

Thus (K_N=K_{\rm gen}=\mathbb F_2) and
(K_N/K_{\rm gen}=0), while the relation factors (N). The corrected
candidate uses this example in exactly the required way.

## 3. Least denominators and cancellation

### 3.1 Gauss denominator identity — PASS

For a rational polynomial (P) with constant term (\pm1), and for each
rational prime (p), define

\[
\lambda_p(P)=-\min_j v_p([T^j]P).
\]

The constant coefficient is a (p)-adic unit, so the minimum is at most zero
and
(lambda_p(P)=v_p(d(P))), where (d(P)) is the least positive coefficient
denominator.

The minimum valuation is additive under multiplication. After scaling two
polynomials to have integral coefficients with at least one unit coefficient,
their reductions modulo (p) are nonzero. Their product is nonzero because
(\mathbb F_p[T]) is a domain. Hence a cancellation cannot remove all terms
of the minimum combined valuation.

Applying this to

\[
S_c^2=\prod_i A_i^{c_i}
\]

gives, prime by prime,

\[
2v_p(d_c)=\sum_i c_i v_p(D_i),
\qquad D_i=d(A_i).
\]

Therefore

\[
d_c^2=\prod_iD_i^{c_i}.
\]

This identity rules out the hidden denominator cancellation that invalidated
the first version's informal treatment. The constant-term hypothesis is
important: it is what identifies the Gauss minimum with the denominator
valuation rather than a signed content valuation.

### 3.2 (U_N) is an exact computable subspace — PASS

All valuations on the right are nonnegative. For every prime (p\mid N),
(p\nmid d_c) exactly when no selected (D_i) is divisible by (p).
Consequently,

\[
U_N=K_{\rm gen}\cap
\{c:c_i=0\text{ whenever }\gcd(D_i,N)>1\}.
\]

This is an intersection of binary subspaces. Given a basis of
(K_{\rm gen}), it is computed by applying the displayed coordinate-zero
constraints and taking a binary kernel. No enumeration of
(K_{\rm gen}) is required.

If (1<\gcd(D_i,N)<N), that gcd is already a valid factor. If
(gcd(D_i,N)=N), the corresponding coordinate is excluded from (U_N)
but remains available in the quotient. This correctly retains the repaired
(N=15) counterexample.

## 4. Rational units in the generic factorization

The algorithm says to factor the (A_i) over (\mathbb Q[T]) and use
irreducible-factor parity. A hostile reading must also check the unit in
(\mathbb Q^\times), because ordinary polynomial factorization determines
nonconstant factors only up to rational scaling.

No integer factorization of rational unit numerators or denominators is needed
here. Normalize every nonconstant irreducible factor to be monic and write

\[
A_i=q_i\prod_f f(T)^{e_{fi}},\qquad q_i\in\mathbb Q^\times.
\]

Suppose a vector (c) makes every nonconstant exponent
(sum_i c_i e_{fi}) even. Then

\[
F_c=q_c\left(\prod_f f^{E_f}\right)^2.
\]

No (f(0)) is zero because every (A_i(0)=1). Evaluation at zero gives

\[
1=F_c(0)=q_c\left(\prod_f f(0)^{E_f}\right)^2,
\]

so (q_c) is automatically a rational square. Conversely, a square in
(\mathbb Q(T)) has even valuation at every nonconstant irreducible.
Therefore the parity matrix of normalized nonconstant irreducibles computes
(K_{\rm gen}) exactly. A P66-style gcd-free refinement of rational unit
contents is not required.

This constant-term argument is the necessary interpretation of algorithmic
step 2. An implementation that instead tried to prime-factor arbitrary unit
contents would not have the stated unconditional polynomial-time bound.

## 5. Root quotient and basis completeness

For (c,e\in K_N), positivity gives the exact overlap identity

\[
R_N(c)R_N(e)
=R_N(c+e)\prod_{i:c_i=e_i=1}a_i.
\]

Every (a_i\equiv1\pmod N), so
(\rho_N(c)=R_N(c)\bmod N) is a homomorphism into the square roots of one.
After quotienting the target by the global subgroup (\{\pm1\}), Theorem 2
gives

\[
U_N\subseteq\ker\bar\rho_N.
\]

Thus (\bar\rho_N) factors through (K_N/U_N). If any quotient vector has
a non-global image, every binary basis of the quotient contains at least one
vector with a non-global image. Extending a basis of (U_N) to one of (K_N)
and screening only the added representatives is therefore complete. Adding
the harmless subspace cannot hide a useful root.

The quotient can contain global vectors outside (U_N), so nonzero dimension
is necessary but not sufficient. The candidate states this limitation.

## 6. Polynomial bit complexity

Under the stated input condition—polynomial total lift degree and coefficient
bit length—all filter steps are polynomial in the explicit numeric list, the
explicit lift list, and (log N):

- P66 computes (K_N) in polynomial bit complexity.
- Deterministic factorization over (\mathbb Q[T]) is polynomial in dense
  degree and coefficient bit length. Monic normalization and exact comparison
  of its factors are polynomial.
- The number of distinct nonconstant factors is at most the total degree, so
  the generic parity matrix has polynomial size.
- Each (D_i) is an lcm of explicit coefficient denominators. Its bit length
  is at most their summed bit lengths. Scaling numerators by this lcm remains
  polynomial.
- Ordinary gcds, the coordinate-restriction kernel, and the basis extension
  use polynomial-size integers and matrices.
- There are at most (m) added quotient representatives. Each exact selected
  numeric product has bit length at most the sum of the input integer bit
  lengths, and its square root has no larger bit length.

The rational-unit point in Section 4 is essential to this conclusion. With
that normalization, no hidden call to integer factorization remains.

The complexity result is conditional preprocessing. It contains no success
probability or expected-trial theorem because the filter does not create a
useful quotient.

## 7. F59-D02/D03 finite provenance and arithmetic

The candidate's pinned artifacts have the stated SHA-256 hashes:

| Artifact | Verified SHA-256 |
| --- | --- |
| F59-D02 source | `05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13` |
| F59-D02 log | `50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018` |
| F59-D02 output | `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e` |
| F59-D03 source | `5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42` |
| F59-D03 log | `7ca87cd0e1255ef7879450bdb50ed0a1b429f4dbefded71e8dcfb20c5d989ebe` |
| F59-D03 output | `9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84` |

The checked finite statements are exact:

- the 12 numeric kernels have total dimension 19;
- all 19 stored basis products are symbolic squares for their selected lifts;
- all 19 symbolic roots have constant (\pm1) and denominator coprime to
  the tested (N);
- hence each complete numeric basis lies in (U_N), so
  (K_N=K_{\rm gen}=U_N) for those 12 batches;
- all numeric dependency roots in those batches are global;
- the seven residual full-batch certificates reduce to the four stated root
  polynomials and denominator lcms (15,230,22533,5040).

The D02 deletion wording is also exact. For every residual support affected by
deleting the raw (N-1) trajectory, a stored occurrence with provenance
((1,j)) is replaced by the identical ((u,v,k)) relation with provenance
((2,j-1)). The original raw occurrence is absent. The retained quotient and
(A=Nk+1) value survive through duplicate provenance. Other support entries
are unchanged.

The corresponding symbolic lift also agrees: the first lifted step from
(T-1) has inverse (T-1) and next state

\[
\frac{(T-1)^2-1}{T}=T-2.
\]

Thus later offset-1 lifts coincide with the one-step-earlier offset-2 lifts.
The candidate nevertheless makes only the correctly scoped finite statement
and does not claim one (N)-independent generic family.

## 8. Surviving scope limits

The following are not consequences of F60:

- (K_N/U_N\ne0) for any unbounded input family;
- a non-global image whenever that quotient is nonzero;
- factor correlation of the F59 completion source;
- a success probability or expected polynomial-time factoring algorithm; or
- an all-input obstruction to another lift or source.

The classification is lift-relative. An arbitrary public lift can move a
numeric relation between the generic and specialization-only classes, and its
coefficient denominators can themselves contain a factor. F60 certifies what
follows after a specific efficiently computable lift is supplied; it does not
manufacture such a useful lift.

Within this scope, I found no new counterexample and no denominator,
unit-content, quotient-completeness, complexity, or provenance defect. The
corrected candidate passes the required fresh hostile audit.

## 9. Error classification and promotion consequence

**Proof errors:** none found.

**Scope or exposition clarifications:** algorithmic step 2 should explicitly
say that nonconstant irreducibles are normalized to monic form and that
`A_i(0)=1` forces the remaining rational unit of every parity-zero product to
be a square. This avoids any possible reading that asks for prime
factorization of rational contents. The derivation is in Section 4 above and
uses only hypotheses already present in the candidate. It does not change the
theorem, quotient, algorithm, or complexity bound. The phrases
`factor-bearing quotient` and `generic` must continue to carry the candidate's
stated meanings: a necessary search space rather than an all-useful quotient,
and classification relative to the selected lift.

Therefore this audit requires no mathematical correction. The candidate can
be promoted after prose-only clarification, provided the separate required
proof-blind reconstruction also passes. Such prose edits do not require
another hostile audit of this mathematical version.
