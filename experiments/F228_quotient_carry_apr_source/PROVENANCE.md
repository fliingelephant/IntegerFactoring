# F228 provenance

## Closest prior routes

- P185/F210: dyadic quotient siblings are locally half-translated; their
  balanced integer point is the unresolved selector.
- F220: factored annihilators can certify common primary blocks and combine
  their lcm with beta-two residue information.
- F226: random remainder-prefix banks are exact-uniform and recursion-safe,
  but their complete child ensemble is independent of `N`; multiplier labels
  and Euclidean quotients were explicitly excluded.
- F227: diffuse factor-cell exponents followed by fresh uniform bases have
  exponentially sparse return probability.

F228 differs by retaining the Euclidean quotient/carry label
`uN=Q_uB+R_u` and recursively factoring `Q_u+c`.

## Development history

The first algebraic check produced the direct identity

\[
\gcd(Q_u,N)=\gcd(R_u,N).
\]

Reducing the shifted identity modulo divisors of `N-1` then gave the stronger
common-primary collapse (6)--(8).  The APR side did not collapse; it gave the
inverse-lift characterization (10)--(14).  A separate random-shift count
gave the harmonic tail theorem.

The user explicitly encouraged remote numerical exploration.  The remote
host was inspected before scaling.  It had 128 logical CPUs, about 367 GiB
available memory, and `/usr/bin/timeout` plus `/usr/bin/g++`, but no Python,
Sage, or Boost headers.  Runs were single-threaded and completed below two
seconds each after compilation.

## Workflow incident

The first source draft used Boost multiprecision.  A dependency preflight
found Boost absent before launch, so the implementation was revised before
data collection to use exact threshold saturation and a local decimal
formatter.  The mathematical menu did not change.

A later local compile check accidentally chained into a full un-timed
execution.  It is preserved as D00 and was disclosed immediately.  The
already-preregistered remote D01 was then run unchanged.  Its deterministic
output matched the accidental output byte for byte, but only the remote D01
is cited as the declared run.

D02 used a fixed divisor cap and its preregistered interpretation overstated
what a zero capped row meant.  The frozen D02 files were not changed.  D03
was preregistered to separate the no-cap source predicate from cap pressure.
It showed that every D02 zero row was a cap artifact.

## Ledger policy

No durable `PROVED.md`, `FAILED.md`, `REGISTRY.md`, `STATEMENT.md`, or
`notes/Progress.md` file was edited by this subagent.  The packet remains a
self-audited candidate until the required fresh hostile audit and blind
reconstruction run.
