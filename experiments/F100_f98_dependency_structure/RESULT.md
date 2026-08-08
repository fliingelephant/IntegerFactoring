# F100 — the F98 certificate is one connected cross-trajectory circuit

**Status:** factor-assisted finite diagnosis. This is not an unbounded
theorem or a factoring algorithm.

The 166 distinct relation values in the F98 public certificate form a binary
matroid circuit. Their prime-valuation parity matrix has rank 165 and nullity
one. Hence the displayed all-column dependency is the unique nonzero
dependency on this selected set, and every proper subset is independent.

The circuit is not a pair or a simple ordinary graph cycle. Its
prime-valuation parity matrix has 230 rows, including the row for prime 2.
Relation columns contain between 3 and 11 parity-prime rows. Prime-row
degrees range from 2 to 80:

- 167 of 230 rows have degree two;
- 31 have degree four;
- the remaining 32 have even degree from six through eighty.

The shared-parity-prime support graph is connected on all 166 relation
values. It remains connected if the prime-2 row is removed. The certificate
uses one initial seed relation and 165 feedback relations from five
active-pair families spanning eight oriented trajectories:

```text
(11, 36824929): 15
(13, 124638221): 10
(2, 5):          54
(2, 17):         53
(3, 17):         33
```

Thus the useful F98 event is genuinely cross-trajectory and amortized. It is
not a duplicate-value direction and not one local pair or triple. It is also
not evidence of an all-input law. The high incidence of small primes and the
many degree-two rows are compatible with a finite smoothness/shared-factor
phenomenon. The computation does not prove that such a circuit occurs with
inverse-polynomial probability as the input length grows.

The exact root again gives

\[
R\equiv132{,}013{,}085\pmod N,
\qquad
(\gcd(R-1,N),\gcd(R+1,N))=(19{,}727,10{,}267).
\]

The diagnosis factors the 166 relation values with Sage. It is not part of
the public F98 algorithm.
