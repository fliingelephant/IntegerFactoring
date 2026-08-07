# F60 hostile audit — generic-specialization decoys

**Candidate audited:** `experiments/F60_generic_specialization_decoy/RESULT.md`
**Verified candidate SHA-256:** `35daff9aab8c7f4d3bd84a80ac138c19e263acc73de98f46dd0a29690adc9176`
**Verdict:** **FAIL**

The failure is narrow but mathematical. The three numbered theorems are correct. The final claim that a nonzero specialization quotient (K_N/K_{\rm gen}) is necessary is false. A useful relation can be generic and have a nonunit root denominator. The candidate's own (N=15) caveat points at this issue but does not propagate it into the verdict, algorithm section, or remaining-gap section.

The exact factor-bearing quotient proved by the candidate is (K_N/G_N), not (K_N/K_{\rm gen}). These quotients agree only under an extra hypothesis such as (G_N=K_{\rm gen}).

## 1. Core algebra

### 1.1 A square in \(\mathbb Q(T)\) has a polynomial root — PASS

Let (F\in\mathbb Q[T]) and suppose (F=(P/Q)^2), where (P,Q\in\mathbb Q[T]) are coprime. Then

\[
P^2=FQ^2.
\]

Every irreducible divisor of (Q) would divide (P^2), hence (P), contrary to coprimality. Thus (Q) is constant and (F=S^2) for some (S\in\mathbb Q[T]). The candidate's use of unique factorization is correct.

### 1.2 Specialization containment — PASS

For (c\in K_{\rm gen}), write

\[
\prod_i A_i(T)^{c_i}=S_c(T)^2
\]

with (S_c\in\mathbb Q[T]). Evaluation at (T=N) gives

\[
\prod_i a_i^{c_i}=S_c(N)^2\in\mathbb Z.
\]

If (x=r/s\in\mathbb Q) is in lowest terms and (x^2\in\mathbb Z), then (s^2\mid r^2), so (s=1). Hence (S_c(N)\in\mathbb Z), and (c\in K_N). Therefore

\[
K_{\rm gen}\subseteq K_N.
\]

The positivity assumption on the (a_i) also makes the exact positive numeric root unambiguous.

### 1.3 Unit-denominator congruence — PASS

Since (A_i(0)=1), a generic root satisfies (S_c(0)=\pm1). If (d_cS_c\in\mathbb Z[T]), then

\[
d_c\bigl(S_c(T)-S_c(0)\bigr)\in T\mathbb Z[T].
\]

Evaluation at (N) gives

\[
d_c\bigl(S_c(N)-S_c(0)\bigr)\equiv0\pmod N.
\]

The preceding integrality argument gives (S_c(N)\in\mathbb Z). If (gcd(d_c,N)=1), cancellation is valid and

\[
S_c(N)\equiv S_c(0)\equiv\pm1\pmod N.
\]

The positive root differs from (S_c(N)) by at most a sign. Theorem 2 is correct.

### 1.4 The displayed \(N=15\) example — PASS, after making \(A\) explicit

Take

\[
S(T)=1+T/5,
\qquad
A(T)=S(T)^2.
\]

Then (A(0)=1), (A(15)=16\equiv1\pmod{15}), (d=5), and (S(15)=4\not\equiv\pm1\pmod{15}). Also (4^2\equiv1\pmod{15}). Thus the unit condition cannot be removed, and (gcd(d,15)=5) exposes a factor. The candidate states only (S), but (A=S^2) supplies the implicit one-relation instance.

## 2. Decisive counterexample to the claimed specialization necessity

The candidate ends with:

> A dimension gap (K_N/K_{\rm gen}\ne0) is necessary but not sufficient.

This is false. The proper-denominator factor in the candidate's example already disproves the unqualified claim. The following variant also prevents the denominator gcd from exposing a proper factor first.

Let (N=15), (m=1), and

\[
S(T)=1-\frac45T+\frac1{15}T^2,
\qquad
A_1(T)=S(T)^2.
\]

Then

\[
S(0)=1,
\qquad
S(15)=1-12+15=4,
\]

so

\[
A_1(0)=1,
\qquad
a_1=A_1(15)=16\in\mathbb Z_{>0},
\qquad
a_1\equiv1\pmod{15}.
\]

The nonzero vector (c=(1)) is in (K_{\rm gen}) because (A_1=S^2), and it is in (K_N) because (a_1=4^2). Hence

\[
K_N=K_{\rm gen}=\mathbb F_2,
\qquad
K_N/K_{\rm gen}=0.
\]

The least coefficient denominator of (S) is (d_c=15), so

\[
\gcd(d_c,N)=N.
\]

The denominator gives no proper divisor. Nevertheless,

\[
R_N(c)=4\not\equiv\pm1\pmod{15},
\]

and the congruence-of-squares decoder returns

\[
\gcd(4-1,15)=3,
\qquad
\gcd(4+1,15)=5.
\]

Thus a generic relation can be factor-bearing, even when its denominator gcd is trivial in the sense (gcd(d_c,N)=N). No specialization-only relation exists in this example.

