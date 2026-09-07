# Work-matched Pollard-rho control

**Family:** route:F29

**Status:** exact finite cost comparison on the SCALE_REPORT.md datasets.
No expected-work or asymptotic claim is made.

The same-probe-cap rho control in SCALE_REPORT.md is heavily censored at the
upper balanced scales. Its capped average is not an estimate of expected
work because one rho step uses only three modular multiplications, while one
adaptive H evaluation has growing depth.

For each public
\[
 B=\min(4096,\operatorname{bitlength}(N)^2),
\]
this control instead gives rho the modular-multiplication budget
\[
 W=B(B-1)/2,
\]
equal to the worst-case adaptive multiplication count if every earlier
proposal becomes a stored root. Each Floyd step uses three multiplications
and one gcd. A gcd equal to \(N\) restarts with fresh public random \(x,c\)
inside the same \(W\). Every trial keeps its full cost and censor status.

The source independently rebuilds the eight public cases and verifies their
\((N,B)\) pairs against the retained scale output before running 32 new
trials per case.

| \(p,q\) | adaptive successes | rho successes | adaptive mean multiplications | rho mean multiplications | adaptive mean gcds | rho mean gcds |
|---|---:|---:|---:|---:|---:|---:|
| 262147, 419443 | 32/32 | 32/32 | 4,374 | 1,074 | 89.94 | 358.16 |
| 1048583, 1677733 | 32/32 | 32/32 | 10,947 | 2,414 | 141.22 | 804.50 |
| 4194319, 6710927 | 32/32 | 32/32 | 29,030 | 4,826 | 230.69 | 1,608.81 |
| 16777259, 26843623 | 32/32 | 32/32 | 57,698 | 8,115 | 310.22 | 2,705.03 |
| 67108879, 107374217 | 32/32 | 32/32 | 179,632 | 17,510 | 572.81 | 5,836.75 |
| 268435459, 429496751 | 32/32 | 32/32 | 408,299 | 38,759 | 859.94 | 12,919.75 |
| 262147, 268435459 | 32/32 | 32/32 | 5,613 | 1,566 | 99.16 | 521.84 |
| 1048583, 4294967311 | 32/32 | 32/32 | 16,262 | 2,826 | 166.72 | 942.03 |

All 256 work-matched rho trials succeeded before their caps. No trial had a
full-cycle gcd equal to \(N\), so the implemented restart branch was not
exercised by this sample. Rho used more gcd calls and fewer modular
multiplications than adaptive roots in every row. Neither operation count
alone establishes bit complexity, and the finite ratios are not fitted or
extrapolated.

The run completed in 0.325042 seconds at 27,017,216 bytes peak RSS. It used
one process, an internal 28-second alarm, an external 30-second timeout, and
a 512 MiB ceiling.

Evidence:
rho_work_matched.py, rho_work_output.json, rho_work_status.json,
rho_work_run.log, RHO_WORK_RESOURCE.md, and SCALE_SHA256SUMS.txt.
