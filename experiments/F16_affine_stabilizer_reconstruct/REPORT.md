# Independent reconstruction: affine stabilizer-chain claims

## Verdict and conventions

All seven requested claims are correct with the following explicit conventions and scope.

- For a nontrivial finite group \(G\), \(\mu(G)\) is the least cardinality of a finite set \(\Omega\) for which there is an injective homomorphism \(G\hookrightarrow \operatorname{Sym}(\Omega)\).
- The integer parameters \(N,r\) below are at least \(2\). If the trivial case is wanted, the displayed empty-sum formula uses the convention \(\mu(1)=0\), allowing the empty permutation set; under the convention that permutation degrees must be positive, instead \(\mu(1)=1\).
- An affine element is written \((b,a)\), acts by \(x\mapsto ax+b\), and has \(a\) a unit.
- A base means a set (or ordered tuple) of points whose pointwise stabilizer is trivial.
- “Explicit permutation action” means that the degree-\(d\) domain and permutations on it are represented explicitly, rather than by a circuit, oracle, or other succinct description.

No computation is used in this reconstruction.

## 1. The prime-order degree obstruction

**Proposition.** If a finite group \(G\) contains an element of prime order \(p\), every faithful permutation action of \(G\) has degree at least \(p\).

**Proof.** Let \(g\in G\) have order \(p\), and let
\[
\rho:G\longrightarrow S_d
\]
be faithful. Then \(\rho(g)\) also has order \(p\). A permutation of prime order \(p\) is a product of disjoint cycles of lengths belonging to \(\{1,p\}\), with at least one \(p\)-cycle. Therefore it moves at least \(p\) points, so \(d\ge p\). \(\square\)

The word “explicit” is not needed for this mathematical lower bound. It matters later when converting a degree bound into an input-size or running-time obstruction.

Now let \(\rho_i:G\to S_{d_i}\) be a family of actions whose diagonal action is faithful, equivalently
\[
\bigcap_i\ker\rho_i=1.
\]
For an element \(g\) of order \(p\), not every \(\rho_i\) can kill \(g\). Some \(\rho_j(g)\) is nonidentity; its order divides \(p\), hence equals \(p\). Applying the preceding cycle argument to that component gives \(d_j\ge p\).

This general argument says that some component **detects the chosen element**. It does not in general say that some component is faithful on all of \(G\).

## 2. The prime-field affine group

Let
\[
G_p=\operatorname{AGL}_1(\mathbb F_p)
   =T_p\rtimes \mathbb F_p^\times,
\qquad
T_p=\{(b,1):b\in\mathbb F_p\}\cong C_p.
\]
With the convention \((b,a):x\mapsto ax+b\), multiplication is
\[
(b,a)(c,d)=(b+ac,ad).
\]

### Minimum faithful degree

The natural action on \(\mathbb F_p\) is faithful: if \(ax+b=x\) for every \(x\), evaluation at \(0\) gives \(b=0\), and evaluation at \(1\) then gives \(a=1\). Thus \(\mu(G_p)\le p\).

The subgroup \(T_p\) contains an element of order \(p\), so the prime-order obstruction gives \(\mu(G_p)\ge p\). Hence
\[
\boxed{\mu(G_p)=p.}
\]

### Bases in the natural action

The ordered pair of affine points \((0,1)\) is a base: fixing \(0\) forces \(b=0\), and then fixing \(1\) forces \(a=1\).

For a single point \(x\), its stabilizer consists of
\[
x\longmapsto a(x-x_0)+x_0,
\qquad a\in\mathbb F_p^\times,
\]
where \(x_0=x\). It has size \(p-1\). Consequently the natural action has base size \(2\) for \(p>2\). For \(p=2\), the multiplier group is trivial, \(G_2=C_2\) acts regularly on two points, and either one point is already a base. Thus its base size is \(1\).

### Every nontrivial normal subgroup contains the translations

**Lemma.** If \(K\lhd G_p\) and \(K\ne1\), then \(T_p\le K\).

**Proof.** If every element of \(K\) has multiplier \(1\), then \(K\le T_p\); since \(|T_p|=p\), nontriviality gives \(K=T_p\).

Otherwise choose \(k=(b,a)\in K\) with \(a\ne1\). For a translation \(t_c=(c,1)\), conjugation by \(k\) sends \(t_c\) to \(t_{ac}\). Hence
\[
kt_ck^{-1}t_c^{-1}=t_{(a-1)c}.
\]
This commutator belongs to \(K\), because \(K\) is normal. Taking \(c=1\) gives a nonidentity translation. A nonidentity subgroup of the order-\(p\) group \(T_p\) is all of \(T_p\), so \(T_p\le K\). For \(p=2\), the first case already covers the whole group. \(\square\)

