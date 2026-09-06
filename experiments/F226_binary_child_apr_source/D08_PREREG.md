# F226-D08 preregistration — exact-rate postprocessor

F226-D07 completed all exact numerator counts.  Sage represented each
`successes/denominator` value as a rational, and the JSON fallback converted
that rational to integer zero.  D08 does not rerun or change any orbit
calculation.  It reads the preserved D07 numerators and denominators, computes
Python floating summaries for display, and also preserves the exact minimum
fraction.  Output is `D08_OUTPUT.json`; log is `logs/F226-D08.log`.

