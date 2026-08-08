# Preserved failed runs

## F01 — Sage pre-parser changed binary XOR assignment

The first named run used the declared source, runner, and hard 180-second
timeout. It factored all 9,414 relation values, then exited 1 before any rank
claim. Sage translated Python-style `value ^= prior` in the `.sage` source to
exponentiation assignment. The exact failure was:

```text
OverflowError: exponent must be at most 9223372036854775807
```

The source correction converts signatures to Python `int` and calls
`value.__xor__(prior)` explicitly. The failed run supports no claim. Its
original `RUN.log` was inspected before the next named run overwrote it.

## F02 — JSON key serialization failure

The corrected XOR run completed factorization, peeling, rank computation,
and all assertions. It then exited 1 while serializing Sage integers used as
histogram keys:

```text
TypeError: keys must be str, int, float, bool or None,
not sage.rings.integer.Integer
```

The source correction converts every histogram key and value to Python
`int`. The failed run supports no claim. Its original `RUN.log` was inspected
before the next named run overwrote it.
