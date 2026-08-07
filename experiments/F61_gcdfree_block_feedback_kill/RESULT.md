# F61 — Gcd-free endpoint-block feedback adds no new small-state relations

**Status:** verifier-backed narrow obstruction. No computation was used. This
version passed hostile audit and proof-blind reconstruction after the latter
forced two scope clarifications: the small-scan source is exact, and the total
dominating-list size includes the original seed presentations.

**Verdict:** the proposed adaptive sampler is exactly redundant for a complete
small-state seed scan. Every endpoint block either was already used as a seed
or reproduces an existing relation value. The feedback closes after the first
global gcd refinement.

This is a method failure for the stated feedback rule. It is not an obstruction
to cross-relation combinations, large-state seeds with exponentially large
quotients, or other adaptive samplers.

## Closest prior route and material difference

The closest promoted result is P66, which computes a gcd-free basis only as a
decoder. P64 closes formal parity cycles of exact inverse-pair labels. F59
tests quotient descent and offset batches.

The proposed retry was materially different at launch: compute the true
arithmetic gcd-free blocks of all known endpoints and feed each block back as
a new modular-inverse state. This uses arithmetic factor sharing rather than
exact endpoint labels. The lemma below shows that this particular feedback
operation nevertheless adds no relation value beyond a nonadaptive small-state
scan.

## 1. Divisor-feedback lemma

Let $N\ge3$. Let $x\in\{2,\ldots,N-1\}$ be a unit modulo $N$, let
$y\in\{1,\ldots,N-1\}$ be its canonical inverse, and write

\[
xy=1+kN.
\tag{1}
\]

Since $y<N$,

\[
1\le k<x.
\tag{2}
\]

Let $g>1$ be any integer divisor of $xy$. Then $g$ is a unit modulo $N$.
Let $\iota_N(g)$ be its canonical inverse and define

\[
g\iota_N(g)=1+k(g)N.
\]

### Lemma

Exactly one of the following useful alternatives holds:

1. $g\le k$; or
2. $g>k$ and
   \[
   \iota_N(g)=\frac{1+kN}{g},
   \qquad
   k(g)=k.
   \tag{3}
   \]

### Proof

The first alternative is only the stated inequality. Suppose $g>k$. Then

\[
1+kN<gN,
\]

so the positive integer

\[
h=\frac{1+kN}{g}
\]

satisfies $h<N$. Equation (1) gives $gh\equiv1\pmod N$. Thus $h$ is the
canonical inverse of $g$. Also $gh=1+kN$, so the new quotient is exactly
$k$. $\square$

The lemma uses any divisor of the relation value, not only a prime factor and
not only one of the two displayed endpoints.

## 2. Closure of the complete small-state scan

Fix $2\le B<N$. Let the initial source consist exactly of every state

\[
x\in\{2,3,\ldots,B\}
\]

that passes the direct screen $\gcd(x,N)=1$. A failed screen has already
factored $N$. For each surviving state, record its canonical inverse pair and
relation (1). Extra seed relations with quotients larger than $B$ are not part
of this theorem. Duplicate endpoint presentations of the same scanned values
are allowed if all of them enter the refinement below.

Refine all known endpoints completely into pairwise-coprime gcd-free blocks
$q_1,\ldots,q_s>1$. “Completely” means that every known endpoint $e$ has an
exact representation

\[
e=\prod_{j=1}^s q_j^{\alpha_{e,j}},
\qquad \alpha_{e,j}\in\mathbb Z_{\ge0},
\tag{4}
\]

and no two current blocks have a nontrivial gcd. This is one global refinement
to a fixed point, not one pairwise gcd operation. Repeatedly apply the proposed
feedback rule:

1. choose an endpoint block $g>1$;
2. add the canonical inverse relation for state $g$ if its relation value is
   new; and
3. recompute the gcd-free endpoint basis.

