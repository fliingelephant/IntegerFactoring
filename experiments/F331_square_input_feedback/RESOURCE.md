# F331 resource control

**Family:** route:F31

The first run checks the controller interface, root pullback, and agreement
with the frozen F328 probe on tiny inputs. It then runs trials 0 and 1 on
modulus b20_i0 under all three policies. With at most 16 rounds, eight F
calls per probe, and four proposals per round, this is estimated below
three seconds and 128 MiB.

The F329 worker confirmed that its corrected numerical rerun had ended before
this pilot. A fresh preflight at approximately 15:57 on 2026-09-07 found
54 percent system-wide free memory, no throttled pages, and load averages
2.46, 2.61, 2.40. Runs are single-process. Every fresh process has an
internal 28-second alarm, external 30-second timeout, and 512 MiB peak-RSS
ceiling.

The full plan will use one modulus per fresh batch. Scaling will start only
after the two-trial pilot is reviewed. If a batch approaches its limit, its
trial interval will be split without deleting any attempt.

## Pilot result

The pilot passed in 0.023252 seconds with peak RSS 28,344,320 bytes.
All 2,720 root-pullback checks and four probe-agreement checks passed.
The six paired policy attempts retained one direct factor, one pulled-back
root decoding failure, and four round-cap censors. No attempt or cost was
discarded. Root review accepted this scope and authorized the full planned
scale in fresh sequential batches.

## Scale result

All eight modulus batches passed and retained 96 policy attempts each.
Their wall times ranged from 0.334 to 2.850 seconds; peak RSS ranged from
36,814,848 to 39,157,760 bytes. No process approached its timeout or memory
limit.

The sequential aggregation loaded one batch at a time. It verified all 768
attempts in 0.490 seconds with peak RSS 179,453,952 bytes. The larger peak
comes from parsing one detailed JSON batch plus the compact audit rows; it
remained below the 512 MiB limit. The aggregate retains all 702 round-cap
censors and 12 pulled-root decoding failures across policies.
