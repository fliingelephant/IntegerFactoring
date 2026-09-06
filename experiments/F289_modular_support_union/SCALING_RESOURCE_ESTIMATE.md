# F289 affine-patch scaling resource estimate

This continuation uses one Python process, a 30-second hard source alarm, a
26-second global soft budget, and a 128 MB measured-RSS cap.

Before the run, the 16 GB host reported load averages 2.18, 2.29, and 2.22,
73% free memory, no swap activity, and no active numerical job.

Each hierarchy node calls the exact one-patch oracle from
F288/PATCH_SUPPORT.py. No target leaves are materialized. A query stops with
the status budget_exhausted if it reaches 100,000 queried nodes or 2.5
seconds between completed node expansions. This state retains its incumbent,
live lower bound, early-factor event, and any certified 1.01-relative result.

Balanced labelled semiprimes increase from factor scale \(2^8\) toward
\(2^{60}\). Before each new input, the driver checks the global time and
measured peak RSS. The modulus is the largest power of two at most \(N/8\).
The first input also runs the streaming exact full-union baseline.
