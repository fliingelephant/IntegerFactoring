# F329 resource plan

Status: pre-run estimate.

## Scope and bounds

The experiment compares rank-L reflection, uniform-center reflection, and a
lazy uniform auxiliary matching. Every sampled arithmetic trajectory supplies
paired baseline-screen and static-screen prefix results. No large rank graph or
complete auxiliary matching is constructed.

The pilot uses `N=209,1333,10807`, 16 accepted unit-square inputs per modulus,
four independent random centers or lazy matchings per square, and caps
`4,16,64,256`. If the pilot is safe, the retained F328 20-, 28-, and 36-bit
moduli use caps `16,64,256,1024`. Scaling jobs will be split by modulus and, if
needed, by query range.

- Each process is single-threaded.
- Each process has a 28-second internal alarm and a 30-second GNU `timeout`.
- Peak RSS is checked against 512 MiB after every query.
- A trajectory stores one current rank, a constant number of prefix snapshots,
  and, only for the lazy method, two sparse pool dictionaries with `O(cap)`
  entries. At cap 1,024 this is estimated below 2 MiB of experiment state.
- The generic exact control enumerates all singleton starts and all auxiliary
  matchings only for odd `d<=9`. Small arithmetic reflection controls use
  `N=15,21,35` and enumerate centers, not matchings. Estimated control runtime
  is below 3 seconds and peak RSS below 128 MiB.
- A full pilot modulus has at most `16*(1+4+4)*256 = 36,864` F calls. Estimated
  runtime is below 8 seconds and peak RSS below 128 MiB.
- A full scale modulus has at most 147,456 F calls. The first scale calibration
  will decide whether to retain one 16-query job or use fresh 8-query batches.

Offline factors are labels for exact controls and output verification. The
inner solver receives only `N`, `a`, method, cap, and an independent matching
seed. Hidden roots remain in the outer driver and are used only after a valid
root output.

## Preflight

At 2026-09-07 15:30 +0800, load averages were `2.35,2.20,1.87`, system-wide
free memory was 60 percent, no pages were throttled, and the boot counters had
zero swap-ins and swap-outs. The process table showed transient UI activity but
no experiment worker. Source construction and exact controls will remain
single-threaded; scaling will start only after the small control and pilot.

## Actual runs

The exact-control process passed in 0.161 seconds at 31,653,888 bytes peak RSS.
It enumerated 15,325 generic matching paths and checked 40,319 sparse-pool
active-set states.

| Scope | Jobs | Inputs per job | Process seconds per job | Largest peak RSS |
|---|---:|---:|---:|---:|
| Pilot | 3 | 16 | 0.133--0.219 | 72,318,976 bytes |
| 20-bit scale | 4 | 8 | 0.868--1.091 | 35,749,888 bytes |
| 28-bit scale | 4 | 8 | 4.032--4.868 | 35,651,584 bytes |
| 36-bit scale | 4 | 8 | 8.939--9.497 | 35,520,512 bytes |

The 12 scale jobs used 59.072 seconds in total. The pilot aggregation used
1.082 seconds and peaked at 50,364,416 bytes. The scale aggregation used 0.070
seconds and peaked at 59,490,304 bytes. Every process passed its status check,
remained below both time limits and the memory limit, and retained every
censored prefix. No local resource anomaly occurred.

An initial completed run was discarded and rerun from the same seeds after a
cost audit found that root-decoding wall time had been measured separately in
each cap view. The corrected implementation caches one outer root decode per
trajectory, so costs remain constant after absorption. All retained outputs use
the corrected source hash recorded in their status files.
