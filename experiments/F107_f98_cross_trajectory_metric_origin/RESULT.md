# F107 — the F98 cross-trajectory circuit is mostly a metric integer effect

**Status:** candidate factor-assisted diagnosis of one fixed circuit. It
requires hostile audit and proof-blind reconstruction before promotion.

The 166-column circuit has 230 prime-parity rows and rank 165. Of its rows,
175 span more than one oriented trajectory. These cross-trajectory rows have
rank 163 and connect all 166 columns.

Only five primes have a cross-trajectory pair explained by an exact shared
public base divisible by that prime:

```text
2, 3, 5, 11, 17
```

They give five rows and rank five. No cross-trajectory row is explained only
by such base inheritance. Across the trajectory-key pairs induced by the
rows, 15 pairs are base-inherited and 724 are not.

Call the latter pair a metric overlap. This means only that the prime is not
in a shared divisible base. It does not mean that the overlap is random.
Every cross-trajectory row has at least one metric pair. Those 175 rows again
have rank 163 and connect the complete circuit. After removing all five rows
that have any base-inherited pair, the remaining 170 rows have rank 158 and
connect 164 of the 166 columns.

The conclusion remains strong after removing local zero-carry rows. The 151
metric cross rows with no carry-chain explanation have rank 143. The stricter
150-row set with neither a carry chain nor any base-inherited pair has rank
142 and a largest connected component of 146 columns.

There are 84 metric cross primes above the public bound \(n^2=784\). The
largest is 2,814,499.

## Meaning and limit

The useful F98 circuit is not primarily a formal consequence of reusing the
same public bases. Canonical integer representatives from different
trajectories acquire many shared factors that are absent from their shared
base data. This is the metric presentation effect that the feedback route
needs.

This is one 28-bit diagnosis. It gives no lower bound on the frequency of
these overlaps at larger sizes. Ordinary shared-factor collisions can be
dense at this size. The result therefore identifies the live source question
but does not answer it and does not give an all-input factoring algorithm.
