# One-block feedback after complete GCD-free refinement

## Verdict

The arithmetic mechanism is valid, but the three claims are not all true as literally written.

1. Claim 1 is true for the intended object: a current block \(g\), hence \(2\le g\le N-1\) and \(\gcd(g,N)=1\). Without the state-range hypothesis, the phrase “canonical inverse of \(g\)” is not defined. For example, \(N=3\), \(k=1\), and \(g=4\mid1+kN\), but \(g\notin\{2,\ldots,N-1\}\).
2. Claim 2 is false if “contains every unit state up to \(B\)” permits additional seeds with quotient larger than \(B\). A small nonvacuous counterexample is \(N=7\), \(B=2\), with seed states \(2\) and \(6\). Feedback on the resulting block \(3\) creates the new relation value \(15\).
3. The structural domination assertion in claim 3 is true. The added saturation has at most \(K\) states and is polynomial-size when \(K=\operatorname{poly}(\log N)\). The *total* dominating source is polynomial-size only if the original seed presentation list is also polynomial-size, or if “size” means the added saturation only.

The corrected result is a redundancy theorem for the specified one-current-block canonical-inverse feedback rule. It is not a decoder obstruction and is not a barrier for any of the operations excluded in the statement.

## 1. Basic bounds for a canonical inverse relation

Let \(x\in\{2,\ldots,N-1\}\) be a unit, let \(y=\iota_N(x)\in\{1,\ldots,N-1\}\), and write

\[
xy=1+k(x)N.
\]

The quotient is never zero. If \(k(x)=0\), then \(xy=1\), impossible because \(x\ge2\) and \(y\ge1\). Also

\[
xy<xN,
\]

so

\[
1+k(x)N<xN
\quad\Longrightarrow\quad
1\le k(x)<x\le N-1.
\]

In particular,

\[
1\le k(x)\le N-2.
\]

These bounds require no parity or compositeness assumption on \(N\).

## 2. The divisor dichotomy

Let

\[
A=1+kN
\]

with \(k\ge0\), and suppose \(g>1\) divides \(A\). Put

\[
h=A/g.
\]

First,

\[
\gcd(g,N)=1,
\]

because every common divisor of \(g\) and \(N\) would divide \(A-kN=1\).

There are two cases.

- If \(g\le k\), this is the first branch of the claimed dichotomy.
- If \(g>k\), then
  \[
  h=\frac{1+kN}{g}
  <\frac{1+gN}{g}
  =N+\frac1g<N+1.
  \]
  Since \(h\) is an integer, \(h\le N\). Equality \(h=N\) would give
  \[
  gN=1+kN,
  \]
  hence \((g-k)N=1\), impossible for \(N\ge3\). Therefore \(1\le h\le N-1\).

If, as in the feedback rule, \(g\) is itself a valid state with \(2\le g\le N-1\), then

\[
gh\equiv1\pmod N
\]

and \(h\) lies in the canonical inverse range. Hence

\[
h=\iota_N(g),
\qquad
k(g)=k,
\qquad
g\iota_N(g)=A.
\]

This proves claim 1 in its intended domain.

The condition \(g\le N-1\) is automatic for a current block. Every current block divides at least one endpoint. Every endpoint is a unit integer in \(\{1,\ldots,N-1\}\), so a block \(g>1\) satisfies

\[
g<N,
\qquad
\gcd(g,N)=1.
\]

If \(k=0\), then \(A=1\), so there is no divisor \(g>1\); the dichotomy is vacuous.

## 3. Why a duplicate relation cannot split a current block

Let \(q_1,\ldots,q_s>1\) be the blocks after complete refinement. They are pairwise coprime. Every endpoint \(z\) has an exact representation

\[
z=\prod_{j=1}^s q_j^{e_j(z)},
\qquad e_j(z)\in\mathbb Z_{\ge0}.
\]

Consider an existing relation value

\[
A=uv=1+kN.
\]

Its block exponents are

\[
\alpha_j=e_j(u)+e_j(v),
\qquad
A=\prod_jq_j^{\alpha_j}.
\]

Suppose feedback selects the whole current block \(g=q_r\), and \(g\mid A\). Pairwise coprimality implies \(\alpha_r\ge1\). Therefore

\[
\frac Ag
=q_r^{\alpha_r-1}\prod_{j\ne r}q_j^{\alpha_j}.
\]