Equal quotient values are equal relation values $1+kN$. All endpoint
presentations enter the global refinement before equal decoder columns are
deduplicated. This order matters: different factor-pair presentations of the
same value can expose different gcd-free blocks.

### Theorem 1 — one-refinement fixed point

The feedback rule adds no distinct relation value beyond the initial scan.
The gcd-free basis does not refine further after the first global refinement.

### Proof

Every gcd-free endpoint block $g$ divides at least one initial endpoint and
therefore divides its relation value $1+kN$. Equation (2) gives $k<B$.

- If $g\le k$, then $2\le g<B$. Because $g\mid1+kN$, it is a unit modulo
  $N$. Its relation was already included in the initial complete scan.
- If $g>k$, the divisor-feedback lemma gives the same relation value
  $1+kN$. Deduplication removes it.

In the second case, the two endpoints are $g=q_r$ and $(1+kN)/g$. If an
existing endpoint containing $q_r$ belongs to the relation value $1+kN$, then
the exact endpoint representations give

\[
1+kN=
\prod_{j=1}^s q_j^{\alpha_{x,j}+\alpha_{y,j}}.
\tag{5}
\]

Dividing (5) by one copy of $q_r$ leaves a product of whole current blocks,
including the correct remaining multiplicity of $q_r$. Thus the alternative
factor pair cannot expose a proper divisor of any block. In the first case,
the relation and both endpoints were present before the first global
refinement. Thus no feedback step adds a new column or a new gcd split.
$\square$

## 3. General dominance by a nonadaptive scan

Let an arbitrary finite explicit list of valid unit seed presentations have
quotients at most $K$. Augment it with every unit state

\[
2\le x\le\min(K,N-1).
\tag{6}
\]

The cap excludes noninvertible or noncanonical states when a loose bound has
$K\ge N$. The same proof gives the following statement.

### Theorem 2 — dominance

Every distinct relation value obtainable by repeated endpoint-block feedback
from the seed list is already present in the seed list together with the
nonadaptive valid-state scan (6).

If $K=\operatorname{poly}(\log N)$, the dominating scan has polynomial size.
More precisely, the total presentation-list size is the original seed-list
size plus $O(K)$. It is polynomial in $\log N$ when the original explicit list
also has polynomial size. Any useful dependency of the adaptive sublist is
also a dependency of this superset, and P66's complete decoder cannot miss it.
Therefore the feedback adds no factoring power in this range.

This theorem does not say that the full nonadaptive scan succeeds. It says
only that the feedback bookkeeping cannot improve it.

If a current block divides more than one relation value, the conclusion is
unchanged. If $g\mid1+kN$ and $g\mid1+\ell N$, then
$g\mid(k-\ell)$ because $g$ is a unit modulo $N$. If both quotients are less
than $g$, then $k=\ell$. If either quotient is at least $g$, state $g$ already
lies in the direct scan.

## 4. Exact example

Take $N=55$ and $B=4$. The initial relations are

\[
(x,y,k)=(2,28,1),\quad(3,37,2),\quad(4,14,1).
\]

The endpoint gcd-free blocks are $2,3,7,37$. Feeding $7$ gives inverse $8$
and

\[
7\cdot8=56=1+55,
\]

the existing $k=1$ value. Feeding $37$ gives inverse $3$ and the existing
$k=2$ value $111$. Blocks $2$ and $3$ were initial states. The closure adds
nothing.

## 5. Scope and retry rule

This result closes only the rule “feed one gcd-free divisor block back as a
canonical inverse state” when the needed smaller states are already scanned.
A retry is materially new if it uses, for example:

- a cross-relation product or quotient that is not one divisor block;
- a noncanonical inverse representative that changes the quotient;
- a large seed whose quotient bound $K$ is not polynomial, together with a
  proof that only polynomially many selected feedback states suffice; or
- an operation that changes the normalized-root image rather than only the
  endpoint factorization.

No all-input factoring theorem follows. The useful-list source problem remains
open.
