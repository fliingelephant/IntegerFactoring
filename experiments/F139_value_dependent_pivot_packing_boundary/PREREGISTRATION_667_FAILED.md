# F139 preregistration — selected canonical multi-pivot certificate

## Purpose

Verify one fixed certificate for the exact failure statement:

> Packing two globally private old prime rows into one small canonical word,
> then preserving both rows in every occupied new digit, need not create a
> binary dependency.

This is a selected-source certificate. It does not test the complete F26-Q
source at the registered input. It makes no statistical or factoring claim.

## Fixed parameters

```text
N = 667 = 23 * 29
B = 5
old endpoints = (7,286), (19,316)
packed q = 133
packed inverse w = 331
anchors = 2,3,5
expected digits = 1,2,2
expected anchored endpoints = (266,499), (399,555), (665,333)
expected distinct new values = 132734,221445
```

## Required checks

1. `23` and `29` are proof-certified primes and `N=23*29`.
2. Every displayed endpoint is in `1..N-1`, is a unit, and is the canonical
   inverse of its partner.
3. Every displayed endpoint difference and sum has gcd one with `N`.
4. The old carries are `3,9`; the packed carry is `66`; and the anchored
   carries are `199,332,332`.
5. `B*q < N`, and the anchor digits are exactly `1,2,2`.
6. The two digit-2 presentations have the same exact value.
7. All four retained exact values have the exact factorizations shown in
   `STATEMENT.md`.
8. Rows `7` and `19` are private to different old columns and occur oddly in
   both new columns.
9. The retained parity matrix on its full prime-row support has four columns,
   rank four, nullity zero, and the declared degree-one peeling witness
   `(11, old_7), (79, old_19), (499, digit_1), (5, digit_2)`.

## Execution contract

- Verifier: `verify.sage`.
- Authoritative output: `OUTPUT.json`.
- Proof mode: Sage proof arithmetic is enabled.
- Required result: the final status is `PASS` and every named Boolean check
  is true.
- The earlier exploratory search that selected this fixed example is not
  registered evidence and supports no frequency claim.
- No durable project ledger is part of this experiment.
