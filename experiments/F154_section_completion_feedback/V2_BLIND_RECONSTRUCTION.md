# F154 V2 blind reconstruction

## Scope and verdict

The input statement was read only after its SHA-256 was verified as

`8c75dd708a4c7bbd99e593e92474b266fb38c2b9ff8c07b3f17d0645583566c6`.

No other F154 artifact was used.

**Verdict: the algebraic completion and decoder-inertness claims are valid, subject to two explicit interpretations.** First, the second component of (E_Q(N)) must mean a residue class in ((\mathbb Z/N\mathbb Z)^\times); with literal integer second components, (2) is not a group. Second, the map called a quotient section in (4) must be the homomorphic section described in the surrounding assumptions. An arbitrary set-theoretic section would not support (5).

The distinctness, pure- and mixed-dependency root claims, triple identity, cost bound, refinement calculation, subgroup enlargement, and interface-restricted inertness all follow under those interpretations. The sentence that the finite witness “does not factor (77)” is valid only in the operational sense that the displayed completion and gcd-free refinement do not themselves output a divisor of (77). Read literally together with the displayed order claim, it is false: (26^{15}\equiv34\pmod {77}), and

\[
\gcd(34-1,77)=11,
\qquad
\gcd(34+1,77)=7.
\]

This route uses modular information already present in the old supplied root (3), since (26=3^{-1}\pmod {77}). It therefore does not contradict the narrower claim that completion adds no modular information.

## 1. The decorated group

Write (U=(\mathbb Z/N\mathbb Z)^\times), and interpret every (z) in (2)--(5) as an element of (U). For bits, addition in the arguments of (Q) and (C) is XOR. Coordinatewise calculation gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2. \tag{A}
\]

It also gives the cocycle identity

\[
C(v,w)C(v+w,u)=C(w,u)C(v,w+u), \tag{B}
\]

because for (a,b,c\in\{0,1\}),

\[
ab+(a\mathbin\oplus b)c
=ab+ac+bc-2abc
=bc+a(b\mathbin\oplus c).
\]

Equation (A) proves closure of (3), and (B) proves associativity. Symmetry of (C) proves commutativity. The identity is ((0,1)). Moreover,

\[
(v,z)\star(v,z)
=
(0,z^2Q(v)^{-1})
=(0,1).
\]

Thus every element is its own inverse, and (E_Q(N)) is an abelian group of exponent two. Since (N) is odd,

\[
H=\{(0,1),(0,-1)\}
\]

is a two-element central subgroup, so the stated quotient is defined. There can be other square roots of (1) modulo a composite (N); this does not affect the definition of (H).

Let (b_1,\ldots,b_d) be the chosen basis of (W), and let (e_k) be its retained actual decorated lift. Define

\[
\widetilde h\!\left(\sum_k x_kb_k\right)
=\mathop{\star}_{k:x_k=1}e_k.
\]

The exponent-two abelian group law makes this a well-defined homomorphism. If (π:E_Q(N)\to E_Q(N)/H) is the quotient map, then homomorphicity of (h) and (π(e_k)=h(b_k)) give

\[
\pi\widetilde h(v)=h(v).
\]

This proves the actual-lift claim. It also forces (widetilde h(0)=(0,1)), hence (z_0=1) for the chosen least-positive representative.

## 2. Completion and distinctness

Each (z_v) is a unit because (z_v^2\equiv Q(v)) and (Q(v)) is a unit. Its least positive inverse (s_v) therefore exists. Then

\[
P_v=s_v^2Q(v)\equiv z_v^{-2}z_v^2\equiv1\pmod N.
\]

For a record presented as (s_v^2Q(v)) with supplied modular root (1), removal of the displayed square factor gives decorated coordinate

\[
1\cdot s_v^{-1}=z_v.
\]

Thus its lift is exactly (widetilde h(v)).

The rational squareclasses (Q(v)) are all different. Indeed, if (v\ne w), choose (j) in their symmetric difference. Since (q_j) is not a square, some prime has odd valuation in (q_j). Pairwise coprimality puts that prime in no other (q_k). Its valuation in (Q(v)/Q(w)) is therefore odd, so that ratio is not a rational square.

If (P_v=P_w), then

\[
\frac{Q(v)}{Q(w)}=\left(\frac{s_w}{s_v}\right)^2,
\]

which contradicts the preceding paragraph unless (v=w). Hence the (P_v) are pairwise distinct. Also (s_0=z_0=1) and (Q(0)=1), so (P_0=1). A nonzero (v) contains at least one (q_j>1), hence (P_v>1).

