# F250 run manifest

## Frozen inputs

- `PREREGISTRATION.md`:
  `6da9f635db9890b7eb5552965a7dc82ad4e1196f7c53dabce61fc06222d60364`
- `scan.py`:
  `dde3bfa5075b1cfa92389bfb30b11d4d2faace2b865ba5352d7872ea0d5b4948`
- `remote_run.sh`:
  `7c1ad7ca11f015e19e83c22e7337ee9858162cddbd16f0d9ecde66029e45d3fd`

## Copied remote outputs

- `output/TRAIN.jsonl`:
  `7c8186d607b81beb7a27ffba1c9122063264b73df95c4810de22971b00e1dca8`
- `output/HELDOUT.jsonl`:
  `f66e01c84b602392ae0146136aaf50b386ff76a5767cef8f0c6d1313be8d7a9c`
- `output/SUMMARY.json`:
  `cf2c046af7d99e21fbd84e20a079c678d1bba7c5b8b77936c764576a1803e833`
- `output/RUN.stdout`:
  `9185a5e4c35512a4c3856be09c5f1481b07342668705e712d6c634480c75476d`
- `output/RUN.stderr`:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `output/WALL_SECONDS.txt`:
  `151797cae5e8e5798aca2def54dcd44f0dfd5213c2f2a05e21483b12d57399be`
- `output/REMOTE_SHA256SUMS`:
  `deef90abe3d41d7ea782ccbdceba2b33d5ea11c79593e50abf516dcbf592626f`

The local hashes match the remote checksum file. The run produced 64 lines
in each JSONL split, an empty stderr file, and exit-success artifacts from
the frozen runner.

## Review

- `HOSTILE_AUDIT.md`:
  `caafd80c82a5c445c98decb96f9ab5334d003fc556fdf5556e8cb8a11b3e98db`

The run is finite evidence only. It supports no asymptotic probability or
runtime claim.