If an action of \(G_p\) is nonfaithful, its kernel is a nontrivial normal subgroup, so it kills all of \(T_p\). Therefore, if a diagonal family of actions of \(G_p\) is faithful, at least one component must itself be faithful: were every component nonfaithful, every component kernel would contain \(T_p\), and so would their intersection.

This last conclusion is special to the monolithic normal-subgroup structure of \(G_p\). It must not be transferred to a CRT product of several such groups.

## 3. The cyclic minimum-degree theorem

Let
\[
r=\prod_{i=1}^s q_i,
\qquad q_i=\ell_i^{e_i},
\]
where the \(\ell_i\) are distinct primes.

**Theorem.**
\[
\boxed{\mu(C_r)=\sum_{i=1}^s q_i.}
\]

**Upper bound.** For each \(i\), let \(C_r\) act transitively through its quotient of order \(q_i\), on a set of size \(q_i\). Take the disjoint union of these actions. If \(g\) generates \(C_r\), its image has order
\[
\operatorname{lcm}(q_1,\ldots,q_s)=\prod_iq_i=r,
\]
so the disjoint action is faithful. Its degree is \(\sum_iq_i\).

**Lower bound.** Consider an arbitrary faithful action of \(C_r=\langle g\rangle\), and decompose its domain into orbits of sizes \(d_1,\ldots,d_m\). Every \(d_j\) divides \(r\). On a transitive orbit of size \(d_j\), the image of \(g\) has order \(d_j\). Therefore the whole action is faithful exactly when
\[
\operatorname{lcm}(d_1,\ldots,d_m)=r.
\]

For each \(q_i\), the full prime power \(q_i\) must divide at least one \(d_j\); otherwise the least common multiple would have \(\ell_i\)-adic exponent below \(e_i\). Assign each \(q_i\) to one such orbit, and let \(S_j\) be the set of prime powers assigned to orbit \(j\). Since the members of \(S_j\) are pairwise coprime,
\[
d_j\ \ge\ \prod_{q_i\in S_j}q_i\ \ge\ \sum_{q_i\in S_j}q_i
\]
for every nonempty \(S_j\). The final elementary inequality holds for pairwise-coprime integers at least \(2\): for two such integers \(u,v\), they cannot both equal \(2\), and \(uv\ge u+v\); induction gives the finite-set version. Summing over the orbits, including any unassigned orbits only on the left, yields
\[
\sum_{j=1}^m d_j\ge\sum_{i=1}^s q_i.
\]
This proves the lower bound and the theorem. \(\square\)

In particular, when \(r=\ell^e\) is a prime power, the formula says \(\mu(C_r)=\ell^e\). No squarefree assumption occurs anywhere in the proof.

## 4. Affine groups over \(\mathbb Z/N\mathbb Z\)

Write
\[
N=\prod_{i=1}^s q_i,
\qquad q_i=\ell_i^{e_i},
\]
with distinct primes \(\ell_i\). The Chinese remainder theorem gives compatible isomorphisms
\[
\mathbb Z/N\mathbb Z\cong\prod_i\mathbb Z/q_i\mathbb Z,
\qquad
(\mathbb Z/N\mathbb Z)^\times\cong
\prod_i(\mathbb Z/q_i\mathbb Z)^\times.
\]
Because multiplication of units on the additive ring is coordinatewise, these induce a group isomorphism
\[
\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)
\cong
\prod_i\operatorname{AGL}_1(\mathbb Z/q_i\mathbb Z).
\]

### Lower bound

The translation subgroup is the additive group of \(\mathbb Z/N\mathbb Z\), hence is cyclic of order \(N\). The restriction of a faithful action of a group to any subgroup is faithful. Therefore
\[
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
\ge \mu(C_N)
=\sum_iq_i.
\]
This proves the lower bound for arbitrary prime powers, not only for squarefree \(N\).

### Upper bound

For each \(i\), the local affine group
\[
G_{q_i}=\operatorname{AGL}_1(\mathbb Z/q_i\mathbb Z)
\]
acts faithfully on the \(q_i\) ring elements: an affine map fixing every point has \(b=0\) by evaluating at \(0\), and then \(a=1\) by evaluating at \(1\).

