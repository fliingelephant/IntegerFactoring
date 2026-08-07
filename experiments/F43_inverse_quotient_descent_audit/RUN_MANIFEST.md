# F43-A01 hostile artifact audit manifest

- Family: F26, modular-inverse quotient descent.
- Run ID: F43-A01.
- Purpose: independently replay the exact finite claims in F43-D01 through
  F43-D03, compare the compact D01 certificate with the retained full archive,
  and check every hash stated in the candidate manifest.
- Disposition: finite artifact audit only. This run supports no asymptotic
  probability, depth, or factoring claim.
- Source: `audit_artifacts.py`.
- Runner: `run_F43_A01.sh`.
- Timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Python: 3.14.5.
- Outcome: exit status 0 under the timeout.
- Source SHA-256:
  `a3dc96675635203976023ea109179ac71c81600e9988be10a413f2459fcad2ac`.
- Runner SHA-256:
  `200e55f53b3a47174ddedd3c48c638bea8307ecd4d2a0af7c51005cc02c63066`.
- Log: `logs/F43-A01.log`, SHA-256
  `bdb496809b9b4c1ce553b58ed8987f5e9ac47b807c1c5747e97a3d3ad8f311e9`.
- Output: `output/F43-A01.json`, SHA-256
  `5e45881457725882193dc18fdfb059bbb6160baba704922f91e6827970f877ad`.

The replay reconstructed all compact D01 records and its summary, all D02
records, and the complete D03 summary, retained counterexample prefix, and
per-bit random records. All comparisons passed. The decompressed D01 attempt-3
archive has the hash stated in the candidate manifest, and its displayed
projection equals the compact attempt-4 certificate. The only declared hash
failure is the preserved failed-attempt partial JSON: the manifest states
`7a2c7e...`, while the retained file has SHA-256 `61a3dd...`.
