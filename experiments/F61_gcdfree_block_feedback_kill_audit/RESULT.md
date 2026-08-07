# F61 hostile audit — gcd-free endpoint-block feedback

**Candidate audited:** `experiments/F61_gcdfree_block_feedback_kill/RESULT.md`
**Verified candidate SHA-256:** `c3ad4d4f5a210d64feeb803e9e8047e6d0b95310c08bed3aaf088d68fb253658`
**Verdict:** **PASS, with scope clarifications**

No counterexample exists within the stated rule:

- source states are units in ({2,ldots,N-1});
- all endpoint presentations enter one complete global gcd-free refinement;
- feedback feeds one current gcd-free block, not a product, power, or proper divisor of a block;
- equal relation values are deduplicated only as decoder columns, not by discarding known endpoint presentations; and
- the comparison scan contains every valid unit state required by the quotient bound.

The divisor lemma, the one-refinement fixed point, and repeated-feedback dominance are correct under these conditions. The result is a narrow redundancy theorem. It is not an obstruction to other adaptive operations.

## 1. Divisor-feedback lemma

Let (2\le x<N), (gcd(x,N)=1), and let (1\le y<N) be the canonical inverse. Write

\[
xy=1+kN.
\]

Since (x>1), one cannot have (y=1); otherwise (x\equiv1\pmod N), contrary to (2\le x<N). Thus (xy>1) and (k\ge1). Also (y<N), so

\[
1+kN=xy<xN.
\]

Therefore

\[
\boxed{1\le k<x}. \tag{1}
\]

Now let (g>1) divide (1+kN). Since

\[
\gcd(1+kN,N)=1,
\]

every such (g), prime or composite, is a unit modulo (N).

If (g>k), define

\[
h=\frac{1+kN}{g}.
\]

The inequality (g>k) gives

\[
1+kN<gN,
\]

so (1\le h<N). Since (gh\equiv1\pmod N), uniqueness of the inverse representative in ({1,ldots,N-1}) gives

\[
h=\iota_N(g).
\]

Consequently

\[
g\iota_N(g)=1+kN
\quad\text{and}\quad
k(g)=k. \tag{2}
\]

If (g\le k), the other branch is exactly the inequality needed by the scan argument. The dichotomy is exhaustive and disjoint. No primality assumption on (g) occurs.

## 2. Exact gcd-free invariant

The phrase “complete global gcd-free refinement” should have the following exact meaning. There are pairwise-coprime blocks

\[
q_1,\ldots,q_s>1
\]

such that every known endpoint (e) has an exact exponent representation

\[
e=\prod_{j=1}^s q_j^{\alpha_{e,j}},
\qquad
\alpha_{e,j}\in\mathbb Z_{\ge0}. \tag{3}
\]

The refinement is complete: no pair of current blocks has a nontrivial gcd. “One refinement” in the candidate must mean one complete global refinement to this fixed point, not one pairwise gcd operation.

Every current block (g=q_j) divides at least one known endpoint. If that endpoint belongs to a relation

\[
A=xy=1+kN,
\]

then (3) gives an exact block representation of (A), including all multiplicities:

\[
A=\prod_{j=1}^s q_j^{\alpha_{x,j}+\alpha_{y,j}}. \tag{4}
\]

This is the invariant used by both fixed-point theorems.

## 3. One-refinement fixed point

Assume (2\le B<N), and initially scan every unit (x\in{2,ldots,B}). For each initial relation, (1) gives

\[
k<x\le B,
\quad\text{hence}\quad
k<B. \tag{5}
\]

Let (g) be any block after the complete first refinement, and choose an initial relation value (A=1+kN) whose endpoint is divisible by (g).

### Case 1: \(g\le k\)

Then

\[
2\le g\le k<B.
\]

The divisor (g) is a unit because it divides (A\), which is coprime to (N). Therefore state (g), its canonical inverse pair, and its relation value were already included in the complete initial scan.

### Case 2: \(g>k\)

Equation (2) shows that feedback from (g) reproduces the same value (A=1+kN). It does not create a new relation value.

It also cannot refine a current block. If (g=q_r), then (4) has exponent at least one at (q_r), and

\[
\frac Ag
=q_r^{\alpha_{x,r}+\alpha_{y,r}-1}
 \prod_{j\ne r}q_j^{\alpha_{x,j}+\alpha_{y,j}}. \tag{6}
\]

Thus both new endpoints, (g) and (A/g), are exact products of whole current blocks. For every current block (q_j), a gcd with either endpoint is (1) or a whole power of (q_j); it is never a proper nontrivial divisor of (q_j). This remains true when (g) is composite and when a block occurs with exponent greater than one.

Both cases add neither a distinct value nor a new arithmetic atom. Theorem 1 is correct.

## 4. Blocks dividing more than one relation value

Suppose a unit block (g) divides

\[
1+kN
\quad\text{and}\quad
1+\ell N.
\]

Then

\[
g\mid N(k-\ell).
\]

