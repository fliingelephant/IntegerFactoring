# F121 registered source correction 1

Registered before the second computation run.

## Trigger

The first registered run failed only
`c110_terminal_gcds_are_proper`. Its output and log remain under the
timestamped `FAILED_` names recorded in `FAILED_RUNS.md`.

## Diagnosis

For exact square column `P=12100`, ROOT recovers `r=sqrt(P)=110` and tests
`gcd(r-1,N)` and `gcd(r+1,N)`. The first source revision instead tested the
unrelated pair screens `gcd(c-w,N)` and `gcd(c+w,N)` at `(c,w)=(110,110)`.

## Fixed change

Only the declared witness calculation and its reported root fields change:

- compute `r = isqrt(P)`;
- compute terminal gcds from `r-1` and `r+1`;
- report `r` as the recovered root.

The source construction, exact deduplication, feedback grammar, parity
matrices, kernels, and registered checks remain unchanged.

## Source pins

- Failed first-run source SHA-256:
  `51465b6e1556a4cdf081f0e361fd5dbff8d5bea46ce881bf49956889733bd71d`
- Corrected second-run source SHA-256:
  `a900bc225ed63620ca9859f685db9a7fac4bd16f3233d7d35563106826b364da`
- Runner SHA-256:
  `c0201bb0f5dc50bb4269c12f5f27eab46fb11ee122fd6338094435489a32a4b6`
- Timeout: 120 seconds.

The original `PREREGISTRATION.md` and `PRE_RUN_PINS.md` are immutable records
of the first run. This file is the pre-run registration for the correction.
