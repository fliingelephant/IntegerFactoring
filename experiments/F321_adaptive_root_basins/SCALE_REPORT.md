# Larger public adaptive-root trials

**Family:** route:F29

**Status:** exact finite discovery data. The original F321 pilot files remain
unchanged. No asymptotic stage law, success theorem, or expected factoring
bound is inferred.

The scale uses balanced inputs with \(p\) just above
\(2^b\), \(b=18,20,22,24,26,28\), and \(q\) just above \(1.6p\), plus two
unbalanced inputs. Each method receives only \(N\), independent random bits,
and the public budget
\[
 B=\min(4096,\operatorname{bitlength}(N)^2).
\]
There are 32 independent trials per case and method. All finite failures are
retained as censors. Factors are offline labels only.

| \(p,q\) | bits | \(B\) | method | successes | mean gcd calls | mean modular multiplications | median successful stage |
|---|---:|---:|---|---:|---:|---:|---:|
| 262147, 419443 | 37 | 1369 | adaptive | 32/32 | 89.94 | 4,374 | 88.5 |
|  |  |  | rho | 32/32 | 420.59 | 1,262 | 379.5 |
|  |  |  | uniform gcd | 1/32 | 1,346.06 | 0 | 635 |
| 1048583, 1677733 | 41 | 1681 | adaptive | 32/32 | 141.22 | 10,947 | 138 |
|  |  |  | rho | 30/32 | 839.69 | 2,519 | 692.5 |
|  |  |  | uniform gcd | 0/32 | 1,681 | 0 | -- |
| 4194319, 6710927 | 45 | 2025 | adaptive | 32/32 | 230.69 | 29,030 | 232.5 |
|  |  |  | rho | 23/32 | 1,460 | 4,380 | 1,294 |
|  |  |  | uniform gcd | 0/32 | 2,025 | 0 | -- |
| 16777259, 26843623 | 49 | 2401 | adaptive | 32/32 | 310.22 | 57,698 | 290.5 |
|  |  |  | rho | 13/32 | 2,052.25 | 6,157 | 1,680 |
|  |  |  | uniform gcd | 0/32 | 2,401 | 0 | -- |
| 67108879, 107374217 | 53 | 2809 | adaptive | 32/32 | 572.81 | 179,632 | 583 |
|  |  |  | rho | 7/32 | 2,519.69 | 7,559 | 1,379 |
|  |  |  | uniform gcd | 0/32 | 2,809 | 0 | -- |
| 268435459, 429496751 | 57 | 3249 | adaptive | 32/32 | 859.94 | 408,299 | 854 |
|  |  |  | rho | 2/32 | 3,206.97 | 9,621 | 2,576.5 |
|  |  |  | uniform gcd | 0/32 | 3,249 | 0 | -- |
| 262147, 268435459 | 47 | 2209 | adaptive | 32/32 | 99.16 | 5,613 | 93 |
|  |  |  | rho | 32/32 | 463.66 | 1,391 | 398 |
|  |  |  | uniform gcd | 0/32 | 2,209 | 0 | -- |
| 1048583, 4294967311 | 53 | 2809 | adaptive | 32/32 | 166.72 | 16,262 | 154.5 |
|  |  |  | rho | 32/32 | 1,023.31 | 3,070 | 939 |
|  |  |  | uniform gcd | 1/32 | 2,739.75 | 0 | 593 |

Adaptive roots succeeded in all 256 trials. Under the same probe cap, rho
succeeded in \(107/192\) balanced trials and all 64 unbalanced trials. Uniform gcd
succeeded in two of 256 trials. The adaptive method uses fewer gcd calls
than rho here, but its evaluation depth makes its modular-multiplication
cost much larger at the upper balanced scales. Both cost coordinates are
material. The censored rho means in this table are finite capped costs, not
estimates of its expected work. A separate multiplication-budget comparison
is retained in RHO_WORK_REPORT.md.

The observed medians are compatible with several growth laws and do not
establish any of them. In particular, this table is not evidence for a
\(p^{1/3}\) stage theorem or a \(p^{2/3}\) work theorem.

The single process completed in 2.208405 seconds at 26,755,072 bytes peak
RSS under the 28-second internal alarm, 30-second external timeout, and
512 MiB ceiling.

Evidence:
composite_scale.py, scale_output.json, scale_status.json, scale_run.log,
SCALE_RESOURCE.md, and SCALE_SHA256SUMS.txt.