Both proposed feedback endpoints, \(g\) and \(A/g\), are already exact products of whole current blocks. Adding them can neither expose a proper divisor inside a composite block nor create a gcd overlap between two blocks. Complete refinement therefore leaves every current block intact.

This argument also covers:

- a composite block \(g\);
- an endpoint or relation containing \(g\) to a repeated power;
- one block dividing several relation values;
- a duplicate relation value with a previously unseen endpoint presentation.

For the last case, the new presentation can add provenance, but not a new relation value or a block split. The requirement that all already known presentations enter refinement before relation-value deduplication is additionally important in the other branch below: when a saturated state \(g\) is said to be present, its actual endpoint presentation must not have been discarded before refinement.

## 4. The general saturation theorem

Consider an arbitrary finite seed list of canonical inverse relations. Assume every seed quotient is at most \(K\). Before feedback begins, add the canonical inverse relation for every valid unit state

\[
2\le x\le\min(K,N-1).
\]

Retain every endpoint presentation through a complete global GCD-free refinement. Duplicate relation values can then be removed as decoder columns.

Every added saturation state \(x\) also has quotient below \(K\), because

\[
k(x)<x\le K.
\]

Thus every relation present after saturation has quotient at most \(K\).

Let feedback select any current block \(g\). The block occurs in some endpoint and hence divides the relation value \(A=1+kN\) containing that endpoint. Apply the divisor dichotomy.

### Case A: \(g\le k\)

Here

\[
2\le g\le k\le K,
\qquad
g\le N-1,
\qquad
\gcd(g,N)=1.
\]

The saturation list already contains state \(g\) and its exact canonical inverse presentation. Feedback adds nothing new.

### Case B: \(g>k\)

The divisor dichotomy gives

\[
\iota_N(g)=A/g,
\qquad
k(g)=k.
\]

The feedback relation value is exactly the existing value \(A\). By the block-exponent argument in the previous section, its two endpoints are products of whole current blocks. It creates no proper split.

In both cases, one feedback step leaves the set of relation values and the complete block refinement unchanged. Therefore the same argument remains valid after the step. Induction proves domination of every finite sequence of repeated one-block feedback steps. It also proves domination of an indefinitely repeated rule in the sense that every finite prefix is redundant.

There is no assumption that \(g\) is prime or squarefree. The proof uses the whole selected block and nothing below its boundary.

## 5. Claim 2 is false as written

Take

\[
N=7,
\qquad
B=2.
\]

The initial source must contain state \(2\), and let it also contain state \(6\). These are both units. Their canonical relations are

\[
2\cdot4=8=1+1\cdot7
\]

and

\[
6\cdot6=36=1+5\cdot7.
\]

Thus the source satisfies the literal premise: it contains every unit state in \(2\le x\le B\). Its endpoint multiset is

\[
2,4,6,6.
\]

Complete GCD-free refinement gives the pairwise-coprime blocks

\[
q_1=2,
\qquad
q_2=3,
\]

with

\[
2=2,
\qquad
4=2^2,
\qquad
6=2\cdot3.
\]

Select the current block \(g=3\). Its canonical inverse relation is

\[
3\cdot5=15=1+2\cdot7.
\]

The value \(15\) is different from both seed values \(8\) and \(36\). Hence feedback creates a new relation value. Re-refinement also adds the new block \(5\), although it does not split either old block. The asserted conjunction “neither a new value nor a proper split” is false.

This is a smallest nonvacuous counterexample with \(B\ge2\): for \(N<7\), the available canonical unit states and inverse pairs do not produce an unseeded current block with a new inverse-relation value.

### Correct version of claim 2

Claim 2 becomes true under either of the following equivalent sufficient formulations:

- every seed quotient is at most \(B\), and every valid state through \(B\) is present; or
- the source consists of relations generated by states at most \(B\), together with arbitrary duplicate presentations of those same relation values.

Indeed, a relation generated by \(x\le B\) has \(k(x)<x\le B\). The corrected statement is then claim 3 with \(K=B\).

## 6. Size qualification in claim 3

The added saturation contains at most

\[
\min(K,N-1)-1\le K
\]

states. Validity can be tested by gcd, and canonical inverses can be computed by the extended Euclidean algorithm. Thus the added list has polynomial description size and is computable in polynomial bit complexity when \(K=\operatorname{poly}(\log N)\).