Since (gcd(g,N)=1),

\[
g\mid k-\ell. \tag{7}
\]

If both (k<g) and (ell<g), equation (7) forces (k=ell). Thus the same block cannot reproduce two different smaller-quotient relation values. If one quotient is at least (g), state (g) lies in the nonadaptive scan. Either parent relation therefore gives the same dominance conclusion.

This resolves the case in which a block divides several relation values with different quotients.

## 5. Repeated feedback and the scan \(2,\ldots,K\)

Let every seed be a valid unit source state, and suppose every seed quotient is at most (K). Add every valid unit state (2,\ldots,K) before the first complete gcd-free refinement.

Take any current feedback block (g). It divides an endpoint of some current relation (A=1+kN), where (k\le K). The same dichotomy applies:

- if (g\le k), the scan already contains state (g) and its relation;
- if (g>k), feedback reproduces (A).

Equation (6) shows at the same time that no new block can appear. Therefore the set of distinct relation values and the complete endpoint-block basis are already at a fixed point. Iteration does not change the invariant. This proves Theorem 2.

If (K=\operatorname{poly}(\log N)), the scan contains polynomially many states, and each gcd, inverse, and relation computation has polynomial bit complexity. The dominance conclusion is still only relative to this source rule and the complete square-dependency decoder.

## 6. Edge-case audit

### Composite blocks

Pass. The proof uses only divisibility and coprimality with (N). Equation (6) shows why a composite current block cannot be split by its feedback complement.

### Multiplicities and exponents

Pass, provided the gcd-free basis retains the exact exponent representation (3). If (g^r\mid A), division by one copy of (g) leaves (g^{r-1}). This creates no proper divisor of (g).

### Equal quotients and equal relation values

Pass with an implementation guardrail. Equal (k) values give the same integer (A=1+kN), so one decoder column is enough. Duplicate columns cannot add a useful normalized root: selecting two copies contributes (A^2), whose positive root (A\equiv1\pmod N) is global.

All known endpoint presentations must nevertheless enter the global gcd-free refinement before their equal relation columns are discarded. Otherwise arithmetic information can be lost. For example, with (N=59), both

\[
2\cdot30=60=1+59
\quad\text{and}\quad
3\cdot20=60=1+59
\]

have (k=1). Keeping only endpoints (2,30) can leave the composite coprime block (15); including endpoints (3,20) splits it into (3) and (5). This is not a counterexample to the candidate, because its stated order records every initial inverse pair and refines all known endpoints before deduplicating relation values. It is a counterexample to premature endpoint deduplication.

### Nonunit seeds and blocks

For (1<x<N), a nonunit seed exposes the proper divisor (gcd(x,N)) before feedback. Every endpoint block derived from a valid relation is a divisor of (1+kN), hence is a unit. The general dominance theorem must quantify over valid unit seeds; an arbitrary nonunit integer has no canonical inverse relation.

### \(k=0\)

In the standard range (2\le x<N), equation (1) proves (k\ge1). The only positive canonical case with (k=0) is (x=y=1). Its relation value is (1), which has no block (g>1), so it is inert.

### \(B\ge N\) or \(K\ge N\)

Theorem 1 explicitly assumes (B<N). It must not be extended verbatim. At (x=N), for example, (gcd(x,N)=N), which is not a proper factor, and no inverse exists.

For standard seed states (x<N), all quotients and endpoint blocks are also (<N). A loose bound (K\ge N) should therefore be implemented as the valid-state scan

\[
2\le x\le\min(K,N-1),
\qquad
\gcd(x,N)=1,
\]

with proper nonunit gcds handled separately. This preserves the proof and avoids undefined states.

### Iteratively created blocks

Pass. There are none after the complete first refinement. Equations (4) and (6) show that every feedback endpoint is built from whole existing blocks. Repeating the operation cannot create a proper gcd split.

## 7. Exact scope

The proved obstruction applies only to feeding one current gcd-free block as a canonical inverse state after the needed smaller states have been scanned. It does not cover:

- a proper divisor of a composite block that is not already exposed;
- a product, quotient, or power of several blocks;
- a noncanonical inverse representative;
- feedback that retains duplicate relation values for a purpose other than the square-dependency decoder;
- large-state selection not dominated by a polynomial-size quotient scan; or
- an operation that changes relation values or normalized-root images.

“No factoring power” must be read in this exact decoder-relative sense. The theorem proves containment of distinct relation values and endpoint-factor information. It does not prove that arbitrary adaptive sampling is useless, that the dominating scan succeeds, or that factoring is hard.

## 8. Final verdict

The candidate's mathematical core passes hostile audit. The edge cases do not refute it once its existing (B<N), unit-state, complete-refinement, and single-block conditions are enforced. The candidate should add the formal exponent invariant (3), the endpoint-before-column-deduplication guardrail, and the valid-state cap for loose bounds (K\ge N). These are scope clarifications, not changes to the theorem.

No new computation was run for this audit.
