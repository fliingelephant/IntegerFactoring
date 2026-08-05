# F04 hostile-audit computation manifest

This computation serves family F04 and the focused hostile audit of C07/X05.
It is independent of the retained scanner: it neither imports nor executes
`experiments/F04/scan_aks_semiprime.sage`.

| Run | Timeout command (inside the repository root) | Log | Output | Status |
| --- | --- | --- | --- | --- |
| A01 | `DOT_SAGE=/tmp/f04_audit_sage timeout 300s sage experiments/F04_audit/verify_f04_counterexample.sage --retained experiments/F04/output/sage_aks_20000000499999937_full.json --output experiments/F04_audit/output/f04_hostile_audit.json > experiments/F04_audit/logs/f04_hostile_audit.log 2>&1` | `experiments/F04_audit/logs/f04_hostile_audit.log` | `experiments/F04_audit/output/f04_hostile_audit.json` (partial, invalid) | exit 1 after both full scans; JSON serialization rejected Sage `Integer`; source SHA-256 before the fix: `485e3439eb7d92c4d60b049b6418428f6fd790ac523a6662ac1f5b3da20e6c84` |
| A02 | `DOT_SAGE=/tmp/f04_audit_sage timeout 300s sage experiments/F04_audit/verify_f04_counterexample.sage --retained experiments/F04/output/sage_aks_20000000499999937_full.json --output experiments/F04_audit/output/f04_hostile_audit_A02.json > experiments/F04_audit/logs/f04_hostile_audit_A02.log 2>&1` | `experiments/F04_audit/logs/f04_hostile_audit_A02.log` | `experiments/F04_audit/output/f04_hostile_audit_A02.json` | exit 0; 71.254 s; `audit_passed=true`; source SHA-256 `843003cabaca6993e8cf5b4d1dad03270638870c2bad4ca12a5a87638f2b7d85` |

A01 is retained as a failed audit run, not as evidence.  A02 repeated every
parameter check, both full coefficient scans, and all direct Frobenius
cross-checks after the serialization-only correction.  A02 certificate
SHA-256 is `388bcac2e95b298f4a823bc717bcf5eac593743b7f2c93d7083d6187035d211b`;
its log SHA-256 is
`72a4e750604882d907a39691f04ce31cd084731affa410fca8dbddd0baf83b47`.
