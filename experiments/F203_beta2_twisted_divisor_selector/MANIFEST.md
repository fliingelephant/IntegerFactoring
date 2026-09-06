# F203 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `10481fa918cffefe71eee3dee08ad23b7b837d685c899a23e5c03a2a74aa9b4f`
- `PROOF.md`
  - SHA-256: `415b2079baed3b0d01ffa1b82d2d537dbf5288c2dce0640a0175f4bb1515c174`
- `SELF_AUDIT.md`
  - SHA-256: `4883be9a2bb0738fa83c527cfa00bb79e7fb4886a66492959fb8cb6f43e9e44f`
- `PROVENANCE.md`
  - SHA-256: `897e48c467222e4ebb58b5e11971bcbb3cf7962fcd2ee26285d7b23f8a5137de`

## Evidence class

Proof-only candidate. No mathematical computation was run. Hashing was used
only to freeze the text. No durable proved or failed ledger was changed.

## Claims to audit

1. The public sibling relation
   \(w_{m,r}(q)=\lambda w_{m,r}(p)\) when both factors share the parent
   class, and zero support for \(q\) otherwise.
2. The three exact values of the corrected twisted divisor coefficient
   \(T\), including the sign reversal when \(T=\epsilon(p-q)\).
3. Polynomial-time factor extraction from each value of \(T\), and the
   converse evaluation from the factorization.
4. The formal Lambert-series coefficient identity and the
   \(m=2,r=1\) specialization to \(\chi_4\).
5. Integrality, size, and coprimality of \(K\) and both candidate
   \(K'_a\).
6. The lift parity relation and the exact coalescence criterion
   \(K'_0=K'_1\) if and only if \(\delta=1,r=c\).
7. The first-stage specialization
   \(K'_0=K'_1=(N-3)/4\) for \(N\equiv3\pmod4\).
8. The scope of the one-child recurrence and the explicit absence of a
   recursive decoder.

## Required reviews

1. Fresh hostile audit of the frozen statement and proof.
2. If that audit passes, fresh strict statement-only reconstruction.
3. Promote only after both reviews pass and the frozen hashes are rechecked.

