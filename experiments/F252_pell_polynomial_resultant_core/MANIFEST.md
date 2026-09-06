# F252 manifest — frozen proof packet

## Status

F252 is frozen as a proof-first structural packet. It contains no research
computation and makes no empirical claim.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | cf49a2ea6ef9158f7ed60e79385b5aad5f28bd7583e9404216eadadf30457cf7 |
| PROOF.md | acf073dc3c5c402eca8b5c9769ce14cc357d5c13ff74caa02c633ce5ac47c130 |
| SELF_AUDIT.md | ac52eddb4ea9bd560007097dc22cadf88ecf0e7d6f9c0027c262bb10ef9e43c9 |

Any mathematical change to one of these files requires a new version and new
hashes.

## Exact contents

The packet proves:

1. the exact content and irreducibility of every post-wrap polynomial
   \(1+D(T-kX)^2\);
2. the closed pairwise resultant formula;
3. the exact zero-resultant and duplicate classification;
4. the complete generic binary square kernel;
5. an integral generic square root with only a global normalized sign;
6. zero generic kernel after constant-square and duplicate cleanup;
7. factor-free saturation of every specialized row by its pairwise
   resultants; and
8. a private parity pivot for every nonsquare residual outside that
   resultant support.

## Comparison boundary

P68 already certifies unit-denominator generic polynomial dependencies as
global-root decoys. F252 does not claim that general principle as new. Its
family-specific gains are the zero cleaned generic kernel, the integral root
construction with no denominator exception, and the explicit
resultant-supported numerical core.

## Exclusions

The packet does not prove:

- that the specialized numerical kernel is zero;
- that every row has a nonsquare private residual;
- any probability bound for the resultant-supported core;
- any non-global root law;
- any claim about implicit banks larger than their materialized input; or
- a quasipolynomial factoring algorithm.

## Methods and provenance

The proof uses elementary Pell identities, polynomial content, quadratic
discriminants, the root definition of the resultant, unique factorization in
\(\mathbb Q[X]\), Sylvester-matrix specialization, gcd saturation, and exact
bit-length accounting.

No script, remote host, random source, dataset, numerical scan, computer
algebra system, hostile audit, strict statement-only reconstruction, human
audit, or publication-level literature review was used. F250 is context only
and is not evidence for F252.
