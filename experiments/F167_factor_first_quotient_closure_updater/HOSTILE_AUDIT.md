# F167 hostile audit — PASS

## Verdict

**PASS.** The frozen statement and proof establish the claimed conditional
factor-first updater. I found no theorem-level defect in the absolute-order
trichotomy, the relative-order branch, the complete fingerprint closure, the
capacity alternative, or the F166 state lift.

The result remains a decoder for a supplied finite block list. It does not
prove that canonical feedback supplies a useful block, that closure occurs
below the cap, that a capacity branch later collapses, or that every input is
factored.

I changed no frozen input and no durable ledger. I performed no research
computation. The only machine operation used as evidence was the requested
file-integrity hash check.

## Frozen-input integrity

The requested SHA-256 hashes match exactly:

- `STATEMENT.md`:
  `e96e12303520b40c459b92ab192de48f7ffc4829daa20c60686007aba8884aad`
- `PROOF.md`:
  `8e639c631355951a1c9656fbf99df46320a4c75bf4ef745949f01705b4df6060`

I read both files in full. I checked only the needed promoted interfaces from
P87, P92, P93, P148, P150, and P151, with the exact F161 and F166 contracts
where the invocation boundary mattered.

## 1. The `Lambda_B` screen is exact for odd prime powers

For each hidden component, put

\[
r_j=\operatorname{ord}_{R_j}(d).
\]

The full prime-power factors present in
`Lambda_B = lcm(1,...,B)` are exactly the prime powers at most `B`. Hence

\[
r_j\mid\Lambda_B
\quad\Longleftrightarrow\quad
\sigma(r_j)\le B.
\]

If `gcd(d^Lambda_B-1,N)=1`, no hidden residue prime divides the difference.
In particular, no complete component is annihilated. Thus every `r_j` fails
to divide `Lambda_B`, which gives `sigma(r_j)>B` for all `j`.

If the gcd is `N`, every complete component is annihilated and every `r_j`
divides `Lambda_B`. Any intermediate gcd is already a proper factor. This
includes a gcd containing only part of a prime-power component. Therefore
the proof does not silently assume that `N` is squarefree.

## 2. Divisor stripping and local screens

Start with a common multiple `T` of all local orders. For a prime `ell | T`,
the test at `T/ell` has three meanings.

- A result `N` says that every local order divides `T/ell`, so the division
  is valid.
- A result one says that no local order divides `T/ell`. Since every local
  order divides `T`, each has the full current `ell`-adic valuation of `T`.
- Any intermediate value is a proper factor, including partial
  prime-power divisibility.

Repeated stripping therefore either factors `N` or leaves exactly the same
prime-adic valuation in every local order. The final value `m` is the exact
order of `d` in every component.

This also justifies the stated removal of the P87 punctured bank. On the
initial gcd-one branch, no divisor of `Lambda_B` can annihilate even one
component. On the global-return branch, a punctured exponent that exposes a
full-order disagreement is subsumed by stripping. A puncture that exposes
only residue-prime agreement is also subsumed: if the reduced order divides
any punctured exponent missing an `ell`-part of `m`, it already divides
`m/ell`, whose gcd test returns a proper factor.

The same argument validates F166's local-order screens. Once one exact
global order is known, any smaller local order divides `m/ell` for some
prime `ell | m` and therefore produces a proper gcd.

It also supplies the coprimality needed for the absolute-branch F166 call.
If a hidden residue prime `p_j` divided the common final order `m`, the
final test at `m/p_j` would leave an order-`p_j` unit. Such a unit reduces
to one modulo `p_j`, so the gcd would be proper. Hence a no-factor stripping
run has `gcd(m,N)=1`. Since `e=lcm(M,m)/M` divides `m` prime by prime, it
also has `gcd(e,N)=1`.

## 3. The absolute-plus-relative hard branch

The relative scan is used only after the absolute gcd is one. For a local
relative order `e_j`, the complete component `R_j` divides
`d^(eM)-1` exactly when `e_j | e`.

If the first non-one scan value is `N`, all earlier values were one. Each
local relative order divides the current `e`; if any one were smaller, its
own index would have produced a prior non-one gcd. A disagreement among
local relative orders would produce a proper gcd at the first local return.
Thus the common return has exact relative order `e` in every component.

If all values through `B` are one, every local relative order exceeds `B`.
Combining this with the absolute gcd-one conclusion proves both halves of
the displayed double-hard certificate. The proof does not infer quotient
independence from this per-block certificate.

The F161/F166 coprimality boundary causes no gap, although F167 should have
made the implication explicit. The certified old state forces
`gcd(M,N)=1`. Indeed, if a hidden residue prime `p_j` divided `M`, exact
local order `M` would make `g^(M/p_j)` have order `p_j` modulo
`p_j^alpha_j`. Its reduction modulo `p_j` would be one, contradicting the
required gcd-one order screen. Likewise, a first no-factor common relative
return cannot have `p_j | e`: the local element `d^M` has order `e`, so
`d^((e/p_j)M)` would have order `p_j`, reduce to one modulo `p_j`, and make
the earlier `D_(e/p_j)` a proper gcd. The explicit F161 `gcd(e,N)` screen is
therefore safe to include and would only expose the same factor.

