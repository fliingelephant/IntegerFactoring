# F243-R2 preregistration — disjoint remote confirmation

## Reason for a new run

F243-R1 was contaminated by a five-input local implementation smoke.  Its
status file preserves that failure.  This run uses a disjoint input set and
is frozen after viewing only the R1 aggregate smoke table.  It does not
change a source, statistic, threshold, or interpretation rule in response to
those values.

## Disjoint input set

For primes in `[2^12,2^14)`, use SHA-256 ranks 20,000 through 39,999 under
the exact ordering in `PREREGISTRATION.md`.  These do not overlap R1's first
20,000 ranks.

For small inputs, use primes in `[512,4096)`.  Sort all distinct pairs by
SHA-256 of

`F243-torus-collision-source-v2 || ":" || p || ":" || q`

and take the first 5,000.  These do not overlap R1's primes below 512.

The full ordered input transcript is the 20,000 large pairs followed by the
5,000 small pairs.  Report its SHA-256 digest.

## Runtime, sources, and outputs

Use the exact C++20 arithmetic, one-process remote resource cap, sources,
statistics, Monte Carlo bucket rule, output schema, and interpretation rules
from `PREREGISTRATION_R1.md`.  The first 100 R2 inputs are the allowed remote
resource pilot.  The pilot may decide only whether the frozen full run fits
the 30-minute and 2-GiB caps.  It may not change the run.

The implementation must self-test SHA-256 and arithmetic identities before
processing inputs.  Do not run R2 locally.
