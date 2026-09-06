# F301 public rectangle reference experiment

**Status:** complete finite validation. This packet implements the public
rectangle construction and a deliberately numerical reference `Empty`
oracle. It does not implement a succinct oracle.

## Implementation boundary

`factor_rectangles.py` uses the exact grid

\[
 L_j=16(17/16)^j
\]

through Python `Fraction`. For each recursive input it first checks exactly
the fixed primes 2, 3, 5, 7, 11, and 13. It then chooses the largest power of
two \(M\leq N/8\), generates the stated nonempty boxes, queries them in
public grid order, and bisects only a box reported nonempty. A singleton is
validated by exact division and both factors are processed recursively.

The reference oracle is called only on odd inputs. For every call it scans
the odd integers \(x\) in the supplied interval and tests whether

\[
 y=Nx^{-1}\bmod M
\]

lies in the supplied \(y\)-interval. It records every query and every odd
\(x\) actually examined. Neither a gcd with \(N\) nor an offline factor label
selects a box, a query, or a bisection branch.

Elementary trial division is separate audit code. It supplies expected
factorizations and coverage labels only after the public boxes and actions
have been generated.

## Exact finite results

| Corpus | Cases | Result | Oracle queries | Odd \(x\) values scanned |
| --- | ---: | --- | ---: | ---: |
| Every \(2\leq N\leq4096\) | 4,095 | All complete factorizations equal trial division | 17,553 | 15,197 |
| Seeded inputs of at most 24 bits | 120 | All complete factorizations equal trial division | 10,116 | 92,209 |
| Labelled 32--512-bit factor pairs | 40 | Every pair is covered by a generated public box | 0 | 0 |

The exhaustive range contains 564 primes, 3,531 composites, 1,605 inputs
with repeated prime factors, and 2,632 composites whose largest recorded
prime factor is at least eight times the smallest. Its public recursion
generated 20,589 boxes. The audit checked every integer pair in every one of
those boxes: every product congruent to \(N\) modulo \(M\) was exactly
\(N\). All 455 composite recursive events that reached the rectangle stage
had a labelled factor pair in an already generated box. The implementation
used 230 nonempty-box bisection queries in this range. Representative public
traces for \(N=289,323,4093\) are retained in `output.json`.

The seeded 24-bit corpus uses seed 30120260907 and has 30 cases in each
declared category: random integers, primes, repeated factors, and unbalanced
composites. Its audit checked 12,316 generated boxes and all 78 composite
recursive events that reached the rectangle stage. The box endpoint and
product-gap assertions passed in every case.

The large coverage audit has eight pairs at each exact product bit length
32, 64, 128, 256, and 512. It contains 15 balanced, 15 unbalanced, and 10
repeated labelled pairs, all with \(a,b\geq17\). All 40 were contained, in
one orientation, in at least one box generated from \(N=ab\) alone. These
cases generated 43,465 boxes in total; the largest single list had 2,881
boxes. No reference-oracle call or large-integer factorization was made.

## Resources and provenance

The formal single-process run completed in 1.777 seconds with 28,590,080
bytes peak RSS, under the source-level 60-second alarm. Preflight and the
planning cap are recorded in `RESOURCE_ESTIMATE.md`.

The first complete run was wrapped in `/usr/bin/time -l`. The Python process
completed, but the wrapper returned exit code 1 because sandbox policy
blocked its final `kern.clockrate` query. That log and output are retained as
`run_time_wrapper_failed.log`, `output_time_wrapper.json`, and
`status_time_wrapper_source_complete.json`; `TIME_WRAPPER_ISSUE.md` records
the issue. The formal `run.log` uses the source's monotonic runtime and peak
RSS. The deterministic mathematical payloads of the two runs agree exactly.

SHA-256:

- statement: `e6a68b51f1dc7f0820741b290c916f4318a126d4932ae3a12da3cab28777623d`
- source: `9f4323098d5542d745997111cc6e91765b89e132dd741a1fda5f594205ea9ab6`
- formal output: `d4b23e8be5d0cce22c1f380f3d2170b06598585280a4adf3eaeb87eef9fec50a`

Full per-input results are in `small_exhaustive.csv`, `random_cases.csv`, and
`large_coverage.csv`. Aggregate counters and traces are in `output.json`.

## What remains unimplemented

These checks do not prove the all-input reduction or an asymptotic running
time. The reference `Empty` oracle explicitly enumerates interval elements;
its scan count is evidence of numerical work, not a candidate
quasipolynomial algorithm. The packet supplies no succinct rectangle oracle,
no large-input reference factorization, and no factoring complexity bound.
