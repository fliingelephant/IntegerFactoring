# F115 audit failed runs

## 2026-08-08 03:15:08Z — incorrect excluded-overlap assertion

The first formal audit stopped before any source replay.  A preliminary shell
comparison had sorted decimal moduli numerically and then passed them to
`comm`, which requires lexicographic order.  That invalid comparison reported
zero overlap between the selected corpus and the excluded wide file.

The JSON-level set calculation correctly found 24 overlapping cases and 62
additional distinct cases.  The verifier assertion was corrected from zero to
24.  The complete failure is preserved in
`AUDIT_FAILED_20260808T031508Z_EXECUTION.log`.  It supplies no mathematical
evidence.
