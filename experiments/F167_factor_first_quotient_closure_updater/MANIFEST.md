# F167 final manifest

## Classification

- Promoted proof-only result after hostile audit and independent
  statement-only reconstruction.
- No computation.
- No finite witness claim.
- No all-input source or factoring claim.

## Main candidate

`STATEMENT.md` states two compatible factor-first decoders.

1. One \(\Lambda_B\) screen plus exact order reduction gives a factor,
   common absolute order, or an absolute large-primary certificate. The
   surviving F161 scan strengthens the last outcome to a simultaneous
   absolute- and relative-order certificate.
2. Capped BFS of the complete generated quotient-fingerprint group gives a
   factor, exact small quotient closure and an F166 common-order lift, or a
   common local-capacity lower bound.

`PROOF.md` proves the candidate from local cyclicity, factor-first gcd
comparisons, and the exact kernel of the local \(M\)-power map.

`SELF_AUDIT.md` records the current internal audit and the required attacks
for an independent review.

## Frozen candidate hashes

- `STATEMENT.md`:
  `e96e12303520b40c459b92ab192de48f7ffc4829daa20c60686007aba8884aad`
- `PROOF.md`:
  `8e639c631355951a1c9656fbf99df46320a4c75bf4ef745949f01705b4df6060`
- `SELF_AUDIT.md`:
  `a7a65c9306a3efdcd64f82b26353f78285e0d8aba82140261cb9d5f926af965f`
- `HOSTILE_AUDIT.md`:
  `6c60b057761dc6e521731a37ef7a9038a2b9de8b1552dcecbdaf6154bd89ca93`
- `BLIND_RECONSTRUCTION.md`:
  `0a74b6b6a59810b128282012a2f606065df8d80d10d5563ca0f0d9d7d2678e7d`

## Closest promoted or audited interfaces

- P87: punctured-lcm order mismatch decoder.
- P92/P93: capped enumeration after subgroup powering.
- P148/F161: factor-first bounded relative-order updater.
- F164: quotient-fingerprint capacity and rank accounting.
- P150/F166: common-order construction without hidden-log alignment.
- P98: related stable powered-capacity obstruction, used only as context.

## Evidence boundary

Both independent reviews passed. The blind reconstruction notes one harmless
redundancy: once the stored fingerprint table has maintained every pairwise
gcd invariant, comparing an exact duplicate against all older values cannot
expose a new factor. The stated scan remains correct and QP.

The result is a conditional decoder and state updater. It does not construct
a useful released block or force the quotient group to close below the cap.
