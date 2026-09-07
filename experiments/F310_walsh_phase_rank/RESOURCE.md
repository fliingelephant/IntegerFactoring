# Resource plan

Preflight was recorded on 2026-09-07 before the run.

- Host memory: 16 GiB; system-reported free memory: 70 percent.
- Load averages: 2.22, 2.20, 2.11.
- One Apple system process occupied one core. No numerical process was active.
- Sage executable: `/usr/local/bin/sage`.
- Hard outer timeout: 30 seconds. Internal alarm: 28 seconds.
- RSS budget and watchdog threshold: 1 GiB.
- Concurrency: one Sage process and one in-process RSS watchdog thread.

The largest matrix is `256 x 256`, or 65,536 field entries. A raw 16-bit
array would take 128 KiB. Sage representation and elimination workspace are
conservatively estimated below 256 MiB, plus Sage startup, and below the
1 GiB cap.

Across all requested cases, matrix ranks require fewer than 77 million
field-elimination steps at the cubic dense bound. Regenerating a full-rank
minor determinant can at most double that estimate. Phase construction and
period checks use 693,504 modular inverse evaluations. The expected wall time
is below 30 seconds. Scaling proceeds only if the first six cases use less
than five seconds and less than 512 MiB peak RSS.
