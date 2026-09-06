# F236 provenance

## Mathematical provenance

P200 identifies the zero-defect identity `N=1+BH` and the hidden residual
orders.  P203 studies shifted quotient children.  P204 permits arbitrary
unfactored QP-bit words but leaves the integer source theorem open.  F236
tests public word families and introduces a different integer-specific
source: centered products of the two hidden factors after a public
multiplier.

The exact centered-carry theorem was derived before its multiplier scans.
The correction from an ordinary trace to a weighted trace is recorded in
the final frozen statement and proof.  No earlier incorrect formula is used.

## Computation provenance

All runs used `ssh seetacloud`, authorized by the user.  Before scaling, the
host reported 503 GiB RAM, 367 GiB available, 22 GiB free disk, 32 visible
CPUs, and high host load near 60.  Each scan used one `nice -n 19` process,
about 35 MB, and no parallel workers.

The complete finite domain and each follow-up menu were frozen in the
corresponding `PREREG*.md` before execution.  The raw outputs preserved from
their first redirected remote run are:

- `output/word_scan.out` from `scan.cpp`;
- `output/multiplier_scaling.out` from `multiplier_scaling_scan.cpp`;
- `output/fixed_center_scaling.out` from `fixed_center_scaling_scan.cpp`;
- `output/first_hit.out` from `first_hit_scan.cpp`;
- `output/gcd_collision.out` from `gcd_collision_scan.cpp`;
- `output/random_hit.out` from `random_hit_scan.cpp`.

The first centered-carry, carry-meta-order, carry/residual-tradeoff, and
`u<=n` multiplier runs printed complete results to the tool transcript but
were not redirected.  On 2026-08-13 they were reproduced from the unchanged
preregistered sources, sequentially and at low priority.  Their frozen raw
reproduction outputs are:

- `output/carry.out` from `carry_scan.cpp`;
- `output/carry_order.out` from `carry_order_scan.cpp`;
- `output/tradeoff.out` from `tradeoff_scan.cpp`;
- `output/multiplier_carry.out` from `multiplier_carry_scan.cpp`.

The reproduced headline values equal those recorded in the original tool
transcript.  No menu or ranking changed.

No SageMath installation was substituted when the remote image lacked
Python.  The declared C++ implementation was used directly.  Numerical
evidence is guidance, not proof.

Exact commands, environment data, compiler version, and output hashes are
recorded in `RUN_LOG.md`.