This does not make an arbitrarily large original seed presentation list polynomial-size. The distinction is real because different presentations of one relation value are retained through refinement.

For a family illustrating the issue, let

\[
M_r=\prod_{j=1}^r p_j,
\qquad
N_r=M_r-1,
\qquad
K=1,
\]

where \(p_j\) are the first \(r\) primes. Every nontrivial proper divisor \(x\mid M_r\) is a valid state modulo \(N_r\), and

\[
x\cdot\frac{M_r}{x}=M_r=N_r+1.
\]

Thus all \(2^r-2\) such states give distinct endpoint presentations with the single quotient \(k=1\). By Bertrand's bound \(p_j<2^j\), one has \(\log N_r=O(r^2)\), while \(2^r\) exceeds every polynomial in \(r^2\). Hence the seed presentation list can be superpolynomial in \(\log N\) even for constant \(K\).

Therefore the precise size conclusion is:

\[
\text{total size}
=\text{seed presentation size}+O(K).
\]

It is polynomial in \(\log N\) if the seed presentation list is polynomial-size and \(K=\operatorname{poly}(\log N)\), or if only the additional saturation cost is being counted.

## 7. Requested boundary cases

### Composite blocks

The proof never factors \(g\). In Case B, \(A/g\) is obtained by decrementing the exponent of the whole block \(g\). In Case A, the exact state-\(g\) presentation was already included. Composite internal structure is invisible and remains invisible.

### Repeated block powers

If \(A\) contains \(g^e\), division by the selected block gives \(g^{e-1}\). No partial power or internal factor is introduced.

### One block dividing several values

Choose any existing relation value containing \(g\). Its quotient gives one of the two cases. The canonical inverse relation of \(g\) is unique. In particular, if \(g>k\) for two containing values, the divisor dichotomy forces those quotients and relation values to be equal.

### Duplicate values with different presentations

All known presentations must participate in the global refinement before decoder-column deduplication. A later Case B presentation has the same value and endpoints that are exact products of current blocks, so it cannot refine them further.

### Nonunit states

They are outside the feedback rule because a canonical inverse does not exist. They also cannot occur as current blocks when all endpoints are units: every divisor of a unit endpoint is coprime to \(N\). If an external rule supplies a nonunit integer, its gcd with \(N\) can already reveal a divisor, but that is a different mechanism.

### \(k=0\)

No valid state \(x\ge2\) has \(k(x)=0\). In the bare divisor statement, \(1+0N=1\) has no divisor \(g>1\).

### \(B\ge N\)

The canonical state space stops at \(N-1\). The meaningful saturation is

\[
2\le x\le\min(B,N-1).
\]

If \(B\ge N-1\), every valid canonical state is already present, so any whole-block feedback state is present. Structural redundancy follows immediately. The source can have \(\Theta(N)\) states, which is not generally polynomial in \(\log N\).

### \(K\ge N\)

Every canonical quotient already satisfies \(k\le N-2\), and the saturation cap includes every valid state. Structural domination still holds. The number of added states is at most \(\min(K,N-1)\le K\). Thus it is polynomial when \(K\) itself is polynomial in \(\log N\), even on an instance where \(K\ge N\).

### Repeated feedback

One step changes neither current blocks nor relation values. This is the induction invariant, so no number of later one-block steps can escape the saturation.

## 8. Exact scope

The theorem concerns only this operation:

1. select one entire current GCD-free block \(g\);
2. require \(g\) to be a canonical valid unit state;
3. add \((g,\iota_N(g))\) and its relation value;
4. recompute complete global refinement.

It says nothing about selecting any of the following:

- a product of blocks;
- a power of a block;
- a quotient involving blocks;
- a proper divisor hidden inside a composite block;
- a noncanonical representative of a residue;
- a state not bounded by the saturated quotient range;
- a value constructed jointly from several relations.

For example, with \(N=7\) and the lone seed state \(6\), the complete refinement can retain the composite block \(6\), and whole-block feedback merely repeats \(6\cdot6=36\). If a stronger rule were allowed to select the hidden proper divisor \(3\), it would add \(3\cdot5=15\) and split \(6\) into \(2\) and \(3\). That is exactly why the whole-block restriction is substantive.

Accordingly, the valid result is only a source-level redundancy theorem for a narrowly defined feedback closure. It does not show that the decoder is deficient, and it does not establish a general obstruction to producing factor-bearing relations by other adaptive constructions.
