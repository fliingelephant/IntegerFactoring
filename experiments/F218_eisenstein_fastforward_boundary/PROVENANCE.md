# F218 provenance

The family was opened after the user explicitly asked for remote numerics
on the core beta-two branch.  The closest prior routes were retrieved from
the local durable ledgers and the frozen F203, F204, F206, F208, F215, and
F217 packets.  No public web search or external mathematical source was
used.

The new mechanisms checked here are:

1. prime-power-local exponent reduction rather than a dense moving-weight
   representation;
2. first-order eta Frobenius lifting at every index;
3. the multiplicative index invariant of standard big-Witt
   Frobenius/Verschiebung; and
4. a moving theta power whose full coefficient compresses under
   characteristic-`r` Frobenius.

The proof shows that the first two are the same depleted divisor target,
the third cannot express the affine shift `2K+1`, and the fourth has a
nonzero cusp contaminant already at `K=17`.  A further first-principles
argument uses prime powers in the progression `rj+1` to prove that its
divisor-sum Cartier section is not eventually periodic and has no fixed
linear recurrence.

The deterministic remote search was preregistered before execution.  Its
first launch failed before the source started because the remote image did
not contain `/usr/bin/time`.  That run is preserved verbatim.  No altered
runner has been used without the explicit workflow approval required by
the repository instructions.
