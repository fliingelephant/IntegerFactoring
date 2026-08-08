# F105 — factor-free and hidden-prime core equivalence

## Question

Does the public P66 gcd-refined row presentation expose the same dependency
core as the unavailable prime-factor parity matrix for every explicit batch,
or was the F102/F103 column-hash match accidental?

## Method

Prove a per-prime parity invariant for the exact gcd-refinement step. At
termination, use pairwise coprimality of the public blocks to classify every
hidden prime row. Then compare row supports, kernels, degree-one peeling, and
column-incidence components.

## Falsifiers

The claim fails if a nonzero hidden prime row is absent from the public row
supports, if a public nonsquare-block row has no hidden prime witness, or if
row multiplicity can change the degree-one peeling core.

## Scope

This is a decoder and compression theorem for an already explicit finite
batch. It supplies no relations, no useful root, and no all-input factoring
law.