Under the CRT product isomorphism, let \(\prod_iG_{q_i}\) act on the disjoint union
\[
\Omega=\bigsqcup_i\mathbb Z/q_i\mathbb Z
\]
by letting the \(i\)-th factor act naturally on its own component. If a product element fixes all of \(\Omega\), each coordinate fixes its local component and is therefore the identity. The action is faithful and has degree \(\sum_iq_i\). Consequently
\[
\boxed{
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
=\sum_{\ell^e\parallel N}\ell^e.}
\]

For a single prime power \(N=\ell^e\), both bounds give \(\mu=\ell^e\). For a distinct semiprime \(N=pq\),
\[
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)=p+q.
\]
If \(p,q=\Theta(\sqrt N)\), then \(p+q=\Theta(\sqrt N)=2^{\Theta(\log N)}\). Thus the minimum explicit faithful degree is exponential in the bit length of a balanced semiprime.

### Constructibility caveat

The disjoint-union upper bound is **factor-aware**. To instantiate it one needs the prime-power factors \(q_i\), the CRT projections, and the local domains. It is an abstract existence proof after the factorization is known; it is not a factor-finding construction.

Nor does this upper-bound construction, by itself, prove that every arbitrary presentation of every minimum action comes with labeled CRT components or efficiently reveals the factors. If an ordinary explicit minimum action and a known generator of the translation subgroup are additionally supplied, further analysis of that generator's cycles can reveal prime-power orbit lengths; that is a separate structural/input-access statement, and processing the explicit domain already costs time proportional to its degree.

## 5. Degree and base size are different invariants

The natural prime-field affine action has degree \(p\), while its base is the ordered pair of affine points \((0,1)\) for \(p>2\). At \(p=2\), its degree is still \(2\), but one point is a base.

More generally, the natural action of \(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\) on \(N\) points has \((0,1)\) as a base. A point stabilizer is isomorphic to \((\mathbb Z/N\mathbb Z)^\times\), so for \(N\ge2\) a singleton is a base only when \(N=2\).

Now let \(N=pq\) with distinct primes, and consider the CRT disjoint local action of \(G_p\times G_q\) on
\[
\mathbb F_p\sqcup\mathbb F_q.
\]
For any chosen point set \(B\), write \(B_p=B\cap\mathbb F_p\) and \(B_q=B\cap\mathbb F_q\). Its pointwise stabilizer is
\[
(G_p)_{(B_p)}\times(G_q)_{(B_q)}.
\]
Thus \(B\) is a base exactly when each local part is a base, and the minimum base size is the sum of the two local base sizes. It follows that
\[
b=p\text{-local base size}+q\text{-local base size}
=
\begin{cases}
4,&p,q\text{ odd},\\
3,&N=2q\text{ with }q\text{ odd}.
\end{cases}
\]
For example, use \(\{0,1\}\) in each odd component and any one point in the two-point component.

These constant base sizes do not reduce the permutation degree \(p+q\).

## 6. Homogeneous coordinates and the exponent stabilizer

An affine point \(x\) is represented in homogeneous coordinates by
\[
\binom{x}{1}.
\]
The affine map \(x\mapsto ax+b\) is represented by
\[
A_{a,b}=\begin{pmatrix}a&b\\0&1\end{pmatrix},
\qquad
A_{a,b}\binom{x}{1}=\binom{ax+b}{1}.
\]
In particular, the affine point \(1\) is \((1,1)^T\), not \(e_1=(1,0)^T\). The vector \(e_1\) lies outside the affine chart whose last coordinate is \(1\).

Separately, take \(a\in(\mathbb Z/N\mathbb Z)^\times\) and
\[
M_a=\operatorname{diag}(a,1)\in
\operatorname{GL}_2(\mathbb Z/N\mathbb Z).
\]
The additive group \(\mathbb Z\) acts on column vectors by \(k:v\mapsto M_a^kv\). This is literal equality of vectors, not equality of projective classes. (After projectivizing, every scalar multiple \((a^k,0)^T\) would represent the same class as \(e_1\), producing a different stabilizer.) Negative exponents are defined because \(a\) is a unit. Since
\[
M_a^ke_1=\binom{a^k}{0},
\]
the stabilizer of \(e_1\) in this exponent action is
\[
\operatorname{Stab}_{\mathbb Z}(e_1)
=\{k\in\mathbb Z:a^k\equiv1\pmod N\}.
\]
If \(t=\operatorname{ord}_N(a)\), the kernel of the homomorphism \(\mathbb Z\to\langle a\rangle\), \(k\mapsto a^k\), is exactly \(t\mathbb Z\). Hence
\[
\boxed{\operatorname{Stab}_{\mathbb Z}(e_1)
=\operatorname{ord}_N(a)\,\mathbb Z.}
\]
Computing the least positive element of this stabilizer is therefore exactly modular order finding. This statement requires \(a\) to be a unit; it is not an assertion about powers of an arbitrary nonunit.

