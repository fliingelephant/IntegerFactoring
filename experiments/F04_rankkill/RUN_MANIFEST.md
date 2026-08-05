# F04 rank-separator computation manifest

All commands serve family `F04_rankkill`. The known factors are used only to
classify the two CRT components of a finite candidate counterexample.

**Provenance limitation.** This discovery manifest retained each named source,
timeout value, log, output, and disposition, but it did not retain the exact
command and environment strings. It is therefore non-authoritative for exact
command provenance. In addition, R04 used binary64 logarithms when ordering its
“first in the box” search; that phrase is exploratory, not a rigorous minimality
claim. The analytic witness does not depend on either point, and the independent
`experiments/F04_rank_audit` A02 run supplies exact authoritative commands and
checks.

| Run | Source | Timeout | Log | Output | Disposition |
| --- | --- | --- | --- | --- | --- |
| R01 | `scan_local_gcd_degrees.sage` | 120 s | `logs/R01_benchmark_1_10.log` | `output/R01_benchmark_1_10.json` (not created) | Failed before computation: Sage tried to write its cache under the sandbox-forbidden `~/.sage`; retained log, superseded by R02 with an explicit writable `DOT_SAGE`. |
| R02 | `scan_local_gcd_degrees.sage` | 120 s | `logs/R02_benchmark_1_10.log` | `output/R02_benchmark_1_10.json` | Passed shifts 1--10; both local gcd-degree sequences are identically zero. Setup/factorization dominated the 43.66 s runtime. |
| R03 | `scan_local_gcd_degrees.sage` | 300 s | `logs/R03_full_1_2943.log` | `output/R03_full_1_2943.json` | Passed full shifts 1--2943 (the standard floor bound 2942 plus the adjacent ceiling convention); every local gcd degree is zero in both CRT fields, so there is no rank separator. |
| R04 | `search_small_rank_counterexample.sage` | 300 s | `logs/R04_small_search_1000.log` | `output/R04_small_search_1000.json` | Passed. Enumerating distinct prime pairs in increasing product found the first hard-regime zero/zero scan in the box at `N=79403=271*293`, `r=269`; all 267 shifts through the ceiling convention have degree zero on both sides. Three smaller hard-regime candidates have genuine mismatches. |
| R05 | `scan_local_gcd_degrees.sage` | 120 s | `logs/R05_verify_79403.log` | `output/R05_verify_79403.json` | Passed direct verification of the small certificate. The local factor-degree patterns are `[1,268]` and `[1,67,67,67,67]`; all 267 tested gcd degrees are zero. |
| R06 | `scan_all_local_residues_79403.sage` | 120 s | `logs/R06_all_local_residues_79403.log` | `output/R06_all_local_residues_79403.json` | Partially valid: exhaustive degree distributions and exact mismatch count are correct, but Sage's rational-to-JSON coercion serialized the derived probability as zero. Superseded by R07. |
| R07 | `scan_all_local_residues_79403.sage` | 120 s | `logs/R07_all_local_residues_79403.log` | `output/R07_all_local_residues_79403.json` | Passed. Exhausted all 271 and 293 local shift residues; distributions are `{0:268,1:2,269:1}` and `{0:290,1:2,269:1}`, with exact uniform-CRT mismatch count `1678/79403`. |
