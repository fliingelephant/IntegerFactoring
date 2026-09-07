# Public selected-fiber guard pilot

**Family:** route:F29

**Status:** exact bounded comparison. It tests the guard in ANALYSIS.md with
no factor-aware rejection. No success or drift theorem is claimed.

After a unit proposal \(a=H(x)\), the guarded variants evaluate
\(K=2\) or \(K=8\) fresh independent values \(H(x_j)\) and gcd-screen
\(H(x_j)-a\). A proper gcd is returned and verified. A gcd equal to \(N\)
rejects the proposed parameter without updating \(H\). The parameter is
accepted only after all \(K\) differences are units. Every proposal and
guard evaluation counts once against
\[
 B=\min(4096,\operatorname{bitlength}(N)^2).
\]
The unguarded adaptive algorithm receives the same total H-evaluation budget.

Four balanced inputs use \(p\) near \(2^b\),
\(b=12,16,20,24\), and \(q\) near \(1.6p\). Each method has 16 independent
trials. All interrupted guards and other censors are retained.

| \(b\) | method | successes | mean H evaluations | mean modular multiplications | accepted/proposed parameters | factor source |
|---:|---|---:|---:|---:|---:|---|
| 12 | base | 16/16 | 24.06 | 305 | 369/369 | 16 proposal |
|  | guard K=2 | 16/16 | 67.25 | 861 | 352/356 | 12 proposal, 4 guard |
|  | guard K=8 | 16/16 | 141.88 | 1,319 | 245/255 | 6 proposal, 10 guard |
| 16 | base | 16/16 | 54.44 | 1,550 | 854/854 | 16 proposal |
|  | guard K=2 | 16/16 | 188.38 | 6,376 | 999/1000 | 15 proposal, 1 guard |
|  | guard K=8 | 16/16 | 462.56 | 13,861 | 818/823 | 11 proposal, 5 guard |
| 20 | base | 16/16 | 161.75 | 13,798 | 2572/2572 | 16 proposal |
|  | guard K=2 | 16/16 | 426.94 | 31,937 | 2271/2272 | 15 proposal, 1 guard |
|  | guard K=8 | 13/16 | 1098 | 78,803 | 1947/1952 | 11 proposal, 2 guard |
| 24 | base | 16/16 | 350.19 | 68,061 | 5587/5587 | 16 proposal |
|  | guard K=2 | 16/16 | 1101.81 | 220,262 | 5871/5871 | 16 proposal |
|  | guard K=8 | 7/16 | 2092.38 | 254,230 | 3712/3721 | 7 proposal |

Guard \(K=2\) succeeded in all 64 trials but used more evaluations and
modular multiplications than the matched base. Guard \(K=8\) succeeded in
52 of 64 trials; three \(b=20\) and nine \(b=24\) trials exhausted the
budget during a guard.

No proposed parameter was rejected by a global equality in any finite
trial. Guard-difference gcds found six factors for \(K=2\) and 17 for
\(K=8\); all other successes came from proposal values. Thus the guard
created an extra factor channel in some trials, but its intended equality
rejection did not activate in this sample and its public cost was larger.
This pilot therefore does not validate a beneficial overshoot mechanism.
The finite tradeoff supplies no all-input conclusion.

The process completed in 0.902084 seconds at 25,919,488 bytes peak RSS
under its separate 28-second internal alarm, 30-second external timeout,
and 512 MiB ceiling.

Evidence:
fiber_guard.py, fiber_guard_output.json, fiber_guard_status.json,
fiber_guard_run.log, FIBER_GUARD_RESOURCE.md, and SCALE_SHA256SUMS.txt.
