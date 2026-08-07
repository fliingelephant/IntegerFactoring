# F43-D01 run manifest

- Family: F26, modular-inverse quotient descent / Euclidean carry dynamics.
- Run ID: F43-D01.
- Status: attempt 4 is the current authoritative compact F43-D01 run. Attempts
  1 and 2 failed, and attempt 3 is retained as historical output without its
  exact source snapshot.
- Source: `scripts/F43_D01_scan.sage`.
- Runner: `run_F43_D01.sh`.
- Declared timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Declared input range: every squarefree odd semiprime \(N=pq\), with distinct
  odd primes \(p<q\) and \(15\le N\le511\).
- Declared uniform source: every \(u\in\{1,\ldots,N-1\}\) satisfying
  \(\gcd(u,N)=1\).
- Declared offset menu: \(c=1,\ldots,\min(N-1,n^2)\), where
  \(n=\lceil\log_2(N+1)\rceil\), with start \(u=N-c\).
- Authoritative attempt-4 recorded objects: per-input exact success fractions,
  ticket and divisor counts, depth maxima and maximizing starts, transcript
  counts and maximum multiplicity, exact successful offset lists, and terminal
  summaries. Complete raw trajectories, per-state inverse/carry records, and
  full collision groups exist only in the historical compressed attempt-3
  archive.
- Log: `logs/F43-D01.log`.
- JSON output: `output/F43-D01.json`.
- Intended disposition: exact finite discovery/certificate only. It cannot support an all-input probability or runtime assertion.
- Sage version: SageMath 10.9, Release Date 2026-05-04.
- Source SHA-256 for attempts 1 and 2: `c9fb4b13c108f33b3697c685bb65084fad09cfba57f0bf2032bef0ae11f6dfaf`.
- Runner SHA-256 for attempts 1 and 2: `6dd64c20d583848abbbe7fcb625cfd94a1989433167fac08e1bc6bf76cb1e2dd`.

## Attempt 1 — failed before source execution

- Command: `./run_F43_D01.sh`, launched from `experiments/F43_inverse_quotient_descent_kill` inside the workspace sandbox.
- Exit status: 1.
- Disposition: Sage import failed because its lazy-import cache attempted a write under `/Users/zhou/.sage/cache`, outside the writable workspace. The canonical log path was later overwritten by attempt 2, so the exact captured stderr was restored verbatim to `logs/F43-D01-attempt1.log` before any source amendment.
- Evidence: `logs/F43-D01-attempt1.log`.
- Output: none.

## Attempt 2 — failed during serialization

- Command: `./run_F43_D01.sh`, launched from the same directory with filesystem escalation solely so the same Sage runner could use its cache.
- Exit status: 1.
- Measured runner wall time: 3.119905 seconds.
- Disposition: all in-memory enumeration completed, but `json.dump` rejected a
  Sage `Integer` inside a carry sequence. The JSON is truncated and invalid,
  and supports no finite claim. Before attempt 3, the exact log was preserved
  at `logs/F43-D01-attempt2.log` and the partial output at
  `output/F43-D01-attempt2-partial.json`. The canonical JSON path now contains
  the authoritative compact attempt-4 certificate. The full attempt-3 JSON is
  retained only in `output/F43-D01-attempt3-full.json.gz`.
- Log SHA-256: `7ce024fb4d5072e7dd129a021923a16f607acc97e083973995ac7d8c5d06bef2`.
- Retained partial-output SHA-256: `61a3dd7260425baabacf7a00687c7d6ff477e4c8b821904776a7a42452e67fc6`.
- Evidence: `logs/F43-D01-attempt2.log` and `output/F43-D01-attempt2-partial.json`.

## Attempt 3 — preregistered mathematical amendment

- Authorization: the user resumed the full research goal on 2026-08-07.
- Intended command: the same `./run_F43_D01.sh`, with the same 120-second
  timeout and declared input range.
- Source amendment: cast carry entries at the JSON boundary, allow JSON to
  convert retained Sage integers with `default=int`, and add the previously
  requested per-state tickets `gcd(u-1,N)` and `gcd(u+1,N)`.
- No input range, source distribution, offset menu, descent recurrence, or
  asymptotic interpretation is changed.
- Source SHA-256: `0664a9132fcdcdc67d69a6a2d83d7773eaba5129b1107050c390fce779985fc9`.
- Provenance limitation: the exact attempt-3 source snapshot is not retained at
  a named path. This historical run is therefore not independently
  reproducible from source. Its full output and log remain preserved, but
  attempt 4 is the sole authoritative F43-D01 computation.
- Runner SHA-256: `6dd64c20d583848abbbe7fcb625cfd94a1989433167fac08e1bc6bf76cb1e2dd`.
- Outcome: completed successfully with exit status 0 under the declared timeout.
- Successful log: `logs/F43-D01.log`, SHA-256
  `e5768ac8c5dd935ed3fa270356796579b1b09c18101e44987949888c240e1525`.
- Successful JSON: `output/F43-D01.json`, SHA-256
  `92af2cee0e33aabdd70f8ee4a4007a7abfbe613473cf231a84fb9a2f5a8b35e2`.
- The JSON parses successfully and contains 52,066,215 bytes.

## F43-D02 — preregistered seeded scaling scan

- Purpose: test whether the favorable small-input hit rates from F43-D01 persist
  when balanced factors grow, before investing in a broader symbolic decoder.
- Source: `scripts/F43_D02_scaling.py`.
- Runner: `run_F43_D02.sh`.
- Declared timeout: 180 seconds, enforced by `/opt/homebrew/bin/timeout 180s`.
- Inputs: for target bits `8,10,12,14,16,18`, let `p` be the first prime at
  least `2^b` and `q` the first prime at least `p+2`; set `N=pq`.
