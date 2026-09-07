# Exact small-input fair-branch comparison

**Family:** route:F31

Status: completed finite rational calculation. The expected-work argument in
FAIR_BRANCH.md remains an author derivation, not independently promoted.

The pilot through N=51 and the scale through N=301 both passed. The full
run covered all 10,272 unit parameters on 89 odd composite inputs, visited
53,230 memoized states, and checked 542 reached small-input floor sums by
direct enumeration. The source evaluated success and operation expectations
over every fair branch, not one sampled path. Every expected query count
satisfied the stated ceil(log_2(h))+1 bound in this finite set.

There were 818 parameters where the minimum-child rule fails but a fair
branch has positive success probability. For example, N=35,a=4 has success
probability 1/2 and expected query count 5/2 under fair branches; the minimum
branch fails. This confirms a change in reachable outputs, not a uniform
success theorem.

Averaging each policy over the complete unit set of each listed N, fair
branches have higher success probability on 28 inputs, lower probability on
22, and the same probability on 39. On 27 inputs with positive success for
both policies, fair branches have lower expected queries per success; for
gcd calls per success the corresponding count is 30. Generation is excluded
from these conditional comparisons. Operation counts are not bit-time bounds.

| N | Minimum success | Fair success | Minimum queries/success | Fair queries/success |
| ---: | ---: | ---: | ---: | ---: |
| 35 | 1/4 | 1/2 | 34/3 | 485/96 |
| 39 | 11/12 | 85/96 | 15/11 | 128/85 |
| 65 | 11/24 | 5/8 | 59/11 | 59/16 |
| 209 | 4/15 | 77/360 | 407/24 | 43361/1792 |
| 299 | 3/22 | 295/1408 | 239/6 | 380099/14160 |

The fair policy is therefore not uniformly better even on the finite set.
The next experiment should compare complete charged attempts on the same
biased rational sources as F336, with fresh branch bits and all failures
retained. Do not extrapolate the small conditional table to large inputs.

The scale took 0.518 seconds and peaked at 27,623,424 bytes RSS. Evidence:
fair_branch_checks.py, fair_branch_pilot.json, fair_branch_scale.json, their
logs and terminal status files, and FAIR_BRANCH_RESOURCE.md. Source SHA-256:
153ceb1021f679a8fb047c99db98355cd7a099a702016ec6f9d8344b08a00797.