## 3. Pure completion dependencies

For (S\subseteq W), let

\[
a_j=\sum_{v\in S}v_j
\]

as an ordinary integer. Then

\[
\prod_{v\in S}P_v
=
\left(\prod_{v\in S}s_v\right)^2
\prod_jq_j^{a_j}. \tag{C}
\]

If every (a_j) is even, (C) is a square. Conversely, if some (a_j) is odd, select a prime having odd valuation in the nonsquare (q_j). Pairwise coprimality again isolates that prime, whose valuation in (C) is odd. Thus (C) is not a square. Therefore

\[
\prod_{v\in S}P_v\text{ is a square}
\quad\Longleftrightarrow\quad
a_j\equiv0\pmod2\text{ for all }j
\quad\Longleftrightarrow\quad
\sum_{v\in S}v=0.
\]

Assume now that this dependency condition holds. Its positive integer square root is

\[
R_S=left(\prod_{v\in S}s_v\right)
\prod_jq_j^{a_j/2}. \tag{D}
\]

The star-product of any family with coordinate counts (a_j) has second coordinate

\[
\left(\prod_{v\in S}z_v\right)
\prod_jq_j^{-\lfloor a_j/2\rfloor}.
\]

Since (widetilde h) is a homomorphism and the parity sum is zero, this product equals (widetilde h(0)=(0,1)). Hence

\[
\prod_{v\in S}z_v
\equiv
\prod_jq_j^{a_j/2}\pmod N.
\]

Using (s_v\equiv z_v^{-1}) in (D) now gives

\[
R_S\equiv1\pmod N. \tag{E}
\]

Every completion record has supplied root (1). The supplied root of the product is therefore (1), and division by the positive square root (R_S) gives normalized root (+1). This proves both (10) and (11), including the sign.

## 4. Mixed old/completion dependencies

Let an old record have parity (u_i\in W) and decorated lift (e_i). The quotient-section hypothesis says

\[
\pi(e_i)=h(u_i)=\pi(\widetilde h(u_i)).
\]

Consequently there is an (ε_i\in\{1,-1\}) such that

\[
e_i=(0,\varepsilon_i)\star\widetilde h(u_i). \tag{F}
\]

For a mixed dependency consisting of old indices (I) and completion indices (S), the total parity is zero. Equations (F) and homomorphicity give

\[
\mathop{\star}_{i\in I}e_i
\star
\mathop{\star}_{v\in S}\widetilde h(v)
=
\left(0,\prod_{i\in I}\varepsilon_i\right)
\star
\widetilde h\!\left(\sum_{i\in I}u_i+\sum_{v\in S}v\right)
=
\left(0,\prod_{i\in I}\varepsilon_i\right).
\]

Thus every mixed normalized root is (+1) or (-1). Completion can create new dependency vectors, and it can expose a global sign that was not represented by an old dependency, but it cannot enlarge the useful root image modulo (H).

The exact-value deletion claim needs the stated “root-aware” condition. If two occurrences have the same exact value and supplied roots (α) and (β), compare (αeta^{-1}\pmod N) before deleting either occurrence. Any dependency using the deleted occurrence can then be rewritten using the retained occurrence; its normalized root differs by a power of that recorded comparison root. Conversely, the comparison is the root attached to the two-occurrence cancellation. A kernel basis for the deduplicated records together with all such comparison roots therefore generates exactly the old normalized-root image. Deleting without recording the comparisons would not justify this claim. It also would not preserve occurrence, presentation, or provenance information.

## 5. Triple identity

Equation (A) can be rewritten as

\[
Q(v)Q(w)Q(v+w)
=\bigl(Q(v+w)C(v,w)\bigr)^2.
\]

Multiplication by the three displayed (s)-squares proves

\[
P_vP_wP_{v+w}
=
\left(s_vs_ws_{v+w}Q(v+w)C(v,w)\right)^2.
\]

The three parities sum to zero, so (E) proves that the displayed positive root is (1\pmod N). This remains true in the degenerate cases (v=0), (w=0), or (v=w), even though the three indexed factors then contain repeated values and are not literally a three-element subset.

## 6. Bit complexity

There is one indexed record for each element of the (d)-dimensional vector space (W), hence exactly (2^d) records. Since (1\le s_v<N<2^n),

\[
\log_2 P_v
<2n+\sum_jv_j\log_2q_j
\le2n+\Lambda_Q.
\]

Allowing for the leading bit gives the claimed (2n+\Lambda_Q+O(1)) bound.