- Uniform-source sample: 50,000 seeded pseudorandom unit draws per input, using
  one deterministic Python PRNG stream per input, master seed `0xF43D02`, and
  exact gcd rejection.
- Offset menu: every `c=1,...,min(N-1,n^2)`, start `u=N-c`.
- Tickets and recurrence: identical to successful F43-D01.
- Step cap: 10,000, recorded as a failure state rather than silently truncated.
- Output: compact counts, rates, terminal types, ticket types, and maximum depths;
  no raw trajectory dump.
- Disposition: finite seeded discovery only. It cannot prove an asymptotic hit,
  depth, or runtime bound.
- Source SHA-256: `6663207572401d6080ff4e593919adc7b0e625d17bd0b4413200aaf2e4e8d00a`.
- Runner SHA-256: `199fbea000e34cd1ba1f45158892edd8e15d9eb95495d56cc28f5b63bc1962a8`.
- Outcome: completed successfully in 6.35 seconds with exit status 0.
- Log: `logs/F43-D02.log`, SHA-256
  `0a77ec99f2db2781cef35fa9fb0e1ef7a7cdedcf288d382c871de413cd7d1ae3`.
- Output: `output/F43-D02.json`, SHA-256
  `d44bfe7e6f39c23fb01c8eed0bddd9d61d8428c637a74e9ac20680f903369e78`.
- Every sampled and offset trajectory terminated before the 10,000-step cap.
- Retained replay environment: Python 3.14.5.

## F43-D01 attempt 4 — preregistered compact certificate rerun

- Purpose: retain the smallest practical exact certificate while preserving the
  complete attempt-3 trajectories in compressed form.
- Attempt-3 full archive: `output/F43-D01-attempt3-full.json.gz`, SHA-256
  `f0c841388ef87ffae82d70daa566e1f64d354ad20c1288690fc3ea902d2eed79`.
  Decompression has SHA-256
  `92af2cee0e33aabdd70f8ee4a4007a7abfbe613473cf231a84fb9a2f5a8b35e2`,
  exactly the recorded successful attempt-3 JSON hash.
- Attempt-3 log copy: `logs/F43-D01-attempt3.log`, SHA-256
  `e5768ac8c5dd935ed3fa270356796579b1b09c18101e44987949888c240e1525`.
- Source amendment: omit raw per-start trajectories and full collision groups
  from the canonical JSON. Retain per-input exact success fractions, ticket and
  divisor counts, depth maxima and maximizing starts, transcript counts and
  maximum multiplicity, and exact successful offset lists.
- Input range, recurrence, tickets, enumeration, and timeout are unchanged.
- Source SHA-256: `8a132c7121774f382f66847f288f667160151b8465e66c4e5442778f0e73341c`.
- Runner SHA-256: `6dd64c20d583848abbbe7fcb625cfd94a1989433167fac08e1bc6bf76cb1e2dd`.
- Outcome: completed successfully with exit status 0 under the declared timeout.
- Compact canonical JSON: `output/F43-D01.json`, 254,235 bytes, SHA-256
  `167970dfbb2ed60f489ebac16c59e7448564feb6c2191c31bbac204437bb7fef`.
- Canonical log: `logs/F43-D01.log`, SHA-256
  `e5768ac8c5dd935ed3fa270356796579b1b09c18101e44987949888c240e1525`.
- The compact summary exactly matches attempt 3 on every displayed F43-D01
  result. The full trajectories remain recoverable from the compressed archive.

## F43-D03 — preregistered two-step contraction counterexample search

- Purpose: test the symbolic conjecture
  \(2D_N(D_N(u))\le u\) whenever \(u\) and \(D_N(u)>1\) are units, before
  attempting a proof of a logarithmic depth bound.
- Source: `scripts/F43_D03_two_step_contraction.py`.
- Runner: `run_F43_D03.sh`.
- Declared timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Exhaustive scope: every \(3\le N\le4095\) and every
  \(u\in\{2,\ldots,N-1\}\) with \(\gcd(u,N)=1\).
- Seeded scope: seed `0xF43D03`; 50 random odd moduli at each of 16, 24, 32,
  and 48 bits; 2,000 independently rejected uniform units per modulus.
- Recorded objects: eligible pair count, strict violations, equalities, the
  largest exact ratio \(2D_N^2(u)/u\), at most the first 100 counterexamples,
  and per-bit random counts.
- Disposition: finite counterexample search only. Passing cannot prove an
  unbounded contraction or depth theorem.
- Source SHA-256:
  `9d5fabddf846ee23fbc0294d4bb0a9cee2b403cb649ac1579cfb8a7703d21529`.
- Runner SHA-256:
  `8a102aaff0a68e8bcfc31e1dadd8ee5a3fb0887e4f6e6d9d10f1a86ad9f5738d`.
- Outcome: completed successfully with exit status 0 in 5.16 seconds.
- Log: `logs/F43-D03.log`, SHA-256
  `55718f818862bda90f5bfa12c31cbe2ae9dac8d61ff4c4c0f17a7e2d74a5e4d8`.
- Output: `output/F43-D03.json`, SHA-256
  `3fde9b23d46830c288c8feb3cae55f7ddca9cc8976cb47c60860b7ac4b43541e`.
- Result: the conjecture is false. The first counterexample is
  \(N=11,u=7\), with \(D_N(u)=5\) and \(D_N^2(u)=4>u/2\).
  Across 3,887,362 eligible pairs, 593,870 strict violations occurred. The
  largest recorded ratio was
  \(2\cdot1,521,444,424/1,526,018,684\), at
  \(N=2,666,124,659\). This is finite counterexample evidence only.
