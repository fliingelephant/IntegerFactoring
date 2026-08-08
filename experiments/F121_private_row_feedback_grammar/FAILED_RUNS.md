# F121 preserved computation failures

## 2026-08-08T06:03:12.851782Z

- Command: `python3 experiments/F121_private_row_feedback_grammar/run_with_timeout.py`
- Outcome: exit status 1 after 0.099234 seconds; no timeout.
- Preserved output: `FAILED_20260808T060312.851782Z_OUTPUT.json`
- Preserved log: `FAILED_20260808T060312.851782Z_RUN.log`
- Output SHA-256: `eea7c71fe1d0bfa10557b38400e0e47da43e9a7d071d285149d0a1288ae7b2c0`
- Log SHA-256: `185e2ab6b11d91e1779e467392ec808bfb1d2b8a9cdc35e6690ed1425026f8ad`
- Failed check: `c110_terminal_gcds_are_proper`.
- Cause: the witness report evaluated `gcd(c-w, N)` and `gcd(c+w, N)` for
  the originating pair `(c,w)=(110,110)`. ROOT termination instead evaluates
  `gcd(r-1,N)` and `gcd(r+1,N)` for the recovered exact square root
  `r=sqrt(P)=110`.
- Scope: reporting/check logic only. The generated source, matrices, kernels,
  feedback candidates, and exact-column deduplication completed successfully.
- Correction: compute the terminal gcds from `isqrt(P)`. Preserve this run and
  preregister the corrected source before a second run.
