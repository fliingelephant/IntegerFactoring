# Fair-branch finite-check resources

This is separate root-owned side work, not part of the frozen biased-source
trial table. Run the named source with --max-n 51 --label pilot, then with
--max-n 301 --label scale only after a successful pilot.

Estimated scale cost: under 10 seconds and 128 MiB, one process. Each job
has a 28-second internal alarm, a 30-second external subprocess timeout,
and a 512 MiB peak-RSS guard checked after each modulus. This guard is a
measurement stop, not an operating-system hard allocation limit.

Preflight at 2026-09-07 10:11 UTC: load 2.08/1.97/1.89; memory_pressure
reported 60 percent system-wide free; swap was zero. The top CPU process
list showed no numerical worker. Process and swap inspection required
read-only sandbox escalation; both completed. The other Sol scale worker
was asked to use one process, leaving one slot for this small check. The
second Sol was told not to launch a third CPU job during this overlap.

The source retains exact rational probabilities, per-input operation means,
counterexamples to minimum-branch reachability, source hashes, logs, and
terminal status. Exhaustive state evaluation and input selection are
validation work; they are not charged as a proposed public sampler.
