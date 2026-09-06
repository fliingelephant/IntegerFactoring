# F193 V3 provenance

## Preserved prior versions

V1 and V2 remain frozen unchanged.

V1's hostile audit failed on a mathematical error: the principal character
modulo `N` has conductor one but value zero at `N`. V2 repaired this by
stating rank at most one and conditioning recovery on a nonzero row.

V2's hostile re-audit found all four substantive claims correct. It failed
the frozen text only because both copies of equation (4.2) omitted the
backslash in `\operatorname{Nm}`. The V2 hostile re-audit has SHA-256
`e3968dd1cf643cbff71bd62a74b21d75da1d087ff1fc845a24f30810ff532cf8`.

## V3 change

V3 repairs those two TeX occurrences. It also updates version labels and
normalizes the two beta symbols in one displayed modular-symbol boundary.
There is no mathematical change from V2.

No mathematical computation was run. No durable ledger was edited.
