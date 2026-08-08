# F114 — the broader fixed menu rescues all seven 50-bit nulls

**Status:** completed factor-assisted candidate. It requires hostile audit and
factor-free replay before any fixed witness is promoted.

The fixed `(2,v)` prefix failed on every 50-bit input in this set. Continuing
the same public lexicographic menu across all unordered seed pairs factors all
seven:

| N | first successful pair | dependency support | frozen / appended |
|---:|---:|---:|---:|
| 799,999,779,999,949 | `(4,7)` | 3,696 | 1,653 / 2,043 |
| 800,000,499,996,757 | `(3,50)` | 3,885 | 1,514 / 2,371 |
| 800,000,739,995,221 | `(3,46)` | 3,792 | 1,746 + 1 seed / 2,045 |
| 800,001,099,992,377 | `(3,50)` | 3,740 | 1,617 / 2,123 |
| 800,002,819,971,857 | `(4,7)` | 3,927 | 1,692 / 2,235 |
| 800,003,059,967,681 | `(3,50)` | 3,968 | 1,826 + 1 seed / 2,141 |
| 800,005,299,946,297 | `(3,49)` | 3,870 | 1,772 / 2,098 |

Every success is a retained parity dependency. Each exact witness crosses the
frozen/appended layer boundary and uses 75 to 92 distinct nonseed trajectory
keys. Thus the factor does not come from one selected residue or one final
trajectory.

Together, F113 and F114 show that F112's 14 failures are narrow-menu failures
on this corpus. They do not show that all seed pairs suffice on every input.
This computation factors endpoint values, so an N-only replay is still
required.
