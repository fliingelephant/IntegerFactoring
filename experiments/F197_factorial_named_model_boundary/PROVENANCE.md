# F197 provenance

## Primary sources

Alin Bostan, Pierrick Gaudry, and Éric Schost, “Linear Recurrences with
Polynomial Coefficients and Application to Integer Factorization and
Cartier--Manin Operator,” *SIAM Journal on Computing* 36(6), 1777--1806
(2007), DOI
[`10.1137/S0097539704443793`](https://doi.org/10.1137/S0097539704443793),
[author-hosted primary PDF](https://specfun.inria.fr/bostan/publications/BoGaSc07.pdf).

Exact premises used:

- the explicit baby-step/giant-step block construction for factorials;
- the arbitrary-ring
  \(O(\mathsf M_R(\sqrt L)\log L)\) factorial bound;
- the scalar polynomial-coefficient recurrence framework with essentially
  square-root dependence on the target index;
- the deterministic factorization bit bound
  \(O(\mathsf M_{\rm int}(N^{1/4}\log N))\).

Edgar Costa and David Harvey, “Faster Deterministic Integer Factorization,”
*Mathematics of Computation* 83(285), 339--345 (2014), DOI
[`10.1090/S0025-5718-2013-02707-X`](https://doi.org/10.1090/S0025-5718-2013-02707-X),
[arXiv:1201.2116](https://arxiv.org/abs/1201.2116).

Exact premises used:

- bit complexity is in the multitape Turing model;
- for \(N=pq\), \(p<q\), their introduction uses
  \(K=\lfloor\sqrt N\rfloor\), \(\gcd(K!\bmod N,N)=p\), and the explicit
  Strassen/BGS block product;
- their Theorem 1 improves the full deterministic factorization bound to
  \(O(\mathsf M_{\rm int}(N^{1/4}\log N/\sqrt{\log\log N}))\).

No secondary source supplies a mathematical premise.

## Symbolic derivations

The factorial valuations, block-count inequality, modular kernels, lift
identities, output-size bounds, easy power-of-two residue, quotient-bit
recovery, and one-child recurrence are proved directly in `PROOF.md`.
No empirical computation is used.

