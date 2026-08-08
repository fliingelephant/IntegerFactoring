# F109 — retained relation state rescues six isolated-pair failures

**Status:** completed factor-assisted candidate.  No claim is promoted.  A
hostile audit and a separate factor-free replay are still required.

All seven stable trial-hard inputs have a first-round parity kernel, but every
tested first-round basis root is the global root `+1`.  The full declared C2T
run later factors all seven inputs.

| N | final pair | C2T round | C2T channel | isolated final pair |
|---:|---:|---:|---|---|
| 3,241,632,473 | `(2,13)` | 3 | 378-relation dependency | null: 284/284 dependencies global |
| 12,809,029,193 | `(3,5)` | 3 | 580-relation dependency | null: 210/210 dependencies global |
| 12,828,426,053 | `(2,7)` | 3 | 418-relation dependency | null: 356/356 dependencies global |
| 12,854,972,153 | `(2,7)` | 3 | 523-relation dependency | null: 366/366 dependencies global |
| 12,859,936,021 | `(2,13)` | 2 | 634-relation dependency | null: 312/312 dependencies global |
| 12,862,140,737 | `(2,5)` | 3 | 509-relation dependency | null: 333/333 dependencies global |
| 204,816,942,773 | `(2,13)` | 4 | direct endpoint gcd | direct endpoint gcd |

For the first six inputs, the final pair does not factor the modulus when it
is run from a fresh decoder that contains only the initial seed columns.  It
does factor the same modulus when earlier trajectory relations remain in the
decoder.  Thus the successful dependency uses cross-batch state.  It is not
the product of one final trajectory followed by one gcd.

The experiment does **not** show that a feedback-created block is necessary.
Every final pair consists only of integers already present among the initial
seeds `2..n`.  The next control must test whether one nonadaptive polynomial
batch of small-seed pairs reproduces the same gain.  It must also identify
which earlier and final-batch columns occur in each successful dependency.

Endpoint factorization is used only in this discovery run.  The result is a
finite seven-input mechanism witness.  It gives no all-input theorem and no
frequency bound.
