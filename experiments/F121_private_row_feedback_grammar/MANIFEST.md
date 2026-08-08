# F121 artifact manifest

## Outcome

- General proof: `RESULT.md`.
- Registered finite replay: PASS.
- Named hard timeout: 120 seconds.
- Successful runtime: 0.100752 seconds.
- Preserved failed runs: one.
- Durable project ledgers changed: none.

## SHA-256 pins

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `d54bf8570646e037278a5fcac1b2a46a210b32a1bc6dda213f0ae1d47ccb22ab` |
| `PRE_RUN_PINS.md` | `f3af2e9c9dd8d785f6e958b0c81cf9f34ea0b7f08d621b9a1927b76aaf84701c` |
| `REVISION_1.md` | `f16f7011f580952a95fc00d70d268fbba3eea079c7a64dc980738f71b482f4af` |
| `analyze.py` | `a900bc225ed63620ca9859f685db9a7fac4bd16f3233d7d35563106826b364da` |
| `run_with_timeout.py` | `c0201bb0f5dc50bb4269c12f5f27eab46fb11ee122fd6338094435489a32a4b6` |
| `OUTPUT.json` | `b15dc0338f7f497522fbda4f8ce35c9b232c1b7e0dbfde6f1ddbb2bc3e5578b3` |
| `RUN.log` | `344f02bc14e23a94fc511de50354f6dfbea6ad1b58d69df1dc37f49738d92303` |
| `FAILED_RUNS.md` | `d785773110d22edff05013612ca174a6c5ab7f14e57c0d0c09c5d73dbbd10d8d` |
| `FAILED_20260808T060312.851782Z_OUTPUT.json` | `eea7c71fe1d0bfa10557b38400e0e47da43e9a7d071d285149d0a1288ae7b2c0` |
| `FAILED_20260808T060312.851782Z_RUN.log` | `185e2ab6b11d91e1779e467392ec808bfb1d2b8a9cdc35e6690ed1425026f8ad` |
| `RESULT.md` | `f9722b8b50ea0875e651824cae4c5502e65b5e205f9db9a61121d1f5c36d5225` |

## Failure history

The first registered source run completed without timeout but failed
`c110_terminal_gcds_are_proper`. It had applied endpoint pair screens to
`(c,w)=(110,110)` instead of terminal root screens to
`r=sqrt(12100)=110`. The failed JSON and log remain pinned above.

`REVISION_1.md` registered the reporting-only correction before the second
run. The successful source computes `gcd(r-1,N)` and `gcd(r+1,N)`. It did not
change source generation, deduplication, matrices, feedback candidates, or
kernel elimination.

## Authoritative finite conclusions

The successful output records all of the following:

- row `q=2017` is private in the static, promoted, and complete canonical-unit
  exact-value universes;
- every promoted word passes its inverse-`2` Laurent identity;
- promotion adds 50 residues and zero exact values;
- the static and promoted matrices are identical;
- `CLOSE` and `ROOT` already hold in the static matrix;
- the `P=12100` witness is static and not a feedback witness.
