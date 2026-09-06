# F148 blind reconstruction

## Verdict

**PASS.** I found no algebraic, gcd, metric, complexity, certificate, or scope defect in the frozen statement.

I used only `STATEMENT.md` from the F148 directory. Before reading it, I verified

```text
SHA-256(STATEMENT.md) = 8d790d05d8161444684d109ad16c3cc1f2be453dcc04638a8d8a10406b78cc35.
```

No conclusion below assumes that a required cycle exists. The result is a conditional decoder, not an all-input factoring algorithm.

## 1. Cycle congruence and exact square class

For an edge of a directed containment cycle,

\[
q_ea_e^2=U_e\equiv c_e=q_{e+1}T_e\pmod N.
\]

Multiplication around the cycle gives

\[
\left(\prod_e q_e\right)\left(\prod_ea_e\right)^2
\equiv
\left(\prod_e q_{e+1}\right)\left(\prod_eT_e\right)\pmod N.
\]

The two cyclic products of the `q` labels are equal. They are units modulo `N`, so they cancel. Thus

\[
\alpha_i^2\equiv T_i\pmod N.
\]

This proves (1).

For completeness, write `beta_e` for the canonical inverse of `c_e` used in the P128 bridge pair. The two retained exact values for edge `e` are `beta_e*c_e` and `beta_e*U_e`. The exact product over cycle `i` is

\[
\begin{aligned}
P_i
&=\prod_e(\beta_ec_e)(\beta_eU_e)\\
&=\left(\prod_e\beta_eq_ea_e\right)^2T_i
=B_i^2T_i,
\end{aligned}
\]

because `prod r_e = prod q_e` around the cycle. Therefore the exact rational square class left by the cycle is precisely that of `T_i`. Also,

\[
B_i
\equiv
\frac{\alpha_i}{T_i}\pmod N,
\]

since `prod c_e = (prod q_e)T_i` and `beta_e*c_e = 1 mod N`.

Global exact-value deduplication can remove only even occurrences of an identical retained value. Such removal changes an exact product by a rational square and changes its exact square root by a value congruent to `1 mod N`. The stated use of the actual, disjoint retained supports is therefore the correct condition for taking the union.

## 2. Same residual class and normalized root

For positive integers `T_i,T_j`, equality of their rational square classes is equivalent to the existence of positive integers `d,s_i,s_j` with

\[
T_i=ds_i^2,\qquad T_j=ds_j^2.
\]

The forward direction does not require prime factorization. If `g=gcd(T_i,T_j)`, equality of square classes means that every prime-exponent difference is even. Hence both `T_i/g` and `T_j/g` are perfect squares. One may take

\[
d=g,\qquad s_i=\sqrt{T_i/g},\qquad s_j=\sqrt{T_j/g}.
\]

Conversely, the displayed common-core form makes `T_i/T_j=(s_i/s_j)^2`. Since each `T` is a unit modulo `N`, `d,s_i,s_j` are also units modulo `N`; every modular division in the theorem is therefore legal.

For disjoint cycle supports,

\[
P_iP_j=(B_iB_jds_is_j)^2.
\]

Thus their union is an exact square relation. Its positive exact root reduces modulo `N` to

\[
\begin{aligned}
\rho_{ij}
&\equiv
\frac{\alpha_i}{T_i}\frac{\alpha_j}{T_j}ds_is_j\\
&=
\frac{\alpha_i\alpha_j}{ds_is_j}\pmod N.
\end{aligned}
\]

Using `alpha_j^2 = d*s_j^2 mod N`,

\[
\frac{\alpha_i\alpha_j}{ds_is_j}
\equiv
\frac{\alpha_is_j}{\alpha_js_i}\pmod N.
\]

This proves both forms in (3), including their orientation.

Set

\[
A=\alpha_is_j,\qquad B=\alpha_js_i.
\]

The integer `B` is a unit modulo `N`, and `rho_ij = A/B mod N`. Multiplication by a unit does not change a gcd with `N`. Therefore

\[
\gcd(\rho_{ij}-1,N)=\gcd(A-B,N)
\]

and

\[
\gcd(\rho_{ij}+1,N)=\gcd(A+B,N).
\]

These are (4) and (5). They reveal exactly the same modular root as the combined square relation; they only avoid constructing its much larger exact root.

## 3. Metric theorem and failure classification

The two cycle congruences imply

\[
A^2=\alpha_i^2s_j^2\equiv ds_i^2s_j^2
\equiv\alpha_j^2s_i^2=B^2\pmod N.
\]

Hence `N` divides `(A-B)(A+B)`. Under (6) and (7),

\[
0<|A-B|<N,\qquad 0<A+B<N.
\]

Both gcds are therefore smaller than `N`. If `gcd(A-B,N)=1`, Euclid's lemma would force `N` to divide `A+B`, a contradiction. If `gcd(A+B,N)=1`, it would force `N` to divide `A-B`, also a contradiction. Thus both gcds lie strictly between `1` and `N`. The metric theorem is valid for composite `N` with repeated prime factors as well as for squarefree `N`.

Define

\[
z_i=\alpha_is_i^{-1}\pmod N.
\]

Then `z_i^2 = d mod N`, and

\[
\rho_{ij}=z_iz_j^{-1}\pmod N.
\]

Thus `rho_ij^2=1 mod N`. The terminal gcds are trivial exactly when `rho_ij` is the global root `+1` or `-1`, equivalently when `z_i` and `z_j` are in the same class modulo global sign. If they are not in the same class, neither terminal gcd can be `1` or `N`, so the pair factors `N`. It follows directly that every pair in a bucket is a decoy if and only if all `z_i` lie in one global-sign class.

