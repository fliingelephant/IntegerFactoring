# F210-D01 prelaunch manifest

Status: frozen preregistration candidate. The experiment has not launched.
Root-agent review and durable registration are required before remote staging
or execution.

## Frozen hashes

- `PREREGISTRATION.md`:
  `e1c1537ba752ba4bf44eb23d5dcaabdb25b51270addcdc25a296c730443a2349`
- `scripts/F210_D01_dyadic_quotient_selector.py`:
  `32d0b4f8ad5141433e7f6d547242620df421f53702ade39d27587ba2079e5648`
- `scripts/run_F210_D01_remote.sh`:
  `b35c5b9200784ba0ff9f2029dd2c3d55ec5e7b27e025e57b05d63889bf9d223c`

The runner contains the frozen source hash and aborts on a mismatch.

## Frozen run identity

- Run ID: `F210-D01`.
- SSH alias: `seetacloud`.
- Remote root: `/root/IntegerFactoring_F210/F210-D01`.
- Timeout: 1,800 seconds.
- Concurrency: one Python process and no workers.
- Address-space cap: 8 GiB.
- Training: 2,000 accepted F205-generator prefix pairs, factor bits 12--17,
  seed `20501`.
- Holdout: 1,000 accepted F205-generator prefix pairs, factor bits 18--23,
  seed `20502`.
- Exhaustive-small: every accepted pair with `p<=500`.
- Dyadic stages: `1 <= t < (N.bit_length()-1)//4`.
- Safe cutoff: `t >= ceil(N.bit_length()/8)`.

The ordered pair-list hashes are emitted before child construction. Their
values are fixed by the frozen source, counts, ranges, seeds, and generator.
They are not post-run selection inputs.

## Expected remote resources

The frozen estimate is 4--12 minutes, below 2 GiB peak memory, below 150 MiB
compressed output, and below 1 GiB total working data. The runner aborts
when one-minute load exceeds twice the CPU count, available memory is below
16 GiB, or free disk is below 5 GiB.

## Validation performed

Only read-only static validation was performed:

- Python source parsed successfully with the local standard-library AST
  parser.
- The runner passed `bash -n`.
- The three hashes above were recomputed after the static checks.

No experiment code path, pair generator, factorization, action bank, local
dry run, remote preflight, remote staging, benchmark, or remote launch has
run. No durable ledger was edited.
