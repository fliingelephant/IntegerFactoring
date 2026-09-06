# Pre-freeze failed self-test

The first remote algebra self-test compiled successfully and then terminated
with a core dump before printing a result. No cohort was generated or scored.

Root cause: the triple-source filter checked that the three source indices
were inside the materialized window, but the associativity cocycle also reads
the target at `i+j+k`. A pattern near the boundary therefore indexed beyond
the Pell table owned by that input.

The source was repaired before freeze by requiring `i+j+k<=4*n`. The next
remote compile and self-test passed. This file preserves the workflow defect;
the failed attempt supports no mathematical claim.