## 4. The local fingerprint power map

Fix a component and write `K_j=<H_j,d_1,...,d_t>`. This is cyclic because it
is a subgroup of the unit group of an odd prime power. The map

\[
K_j/H_j\longrightarrow U_j,
\qquad xH_j\longmapsto x^M
\]

is well-defined and multiplicative. Since `H_j` has order `M`, the integer
`M` divides `|K_j|`. The kernel of the `M`-power map on cyclic `K_j` has
order

\[
\gcd(M,|K_j|)=M.
\]

There is only one subgroup of this order, namely `H_j`. The quotient map is
therefore injective, and its image is exactly

\[
F_j=\langle d_1^M,\ldots,d_t^M\rangle.
\]

Thus `Q_j` and `F_j` are isomorphic and cyclic. No hidden logarithm or
squarefree assumption occurs in this step.

## 5. Gcd comparison, BFS closure, and cyclicity

Every newly generated fingerprint is compared with every stored
fingerprint before it is accepted or discarded. For two globally different
values, equality in any complete hidden component makes their difference
gcd nontrivial. Equality in only part of a prime-power component also gives
a proper factor. Consequently, on a no-factor run, every pair of globally
different stored values is different in every hidden component.

If the queue closes, the stored set is the full finite group `F`. Positive
multiplication by the listed generators suffices: in a finite group, the
generated monoid equals the generated subgroup. Projection `F -> F_j` is
surjective by construction and injective by the pairwise comparison. Hence

\[
F\cong F_j\cong Q_j
\]

for every component. Since each `F_j` is cyclic, the global fingerprint
group `F` is cyclic as well. This conclusion is not an unjustified claim
that an arbitrary subgroup of a CRT product is cyclic; it follows from the
proved projection isomorphism.

Continuing comparisons after a candidate equals one stored global value is
safe. It preserves the invariant that every relevant pair was tested and
cannot suppress a partial-component collision.

## 6. Provenance, generator recovery, and the F166 lift

The predecessor chain stores a word `a_y` satisfying `a_y^M=y`. This
identity is preserved along a BFS edge because the unit group is abelian.

On closure, trial division of `kappa=|F|` and the standard prime-divisor
order criterion recover a generator `y=a^M` of the known cyclic table.
Projection isomorphism then gives

\[
\operatorname{ord}_{Q_j}(aH_j)=\kappa
\]

in every component. The hypotheses needed by the F166 lift are therefore
present: a public word, its common exact relative order, and
`a^(kappa M)=1`. F166 either exposes an intervening gcd or returns an exact
common-order state of order `M kappa`.

F166 also states `gcd(kappa,N)=1` as an input condition. This follows from
the closed no-factor table even though F167 does not spell it out. If a
hidden residue prime `p_j` divided `kappa`, cyclic `F` would contain a
nonidentity fingerprint of order `p_j`. Projection preserves its order.
An order-`p_j` unit modulo `p_j^alpha_j` reduces to one modulo `p_j`, so its
comparison with the stored identity would have produced a proper gcd.
This contradicts the no-factor branch. Thus the invocation is valid. An
explicit `gcd(kappa,N)` before F166 would be a harmless factor-first screen,
but it is not logically necessary and its omission does not change the
algorithmic outcome.

The lift also has the right local state semantics. Since `aH_j` generates
the full quotient `Q_j`, the new local cyclic subgroup contains every old
block. Globally, old named generators need not be powers of the new state
generator, and the statement correctly requires their provenance to remain.

When `kappa=1`, the stored group is trivial. Every block lies in every old
local `H_j`, but its hidden logarithms can differ across components. The
statement claims no growth and no global aligned membership. This is the
exact boundary inherited from P150.

## 7. Optional global alignment

On the closed branch, the cyclic table supplies global equations

\[
d_i^M=(a^M)^{c_i}.
\]

Thus `x_i=d_i a^(-c_i)` has `x_i^M=1` and lies in every local `H_j`.
Factor-first alignment either factors `N` or gives one global power of `g`.
The same applies to `a^kappa`. If all alignments succeed, every `d_i` is a
word in `g,a`, while provenance already makes `a` a word in the `d_i`.
This proves equality of the named subgroups.

The resulting two-generator group has order `M kappa`: the presentation
has that upper bound, and every local image already has that order. Its
projection to a local cyclic group is therefore an isomorphism, so global
cyclicity and the Smith-generator conclusion are valid.

The statement correctly keeps these alignments optional for common-order
state growth and necessary for global compression or F164-style relation
accounting.

