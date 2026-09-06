# ROOT_GAUSS_WINDOW resource check

The validation uses one lightweight Python process followed by one Sage
process. Each source has an internal alarm of at most 30 seconds.

At 2026-09-07 03:57 local time, the 16 GB host reported load averages 1.82,
1.99, and 2.00, 72% free memory, and no swap activity. No numerical job was
active. One macOS suggestion service occupied approximately one CPU core.

The Python coefficient arrays have maximum length 8,192 and are discarded
after each case. Estimated runtime is below 20 seconds and peak memory below
100 MB. The Sage checks use cyclotomic fields of conductor at most 256.
Estimated runtime is below 30 seconds and peak memory below 600 MB.
