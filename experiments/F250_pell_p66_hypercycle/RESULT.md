# F250 result — canonical Pell/P66 hypercycle scan

## Status

The preregistered remote run completed successfully. The result is finite
discovery evidence only. It is not an asymptotic obstruction and it is not a
factoring algorithm.

## Frozen run

- Cohort: 64 training inputs at 20, 24, 28, and 32 bits; 64 held-out inputs
  at 36, 40, 44, and 48 bits.
- Source: the eight fixed nonsquare discriminants
  `2, 3, 5, 6, 7, 10, 11, 13`.
- Window: Pell powers through `4n` for each discriminant.
- Decoder banks: one bank for each discriminant and one combined bank, for
  nine banks per input and 1,152 banks in total.
- Remote runtime: 335 seconds with one low-priority Python process. The
  recorded peak resident-set value was 20,232 platform units on Linux
  (approximately 20 MiB).

## Result

Every one of the 1,152 factor-free parity matrices had full column rank.
Thus every decoded kernel was zero-dimensional. No bank produced a
non-global square root.

The training split had 21 inputs with an earlier directly verified cleanup
factor. It had no decoder hit after cleanup. The held-out split had:

- zero earlier cleanup factors;
- zero decoder hits;
- zero strict screen-free hits;
- zero tangent events.

The preregistered interpretation is therefore `null finite signal`.

This rules out only the tested finite schedule. It does not prove that a
larger Pell window, another discriminant family, or a general multirow P66
decoder has exponentially small success probability.

## Integrity and audit

The copied local outputs match every checksum written by the remote runner.
The hostile audit independently reconstructed all 128 deterministic cohort
members and checked every stored bank invariant. It returned PASS for the
exact algebra and finite interpretation.

The audit recorded two nonoperative protocol qualifications. The source
scanned unordered tangent pairs although the preregistration said ordered
pairs, and the output omitted some requested per-discriminant cleanup
counters. No tangent event occurred, and these omissions do not alter the
stored nullity or factor results.

Hostile-audit SHA-256:
`caafd80c82a5c445c98decb96f9ab5334d003fc556fdf5556e8cb8a11b3e98db`.
