# F04 rank-obstruction hostile-audit manifest

Every run in this directory uses the independently written source
`audit_rank_obstruction.sage` and family ID `F04_rank_audit`.

| Run | Exact command | Timeout | Log | Output | Disposition |
| --- | --- | --- | --- | --- | --- |
| A01 | `env DOT_SAGE=/tmp/f04_rank_audit_sage timeout 180 sage experiments/F04_rank_audit/audit_rank_obstruction.sage --output experiments/F04_rank_audit/output/A01.json > experiments/F04_rank_audit/logs/A01.log 2>&1` | 180 s | `logs/A01.log` | `output/A01.json` (truncated invalid JSON) | All mathematical assertions passed, but JSON serialization failed on Sage-integer dictionary keys in `chain_24_mod_269`; retained and superseded by A02. |
| A02 | `env DOT_SAGE=/tmp/f04_rank_audit_sage timeout 180 sage experiments/F04_rank_audit/audit_rank_obstruction.sage --output experiments/F04_rank_audit/output/A02.json > experiments/F04_rank_audit/logs/A02.log 2>&1` | 180 s | `logs/A02.log` | `output/A02.json` | Passed all exact parameter assertions; full local-shift distributions; factor-degree checks; degree-23 checks; and direct exponent-`N` versus Frobenius-substituted identities at five shifts in both fields. |
