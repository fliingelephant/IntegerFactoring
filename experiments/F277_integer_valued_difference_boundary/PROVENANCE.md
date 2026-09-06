# F277 provenance

## Closest promoted boundary

F277 addresses an explicit exclusion in P224/F274. The authenticated F274
artifacts are:

| F274 artifact | SHA-256 |
|---|---|
| Statement | 22674281efe2fc593ef8b657bc4782f1892e118a2a193c6f5028d514a245ce47 |
| Proof | 0077b4d4bea0ceed8d4771b78d02a48f67b446af7358a86273145f3215866d0b |
| Frozen root | b7a307fcc0aa0f818e250775499d355fd07396da22bebb4f74e1f5e5b5ebab86 |
| Hostile audit | 9bc97d0d1cb36b0801e335f3f4506dba74785e23b9419ac49b4ef802ec5b7f52 |
| Strict reconstruction | e890d571c53e85088881e088eaf616c1f2933a8a3105c95d53bec922a17e84d3 |

P224 proves that \(\Delta^BF(a)\) is divisible by \(B!\) for
\(F\in\mathbb Z[X]\), and explicitly excludes integer-valued rational
polynomials such as \(\binom XB\). F277 is materially different: it uses
the Newton basis of \(\operatorname{Int}(\mathbb Z)\), then analyzes the
canonical normalized quotient rather than retaining the factorial.

## Binomial-gate context

P171--P177 isolate the balanced beta-two remote coefficient and its exact
quotient/carry boundary. F277 uses their scope as context but does not use a
carry evaluator or a factoring conclusion as a premise.

The closest proof packet for the shifted family is F249/P215:

| F249 artifact | SHA-256 |
|---|---|
| Statement | 2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825 |
| Proof | 8938898cf8118ddcee1b4831468c7f6a62a4928c35688abe61ace52ca8bd9865 |

F249 proves the \(k=0\) shifted-binomial threshold and its unique recurrence
singularity. F277 proves the complete high-difference law (10), including
the exact disappearance of the local asymmetry after \(k>s\).

## Prior symbolic-search context

The authenticated F263 V2 packet and F267 proof boundary have hashes:

| Artifact | SHA-256 |
|---|---|
| F263 V2 algebra | fdf72364070e5b0ded549be171afcf005dc063afe4d7179968aa58ffdbb318d6 |
| F263 V2 frozen root | 2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271 |
| F263 V2 result audit | 320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976 |
| F267 statement | feff0a8b5dfd254cba265c9378106520c4fed718bbff3d507112c59a367045ee |
| F267 proof | f6e95ae5d8a27828cfd4802cdc587f2bba2b2e94d50f523d42b559ef14e4fac3 |

F263 searched short affine block jets, transfers, and fixed numerical
observables. F267 proves that its shifted non-direct hits are public block
boundaries. F277 uses no F263 output. Its exact shifted law and short-side
factor-first theorem explain why adding more finite differences of those
same binomial blocks does not address the remote evaluator.

## Mathematical dependencies

The proof is self-contained. It uses only:

- Newton interpolation on consecutive integers;
- Pascal's identity;
- the inclusion-exclusion formula for Stirling numbers;
- Lucas's and Kummer's elementary prime congruence interpretations;
- Fermat's identity modulo a prime;
- a cyclic group action on set partitions; and
- the ordinary Stirling recurrence.

No external paper, web source, unproved distribution law, factor oracle,
hidden-prime advice, or computational result is used in the proof.

## Evidence boundary

F277 is a candidate proof-only named-family boundary. It awaits a fresh
hostile audit and an independent statement-only reconstruction. It is not
promoted and was not recorded in any durable ledger.

Exploratory finite checks outside the frozen packet motivated inspection of
the simultaneous-zero condition. They are not evidence for any theorem and
are deliberately absent from the statement and proof.
