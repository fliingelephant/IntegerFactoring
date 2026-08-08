# F106 failed runs

## R01 — adjacent selected pairs only

The first completed diagnosis counted only consecutive exponents when both
columns were selected. This can miss a zero-carry chain whose intermediate
columns are outside the 166-column certificate. Its output and log are
preserved as:

```text
OUTPUT_R01_ADJACENT_ONLY.json
RUN_R01_ADJACENT_ONLY.log
```

The arithmetic in R01 is valid for its narrower classification, but it is
not authoritative for the stated carry-origin question. R02 tests every
selected pair in each oriented trajectory for an exact zero-carry chain.
