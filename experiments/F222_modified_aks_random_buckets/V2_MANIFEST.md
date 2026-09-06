# F222 V2 audit manifest

## Authoritative theorem packet

- `V2_STATEMENT.md`:
  `586d2edd549a8c580aa9d66c9dd2cee7866ee4f0d74ed0956bc3f07772ad6cd9`
- `V2_PROOF.md`:
  `e098bb138dd033537436cdc64ed8a46e67b80ba4ae1e0c489c48a8d0c71ff4c1`
- `V2_SELF_AUDIT.md`:
  `f7a5b3a852c7e8843fa4727e925f3bdb628d8e3e417ff291d8650a0f2f0dbeb1`
- `V2_RESULT.md`:
  `5704609d26498ad842fbf82ef2f04f1faf001720b7c5a001d5fb38c479c5b032`
- `V2_PROVENANCE.md`:
  `cfcb1945ece5b0e72af261bcd4b6f15be27ba1d8294cf22578046e77eda17510`

The original F222 files are preserved and are not authoritative for V2.

## Required hostile checks

1. Reconstruct the two local Frobenius identities from the homogeneous error.
2. Check every index and binomial coefficient in the `p`-local expansion.
3. Test separately the cases `p=1 mod r` and `p!=1 mod r`.
4. Verify that every `q`-local cyclic coefficient polynomial is nonzero.
5. Reconstruct `(X+a)J=1-(-a)^r` in the cyclic quotient.
6. Check the degree `d(r+1)-1` and that the exceptional roots are counted
   once globally.
7. Check the contradiction proving every cleared numerator is nonzero.
8. Check that a proper coefficient gcd is contained in the local-zero union.
9. Recheck the weakened nullity premise `r<d<p-1`.
10. Verify Baker--Harman--Pintz Theorem 1 from the primary source and the
    construction at `x=p+floor(p^(3/5))`.
11. Recompute the numerical-QP-to-`2^(-Omega(n))` conversion.
12. Reject any accidental extension to biased shifts or same-shift adaptive
    moduli.

## Blind reconstruction input

A strict blind reconstruction should receive only `V2_STATEMENT.md`, plus
the bibliographic identity of Baker--Harman--Pintz Theorem 1.  It must not
receive `V2_PROOF.md`, the self-audit, or F222-D01 before completing its own
proof or reporting failure.

## Finite run

F222-D01 is not used in the proof.  As a post hoc consistency check, all 143
frozen D01 rows satisfying `r<d<p-1` obeyed (S4); this observation is finite
and nonauthoritative.

## Promotion gate

Do not promote without a fresh hostile audit and a fresh strict blind
reconstruction of the exact hashes above.

