# Preserve useful dyadic phases without losing the sufficient normal cover

**Family:** route:F31

**Status:** root-derived elementary corollaries with finite checks; no localized
count algorithm or novelty claim. The approximation argument uses the exact
factor-cost inequality in
`../F289_modular_support_union/PATCH_RECONSTRUCTION.md`.

## Mixed parity makes the complete histogram uniform

If N is odd and exactly one of a,b is even, the map

    u -> a*u+b*N/u mod2^k

is a bijection of the odd residues. Its derivative a-b*N/u^2 is odd;
each solution lifts uniquely from modulus2 to modulus2^k. Therefore its
histogram is exactly1 on odd objective residues and0 on even ones. In
particular the noncentral normals in the literal dyadic menu have uniform
complete histograms. This says nothing about their unwrapped geometry.

## An odd normal menu with stationary roots at every depth

For odd composite N, let n be its bit length and r=N mod8 in {1,3,5,7}.
Use the public menu

    a_j=2^(j+3)+r, b_j=65,  0<=j<=n+4.

Both weights are odd and a_j=b_j*N mod8. Hence b_j*N/a_j is1 mod8 and
the stationary square equations have roots at every dyadic depth. This
avoids the specific no-stationary-root degeneration of the (1,1) histogram
when N=3 mod8.

The first ratio a_0/65 is below1, the last exceeds N, and consecutive ratios
have quotient strictly less than2. For any factor pair 3<=p<=q, one normal
therefore has (a_j/b_j)/(q/p) between1/sqrt(2) and sqrt(2). The same
one-percent approximation argument applies unchanged at N/16<M<=N/8.
There are O(n) queries with O(n)-bit weights, all chosen from N alone.

The counterexamples in REPORT.md concern the fixed (1,1) histogram. They
do not compare this entire menu. Nonetheless a nonuniform complete histogram
is still a modular marginal: its positive mass does not certify a short
unwrapped cap point. The missing operation remains joint localization, now
with a normal family that preserves a nondegenerate dyadic phase.

`normal_grid_check.py/json/log` checks the mixed-parity permutation and the
factor-cost margin on a finite labelled matrix. Labels never select a query.