This counterexample refutes all unqualified versions of these candidate statements:

- “A useful sampler must create a specialization-only dependency.”
- “The decoder now retains only dependencies created by specialization.”
- “A dimension gap (K_N/K_{\rm gen}\ne0) is necessary.”
- The remaining-gap target when it is stated only in terms of the specialization quotient.

Each statement becomes valid only after an extra condition that puts all of (K_{\rm gen}) in the global-root kernel, for example (G_N=K_{\rm gen}).

## 3. The root map and the correct quotient

### 3.1 Homomorphism — PASS

Let

\[
H_N=\{x\in(\mathbb Z/N\mathbb Z)^\times:x^2=1\}.
\]

For (c,e\in K_N), let (I=\{i:c_i=e_i=1\}). Positivity of the roots gives the exact identity

\[
R_N(c)R_N(e)
=R_N(c+e)\prod_{i\in I}a_i.
\]

Since every (a_i\equiv1\pmod N), reduction modulo (N) gives

\[
\rho_N(c+e)=\rho_N(c)\rho_N(e).
\]

Thus (ho_N:K_N\to H_N) is a homomorphism. Since (N) is odd, ({\pm1\}) is a subgroup, and the quotient map

\[
\bar\rho_N:K_N\longrightarrow H_N/\{\pm1\}
\]

is well-defined.

### 3.2 The \(U_N\), \(G_N\) construction — PASS

Every element of

\[
U_N=\{c\in K_{\rm gen}:\gcd(d_c,N)=1\}
\]

maps to the identity coset in (H_N/\{\pm1\}). A kernel is an (mathbb F_2)-subspace, so

\[
G_N=\operatorname{span}_{\mathbb F_2}(U_N)
\subseteq\ker\bar\rho_N.
\]

Therefore Theorem 3 and factorization through (K_N/G_N) are correct. A useful congruence-of-squares relation must lie outside (G_N), but it need not lie outside (K_{\rm gen}). The counterexample above has (G_N=0) and (K_N=K_{\rm gen}).

### 3.3 A stronger denominator fact

The span definition is safe. Under the candidate's hypotheses, one can prove more: (U_N) is already a subspace.

For a rational polynomial (P) with constant term (pm1), let (d(P)) be its least coefficient denominator. For each prime (p), define

\[
\lambda_p(P)=v_p(d(P))
=-\min_j v_p([T^j]P).
\]

The Gauss valuation is multiplicative:

\[
\lambda_p(PQ)=\lambda_p(P)+\lambda_p(Q).
\]

Indeed, after scaling each polynomial so its least coefficient valuation is zero, both reductions modulo (p) are nonzero, and so is their product.

Let (D_i=d(A_i)). If (c\in K_{\rm gen}), then

\[
S_c^2=\prod_i A_i^{c_i}
\]

implies, prime by prime,

\[
2v_p(d_c)=\sum_i c_i v_p(D_i).
\]

Equivalently,

\[
d_c^2=\prod_iD_i^{c_i}. \tag{1}
\]

All terms on the right have nonnegative valuations. Therefore

\[
\gcd(d_c,N)=1
\iff
c_i=0\text{ for every }i\text{ with }\gcd(D_i,N)>1.
\]

Hence

\[
U_N
=K_{\rm gen}\cap
\{c:c_i=0\text{ whenever }\gcd(D_i,N)>1\},
\]

which is a subspace, and (G_N=U_N). This identity supplies the missing direct way to compute (G_N) once a basis of (K_{\rm gen}) is available.

## 4. F59-D02/D03 finite certificate

### 4.1 Artifact integrity

The pinned artifacts match their recorded hashes.

| Artifact | Verified SHA-256 |
|---|---|
| F59-D02 source | `05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13` |
| F59-D02 log | `50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018` |
| F59-D02 output | `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e` |
| F59-D03 source | `5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42` |
| F59-D03 log | `7ca87cd0e1255ef7879450bdb50ed0a1b429f4dbefded71e8dcfb20c5d989ebe` |
| F59-D03 output | `9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84` |

### 4.2 What D03 certifies — PASS

Static inspection of the D02 and D03 sources and outputs confirms:

- There are 12 full deterministic-offset batches.
- Their numeric kernel dimensions sum to (19).
- One basis vector in each batch is the singleton (A=(N-1)^2), for 12 such vectors.
- The other seven full-batch basis vectors do not use that singleton and are arithmetic-only under the stored endpoint-label representation.
- D03 reconstructs and checks all 19 selected products as squares in (mathbb Q[T]).
- Each selected symbolic root has constant term (pm1) and coefficient denominator coprime to its tested (N).
- The 19 numeric basis images are global. They consist of 18 global-minus roots and one global-plus root.
- Since a complete basis of (K_N) lies in (K_{\rm gen}), Theorem 1 gives equality of the two kernels for each of these 12 chosen lifts. Homomorphicity then proves that every numeric dependency in each full batch has a global root.
- The seven nonsingleton certificates reduce to the four root polynomials stated by the candidate. The repeated degree-three root occurs four times. The other denominator least common multiples are (230), (22533), and (5040).

