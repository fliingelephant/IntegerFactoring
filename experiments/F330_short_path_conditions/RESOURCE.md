# F330 resource control

**Family:** route:F31

The initial pilot exhausts every odd N through 101, every unit a, and every
allowed t for the stated identity. It then reproduces three fixed paths of at
most 32 calls. The estimate is below three seconds and 128 MiB.

Before execution, the F329 worker confirmed that all of its local numerical
processes had ended. A fresh preflight at approximately 15:47 on 2026-09-07
found 55 percent system-wide free memory, no throttled pages, and load
averages 2.97, 2.47, 2.17. The single F330 process has an internal 28-second
alarm, an external 30-second timeout, and a 256 MiB peak-RSS ceiling.

The follow-on a=-1 experiment in DESIGN.md is outside this initial run and
will not start before the pilot is reported to the route owner.

## Initial pilot result

The process passed in 0.060839 seconds with peak RSS 28,065,792 bytes.
It checked 70,620 reciprocity identities and discrepancy bounds and
reproduced all three frozen endpoints at calls 7, 31, and 25. No timeout,
memory failure, censor, or discarded discrepancy occurred. Direct Q
prefixes and sorted inverse-image sets are validation work; the experiment
does not claim them as a faster unbounded evaluator.
