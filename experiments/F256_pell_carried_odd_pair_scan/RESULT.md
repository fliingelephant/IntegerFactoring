# F256 result — carried odd-multiple Pell pair scan

## Outcome

The frozen run completed normally and produced a `null finite signal` for
the fixed pair grammar.

Across 1,024 balanced semiprimes, the scan tested 2,311,478 carried pairs of
distinct retained rows.  Of these pairs, 923,599 (39.957075084%) had
`d=gcd(A,A')>1`.  No pair made either coprime quotient `A/d` or `A'/d` an
exact square.  Therefore:

- exact square dependencies: `0`;
- global normalized-root classes: `0`;
- non-global normalized-root classes: `0`;
- decoder factors from this pair family: `0`.

The absence of root classes is vacuous: the scan found no exact square pair
whose normalized root could be classified.

## Exact split totals

| split | inputs | carried pairs | `d=1` | `d>1` | either quotient square | dependencies | non-global |
|---|---:|---:|---:|---:|---:|---:|---:|
| training | 512 | 879,914 | 529,131 | 350,783 | 0 | 0 | 0 |
| held-out | 512 | 1,431,564 | 858,748 | 572,816 | 0 | 0 | 0 |
| total | 1,024 | 2,311,478 | 1,387,879 | 923,599 | 0 | 0 | 0 |

There were 2,311,481 admissible retained pairs.  Three training pairs had
zero carry and were excluded exactly as preregistered.  Every held-out
admissible pair was carried.

The public cleanup exposed an earlier factor on 289 training inputs and 3
held-out inputs.  The held-out counts by bit length were one input each at
36, 40, and 44 bits, and zero at 48 bits.  Since the pair family produced no
dependency on any input, cleanup status does not change its null outcome.

## Exact algebraic conclusion

For every admitted pair, the root-unit screen makes `gcd(A,N)=1`.  The carry
identity

`A*G^2-A'=N*H`

then proves

`gcd(A,A')=gcd(A,H)`.

If `d` is this gcd, the coprime-valuation argument proves

`A*A' is a square` if and only if both `A/d` and `A'/d` are squares.

This gives a cheap exact public screen.  It discards 60.042924916% of the
carried pairs immediately through `d=1`, because retained individual rows
are nonsquares.  The scan shows that a nontrivial shared gcd was common in
this cohort, but it never completed the much stronger two-square condition.

The proof and normalized-root formula are in `ALGEBRA.md`.

## Scope

This is finite evidence for the fixed menus

`D={2,3,5,6,7,10,11,13}`, `h={3,5,7,9}`, and `1<=j,hj<=12n`.

It does not exclude larger odd multipliers, longer windows, other Pell
discriminants, pairs not related by an odd multiple, or dependencies with
three or more rows.  It also does not prove that carried two-row
dependencies are asymptotically rare.  In particular, the result cannot be
promoted to an impossibility theorem.