The implementation checks each selected identity once with its exact rational polynomial arithmetic and again with Sage polynomial arithmetic. This is a useful second arithmetic backend. It is not an independent-agent verification round, and the candidate correctly leaves its status at `candidate`.

### 4.3 Meaning of “survive both deletion variants”

The finite statement is correct at the retained relation-value level, but its provenance should be stated precisely.

The seven full-batch residual vectors exclude the global-square singleton, so they survive that deletion unchanged. Each displayed full-batch certificate does use a later relation from the trajectory started at (N-1). After deletion of that raw trajectory, D02 retains the same (k) and (A=Nk+1) values through duplicate provenance from the trajectory started at (N-2). In every affected support, a provenance ((1,j)) is replaced by ((2,j-1)).

This replacement also preserves the D03 lift. At the first symbolic step from (T-1), the lifted inverse is (T-1), and

\[
\frac{(T-1)^2-1}{T}=T-2.
\]

Thus the later lift from offset (1) is the same as the one-step-earlier lift from offset (2). The same seven retained (k/A) dependencies and the same four square identities remain. The raw provenance does not survive; the deduplicated relation does. The candidate should use this precise wording.

### 4.4 Finite scope — PASS

The candidate correctly calls D03 finite evidence about one deterministic sampler. It makes no asymptotic source claim, probability claim, or factor-correlation claim. Nothing in D02 or D03 proves an all-input obstruction.

## 5. Algorithmic and interpretation limits

### 5.1 The generic kernel is lift-relative

The same numeric relation can be generic or specialization-only under two admissible lifts. For (N=15) and (a=16), compare

\[
A(T)=(1+T/5)^2
\]

with

\[
A'(T)=1+T.
\]

Both have constant term (1) and specialize to (16) at (T=15). The first is a square in (mathbb Q(T)); the second is not. Therefore (K_{\rm gen}) and (K_N/K_{\rm gen}) are not invariants of the numeric relation list. They are invariants only after a lift rule is fixed.

D03's affine lifts are constructed from the already known modulus, inverse value, branch, and trajectory provenance. They are valid public lifts, but “before (N) is substituted” must mean only that (T) is left indeterminate in the resulting polynomial identity. It must not imply an (N)-independent generic family.

### 5.2 The polynomial filter claim needs one more proof

The candidate assumes polynomial total lift size and polynomial-time square-class computation. It then calls the whole filter polynomial without explaining how (G_N) is computed. Equation (1) repairs this gap: compute each (D_i), compute (gcd(D_i,N)), intersect the computed (K_{\rm gen}) with the coordinate subspace that excludes every bad-denominator column, and use binary linear algebra to form (K_N/U_N). A proper denominator gcd is already a factor.

Without this lemma or an equivalent algorithm and bit-length bound, “this filter is also polynomial” is unsupported as written. Even after repair, it is only a conditional preprocessing theorem. No proof makes the quotient nonzero or its root image non-global with inverse-polynomial probability.

### 5.3 No factoring or novelty claim — PASS

The candidate correctly says that it is not a source-success theorem and not a factoring algorithm. It gives no all-input sampler, no success law, no expected-trial bound, and no complete-factorization complexity proof. It also explicitly declines a publication-level novelty claim. These scope disclaimers are correct.

## 6. Required corrections

The exact candidate version cannot pass. A corrected version must make all of the following changes.

1. Replace every general claim that the root map factors through (K_N/K_{\rm gen}) with the proved quotient (K_N/G_N).
2. Delete “a dimension gap (K_N/K_{\rm gen}\ne0) is necessary.” Replace it with: a nonzero quotient (K_N/G_N) is necessary, but not sufficient, for a non-global root under this decoder.
3. Replace “a useful sampler must create a specialization-only dependency” with: a useful sampler must create a relation outside (G_N) whose normalized root is non-global, unless a denominator gcd has already exposed a factor.
4. Say that the decoder retains only specialization-created dependencies only under the extra condition (G_N=K_{\rm gen}). In general, (K_N/G_N) can retain generic, nonunit-denominator relations.
5. State the remaining source target using (K_N/G_N) and (ar\rho_N), or explicitly assume (G_N=K_{\rm gen}) before using the specialization quotient (K_N/K_{\rm gen}).
6. Add a method and bit-complexity proof for computing (G_N). The denominator identity in Section 3.3 gives a direct repair under the present hypotheses.
7. State that every generic/specialization classification is relative to the selected symbolic lift. Describe the D03 lift as branch- and (N)-dependent.
8. Clarify that the seven residual D02 relation values survive deletion of the (N-1) path through duplicate (N-2) provenance; the original raw occurrences do not survive.

After corrections 1--8, Theorems 1--3 and the finite D03 certificate can be retained. The false necessity claim changes mathematical content, so the corrected version requires the prescribed new verification cadence.

No new research experiment was run for this audit. The finite checks were read-only hash verification and inspection of the preregistered D02/D03 sources and outputs.
