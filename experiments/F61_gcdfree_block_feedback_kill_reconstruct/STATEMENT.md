# F61 reconstruction statement

Work only from this file. Do not read the candidate proof or hostile audit.

Let $N\ge3$. For a unit state $x\in\{2,\ldots,N-1\}$, let
$\iota_N(x)\in\{1,\ldots,N-1\}$ be its canonical inverse and write

\[
x\iota_N(x)=1+k(x)N.
\]

A finite set of endpoint presentations is refined completely into pairwise
coprime blocks $q_1,\ldots,q_s>1$. Every endpoint retains an exact
nonnegative exponent vector over these blocks. All presentations enter the
refinement before duplicate relation values are removed as decoder columns.

The feedback rule selects one current block $g$ and adds the canonical inverse
relation for state $g$. It then recomputes the complete gcd-free refinement.
The rule does not select a product, power, quotient, or proper divisor of
several blocks.

Reconstruct or refute these claims from first principles:

1. If $g>1$ divides $1+kN$, then either $g\le k$, or $g>k$ and the canonical
   inverse of $g$ is $(1+kN)/g$, so its quotient and relation value are the
   same $k$ and $1+kN$.
2. If the initial source contains every unit state $2\le x\le B<N$, then
   after one complete global gcd-free refinement the feedback rule creates
   neither a new relation value nor a proper split of a current block.
3. More generally, if all seed quotients are at most $K$, then the seed list
   plus every valid unit state $2\le x\le\min(K,N-1)$ dominates all repeated
   one-block feedback. If $K=\operatorname{poly}(\log N)$, this domination has
   polynomial size.

Audit composite blocks, repeated block powers, one block dividing several
relation values, duplicate values with different endpoint presentations,
nonunit states, $k=0$, $B\ge N$, $K\ge N$, and repeated feedback.

The intended scope is narrow. Do not infer a barrier for cross-relation
products, powers, quotients, noncanonical representatives, unknown proper
divisors of composite blocks, or large adaptively selected states.

Return a complete proof or the smallest counterexample. State the exact scope
and whether the claim is a source obstruction, a decoder obstruction, or only
a redundancy theorem for this feedback rule.
