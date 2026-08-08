# F98 kill target: bounded multi-seed presentation closure

**Status:** precise candidate rule tested by F98. One round has an exact
positive witness. No all-input progress law is claimed.

## Closest prior route and material change

The closest prior route is F97/X68. It keeps one square-inverse seed and
asks for one distinct relation in that seed's square class. Its complete old
subgroup can contain no such relation.

F98 tests a materially larger state. It starts with many seeds, keeps all
nonclosing relations, refines all integer endpoints by exact gcd operations,
and decodes every binary dependency. It also uses several feedback rounds.
It does not require a new relation to match one selected old square class.

## The exact public rule C2T

Let `n = N.bit_length()` and `B = n^2`. The kill test is for odd distinct
semiprimes, but every operation below uses only `N`.

1. Compute `gcd(t,N)` for every `2 <= t <= B`. Return a proper gcd.
2. For every `s = 2,...,n`, retain the canonical-inverse presentation
   `(s, inv_N(s))`. Keep repeated relation values and nonclosing columns.
3. From all retained endpoints, compute an exact factorization-free
   pairwise-coprime basis. Split by gcd and exact perfect-power extraction.
   Express every retained relation product in this basis.
4. Compute the full kernel of the relation matrix modulo two. Test one basis
   of induced square roots with `gcd(root-1,N)` and `gcd(root+1,N)`.
5. Maintain the retained presentations in FIFO order. In each of `n` rounds,
   take the first at most `n` unexpanded presentations whose relation column
   is nonzero modulo two. Let `u <= v` be the two smallest basis blocks in
   the support of that relation. If it has one support block, use `v=1`.
6. For every selected `(u,v)` and every `0 <= e <= B`, in this order retain
   the canonical-inverse presentations of

       [u^e v]_N  and  [u v^e]_N.

   Skip only residues already processed. For each new residue `c`, first test
   `gcd(c-inv_N(c),N)` and `gcd(c+inv_N(c),N)`. Do not delete a relation
   because it fails to close. After the batch, repeat the exact refinement
   and full binary decoder.
7. Return failure if no factor appears after `n` rounds or if the FIFO has no
   unexpanded nonzero column.

The two trajectories include the F96 word `3^99*43` when the exposed pair is
`(3,43)`. The state can receive at most `n-1 + 2*n^2*(n^2+1) = O(n^4)`
presentations. Endpoints and relation products have `O(n)` bits. Standard
integer gcd, exact-root, basis-refinement, and binary linear-algebra
algorithms make the declared rule polynomial in `n`.

## Universal claim originally targeted by the kill test

> After the `n^2` gcd screen, C2T returns a proper factor on every stable
> distinct odd semiprime.

A stronger diagnostic progress claim is also recorded per round:

> Before a factor appears, every nonempty feedback batch either splits a
> previously available integer block or increases binary dependency nullity.

One exact trial-hard stable semiprime on which C2T finishes without a factor
refutes the first claim. One nonempty round with neither event refutes the
second claim.

F98 did not establish either universal claim or its negation. It instead
found one trial-hard stable input on which the complete direct screen is null
but the retained factorization-free relation decoder returns a factor.