## 7. Algorithmic conclusion, with its exact scope

Let \(L=\lceil\log_2N\rceil\). For balanced \(N=pq\), every faithful explicit permutation action of the affine group has degree
\[
d\ge p+q=2^{\Theta(L)}.
\]
In an ordinary explicit permutation representation, even one degree-\(d\) generator is represented by its images on \(d\) points, so merely reading or storing it costs \(\Omega(d)\). Standard explicit-permutation Schreier--Sims procedures, and Luks-style routines operating on such an explicitly enumerated domain, therefore do not become polynomial in \(L\) merely because the action has a constant-size base.

This is a representation-size conclusion, not a general impossibility theorem. It does **not** rule out:

- quotient certificates that avoid a faithful action of the entire affine group;
- succinct, oracle, or circuit representations of permutations;
- algorithms exploiting special arithmetic structure without enumerating the permutation domain;
- new stabilizer algorithms acting directly on matrices or modules;
- polynomial-time order finding or factoring by some logically unrelated method.

## Edge-case and scope audit

1. **Characteristic two.** \(\mu(G_2)=2\), but the natural two-point regular action has base size \(1\), not \(2\).
2. **Prime powers.** The terms in all sums are the full powers \(\ell^e\parallel N\), not merely the primes \(\ell\). The cyclic lower bound explicitly forces the full \(\ell\)-adic exponent into some orbit length.
3. **Trivial modulus/group.** The formulas are stated for \(N,r\ge2\). At \(1\), the answer depends on whether degree zero is allowed.
4. **Repeated semiprime.** The displayed \(p+q\) statement is for distinct primes. If \(N=p^2\), it is a single prime power and the formula gives \(\mu=p^2\), not \(2p\).
5. **Even distinct semiprime.** For \(N=2q\) with odd \(q\), the disjoint local base size is \(1+2=3\).
6. **Arbitrary actions.** The degree lower bounds do not assume transitivity. Orbit decompositions are part of the cyclic proof.
7. **Diagonal families.** For general groups, faithfulness only ensures that every nonidentity element is seen somewhere. A faithful component is forced for \(G_p\) because every nontrivial normal subgroup contains \(T_p\). It is not forced for \(G_p\times G_q\): the two coordinate actions can each be nonfaithful while their diagonal is faithful.
8. **Natural versus disjoint action.** The natural action over \(\mathbb Z/N\mathbb Z\) has degree \(N\) and base size \(2\) for \(N>2\). The factor-aware disjoint action has minimum degree \(\sum q_i\), with a different base calculation.
9. **Coordinates.** The ordered base \((0,1)\) consists of two affine points. It must not be confused with the homogeneous vector \((0,1)^T\), nor may \(e_1=(1,0)^T\) be called the affine point \(1\). The exponent stabilizer is a vector stabilizer, not a projective stabilizer.
10. **Order finding.** The exponent-stabilizer identity assumes \(a\) is invertible modulo \(N\); this is what makes a \(\mathbb Z\)-action by all positive and negative powers possible.
11. **Complexity claim.** The obstruction concerns ordinary explicit permutation input. Constant base size alone does not compress such input and does not justify claims about other representation models.

## Exact retry boundary

Within the conventions at the start, the requested theorem package passes and needs no mathematical retry. A revision or new proof attempt is required if a target statement crosses any of these exact boundaries:

- it includes \(N=1\) or \(r=1\) without fixing the degree-zero convention;
- it replaces the prime-power terms \(\ell^e\) by their underlying primes;
- it claims the CRT disjoint action can be constructed without already knowing the factorization;
- it claims, solely from the upper-bound construction, that every presentation of every minimum action efficiently reveals factors;
- it extends the “one component is faithful” conclusion from \(G_p\) to arbitrary groups or CRT product groups;
- it assigns base size \(2\) to the natural action at \(p=2\), or base size \(4\) to the \(2q\) disjoint action;
- it identifies \(e_1=(1,0)^T\) with an affine point, or silently projectivizes the vector exponent action, rather than treating it separately;
- it applies the modular-order stabilizer identity to a nonunit \(a\);
- it upgrades the explicit-degree obstruction into a lower bound against quotient, succinct, circuit, arithmetic, or direct matrix algorithms.

Any such stronger assertion is outside what the proofs above establish; it should be removed, separately proved, or explicitly qualified before acceptance.
