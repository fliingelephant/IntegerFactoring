# F159 V2 self-audit

## Result

**Internal pass, pending fresh hostile and statement-only review.**

## Checks

1. The V1 fixed-root-layer theorem is retained only for
   `generated subgroup <H,X>`. V2 never applies its index-two bound to
   refinement-created blocks.
2. The explicit priority scan continues after an `N` comparison, so a
   different hidden-component collision can still return a proper gcd.
3. The exact bound `2|H||X|` uses sequential processing. It does not count
   a redundant full `H` pre-scan followed by a full `K` scan.
4. The compact theorem keeps every V1 hypothesis. In particular, every
   root has a supplied exponent and `gcd(a_i,M)=1`.
5. The odd-order qualification states that every root residue is a public
   power or its public negative. It does not call the integer representative
   inert.
6. The `N=341` certificate satisfies the compact hypotheses with
   `(g,M)=(70,5)` and exponent `a=4`.
7. The legal base record uses square part `t=467`, with
   `gcd(467,70)=1`. Canonical completion reduces it to `s=126`, which is
   the first displayed representative that splits the old block.
8. All direct screens, both complete membership screens, the integer split,
   the local group sizes, the global group size, and the exponent-five gcd
   were recomputed exactly.
9. The post-refinement screen uses cyclic uniqueness of the order-`M`
   subgroup. Its `N` outcome is stated only as two local memberships, not
   as global diagonal membership.
10. The finite factor certificate says that `z` and `s` are already public
    powers. It does not claim that section completion is the only way to
    generate them.
11. The finite factor certificate is not stated as an all-input theorem.
12. V2 leaves three possible progress channels open: new adaptive root
   layers, alignment disagreement, and refinement-created generators.

## Remaining review target

A fresh audit should attack the exact global size `75`, the two CRT-isolated
elements in the proof, and whether the abstract one-dimensional section is
a legal F154 completion instance. It should also verify that no sentence
again conflates root residues with integer subblocks.
