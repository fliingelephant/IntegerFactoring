# F04/X12 hostile-audit run manifest

All commands used named source files and hard process-group timeouts. No canonical file was edited.

| Run | Timeout | Wall time | Exit | Disposition | Retained evidence |
|---|---:|---:|---:|---|---|
| A01_theorem_stress | 180 s | 4.119 s | 1 | Failed after completing the search because JSON could not serialize a Sage integer. No result JSON. Source was corrected in place, so this exact failed source revision is not retained; log/status are retained and the run supports no claim. | `logs/A01_theorem_stress.log`, `output/A01_theorem_stress_status.json` |
| A02_theorem_stress | 180 s | 2.045 s | 0 | Completed, but its “gap” counter also counted the initial `deg F -> deg G` gap rather than only internal Euclidean gaps. Superseded by A03. Its exact source revision was modified in place and is not retained; output/log/status are retained and no conclusion relies on its gap count. | `output/A02_theorem_stress.json`, `logs/A02_theorem_stress.log`, `output/A02_theorem_stress_status.json` |
| A03_theorem_stress | 180 s | 2.042 s | 0 | **Authoritative direct fixed-matrix theorem stress test.** No timeout; no counterexample in 4,932 cases / 17,556 determinants. | `stress_field_theorem.sage`, generated `.sage.py`, `output/A03_theorem_stress.json`, `logs/A03_theorem_stress.log`, `output/A03_theorem_stress_status.json` |
| A04_full_exhaustion | 900 s | 202.354 s | 0 | **Authoritative fresh 2,942-shift global-before-local exhaustion and endpoint residue materialization.** | `exhaust_degree_chains.sage`, generated `.sage.py`, `output/A04_full_exhaustion.json`, `output/A04_rows.jsonl`, `output/A04_endpoints.json`, `logs/A04_full_exhaustion.log`, `output/A04_full_exhaustion_status.json` |
| A05_artifact_audit | 120 s | 0.085 s | 0 | **Authoritative artifact/count/hash/CRT audit; `audit_passed=true`.** | `audit_artifacts.py`, `output/A05_artifact_audit.json`, `logs/A05_artifact_audit.log`, `output/A05_artifact_audit_status.json` |
| A06_exact_convention | 180 s | 1.868 s | 1 | Failed: assumed Sage's generic subresultant return list was dense under positive-gcd/gap cases; `IndexError`. The exact failed source revision was modified in place and is not retained. Log/status retained; supports no claim. | `logs/A06_exact_convention.log`, `output/A06_exact_convention_status.json` |
| A07_exact_convention | 180 s | 1.771 s | 1 | Failed again after restricting to coprime cases: the exhaustive rescaled family still encountered a sparse Sage list. Current source/preparse and log/status retained. Supports no claim and establishes no counterexample to the determinant theorem. | `verify_exact_convention.sage`, generated `.sage.py`, `logs/A07_exact_convention.log`, `output/A07_exact_convention_status.json` |

The full commands are recorded verbatim in each log and status JSON. Status files also record UTC start/finish times, exit code, timeout flag, disposition, and complete-log SHA-256. None of A01-A07 timed out.

## Authoritative hashes

- A03 source: `f1dc76124e52d3e09152256eb89124c6f1931241b776b711398a6e4df3943867`.
- A04 source: `cdf1e2c79ef367c1bb8367f16ce168e5a4ddbe217c7c1c71d27c5774e1fa3aae`.
- A04 rows: `7b1d411243e808e199d8bdd9e89b63f48aecfd344f650d80cc1dcae3a4298cb7`.
- A04 endpoints: `9fb793aefbeaddd1901ed612eb4a2a9fa9f9ec74ec526f3d0b46b93dea65b5d2`.
- A04 summary: `120ef676892e2165a50c78044dc8e3d149fc10b383ea78c0cb780db5fa8e4e2e` (recorded by A05).
- A05 audit source: `08294257a9bcb9dddaa7c3a8fbed4ecab06770f3d7338a6c4bd66e46dd5d6c1f`.

## Counts and provenance

A04 checked 8,687,726 global coefficients, 17,381,336 local degree-chain entries (two chains of length 2,954 per shift), and 17,375,452 determinant zero/nonzero statuses (2,953 indices per field per shift). A05 compared all 2,942 fresh global coefficient hashes with the prior R08 rows and both complete endpoint vectors with prior R05/R09.

The authoritative claims use A03-A05 only. A01, A02, A06, and A07 are fully dispositioned above; missing exact source revisions for A01/A02/A06 are explicit provenance limitations rather than silently reconstructed artifacts.
