# F196 provenance

## Local antecedent

F196 preserves the notation and balanced-prime congruence from the frozen
F194 proof-only package:

- `experiments/F194_beta2_binomial_hidden_cancellation/V2_STATEMENT.md`;
- `experiments/F194_beta2_binomial_hidden_cancellation/V2_PROOF.md`.

The congruence is reproved in F196, so those files are provenance rather
than external premises.

## Primary published premise

Mugurel Ionut Andreica, “A Fast Algorithm for Computing Binomial
Coefficients Modulo Powers of Two,” *The Scientific World Journal*, 2013,
Article ID 751358, DOI
[`10.1155/2013/751358`](https://doi.org/10.1155/2013/751358), PMCID
[`PMC3856163`](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856163/), PMID
[`24348186`](https://pubmed.ncbi.nlm.nih.gov/24348186/).

Exact premise used:

- for modulus \(2^T\), preprocessing costs
  \(O(T^3\mathsf M(T)+T^4)\) bit operations;
- after preprocessing, one coefficient \(\binom P Q\bmod2^T\), with
  \(0\le Q\le P\le2^T-1\), costs
  \(O(T^2\log T\,\mathsf M(T))\) bit operations.

The abstract and Sections 7--8 state this range and complexity. F196 does
not use the Section 9 extension for \(P\ge2^T\).

## Derivation boundary

All other claims in F196 are proved symbolically from the displayed
definitions, Lucas' theorem, Euclidean division, modular inversion, and the
Chinese remainder theorem. No secondary source, unpublished computation,
or empirical timing is used.

