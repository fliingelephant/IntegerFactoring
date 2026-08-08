# F110 — frozen-batch seed-pair rescue

## Question

Does F109 need recursive feedback, or can one public nonadaptive polynomial
batch reproduce its six cross-batch successes?

## Source

For each of the seven F109 inputs:

1. retain the initial residues `2..n`;
2. compute the factor-free gcd/perfect-power block basis of this frozen seed
   endpoint batch;
3. for each seed relation, select its first two public blocks by the declared
   F98 rule and generate both exponent trajectories through `0..n^2`;
4. freeze this complete first layer;
5. append both exponent trajectories for every unordered integer pair
   `2 <= u < v <= n` in lexicographic order;
6. keep one joint parity decoder and every direct endpoint screen throughout.

The second menu is fixed before any generated relation is inspected.  It
contains `O(n^2)` pairs and `O(n^2)` states per pair, so the explicit source
has `O(n^4)` residues.

The discovery implementation factors endpoint values to accelerate parity
decoding.  A promoted fixed witness requires a separate N-only replay with
the factor-free P106 basis.

## Falsifiers

The nonadaptive explanation fails on an input if the frozen source reaches
the end of the complete seed-pair menu without a factor.  The cross-batch
interpretation fails if a successful parity dependency uses no relation from
the frozen first layer outside its initial seed columns.

## Scope

This is a seven-input control.  Success would remove recursion from these
specific witnesses.  It would not prove that the frozen source factors every
input or that its success probability is bounded below.
