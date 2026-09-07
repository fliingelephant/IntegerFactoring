# F320 execution status

- Terminal: PASS. Mathematical claims remain author-derived and unpromoted.
- Source: `check.py`; log: `run.log`; exact output: `output.json`.
- Initial budget: 30 seconds, 512 MiB. Estimated pilot: under 5 seconds and
  32 MiB. Actual computation: 0.049 seconds. No scale-up was required.
- Resource preflight: load 2.22/2.19/2.19; vm_stat showed no swapins/swapouts,
  351751 inactive pages at 16 KiB (about 5.37 GiB), and 193840 compressor
  pages. Inactive pages are not assumed fully reclaimable. Process inspection initially
  hit the sandbox restriction; the same ps call was approved and retried.
  The leading CPU process was suggestd at 99.6%, about 135 MiB RSS; Codex
  was 15.3%, about 672 MiB RSS. Only this tiny sequential pilot was launched.
- Timeout: source-level SIGALRM at 30 seconds. Arrays have maximum length
  10403. The exhaustive bank loop has 9^4+15^4 cases and stores no case bank.
- Factors/divisors appear only in offline identity checking. Public proposal
  rules use N, uniform residues, gcd, and monic polynomial arithmetic.
- No shared catalog, ledger, skill, framework, or git changes by this worker.
