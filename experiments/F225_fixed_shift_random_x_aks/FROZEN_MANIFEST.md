# F225 frozen manifest

## Candidate hashes

- `STATEMENT.md`:
  `57a0764b549a79a5a725612b95a6f57b41791760bc6a1a2d188354041d6b1a20`
- `PROOF.md`:
  `b6f9feb7d2dfe9cb9a0829e750defdd1a2a1025c7c42523671b4a6a6ea35c03a`
- `SELF_AUDIT.md`:
  `8da3567fe6671c7f12604d9557e041815908bb5146ba878f037243e0a6c90dd6`
- `RESULT.md`:
  `7ef7c9ee3ecc8620061c75982cc6c3998e5cfb0fe633ceb96e2fdb089fd7c2c8`
- `PROVENANCE.md`:
  `6c49d5cfe74bf0af6aa9c416bfa22d04dfa5f4223cbd693305fcf525c02b5416`

## Required hostile checks

1. Reconstruct both Frobenius collapses without importing F221.
2. Check the exponent identities for `c=2p-q`, including parity.
3. Check that clearing denominators loses only `0,-1` and that both are
   genuine roots.
4. Check the exact degree `2(c-2)` of `P_k`.
5. Check all four quadratic-character cells and the degrees `s,s,s-1,s-1`.
6. Reconstruct both exact CRT XOR probabilities.
7. Verify the BHP interval stays in `(p,2p)` and makes
   `c=Theta(p^(3/5))`.
8. Verify the conversion `O(p^(-2/5))=2^(-Omega(n))` and the numerical-QP
   union bound.
9. Reject any extension to biased points, joint nonzero-value processing,
   or a promised class modulo `4`.
