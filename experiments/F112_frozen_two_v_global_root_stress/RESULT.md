# F112 — the frozen `(2,v)` source fails at 46 and 50 bits

**Status:** completed factor-assisted counterexample scan.  The proposed
all-corpus claim failed.

The corpus contains all 100 distinct completed F104 cases whose first frozen
round has a nonzero kernel but whose complete reported basis has only the
global root `+1`.

The frozen first layer plus the fixed `(2,v)` menu factors 86 inputs:

- 67 by a parity dependency that uses relations from both layers;
- 19 by a direct endpoint gcd.

It fails on all 14 larger inputs:

- all seven 46-bit inputs near \(5\times10^{13}\);
- all seven 50-bit inputs near \(8\times10^{14}\).

It succeeds on every tested input from 32 through 42 bits.  This sharp finite
cutoff is not an asymptotic theorem, but it defeats the exact proposed source.
The null runs still have many new dependencies.  For example, the 46-bit
cases finish with 22,381 to 31,155 dependencies.  Relation volume and nullity
therefore do not repair the missing non-global root.

The six original F109/F110 parity rescues remain valid finite cross-layer
witnesses.  What fails is their extrapolation to the fixed one-parameter
`(2,v)` sampler.  A materially new retry must broaden the public menu or prove
a different source law.
