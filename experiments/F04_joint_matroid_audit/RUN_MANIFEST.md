# F04 joint-matroid hostile-audit manifest

**Audit family:** `F04_joint_matroid_audit`.

All commands were executed through `run_with_timeout.py`.  Each status JSON
contains the exact argv, hard timeout, UTC start/end timestamps, wall duration,
exit code, timeout flag, disposition, log path, and log SHA-256.  Logs contain
matching machine-readable start and finish envelopes.

## Runs

| Run | Hard limit | Disposition | Wall time | Named source | Retained result |
| --- | ---: | --- | ---: | --- | --- |
| A01 | 120 s | completed, exit 0 | 4.042646 s | `reconstruct_joint_profiles.sage` | Fresh joint P14 matrix, ranks, determinants, CRT: `output/A01_P14_joint.json` |
| A02 | 900 s | **timed out**, SIGTERM `-15` | 900.005356 s | `reconstruct_joint_profiles.sage` | Non-authoritative monolithic P11 attempt; no output JSON |
| A03 | 400 s | **failed**, exit 1 | 212.804281 s | `build_p11_joint_matrices.sage` | Both full matrices were saved; final summary JSON failed on Sage-integer serialization |
| A04 | 300 s | **failed**, exit 1 | 24.706607 s | `certify_p11_joint_matrices.sage` | Non-authoritative v1 recovery failed on the same serialization boundary |
| A05 | 300 s | completed, exit 0 | 61.285845 s | `certify_p11_joint_matrices_v2.sage` | Authoritative CRT reconstruction, hashes, counts, and prefix determinants: `output/A05_P11_joint_certify_v2.json` |
| A06 | 1200 s | completed, exit 0 | 1102.150164 s | `solve_p11_tail.sage` | Exact `p` normalization and full product check: `output/A06_P11_tail_mod_100000007.json` |
| A07 | 1500 s | completed, exit 0 | 1111.119644 s | `solve_p11_tail.sage` | Exact `q` normalization and full product check: `output/A07_P11_tail_mod_199999991.json` |
| A08 | 180 s | completed, exit 0 | 53.240473 s | `compare_p11_tail_supports.sage` | Exhaustive one-/two-tail support counts and direct separator: `output/A08_P11_tail_supports.json` |
| A09 | 120 s | completed, exit 0 | 0.378381 s | `audit_artifacts.py` | Cross-source/status/artifact audit: `output/A09_artifact_audit.json` |

The exact runner commands are preserved twice: as the first JSON line of each
`logs/A*.log` and in the corresponding `status/A*.json`.  A02, A03, and A04
remain present as failed, non-authoritative runs; no later file overwrites
their logs or statuses.

## Authoritative large artifacts

A03 wrote both full matrices before its final JSON error.  A05 loaded both,
reconstructed every global entry by CRT, reproduced every candidate row hash
and the aggregate global hash, recomputed both prefix determinants, and only
then certified their byte hashes for A06/A07.

| Artifact | Bytes | SHA-256 | Status |
| --- | ---: | --- | --- |
| `output/matrices/A03_P11_mod_100000007.sobj` | 414018575 | `5556711714baa4dec8b8f79b292bf228c2a04201604ec22c684b20adf7169d71` | A03-produced; A05-validated |
| `output/matrices/A03_P11_mod_199999991.sobj` | 415523429 | `ba4b6bf757174d153a6b5986eb161b1857ac7cb8e54dac77752712dc8f3a1de6` | A03-produced; A05-validated |
| `output/matrices/A06_P11_normalized_mod_100000007.sobj` | 1542030 | `311fa71d9001fffb2d23ca77edd9a705dbec55d0a1ccd3ba5ed38111b60b6998` | A06 authoritative |
| `output/matrices/A07_P11_normalized_mod_199999991.sobj` | 1547823 | `c90dec16e95d0ce60bbb1ad962b02add397d3f26e9cac19d34446ed00262cb98` | A07 authoritative |

The two A03 matrices are retained unmodified and uncompressed, totaling
`829,542,004` bytes.  They were not deleted or replaced after the failed run.

## Named source hashes

| Source | SHA-256 | Role |
| --- | --- | --- |
| `run_with_timeout.py` | `3ad9aee2d55548ef74b1347233a47978ecf0806b5f8ef458ea8008bf5e8388db` | Hard-timeout/status runner |
| `reconstruct_joint_profiles.sage` | `ea1419b9a577641ef9bfc072ca2c32cd8faa5e70f38064e01b167adc79cc3e89` | A01 and failed A02 |
| `build_p11_joint_matrices.sage` | `9d332825facafc2bed2175541f046c2f1d9c703937b6d1236d648a1bcffdc4e3` | A03 producer; failed after matrix saves |
| `certify_p11_joint_matrices.sage` | `921d644b7d3322a99258ef98f79f9f141e842d9dc52f7096d88876687db13968` | Failed A04 certificate v1 |
| `certify_p11_joint_matrices_v2.sage` | `f2440b965df180671a236ba106598a5f567ef61d26a8d9cf86aa7366ef6f9e94` | A05 authoritative matrix certificate |
| `solve_p11_tail.sage` | `59718b0d3656458617e14a3c903efc4e1646b7cd42ef0d77d97b9032987ed62f` | A06/A07 exact normalizations |
| `compare_p11_tail_supports.sage` | `9b00c083cce68755b1bb129c61b1a1d1219c6d03bf88abfbece44a914618dc59` | A08 support scan and direct determinants |
| `audit_artifacts.py` | `e4ccbccb8dc0d90a8a2487e3e2e64fc5d9f1152efb2a3403d76d4f5281131dd2` | A09 final artifact audit |

Sage generated preparsed `.sage.py` cache files during execution.  They are
not named mathematical sources; each authoritative JSON records and hashes
the corresponding immutable `.sage` source.

## Key outputs

- A01: P14 global hash
  `170e8b80ca1c4e6a5f335c376a4a8ebd3c95c782f2b9d74da1d4ab9cd3f997d7`,
  ranks `23/266`, determinants `0/30`, CRT/gcd `71815/271`.
- A05: P11 global hash
  `85c4bcda5ff5d0f23117721a503fedb77e3a84b9d708a3ceb0f7bed1673c6f53`,
  determinants `56136614/132391112`, CRT/gcd
  `16315256998204520/1`, all raw entries units.
- A06/A07: exact product identities `B_l C_l = T_l`, with no zero entries
  in either 2942-by-11 normalized matrix.
- A08: zero one-tail support mismatches; exactly two two-tail support
  mismatches among `237,941,605` exchanges per field.  The directly verified
  first exchange has local determinants `15564403/0`, CRT
  `2473353088699106`, and gcd `199999991`.
- A09: `audit_passed=true`; all fresh/candidate hashes and arithmetic checked.
