# F112 audited correction

The F115 hostile audit independently replayed all 100 declared cases.

The per-case result and RESULT.md prose are correct:

- 67 parity factors;
- 19 direct factors;
- 14 nulls.

The authoritative JSON field direct_factor_cases is wrong. It reports 33
because it subtracts the 67 parity cases from all 100 cases and therefore
counts the 14 nulls as direct factors.

The exact corpus qualifier is also narrower than the first sentence of
RESULT.md. F112 includes all 100 distinct qualifying rows from completed,
non-running F104 output files after it explicitly excludes
PRIME_SCAN_320K_640K_WIDE_OUTPUT.json. That interrupted file has status
running but contains 86 qualifying completed rows: 24 overlap the declared
corpus and 62 are additional distinct cases.

No candidate artifact was changed. The corrected bounded claim and the
original aggregate failure are pinned by the F115 audit.
