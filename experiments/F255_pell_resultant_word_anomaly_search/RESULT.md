# F255 result — Pell/resultant/carry word anomaly search

## Status

The frozen remote run completed with exit status zero. The tested fixed word
grammar is a finite null under the preregistered interpretation. This is
discovery evidence only. It proves no all-input probability or runtime bound.

A fresh hostile audit is still required before any durable promotion.

## Frozen run

- Inputs: 50,304 labelled balanced semiprime rows across the ten frozen
  factor-bit sizes.
- Bank: the eight frozen Pell discriminants, with post-wrap powers through
  `4n`.
- Words: `baseline`, `rows`, `same_res`, `cross_res`, `hash_res`,
  `norm_minus`, `norm_plus`, `carry3`, `carry5`, and `combined`.
- Execution: eight worker threads under `nice -n 15` and a 14,400-second
  search timeout.
- Recorded mathematical runtime: 139.224 seconds. The remote manifest spans
  `2026-08-13T13:17:08Z` through `2026-08-13T13:19:30Z`.

The runner did not record peak resident memory. Thus the preregistered
four-GiB memory ceiling is not empirically authenticated.

## Exact result

The TSV has 50,304 data rows and all ten exact gcd pairs for every input. The
JSON has all 200 expected `(factor_bits, cohort, word)` summaries. Independent
reaggregation reproduced every count, mean, interpolated percentile, worst
witness, strict-improvement count, and saturation count. Exact rational
comparisons reproduced all strict-improvement counts.

The decisive safe-safe tail is null. At factor-bit sizes 32, 40, 48, 56, and
60, every non-baseline word has exactly the baseline summary. Every word has
zero strict improvements and zero saturated residuals there. For `combined`,
the worst-sample values of `-log2(H_N)` are respectively
`30.9753, 38.9804, 46.9744, 54.9707, 58.9854`. This is linear growth with the
factor bit size.

The `combined` word still has many strict improvements on random inputs, but
its random worst-sample values are also linear: `30.6813, 38.5964, 46.6919,
54.8809, 58.4931` at the same five sizes. These finite improvements are
anomalies to explain. They do not meet the frozen useful-lead threshold.

The exact global event totals reaggregated from the TSV are:

| Word | Strict improvements | Saturated residuals |
|---|---:|---:|
| `baseline` | 0 | 127 |
| `rows` | 39,826 | 15,188 |
| `same_res` | 41,052 | 22,763 |
| `cross_res` | 40,322 | 18,237 |
| `hash_res` | 40,463 | 19,197 |
| `norm_minus` | 40,679 | 20,827 |
| `norm_plus` | 40,719 | 20,863 |
| `carry3` | 39,641 | 13,604 |
| `carry5` | 39,293 | 11,273 |
| `combined` | 41,351 | 24,163 |

These totals mix different bit sizes and are descriptive only.

## Independent implementation checks

Source review confirmed the frozen discriminant, offset, odd-multiple,
cross-discriminant, and four-hash-partner menus. It also confirmed the exact
resultant, norm, carry, neutral-carry, final-power, and P205 score formulas.
The candidate words are evaluated modulo each hidden residual only after the
public words have been fixed.

An independent Python reconstruction evaluated one stored input from each of
the 20 `(factor_bits, cohort)` cells. It independently generated the Pell
rows and every edge and carry menu, then recomputed all 400 stored gcds. Every
value matched. A separate full-TSV pass checked primality, safe-prime labels,
bit sizes, balance, products, residuals, gcd divisibility, and stored quality
values. It found no arithmetic error.

## Protocol qualifications

1. The preregistration calls the random and safe-safe cohorts disjoint. They
   are not fully disjoint: the two 12-bit cohorts share 22 exact semiprimes.
   Each individual cohort has no duplicate, and every cohort of size 16 bits
   or larger is disjoint from its counterpart. The run therefore contains
   50,304 rows but 50,282 distinct semiprimes. This defect qualifies the
   12-bit comparison. It does not alter the larger-size finite null.
2. The JSON records the global input count and elapsed time, but it does not
   contain per-word global aggregate summaries. The exact event totals above
   were reconstructed from the preserved TSV.
3. The runner invokes `--self-test` under `set -e` before the mathematical
   run. The later successful run establishes that this command returned zero,
   but its stdout was not preserved in the experiment logs.
4. The remote artifacts establish the run interval and exact bytes. They do
   not establish which agent or process owner launched `remote_run.sh`.
   Launch ownership is unknown.

## Frozen interpretation

The preregistered outcome is `finite null for this fixed word grammar`.
Nothing here proves that another Pell bank, word grammar, or adaptive public
construction fails. Nothing here supplies an inverse-quasipolynomial progress
bound.
