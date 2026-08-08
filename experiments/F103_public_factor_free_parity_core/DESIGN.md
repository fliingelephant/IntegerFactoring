# F103 — public factor-free parity-core replay

## Question

Can the lossless degree-one peeling from F102 be applied to the actual
factor-free P66 matrix, rather than to a diagnostic prime-factor matrix?

## Public source

The executable receives only (N). It replays the exact F98 round-one rule:
trial division through (n^2), seeds 2 through (n), public gcd-free endpoint
refinement, the first (n) active block pairs, and both bounded trajectories.
It imports only the pinned arithmetic primitives from the audited F98 public
source.

After exact-value deduplication, it constructs the P66 pairwise-coprime
factor-free parity rows. It repeatedly removes a column forced to zero by a
degree-one row. It reports the remaining core, rank, nullity, components,
provenance, and whether the public useful kernel vector is inside the core.

## Falsifiers

The candidate fails if any F98 count or factor differs, if peeling changes
nullity, if different degree-one removal orders give different cores, or if
the useful 166-value certificate is not contained in the public core.

## Scope

This is one fixed-input public replay. Even if it passes, it gives no
all-input core-existence law and no useful-root probability law.
