# F110 — a frozen nonadaptive source reproduces all seven rescues

**Status:** completed factor-assisted candidate.  No claim is promoted.  It
requires hostile audit and a separate factor-free replay.

The complete frozen first layer has between 14,351 and 23,703 retained
relations on the seven inputs.  It has thousands of dependencies on every
input, but every dependency found by the online decoder has a global root.
It does not factor any input.

After that layer is frozen, the source appends a lexicographic menu of small
integer pairs.  All seven runs factor before the menu leaves the prefix

```text
(2,3), (2,4), ..., (2,n).
```

Thus the executed traces define a smaller predetermined source: use only
`(2,v)`, `3 <= v <= n`, after the frozen layer.  It would produce the same
seven traces because no run reaches a pair with first member larger than 2.
It contains `O(n)` pairs and `O(n^2)` states per pair.  Together with the
`O(n)` frozen seed-basis trajectories, this narrowed source has `O(n^3)`
residue attempts.  The stored executable declares the larger `O(n^4)`
all-pairs menu but stops inside this common prefix on every fixed input.

| N | first successful appended pair | channel | dependency split |
|---:|---:|---|---|
| 3,241,632,473 | `(2,4)` | parity | 327 frozen + 36 appended |
| 12,809,029,193 | `(2,9)` | parity | 372 frozen + 2 seed + 148 appended |
| 12,828,426,053 | `(2,7)` | parity | 455 frozen + 69 appended |
| 12,854,972,153 | `(2,4)` | parity | 450 frozen + 1 seed + 43 appended |
| 12,859,936,021 | `(2,4)` | parity | 611 frozen + 28 appended |
| 12,862,140,737 | `(2,5)` | parity | 384 frozen + 31 appended |
| 204,816,942,773 | `(2,13)` | direct endpoint gcd | not applicable |

The six parity witnesses use between 8 and 14 distinct nonseed trajectory
keys.  Each witness contains relations from both layers.  The gain is
therefore an amortized cross-trajectory effect.  It is not an isolated scalar
identity followed by one gcd.

This control removes recursive feedback and feedback-created blocks from the
seven witnesses.  The first layer depends only on the initial seed endpoint
batch.  The appended menu is fixed independently of all generated relations.

The computation still factors endpoint values to accelerate its parity
decoder.  P106 gives a factor-free polynomial decoder for an explicit frozen
batch, but a separate N-only replay must verify these exact witnesses.  The
result is finite.  It supplies neither an all-input source theorem nor a
success-density bound.
