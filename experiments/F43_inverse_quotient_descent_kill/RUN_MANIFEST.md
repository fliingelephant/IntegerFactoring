# F43-D01 run manifest

- Family: F26, modular-inverse quotient descent / Euclidean carry dynamics.
- Run ID: F43-D01.
- Status: stopped after two failed attempts; no successful authoritative run.
- Source: `scripts/F43_D01_scan.sage`.
- Runner: `run_F43_D01.sh`.
- Declared timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Declared input range: every squarefree odd semiprime (N=pq), with distinct odd primes (p<q) and (15\le N\le511).
- Declared uniform source: every (u\in\{1,\ldots,N-1\}) satisfying \(\gcd(u,N)=1\).
- Declared offset menu: (c=1,\ldots,\min(N-1,n^2)), (n=\lceil\log_2(N+1)\rceil), with start (u=N-c).
- Recorded objects: complete raw descent trajectories; exact inverse and carry at every unit state; first current/carry nonunit ticket; first ticket after additionally testing \(\gcd(u-v,N)\), \(\gcd(u+v,N)\), and \(\gcd(u^2-1,N)\); complete carry-transcript collision groups; depths and terminal states.
- Log: `logs/F43-D01.log`.
- JSON output: `output/F43-D01.json`.
- Intended disposition: exact finite discovery/certificate only. It cannot support an all-input probability or runtime assertion.
- Sage version: SageMath 10.9, Release Date 2026-05-04.
- Source SHA-256 for both attempts: `c9fb4b13c108f33b3697c685bb65084fad09cfba57f0bf2032bef0ae11f6dfaf`.
- Runner SHA-256 for both attempts: `6dd64c20d583848abbbe7fcb625cfd94a1989433167fac08e1bc6bf76cb1e2dd`.

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
- Disposition: all in-memory enumeration completed, but `json.dump` rejected a Sage `Integer` inside a carry sequence. The JSON is truncated and invalid, and supports no finite claim. The exact log is preserved both at the declared canonical path and at `logs/F43-D01-attempt2.log`; the partial output is preserved at both the canonical output path and `output/F43-D01-attempt2-partial.json` until any explicitly authorized correction.
- Log SHA-256: `7ce024fb4d5072e7dd129a021923a16f607acc97e083973995ac7d8c5d06bef2`.
- Partial-output SHA-256: `7a2c7e1df11985ae624a4806a2639c900b5440b5920a759c88115fb880945775`.
- Evidence: `logs/F43-D01.log`, `logs/F43-D01-attempt2.log`, `output/F43-D01.json`, and `output/F43-D01-attempt2-partial.json`.

No source amendment or third attempt has been made. The requested workflow explicitly required stopping and reporting after failure rather than silently substituting or repairing it.
