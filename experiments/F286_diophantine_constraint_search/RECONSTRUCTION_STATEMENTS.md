# F286 — Global tangent-cut reconstruction statement

Let N be odd and B,A positive integers with 2B^2 <= N <= 9B^2/4.
Let M=2^k, k>=1, and suppose M <= B/(4096 A^3).

For each odd u in {0,...,M-1}, let v be the unique residue in that set
with uv=N modulo M. Let I_u be the closed interval between the least and
greatest integers in [B,2B] congruent to u modulo M; define I_v similarly.
These are coordinate interval bounds, not discrete congruences on real points.

For each integer pair 1<=a,b<=A, let T_ab be the least integer at least
2 sqrt(abN) congruent to au+bv modulo M. Retain the real constraints

    x in I_u, y in I_v, xy=N, ax+by>=T_ab for all a,b.

Claim: for every u, these constraints have a real solution. The same point
satisfies the corresponding constraints for every ancestral modulus 2^j,
1<=j<=k, using the reductions of u,v. Thus all M/2 branches survive this
particular relaxation and global-tangent menu through that depth.

Reconstruct or refute the claim independently, including the constant 4096.
It does not concern iterated local-minimum cuts, other constraints, compressed
representations, or arbitrary factoring algorithms. No prime-distribution
theorem or numerical observation is needed.
