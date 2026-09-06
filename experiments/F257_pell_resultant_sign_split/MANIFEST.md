# F257 manifest — frozen proof packet

## Status

F257 is frozen as a proof-only refinement of P217. It contains no research
computation and makes no empirical claim.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | de5c6833d7a5af14b144188b24cfa0c6e4734d5699824689baeed0bb45b2aa8a |
| PROOF.md | f5d1efbc4a61d67fe2cb4c68de7b96ceec281d144b1a899dd5eb8d737f99ab73 |
| SELF_AUDIT.md | 7ff1899f338f6079886fe827ab4fba35d5b40820b22d65e13df1b20d8bd0932f |

Any mathematical change to one of these files requires a new version and
new hashes.

## Exact contents

The packet proves:

1. the full odd-prime-power split of a shared same-\(D\) Pell-row gcd into
   public equal-coordinate and opposite-coordinate channels;
2. the exact factor-of-two overlap and missing-lcm correction;
3. divisibility of the two signed gcds into P217's two explicit resultant
   factors;
4. two closed orbit-index/carry formulas for those factors;
5. a one-sided Jacobi-minus-one gcd screen under a public short nonzero carry
   condition;
6. factor-free signed refinement of an explicit P66 bank; and
7. exact global and non-global examples with the same minus coordinate
   label, proving that the coordinate label does not determine the
   normalized-root sign.

## Exclusions

The packet does not prove:

- an inverse-QP lower bound for the split-side resultant-zero event;
- existence of a signed resultant-supported square dependency;
- a non-global-root law for such dependencies;
- a sign split for different discriminants; or
- a complete factoring algorithm.

## Methods and provenance

The proof uses exact Pell identities, valuation accounting, P217's closed
same-discriminant resultant formula, quadratic norm anisotropy over finite
fields, Jacobi symbols, Euclidean gcds, and P66 factor-free refinement.

The global \(N=13859\) certificate is derived symbolically from the exact
sixth \(D=2\) Pell power and the fifth-multiple identity. The non-global
\(N=143\) arithmetic is the preserved F253 certificate and is explicitly
not a screen-free hit.

No script, remote host, random source, dataset, numerical scan, computer
algebra system, hostile audit, strict statement-only reconstruction, human
audit, or publication-level literature review was used.