Under (7), a pair with unequal exact slopes has `A != B`, so the metric theorem factors `N`. Conversely, equality of the positive rational slopes is exactly `A=B`, which gives the global root `+1`. Therefore, when (7) holds pairwise throughout a bucket, absence of a factoring pair forces all exact slopes `alpha_i/s_i` to be equal. The metric also excludes an exact positive pair representing the global `-1` case, because that would require `N` to divide the positive integer `A+B<N`.

## 4. Conditional quasipolynomial corollary

Here `d_i` is the positive squarefree kernel of `T_i` (or an equivalent consistently chosen factor-free representative of its rational square class). It satisfies `d_i<=T_i<=R`. Hence there are at most `R` possible cores. More than `R` cycles force two, say `i,j`, into the same core bucket.

For this pair,

\[
s_i\le\sqrt R,\qquad s_j\le\sqrt R
\]

and

\[
\alpha_is_j+\alpha_js_i
\le 2H\sqrt R<N.
\]

Item 3 makes their exact slopes unequal. Conditions (6) and (7) therefore hold, and (4)--(5) factor `N`. Column-disjointness is exactly what permits the two cycle vectors to be united without parity cancellation between them.

The complexity claim also survives a hostile check. Let the number of cycles be `M`. When `M,R <= 2^polylog(n)`, at most `M^2` pair operations are still quasipolynomial. Rational-square-class equality can be tested without factorization by computing `g=gcd(T_i,T_j)` and testing `T_i/g` and `T_j/g` for being integer squares. Equivalently, joint gcd-free refinement produces pairwise-coprime blocks and parity vectors. Once a pair is found, its `s` values come from exact integer square roots. Exact slope comparison uses a cross-product, and the terminal work uses the two stated gcds. All involved integers have quasipolynomial presentation length; `alpha_i<=H<N` gives each anchor product only `O(n)` bits. Standard multiplication, integer-square-root, and gcd algorithms therefore keep the total work quasipolynomial. The numerical size of `H` does not cause enumeration over `H`.

This is an existence-and-decoding implication only. None of its four assumptions is derived by F148.

## 5. Independent certificate audit

The modulus is the stated odd composite:

\[
745=5\cdot149.
\]

The anchor identities are exact:

\[
119^2=14161=19\cdot745+6,
\]

\[
179^2=32041=43\cdot745+6.
\]

For the first one-edge cycle,

\[
U_1=57\cdot119^2=807177,\qquad c_1=57\cdot6=342,
\]

and `U_1 mod 745 = 342`. For the second,

\[
U_2=92\cdot179^2=2947772,\qquad c_2=92\cdot6=552,
\]

and `U_2 mod 745 = 552`. All displayed factors are coprime to `745`.

The inverse checks are

\[
342\cdot403=137826=185\cdot745+1,
\]

\[
552\cdot193=106536=143\cdot745+1.
\]

The retained values reconstruct exactly as

\[
(403c_1,403U_1)=(137826,325292331),
\]

\[
(193c_2,193U_2)=(106536,568919996).
\]

They are pairwise distinct. Direct square bracketing gives

```text
371^2  < 137826    < 372^2
18035^2 < 325292331 < 18036^2
326^2  < 106536    < 327^2
23852^2 < 568919996 < 23853^2
```

so each retained value is nonsquare. With

\[
L_1=403\cdot57\cdot119=2733549,
\qquad
L_2=193\cdot92\cdot179=3178324,
\]

the two cycle products are

\[
44833740812406=6L_1^2,
\]

\[
60610460693856=6L_2^2.
\]

Neither is a square because the valuations of `2` and `3` contributed by the factor `6` are odd. Their combined product is

\[
(6L_1L_2)^2
=52128626351256^2
=2717393685268861431892777536.
\]

The exact root satisfies

\[
52128626351256\equiv446\pmod{745}.
\]

The two forms of (3) independently give the same residue:

\[
119\cdot179\cdot6^{-1}\equiv119\cdot179^{-1}\equiv446\pmod{745}.
\]

Finally,

\[
\gcd(445,745)=5,\qquad\gcd(447,745)=149,
\]

and the smaller witnesses are

\[
\gcd(179-119,745)=\gcd(60,745)=5,
\]

\[
\gcd(179+119,745)=\gcd(298,745)=149.
\]

Each of the four retained values is `1 mod 745`. Hence every individual endpoint screen is null:

\[
\gcd(v-1,745)=745,\qquad\gcd(v+1,745)=1.
\]

All certificate claims check exactly.

## 6. Scope check

The statement proves only these implications:

1. A supplied legal directed containment cycle exposes the congruence and residual square class stated in Section 1.
2. Two supplied disjoint cycles in one residual class yield a combined exact square relation and the cross-ratio decoder.
3. The metric hypotheses force both terminal gcds to be proper.
4. More than `R` supplied cycles satisfying all four corollary assumptions force such a pair in quasipolynomial decoding time.

It does not construct cycles, prove enough cycles exist, establish small residual products, establish the anchor bound, force slope diversity, prove a frequency statement, or factor every odd composite. The finite example demonstrates nondegeneracy only. The final two proposed F26-Q continuations are correctly presented as unresolved source-side targets. The phrase that the second target is more permissive on each individual cycle is valid in the stated residual-class sense: an individual residual need not already be a square; the compensating cycle-count, metric, and diversity hypotheses remain explicit.

**Final result: PASS; no defect found.**