## 8. The `C+1` capacity branch

When `C+1` globally distinct values have been stored without a proper gcd,
they remain distinct in every component. Therefore each `F_j`, and hence
each isomorphic `Q_j`, has at least `C+1` elements. Since `|H_j|=M`,

\[
|K_j|=M|Q_j|\ge M(C+1).
\]

Closure is not needed for this lower bound. The proof does not mistake
cardinality for rank or independence, and it expressly retains the
synchronized large cyclic quotient as the obstruction.

## 9. Reset and two-ledger semantics

After a strict update, both the exponent in `x -> x^M` and its local kernel
change. Old fingerprint tables and old quotient-capacity counts are
therefore invalid and must be rebuilt. Integer identities, occurrence
records, block decompositions, and generator words do not depend on the
current `M`; retaining them is correct.

The two ledgers serve different equivalence relations. Root-aware
exact-value deduplication is sufficient for parity columns, but it is not
sufficient for endpoint refinement because equal relation values can have
different endpoint factorizations. Keeping every endpoint occurrence in a
presentation ledger preserves gcd overlaps and full word provenance.
Recording an old block's exact decomposition when it splits preserves the
meaning of historical generator words. Nothing in the updater licenses
deletion of those words after an alignment-free state lift.

The frozen-list rule prevents the generated subgroup from changing during
one BFS. New blocks enter only between searches. This makes the closure and
capacity certificates well-defined.

## 10. Quasipolynomial cost and fixed-depth feedback

With numerical bounds `B` and `C` quasipolynomial in `n`, the direct bounds
are valid:

- `Lambda_B` has `O(B log B)` bits;
- stripping and bounded scans use quasipolynomially many modular operations;
- at most `O(tC)` BFS edges are generated;
- direct comparison uses `O(tC^2)` gcds; and
- a shortest predecessor word has length at most `C`.

Factoring a closed `kappa <= C` by trial division is also
quasipolynomial under this numerical cap. Every strict update multiplies
`M` by at least two, while an exact common local order satisfies `M<N`.
There are therefore fewer than `n` strict updates. Resetting and rescanning
a quasipolynomially bounded pool after each update preserves the total
bound.

The fixed-depth corollary is conditional on the complete explicit source
and decoder transcript being quasipolynomially bounded. Its cap covers the
number and bit size of blocks, stored fingerprints, words, relations,
decompositions, occurrences, and coefficients. Under that stated condition,
the two-ledger bookkeeping does not hide an uncapped coordinate or
provenance blow-up.

One wording boundary must remain explicit. Quasipolynomial **bit length of
the integers** `B` and `C` alone would not justify loops of length `B` or
`C`; their numerical values, or equivalently the complete explicit loop
transcript, must be quasipolynomially bounded. Sections 4 and 6 impose this
stronger cap, so the proved cost claim is sound under its operative wording.
Likewise, optional Pohlig--Hellman alignment is quasipolynomial only when
the relevant prime values are numerically bounded as stated there. The
minimal F166 state lift does not require that optional alignment.

## 11. Novelty and scope

Relative to the cited local registry, the increment is real but narrow.

- P87 supplies the punctured bounded-order bank. F167 replaces it, after a
  global return, by factor-first exact-order stripping.
- P92/P93 enumerate powered supplied subgroups under structural promises.
  F167 instead enumerates the complete subgroup of quotient fingerprints
  when it fits below the cap.
- P148 gives the bounded one-block relative-order classification.
- P150 gives the alignment-free lift once a common relative order is known.
- P151 gives finite-bank fingerprint capacity and conditional presentation
  closure. F167 makes the bank adaptive and complete, so closure itself
  yields the exact cyclic local quotient order and a generator word.

This is registry-relative novelty only. No external prior-art search or
publication-level novelty claim is part of this audit.

The scope exclusions are correctly preserved. F167 proves no useful-block
source law, no forced below-cap closure, no contradiction from repeated
capacity certificates, no feedback-only event, and no factoring algorithm.

## Final classification

- Frozen hashes: **PASS**.
- Arbitrary odd prime-power scope: **PASS**.
- `Lambda_B` trichotomy and exact stripping: **PASS**.
- Absolute-plus-relative hard certificate: **PASS**.
- Fingerprint kernel and quotient isomorphism: **PASS**.
- Pairwise gcd synchronization and closed-BFS cyclicity: **PASS**.
- Provenance generator and F166 lift: **PASS**.
- `kappa=1` boundary: **PASS**.
- `C+1` capacity lower bound: **PASS**.
- Reset and two-ledger semantics: **PASS**.
- Fixed-depth quasipolynomial cost under the full numerical/transcript cap:
  **PASS**.
- Registry-relative novelty and stated scope: **PASS**.
- All-input source theorem or factoring algorithm: **not claimed**.

**Overall verdict: PASS.**
