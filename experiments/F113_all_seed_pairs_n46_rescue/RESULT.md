# F113 — the broader fixed menu rescues all seven 46-bit nulls

**Status:** completed factor-assisted candidate.  It requires hostile audit
and factor-free replay before any fixed witness is promoted.

The full `(2,v)` prefix failed on every 46-bit input.  Continuing the same
fixed lexicographic menu to first member 3 factors all seven:

| N | first successful pair | dependency support | frozen / appended |
|---:|---:|---:|---:|
| 50,000,764,992,341 | `(3,19)` | 2,265 | 1,013 / 1,252 |
| 50,001,624,955,573 | `(3,20)` | 2,288 | 969 / 1,319 |
| 50,001,724,887,113 | `(3,20)` | 2,444 | 999 / 1,445 |
| 50,002,154,865,017 | `(3,19)` | 2,492 | 1,390 / 1,102 |
| 50,002,584,754,033 | `(3,20)` | 2,405 | 1,213 / 1,192 |
| 50,002,694,807,489 | `(3,20)` | 2,571 | 1,346 + 1 seed / 1,224 |
| 50,002,744,708,409 | `(3,17)` | 2,240 | 1,209 / 1,031 |

Every success is a parity dependency.  Each exact witness crosses the layer
boundary and uses 54 to 62 distinct nonseed trajectory keys.  The factor does
not come from one selected residue or one final trajectory.

This proves only that F112's 46-bit failures were narrow-menu failures.  It
does not show that all seed pairs suffice on every input.  The computation
factors endpoint values, so a factor-free fixed replay is still required.
