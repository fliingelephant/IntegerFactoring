# Run manifest

Scope: proof-blind reconstruction from only `N=79403`, `r=269`, `a=1`, `P=X^269-1`, the stated `H`, and the stated coefficient-map determinant convention. Canonical result/progress files and `experiments/F04_psckill`, `experiments/F04_psc_audit` were excluded. All paths below are relative to this directory.

## Sources

- `global_discovery.sage`: factor-blind cyclic computation of `H`; exact-integer determinant scan with increasing `j` and no preselected witness.
- `local_certificate.sage`: independently recomputes both finite-field quotients after taking the factor from R01's gcd; checks every determinant reduction.
- `verify_outputs.py`: asserts dimensions, exact determinant reductions, gcds, local degrees/residues, CRT, formal padding, and raw coefficient separator.
- `run_with_timeout.py`: process-group timeout runner; records command, UTC times, duration, exit code, timeout flag, disposition, and log SHA-256.
- `probe_exact.sage` and its generated `probe_exact.sage.py`: a non-authoritative, preselected-`j=47` development probe, restored for provenance only.

## Recorded runs

| Run | Command | Hard timeout | Duration | Exit | Timeout | Disposition | Log | Output/status |
|---|---|---:|---:|---:|---|---|---|---|
| R01_global | `sage global_discovery.sage output/R01_global.json` | 900 s | 66.404 s | 0 | no | completed | `logs/R01_global.log` | `output/R01_global.json`, `output/R01_global_status.json` |
| R02_local | `sage local_certificate.sage output/R01_global.json output/R02_local.json` | 600 s | 3.977 s | 0 | no | completed | `logs/R02_local.log` | `output/R02_local.json`, `output/R02_local_status.json` |
| R03_verify | `python3 verify_outputs.py output/R01_global.json output/R02_local.json output/R03_verify.json` | 60 s | 0.044 s | 0 | no | completed | `logs/R03_verify.log` | `output/R03_verify.json`, `output/R03_verify_status.json` |
| P04_probe_replay | `sage probe_exact.sage 47` | 60 s | 3.039 s | 0 | no | completed, non-authoritative provenance replay | `logs/P04_probe_replay.log` | `output/P04_probe_replay.json`, `output/P04_probe_replay_status.json` |

Failure disposition: none of authoritative R01-R03 failed or timed out. Before those runs, `probe_exact.sage` was executed several times without durable run records: once Sage failed before execution because its default `~/.sage` cache was unwritable; once the determinant completed but JSON serialization failed on a Sage `Integer`; and corrected probe invocations then completed. The probe source and generated preparse were subsequently deleted during cleanup. That deletion and the absence of durable logs/status files for those executions is a **provenance violation**. Those executions support no claim. The final probe source was restored, its preparse retained, and P04 is a fresh controlled replay; it is still non-authoritative because it takes `j=47` explicitly. The runner avoids the original environment failure with `DOT_SAGE=/private/tmp/f04_psc_reconstruct_sage`.

## Integrity

The per-run status JSON files contain the complete log hashes. R03 records SHA-256 hashes of the authoritative sources as they stood during R03 and both substantive input artifacts. Its terminal assertion is `all_assertions_passed: true`. All mathematical conclusions in `RESULT.md` rest on R01-R03, not on the probe or its replay.