Enumeration of (W), star-products of basis lifts, extended-Euclidean inversion modulo (N), construction of (Q(v)), and multiplication by (s_v^2) all take time polynomial in the number of outputs and their bit lengths. Thus the total bit cost is

\[
\operatorname{poly}(2^d,n+\Lambda_Q).
\]

A parity-kernel basis can likewise be computed by binary Gaussian elimination in time polynomial in the expanded transcript size. Evaluating the normalized-root map on that basis gives a compact image description and does not enumerate all vectors in the dependency kernel. If (d=(\log n)^{O(1)}), then (2^d=\exp((\log n)^{O(1)})). Combined with a quasipolynomial-size explicit input transcript, both construction and this compact decode are quasipolynomial in (n).

## 7. Restricted feedback interface

The completion values can change raw state: the canonical representatives (s_v) can repeat each other, coincide with old values, or have nontrivial gcds with old endpoints. A joint gcd-free refinement can therefore name factors that the old block list did not name. This does not conflict with decoder inertness, because every completion lift is already on (widetilde h(W)).

Under the stated interface, the only path from completion to the later grammar is the set of newly named refinement blocks. It follows directly that:

1. if refinement names no new block, the later grammar receives no completion-dependent input; and
2. if the grammar excludes every newly named block as a generator, those blocks cannot change its generated state.

These are interface-relative inertness statements. They do not imply observational equivalence for a grammar allowed to inspect (s_v), (P_v), record count, presentation, timing, occurrence, or provenance. The restriction is therefore essential, not cosmetic.

## 8. The (N=77) witness

The displayed arithmetic checks as follows:

\[
4706=61\cdot77+9=26\cdot181,
\qquad
\gcd(4706,77)=1.
\]

The factor (2) has odd valuation in (4706), so (4706) is not an integer square. Also (3^2\equiv9\equiv4706\pmod {77}). A transcript containing only the nonzero parity vector ((1)) has no nonempty parity dependency. The inverse calculation

\[
3\cdot26=78\equiv1\pmod {77}
\]

gives (s_{(1)}=26), and

\[
P_{(1)}=26^2\cdot4706=3{,}181{,}256\equiv1\pmod {77}.
\]

Moreover,

\[
\gcd(26,4706)=26,
\qquad
\gcd(26,181)=1.
\]

Thus refinement of (4706) against (26) replaces the single old named block by the coprime named blocks (26) and (181). Both remain units modulo (77), so this refinement gcd does not itself factor (N).

Using (77=7\cdot11),

\[
\operatorname{ord}_{77}(9)
=\operatorname{lcm}(\operatorname{ord}_{7}(2),\operatorname{ord}_{11}(9))
=\operatorname{lcm}(3,5)=15,
\]

while

\[
\operatorname{ord}_{77}(26)
=\operatorname{lcm}(\operatorname{ord}_{7}(5),\operatorname{ord}_{11}(4))
=\operatorname{lcm}(6,5)=30.
\]

Since (26^{-1}\equiv3) and (9\equiv3^2\equiv26^{-2}),

\[
\langle9\rangle\subsetneq\langle26\rangle.
\]

A grammar that retains the old generator through its factorization and accepts the new block (26) therefore has a strictly larger generated modular subgroup. This proves the named-state expansion claim. It also proves the stated caveat: an unrestricted modular grammar already knew (26), because it already knew the supplied root (3).

There is, however, a literal caveat to “the witness does not factor (77).” The verified order (30) yields

\[
26^{15}\equiv34\pmod {77},
\qquad
34^2\equiv1\pmod {77},
\qquad
34\not\equiv\pm1\pmod {77}.
\]

The two gcds with (34\pm1) give (11) and (7). Hence the finite data do permit a factorization if order computation is admitted. This is not a completion-created advantage: the old root (3=26^{-1}) has the same order and yields the same non-global square root. The defensible conclusion is therefore narrower: the completion dependency and the displayed integer refinement do not themselves emit a nontrivial factor.

## 9. Boundary of the result

Nothing above proves that refinement must name a new block on general inputs, that a named block is usable by a later grammar, that a later relation closes, that a later lift disagrees with (widetilde h), or that an iteration terminates with a non-global root. The proposed second-stage dichotomy in Section 7 of the statement is not a consequence of the proved claims. Terms such as “terminal,” “usable,” and “separate public restriction” would also need formal definitions before that paragraph could be a theorem. The established result is exactly a bounded one-round completion with current-decoder inertness and a possible, interface-mediated named-state change.
