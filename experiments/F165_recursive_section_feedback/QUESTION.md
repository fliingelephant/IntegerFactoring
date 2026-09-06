# F165-D01 — depth-two recursive decorated-section feedback

**Status before the authoritative run:** preregistered finite question.

## Closest prior work

F156 V2 proves that one nonrecursive sparse decorated-section feedback layer
has quasipolynomial cost. Its feedback records stay out of every later
section basis. F109 found finite cross-batch gains in a different,
factor-assisted recursive feedback search.

F165 differs materially in one point. It puts the retained canonical-inverse
records from level one into the public factor-free decoder. It then chooses
the next actual decorated-section basis from that union. It repeats this for
exactly two frozen levels. Thus the first feedback layer can change the
source of the second layer.

## Exact finite question

Use the first 64 lexicographic pairs of distinct primes `p,q` in
`[10000,20000]` with `p<q<2p`. After the corpus is constructed, the public
workflow receives only `N=pq`.

For each `N`, let `n=ceil(log2(N+1))`. The base source contains every unit
seed `c` with `2<=c<=n+1` and its least positive inverse `w` modulo `N`.
Retain the exact value `c*w` with supplied root `1`.

At the base and after each of two recursive feedback levels:

1. Apply supplied-root-aware exact-value deduplication.
2. Build the complete factor-free parity basis.
3. Decode the complete parity kernel and its normalized-root image.
4. Select a deterministic first-occurrence parity basis with its actual
   decorated lifts.
5. Enumerate all nonempty basis subsets of support one or two.
6. Compute the actual decorated star-product `z`.
7. Compute its least positive inverse `w`.
8. Test both `gcd(z-w,N)` and `gcd(z+w,N)`.
9. Retain `z*w` before the union decoder is rebuilt.

The target event is a proper direct gcd or a non-global normalized root that
first occurs at level two. The base and level one must both be null. Also
record strict new exact values and strict factor-free block refinements.

## Scope

This is a finite capability scan. It proves no density, no minimum depth, no
all-input success law, and no asymptotic factoring result. Disclosed `p,q`
may classify results after the public computation. They cannot select a
candidate or enter a public replay.
