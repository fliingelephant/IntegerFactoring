# F253 V2 hostile re-audit

## Verdict

**PASS.** The V1 two-column defect is repaired. The rank, subset-count,
odd-multiple, normalized-root-span, and carry claims reconstruct as stated.

## Authentication

| File | Required SHA-256 | Result |
|---|---|---|
| `V2_STATEMENT.md` | `53c7f59bc3f2a2e1b2f38d77661abfe94465945f5ce8691516e5c5c76ec277ba` | match |
| `V2_PROOF.md` | `b76aed1d24455ec1a32d9c586d1b9f55f9b0c713273a9a3a7f1ba54b5ba1afec` | match |

## Hostile checks

Theorem B now requires odd `k>1`, so `kj` and `j` are different indices.
It separately requires both indexed rows to be present and retained, and
requires `y_{kj} != y_j`. Thus every admitted `e_j+e_{kj}` is a genuine
nonzero vector on two distinct retained columns. A modular orbit repetition,
missing index, or cleanup-removed row is outside the pair set.

For an admitted no-carry pair, Pell specialization gives

\[
y_{kj}=F_{k,D}(y_j),\qquad
A_{kj}=A_jG_{k,D}(y_j)^2.
\]

Hence its exact product is square. The supplied-root congruence gives
`x_j x_{kj} = A_j G_{k,D}(y_j) (mod N)`. Unit retention makes normalization
valid, so the normalized root is `+1`. Since the normalized-root map is a
homomorphism on the parity kernel, it is trivial on exactly the binary span
of the admitted pair vectors. V2 makes no claim about vectors outside that
span.

For rank, removal of singleton squares eliminates the zero class. The P214
fibre cap therefore counts at most `B_Sigma` rows in each of the
`2^r-1` nonzero classes, giving `m <= B_Sigma(2^r-1)` and the stated rank
and nullity bounds. Marking one member of each square `k`-subset gives
`k Z_k <= B_Sigma binom(m,k-1)`. The uniform-subset formula is exactly
`2^{-r}`, with the stated relaxation from the rank bound.

Finally, canonical reduction uniquely gives

\[
F_{k,D}(y_j)=y_{kj}+cN,\qquad c\ge0,
\]

and direct substitution gives

\[
A_jG_{k,D}(y_j)^2-A_{kj}=DcN(2y_{kj}+cN).
\]

The right side is zero exactly for `c=0` and positive for `c>0`. The proof
correctly limits this conclusion to the clean polynomial witness and does
not exclude an unrelated square-class coincidence.

