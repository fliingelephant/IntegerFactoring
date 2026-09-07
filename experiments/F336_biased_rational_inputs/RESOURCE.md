# F336 resource control

**Family:** route:F31

The 2026-09-07 preflight found 59 percent system-wide free memory, zero swap
I/O, and load averages near 2.5, 2.0, and 1.9. Process-list inspection was
restricted, but both F334 and F335 workers explicitly reported that their
bounded numerical jobs had ended before the F336 pilot began.

The source keeps one Python process and one thread. It enforces a 28-second
internal alarm, a 30-second external timeout, and a 512 MiB peak-RSS ceiling.
The planned scale uses 64 outer trials per job, or 896 policy attempts, so the
largest job has approximately the attempt count of a completed F334 batch.
Removing full traces from ordinary scale rows should keep each 92-bit batch
below 20 seconds and 200 MiB. Pilot measurements are recorded before any scale
job is launched; later batch sizes may be reduced if this estimate fails.

All runs use the frozen F328 modulus list. Offline factors only check modulus
metadata and label an already verified divisor. They never select a source
parameter, policy, trajectory, or stopping action.

The exact tiny check passed in 0.028 seconds at 33,226,752 bytes peak RSS.
The two-trial pilot passed in 0.015 seconds at 31,260,672 bytes peak RSS.
All 24 scale jobs passed. Their charged wall times sum to 11.991 seconds;
the slowest job took 1.350 seconds and the largest peak RSS was 37,355,520
bytes. The aggregate pass took 0.449 seconds and peaked at 254,050,304 bytes
while loading all compact rows. Every run stayed within its timeout and memory
ceiling. No local numerical process remains.
