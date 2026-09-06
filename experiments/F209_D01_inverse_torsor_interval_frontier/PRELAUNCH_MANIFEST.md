# F209-D01 prelaunch manifest

Status: frozen preregistration candidate.  The experiment has not launched.
Root-agent approval is required before remote staging or execution.

Frozen SHA-256 hashes:

- `PREREGISTRATION.md`:
  `09fab369dc9519dfb07c3f73c436e9995e9269696cb9a6bed9d5b446689ddf3d`
- `scripts/F209_D01_inverse_torsor_frontier.py`:
  `61b13495b8455b2697b983668602829053c297a8fc68e08188966ea824634d6a`
- `scripts/run_F209_D01_remote.sh`:
  `00bbe754566d26d9757af39dbb82791ba955f3ac856266a187e79f187221c03e`

Frozen run identity:

- run ID: `F209-D01`;
- SSH alias: `seetacloud`;
- remote root: `/root/IntegerFactoring_F209/F209-D01`;
- timeout: 1,800 seconds;
- concurrency: one Python process;
- address-space limit: 8 GiB;
- datasets: 256 paired F205-prefix train rows, 64 paired F205-prefix
  holdout rows, exhaustive accepted pairs with `p<=1000`, and the four
  frozen pairs in `PREREGISTRATION.md`;
- seeds: `20501` and `20502`;
- strict work proxy: `n^4`;
- maximum odd small-factor representatives: 2,000,000, with abort rather
  than truncation.

The deterministic pair-list hashes are emitted at run start.  Their identity
is already fixed by the frozen source, counts, bit ranges, seeds, and exact
generator inherited from F205-D01.  They are not post-run selection inputs.

No local dry run, remote preflight, remote staging, experiment launch,
output, benchmark, or durable-ledger edit has occurred.
