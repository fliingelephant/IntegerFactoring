# F139 preregistration — corrected selected canonical multi-pivot certificate

## Purpose

Verify one fixed certificate for the exact failure statement:

> Packing two degree-one rows from different owners in one frozen selected
> ledger, then preserving both rows in every nonzero anchored digit, need not
> create a binary dependency.

This is a selected-source certificate. It does not assert that the two rows
are degree one in the complete F26-Q ledger or in the complete canonical
universe. It does not test the complete F26-Q source at the registered input.
It makes no statistical or factoring claim.

## Fixed parameters

```text
N = 989 = 23 * 43
B = 5
old endpoints = (2,495), (16,680)
selected private rows = 11,17
packed q = 187
packed inverse w = 238
integer anchors = 1,2,3,4,5
expected digits = 0,0,1,2,3
expected anchored endpoints =
  (187,238), (374,119), (561,409), (748,554), (935,641)
expected distinct anchor values = 44506,229449,414392,599335
```

## Required checks

1. `23` and `43` are proof-certified primes and `N=23*43`.
2. Every displayed endpoint is in `1..N-1`, is a unit, and is the canonical
   inverse of its partner.
3. The packed base and every integer-anchor presentation have both endpoint
   sign gcds equal to one.
4. Every integer `1 <= ell <= B` is eligible. The digits are exactly
   `0,0,1,2,3`.
5. The old carries are `1,11`; the packed carry is `45`; and the anchored
   carries are `45,45,232,419,606`.
6. `B*q < N`, and `q*w=1+45*N`.
7. The two zero-digit presentations have the same exact value. The four
   retained anchor values are pairwise distinct and are distinct from the two
   selected old values.
8. All six retained exact values have the exact factorizations shown in
   `STATEMENT.md`.
9. Rows `11` and `17` have degree one with different owners in the frozen
   two-column selected old ledger. Every nonzero-digit column contains both
   rows oddly.
10. The retained parity matrix on its full prime-row support has six columns,
    rank six, nullity zero, and the declared peeling witness
    `(7,V0), (3,V1), (277,V2), (641,V3), (11,old_2), (17,old_16)`.

## Execution contract

- Verifier: `verify.sage`.
- Authoritative output: `OUTPUT.json`.
- Proof mode: Sage proof arithmetic is enabled.
- Required result: the final status is `PASS` and every named Boolean check
  is true.
- The unregistered exploratory searches are not evidence and support no
  frequency claim.
- The preserved `N=667` run is invalid for this purpose because its packed
  plus screen factors that input.
- No durable project ledger is part of this experiment.
